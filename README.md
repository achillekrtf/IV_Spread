# 🤖 Bot Trading IV Spread - Stratégie Sophistiquée

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

## 🎯 Description

Bot de trading automatisé utilisant une stratégie sophistiquée basée sur le **spread IV des options .25 delta**. Cette stratégie combine plusieurs indicateurs avancés pour générer des signaux de trading optimaux.

## ✨ Fonctionnalités

### 🔍 **Stratégie IV Spread Sophistiquée**
- **Options .25 delta** : Sélection automatique des options calls et puts
- **Moyennes mobiles** : Croisement MA courte (5) et longue (20)
- **Z-scores** : Court terme (20) et long terme (120)
- **Détection de peaks** : Identification des maxima locaux
- **Accélération du spread** : Capture des mouvements rapides
- **Sizing dynamique** : Position sizing basé sur le risque

### 🚀 **Trading Automatisé**
- **API Alpaca** : Intégration complète avec Alpaca Markets
- **Signaux en temps réel** : Génération automatique des signaux
- **Exécution automatique** : Ordres d'achat/vente automatiques
- **Gestion des positions** : Ouverture/fermeture automatique

### 📊 **Monitoring et Analytics**
- **Logs détaillés** : Suivi complet des opérations
- **Métriques de performance** : Sharpe ratio, volatilité, rendements
- **Statut en temps réel** : Monitoring des positions et du compte
- **Alertes automatiques** : Notifications des événements importants

## 🏗️ Architecture

```
IV_Spread/
├── main.py                 # Bot principal avec stratégie sophistiquée
├── config.py              # Configuration et gestion des variables d'environnement
├── deploy.sh              # Script de déploiement VPS
├── start_bot.sh           # Démarrage du bot
├── stop_bot.sh            # Arrêt sécurisé du bot
├── monitor_bot.sh         # Monitoring en temps réel
├── trading-bot.service    # Service systemd pour VPS
├── requirements.txt       # Dépendances Python
├── .env                   # Variables d'environnement (à créer)
├── env_template.txt       # Template des variables d'environnement
└── DEPLOYMENT_GUIDE.md    # Guide complet de déploiement
```

## 🚀 Installation

### Prérequis
- Python 3.9+
- Compte Alpaca Markets (Paper Trading ou Live)
- Clés API Alpaca

### Installation locale
```bash
# 1. Cloner le repository
git clone https://github.com/votre-username/IV_Spread.git
cd IV_Spread

# 2. Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp env_template.txt .env
# Modifier .env avec vos clés API Alpaca

# 5. Lancer le bot
python main.py
```

### Déploiement VPS
```bash
# Déploiement automatique
wget https://raw.githubusercontent.com/votre-username/IV_Spread/main/deploy.sh
chmod +x deploy.sh
./deploy.sh
```

## ⚙️ Configuration

### Variables d'environnement (.env)
```env
# Clés API Alpaca
ALPACA_API_KEY=votre_clé_api_ici
ALPACA_SECRET_KEY=votre_clé_secrète_ici
BASE_URL=https://paper-api.alpaca.markets

# Configuration du trading
SYMBOL=AAPL
TIMEFRAME=1Min
LOOKBACK=200
SHORT_WINDOW=5
LONG_WINDOW=20
RISK_LEVEL=0.02
```

### Paramètres de la stratégie
```python
# Paramètres ajustables dans main.py
SHORT_WINDOW = 5          # MA courte
LONG_WINDOW = 20          # MA longue
SHORT_Z = 20              # Z-score court terme
LONG_Z = 120              # Z-score long terme
RISK_MULTIPLIER = 5       # Multiplicateur de risque
Z_THRESH_SHORT = 1.0      # Seuil Z-score court
Z_THRESH_LONG = 0.5       # Seuil Z-score long
MA_TOLERANCE = 0.01       # Tolérance MA
ACCEL_THRESH = 0.001      # Seuil accélération
```

## 📊 Utilisation

### Démarrage du bot
```bash
# Mode local
python main.py

# Sur VPS
./start_bot.sh

# Via systemd
sudo systemctl start trading-bot
```

### Monitoring
```bash
# Statut du bot
./monitor_bot.sh

# Logs en temps réel
tail -f /var/log/trading-bot.log

# Statut systemd
sudo systemctl status trading-bot
```

### Arrêt du bot
```bash
# Arrêt sécurisé
./stop_bot.sh

# Via systemd
sudo systemctl stop trading-bot
```

## 🔧 Déploiement

### VPS Ubuntu/Debian
1. **Préparation** : Mise à jour du système
2. **Déploiement** : Script automatique `deploy.sh`
3. **Configuration** : Variables d'environnement
4. **Service** : Installation systemd pour persistance
5. **Monitoring** : Scripts de surveillance

### Docker (optionnel)
```dockerfile
# Dockerfile disponible sur demande
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 📈 Stratégie de Trading

### Logique des signaux
Le bot génère des signaux d'achat quand :
1. **MA courte ≥ MA longue** (tendance haussière)
2. **Z-score court > 1.0** (survente à court terme)
3. **Z-score long > 0.5** (survente à long terme)
4. **Accélération > 0.001** (mouvement rapide)
5. **Peak détecté** (maximum local)

### Sizing dynamique
- **Position size** = Signal × (Spread normalisé × Multiplicateur de risque)
- **Maximum** : 150% du capital
- **Gestion du risque** : 2% par trade

## 🛡️ Sécurité

- **Variables d'environnement** : Clés API sécurisées
- **Firewall** : Configuration UFW sur VPS
- **Permissions** : Accès restreint aux fichiers sensibles
- **Logs** : Audit complet des opérations
- **Sauvegarde** : Backup automatique quotidien

## 📊 Performance

### Métriques calculées
- **Rendement cumulé** : Performance totale de la stratégie
- **Volatilité annualisée** : Risque de la stratégie
- **Sharpe ratio** : Rendement ajusté au risque
- **Nombre de trades** : Fréquence des opérations

### Optimisation
- **Paramètres ajustables** : Seuils et fenêtres configurables
- **Backtesting** : Validation historique de la stratégie
- **A/B testing** : Comparaison de paramètres

## 🔍 Dépannage

### Problèmes courants
1. **Clés API invalides** : Vérifier .env
2. **Dépendances manquantes** : `pip install -r requirements.txt`
3. **Permissions** : Vérifier les droits d'accès
4. **Connexion API** : Vérifier la connectivité réseau

### Logs et debugging
```bash
# Logs détaillés
tail -f /var/log/trading-bot.log

# Statut du processus
./monitor_bot.sh

# Redémarrage
sudo systemctl restart trading-bot
```

## 🤝 Contribution

### Comment contribuer
1. Fork le repository
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Standards de code
- **PEP 8** : Style Python
- **Docstrings** : Documentation des fonctions
- **Tests** : Validation des fonctionnalités
- **Logs** : Traçabilité des opérations

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ⚠️ Avertissement

**Le trading automatisé comporte des risques financiers importants.**
- Testez toujours en mode Paper Trading avant le live
- Surveillez régulièrement les performances
- Ajustez les paramètres selon vos objectifs
- Ne tradez que ce que vous pouvez vous permettre de perdre

## 📞 Support

- **Issues** : [GitHub Issues](https://github.com/votre-username/IV_Spread/issues)
- **Documentation** : [Wiki](https://github.com/votre-username/IV_Spread/wiki)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/IV_Spread/discussions)

---

**🎯 Développé avec ❤️ pour le trading automatisé professionnel**

*N'oubliez pas : Le trading comporte des risques. Tradez responsablement.*
