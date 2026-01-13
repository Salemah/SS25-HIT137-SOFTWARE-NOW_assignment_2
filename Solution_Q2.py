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

# testing