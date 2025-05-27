THINGSBOARD_TOKEN = "greenhouse"
THINGSBOARD_HOST = "localhost"

COMM_LINK = 'mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "GreenHouseToken" -m "{temperature:25, humidity:50}"'