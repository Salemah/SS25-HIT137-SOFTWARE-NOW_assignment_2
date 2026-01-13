# Solution Q2

import os
import csv
import math
# Here we have declared the months according to the questions
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}


def analyze_temp_data_folder(base_dir, folder_name="temperatures"):
    """
    Reads all CSVs in the specified folder and organizes data.
    """
    station_all_temps = {}  
    seasonal_collect = {s: [] for s in SEASONS} 

    # We are looking for the temperature folder on the base folder where the script is
    folder_path = os.path.join(base_dir, folder_name)

    # folder path if not found
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_name}' not found at {folder_path}")
        return None, None

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            
            with open(filepath, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row.get('STATION_NAME')
                    if not name: continue
                    
                    if name not in station_all_temps:
                        station_all_temps[name] = []

                    # Ignoring missing temperatures
                    for season_name, months in SEASONS.items():
                        for m_name in months:
                            raw_val = row.get(m_name)
                            if raw_val and raw_val.strip().upper() != "NAN" and raw_val.strip() != "":
                                try:
                                    temp = float(raw_val)
                                    station_all_temps[name].append(temp)
                                    seasonal_collect[season_name].append(temp)
                                except ValueError:
                                    continue 
                                    
    return station_all_temps, seasonal_collect


def find_each_season_average(base_dir, seasonal_data):
    file_path = os.path.join(base_dir, "average_temp.txt")
    with open(file_path, "w", encoding='utf-8') as f:
        for season, temps in seasonal_data.items():
            if temps:
                avg = sum(temps) / len(temps)
                f.write(f"{season}: {round(avg, 1)}°C\n")


def find_temperature_range(base_dir, station_data):
    max_range = -1.0
    winners = []
    details = {}

    for name, temps in station_data.items():
        if not temps: continue
        
        current_range = max(temps) - min(temps)
        if current_range > max_range:
            max_range = current_range
            winners = [name]
            details[name] = {'max': max(temps), 'min': min(temps)}
        elif math.isclose(current_range, max_range, rel_tol=1e-7):
            winners.append(name)
            details[name] = {'max': max(temps), 'min': min(temps)}

    file_path = os.path.join(base_dir, "largest_temp_range_station.txt")
    with open(file_path, "w", encoding='utf-8') as f:
        for name in winners:
            d = details[name]
            f.write(f"Station {name}: Range {round(max_range, 1)}°C (Max: {d['max']}°C, Min: {d['min']}°C)\n")
 
 
 
def find_temp_stability(base_dir, station_data):
    stability_metrics = {}
    for name, temps in station_data.items():
        if len(temps) < 2: continue
        mean = sum(temps) / len(temps)
        variance = sum((t - mean) ** 2 for t in temps) / len(temps)
        stability_metrics[name] = math.sqrt(variance)

    if not stability_metrics: return
    min_std = min(stability_metrics.values())
    max_std = max(stability_metrics.values())

    file_path = os.path.join(base_dir, "temperature_stability_stations.txt")
    with open(file_path, "w", encoding='utf-8') as f:
        for name, val in stability_metrics.items():
            if math.isclose(val, min_std, rel_tol=1e-7):
                f.write(f"Most Stable: Station {name}: StdDev {round(val, 1)}°C\n")
        for name, val in stability_metrics.items():
            if math.isclose(val, max_std, rel_tol=1e-7):
                f.write(f"Most Variable: Station {name}: StdDev {round(val, 1)}°C\n")



# main function to generate files
if __name__ == "__main__":
    # Get the folder of the script base folder
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # data processing
    stations, seasons = analyze_temp_data_folder(current_folder, "temperatures")

    # Sving Reports
    if stations:
        find_each_season_average(current_folder, seasons)
        find_temperature_range(current_folder, stations)
        find_temp_stability(current_folder, stations)
        print(f"Success! Files have been created")
    else:
        print("No data processed. Something Wrong !")