import pandas as pd
from datetime import datetime, timedelta
from math import *
def import_filter_data(file, start_date, stop_date, place):
    data = pd.read_csv(file, delimiter=';')
    data = data[data["NUM_POSTE"] == place]
    data = data[["NUM_POSTE","AAAAMMJJHH","T","U"]]
    data.sort_values("AAAAMMJJHH",inplace=True)
    data = data[data["AAAAMMJJHH"]< stop_date]
    data = data[data["AAAAMMJJHH"]>= start_date]
    return data

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

def s_to_values(data : pd.DataFrame, s : float, keys : list): # s un temps en secondes (flottant positif), retourne les valeurs par interpolation linéaire entre les deux observations les plus proches
    
    h = s / 3600
    date1 = t_to_date(floor(h), int(data["AAAAMMJJHH"].iloc[0]))
    date2 = t_to_date(floor(h)+1, int(data["AAAAMMJJHH"].iloc[0]))

    tau = h - floor(h)

    v1 = date_to_values(data, date1, keys)
    v2 = date_to_values(data, date2, keys)

    return {key : (1-tau)*v1[key] + tau*v2[key] for key in keys}

#print(s_to_values(data, 6, ["T"]))

    
