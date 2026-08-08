---
title: "Configuring {ibm-title} Secure Execution virtual machines on {ibm-z-title} and {ibm-linuxone-title}"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-ibm-secure-execution-vms-ibm-z
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-ibm-secure-execution-vms-ibm-z
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring {ibm-title} Secure Execution virtual machines on {ibm-z-title} and {ibm-linuxone-title}

[id="virt-configuring-ibm-secure-execution-vms-ibm-z"]
= Configuring {ibm-title} Secure Execution virtual machines on {ibm-z-title} and {ibm-linuxone-title}

[role="_abstract"]
You can configure {ibm-name} Secure Execution virtual machines (VMs) on {ibm-z-name} and {ibm-linuxone-name}.

{ibm-name} Secure Execution for Linux is a s390x security technology that is introduced with {ibm-name} z15 and {ibm-linuxone-name} III. It protects data of workloads that run in a KVM guest from being inspected or modified by the server environment.

Hardware administrators, KVM administrators, and KVM code cannot access data in an {ibm-name} Secure Execution guest VM.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-configuring-ibm-secure-execution-vms-ibm-z.adoc

[id="virt-enabling-vms-ibm-secure-execution-ibm-z_{context}"]
= Enabling VMs to run {ibm-title} Secure Execution on {ibm-z-title} and {ibm-linuxone-title}

[role="_abstract"]
To enable {ibm-name} Secure Execution virtual machines (VMs) on {ibm-z-name} and {ibm-linuxone-name} on the compute nodes of your cluster, you must ensure that you meet the prerequisites and complete the following steps.

.Prerequisites

* Your cluster has logical partition (LPAR) nodes running on {ibm-name} z15 or later, or {ibm-linuxone-name} III or later.
* You have {ibm-name} Secure Execution workloads available to run on the cluster.
* You have installed the {oc-first}.

.Procedure

. To run {ibm-name} Secure Execution VMs, you must add the `prot_virt=1` kernel parameter for each compute node. To enable all compute nodes, create a file named `secure-execution.yaml` that contains the following machine config manifest:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: secure-execution
  labels:
    machineconfiguration.openshift.io/role: worker
spec:
  kernelArguments:
    - prot_virt=1
----
+
where:
+
`prot_virt=1`:: Specifies that the ultravisor can store memory security information.

. Apply the changes by running the following command:
+
[source,terminal]
----
$ oc apply -f secure-execution.yaml
----
+
The Machine Config Operator (MCO) applies the changes and reboots the nodes in a controlled rollout.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-configuring-ibm-secure-execution-vms-ibm-z.adoc

[id="virt-launching-ibm-secure-execution-vm-ibm-z_{context}"]
= Launching an {ibm-title} Secure Execution VM on {ibm-z-title} and {ibm-linuxone-title}

[role="_abstract"]
Before launching an {ibm-name} Secure Execution VM on {ibm-z-name} and {ibm-linuxone-name}, you must add the `launchSecurity` parameter to the VM manifest. Otherwise, the VM does not start correctly because it does not have access to the devices.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-configuring-ibm-secure-execution-vms-ibm-z.adoc

[id="virt-launching-ibm-secure-execution-vm-using-cli-ibm-z_{context}"]
= Launching an {ibm-title} Secure Execution VM by using the CLI

[role="_abstract"]
You can launch an {ibm-name} Secure Execution VM on {ibm-z-name} and {ibm-linuxone-name} by using the command-line interface.

To launch {ibm-name} Secure Execution VMs, you must include the `launchSecurity` parameter to the `VirtualMachine` manifest. The rest of the VM manifest depends on your setup.

.Procedure

* Apply a `VirtualMachine` manifest similar to the following, to the cluster:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    kubevirt.io/vm: f41-se
  name: f41-se
spec:
  runStrategy: Always
  template:
    metadata:
      labels:
        kubevirt.io/vm: f41-se
    spec:
      domain:
        launchSecurity: {}
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootfs
        machine:
          type: ""
        resources:
          requests:
            memory: 4Gi
      terminationGracePeriodSeconds: 0
      volumes:
        - name: rootfs
          dataVolume:
            name: f41-se
----
+
where:

`spec.template.spec.domain.launchSecurity`:: Specifies to enable hardware-based memory encryption.
+
[NOTE]
====
Because the memory of the VM is protected, you cannot live migrate {ibm-name} Secure Execution VMs. The VMs can only be migrated offline.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-configuring-ibm-secure-execution-vms-ibm-z.adoc

[id="virt-launching-ibm-secure-execution-vm-using-common-instance-type-ibm-z_{context}"]
= Launching an {ibm-title} Secure Execution VM by using a common instance type

[role="_abstract"]
You can launch an {ibm-name} Secure Execution VM on {ibm-z-name} and {ibm-linuxone-name} by using a common instance type.

.Prerequisites

* You have followed the procedure described in "Creating a VM from an instance type by using the web console" and performed the required steps.

* You are using an {ibm-name} Secure Execution enabled VM image.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.

. Click the *Customize VirtualMachine* button.

