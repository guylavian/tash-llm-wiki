---
title: "Configuring and using multiple networks"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-cni-multus-using
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-cni-multus-using
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Configuring and using multiple networks

[id="microshift-cni-multus-using"]
= Configuring and using multiple networks

[role="_abstract"]
After you have installed the {microshift-short} Multus Container Network Interface (CNI), you can use other networking plugins by using configurations.

// Module included in the following assemblies:
//
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="IP-address-management-types-and-additional-networks_{context}"]
= IP address management types and additional networks

[role="_abstract"]
IP addresses are provisioned for an additional network through an IP Address Management (IPAM) CNI plugin that you configure. Supported IP address provisioning types in {microshift-short} are `host-local`, `static`, and `dhcp`.

[id="bridge-interface-specifics_{context}"]
== bridge interface specifics
When using the `bridge` type interface and the `dhcp` IPAM, a DHCP server listening on the bridged network is required. If you are using a firewall, configuring the `firewalld` service by running the `firewall-cmd --remove-service=dhcp` command to allow DHCP traffic on the network zone is also required.

[id="macvlan-interface-specifics_{context}"]
== macvlan interface specifics
The `macvlan` type interface accesses the network that the host is connected to. This means that the interface can receive an IP address from the DHCP server on the host network if the `dhcp` IPAM plugin is used.

[id="ipvlan-interface-specifics_{context}"]
== ipvlan interface specifics
The `ipvlan` interface also has direct access to the host network, but shares a MAC address with the host interface. The `ipvlan` type interface cannot be used with the `dhcp` plugin because of the shared MAC address. The IPAM plugin does not support the DHCP protocol with `ClientID`.

// Module included in the following assemblies:
//
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="microshift-cni-multus-nad-additional-network_{context}"]
= Creating a NetworkAttachmentDefinition for an additional network

[role="_abstract"]
You can create a `NetworkAttachmentDefinition` configuration file for an additional network in order to use other CNI plugins.

In this example, a bridge-type interface is used. You can also use the example workflow here that uses `host-local` IP address management (IPAM) to configure other supported additional network types.

[IMPORTANT]
====
If you use `bridge` and the `dhcp` IPAM, a DHCP server listening on the bridged network is required. If you are also using a firewall, configuring the firewalld service to allow DHCP traffic on the network zone is also required. You can run the `firewall-cmd --remove-service=dhcp` command in this case.
====

.Prerequisites

* The {microshift-short} Multus CNI is installed.
* The {oc-first} is installed.
* {microshift-short} is running.

.Procedure

. Optional: Verify that the {microshift-short} node is running with the Multus CNI by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-multus
----
+
.Example output
[source,terminal]
----
NAME                READY   STATUS    RESTARTS   AGE
dhcp-daemon-dfbzw   1/1     Running   0          5h
multus-rz8xc        1/1     Running   0          5h
----

