# ⛓ ChainGuardian – Corrélation multi-logs & Timeline d'attaque

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/MITRE_ATT&CK-Framework-red.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9IndoaXRlIiBkPSJNMTIgMTBhMiAyIDAgMCAxLTEuNDEgMS40MXYxLjU5YTQgNCAwIDAgMS00LTR2LS41YTIuNSAyLjUgMCAwIDEtMi41LTIuNWgyLjVhMiAyIDAgMCAxIDIgMmgyYTQgNCAwIDAgMSA0IDRhMiAyIDAgMCAxLTEgMS43M1ptLTEuNDEtNC40MXYtMi41QTguMzYgOC4zNiAwIDAgMCAxMiAxOS41MVYyMmgtMXYtMi41QTcuNTEgNy41MSAwIDAgMSA0LjVuMTRWMTBhMSAxIDAgMCAwLTEtMWgtLjVDMyA3LjI1IDMuNyA2IDExLjE5IDZoLjQxYTEgMSAwIDAgMC0xLjA1IDF2MUgxMWExIDEgMCAwIDAgMCAyWk0xOSA2aC0uVjVhMSAxIDAgMCAwLTEtMWgtLjVhMS4xIDEuMSAwIDAgMC0xLjE1LjlsLS4yMi0uMUEyLjUgMi41IDAgMCAwIDE0IDcuNWE0LjAzIDQuMDMgMCAwIDEgLjMxIDBhMS41IDEuNSAwIDAgMSAxLjIgMSIvPjwvc3ZnPg==" alt="MITRE ATT&CK Framework"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License: MIT"/>
</p>

<p align="center">
  <b>Visualisation chronologique des attaques à partir de logs hétérogènes</b><br>
  <sub>🔍 Corrélation multiformat | 🔔 Détection MITRE ATT&CK | 📊 Timeline interactive | 🧩 Multi-source</sub>
</p>

---

## 📋 Description

**ChainGuardian** est un outil CLI permettant de corréler des logs provenant de différentes sources, d'identifier les techniques d'attaque selon le framework MITRE ATT&CK, et de générer une timeline visuelle des événements suspects. Il aide les analystes SOC et les répondants d'incidents à reconstituer rapidement la chronologie d'une attaque.

> ⚠️ **Note** : Ce projet est en phase de développement initial. Les fonctionnalités de base sont opérationnelles, mais plusieurs améliorations sont prévues.

### 🔍 Fonctionnalités principales

- 📥 **Ingestion multi-format** de logs (JSON, CSV, texte brut)
- 🔄 **Corrélation des événements** provenant de sources diverses
- 🎯 **Détection des techniques ATT&CK** via des patterns
- ⏱️ **Construction d'une timeline chronologique**
- 🖥️ **Visualisation interactive HTML** des événements
- 🧰 **Simple et léger** - aucune dépendance lourde requise

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/servais1983/ChainGuardian.git
cd ChainGuardian

# Installer les dépendances (minimales pour l'instant)
chmod +x install.sh
./install.sh
```

## 🛠️ Utilisation

### Analyse de base avec des logs multiples

```bash
# Analyser des logs de formats différents
python3 chainguardian.py --logs logs/sysmon.json logs/cloudtrail.csv
```

### Formats de logs supportés

- **JSON** (un objet par ligne) : logs Sysmon, CloudTrail JSON, etc.
- **CSV** : exports CloudTrail, logs de connexion, etc.
- **Texte** (.log) : logs système, logs d'application, etc.

### Exemple de résultat

Un fichier HTML `timeline.html` est généré, contenant :

- Une timeline chronologique des événements suspects
- Des détails sur les techniques MITRE ATT&CK détectées
- Les extraits pertinents des logs source
- Des liens vers la documentation MITRE pour chaque technique identifiée

## 🏗️ Structure du projet

```
chainguardian/
├── core/                  # Modules principaux
│   ├── parser.py          # Parseur multi-formats (JSON, Syslog, CSV)
│   ├── matcher.py         # Match avec les patterns MITRE ATT&CK
│   ├── timeline.py        # Construction de la timeline chronologique
│   ├── visualizer.py      # Générateur HTML interactif
│   └── utils.py           # Fonctions générales
├── logs/                  # Exemples de logs pour démonstration
│   ├── sysmon.json        # Exemple de logs sysmon
│   └── cloudtrail.csv     # Exemple de logs CloudTrail
├── chainguardian.py       # CLI principale
├── requirements.txt       # Dépendances Python
├── install.sh             # Script d'installation
└── README.md              # Documentation
```

## 🔮 Roadmap

Voici les fonctionnalités prévues pour les versions futures :

- [ ] **Intégration STIX/TAXII** pour la collecte standardisée d'IoCs
- [ ] **Export vers MISP** pour le partage de menaces
- [ ] **Visualisation graphique avancée** avec D3.js ou Bokeh
- [ ] **Graphe de relations Neo4j** entre entités
- [ ] **Machine learning** pour la détection d'anomalies
- [ ] **API REST** pour intégration avec d'autres outils
- [ ] **Support Sigma** pour les règles de détection standards
- [ ] **Analyse de malware** statique et dynamique

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

1. **Développer des parseurs** pour d'autres formats de logs
2. **Ajouter des patterns** MITRE ATT&CK plus précis
3. **Améliorer la visualisation** avec des graphiques interactifs
4. **Documenter** des cas d'usage supplémentaires

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

<p align="center">
  <sub>🔐 Développé pour les SOC et les équipes d'investigation numérique</sub>
</p>
