<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&center=true&vCenter=true&width=435&lines=NEXUS-V1+by+GRIMM;Outil+%F0%9F%94%91+%C3%A9ducatif+Termux+%2B+Python;Envoyeur+automatique+de+signalements" alt="Typing SVG" />
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

## Installation

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/Grimm-hackeur/NEXUS-V1.git
cd NEXUS-V1
bash run.s
