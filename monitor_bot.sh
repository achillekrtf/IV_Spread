#!/bin/bash

# ========================================
# Script de monitoring du Bot Trading
# ========================================

# Use current directory instead of hardcoded path
BOT_DIR="$(pwd)"
PID_FILE="$BOT_DIR/trading-bot.pid"
LOG_FILE="$BOT_DIR/trading-bot.log"

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Monitoring du Bot Trading IV Spread${NC}"
echo "=========================================="

# 1. Statut du processus
echo -e "\n${BLUE}📊 Statut du processus:${NC}"
if [ -f "$PID_FILE" ]; then
    PID=$(cat $PID_FILE)
    if ps -p $PID > /dev/null 2>&1; then
        echo -e "   ${GREEN}✅ Bot en cours d'exécution (PID: $PID)${NC}"
        
        # Informations sur le processus
        CPU=$(ps -p $PID -o %cpu --no-headers)
        MEM=$(ps -p $PID -o %mem --no-headers)
        UPTIME=$(ps -p $PID -o etime --no-headers)
        echo "   📈 CPU: ${CPU}% | Mémoire: ${MEM}% | Uptime: ${UPTIME}"
    else
        echo -e "   ${RED}❌ Bot arrêté (PID obsolète)${NC}"
    fi
else
    echo -e "   ${YELLOW}⚠️  Aucun bot en cours d'exécution${NC}"
fi

# 2. Utilisation des ressources système
echo -e "\n${BLUE}💻 Ressources système:${NC}"
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
MEM_USAGE=$(free | grep Mem | awk '{printf "%.1f", $3/$2 * 100.0}')
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | cut -d'%' -f1)

echo "   🖥️  CPU: ${CPU_USAGE}%"
echo "   💾 Mémoire: ${MEM_USAGE}%"
echo "   💿 Disque: ${DISK_USAGE}%"

# 3. Logs récents
echo -e "\n${BLUE}📝 Logs récents (dernières 10 lignes):${NC}"
if [ -f "$LOG_FILE" ]; then
    tail -10 "$LOG_FILE" | while read line; do
        echo "   $line"
    done
else
    echo "   ⚠️  Fichier de log non trouvé"
fi

# 4. Vérification des fichiers de configuration
echo -e "\n${BLUE}🔧 Configuration:${NC}"
if [ -f "$BOT_DIR/.env" ]; then
    echo -e "   ${GREEN}✅ Fichier .env présent${NC}"
else
    echo -e "   ${RED}❌ Fichier .env manquant${NC}"
fi

if [ -d "$BOT_DIR/venv" ]; then
    echo -e "   ${GREEN}✅ Environnement virtuel présent${NC}"
else
    echo -e "   ${RED}❌ Environnement virtuel manquant${NC}"
fi

# 5. Actions rapides
echo -e "\n${BLUE}🎯 Actions rapides:${NC}"
echo "   🚀 Démarrer: ./start_bot.sh"
echo "   🛑 Arrêter: ./stop_bot.sh"
echo "   🔄 Redémarrer: ./stop_bot.sh && ./start_bot.sh"
echo "   📊 Logs en temps réel: tail -f $LOG_FILE"
echo "   📁 Répertoire: $BOT_DIR"

echo -e "\n${GREEN}✅ Monitoring terminé${NC}"
