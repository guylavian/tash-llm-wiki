---
title: "Expanding the cluster"
type: reference
domain: openshift
slug: installing-4-22-bare-metal-expanding-the-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/bare-metal-expanding-the-cluster
version: 4.22
family: installing
documentKind: "Documentation"
---

# Expanding the cluster

[id="bare-metal-expanding-the-cluster"]
= Expanding the cluster

[role="_abstract"]
You can expand a bare-metal cluster by adding worker nodes after initial deployment to increase capacity and maintain high availability.

[NOTE]
====
Expanding the cluster using Redfish Virtual Media involves meeting minimum firmware requirements. See *Firmware requirements for installing with virtual media* in the *Prerequisites* section for additional details when expanding the cluster using Redfish Virtual Media.
====

// This is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-expanding-the-cluster.adoc

[id='preparing-the-bare-metal-node_{context}']
= Preparing the bare-metal node

[role="_abstract"]
Configure IP addressing for a new bare-metal node by using either static configuration or DHCP (Dynamic Host Configuration Protocol) reservations to enable network connectivity before adding the node to your cluster.

[IMPORTANT]
====
Some administrators prefer to use static IP addresses so that each node's IP address remains constant in the absence of a DHCP server. To configure static IP addresses with NMState, see "Optional: Configuring host network interfaces in the `install-config.yaml` file" in the "Setting up the environment for an OpenShift installation" section for additional details.
====

Preparing the bare-metal node requires executing the following procedure from the provisioner node.

.Prerequisites

* You have downloaded the `oc` binary.
* You have installed a bare-metal cluster.
* If you intend to use DHCP to provide the new machine's IP address, you have a DHCP server on your network.
* If you intend to use PXE to provide the boot image, you have a PXE server on your network.
* If you intend to install a machine of a different architecture than the control plane, your cluster uses the multi-architecture release image.

.Procedure

. Power off the bare-metal node by using the baseboard management controller (BMC), and ensure it is off.

. Retrieve the user name and password of the bare-metal node's baseboard management controller.

. Create `base64` strings from the user name and password:
+
[source,terminal,subs="+quotes"]
----
$ echo -ne "root" | base64
$ echo -ne "password" | base64
----

. Create a configuration file for the bare-metal node. Depending on whether you are using a static configuration or a DHCP server, use one of the following example `bmh.yaml` files, replacing values in the YAML to match your environment:
+
[source,terminal]
----
$ vim bmh.yaml
----
.. *Static configuration* `bmh.yaml`:
+
[source,yaml]
----
---
apiVersion: v1
kind: Secret
metadata:
 name: openshift-worker-<num>-network-config-secret
 namespace: openshift-machine-api
type: Opaque
stringData:
 nmstate: |
  interfaces:
  - name: <nic1_name>
    type: ethernet
    state: up
    ipv4:
      address:
      - ip: <ip_address>
        prefix-length: 24
      enabled: true
  dns-resolver:
    config:
      server:
      - <dns_ip_address>
  routes:
    config:
    - destination: 0.0.0.0/0
      next-hop-address: <next_hop_ip_address>
      next-hop-interface: <next_hop_nic1_name>
---
apiVersion: v1
kind: Secret
metadata:
  name: openshift-worker-<num>-bmc-secret
  namespace: openshift-machine-api
type: Opaque
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: openshift-worker-<num>
  namespace: openshift-machine-api
spec:
  online: True
  bootMACAddress: <nic1_mac_address>
  bmc:
    address: <protocol>://<bmc_url>
    credentialsName: openshift-worker-<num>-bmc-secret
    disableCertificateVerification: True
    username: <bmc_username>
    password: <bmc_password>
  rootDeviceHints:
    deviceName: <root_device_hint>
  preprovisioningNetworkDataName: openshift-worker-<num>-network-config-secret
----
+
where:

--
`metadate.name: openshift-worker-<num>-network-config-secret`:: Specifies the name of the secret that contains the network configuration for a newly created node. Follow the `nmstate` syntax to define the network configuration for your node. See "Optional: Configuring host network interfaces in the install-config.yaml file" for details on configuring NMState syntax.
`metadate.name: openshift-worker-<num>`:: Specifies the worker number of the bare-metal node in the `name` fields, the `credentialsName` field, and the `preprovisioningNetworkDataName` field. Replace `<num>` with the worker number.
`stringData.nmstate: |`:: Specifies the NMState YAML syntax to configure the host interfaces.
`stringData.nmstate.interfaces.state: up`:: Specifies the interface state. Optional: If you have configured the network interface with `nmstate`, and you want to disable an interface, set `state: up` with the IP addresses set to `enabled: false` as shown:
+
[source,yaml]
----
---
   interfaces:
   - name: <nic_name>
     type: ethernet
     state: up
     ipv4:
       enabled: false
     ipv6:
       enabled: false
