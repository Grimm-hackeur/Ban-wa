import smtplib
from email.mime.text import MIMEText
import os
import time

# ======== BANNIÈRE ======== #
def banner():
    os.system("clear")
    print(r"""
    ████╗ ███████╗██╗   ██╗██╗  ██╗██╗   ██╗███╗   ██╗██╗   ██╗
    ██╔══╝ ██╔════╝╚██╗ ██╔╝██║ ██╔╝╚██╗ ██╔╝████╗  ██║██║   ██║
    ████╗  █████╗   ╚████╔╝ █████╔╝  ╚████╔╝ ██╔██╗ ██║██║   ██║
    ██╔═╝  ██╔══╝    ╚██╔╝  ██╔═██╗   ╚██╔╝  ██║╚██╗██║██║   ██║
    █████╗ ███████╗   ██║   ██║  ██╗   ██║   ██║ ╚████║╚██████╔╝
    ╚════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ 

                   > Outil éducatif by GRIMM <
    """)

# ======== VÉRIFICATION PAR MOT DE PASSE ======== #
def check_password():
    print(">> ACCÈS SÉCURISÉ À NEXUS-V1")
    password = input("Entrez le mot de passe : ")
    if password != "NEXUSYAMA":
        print("Mot de passe incorrect !")
        exit()
    print("Accès autorisé. Bienvenue GRIMM.")
    time.sleep(1)

# ======== CONFIGURATION DES EMAILS ======== #
senders = [
    {
        'email': 'mails.pasavendrepourmoiseul@gmail.com',
        'app_password': 'Ksgeksvrksvrksjceosbepdvrj'
    },
    {
        'email': 'klivensjeanjacques@gmail.com',
        'app_password': 'ovqh hkke vets ogvj'
    }
]

receiver_email = 'Support@whatsapp.com'

# ======== MESSAGE PERSONNALISÉ ======== #
def get_message():
    number = input("Numéro à signaler : ")
    whatsapp_link = f"https://api.whatsapp.com/send?phone={number}"
    
    # >>>> MODIFIE ICI TON MESSAGE <<<<
    subject = "Demande d'intervention"
    body = f"""Bonjour,

Je vous contacte concernant le numéro suivant : {number}

Lien vers le profil : {whatsapp_link}

Merci d'enquêter.

Cordialement,
GRIMM.
"""
    return subject, body

# ======== ENVOI DU MESSAGE ======== #
def send_email(from_email, app_password, subject, body):
    try:
        msg = MIMEText(body)
        msg['From'] = from_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, receiver_email, msg.as_string())
        server.quit()
        print(f"[+] Message envoyé depuis {from_email}")
    except Exception as e:
        print(f"[!] Échec de l'envoi depuis {from_email} : {str(e)}")

# ======== MAIN ======== #
def main():
    banner()
    check_password()
    subject, body = get_message()

    print("\nEnvoi en cours...\n")
    for sender in senders:
        send_email(sender['email'], sender['app_password'], subject, body)
        time.sleep(1)

    print("\n[✓] Tous les messages ont été envoyés.")
    print("\n— Script terminé | Développé par GRIMM")

if __name__ == '__main__':
    main(
