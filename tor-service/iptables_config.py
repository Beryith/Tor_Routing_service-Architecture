import subprocess
from utils import log_result

def configure_iptables():
    """
    Configure iptables pour rediriger tout le trafic TCP sortant vers Tor (port 9040).
    Exclut les IP locales pour éviter de casser les services système.
    """
    try:
        rules = [
            ["iptables", "-t", "nat", "-A", "OUTPUT", "-p", "tcp", "--syn", "-m", "owner", "!", "--uid-owner", "debian-tor", "-j", "REDIRECT", "--to-ports", "9040"],
            ["iptables", "-t", "nat", "-A", "OUTPUT", "-d", "127.0.0.1/8", "-j", "RETURN"],
            ["iptables", "-t", "nat", "-A", "OUTPUT", "-d", "192.168.0.0/16", "-j", "RETURN"],
            ["iptables", "-t", "nat", "-A", "OUTPUT", "-d", "10.0.0.0/8", "-j", "RETURN"]
        ]
        for rule in rules:
            subprocess.run(rule, check=True)
        log_result("iptables configured successfully.")
    except subprocess.CalledProcessError as e:
        log_result(f"Error configuring iptables: {e}")