----

`stringData.nmstate.interfaces.name: <nic1_name>`:: Specifies the network interface name.
`stringData.nmstate.interfaces.ipv4.address.ip: <ip_address>`:: Specifies the IPv4 address.
`stringData.nmstate.dns-resolver.config.server: <dns_ip_address>`:: Specifies the DNS server IP address.
`stringData.nmstate.routes.config.next-hop-address: <next_hop_ip_address>`:: Specifies the next hop IP address for the default route.
`stringData.nmstate.routes.config.next-hop-interface: <next_hop_nic1_name>`:: Specifies the next hop interface for the default route.
`data.username: <base64_of_uid>`:: Specifies the base64-encoded user name.
`data.password: <base64_of_pwd>`:: Specifies the base64-encoded password.
`spec.bootMACAddress: <nic1_mac_address>`:: Specifies the MAC address of the bare-metal node's first NIC. See the "BMC addressing" section for additional BMC configuration options.
`spec.bmc.address: <protocol>://<bmc_url>`:: Specifies the BMC address protocol. Replace `<protocol>` with the BMC protocol, such as IPMI, Redfish, or others.
`spec.bmc.address: <protocol>://<bmc_url>`:: Specifies the BMC URL.
`spec.bmc.disableCertificateVerification: True`:: Specifies whether to skip certificate validation. Set `disableCertificateVerification` to true to skip certificate validation.
`spec.bmc.username: <bmc_username>`:: Specifies the BMC user name.
`spec.bmc.password: <bmc_password>`:: Specifies the BMC password.
`spec.rootDeviceHints.deviceName: <root_device_hint>`:: Specifies the root device hint. Optional: Replace `<root_device_hint>` with a device path if you specify a root device hint.
`spec.preprovisioningNetworkDataName: openshift-worker-<num>-network-config-secret`:: Specifies the network configuration secret name in the `preprovisioningNetworkDataName` of the `BareMetalHost` CR. Optional: Provide this value if you have configured the network interface for the newly created node.
--

.. *DHCP configuration* `bmh.yaml`:
+
[source,yaml]
----
---
apiVersion: v1
kind: Secret
metadata:
  name: openshift-worker-<num>-bmc-secret
  namespace: openshift-machine-api
type: Opaque
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: openshift-worker-<num>
  namespace: openshift-machine-api
spec:
  online: True
  bootMACAddress: <nic1_mac_address>
  bmc:
    address: <protocol>://<bmc_url>
    credentialsName: openshift-worker-<num>-bmc-secret
    disableCertificateVerification: True
    username: <bmc_username>
    password: <bmc_password>
  rootDeviceHints:
    deviceName: <root_device_hint>
  preprovisioningNetworkDataName: openshift-worker-<num>-network-config-secret
----
+
where:

--
`data.username: <base64_of_uid>`:: Specifies the base64-encoded user name.
`data.password: <base64_of_pwd>`:: Specifies the base64-encoded password.
`spec.bootMACAddress: <nic1_mac_address>`:: Specifies the MAC address of the bare-metal node's first NIC. See the "BMC addressing" section for additional BMC configuration options.
`spec.bmc.address: <protocol>://<bmc_url>`:: Specifies the BMC address protocol. Replace `<protocol>` with the BMC protocol, such as IPMI, Redfish, or others.
`spec.bmc.address: <protocol>://<bmc_url>`:: Specifies the BMC URL.
`spec.bmc.credentialsName: openshift-worker-<num>-bmc-secret`:: Specifies the BMC credentials secret name. Replace `<num>` with the worker number of the bare-metal node in the `name` fields, the `credentialsName` field, and the `preprovisioningNetworkDataName` field.
`spec.bmc.disableCertificateVerification: True`:: Specifies whether to skip certificate validation. Set `disableCertificateVerification` to true to skip certificate validation.
`spec.bmc.username: <bmc_username>`:: Specifies the BMC user name.
`spec.bmc.password: <bmc_password>`:: Specifies the BMC password.
`spec.rootDeviceHints.deviceName: <root_device_hint>`:: Specifies the root device hint. Optional: Replace `<root_device_hint>` with a device path if you specify a root device hint.
`spec.preprovisioningNetworkDataName: openshift-worker-<num>-network-config-secret`:: Specifies the network configuration secret name in the `preprovisioningNetworkDataName` of the `BareMetalHost` CR. Optional: Provide this value if you have configured the network interface for the newly created node.
--

