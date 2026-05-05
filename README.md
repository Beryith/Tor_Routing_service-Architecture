# 🛡️ Tor Routing Service – Python

A Python service that forces all TCP traffic through Tor and automatically rotates identity (exit IP) every 5 seconds using Tor’s control API. Designed for security labs and red team simulations.

---

## ✨ Features
- 🔄 **Automatic identity rotation** every 5 seconds (`SIGNAL NEWNYM`).  
- 🔒 **iptables reconfiguration** to redirect all TCP traffic through Tor’s TransPort (9040).  
- 🕵️ **OS‑safe exclusions** (local IP ranges excluded to avoid breaking system services).  
- 📊 **Logging** of actions and current Tor IP in timestamped files.  
- ✅ **Security best practices**: timeouts, input validation, TLS for sensitive data, exception handling.  

---

## 📂 Project Structure
```
tor_service/
│── torrc                # Tor configuration file
│── iptables_config.py   # iptables rules for TCP redirection
│── tor_controller.py    # Tor control API (SIGNAL NEWNYM)
│── rotation_thread.py   # Identity rotation thread
│── utils.py             # Logging and validation utilities
│── tor_service.py       # Main entry point
```

---

## 🛠️ Requirements
- **Linux** (Ubuntu/Kali recommended)  
- **Tor** installed and running (`sudo apt install tor`)  
- Python 3.x  
- Libraries:  
  ```bash
  pip install stem requests scapy cryptography paramiko impacket dpkt
  ```

---

## ⚙️ Setup

1. **Configure Tor**  
   Edit `/etc/tor/torrc` and add:  
   ```
   TransPort 9040
   ControlPort 9051
   CookieAuthentication 1
   ```
   Restart Tor:  
   ```bash
   sudo systemctl restart tor
   ```

2. **Clone the project**  
   ```bash
   git clone https://github.com/<your-username>/tor_service.git
   cd tor_service
   ```

3. **Run the service**  
   ```bash
   sudo python3 tor_service.py
   ```

---

## 🚀 Usage

- On startup, the service:  
  1. Configures iptables to redirect all TCP traffic through Tor.  
  2. Starts a background thread that sends `SIGNAL NEWNYM` every 5 seconds.  
  3. Logs the new Tor IP each time.  

- Logs are saved in a timestamped folder:  
  ```
  outputs/2026-05-05_15-09-00/tor_service.log
  ```

### Example log output
```
2026-05-05 15:09:01 - iptables configured successfully.
2026-05-05 15:09:06 - Tor identity renewed successfully.
2026-05-05 15:09:06 - New Tor IP: 185.220.101.45
```

---

## 🔒 Security Practices
- Timeout on every socket and request.  
- Input validation (size, type, format).  
- Proper closure of sockets (`try/finally`).  
- Logging only IPs and timestamps (no sensitive data).  
- Exception handling for `ConnectionRefusedError`, `TimeoutError`, `OSError`.  

---
