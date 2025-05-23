import pandas as pd
from datetime import datetime, timedelta

def import_filter_data(file, start_date, stop_date, place):
    data = pd.read_csv(file, delimiter=';')
    data = data[data["NUM_POSTE"] == place]
    data = data[["NUM_POSTE","AAAAMMJJHH","T","U"]]
    data.sort_values("AAAAMMJJHH",inplace=True)
    data = data[data["AAAAMMJJHH"]< stop_date]
    data = data[data["AAAAMMJJHH"]>= start_date]
    return data

data = import_filter_data("/home/maloe/dev/SPEIT/IOT/projet/H_73_latest-2024-2025.csv",2024110600,2024110612, 73329001)

def date_to_values(data : pd.DataFrame, date : int , keys : list):
    for key in keys:
        if not key in data.keys():
            raise(KeyError, "error : " + str(key) +" is not a valid key")
    row = data[data["AAAAMMJJHH"] == date]
    if row.shape[0] == 0 : 
        raise(ValueError, "error : date provided is not in range")
    return {key : float(row[key].iloc[0]) for key in keys}


def t_to_date(t: int, start_date: int): # t un nombre d'heures, start_date au format AAAAMMJJHH. Renvoie une date 


    start_date = datetime.strptime(str(start_date), "%Y%m%d%H")
    new_date = start_date + timedelta(hours=t)
    
    # Format back to YYYYMMDDHH
    return int(new_date.strftime("%Y%m%d%H"))

def t_to_values(data : pd.DataFrame, t : int, keys : list):
    date = t_to_date(t, int(data["AAAAMMJJHH"].iloc[0]))
    return date_to_values(data, date, keys)

print(t_to_values(data, 6, ["T"]))

    
