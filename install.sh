#!/bin/bash
echo "[*] Installation ChainGuardian..."

sudo apt update
sudo apt install -y python3 python3-pip

echo "[✓] Prêt. Exécution exemple :"
echo "python3 chainguardian.py --logs logs/sysmon.json logs/cloudtrail.csv"