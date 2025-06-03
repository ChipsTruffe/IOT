THINGSBOARD_TOKEN = "GreenHouseToken"
THINGSBOARD_HOST = "localhost"

CLIENT_ADDR = "127.0.0.1"
CLIENT_PORT = 5005

COMM_LINK = 'mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "GreenHouseToken" -m "{temperature:25, humidity}"'


DATASETPATH_MALOE = "/home/maloe/dev/SPEIT/IOT/projet/H_73_latest-2024-2025.csv"
DATASETPATH_THEO = ""
DATASETPATH_BAPTISTE = "./db.csv"

download_dataset = "https://www.data.gouv.fr/fr/datasets/r/7c18ae09-a2bb-49f5-9f0d-990bc8df78ef"