[NOTE]
====
If the MAC address of an existing bare-metal node matches the MAC address of a bare-metal host that you are attempting to provision, then the Ironic installation will fail. If the host enrollment, inspection, cleaning, or other Ironic steps fail, the Bare Metal Operator retries the installation continuously. See "Diagnosing a host duplicate MAC address" for more information.
====

. Create the bare-metal node:
+
[source,terminal]
----
$ oc -n openshift-machine-api create -f bmh.yaml
----
+
.Example output
[source,terminal]
----
secret/openshift-worker-<num>-network-config-secret created
secret/openshift-worker-<num>-bmc-secret created
baremetalhost.metal3.io/openshift-worker-<num> created
----
+
Replace `<num>` with the worker number.

. Power on and inspect the bare-metal node:
+
[source,terminal]
----
$ oc -n openshift-machine-api get bmh openshift-worker-<num>
----
+
Replace `<num>` with the worker node number.
+
.Example output
[source,terminal]
----
NAME                    STATE       CONSUMER   ONLINE   ERROR
openshift-worker-<num>  available              true
----

. Add the new machine to the cluster by scaling the machine set.

.. To manually scale the machine set, follow the procedure titled _Provisioning the bare-metal node_.
.. To automatically scale the machine set, follow the procedure titled _Automatically scaling machines to the number of available bare-metal hosts_ in the _Scalability and Performance_ section.

[role="_additional-resources"]
.Additional resources

* Optional: Configuring host network interfaces in the install-config.yaml file

* Automatically scaling machines to the number of available bare-metal hosts

// This is included in the following assemblies:
//
// installing/installing_bare_metal/bare-metal-expanding-the-cluster.adoc

[id="replacing-a-bare-metal-control-plane-node_{context}"]
= Replacing a bare-metal control plane node

[role="_abstract"]
Replace a failed or unhealthy control plane node by removing the old `BareMetalHost` and `Machine` objects, then creating new ones to maintain cluster high availability.

[IMPORTANT]
====
If you reuse the `BareMetalHost` object definition from an existing control plane host, do not leave the `externallyProvisioned` field set to `true`.

Existing control plane `BareMetalHost` objects might have the `externallyProvisioned` flag set to `true` if they were provisioned by the OpenShift Container Platform installation program.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

* You have taken an etcd backup.
+
[IMPORTANT]
====
Take an etcd backup before performing this procedure so that you can restore your cluster if you encounter any issues. For more information about taking an etcd backup, see the _Additional resources_ section.
====

.Procedure

. Ensure that the Bare Metal Operator is available:
+
[source,terminal]
----
$ oc get clusteroperator bare-metal
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
baremetal        True          False      False   3d15h
----

. Remove the old `BareMetalHost` and `Machine` objects:
+
[source,terminal]
----
$ oc delete bmh -n openshift-machine-api <host_name>
----
+
[source,terminal]
----
$ oc delete machine -n openshift-machine-api <machine_name>
----
+
Replace `<host_name>` with the name of the host and `<machine_name>` with the name of the machine. The machine name is displayed under the `CONSUMER` field.
+
After you remove the `BareMetalHost` and `Machine` objects, then the machine controller automatically deletes the `Node` object.

. Create the new `BareMetalHost` object and the secret to store the BMC credentials. Set the following parameters:
+
--
`spec.bmc.credentialsName: control-plane-<num>-bmc-secret`:: Specifies the BMC credentials secret name. Replace `<num>` with the control plane number of the bare-metal node in the `name` fields and the `credentialsName` field.
`data.username: <base64_of_uid>`:: Specifies the base64-encoded user name. Replace `<base64_of_uid>` with the `base64` string of the user name.
`data.password: <base64_of_pwd>`:: Specifies the base64-encoded password. Replace `<base64_of_pwd>` with the `base64` string of the password.
`spec.bmc.address: <protocol>://<bmc_ip>`:: Specifies the BMC address. Replace `<protocol>` with the BMC protocol, such as `redfish`, `redfish-virtualmedia`, `idrac-virtualmedia`, or others. Replace `<bmc_ip>` with the IP address of the bare-metal node's baseboard management controller. For additional BMC configuration options, see "BMC addressing" in the _Additional resources_ section.
`spec.bootMACAddress: <NIC1_mac_address>`:: Specifies the MAC address of the bare-metal node's first NIC. Replace `<NIC1_mac_address>` with the MAC address.
--

