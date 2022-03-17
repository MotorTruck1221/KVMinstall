#!/bin/bash

#list all virtual machines
virsh list --all

#Have user type in the correct vm that they want to delete
read -p "Enter the name of the VM in which you want to delete: " vm_name


#Find source file for vm
vm_qcow=`virsh dumpxml $vm_name | grep 'source file'`
vm_qcow=`virsh dumpxml --domain $vm_name | grep 'source file'`
#Format from the beginning to the equal sign of the output
vm_qcow1=`echo "$(echo "$vm_qcow" | cut -d '=' -f2);"`
#Format the end to delte all including the single quotation mark
vm_qcow2=` echo $vm_qcow1 | rev | cut -c5- | rev`
#Cut the one single quotation mark at the beginning
vm_qcow3=` echo $vm_qcow2 | cut -c 2-`

#shutdown Virtual machine if not shutdown before
virsh shutdown $vm_name
virsh shutdown --domain $vm_name
virsh destroy $vm_name
virsh destroy --domain $vm_name

#Delte snapshots
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
do
    virsh snapshot-delete --domain $vm_name --current
done
#Delete virtual machine
virsh undefine $vm_name 
virsh undefine --domain $vm_name 
#If it has nvram delete that way
virsh undefine $vm_name --nvram
virsh undefine --domain $vm_name --nvram
##Note: The --domain option is givien if virsh does not recognize the name
#
##delete file aswell
rm -rf $vm_qcow3
#Do not worry about the errors you are fine



