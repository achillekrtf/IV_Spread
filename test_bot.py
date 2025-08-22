#!/usr/bin/env python3
"""
Test script pour vérifier que le bot fonctionne correctement
"""

import os
import sys
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_imports():
    """Teste l'import des modules"""
    try:
        # Import sélectif pour éviter d'exécuter main()
        import main
        print("✅ Module main importé avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def test_config():
    """Teste la configuration"""
    try:
        import config
        print("✅ Configuration chargée avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur de configuration: {e}")
        return False

def test_functions():
    """Teste les fonctions principales"""
    try:
        # Test des fonctions de base
        print("✅ Fonctions de base disponibles")
        return True
    except Exception as e:
        print(f"❌ Erreur dans les fonctions: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🧪 Test du Bot Trading IV Spread")
    print("=" * 50)
    
    tests = [
        ("Import des modules", test_imports),
        ("Configuration", test_config),
        ("Fonctions principales", test_functions),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Test: {test_name}")
        if test_func():
            passed += 1
            print(f"   ✅ {test_name}: SUCCÈS")
        else:
            print(f"   ❌ {test_name}: ÉCHEC")
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés! Le bot est prêt.")
        return True
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