. Click the *YAML* tab, and include the `launchSecurity: {}` parameter in the YAML.
+
[source,yaml]
----
spec:
  template:
    spec:
       domain:
         launchSecurity: {}
----

. Click *Save*.

. Click *Create VirtualMachine*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-configuring-ibm-secure-execution-vms-ibm-z.adoc

[id="virt-creating-bootable-encrypted-ibm-secure-execution-vm-image-ibm-z_{context}"]
= Creating a bootable and encrypted {ibm-title} Secure Execution VM image on {ibm-z-title} and {ibm-linuxone-title}

[role="_abstract"]
You can create a bootable and encrypted {ibm-title} Secure Execution VM image for {op-system-base-full} on {ibm-z-title} and {ibm-linuxone-title}.

.Prerequisites

* You are using an {ibm-name} Secure Execution enabled VM image.

.Procedure

. On a trusted instance, create the `install.ks` kickstart file in the `/var/lib/libvirt/image/` directory with the following content:
+
[source,terminal]
----
[trusted instance ~]
text
lang en_US.UTF-8
keyboard us
network --bootproto=dhcp
rootpw --plaintext <password>
timezone <>
firewall --enabled
selinux --enforcing
bootloader --location=mbr
reboot

# Wipe and partition the disk
clearpart --all --initlabel
zerombr

# /boot gets encrypted on post reboot
part /boot --fstype ext4 --size=512 --label=boot
# Root (/) is LUKS-encrypted
part / --fstype xfs --size=3000 --pbkdf=pbkdf2 --encrypted --passphrase <passphrase>
# SE (/se) Non Encrypted for encrypted boot image.
part /se --fstype xfs --size=512 --label=se
#Packages
%packages
@core
dracut
s390-tools
%end
----

. Create the VM with the {op-system-base} image by running the following command:
+
[source,terminal]
----
[trusted instance ~]$ qemu-img create -f qcow2 <path to qcow2 image> <size>G
----

. Run the `virt-install` command with the following parameters:
+
[source,terminal]
----
[trusted instance ~]virt-install
    --name <guest_vm_name> \
    --memory 4096 --vcpus 2 \
    --disk path=<path_to_qcow2_image>,format=qcow2,bus=virtio,cache=none \
    --location <path_to_os>  \
    --initrd-inject=<path_to_kickstart_file> \
    --extra-args="inst.ks=file:/<kickstart_file_name> console=ttyS0 \
    --inst.text inst.noninteractive" \
    --os-variant=<os_variant> \
    --launchSecurity type=s390-pv \
    --graphics none
----

. Run the `virsh start` command to access the system console.

. Run the `sudo -s` command to achieve root user privileges.

. Generate keyfiles for the root and the boot partition by running the following commands:
+
[source,terminal]
----
[secure guest ~]$ mkdir -p /etc/luks
----
+
[source,terminal]
----
[secure guest ~]$ chmod 700 /etc/luks
----
+
[source,terminal]
----
[secure guest ~]$ dd if=/dev/urandom of=/etc/luks/root_keyfile.bin bs=1024 count=4
----
+
[source,terminal]
----
[secure guest ~]$ dd if=/dev/urandom of=/etc/luks/boot_keyfile.bin bs=1024 count=4
----
+
[source,terminal]
----
[secure guest ~]$ cryptsetup luksAddkey <root_partition_device> /etc/luks/root_keyfile.bin --pbkdf pbkdf2
----

. Obtain the LUKS device name and UUID by running the following command:
+
[source,terminal]
----
$ lsblk -f
----

. Rename the existing fstab file to `/etc/fstab_bak`.

. Create new crypttab and fstab files similar to the following examples:
+
Crypttab example output:
+
[source,screen]
----
luks device name   UUID                                       KEYFILE 			      OPTIONS
root 		       UUID=9cb04587-a670-458a-97eb-52fc0f4008ae  /etc/luks/keyfile.bin   luks
----
+
Fstab example output:
+
[source,screen]
----
/dev/mapper/root /          xfs	  defaults 0 1
----

. Add the SE boot filesystem entry into the `/etc/fstab` file by running the following command:
+
[source,terminal]
----
[secure guest ~]$ grep ‘/se’ /etc/fstab_bak >> /etc/fstab
----

. Add entries to the `initramfs` by running the following commands:
+
[source,terminal]
----
[secure guest ~]$ cat > /etc/dracut.conf.d/10-lukskey.conf <<'EOF'
    install_items+=" /etc/luks/root_keyfile.bin /etc/luks/boot_keyfile.bin "
    EOF
----
+
[source,terminal]
----
[secure guest ~]$ dracut -f --regenerate-all
----

. Verify that the key files are present in `initramfs` by running the following command:
+
[source,terminal]
----
[secure guest ~]$ lsinitrd /boot/initramfs-$(uname-r) | grep -i luks
----

. LUKS Encrypt the `/boot` volume.

.. Change into the boot directory by running the following command:
+
[source,terminal]
----
[secure guest ~]$ cd /boot
----

