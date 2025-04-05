#!/bin/bash

# Récupérer la page du SPY
page=$(curl -s https://www.barchart.com/stocks/quotes/SPY/overview)

# Extraire le prix avec regex
price=$(echo "$page" | grep -oP '"lastPrice":\K[0-9.]+' | head -1)

# Timestamp actuel
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Vérifie que le prix n'est pas vide avant d'écrire
if [[ -n "$price" ]]; then
    echo "$timestamp,$price" >> spy_data.csv
    echo "$(date) - Prix SPY = $price" >> spy_cron_debug.log
else
    echo "$(date) - WARNING: Prix vide !" >> spy_cron_debug.log
fi
