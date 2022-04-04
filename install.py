#Importing the neccessary modules to tell between which distro and what os and shell you are using
import os
from os import environ
import distro
#Importing time and random as I always do
import time 
import random


def installv():
    #Installs Utils for vm's
    if 'Fedora Linux' in distr:
        os.system('sudo dnf -y install bridge-utils libvirt virt-install qemu-kvm')
        os.system('sudo dnf -y install libvirt-devel virt-top libguestfs-tools guestfs-tools')
        os.system('sudo systemctl start libvirtd')
        os.system('sudo systemctl enable libvirtd')
        os.system('sudo dnf -y install virt-manager')
        os.system('sudo dnf -y install virt-viewer')
    if '"like": "fedora"' in distr:
        os.system('sudo dnf -y install bridge-utils libvirt virt-install qemu-kvm')
        os.system('sudo dnf -y install libvirt-devel virt-top libguestfs-tools guestfs-tools')
        os.system('sudo systemctl start libvirtd')
        os.system('sudo systemctl enable libvirtd')
        os.system('sudo dnf -y install virt-manager')
        os.system('sudo dnf -y install virt-viewer')
    if 'Debian Linux' in distr:
        os.system('sudo apt update')
        os.system('sudo apt install qemu qemu-kvm qemu-system qemu-utils -y')
        os.system('sudo apt install libvirt-clients libvirt-daemon-system virtinst -y')
        os.system('sudo virsh net-start default')
        os.system('sudo virsh net-start default')
        os.system('sudo adduser "$username" libvirt')
        os.system('sudo systemctl enable --now libvirtd')
    if '"like": "debian"' in distr:
        os.system('sudo apt update')
        os.system('sudo apt install qemu qemu-kvm qemu-system qemu-utils -y')
        os.system('sudo apt install libvirt-clients libvirt-daemon-system virtinst -y')
        os.system('sudo virsh net-start default')
        os.system('sudo virsh net-start default')
        os.system('sudo adduser "$username" libvirt')
        os.system('sudo systemctl enable --now libvirtd')
        os.system('sudo apt install virt-viewer -y')
        os.system('sudo apt install git -y')
    if 'Ubuntu Linux' in distr:
        os.system('sudo apt update')
        os.system('sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y')
        os.system('sudo adduser "$username" libvirt')
        os.system('sudo systemctl enable --now libvirtd')
        os.system('sudo apt install virt-manager -y')
        os.system('sudo apt install virt-viewer -y')
        os.system('sudo apt install git -y')
    if '"like": "ubuntu"' in distr:
        os.system('sudo apt update')
        os.system('sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y')
        os.system('sudo adduser "$username" libvirt')
        os.system('sudo systemctl enable --now libvirtd')
        os.system('sudo apt install virt-manager -y')
        os.system('sudo apt install virt-viewer -y')
        os.system('sudo apt install git -y')
    if "Arch Linux" in distr: 
        os.system('sudo pacman -S virt-manager qemu vde2 ebtables dnsmasq bridge-utils openbsd-netcat')
        os.system('sudo systemctl enable libvirtd.service')
        os.system('sudo systemctl start libvirtd.service')
        os.system('sudo pacman -S vim')
        os.system('sudo pacman -S nano')
        #sudo nano /etc/libvirt/libvirtd.conf
        # make unix_sock_group = "libvirt"
        # make unix_sock_rw_perms = "0770"
        os.system('newgrp libvirt')
        os.system('sudo systemctl restart libvirtd.service')
        os.system('sudo modprobe -r kvm_intel')
        os.system('sudo modprobe kvm_intel nested=1')
        os.system('echo "options kvm-intel nested=1" | sudo tee /etc/modprobe.d/kvm-intel.conf')
        os.system('sudo pacman -S virt-viewer')
        os.system('sudo pacman -S git')
        print('To finish this on arch you must add to the lines unix_sock_group, unix_sock_rw_perms \n And change unix_sock_group to "libvirt" \n and change unix_sock_rw_perms to "0770')
        os.system('sudo nano /etc/libvirt/libvirt.conf')
    if '"like": "arch"' in distr:
        os.system('sudo pacman -S virt-manager qemu vde2 ebtables dnsmasq bridge-utils openbsd-netcat')
        os.system('sudo systemctl enable libvirtd.service')
        os.system('sudo systemctl start libvirtd.service')
        os.system('sudo pacman -S vim')
        os.system('sudo pacman -S nano')
        #sudo nano /etc/libvirt/libvirtd.conf
        # make unix_sock_group = "libvirt"
        # make unix_sock_rw_perms = "0770"
        os.system('newgrp libvirt')
        os.system('sudo systemctl restart libvirtd.service')
        os.system('sudo modprobe -r kvm_intel')
        os.system('sudo modprobe kvm_intel nested=1')
        os.system('echo "options kvm-intel nested=1" | sudo tee /etc/modprobe.d/kvm-intel.conf')
        os.system('sudo pacman -S virt-viewer')
        os.system('sudo pacman -S git')
        print('To finish this on arch you must add to the lines unix_sock_group, unix_sock_rw_perms \n And change unix_sock_group to "libvirt" \n and change unix_sock_rw_perms to "0770')
        os.system('sudo nano /etc/libvirt/libvirt.conf')
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