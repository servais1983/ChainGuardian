# Fonctions utilitaires pour ChainGuardian

import os
import json
from datetime import datetime

def ensure_directory(path):
    """S'assure qu'un répertoire existe, le crée si nécessaire."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def format_timestamp(timestamp):
    """Formate un timestamp en format lisible."""
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return timestamp

def save_json(data, filename):
    """Sauvegarde des données au format JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
def get_mitre_url(technique_id):
    """Retourne l'URL de la documentation MITRE pour une technique donnée."""
    return f"https://attack.mitre.org/techniques/{technique_id}/"