. Create a `NetworkAttachmentDefinition` configuration file by running the following command and using the following example file for reference:
+
[source,terminal]
----
$ oc apply -f network-attachment-definition.yaml
----
+
.Example `NetworkAttachmentDefinition` file
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: bridge-conf
spec:
  config: '{
      "cniVersion": "0.4.0",
      "type": "bridge",
      "bridge": "br-test",
      "mode": "bridge",
      "ipam": {
        "type": "host-local",
        "ranges": [
          [
            {
              "subnet": "10.10.0.0/24",
              "rangeStart": "10.10.0.20",
              "rangeEnd": "10.10.0.50",
              "gateway": "10.10.0.254"
             }
          ],
          [
            {
              "subnet": "fd00:IJKL:MNOP:10::0/64",
              "rangeStart": "fd00:IJKL:MNOP:10::1",
              "rangeEnd": "fd00:IJKL:MNOP:10::9"
        "dataDir": "/var/lib/cni/br-test"
      }
    }'
----
+
where:

`type`:: Specifies a name of the CNI plugin. This example uses the `bridge` type.
`bridge`:: Specifies the name of the bridge on the {microshift-short} host that is used. The additional interface of the pod is connected to that bridge. If the interface does not exist on the host, the Bridge CNI creates it. If the interface already exists, it is reused. In this example, the name of the interface is `br-test`.
`ipam`:: Specifies the IPAM type.
`ipam.ranges.`:: Specifies the IP address range for the additional network. IPv6 addresses can be added to the secondary interface.
+
--
[NOTE]
====
Using the name of the bridge is specific to the `bridge` type of plugin. Other plugins use different fields in their `NetworkAttachmentDefinitions`. For example, the `macvlan` and `ipvlan` configurations use `master` to specify the host interface to attach.
====
--

//MicroShift-edited version of OCP procedure
// Module included in the following assemblies:
//
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="microshift-nw-multus-add-pod_{context}"]
= Adding a pod to an additional network

[role="_abstract"]
You can add a pod to an additional network. At the time a pod is created, additional networks are attached to it. The pod continues to send normal node-related network traffic over the default network.

If you want to attach additional networks to a pod that is already running, you must restart the pod.

.Prerequisites

* The {oc-first} is installed.
* The node is running.
* A network defined by a `NetworkAttachmentDefinition` object that you want to attach the pod to exists.

.Procedure

. Add an annotation to a `Pod` YAML file. Only one of the following annotation formats can be used:

.. To attach an additional network without any customization, add an annotation with the following format. Replace `_<network>_` with the name of the additional network to associate with the pod:
+
[source,yaml,subs="+quotes"]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: _<network>_[,_<network>_,...]
# ...
----
+
Replace `_<network>_` with the name of each additional network to associate with the pod. To specify more than one additional network, separate each network with a comma. Do not include whitespaces between the commas. If you specify the same additional network multiple times, that pod has multiple network interfaces attached to that network.
+
The following example annotation specifies a bridge-type additional network:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: bridge-conf
# ...
----

.. To attach an additional network with customizations, add an annotation with the following format:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "<network>",
          "namespace": "<namespace>",
          "default-route": ["<default-route>"]
        }
      ]
# ...
----
+
where:

`name`:: Specifies the name of the additional network defined by a `NetworkAttachmentDefinition` object.
`namespace`:: Specifies the namespace where the `NetworkAttachmentDefinition` object is defined.
`default-route`:: Specifies an optional field to provide an override for the default route, such as `192.168.17.1`.

. To create a `Pod` YAML file and add the  `NetworkAttachmentDefinition` annotation for an additional network, run the following command and use the example YAML:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f ./_<test_bridge>_.yaml
----
+
Replace `_<test_bridge>_` with the pod name that you want to use.
+
The following example output shows that the `test_bridge` pod has been created:
+
[source,terminal]
----
pod/test_bridge created
----
+
.Example `test_bridge` pod YAML
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: test_bridge
  annotations:
    k8s.v1.cni.cncf.io/networks: bridge-conf
  labels:
    app: test_bridge
spec:
  terminationGracePeriodSeconds: 0
  containers:
  - name: hello-microshift
    image: quay.io/microshift/busybox:1.36
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo -ne \"HTTP/1.0 200 OK\r\nContent-Length: 16\r\n\r\nHello MicroShift\" | nc -l -p 8080 ; done"]
    ports:
    - containerPort: 8080
      protocol: TCP
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      runAsNonRoot: true
      runAsUser: 1001
      runAsGroup: 1001
      seccompProfile:
        type: RuntimeDefault
----
+
. Make sure that the `NetworkAttachmentDefinition` annotation is correct:
+
The following example `NetworkAttachmentDefinition` annotation specifies a bridge-type additional network:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: bridge-conf
# ...
----

. Optional: To confirm that the `NetworkAttachmentDefinition` annotation exists in a `Pod` YAML, run the following command, replacing `_<name>_` with the name of the pod.
+
[source,terminal,subs="+quotes"]
----
$ oc get pod _<name>_ -o yaml
----
+
Replace `_<name>_` with the pod name you want to use. In the following example, `_<test_bridge>_` is used.

+
In the following example, the `test_bridge` is attached to the `net1` additional network:
+

[source,terminal,subs="+quotes"]
----
$ oc get pod _<test_bridge>_ -o yaml
----
+
Replace `_<test_bridge>_` with the name of the bridge you want to use.
+
The following example output shows that the `test_bridge` pod is attached to the `net1` additional network:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: bridge-conf
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.42.0.18"
          ],
          "default": true,
          "dns": {}
      },{
          "name": "bridge-conf",
          "interface": "net1",
          "ips": [
              "20.2.2.100"
          ],
          "mac": "22:2f:60:a5:f8:00",
          "dns": {}
      }]
  name: pod
  namespace: default
