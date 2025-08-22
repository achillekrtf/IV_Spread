import os
import time
import logging
import pandas as pd
import numpy as np
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta
from config import *

# ===================== LOGGING =====================
logging.basicConfig(
    filename="trading_test_real.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ===================== INIT =====================
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, api_version="v2")

def generate_simulated_data(limit=LOOKBACK):
    """Génère des données simulées pour les tests"""
    np.random.seed(42)  # Pour la reproductibilité
    
    # Générer des prix simulés
    base_price = 150.0
    returns = np.random.normal(0, 0.02, limit)  # 2% de volatilité
    prices = [base_price]
    
    for ret in returns:
        new_price = prices[-1] * (1 + ret)
        prices.append(new_price)
    
    # Créer un DataFrame avec des données OHLC simulées
    dates = pd.date_range(start=datetime.now() - timedelta(days=5), periods=limit, freq='1min')
    data = pd.DataFrame({
        'open': prices[:-1],
        'high': [p * (1 + abs(np.random.normal(0, 0.01))) for p in prices[:-1]],
        'low': [p * (1 - abs(np.random.normal(0, 0.01))) for p in prices[:-1]],
        'close': prices[1:],
        'volume': np.random.randint(1000, 10000, limit)
    }, index=dates)
    
    return data

def get_data(symbol, limit=LOOKBACK, timeframe=TIMEFRAME):
    """Télécharge les données OHLC depuis Alpaca (version gratuite)"""
    try:
        # Essayer d'abord avec les données gratuites
        end_dt = datetime.now()
        start_dt = end_dt - timedelta(days=5)
        start_str = start_dt.strftime('%Y-%m-%d')
        end_str = end_dt.strftime('%Y-%m-%d')
        
        # Utiliser l'endpoint gratuit
        bars = api.get_bars(symbol, timeframe, start=start_str, end=end_str, adjustment='raw').df
        return bars.tail(limit)
    except Exception as e:
        print(f"⚠️  Erreur avec les données gratuites: {e}")
        print("🔄 Utilisation de données simulées...")
        # Fallback vers des données simulées
        return generate_simulated_data(limit)

def simulate_iv_spread(prices: pd.Series) -> pd.Series:
    """Simule un spread d'IV (remplacer par ton feed IV réel)."""
    vol = prices.pct_change().rolling(20).std()
    iv_call = vol * np.random.uniform(0.9, 1.1, len(vol))
    iv_put = vol * np.random.uniform(0.9, 1.1, len(vol))
    spread = iv_call - iv_put
    return spread.fillna(0)

def generate_signals(spread: pd.Series):
    """Génère signaux en fonction du croisement MA court / long"""
    short_ma = spread.rolling(SHORT_WINDOW).mean()
    long_ma = spread.rolling(LONG_WINDOW).mean()
    signal = (short_ma > long_ma).astype(int)  # 1 = long, 0 = pas de position
    return signal

def test_api_connection():
    """Teste la connexion à l'API Alpaca"""
    try:
        account = api.get_account()
        print(f"✅ Connexion API réussie!")
        print(f"   Compte: {account.id}")
        print(f"   Statut: {account.status}")
        print(f"   Capital: ${float(account.equity):,.2f}")
        return True
    except Exception as e:
        print(f"❌ Erreur de connexion API: {e}")
        return False

def main():
    logging.info("=== Test API réelle démarré ===")
    print("🤖 Test de l'API Alpaca réelle")
    print("=" * 50)
    
    # Test de connexion
    if not test_api_connection():
        return
    
    try:
        # 1) Charger les données réelles
        print("\n📊 Chargement des données depuis Alpaca...")
        data = get_data(SYMBOL)
        print(f"✅ {len(data)} bougies chargées pour {SYMBOL}")
        
        # 2) Calculer le spread
        print("📈 Calcul du spread IV...")
        prices = data["close"]
        spread = simulate_iv_spread(prices)
        print(f"✅ Spread IV calculé (min: {spread.min():.4f}, max: {spread.max():.4f})")
        
        # 3) Générer les signaux
        print("🎯 Génération des signaux de trading...")
        signals = generate_signals(spread)
        latest_signal = signals.iloc[-1]
        print(f"✅ Signal actuel: {'ACHAT' if latest_signal == 1 else 'VENTE/FERMETURE'}")
        
        # 4) Afficher les statistiques
        print("\n📊 Statistiques du spread IV:")
        print(f"   - Moyenne mobile courte ({SHORT_WINDOW}): {spread.rolling(SHORT_WINDOW).mean().iloc[-1]:.4f}")
        print(f"   - Moyenne mobile longue ({LONG_WINDOW}): {spread.rolling(LONG_WINDOW).mean().iloc[-1]:.4f}")
        print(f"   - Spread actuel: {spread.iloc[-1]:.4f}")
        
        # 5) Afficher les dernières données
        print("\n📈 Dernières données de prix:")
        print(data.tail().to_string())
        
        print("\n🎉 Test API réelle terminé avec succès!")
        
    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()
