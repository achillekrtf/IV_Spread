#!/usr/bin/env python3
"""
Test script pour vérifier le scraping d'IV des options .25 delta
"""

import logging
from datetime import datetime
from config import *

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_option_data_retrieval():
    """Test direct de récupération des données d'options"""
    print("🔍 Test de récupération des données d'options .25 delta")
    print("=" * 60)
    
    symbol = "AAPL"
    current_price = 230.0  # Prix de test
    
    print(f"📊 Symbole: {symbol}")
    print(f"💰 Prix actuel: ${current_price}")
    
    try:
        # Import des fonctions depuis main.py
        import main
        
        # Test 1: Récupération des contrats d'options
        print("\n1️⃣ Test: Récupération des contrats d'options...")
        try:
            contracts = main.get_option_contracts(symbol)
            if contracts:
                print(f"   ✅ {len(contracts)} contrats trouvés")
                
                # Afficher quelques exemples
                for i, contract in enumerate(contracts[:3]):
                    print(f"   📋 Contrat {i+1}: {contract.symbol} - Strike: ${contract.strike_price}")
            else:
                print("   ⚠️  Aucun contrat trouvé")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
        
        # Test 2: Recherche d'options .25 delta
        print("\n2️⃣ Test: Recherche d'options .25 delta...")
        try:
            option_data = main.get_real_option_data(symbol, current_price)
            if option_data:
                print(f"   ✅ Call .25 delta trouvé: Strike ${option_data['call_strike']}")
                print(f"   ✅ Put .25 delta trouvé: Strike ${option_data['put_strike']}")
                print(f"   📞 Call IV: {option_data.get('call_iv', 'N/A')}")
                print(f"   📉 Put IV: {option_data.get('put_iv', 'N/A')}")
                
                if option_data.get('call_iv') and option_data.get('put_iv'):
                    spread = option_data['put_iv'] - option_data['call_iv']
                    print(f"   📊 IV Spread: {spread:.6f}")
            else:
                print("   ⚠️  Options .25 delta non trouvées")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
        
        # Test 3: Données de fallback si options réelles non disponibles
        print("\n3️⃣ Test: Test de fallback avec simulation...")
        if not option_data or not option_data.get('call_iv'):
            try:
                # Simulation d'IV pour test
                import numpy as np
                np.random.seed(42)
                vol = np.random.uniform(0.15, 0.35)
                call_iv = vol * 0.95
                put_iv = vol * 1.05
                spread = put_iv - call_iv
                
                print(f"   ✅ Données simulées générées:")
                print(f"   📞 Call IV simulé: {call_iv:.4f}")
                print(f"   📉 Put IV simulé: {put_iv:.4f}")
                print(f"   📊 Spread simulé: {spread:.6f}")
            except Exception as e:
                print(f"   ❌ Erreur: {e}")
        else:
            print("   ✅ Données réelles déjà obtenues, pas besoin de simulation")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'import: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 Test terminé")

if __name__ == "__main__":
    test_option_data_retrieval()
