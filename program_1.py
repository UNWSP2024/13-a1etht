# Programmer: Alethea Lo
# Date: 5/1/2025
# Title: Cities Database
import sqlite3

#Connecting to the SQLite database
conn = sqlite3.connect('cities.db')
cursor = conn.cursor()

#Gathering from CITIES
cursor.execute('SELECT * FROM cities')

#All rows
cities = cursor.fetchall()

#Display results
print(f"{'ID':<5} {'City Name':<20} {'Country':<20} {'Population':<15} {'Region':<15}")
print("="*70)

for city in cities:
    print(f"{city[0]:<5} {city[1]:<20} {city[2]:<20} {city[3]:<15} {city[4]:<15}")

#End of Program
conn.close()
