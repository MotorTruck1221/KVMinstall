#!/bin/bash

virsh list --all
read -p "Enter the name of the vm that you would like to start: " start
virsh start $start
