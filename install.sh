#/bin/bash
echo Do not Worry about the errors it will run anyways
username=$(whoami)
# Debian
sudo apt update
sudo apt install qemu qemu-kvm qemu-system qemu-utils -y
sudo apt install libvirt-clients libvirt-daemon-system virtinst -y
sudo virsh net-start default
sudo virsh net-start default
sudo adduser "$username" libvirt
sudo systemctl enable --now libvirtd
#Ubuntu
sudo apt update 
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
sudo adduser "$username" libvirt
sudo systemctl enable --now libvirtd
sudo apt install virt-manager -y
#Debian and Ubuntu
sudo apt install virt-viewer -y
sudo apt install git -y

##Arch(Unstable)
#sudo pacman -S virt-manager qemu vde2 ebtables dnsmasq bridge-utils openbsd-netcat
#sudo systemctl enable libvirtd.service
#sudo systemctl start libvirtd.service
#sudo pacman -S vim
#sudo pacman -S nano
##sudo nano /etc/libvirt/libvirtd.conf
## unix_sock_group = "libvirt"
## unix_sock_rw_perms = "0770"
#newgrp libvirt
#sudo systemctl restart libvirtd.service
#sudo modprobe -r kvm_intel
#sudo modprobe kvm_intel nested=1
#echo "options kvm-intel nested=1" | sudo tee /etc/modprobe.d/kvm-intel.conf
#sudo pacman -S virt-viewer
#sudo pacman -S git
# I am currently working on the version for arch it does not work at the moment

#Fedora
sudo dnf -y install git
sudo dnf -y install bridge-utils libvirt virt-install qemu-kvm
sudo dnf -y install libvirt-devel virt-top libguestfs-tools guestfs-tools
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
sudo dnf -y install virt-manager
sudo dnf -y install virt-viewer
#ALL DISTROS
mkdir ~/.scripts
echo alias vmi="'~/scripts/vm/install_and_delete/vm_install.sh'"  >> ~/.bashrc
echo alias vmd="'~/scripts/vm/install_and_delete/vm_delete.sh'" >> ~/.bashrc
echo alias vms="'~/scripts/vm/start_and_stop/vm_start.sh'" >> ~/.bashrc
echo alias vmfs="'~/scripts/vm/start_and_stop/vm_force_stop.sh'" >> ~/.bashrc
echo alias vmv="'~/scripts/vm/view/vm_view.sh'" >> ~/.bashrc
echo alias vmst="'~/scripts/vm/start_and_stop/vm_stop.sh'" >> ~/.bashrc
echo alias vml="'~/scripts/vm/view/vm_list.sh'" >> ~/.bashrc
