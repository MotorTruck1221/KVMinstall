
# KVM/Qemu auto installer

Welcome to the KVM/Qemu automatic installer here you can install all of the assets required to run KVM on GNU/Linux


## Prerequisites
- A Debian, Ubuntu or Arch Based Distro
- Access to SUDO permissions or the root account
- The Systemd init system(if you don't know what this is don't worry about it.)
## Installation

Run the auto installer
- Download the .sh script from the releases page and then type or copy and paste these commands

```bash
  cd Downloads
  chmod u+x install.sh
  ./install.sh
```
This will then install KVM on your computer simply enter your SUDO password

    
## Some Commands you can use

(Explanation Below the command)
```bash
vmi
```
- Installs the selected Image
```bash
vmd
```
- Deletes the selected image
```bash
vms
```
- Starts the selected VM
```bash
vmfs
```
- Force Stops the selected VM (Not recommended only use if your selected VM won't stop by using the normal stop command)
```bash
vmv
```
- Allows you to view the OS gui to the selected VM
```bash
vmst
```
- Stops the selected VM
```bash
vml
```
- Lists all VM's
```bash
vmh
``` 
- Shows help dialogue
## Thanks for using!