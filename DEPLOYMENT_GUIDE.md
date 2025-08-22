# 🚀 Guide de Déploiement VPS - Bot Trading IV Spread

## 📋 Prérequis

- **VPS Ubuntu 20.04+** avec accès SSH
- **Clés API Alpaca** (Paper Trading ou Live)
- **Git** installé sur votre machine locale
- **Accès root** ou sudo sur le VPS

## 🔧 Étape 1: Préparation du VPS

### Connexion SSH
```bash
ssh root@votre-vps-ip
```

### Mise à jour du système
```bash
apt update && apt upgrade -y
```

## 📥 Étape 2: Déploiement Automatique

### Option A: Déploiement via script (Recommandé)
```bash
# Télécharger le script de déploiement
wget https://raw.githubusercontent.com/votre-username/IV_Spread/main/deploy.sh

# Rendre exécutable et lancer
chmod +x deploy.sh
./deploy.sh
```

### Option B: Déploiement manuel
```bash
# 1. Créer le répertoire
mkdir -p /opt/trading-bot
cd /opt/trading-bot

# 2. Cloner le projet
git clone https://github.com/votre-username/IV_Spread.git
cd IV_Spread

# 3. Installer Python 3.9+
sudo apt install python3.9 python3.9-venv python3.9-dev

# 4. Créer l'environnement virtuel
python3.9 -m venv venv
source venv/bin/activate

# 5. Installer les dépendances
pip install -r requirements.txt
```

## 🔐 Étape 3: Configuration des Clés API

### Créer le fichier .env
```bash
cd /opt/trading-bot/IV_Spread
cp env_template.txt .env
nano .env
```

### Modifier avec vos clés Alpaca
```env
ALPACA_API_KEY=votre_clé_api_ici
ALPACA_SECRET_KEY=votre_clé_secrète_ici
BASE_URL=https://paper-api.alpaca.markets
```

## 🚀 Étape 4: Démarrage du Bot

### Rendre les scripts exécutables
```bash
chmod +x start_bot.sh stop_bot.sh monitor_bot.sh
```

### Démarrer le bot
```bash
./start_bot.sh
```

### Vérifier le statut
```bash
./monitor_bot.sh
```

## 🔄 Étape 5: Configuration du Service Systemd

### Installer le service
```bash
sudo cp trading-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable trading-bot
sudo systemctl start trading-bot
```

### Commandes de gestion
```bash
# Démarrer
sudo systemctl start trading-bot

# Arrêter
sudo systemctl stop trading-bot

# Redémarrer
sudo systemctl restart trading-bot

# Statut
sudo systemctl status trading-bot

# Logs
sudo journalctl -u trading-bot -f
```

## 📊 Étape 6: Monitoring et Maintenance

### Vérifier les logs
```bash
# Logs en temps réel
tail -f /var/log/trading-bot.log

# Logs systemd
sudo journalctl -u trading-bot -f
```

### Monitoring des ressources
```bash
# Statut du bot
./monitor_bot.sh

# Utilisation système
htop
df -h
free -h
```

### Mise à jour du bot
```bash
cd /opt/trading-bot/IV_Spread
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart trading-bot
```

## 🛡️ Étape 7: Sécurité et Sauvegarde

### Firewall
```bash
# Installer ufw
sudo apt install ufw

# Configuration basique
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

### Sauvegarde automatique
```bash
# Créer un script de sauvegarde
cat > /opt/backup_bot.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/opt/backups"
DATE=$(date +%Y%m%d_%H%M%S)
tar -czf "$BACKUP_DIR/trading-bot_$DATE.tar.gz" /opt/trading-bot
find $BACKUP_DIR -name "trading-bot_*.tar.gz" -mtime +7 -delete
EOF

chmod +x /opt/backup_bot.sh

# Ajouter au cron (sauvegarde quotidienne)
echo "0 2 * * * /opt/backup_bot.sh" | crontab -
```

## 🔍 Dépannage

### Problèmes courants

#### 1. Bot ne démarre pas
```bash
# Vérifier les logs
tail -f /var/log/trading-bot.log

# Vérifier les permissions
ls -la /opt/trading-bot/IV_Spread/

# Vérifier l'environnement virtuel
source /opt/trading-bot/IV_Spread/venv/bin/activate
python --version
```

#### 2. Erreurs de dépendances
```bash
cd /opt/trading-bot/IV_Spread
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

#### 3. Problèmes de permissions
```bash
sudo chown -R $USER:$USER /opt/trading-bot
sudo chmod -R 755 /opt/trading-bot
```

## 📱 Accès à Distance

### Via SSH
```bash
ssh root@votre-vps-ip
cd /opt/trading-bot/IV_Spread
./monitor_bot.sh
```

### Via Web (Optionnel)
```bash
# Installer nginx pour une interface web
sudo apt install nginx
# Configurer selon vos besoins
```

## ✅ Checklist de Déploiement

- [ ] VPS configuré et mis à jour
- [ ] Bot déployé et testé
- [ ] Clés API configurées
- [ ] Service systemd installé
- [ ] Monitoring configuré
- [ ] Sauvegarde configurée
- [ ] Sécurité configurée
- [ ] Tests de redémarrage effectués

## 🆘 Support

En cas de problème :
1. Vérifiez les logs : `tail -f /var/log/trading-bot.log`
2. Vérifiez le statut : `./monitor_bot.sh`
3. Redémarrez le service : `sudo systemctl restart trading-bot`
4. Consultez la documentation Alpaca

---

**🎯 Votre bot est maintenant prêt pour le trading 24/7 sur votre VPS !**
