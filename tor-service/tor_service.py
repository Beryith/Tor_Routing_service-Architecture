# tor_service.py
from iptables_config import configure_iptables
from rotation_thread import start_rotation_thread
from utils import setup_logger
import time

def main():
    """
    Point d’entrée principal du service Tor Routing.
    - Configure iptables
    - Lance le thread de rotation d’identité
    - Maintient le service actif
    """
    logfile = setup_logger()
    print(f"Logs will be saved in: {logfile}")

    print("Configuring iptables...")
    configure_iptables()

    print("Starting Tor identity rotation thread...")
    start_rotation_thread()

    print("Tor Routing Service is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Service stopped.")

if __name__ == "__main__":
    main()