. Run the following command:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
----
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: control-plane-<num>-bmc-secret
  namespace: openshift-machine-api
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
type: Opaque
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: control-plane-<num>
  namespace: openshift-machine-api
spec:
  automatedCleaningMode: disabled
  bmc:
    address: <protocol>://<bmc_ip>
    credentialsName: control-plane-<num>-bmc-secret
  bootMACAddress: <NIC1_mac_address>
  bootMode: UEFI
  externallyProvisioned: false
  online: true
EOF
----
+
After the inspection is complete, the `BareMetalHost` object is created and available to be provisioned.

. View available `BareMetalHost` objects:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                          STATE                    CONSUMER                   ONLINE   ERROR   AGE
control-plane-1.example.com   available                control-plane-1            true             1h10m
control-plane-2.example.com   externally provisioned   control-plane-2            true             4h53m
control-plane-3.example.com   externally provisioned   control-plane-3            true             4h53m
compute-1.example.com         provisioned              compute-1-ktmmx            true             4h53m
compute-1.example.com         provisioned              compute-2-l2zmb            true             4h53m
----
+
[NOTE]
====
There are no `MachineSet` objects for control plane nodes, so you must create a `Machine` object instead. You can copy the `providerSpec` from another control plane `Machine` object.
====

. Create a `Machine` object:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  annotations:
    metal3.io/BareMetalHost: openshift-machine-api/control-plane-<num>
  labels:
    machine.openshift.io/cluster-api-cluster: control-plane-<num>
    machine.openshift.io/cluster-api-machine-role: master
    machine.openshift.io/cluster-api-machine-type: master
  name: control-plane-<num>
  namespace: openshift-machine-api
spec:
  metadata: {}
  providerSpec:
    value:
      apiVersion: baremetal.cluster.k8s.io/v1alpha1
      customDeploy:
        method: install_coreos
      hostSelector: {}
      image:
        checksum: ""
        url: ""
      kind: BareMetalMachineProviderSpec
      metadata:
        creationTimestamp: null
      userData:
        name: master-user-data-managed
EOF
----
+
Replace `<num>` with the control plane number of the bare-metal node in the `annotations`, `labels` and `name` fields.
+
. To view the `BareMetalHost` objects, run the following command:
+
[source,terminal]
----
$ oc get bmh -A
----
+
.Example output
[source,terminal]
----
NAME                          STATE                    CONSUMER                   ONLINE   ERROR   AGE
control-plane-1.example.com   provisioned              control-plane-1            true             2h53m
control-plane-2.example.com   externally provisioned   control-plane-2            true             5h53m
control-plane-3.example.com   externally provisioned   control-plane-3            true             5h53m
compute-1.example.com         provisioned              compute-1-ktmmx            true             5h53m
compute-2.example.com         provisioned              compute-2-l2zmb            true             5h53m
----

. After the RHCOS installation, verify that the `BareMetalHost` is added to the cluster:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS      ROLES     AGE   VERSION
control-plane-1.example.com    available   master    4m2s  v1.35.4
control-plane-2.example.com    available   master    141m  v1.35.4
control-plane-3.example.com    available   master    141m  v1.35.4
compute-1.example.com          available   worker    87m   v1.35.4
compute-2.example.com          available   worker    87m   v1.35.4
----
+
[NOTE]
====
After replacement of the new control plane node, the etcd pod running in the new node is in `crashloopback` status. See "Replacing an unhealthy etcd member" in the _Additional resources_ section for more information.
====

[role="_additional-resources"]
.Additional resources

* Replacing an unhealthy etcd member

* Backing up etcd

* Configuration using the Bare Metal Operator

* BMC addressing

// This is included in the following assemblies:
//
// installing_bare_metal/ipi/ipi-install-expanding-the-cluster.adoc

[id="preparing-to-deploy-with-virtual-media-on-the-baremetal-network_{context}"]
= Preparing to deploy with Virtual Media on the `bare-metal` network