.. Backup the existing boot volume content by running the following commands:
+
[source,terminal]
----
[secure guest /boot ~]$ tar -cf /root/boot_backup.tar
----
+
[source,terminal]
----
[secure guest /boot ~]$ cd
----
+
[source,terminal]
----
[secure guest ~]$ umount /boot
----

.. Encrypt the boot volume by running the following commands:
+
[source,terminal]
----
[secure guest ~]$ cryptsetup -q luksFormat <boot_partition> --key-file /etc/luks/boot_keyfile.bin
----
+
[source,terminal]
----
[secure guest ~]$ cryptsetup luksOpen <boot_partition> boot -–key-file /etc/luks/boot_keyfile.bin
----

.. Create the file system by running the following command:
+
[source,terminal]
----
[secure guest ~]$ mke2fs –t ext4 /dev/mapper/boot
----

.. Obtain the boot UUID by running the following command:
+
[source,terminal]
----
[secure guest ~]$ blkid –s UUID  -o value <boot_partition>
----

.. Add the boot partition with the key file to `/etc/crypttab` by running the following command:
+
[source,terminal]
----
[secure guest ~]$ echo “boot <UUID> /etc/luks/boot_keyfile.bin luks” >>  /etc/crypttab
----

.. Add the mount entry to the fstab file by running the following command:
+
[source,terminal]
----
[secure guest ~]$ echo “/dev/mapper/boot  /boot ext4 defaults 1 2” >> /etc/fstab
----

.. Mount the boot volume by running the following command:
+
[source,terminal]
----
[secure guest ~]$ mount /dev/mapper/boot /boot
----

.. Change into the boot directory by running the following command:
+
[source,terminal]
----
[secure guest ~]$ cd /boot
----

.. Restore the boot backup file by running the following command:
+
[source,terminal]
----
[secure guest /boot~]$ tar -xvf /root/boot_backup.tar
----

. Set up SSH key login for the local user and disable password login and root login.

. Security hardening the VM.

.. To disable login on consoles by disabling serial and virtual TTYs, run the following commands:
+
[source,terminal]
----
[secure guest ~]$ mkdir -p /etc/systemd/system/serial-getty@.service.d
----
+
[source,terminal]
----
[secure guest ~]$ echo -e "[Unit]\nConditionKernelCommandLine=allowlocallogin" | tee /etc/systemd/system/serial-getty@.service.d/disable.conf
----
+
[source,terminal]
----
[secure guest ~]$ mkdir -p /etc/systemd/system/autovt@.service.d
----
+
[source,terminal]
----
[secure guest ~]$ echo -e "[Unit]\nConditionKernelCommandLine=allowlocallogin" | tee /etc/systemd/system/autovt@.service.d/disable.conf
----

.. Disable debug, emergency, and rescue shells by running the following commands:
+
[source,terminal]
----
[secure guest ~]$ systemctl mask emergency.service
----
+
[source,terminal]
----
[secure guest ~]$ systemctl mask emergency.target
----
+
[source,terminal]
----
[secure guest ~]$ systemctl mask rescue.service
----
+
[source,terminal]
----
[secure guest ~]$ systemctl mask rescue.target
----

.. Disable the `virtio-rng` device by running the following command:
+
[source,terminal]
----
[secure guest ~]$ echo "blacklist virtio-rng" | tee /etc/modprobe.d/virtio-rng.conf
----

. Enable {ibm-title} Secure Execution for the guest.

.. Copy the current command line to a file by running the following command:
+
[source,terminal]
----
[secure guest ~]$ cat /proc/cmdline > parmfile
----

.. Append the following parameters to the `parmfile`:
+
[source,terminal]
----
loglevel=0 systemd.show_status=0 panic=0 crashkernel=196M swiotlb=262144
----

.. Generate the {ibm-title} SEL image on the `/se` partition by running the following command:
+
[source,terminal]
----
[secure guest ~]$ genprotimg -i <image> \
                             -r <ramdisk> \
                             -p <parmfile> \
                             -k </path/to/host-key-doc.crt> \
                             --cert <ibm_signkey>  \
                             -o /se/secure-linux.img

----
+
where:

`<image>`:: Specifies the original guest kernel image.
`<ramdisk>`:: Specifies the original initial RAM file system.
`<parmfile>`:: Specifies the file that contains the kernel parameters.
`</path/to/host-key-doc.crt>`:: Specifies the public host key document.
`<ibm_signkey>`:: Specifies the {ibm-z-name} signing-key certificate and the DigiCert intermediate certificate for the verification of the host key documents.

.. Update the boot configuration by running the following command:
+
[source,terminal]
----
[secure guest ~]$ zipl -i /se/secure-linux.img -t /se
----

.. Reboot the VM by running the following command:
+
[source,terminal]
----
[secure guest ~]$ reboot
----

.. Verify that the guest VM is secure by running the following command:
+
[source,terminal]
----
[secure guest ~]$ cat /sys/firmware/uv/prot_virt_guest
----
+
Example output:
+
[source,terminal]
----
1
----
+
The value of this attribute is 1 for Linux instances that detect their environment as consistent with that of a secure host. For other instances, the value is 0.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* What is IBM Secure Execution?