spec:
# ...
status:
# ...
----
+
The `k8s.v1.cni.cncf.io/network-status` parameter is a JSON array of objects. Each object describes the status of an additional network attached to the pod. The annotation value is stored as a plain text value.

. Verify that the pod is running by running the following command:
+
[source,terminal]
----
$ oc get pod
----
+
.Example output
[source,terminal]
----
NAME          READY   STATUS    RESTARTS   AGE
test_bridge   1/1     Running   0          81s
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="microshift-cni-multus-add-network-example-config_{context}"]
= Configuring an additional network

[role="_abstract"]
After you have created the `NetworkAttachmentDefinition` object and applied it, you can configure an additional network.

In this example, the `bridge` type additional network is used. You can also use this workflow for other network types.

.Prerequisites
* You created and applied the `NetworkAttachmentDefinition` object configuration.

.Procedure
. Verify that the bridge was created on the host by running the following command:
+
[source,terminal]
----
$ ip a show br-test
----
+
.Example output
[source,terminal]
----
22: br-test: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 96:bf:ca:be:1d:15 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::34e2:bbff:fed2:31f2/64 scope link
       valid_lft forever preferred_lft forever
----

. Configure an IP address for the bridge by running the following command:
+
[source,terminal]
----
$ sudo ip addr add 10.10.0.10/24 dev br-test
----

. Verify that the IP address configuration is added to the bridge by running the following command:
+
[source,terminal]
----
$ ip a show br-test
----
+
.Example output
[source,terminal]
----
22: br-test: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 96:bf:ca:be:1d:15 brd ff:ff:ff:ff:ff:ff
    inet 10.10.0.10/24 scope global br-test
       valid_lft forever preferred_lft forever
    inet6 fe80::34e2:bbff:fed2:31f2/64 scope link
       valid_lft forever preferred_lft forever
----
+
Confirm that the IP address is configured as expected.

. Verify the IP address of the pod by running the following command:
+
[source,terminal]
----
$ oc get pod test-bridge --output=jsonpath='{.metadata.annotations.k8s\.v1\.cni\.cncf\.io/network-status}'
----
+
.Example output
[source,terminal]
----
[{
    "name": "ovn-kubernetes",
    "interface": "eth0",
    "ips": [
        "10.42.0.17"
    ],
    "mac": "0a:58:0a:2a:00:11",
    "default": true,
    "dns": {}
},{
    "name": "default/bridge-conf",
    "interface": "net1",
    "ips": [
        "10.10.0.20"
    ],
    "mac": "82:01:98:e5:0c:b7",
    "dns": {}
----
+
Confirm that the bridge additional network is attached as expected-`"default/bridge-conf"`.

. Optional: You can use `oc exec` to access the pod and confirm its interfaces by using the `ip` command:
+
[source,terminal]
----
$ oc exec -ti test-bridge -- ip a
----
+
.Example output
[source,terminal]
----
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0@if21: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue
    link/ether 0a:58:0a:2a:00:11 brd ff:ff:ff:ff:ff:ff
    inet 10.42.0.17/24 brd 10.42.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::858:aff:fe2a:11/64 scope link
       valid_lft forever preferred_lft forever
3: net1@if23: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue
    link/ether 82:01:98:e5:0c:b7 brd ff:ff:ff:ff:ff:ff
    inet 10.10.0.20/24 brd 10.10.0.255 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::8001:98ff:fee5:cb7/64 scope link
       valid_lft forever preferred_lft forever
----
+
In the example the pod is attached to the 10.10.0.20 IP address on the `net1 interface` as expected.

. Confirm that the connection is working as expected by accessing the HTTP server in the pod from the {microshift-short} host. Use the following command:
+
[source,terminal]
----
$ curl 10.10.0.20:8080
----
+
.Example output
[source,terminal]
----
Hello MicroShift
----

//OCP procedure, edit with conditionals and care
// Module included in the following assemblies:
//
// * networking/multiple_networks/removing-pod.adoc
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="nw-multus-remove-pod_{context}"]
= Removing a pod from a secondary network

[role="_abstract"]
To disconnect a pod from specific network configurations in OpenShift Container Platform, you can remove the pod from a secondary network. Delete the pod using the `oc delete pod` command to remove its connection to the secondary network.

.Prerequisites

* A secondary network is attached to the pod.
* Install the OpenShift CLI (`oc`).
* Log in to the cluster.

.Procedure

* Delete the pod by entering the following command:
+
[source,terminal]
----
$ oc delete pod <name> -n <namespace>
----
+
--
where:

`<name>`:: Specifies the name of the pod.
`<namespace>`:: Specifies the namespace that contains the pod.
--

// Module included in the following assemblies:
//
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="microshift-cni-multus-troubleshoot_{context}"]
= Troubleshooting Multus networking

