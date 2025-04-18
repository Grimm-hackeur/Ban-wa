<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&center=true&vCenter=true&width=435&lines=NEXUS-V1+by+GRIMM;Outil+%F0%9F%94%91+%C3%A9ducatif+Termux+%2B+Python;Envoyeur+automatique+de+secret" alt="Typing SVG" />
</p>

---

## NEXUS-V1

**NEXUS-V1** est un outil éducatif développé par **GRIMM**. Il permet d'envoyer automatiquement des messages (signalements ou autres) via email avec protection, intégration d'un lien WhatsApp cliquable, et configuration pro.

### Fonctionnalités

- Interface pro avec bannière animée
- Exécution depuis Termux
- Envoi de messages depuis plusieurs adresses Gmail
- Mot de passe d'accès : `NEXUSYAMA`
- Génération de lien direct : `https://api.whatsapp.com/send?phone=NUMÉRO`

---

## Installation & Exécution

Voici les étapes pour installer et exécuter **NEXUS-V1** via Termux :

```bash
# 1. Mettre à jour Termux
pkg update && pkg upgrade -y

# 2. Installer les dépendances nécessaires
pkg install git python -y
pip install requests

# 3. Cloner le dépôt GitHub
git clone https://github.com/Grimm-hackeur/Ban-wa.git
cd Ban-wa

# 4. Rendre le script exécutable
chmod +x run.sh

# 5. Lancer l'outil
bash run.sh
```

---

**Fonctionnalités** :
- Script éducatif développé par **GRIMM**
- Envoi automatique de messages (signaux ou autres) via email
- Génération de lien WhatsApp cliquable :
  `https://api.whatsapp.com/send?phone=NUMÉRO_ICI`
- Interface protégée
- Configuration personnalisée

---

**Développeur** : GRIMM  
**Licence** : MIT

