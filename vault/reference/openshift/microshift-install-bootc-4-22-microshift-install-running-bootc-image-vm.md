---
title: "Running the bootc image in a virtual machine"
type: reference
domain: openshift
slug: microshift-install-bootc-4-22-microshift-install-running-bootc-image-vm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_bootc/microshift-install-running-bootc-image-vm
version: 4.22
family: microshift_install_bootc
documentKind: "Documentation"
---

# Running the bootc image in a virtual machine

[id="microshift-install-running-bootc-image-in-vm"]
= Running the bootc image in a virtual machine

[role="_abstract"]
Use the bootable container image as an installation source to set up a {op-system-base-full} virtual machine.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-running-bootc-image-in-VM.adoc

[id="microshift-install-bootc-prepare-kickstart_{context}"]
= Creating the Kickstart file

[role="_abstract"]
You must create the Kickstart file to use during installation.

.Prerequisites

* You have root-user access.
* You are logged in to the physical hypervisor host.

.Procedure

. Set the `AUTH_CONFIG` environment variable to reference the secret file in the `kickstart.ks` file to authenticate private container registry access by running the following command:
+
[source,terminal]
----
$ AUTH_CONFIG=~/.quay-auth.json
----

. Set the `PULL_SECRET` environment variable to reference the secret files in the `kickstart.ks` file to authenticate the {OCP} registry access by running the following command:
+
[source,terminal]
----
$ PULL_SECRET=~/.pull-secret.json
----

. Set the `IMAGE_REF` environment variable to reference the image mode for your container image to use during installation by running the following command:
+
[source,terminal,subs="attributes+,quotes"]
----
$ IMAGE_REF="quay.io/_<myorg>/<mypath>_/microshift--bootc"
----
+
Replace _<myorg/<mypath>_ with your remote registry organization name and path.

. Create the `kickstart.ks` file to use during installation by running the following script:
+
[source,terminal]
----
$ cat > kickstart.ks <<EOFKS
lang en_US.UTF-8
keyboard us
timezone UTC
text
reboot

# Partition the disk with hardware-specific boot and swap partitions, adding an
# LVM volume that contains a 10GB+ system root. The remainder of the volume will
# be used by the CSI driver for storing data.
zerombr
clearpart --all --initlabel
# Create boot and swap partitions as required by the current hardware platform
reqpart --add-boot
# Add an LVM volume group and allocate a system root logical volume
part pv.01 --grow
volgroup rhel pv.01
logvol / --vgname=rhel --fstype=xfs --size=10240 --name=root

# Lock root user account
rootpw --lock

# Configure network to use DHCP and activate on boot
network --bootproto=dhcp --device=link --activate --onboot=on

%pre-install --log=/dev/console --erroronfail

# Create a 'bootc' image registry authentication file
mkdir -p /etc/ostree
cat > /etc/ostree/auth.json <<'EOF'
$(cat "${AUTH_CONFIG}")
EOF

%end

# Pull a 'bootc' image from a remote registry
ostreecontainer --url "${IMAGE_REF}"

%post --log=/dev/console --erroronfail

# Create an OpenShift pull secret file
cat > /etc/crio/openshift-pull-secret <<'EOF'
$(cat "${PULL_SECRET}")
EOF
chmod 600 /etc/crio/openshift-pull-secret

%end
EOFKS
----

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-running-bootc-image-in-VM.adoc

[id="microshift-install-bootc-creating-vm_{context}"]
= Creating a virtual machine

[role="_abstract"]
You can create a virtual machine by using the {op-system-base-full} boot ISO image.

.Prerequisites

* You created the Kickstart file.

* You installed the {oc-first}.

* You have `redhat` credentials.

.Procedure

. Download the {op-system-base-full} boot ISO image from the Download Red{nbsp}Hat Enterprise Linux.

. Copy the downloaded file to the `/var/lib/libvirt/images` directory.

. Configure the VMNAME environment variable with your value by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ VMNAME=microshift--bootc
----

. Configure the NETNAME environment variable with your value by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ NETNAME=default
----

. Create a {op-system-base} virtual machine with 2 cores, 2GB of RAM and 20GB of storage by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo virt-install \
    --name ${VMNAME} \
    --vcpus 2 \
    --memory 2048 \
    --disk path=/var/lib/libvirt/images/${VMNAME}.qcow2,size=20 \
    --network network=${NETNAME},model=virtio \
    --events on_reboot=restart \
    --location /var/lib/libvirt/images/rhel-{op-system-version}-$(uname -m)-boot.iso \
    --initrd-inject kickstart.ks \
    --extra-args "inst.ks=file://kickstart.ks" \
    --wait
----
+
[NOTE]
====
The `sudo virt-install` command uses the Kickstart file to pull a bootc image from the remote registry and install the {op-system-base} operating system.
====

. Log in to the virtual machine by using your `redhat` credentials.

.Verification

. Verify that all of the {microshift-short} pods are running without error by entering the following command:
+
[source,terminal]
----
$ watch sudo oc get pods -A \
    --kubeconfig /var/lib/microshift/resources/kubeadmin/kubeconfig
----
+
.Example output
[source,text]
----
NAMESPACE                  NAME                                       READY   STATUS    RESTARTS      AGE
kube-system                csi-snapshot-controller-7cfb9df49c-kc9dx   1/1     Running   0             31s
openshift-dns              dns-default-rpnlt                          2/2     Running   0             14s
openshift-dns              node-resolver-rxvdk                        1/1     Running   0             31s
openshift-ingress          router-default-69cd7b5545-7zcw7            1/1     Running   0             29s
openshift-ovn-kubernetes   ovnkube-master-c7hlh                       4/4     Running   1 (16s ago)   31s
openshift-ovn-kubernetes   ovnkube-node-mkpht                         1/1     Running   1 (17s ago)   31s
openshift-service-ca       service-ca-5d5d96459d-5pd5s                1/1     Running   0             28s
openshift-storage          topolvm-controller-677cbfcdb9-28dqr        5/5     Running   0             31s
openshift-storage          topolvm-node-6fzbl                         3/3     Running   0             14s
----