[role="_abstract"]
If the settings for multiple networks are not configured properly, pods can fail to start. You can check pod network status and the configuration to help you solve a couple common scenarios.

[id="Pod-networking-cannot-be-configured_{context}"]
== Pod networking cannot be configured

If the Multus CNI plugin cannot apply networking annotations to a pod, the pod does not start. Pods can also fail to start if any of the additional network CNIs fail.

.Example error
[source,terminal]
----
Warning  NoNetworkFound     0s     multus    cannot find a network-attachment-definitio (asdasd) in namespace (default): network-attachment-definitions.k8s.cni.cncf.io "bad-ref-doesnt-exist" not found
----

In this case, you can take the following steps to trouble CNI failures:

* Verify the values in both the `NetworkAttachmentDefinitions` and the annotations.
* Remove the annotation to verify whether the pod is created successfully with just the default network. If not, this might indicate a networking problem other than the Multus configuration.
* If you are a device administrator, you can inspect the `crio.service` or `microshift.service` logs, paying special attention to those that are generated by the `kubelet`.
+
For example, the following error from the `kubelet` shows that the primary CNI is not running. This situation can be caused by pods not starting or because of a CRI-O misconfiguration such as an incorrect `cni_default_network` setting.
+
.Example kubelet-generated error
[source,terminal]
----
Feb 06 13:47:31 dev microshift[1494]: kubelet E0206 13:47:31.163290    1494 pod_workers.go:1298] "Error syncing pod, skipping" err="network is not ready: container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: No CNI configuration file in /etc/cni/net.d/. Has your network provider started?" pod="default/samplepod" podUID="fe0f7f7a-8c47-4488-952b-8abc0d8e2602"
----

[id="missing-nad_{context}"]
== Missing configuration file

Sometimes a pod cannot be created because the annotations reference a `NetworkAttachmentDefinition` configuration YAML that does not exist. In this case an error such as the following is usually produced:

.Example log
[source,terminal]
----
cannot find a network-attachment-definition (bad-conf) in namespace (default): network-attachment-definitions.k8s.cni.cncf.io "bad-conf" not found" pod="default/samplepod"`
----
.Example error output
[source,terminal]
----
"CreatePodSandbox for pod failed" err="rpc error: code = Unknown desc = failed to create pod network sandbox k8s_samplepod_default_5fa13105-1bfb-4c6b-aee7-3437cfb50e25_0(7517818bd8e85f07b551f749c7529be88b4e7daef0dd572d049aa636950c76c6): error adding pod default_samplepod to CNI network \"multus-cni-network\": plugin type=\"multus\" name=\"multus-cni-network\" failed (add): Multus: [default/samplepod/5fa13105-1bfb-4c6b-aee7-3437cfb50e25]: error loading k8s delegates k8s args: TryLoadPodDelegates: error in getting k8s network for pod: GetNetworkDelegates: failed getting the delegate: getKubernetesDelegate: cannot find a network-attachment-definition (bad-conf) in namespace (default): network-attachment-definitions.k8s.cni.cncf.io \"bad-conf\" not found" pod="default/samplepod"
----

To fix this error, create and apply the `NetworkAttachmentDefinitions` YAML.

[id="additional-resources_microshift-cni-multus-using_{context}"]
== Additional resources
* About using multiple networks

* Configuration of IP address assignment for a network attachment
