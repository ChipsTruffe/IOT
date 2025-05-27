import paho.mqtt.client as mqtt
import json
import time


# THINGSBOARD_TOKEN = "GreenHouseToken"
# THINGSBOARD_HOST = "mqtt.thingsboard.cloud"

THINGSBOARD_TOKEN = "greenhouse"
THINGSBOARD_HOST = "localhost"


class ThingsBoardClient:
    def __init__(self):
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(THINGSBOARD_TOKEN)
        
        # Configuration des callbacks
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message  # Callback pour les messages RPC
        
        print(f"Connexion à {THINGSBOARD_HOST}...")
        self.client.connect(THINGSBOARD_HOST, 1883, 60)
        # Démarrage de la boucle de maintien de la connexion
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc, reasonCode=None, properties=None):
        if rc == 0:
            print("Connecté à ThingsBoard avec succès!")
            # S'abonner au topic RPC lors de la connexion
            self.client.subscribe("v1/devices/me/rpc/request/+")
            print("Abonné au topic RPC")
        else:
            print(f"Échec de la connexion, code de retour: {rc}, raison: {reasonCode}")

    def on_message(self, client, userdata, msg):
        """Gestion des messages RPC reçus"""
        print("📩 Message reçu")
        print(f"Topic: {msg.topic}")
        print(f"Payload: {msg.payload}")

    def on_publish(self, client, userdata, mid, reasonCode, properties):
        print(f"Message publié avec succès (mid: {mid}, raison: {reasonCode})")

    def on_disconnect(self, client, userdata, disconnect_flags, rc, properties=None):
        print(f"Déconnecté du serveur (code: {rc}, flags: {disconnect_flags})")

    def publish(self, temp, hum):
        payload = json.dumps({
            "temperature": temp,
            "humidity": hum
        })
        print(f"Publication des données: {payload}")
        result = self.client.publish('v1/devices/me/telemetry', payload)
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"Erreur lors de la publication: {result.rc}")
        return result

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()

# Test de la connexion et publication


# Boucle principale pour maintenir le programme en vie
if __name__ == "__main__":
    client = ThingsBoardClient()
    print("Client démarré, en attente de messages RPC...")
    try:
        while True:
            # Publication périodique des données
            client.publish(22, 50)
            time.sleep(10)  # Attendre 10 secondes entre chaque publication
    except KeyboardInterrupt:
        print("\nArrêt du client...")
