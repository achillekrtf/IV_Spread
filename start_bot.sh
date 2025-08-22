#!/bin/bash

# ========================================
# Script de démarrage du Bot Trading
# ========================================

BOT_DIR="/opt/trading-bot/IV_Spread"
LOG_FILE="/var/log/trading-bot.log"
PID_FILE="/var/run/trading-bot.pid"

# Fonction de log
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a $LOG_FILE
}

# Vérifier si le bot est déjà en cours d'exécution
if [ -f "$PID_FILE" ]; then
    PID=$(cat $PID_FILE)
    if ps -p $PID > /dev/null 2>&1; then
        log "⚠️  Le bot est déjà en cours d'exécution (PID: $PID)"
        exit 1
    else
        log "🧹 Suppression du PID obsolète"
        rm -f $PID_FILE
    fi
fi

# Aller dans le répertoire du bot
cd $BOT_DIR || {
    log "❌ Erreur: Impossible d'accéder au répertoire $BOT_DIR"
    exit 1
}

# Activer l'environnement virtuel
source venv/bin/activate || {
    log "❌ Erreur: Impossible d'activer l'environnement virtuel"
    exit 1
}

# Vérifier que le fichier .env existe
if [ ! -f ".env" ]; then
    log "❌ Erreur: Fichier .env manquant. Configurez d'abord vos clés API !"
    exit 1
fi

# Démarrer le bot en arrière-plan
log "🚀 Démarrage du bot de trading..."
nohup python main.py > /dev/null 2>&1 &
BOT_PID=$!

# Sauvegarder le PID
echo $BOT_PID > $PID_FILE

# Vérifier que le bot a démarré
sleep 2
if ps -p $BOT_PID > /dev/null 2>&1; then
    log "✅ Bot démarré avec succès (PID: $BOT_PID)"
    log "📊 Logs disponibles: tail -f $LOG_FILE"
    log "🛑 Pour arrêter: ./stop_bot.sh"
else
    log "❌ Erreur: Le bot n'a pas pu démarrer"
    rm -f $PID_FILE
    exit 1
fi
