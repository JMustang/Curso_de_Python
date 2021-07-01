# Exemplo simples de como usar banco de dados no python
import sqlite3
conn = sqlite3.connect('C:/Users/junior/OneDrive/Documents/www/database/weather_stations.db')
cursor = conn.execute('select * from station_data')
rows = cursor.fetchall()
for row in rows:
    print(row)