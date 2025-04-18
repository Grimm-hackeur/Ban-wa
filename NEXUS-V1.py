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
    subject = "criminal "
    body = f"""HI, I'M MARC, A CHILD PORNOGRAPHY ACTOR AND AN ORGAN TRAFFICKER.

HERE ARE SOME VIDEOS AND IMAGES OF WHAT I DO.

https://image.noelshack.com/fichiers/2025/15/1/1744035179-img-20250404-190355-761.jpg

https://ibb.co.com/2nMXfTY

https://www.mediafire.com/file/6p0ecl3po76kj3g/2025-04-07-132009683.mp4/file

ALL MY CLIENTS ARE SATISFIED WITH THE WORK I DO. I ALSO WORK WITH GREAT MEN WHO KEEP ME OUT OF PRISON. THIS WORK IS WITHOUT RISK IF YOU HAVE RELATIONSHIPS, AND I HAVE MANY RELATIONSHIPS ALL OVER THE WORLD, AND THE WORK IS WELL-PAID. YOU CAN MAKE MORE THAN 1 MILLION A WEEK.

IF YOU WANT TO WORK WITH ME, WRITE TO MY MAIN NUMBER. YOU WILL BE PAID 500,000 FRANCS TO START. SINCE IT'S A START, BUT IT'S UP TO YOU TO DECIDE IF YOU WANT TO BE AN ORGAN TRAFFICKER OR A CHILD PORNOGRAPHY ACTOR. HERE'S MY NUMBER. CONTACT ME.

https://api.whatsapp.com/send?phone= : {number}

Lien vers le profil : {whatsapp_link}
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
