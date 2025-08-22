# Configuration pour le bot de trading IV Spread
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration Alpaca API
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY", "")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY", "")
BASE_URL = os.getenv("BASE_URL", "https://paper-api.alpaca.markets")

# Configuration du trading
SYMBOL = os.getenv("SYMBOL", "AAPL")
TIMEFRAME = os.getenv("TIMEFRAME", "1Min")
LOOKBACK = int(os.getenv("LOOKBACK", "200"))
SHORT_WINDOW = int(os.getenv("SHORT_WINDOW", "10"))
LONG_WINDOW = int(os.getenv("LONG_WINDOW", "50"))
RISK_LEVEL = float(os.getenv("RISK_LEVEL", "0.02"))

# Vérification des credentials
def check_credentials():
    """Vérifie si les credentials Alpaca sont configurés"""
    if not ALPACA_API_KEY or not ALPACA_SECRET_KEY:
        print("❌ Erreur: Credentials Alpaca non configurés!")
        print("   Veuillez créer un fichier .env avec vos clés API:")
        print("   ALPACA_API_KEY=votre_clé_api")
        print("   ALPACA_SECRET_KEY=votre_clé_secrète")
        print("\n   Ou définir les variables d'environnement:")
        print("   export ALPACA_API_KEY='votre_clé_api'")
        print("   export ALPACA_SECRET_KEY='votre_clé_secrète'")
        return False
    
    print("✅ Credentials Alpaca configurés")
    print(f"   API Key: {ALPACA_API_KEY[:8]}...")
    print(f"   Base URL: {BASE_URL}")
    return True

def show_config():
    """Affiche la configuration actuelle"""
    print("\n📋 Configuration actuelle:")
    print(f"   Symbole: {SYMBOL}")
    print(f"   Timeframe: {TIMEFRAME}")
    print(f"   Lookback: {LOOKBACK} bougies")
    print(f"   MA courte: {SHORT_WINDOW}")
    print(f"   MA longue: {LONG_WINDOW}")
    print(f"   Niveau de risque: {RISK_LEVEL*100}%")

if __name__ == "__main__":
    print("🔧 Vérification de la configuration...")
    if check_credentials():
        show_config()
    else:
        print("\n💡 Pour obtenir vos clés API Alpaca:")
        print("   1. Créez un compte sur https://app.alpaca.markets")
        print("   2. Allez dans Paper Trading > API Keys")
        print("   3. Copiez vos clés dans le fichier .env")
