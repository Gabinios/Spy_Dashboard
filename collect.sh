 #!/bin/bash

page=$(curl -s https://www.barchart.com/stocks/quotes/SPY/overview)
price=$(echo "$page" | grep -oP '"lastPrice":\K[0-9.]+' | head -1)
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

if [[ -n "$price" ]]; then
    echo "$timestamp,$price" >> /home/ubuntu/Spy_Dashboard/spy_data.csv
    echo "$(date) - Prix SPY = $price" >> /home/ubuntu/Spy_Dashboard/spy_cron_debug.log
else
    echo "$(date) - WARNING: Prix vide !" >> /home/ubuntu/Spy_Dashboard/spy_cron_debug.log
fi
