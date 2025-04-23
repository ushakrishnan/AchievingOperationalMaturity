#!/bin/bash
# Provision Open-Source VMs using KVM
sudo apt update && sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
sudo systemctl enable --now libvirtd
# Create a virtual machine (example)
sudo virt-install --name example-vm --vcpus 2 --memory 2048 --disk size=10 --os-variant ubuntu20.04 --network bridge=virbr0 --graphics none --console pty,target_type=serial