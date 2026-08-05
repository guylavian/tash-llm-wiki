---
title: "Configuring IPv6 single or dual-stack networking"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-nw-ipv6-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-nw-ipv6-config
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Configuring IPv6 single or dual-stack networking

[id="microshift-nw-ipv6-config"]
= Configuring IPv6 single or dual-stack networking

[role="_abstract"]
You can use the IPv6 networking protocol in either single-stack or dual-stack networking modes.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-nw-ipv6-config.adoc

[id="microshift-intro-ipv6_{context}"]
= IPv6 networking with {microshift-short}

[role="_abstract"]
The OpenShift Container Platform service defaults to IPv4. IPv6 single-stack and IPv4/IPv6 dual-stack networking is available on supported platforms. You configure IPv6 or dual-stack networking in the configuration file.

Consider the following when configuring IPv6 or dual-stack networking with {microshift-short}:

* When you set the values for IPv6 in the {microshift-short} configuration file and restart the service, settings managed by the OVN-Kubernetes network plugin are updated automatically.

* After migrating to dual-stack networking, both new and existing pods have dual-stack networking enabled.

* If you require node-wide IPv6 access, such as for the control plane and other services, use the following configuration examples. The {microshift-short} Multus Container Network Interface (CNI) plugin can enable IPv6 for pods.

* For dual-stack networking, each {microshift-short} node network and service network supports up to two values in the node and service network configuration parameters.

[IMPORTANT]
====
Plan for IPv6 before starting {microshift-short} for the first time. Switching a node to and from different IP families is not supported unless you are migrating a node from default single-stack to dual-stack networking.

If you configure your networking for either IPv6 single stack or IPv4/IPv6 dual stack, you must restart application pods and services. Otherwise pods and services remain configured with the default IP family.
====

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-nw-ipv6-config.adoc

[id="microshift-configuring-ipv6-single-stack-config_{context}"]
= Configuring IPv6 single-stack networking

[role="_abstract"]
To run {microshift-short} with IPv6-only networking, you can update the service configuration file and set the network section with your cluster and service CIDRs. You can verify the configuration by checking that pods and services use IPv6 addresses.

.Prerequisites

* You installed the {oc-first}.
* You have root access to the node.
* Your node uses the OVN-Kubernetes network plugin.
* The host has an IPv6 address and IPv6 routes, including the default.

.Procedure

. If you have not done so, make a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, renaming it `config.yaml`.

. Keep the new {microshift-short} `config.yaml` in the `/etc/microshift/` directory. Your `config.yaml` file is read every time the {microshift-short} service starts.
+
[NOTE]
====
After you create it, the `config.yaml` file takes precedence over built-in settings.
====

. Replace the default values in the `network` section of the {microshift-short} YAML with your valid values.
+
.Example single-stack IPv6 networking configuration
[source,yaml]
----
apiServer:
# ...
network:
  clusterNetwork:
  - fd01::/48
  serviceNetwork:
  - fd02::/112
node:
  nodeIP: 2600:1f14:1c48:ee00:2d76:3190:5bc2:5aef
# ...
----
+
where:
+
--
`networking.clusterNetwork`:: Specifies a `clusterNetwork` address with a CIDR value that is less than `64`. For example, `fd01::/48`.
`network.serviceNetwork`:: Specifies an IPv6 CIDR with a prefix of `112`, for example, `fd02::/112`. Kubernetes uses only the lowest 16 bits. For a prefix of `112`, IP addresses are assigned from `112` to `128` bits.
`node.nodeIP`:: Specifies a node IP address. Valid values are IP addresses in the IPv6 address family. You must only specify an IPv6 address when an IPv4 network is also present. If an IPv4 network is not present, the {microshift-short} service automatically fills in this value upon restart.
--

