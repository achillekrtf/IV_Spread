#!/bin/bash

# ========================================
# Script d'arrêt du Bot Trading
# ========================================

PID_FILE="/var/run/trading-bot.pid"
LOG_FILE="/var/log/trading-bot.log"

# Fonction de log
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a $LOG_FILE
}

# Vérifier si le fichier PID existe
if [ ! -f "$PID_FILE" ]; then
    log "ℹ️  Aucun bot en cours d'exécution"
    exit 0
fi

# Lire le PID
PID=$(cat $PID_FILE)

# Vérifier si le processus existe
if ! ps -p $PID > /dev/null 2>&1; then
    log "🧹 Processus déjà terminé, suppression du PID"
    rm -f $PID_FILE
    exit 0
fi

# Arrêter le bot gracieusement
log "🛑 Arrêt du bot de trading (PID: $PID)..."
kill -TERM $PID

# Attendre l'arrêt gracieux
sleep 5

# Vérifier si le processus est toujours en cours
if ps -p $PID > /dev/null 2>&1; then
    log "⚠️  Arrêt gracieux échoué, arrêt forcé..."
    kill -KILL $PID
    sleep 2
fi

# Vérifier que le processus est arrêté
if ! ps -p $PID > /dev/null 2>&1; then
    log "✅ Bot arrêté avec succès"
    rm -f $PID_FILE
else
    log "❌ Erreur: Impossible d'arrêter le bot"
    exit 1
fi
