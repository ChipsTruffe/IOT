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
        
        # État des contrôles
        self.controls = {
            "window": False,
            "irrigation": False,
            "humidifier": False,
            "heater": False
        }
        
        # Configuration des callbacks
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        
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
        
        try:
            # Décodage du payload JSON
            payload = json.loads(msg.payload.decode())
            
            # Vérification si c'est une commande de contrôle
            if payload.get('method') == 'control':
                params = payload.get('params', {})
                # Mise à jour des états
                if 'window' in params:
                    self.controls['window'] = params['window']
                if 'irrigation' in params:
                    self.controls['irrigation'] = params['irrigation']
                if 'humidifier' in params:
                    self.controls['humidifier'] = params['humidifier']
                if 'heater' in params:
                    self.controls['heater'] = params['heater']
                
                print(f"État des contrôles mis à jour: {self.controls}")
                
                # Envoi d'une réponse de confirmation
                request_id = msg.topic.split('/')[-1]
                response = {"success": True, "controls": self.controls}
                response_topic = f"v1/devices/me/rpc/response/{request_id}"
                self.client.publish(response_topic, json.dumps(response))
                
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON: {e}")
        except Exception as e:
            print(f"Erreur lors du traitement du message: {e}")

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

    def get_controls_state(self):
        """Retourne l'état actuel des contrôles"""
        return self.controls.copy()

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()

if __name__ == "__main__":
    client = ThingsBoardClient()
    print("Client démarré, en attente de messages RPC...")

# Boucle principale pour maintenir le programme en vie
    try:
        while True:
            # Publication périodique des données et de l'état des contrôles
            telemetry = {
                "temperature": 22,
                "humidity": 50,
                **client.get_controls_state()  # Inclusion de l'état des contrôles dans la télémétrie
            }
            client.publish(telemetry["temperature"], telemetry["humidity"])
            print(f"État actuel des contrôles: {client.get_controls_state()}")
            time.sleep(10)  # Attendre 10 secondes entre chaque publication
    except KeyboardInterrupt:
        print("\nArrêt du client...")