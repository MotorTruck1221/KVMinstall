#!/bin/bash

virsh list

read -p "Please enter the name of the VM that you want to stop: " vm

virsh shutdown $vm
echo "Fetching list..."
sleep 5
virsh list