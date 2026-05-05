# utils.py
import logging
from datetime import datetime
import os

def setup_logger():
    """
    Crée un fichier de log horodaté dans outputs/.
    """
    folder = datetime.now().strftime("outputs/%Y-%m-%d_%H-%M-%S")
    os.makedirs(folder, exist_ok=True)
    logfile = os.path.join(folder, "tor_service.log")
    logging.basicConfig(filename=logfile, level=logging.INFO, format="%(asctime)s - %(message)s")
    return logfile

def log_result(msg):
    """
    Log sécurisé (jamais de données sensibles).
    """
    logging.info(msg)
