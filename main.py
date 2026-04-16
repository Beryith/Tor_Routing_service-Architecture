import random
import time

# Simulation simple de chiffrement/déchiffrement
def encrypt(message, key):
    return "".join(chr((ord(c) + key) % 256) for c in message)

def decrypt(message, key):
    return "".join(chr((ord(c) - key) % 256) for c in message)

# Définition des relais avec leurs clés
relays = [
    {"name": "Relay A", "key": 5},
    {"name": "Relay B", "key": 12},
    {"name": "Relay C", "key": 20},
    {"name": "Relay D", "key": 7},
    {"name": "Relay E", "key": 15}
]

# Demander le message à l'utilisateur
message = input("Entrez le message que vous voulez envoyer via Tor: ")

# Construction d’un circuit aléatoire de 3 relais
circuit = random.sample(relays, 3)
print("\nCircuit choisi:", [r["name"] for r in circuit])
time.sleep(2)

# Étape 1 : Encapsulation en couches
print("\n--- Étape 1 : Encapsulation en couches (Onion) ---")
encrypted = message
for relay in reversed(circuit):  # du dernier au premier
    print(f"Encapsulation avec la clé de {relay['name']}...")
    encrypted = encrypt(encrypted, relay["key"])
    time.sleep(2)

print("\nMessage encapsulé (chiffré en plusieurs couches):", encrypted)
time.sleep(3)

# Étape 2 : Transmission et décapsulation
print("\n--- Étape 2 : Transmission et décapsulation ---")
decrypted = encrypted
for relay in circuit:  # du premier au dernier
    print(f"{relay['name']} enlève sa couche de chiffrement...")
    decrypted = decrypt(decrypted, relay["key"])
    time.sleep(2)

print("\nMessage final reçu au nœud de sortie:", decrypted)
