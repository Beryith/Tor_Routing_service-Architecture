# tor_controller.py
from stem import Signal
from stem.control import Controller
from utils import log_result

def renew_identity():
    """
    Envoie SIGNAL NEWNYM à Tor pour demander un nouveau circuit (nouvelle IP de sortie).
    """
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # CookieAuthentication
            controller.signal(Signal.NEWNYM)
            log_result("Tor identity renewed successfully.")
    except Exception as e:
        log_result(f"Error renewing Tor identity: {e}")
