#!/bin/bash

page=$(curl -s https://www.barchart.com/stocks/quotes/SPY/overview)

price=$(echo "$page" | grep -oP '"lastPrice":\K[0-9.]+' | head -1)

timestamp=$(date '+%Y-%m-%d %H:%M:%S')

echo "$timestamp,$price" >> /home/gabin/Scrap/spy_data.csv

echo "$(date) - Prix SPY = $price" >> /home/gabin/Scrap/spy_cron_debug.log
