"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [21.5, 22.0, 19.8, 23.1, 20.6, 18.9, 22.4]  # 7 daily temperatures
city_population = {
    "Riga": 632614,
    "Daugavpils": 83490,
    "Liepaja": 67800,
    "Jelgava": 56500,
    "Jurmala": 49500,
}

# TODO: Compute aggregates
average_temperature = (
    round(sum(temperatures) / len(temperatures), 2) if temperatures else 0.0
)
largest_city, largest_population = max(city_population.items(), key=lambda kv: kv[1])
smallest_city, smallest_population = min(city_population.items(), key=lambda kv: kv[1])
total_population = sum(city_population.values())

# TODO: Print results
print(f"Temperatures (week): {temperatures}")
print(f"Average temperature: {average_temperature} °C")
print(f"Largest city: {largest_city} — {largest_population:,} inhabitants")
print(f"Smallest city: {smallest_city} — {smallest_population:,} inhabitants")
print(f"Total population: {total_population:,} inhabitants")
