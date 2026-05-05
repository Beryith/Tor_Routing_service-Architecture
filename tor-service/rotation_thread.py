# rotation_thread.py
import threading
import time
import requests
from tor_controller import renew_identity
from utils import log_result

def get_current_ip():
    """
    Récupère l’IP publique actuelle via un service externe.
    """
    try:
        ip = requests.get("https://check.torproject.org/api/ip", timeout=5).json().get("IP")
        return ip
    except Exception:
        return "Unknown"

def rotation_loop():
    """
    Boucle qui renouvelle l’identité Tor toutes les 5 secondes et log l’IP publique.
    """
    while True:
        renew_identity()
        ip = get_current_ip()
        log_result(f"New Tor IP: {ip}")
        time.sleep(5)

def start_rotation_thread():
    """
    Démarre le thread de rotation.
    """
    thread = threading.Thread(target=rotation_loop, daemon=True)
    thread.start()
