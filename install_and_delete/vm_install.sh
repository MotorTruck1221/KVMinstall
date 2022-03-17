#/bin/bash
read -p "Enter Name Of VM: " name
read -p "Enter amount of vcpus: " vcpus
read -p "Enter amount of ram: " ram
read -p "Enter full file path of iso file: " iso
read -p "Enter size of disk: " disk

virt-install --name=$name --vcpus $vcpus --memory=$ram --cdrom=$iso --disk size=$disk --boot uefi --osinfo detect=on,require=off