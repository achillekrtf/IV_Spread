#!/bin/bash

# ========================================
# Script de déploiement du Bot Trading
# ========================================

echo "🚀 Déploiement du Bot Trading IV Spread sur VPS..."

# 1. Mise à jour du système
echo "📦 Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

# 2. Installation des dépendances système
echo "🔧 Installation des dépendances système..."
sudo apt install -y python3 python3-pip python3-venv git screen htop nginx

# 3. Installation de Python 3.9+ si nécessaire
if ! command -v python3.9 &> /dev/null; then
    echo "🐍 Installation de Python 3.9..."
    sudo apt install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt update
    sudo apt install -y python3.9 python3.9-venv python3.9-dev
fi

# 4. Création du répertoire de travail
echo "📁 Création du répertoire de travail..."
sudo mkdir -p /opt/trading-bot
sudo chown $USER:$USER /opt/trading-bot
cd /opt/trading-bot

# 5. Clonage du projet (si pas déjà fait)
if [ ! -d "IV_Spread" ]; then
    echo "📥 Clonage du projet..."
    git clone https://github.com/votre-username/IV_Spread.git
    cd IV_Spread
else
    echo "📁 Projet déjà présent, mise à jour..."
    cd IV_Spread
    git pull
fi

# 6. Création de l'environnement virtuel
echo "🐍 Création de l'environnement virtuel..."
python3.9 -m venv venv
source venv/bin/activate

# 7. Installation des dépendances Python
echo "📦 Installation des dépendances Python..."
pip install --upgrade pip
pip install -r requirements.txt

# 8. Configuration des variables d'environnement
echo "🔐 Configuration des variables d'environnement..."
if [ ! -f ".env" ]; then
    cp env_template.txt .env
    echo "⚠️  IMPORTANT: Modifiez le fichier .env avec vos clés API Alpaca !"
    echo "   nano .env"
fi

# 9. Test du bot
echo "🧪 Test du bot..."
python main.py --test

echo "✅ Déploiement terminé !"
echo "📝 Prochaines étapes:"
echo "   1. Modifiez le fichier .env avec vos clés API"
echo "   2. Testez le bot: python main.py --test"
echo "   3. Lancez en production: ./start_bot.sh"
