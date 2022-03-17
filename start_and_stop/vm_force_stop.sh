#!/bin/bash

virsh list

read -p "Please enter the name of the VM that you want to forcefully stop: " vm

virsh destroy $vm

virsh list
