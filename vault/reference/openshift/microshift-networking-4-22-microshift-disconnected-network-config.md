---
title: "Configuring network settings for fully disconnected hosts"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-disconnected-network-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-disconnected-network-config
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Configuring network settings for fully disconnected hosts

[id="microshift-disconnected-network-config"]
= Configuring network settings for fully disconnected hosts

[role="_abstract"]
Learn how to apply networking customization and settings to run {microshift-short} on fully disconnected hosts. A disconnected host should be the {op-system-base-full} operating system, versions 9.0+, whether real or virtual, that runs without network connectivity.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-disconnected-network-config.adoc

[id="microshift-disconnected-host-preparation_{context}"]
= Preparing networking for fully disconnected hosts

[role="_abstract"]
To run {microshift-short} on a fully disconnected host with no external network connectivity, you prepare a persistent hostname, loopback IP addressing, DNS, and `/etc/hosts` entries before you apply {microshift-short} network configuration.

Typically this means that the device does not have an attached network interface controller (NIC) to provide a subnet. These steps can also be completed on a host with a NIC that is removed after setup. You can also automate these steps on a host that does not have a NIC by using the `%post` phase of a Kickstart file.

[IMPORTANT]
====
Configuring networking settings for disconnected environments is necessary because {microshift-short} requires a network device to support node communication. To meet this requirement, you must configure {microshift-short} networking settings to use the "fake" IP address you assign to the system loopback device during setup.
====

[id="microshift-disconnected-host-procedure-summary_{context}"]
== Procedure summary

To run {microshift-short} on a disconnected host, the following steps are required:

Prepare the host::
* Stop {microshift-short} if it is currently running and clean up changes the service has made to the network.
* Set a persistent hostname.
* Add a “fake” IP address on the loopback interface.
* Configure DNS to use the fake IP as local name server.
* Add an entry for the hostname to `/etc/hosts`.

Update the {microshift-short} configuration::
* Define the `nodeIP` parameter as the new loopback IP address.
* Set the `.node.hostnameOverride` parameter to the persistent hostname.

For the changes to take effect::
* Disable the default NIC if attached.
* Restart the host or device.

After starting, {microshift-short} runs using the loopback device for intra-node communication.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-disconnected-network-config.adoc

[id="microshift-undo-network-config_{context}"]
= Restoring {microshift-short} networking settings to default

[role="_abstract"]
To remove networking customizations and return the network to default settings, stop {microshift-short} and run a clean-up script.

.Prerequisites
* RHEL 9 or newer.
* MicroShift 4.14 or newer.
* Access to the host CLI.

.Procedure

. Stop the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl stop microshift
----

. Stop the `kubepods.slice` systemd unit by running the following command:
+
[source,terminal]
----
$ sudo systemctl stop kubepods.slice
----

. {microshift-short} installs a helper script to undo network changes made by OVN-K. Run the cleanup script by entering the following command:
+
[source,terminal]
----
$ sudo /usr/bin/microshift-cleanup-data --ovn
----

//Q: any sample output? what should we see when we run the script?

// Module included in the following assemblies:
//
// * microshift_networking/microshift-disconnected-network-config.adoc

[id="microshift-disconnected-host-network-config_{context}"]
= Configuring the networking settings for fully disconnected hosts

[role="_abstract"]
To configure the networking settings for running {microshift-short} on a fully disconnected host, you must prepare the host, update the networking configuration, then restart to apply the new settings. All commands are executed from the host CLI.

.Prerequisites
* RHEL 9 or newer.
* {microshift-short} 4.16 or newer.
* Access to the host CLI.
* A valid IP address chosen to avoid both internal and potential future external IP conflicts when running {microshift-short}.
* {microshift-short} networking settings are set to defaults.

[IMPORTANT]
====
The following procedure is for use cases in which access to the {microshift-short} node is not required after devices are deployed in the field. There is no remote node access after the network connection is removed.
====

.Procedure

. Add a fake IP address to the loopback interface by running the following command:
+
[source,terminal]
----
$ IP="10.44.0.1"
----
+
The fake IP address used in this example is `"10.44.0.1"`.
+
[source,terminal]
----
$ sudo nmcli con add type loopback con-name stable-microshift ifname lo ip4 ${IP}/32
----
+
[NOTE]
====
Any valid IP works if it avoids both internal {microshift-short} and potential future external IP conflicts. This can be any subnet that does not collide with the {microshift-short} node subnet or is be accessed by other services on the device.
====

. Configure the DNS interface to use the local name server by setting modifying the settings to ignore automatic DNS and reset it to the local name server:
+
.. Bypass the automatic DNS by running the following command:
+
[source,terminal]
----
$ sudo nmcli conn modify stable-microshift ipv4.ignore-auto-dns yes
----
+
.. Point the DNS interface to use the local name server:
+
[source,terminal]
----
$ sudo nmcli conn modify stable-microshift ipv4.dns "10.44.1.1"
----

. Get the hostname of the device by running the following command:
+
[source,terminal]
----
$ NAME="$(hostnamectl hostname)"
----

. Add an entry for the hostname of the node in the `/etc/hosts` file by running the following command:
+
[source,terminal]
----
$ echo "$IP $NAME" | sudo tee -a /etc/hosts >/dev/null
----

. Update the {microshift-short} configuration file by adding the following YAML snippet to `/etc/microshift/config.yaml`:
+
[source,terminal]
----
sudo tee /etc/microshift/config.yaml > /dev/null <<EOF
node:
  hostnameOverride: $(echo $NAME)
  nodeIP: $(echo $IP)
EOF
----

. {microshift-short} is now ready to use the loopback device for intra-node communications. Finish preparing the device for offline use.
+
.. If the device currently has a NIC attached, disconnect the device from the network.
+
.. Shut down the device and disconnect the NIC.
+
.. Restart the device for the offline configuration to take effect.

. Restart the {microshift-short} host to apply the configuration changes by running the following command:
+
[source,terminal]
----
$ sudo systemctl reboot
----
+
This step restarts the node. Wait for the greenboot health check to report the system healthy before implementing verification.

.Verification

At this point, network access to the {microshift-short} host has been severed. If you have access to the host terminal, you can use the host CLI to verify that the node has started in a stable state.

. Verify that the {microshift-short} node is running by entering the following commands:
+
[source,terminal]
----
$ export KUBECONFIG=/var/lib/microshift/resources/kubeadmin/kubeconfig
----
+
[source,terminal]
----
$ sudo -E oc get pods -A
----
+
.Example output
[source,terminal]
----
NAMESPACE                  NAME                                       READY   STATUS    RESTARTS      AGE
kube-system                csi-snapshot-controller-74d566564f-66n2f   1/1     Running   0             1m
openshift-dns              dns-default-dxglm                          2/2     Running   0             1m
openshift-dns              node-resolver-dbf5v                        1/1     Running   0             1m
openshift-ingress          router-default-8575d888d8-xmq9p            1/1     Running   0             1m
openshift-ovn-kubernetes   ovnkube-master-gcsx8                       4/4     Running   1             1m
openshift-ovn-kubernetes   ovnkube-node-757mf                         1/1     Running   1             1m
openshift-service-ca       service-ca-7d7c579f54-68jt4                1/1     Running   0             1m
openshift-storage          topolvm-controller-6d777f795b-bx22r        5/5     Running   0             1m
openshift-storage          topolvm-node-fcf8l                         4/4     Running   0             1m
----
