#!/bin/bash

virsh list --all

read -p "Please enter the name of the Vm in which you would like to view: " vm

virt-viewer $vm