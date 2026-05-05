import random
import time
from colorama import Fore, Style, init

# Initialiser colorama
init()

# Simulation simple de chiffrement/déchiffrement
def encrypt(message, key):
    return "".join(chr((ord(c) + key) % 256) for c in message)

def decrypt(message, key):
    return "".join(chr((ord(c) - key) % 256) for c in message)

# Animation de progression
def animation(text, delay=0.5, steps=3):
    print(text, end="", flush=True)
    for _ in range(steps):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

# Définition des relais avec leurs clés
relays = [
    {"name": "Relay A", "key": 5},
    {"name": "Relay B", "key": 12},
    {"name": "Relay C", "key": 20},
    {"name": "Relay D", "key": 7},
    {"name": "Relay E", "key": 15}
]

# Demander le message à l'utilisateur
message = input(Fore.CYAN + "Entrez le message que vous voulez envoyer via Tor: " + Style.RESET_ALL)

# Construction d’un circuit aléatoire de 3 relais
circuit = random.sample(relays, 3)
print(Fore.YELLOW + "\nCircuit choisi:", [r["name"] for r in circuit], Style.RESET_ALL)
time.sleep(2)

# Étape 1 : Encapsulation en couches
print(Fore.GREEN + "\n--- Étape 1 : Encapsulation en couches (Onion) ---" + Style.RESET_ALL)
encrypted = message
for relay in reversed(circuit):  # du dernier au premier
    animation(Fore.BLUE + f"Encapsulation avec la clé de {relay['name']}" + Style.RESET_ALL)
    encrypted = encrypt(encrypted, relay["key"])
    time.sleep(1)

print(Fore.MAGENTA + "\nMessage encapsulé (chiffré en plusieurs couches):" + Style.RESET_ALL, encrypted)
time.sleep(3)

# Étape 2 : Transmission et décapsulation
print(Fore.GREEN + "\n--- Étape 2 : Transmission et décapsulation ---" + Style.RESET_ALL)
decrypted = encrypted
for relay in circuit:  # du premier au dernier
    animation(Fore.RED + f"{relay['name']} enlève sa couche de chiffrement" + Style.RESET_ALL)
    decrypted = decrypt(decrypted, relay["key"])
    time.sleep(1)

print(Fore.CYAN + "\nMessage final reçu au nœud de sortie:" + Style.RESET_ALL, decrypted)
