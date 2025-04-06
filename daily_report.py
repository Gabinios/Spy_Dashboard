import pandas as pd
from datetime import datetime

df = pd.read_csv("spy_data.csv", names=["timestamp", "price"], parse_dates=["timestamp"])

# On Filtre les données du jour
today = pd.Timestamp.today().normalize()
df_today = df[df["timestamp"].dt.normalize() == today]

if df_today.empty:
    report = "❌ Aucun prix disponible pour aujourd'hui."
else:
    open_price = df_today.iloc[0]["price"]
    close_price = df_today.iloc[-1]["price"]
    high_price = df_today["price"].max()
    low_price = df_today["price"].min()
    volatility = df_today["price"].std()

    report = (
        f" Rapport du {today.date()}\n"
        f"🟢 Ouverture : {open_price:.2f}\n"
        f"🔴 Clôture  : {close_price:.2f}\n"
        f" Plus haut : {high_price:.2f}\n"
        f" Plus bas  : {low_price:.2f}\n"
        f"📊 Volatilité (écart-type) : {volatility:.2f}\n"
    )

# DailyReport
with open("daily_report.txt", "w") as f:
    f.write(report)