[role="_abstract"]
Configure the provisioning custom resource to enable Virtual Media deployment on the `bare-metal` network when expanding clusters that use a separate provisioning network.

.Prerequisites

* There is an existing cluster with a `bare-metal` network and a `provisioning` network.

.Procedure

. Edit the `provisioning` custom resource (CR) to enable deploying with Virtual Media on the `bare-metal` network:
+
[source,terminal]
----
oc edit provisioning
----
+
[source,yaml]
----
  apiVersion: metal3.io/v1alpha1
  kind: Provisioning
  metadata:
    creationTimestamp: "2021-08-05T18:51:50Z"
    finalizers:
    - provisioning.metal3.io
    generation: 8
    name: provisioning-configuration
    resourceVersion: "551591"
    uid: f76e956f-24c6-4361-aa5b-feaf72c5b526
  spec:
    provisioningDHCPRange: 172.22.0.10,172.22.0.254
    provisioningIP: 172.22.0.3
    provisioningInterface: enp1s0
    provisioningNetwork: Managed
    provisioningNetworkCIDR: 172.22.0.0/24
    virtualMediaViaExternalNetwork: true
  status:
    generations:
    - group: apps
      hash: ""
      lastGeneration: 7
      name: metal3
      namespace: openshift-machine-api
      resource: deployments
    - group: apps
      hash: ""
      lastGeneration: 1
      name: metal3-image-cache
      namespace: openshift-machine-api
      resource: daemonsets
    observedGeneration: 8
    readyReplicas: 0
----
+
Replace `spec.virtualMediaViaExternalNetwork: true` with `virtualMediaViaExternalNetwork: true` to add to the `provisioning` CR.

. If the image URL exists, edit the `machineset` to use the API VIP address. This step only applies to clusters installed in versions 4.9 or earlier.
+
[source,terminal]
----
oc edit machineset
----
+
[source,yaml]
----
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    creationTimestamp: "2021-08-05T18:51:52Z"
    generation: 11
    labels:
      machine.openshift.io/cluster-api-cluster: ostest-hwmdt
      machine.openshift.io/cluster-api-machine-role: worker
      machine.openshift.io/cluster-api-machine-type: worker
    name: ostest-hwmdt-worker-0
    namespace: openshift-machine-api
    resourceVersion: "551513"
    uid: fad1c6e0-b9da-4d4a-8d73-286f78788931
  spec:
    replicas: 2
    selector:
      matchLabels:
        machine.openshift.io/cluster-api-cluster: ostest-hwmdt
        machine.openshift.io/cluster-api-machineset: ostest-hwmdt-worker-0
    template:
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: ostest-hwmdt
          machine.openshift.io/cluster-api-machine-role: worker
          machine.openshift.io/cluster-api-machine-type: worker
          machine.openshift.io/cluster-api-machineset: ostest-hwmdt-worker-0
      spec:
        metadata: {}
        providerSpec:
          value:
            apiVersion: baremetal.cluster.k8s.io/v1alpha1
            hostSelector: {}
            image:
              checksum: http:/172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2.<md5sum>
              url: http://172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2
            kind: BareMetalMachineProviderSpec
            metadata:
              creationTimestamp: null
            userData:
              name: worker-user-data
  status:
    availableReplicas: 2
    fullyLabeledReplicas: 2
    observedGeneration: 11
    readyReplicas: 2
    replicas: 2
----
+
where:
--
`spec.template.spec.providerSpec.value.image.checksum: http:/172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2.<md5sum>`:: Specifies to edit the `checksum` URL to use the API VIP address.
`spec.template.spec.providerSpec.value.image.url: http://172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2`:: Specifies to edit the `url` URL to use the API VIP address.
--

[id="ipi-install-diagnosing-duplicate-mac-address_{context}"]
= Diagnosing a duplicate MAC address when provisioning a new host in the cluster

[role="_abstract"]
You can diagnose a duplicate MAC address issue by examining bare-metal host registration errors in the cluster to identify and resolve conflicts preventing new node provisioning.

You can diagnose a duplicate MAC address by examining the bare-metal hosts that are running in the `openshift-machine-api` namespace.

.Prerequisites

