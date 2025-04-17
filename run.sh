#!/bin/bash

clear
echo -e "\e[92m
███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗███████╗
████╗  ██║██╔════╝██║  ██║╚██╗ ██╔╝██╔════╝██╔════╝
██╔██╗ ██║█████╗  ███████║ ╚████╔╝ █████╗  ███████╗
██║╚██╗██║██╔══╝  ██╔══██║  ╚██╔╝  ██╔══╝  ╚════██║
██║ ╚████║███████╗██║  ██║   ██║   ███████╗███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝

            >>> TOOL ÉDUCATIF BY GRIMM <<<
"

echo -e "\e[93m[~] Mise à jour de Termux & installation des paquets requis..."
pkg update -y && pkg upgrade -y
pkg install python git -y

echo -e "\e[94m[~] Mise à jour de pip..."
pip install --upgrade pip

echo -e "\e[92m[✓] Lancement du script NEXUS-V1..."
sleep 2

python nexus-v1.p