. Complete any other configurations you require, then start {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----

.Verification

. Retrieve the networks defined in the node resource by running the following command:
+
[source,terminal]
----
$ oc get node -o jsonpath='{.items[].spec.podCIDRs[]}'
----
+
.Example output
[source,text]
----
fd01::/48
----

. Retrieve the status of the pods by running the following command:
+
[source,terminal]
----
$ oc get pod -A -o wide
----
+
.Example output
[source,text]
----
NAMESPACE                  NAME                                      READY   STATUS    RESTARTS   AGE   IP                      NODE           NOMINATED NODE   READINESS GATES
kube-system                csi-snapshot-controller-bb7cb654b-rqrt6   1/1     Running   0          65s   fd01:0:0:1::5           microshift-9   <none>           <none>
openshift-dns              dns-default-cjn66                         2/2     Running   0          62s   fd01:0:0:1::9           microshift-9   <none>           <none>
openshift-dns              node-resolver-ppnjb                       1/1     Running   0          63s   2001:db9:ca7:ff::1db8   microshift-9   <none>           <none>
openshift-ingress          router-default-6d97d7b8b6-wdtmg           1/1     Running   0          61s   fd01:0:0:1::8           microshift-9   <none>           <none>
openshift-ovn-kubernetes   ovnkube-master-gfvp5                      4/4     Running   0          63s   2001:db9:ca7:ff::1db8   microshift-9   <none>           <none>
openshift-ovn-kubernetes   ovnkube-node-bnpjh                        1/1     Running   0          63s   2001:db9:ca7:ff::1db8   microshift-9   <none>           <none>
openshift-service-ca       service-ca-5d7bd9db6-j25bd                1/1     Running   0          60s   fd01:0:0:1::4           microshift-9   <none>           <none>
openshift-storage          lvms-operator-656cd9b59b-bwr47            1/1     Running   0          63s   fd01:0:0:1::7           microshift-9   <none>           <none>
openshift-storage          vg-manager-f7dmk                          1/1     Running   0          27s   fd01:0:0:1::a           microshift-9   <none>           <none>
----

. Retrieve the status of services by running the following command:
+
[source,terminal]
----
$ oc get svc -A
----
+
.Example output
[source,text]
----
NAMESPACE           NAME                            TYPE           CLUSTER-IP   EXTERNAL-IP                                             PORT(S)                      AGE
default             kubernetes                      ClusterIP      fd02::1      <none>                                                  443/TCP                      3m42s
openshift-dns       dns-default                     ClusterIP      fd02::a      <none>                                                  53/UDP,53/TCP,9154/TCP       2m58s
openshift-ingress   router-default                  LoadBalancer   fd02::f2e6   2001:db9:ca7:ff::1db8,fd01:0:0:1::2,fd02::1:0,fd69::2   80:31133/TCP,443:31996/TCP   2m58s
openshift-ingress   router-internal-default         ClusterIP      fd02::c55e   <none>                                                  80/TCP,443/TCP,1936/TCP      2m58s
openshift-storage   lvms-operator-metrics-service   ClusterIP      fd02::7afb   <none>                                                  443/TCP                      2m58s
openshift-storage   lvms-webhook-service            ClusterIP      fd02::d8dd   <none>                                                  443/TCP                      2m58s
openshift-storage   vg-manager-metrics-service      ClusterIP      fd02::fc1    <none>                                                  443/TCP                      2m58s
----

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-nw-ipv6-config.adoc

[id="microshift-configuring-ipv6-dual-stack-config_{context}"]
= Configuring IPv6 dual-stack networking before {microshift-short} starts

[role="_abstract"]
To run your {microshift-short} node with IPv4 and IPv6 dual-stack networking, you can configure the network section in the configuration file before starting the service.

* The first IP family in the configuration is the primary IP stack in the node.
* After the node is running with dual-stack networking, enable application pods and add-on services for dual-stack by restarting them.

[IMPORTANT]
====
The OVN-Kubernetes network plugin requires that both IPv4 and IPv6 default routes be on the same network device. IPv4 and IPv6 default routes on separate network devices is not supported.
====

[IMPORTANT]
====
When using dual-stack networking where IPv6 is required, you cannot use IPv4-mapped IPv6 addresses, such as `::FFFF:198.51.100.1`.
====

.Prerequisites

* You installed the {oc-first}.
* You have root access to the node.
* Your node uses the OVN-Kubernetes network plugin.
* The host has both IPv4 and IPv6 addresses and routes, including a default for each.
* The host has at least two L3 networks, IPv4 and IPv6.

.Procedure

. If you have not done so, make a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, renaming it `config.yaml`.

. Keep the new {microshift-short} `config.yaml` in the `/etc/microshift/` directory. Your `config.yaml` file is read every time the {microshift-short} service starts.
+
[NOTE]
====
After you create it, the `config.yaml` file takes precedence over built-in settings.
====

. If you have not started {microshift-short}, replace the default values in the `network` section of the {microshift-short} YAML with your valid values.
+
.Example dual-stack IPv6 networking configuration with network assignments
[source,yaml]
----
apiServer:
# ...
apiServer:
  subjectAltNames:
  - 192.168.113.117
  - 2001:db9:ca7:ff::1db8
network:
  clusterNetwork:
  - 10.42.0.0/16
  - fd01::/48
  serviceNetwork:
  - 10.43.0.0/16
  - fd02::/112
node:
  nodeIP: 192.168.113.117
  nodeIPv6: 2001:db9:ca7:ff::1db8
# ...
----
+
where:
+
--
`network.clusterNetwork`:: Specifies an IPv6 `clusterNetwork` with a CIDR value that is less than `64`.
`network.serviceNetwork`:: Specifies an IPv6 CIDR with a prefix of `112`. Kubernetes uses only the lowest 16 bits. For a prefix of `112`, IP addresses are assigned from `112` to `128` bits.
`node.nodeIP`:: Specifies an IPv4 address family.
`node.nodeIPv6`:: Specifies an IPv6 address family. Configurable only with dual-stack networking.
--

. Complete any other {microshift-short} configurations you require, then start {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----

. Reset the IP family policy for application pods and services as needed, then restart those application pods and services to enable dual-stack networking. See "Resetting the IP family policy for application pods and services" for a simple example.

.Verification

. You can verify that all of the system services and pods to have two IP addresses, one for each family, by using the following steps:

.. Retrieve the networks defined in the node resource by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ingress router-default-5b75594b4-w7w6s -o jsonpath='{.status.podIPs}'
----
+
.Example output
[source,text]
----
[{"ip":"10.42.0.4"},{"ip":"fd01:0:0:1::4"}]
----

.. Retrieve the networks defined by the host network pods by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ovn-kubernetes ovnkube-master-2fm2k -o jsonpath='{.status.podIPs}'
----
+
.Example output
[source,terminal]
----
[{"ip":"192.168.113.117"},{"ip":"2001:db9:ca7:ff::1db8"}]
----

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-nw-ipv6-config.adoc

[id="microshift-nw-ipv6-dual-stack-migrating-config_{context}"]
= Migrating a {microshift-short} node to IPv6 dual-stack networking

[role="_abstract"]
To convert a single-stack node to dual-stack node networking that supports IPv4 and IPv6 address families, set two entries in the service and node network parameters in the {microshift-short} configuration file and restart the service.

* The first IP family in the configuration is the primary IP stack in the node.
* {microshift-short} system pods and services are automatically updated upon {microshift-short} restart.
* After the node is migrated to dual-stack networking and has restarted, enable workload pods and services for dual-stack networking by restarting them.

[IMPORTANT]
====
The OVN-Kubernetes network plugin requires that both IPv4 and IPv6 default routes be on the same network device. IPv4 and IPv6 default routes on separate network devices is not supported.
====

[IMPORTANT]
====
When using dual-stack networking where IPv6 is required, you cannot use IPv4-mapped IPv6 addresses, such as `::FFFF:198.51.100.1`.
====

.Prerequisites

* You installed the {oc-first}.
* You have root access to the node.
* Your node uses the OVN-Kubernetes network plugin.
* The host has both IPv4 and IPv6 addresses and routes, including a default for each.
* The host has at least two L3 networks, IPv4 and IPv6.

.Procedure

. If you have not done so, make a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, renaming it `config.yaml`.

. Keep the new {microshift-short} `config.yaml` in the `/etc/microshift/` directory. Your `config.yaml` file is read every time the {microshift-short} service starts.
+
[NOTE]
====
After you create it, the `config.yaml` file takes precedence over built-in settings.
====

. Add IPv6 configurations to the `network` section of the {microshift-short} YAML with your valid values:
+
[WARNING]
====
You must keep the same first entry across restarts and migrations. This is true for any migration: single-to-dual stack, or dual-to-single stack. A complete wipe of the etcd database is required if a change to the first entry is needed. This might result in application data loss and is not supported.
====
+
.. Add an IPv6 configuration for a second network in the `network` section of the {microshift-short} YAML with your valid values.

.. Add network assignments to the `network` section of the {microshift-short} `config.yaml` to enable dual stack with IPv6 as secondary network.
+
.Example dual-stack IPv6 configuration with network assignments
[source,yaml]
----
# ...
apiServer:
  subjectAltNames:
  - 192.168.113.117
  - 2001:db9:ca7:ff::1db8
network:
  clusterNetwork:
  - 10.42.0.0/16
  - fd01::/48
  serviceNetwork:
  - 10.43.0.0/16
  - fd02::/112
node:
  nodeIP: 192.168.113.117
  nodeIPv6: 2001:db9:ca7:ff::1db8
# ...
----
+
where:
+
--
`2001:db9:ca7:ff::1db8`:: Specifies an IPv6 node address.
`10.42.0.0/16`:: Specifies an IPv4 `clusterNetwork` address with a CIDR value that is less than `24`.
`fd01::/48`:: Specifies an IPv6 `clusterNetwork` address with a CIDR value that is less than `64`.
`fd02::/112`:: Specifies an IPv6 CIDR with a prefix of `112`. Kubernetes uses only the lowest 16 bits. For a prefix of `112`, IP addresses are assigned from `112` to `128` bits.
`192.168.113.117`:: Specifies an IPv4 node IP address. Maintain the previous IPv4 IP address.
`2001:db9:ca7:ff::1db8`:: Specifies an IPv6 node IP address. Must be an IPv6 address family.
--

. Complete any other configurations you require, then restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

. Reset the IP family policy for application pods and services as needed, then restart those application pods and services to enable dual-stack networking. See "Resetting the IP family policy for application pods and services" for a simple example.

.Verification

You can verify that all of the system services and pods to have two IP addresses, one for each family, by using the following steps:

. Retrieve the status of the pods by running the following command:
+
[source,terminal]
----
$ oc get pod -A -o wide
----
+
.Example output
[source,text]
----
NAMESPACE                  NAME                                      READY   STATUS    RESTARTS        AGE     IP                NODE           NOMINATED NODE   READINESS GATES
kube-system                csi-snapshot-controller-bb7cb654b-7s5ql   1/1     Running   0               46m     10.42.0.6         microshift-9   <none>           <none>
openshift-dns              dns-default-zxkqn                         2/2     Running   0               46m     10.42.0.5         microshift-9   <none>           <none>
openshift-dns              node-resolver-r2h5z                       1/1     Running   0               46m     192.168.113.117   microshift-9   <none>           <none>
openshift-ingress          router-default-5b75594b4-228z7            1/1     Running   0               2m5s    10.42.0.3         microshift-9   <none>           <none>
openshift-ovn-kubernetes   ovnkube-master-bltk7                      4/4     Running   2 (2m32s ago)   2m36s   192.168.113.117   microshift-9   <none>           <none>
openshift-ovn-kubernetes   ovnkube-node-9ghgs                        1/1     Running   2 (2m32s ago)   46m     192.168.113.117   microshift-9   <none>           <none>
openshift-service-ca       service-ca-5d7bd9db6-qgwgw                1/1     Running   0               46m     10.42.0.7         microshift-9   <none>           <none>
openshift-storage          lvms-operator-656cd9b59b-8rpf4            1/1     Running   0               46m     10.42.0.8         microshift-9   <none>           <none>
openshift-storage          vg-manager-wqmh4                          1/1     Running   2 (2m39s ago)   46m     10.42.0.10        microshift-9   <none>           <none>
----

. Retrieve the networks defined by the OVN-K network plugin by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ovn-kubernetes ovnkube-master-bltk7 -o jsonpath='{.status.podIPs}'
----
+
.Example output
[source,text]
----
[{"ip":"192.168.113.117"},{"ip":"2001:db9:ca7:ff::1db8"}]
----

. Retrieve the networks defined in the node resource by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ingress router-default-5b75594b4-228z7 -o jsonpath='{.status.podIPs}'
----
+
.Example output
[source,text]
----
[{"ip":"10.42.0.3"},{"ip":"fd01:0:0:1::3"}]
----
+
[NOTE]
====
To return to single-stack networking, you can remove the second entry to the networks and return to the single stack that was configured before migrating to dual-stack.
====

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-nw-ipv6-config.adoc

[id="microshift-nw-ipv6-dual-stack-reset-ipfam_{context}"]
= Resetting the IP family policy for application pods and services

[role="_abstract"]
The default `PreferSingleStack` value does not change when you migrate the {microshift-short} node to dual-stack.
To enable dual-stack networking in application pods and services on a node that uses dual-stack, set the `ipFamilyPolicy` field to `PreferDualStack` or `RequireDualStack` and restart the pods.

.Prerequisites

* You used the {microshift-short} `config.yaml` to define a dual-stack network with an IPv6 address family.

.Procedure

. Set the `spec.ipFamilyPolicy` field to a valid value for dual-stack networking in your service or pod by using the following example:
+
.Example dual-stack network configuration for a service
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  name: microshift-new-service
  labels: app: microshift-application
spec:
  type: NodePort
  ipFamilyPolicy: PreferDualStack
# ...
----
+
where:

`spec.ipFamilyPolicy`:: Required. Specifies the IP family policy for the service. Valid values are `PreferDualStack` and `RequireDualStack`. The value you set depends on the requirements of your application. `PreferSingleStack` is the default value for the `ipFamilyPolicy` field.

. Restart any application pods that do not have a `hostNetwork` defined. Pods that do have a `hostNetwork` defined do not need to be restarted to update the `ipFamilyPolicy` value.
+
[NOTE]
====
{microshift-short} system services and pods are automatically updated when the `ipFamilyPolicy` value is updated.
====

//OCP module, edit with conditionals and care
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.adoc
// * microshift_networking/microshift-nw-ipv6-config.adoc

[id="nw-ovn-kubernetes-limitations_{context}"]
= OVN-Kubernetes IPv6 and dual-stack limitations

[role="_abstract"]
The OVN-Kubernetes network plugin has specific IPv6 and dual-stack networking configuration limitations. These limitations affect gateway configuration, routing layouts, and infrastructure environment stability.

// The following limitation is also recorded in the installation section.
* For clusters configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway.
* For a cluster configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway.
+
If this requirement is not met, pods on the host in the `ovnkube-node` daemon set enter the `CrashLoopBackOff` state.
+
If you display a pod with a command such as `oc get pod -n openshift-ovn-kubernetes -l app=ovnkube-node -o yaml`, the `status` field has more than one message about the default gateway, as shown in the following output:
+
[source,terminal]
----
I1006 16:09:50.985852   60651 helper_linux.go:73] Found default gateway interface br-ex 192.168.127.1
I1006 16:09:50.985923   60651 helper_linux.go:73] Found default gateway interface ens4 fe80::5054:ff:febe:bcd4
F1006 16:09:50.985939   60651 ovnkube.go:130] multiple gateway interfaces detected: br-ex ens4
----
+
The only resolution is to reconfigure the host networking so that both IP families use the same network interface for the default gateway.
* For clusters configured for dual-stack networking, both the IPv4 and IPv6 routing tables must contain the default gateway.
* For a cluster configured for dual-stack networking, both the IPv4 and IPv6 routing tables must contain the default gateway.
+
If this requirement is not met, pods on the host in the `ovnkube-node` daemon set enter the `CrashLoopBackOff` state.
+
If you display a pod with a command such as `oc get pod -n openshift-ovn-kubernetes -l app=ovnkube-node -o yaml`, the `status` field has more than one message about the default gateway, as shown in the following output:
+
[source,terminal]
----
I0512 19:07:17.589083  108432 helper_linux.go:74] Found default gateway interface br-ex 192.168.123.1
F0512 19:07:17.589141  108432 ovnkube.go:133] failed to get default gateway interface
----
+
The only resolution is to reconfigure the host networking so that both IP families contain the default gateway.

* If you set the `ipv6.disable` parameter to `1` in the `kernelArgument` section of the `MachineConfig` custom resource (CR) for your cluster, OVN-Kubernetes pods enter a `CrashLoopBackOff` state. Additionally, updating your cluster to a later version of OpenShift Container Platform fails because the Network Operator remains on a `Degraded` state. Red{nbsp}Hat does not support disabling IPv6 addresses for your cluster so do not set the `ipv6.disable` parameter to `1`.

[id="additional-resources_microshift-ipv6-config_{context}"]
[role="_additional-resources"]
== Additional resources

* Using NetworkManager to disable IPv6 for a specific connection (Red Hat Enterprise Linux documentation)
