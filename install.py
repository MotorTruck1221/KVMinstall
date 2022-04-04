#Importing the neccessary modules to tell between which distro and what os and shell you are using
import os
from os import environ
import distro
#Importing time and random as I always do
import time 
import random


def installv():
    #Installs Utils for vm's
    print('hi')
def all():
    #Does things that all distros need to do
    os.system('mkdir ~/.scripts')
    if 'Fedora Linux' in distr:
        os.system('sudo dnf -y update && sudo dnf -y install git wget')
    if '"like": "fedora"' in distr:
        os.system('sudo dnf -y update && sudo dnf -y install git wget')
    if 'Debian Linux' in distr:
        os.system('sudo apt update -y && sudo apt install -y wget git')
    if '"like": "debian"' in distr:
        os.system('sudo apt update -y && sudo apt install -y wget git')
    if 'Ubuntu Linux' in distr:
        os.system('sudo apt update -y && sudo apt install -y wget git')
    if '"like": "ubuntu"' in distr:
        os.system('sudo apt update -y && sudo apt install -y wget git')
    if "Arch Linux" in distr: 
        os.system('sudo pacman -Syy && sudo pacman -Syu && sudo pacman -S wget git')
    if '"like": "arch"' in distr:
        os.system('sudo pacman -Syy && sudo pacman -Syu && sudo pacman -S wget git')
    os.system('wget https://github.com/MotorTruck1221/KVMinstall/archive/refs/heads/master.zip -P ~/.scripts')
    os.system('unzip ~/.scripts/master.zip -d ~/.scripts')
    os.system('rm -rf ~/.scripts/master.zip')
    installv()

#Getting the Shell 
shellp = environ['SHELL']
#Getting what the distro is based off of
distr = str(os.system('distro -j | grep -a "like"'))
distrr = distro.name()
if "Fedora Linux" in distrr:
    distr = distrr
if "Arch Linux" in distrr:
    distr = distrr
if "Ubuntu Linux" in distrr:
    distr = distrr
if "Debian Linux" in distrr:
    distr = distrr
if os.name in ('nt', 'dos'):
    print("Sorry! This is only for GNU/Linux.")
    exit()

#Add aliases to the shells
def aliasbash():
    os.system('echo alias vmi='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_install.sh"'+"'"+'  >> ~/.bashrc')
    os.system('echo alias vmd='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_delete.sh"'+"'"+' >> ~/.bashrc')
    os.system('echo alias vms='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_start.sh"'+"'"+' >> ~/.bashrc')
    os.system('echo alias vmfs='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_force_stop.sh"'+"'"+' >> ~/.bashrc')
    os.system('echo alias vmv='+"'"+'"~/.scripts/KVMinstall-master/view/vm_view.sh"'+"'"+'>> ~/.bashrc')
    os.system('echo alias vmst='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_stop.sh"'+"'"+' >> ~/.bashrc')
    os.system('echo alias vml='+"'"+'"~/.scripts/KVMinstall-master/view/vm_list.sh"'+"'"+' >> ~/.bashrc')
    os.system('echo alias vmh='+"'"+'"~/.scripts/KVMinstall-master/list.sh"'+"'"+'>> ~/.bashrc')
    aliasfish()
    aliaszsh()
def aliasfish():
    os.system('echo alias vmi='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_install.sh"'+"'"+'  >> ~/.config/fish/config.fish')
    os.system('echo alias vmd='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_delete.sh"'+"'"+' >> ~/.config/fish/config.fish')
    os.system('echo alias vms='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_start.sh"'+"'"+' >> ~/.config/fish/config.fish')
    os.system('echo alias vmfs='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_force_stop.sh"'+"'"+' >> ~/.config/fish/config.fish')
    os.system('echo alias vmv='+"'"+'"~/.scripts/KVMinstall-master/view/vm_view.sh"'+"'"+'>> ~/.config/fish/config.fish')
    os.system('echo alias vmst='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_stop.sh"'+"'"+' >> ~/.config/fish/config.fish')
    os.system('echo alias vml='+"'"+'"~/.scripts/KVMinstall-master/view/vm_list.sh"'+"'"+' >> ~/.config/fish/config.fish')
    os.system('echo alias vmh='+"'"+'"~/.scripts/KVMinstall-master/list.sh"'+"'"+'>> ~/.config/fish/config.fish')
    aliasbash()
    aliasfish()
def aliaszsh():
    os.system('echo alias vmi='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_install.sh"'+"'"+'  >> ~/.zshrc')
    os.system('echo alias vmd='+"'"+'"~/.scripts/KVMinstall-master/install_and_delete/vm_delete.sh"'+"'"+' >> ~/.zshrc')
    os.system('echo alias vms='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_start.sh"'+"'"+' >> ~/.zshrc')
    os.system('echo alias vmfs='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_force_stop.sh"'+"'"+' >> ~/.zshrc')
    os.system('echo alias vmv='+"'"+'"~/.scripts/KVMinstall-master/view/vm_view.sh"'+"'"+'>> ~/.zshrc')
    os.system('echo alias vmst='+"'"+'"~/.scripts/KVMinstall-master/start_and_stop/vm_stop.sh"'+"'"+' >> ~/.zshrc')
    os.system('echo alias vml='+"'"+'"~/.scripts/KVMinstall-master/view/vm_list.sh"'+"'"+' >> ~/.zshrc')
    os.system('echo alias vmh='+"'"+'"~/.scripts/KVMinstall-master/list.sh"'+"'"+'>> ~/.zshrc')
    aliasbash()
    aliasfish()
#Taking the shell and running the neccesary code to add aliases
if '/bin/fish' in shellp:
    aliasfish()
if '/bin/zsh' in shellp:
    aliaszsh()
if '/bin/bash' in shellp:
    aliasbash()
all()