* Install an OpenShift Container Platform cluster on bare metal.
* Install the OpenShift Container Platform CLI `oc`.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Get the bare-metal hosts running in the `openshift-machine-api` namespace:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                 STATUS   PROVISIONING STATUS      CONSUMER
openshift-master-0   OK       externally provisioned   openshift-zpwpq-master-0
openshift-master-1   OK       externally provisioned   openshift-zpwpq-master-1
openshift-master-2   OK       externally provisioned   openshift-zpwpq-master-2
openshift-worker-0   OK       provisioned              openshift-zpwpq-worker-0-lv84n
openshift-worker-1   OK       provisioned              openshift-zpwpq-worker-0-zd8lm
openshift-worker-2   error    registering
----

. To see more detailed information about the status of the failing host, run the following command replacing `<bare_metal_host_name>` with the name of the host:
+
[source,terminal]
----
$ oc get -n openshift-machine-api bmh <bare_metal_host_name> -o yaml
----
+
.Example output
[source,yaml]
----
...
status:
  errorCount: 12
  errorMessage: MAC address b4:96:91:1d:7c:20 conflicts with existing node openshift-worker-1
  errorType: registration error
...
----

// This is included in the following assemblies:
//
// ipi-install-expanding-the-cluster.adoc

[id='provisioning-the-bare-metal-node_{context}']
= Provisioning the bare-metal node

[role="_abstract"]
Scale the compute machine set to provision a new bare-metal node and add it as a worker to your cluster after the node is prepared and available.

.Procedure

. Ensure the `STATE` is `available` before provisioning the bare-metal node.
+
[source,terminal]
----
$  oc -n openshift-machine-api get bmh openshift-worker-<num>
----
+
Replace `<num>` with the worker node number.
+
[source,terminal]
----
NAME              STATE     ONLINE ERROR  AGE
openshift-worker  available true          34h
----

. Get a count of the number of worker nodes.
[source,terminal]
+
----
$ oc get nodes
----
+
[source,terminal]
----
NAME                                                STATUS   ROLES           AGE     VERSION
openshift-master-1.openshift.example.com            Ready    master          30h     v1.35.4
openshift-master-2.openshift.example.com            Ready    master          30h     v1.35.4
openshift-master-3.openshift.example.com            Ready    master          30h     v1.35.4
openshift-worker-0.openshift.example.com            Ready    worker          30h     v1.35.4
openshift-worker-1.openshift.example.com            Ready    worker          30h     v1.35.4
----

. Get the compute machine set.
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
[source,terminal]
----
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
...
openshift-worker-0.example.com      1         1         1       1           55m
openshift-worker-1.example.com      1         1         1       1           55m
----

. Increase the number of worker nodes by one.
+
[source,terminal]
----
$ oc scale --replicas=<num> machineset <machineset> -n openshift-machine-api
----
+
Replace `<num>` with the new number of worker nodes. Replace `<machineset>` with the name of the compute machine set from the previous step.

. Check the status of the bare-metal node.
+
[source,terminal]
----
$ oc -n openshift-machine-api get bmh openshift-worker-<num>
----
+
Replace `<num>` with the worker node number. The STATE changes from `ready` to `provisioning`.
+
[source,terminal]
----
NAME                    STATE             CONSUMER                          ONLINE   ERROR
openshift-worker-<num>  provisioning      openshift-worker-<num>-65tjz      true
----
+
The `provisioning` status remains until the OpenShift Container Platform cluster provisions the node. This can take 30 minutes or more. After the node is provisioned, the state will change to `provisioned`.
+
[source,terminal]
----
NAME                    STATE             CONSUMER                          ONLINE   ERROR
openshift-worker-<num>  provisioned       openshift-worker-<num>-65tjz      true
----

. After provisioning completes, ensure the bare-metal node is ready.
+
[source,terminal]
----
$ oc get nodes
----
+
[source,terminal]
----
NAME                                          STATUS   ROLES   AGE     VERSION
openshift-master-1.openshift.example.com      Ready    master  30h     v1.35.4
openshift-master-2.openshift.example.com      Ready    master  30h     v1.35.4
openshift-master-3.openshift.example.com      Ready    master  30h     v1.35.4
openshift-worker-0.openshift.example.com      Ready    worker  30h     v1.35.4
openshift-worker-1.openshift.example.com      Ready    worker  30h     v1.35.4
openshift-worker-<num>.openshift.example.com  Ready    worker  3m27s   v1.35.4
----
+
You can also check the kubelet.
+
[source,terminal]
----
$ ssh openshift-worker-<num>
----
+
[source,terminal]
----
[kni@openshift-worker-<num>]$ journalctl -fu kubelet
----
