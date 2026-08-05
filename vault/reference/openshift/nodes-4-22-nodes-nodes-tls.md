---
title: "Enabling TLS security profiles for the kubelet"
type: reference
domain: openshift
slug: nodes-4-22-nodes-nodes-tls
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-nodes-tls
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Enabling TLS security profiles for the kubelet

[id="nodes-nodes-tls"]
= Enabling TLS security profiles for the kubelet

You can use a TLS (Transport Layer Security) security profile to define which TLS ciphers are required by the kubelet when it is acting as an HTTP server. The kubelet uses its HTTP/GRPC server to communicate with the Kubernetes API server, which sends commands to pods, gathers logs, and run exec commands on pods through the kubelet.

A TLS security profile defines the TLS ciphers that the Kubernetes API server must use when connecting with the kubelet to protect communication between the kubelet and the Kubernetes API server.

[NOTE]
====
By default, when the kubelet acts as a client with the Kubernetes API server, it automatically negotiates the TLS parameters with the API server.
====

// Module included in the following assemblies:
//
// * security/tls-security-profiles.adoc

[id="tls-profiles-understanding_{context}"]
= Understanding TLS security profiles

[role="_abstract"]
You can use a TLS (Transport Layer Security) security profile, as described in this section, to define which TLS ciphers are required by various OpenShift Container Platform components.

The OpenShift Container Platform TLS security profiles are based on Mozilla recommended configurations.

You can specify one of the following TLS security profiles for each component:

.TLS security profiles
[cols="1,2a",options="header"]
|===
|Profile
|Description

|`Old`
|This profile is intended for use with legacy clients or libraries. The profile is based on the Old backward compatibility recommended configuration.

The `Old` profile requires a minimum TLS version of 1.0.

[NOTE]
====
For the Ingress Controller, the minimum TLS version is converted from 1.0 to 1.1.
====

|`Intermediate`
|This profile is the default TLS security profile for the Ingress Controller, kubelet, and control plane. The profile is based on the Intermediate compatibility recommended configuration.

The `Intermediate` profile requires a minimum TLS version of 1.2.

[NOTE]
====
This profile is the recommended configuration for the majority of clients.
====

|`Modern`
|This profile is intended for use with modern clients that have no need for backwards compatibility. This profile is based on the Modern compatibility recommended configuration.

The `Modern` profile requires a minimum TLS version of 1.3.

|`Custom`
|This profile allows you to define the TLS version and ciphers to use.

[WARNING]
====
Use caution when using a `Custom` profile, because invalid configurations can cause problems.
====
|===

[NOTE]
====
When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout.
====

// TODO: Make sure all this is captured somewhere as necessary
// [IMPORTANT]
// ====
// The HAProxy Ingress Controller image does not support TLS `1.3` and because the `Modern` profile requires TLS `1.3`, it is not supported. The Ingress Operator converts the `Modern` profile to `Intermediate`.
//
// The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`, and TLS `1.3` of a `Custom` profile to `1.2`.
// ====

// Module included in the following assemblies:
//
// * security/tls-profiles.adoc
// * nodes/nodes/nodes-nodes-tls.adoc

[id="tls-profiles-kubelet-configuring_{context}"]
= Configuring the TLS security profile for the kubelet

[role="_abstract"]
You can configure a TLS security profile for the kubelet when it is acting as an HTTP server by creating a `KubeletConfig` custom resource (CR) to specify a predefined or custom TLS security profile for specific nodes.

If a TLS security profile is not configured, the default TLS security profile, `Intermediate`, is used.

The kubelet uses its HTTP/GRPC server to communicate with the Kubernetes API server, which sends commands to pods, gathers logs, and run exec commands on pods through the kubelet.

.Sample `KubeletConfig` CR that configures the `Old` TLS security profile on worker nodes
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
# ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
# ...
----

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `kubelet.conf` file on a configured node.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Create a `KubeletConfig` CR to configure the TLS security profile:
+
.Sample `KubeletConfig` CR for a `Custom` profile
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: set-kubelet-tls-security-profile
spec:
  tlsSecurityProfile:
    type: Custom
    custom:
      ciphers:
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
#...
----
where:

`spec.tlsSecurityProfile.type`:: Specifies the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.
`spec.tlsSecurityProfile.type.custom`:: Specifies the appropriate field for the selected type:
+
--
* `old: {}`
* `intermediate: {}`
* `modern: {}`
* `custom:`
--
`spec.tlsSecurityProfile.type.custom`:: For the `custom` type, specifies a list of TLS ciphers and the minimum accepted TLS version.
`spec.machineConfigPoolSelector.matchLabels.custom`:: Specifies the machine config pool label for the nodes you want to apply the TLS security profile. This parameter is optional.

. Create the `KubeletConfig` object:
+
[source,terminal]
----
$ oc create -f <filename>
----
+
Depending on the number of worker nodes in the cluster, wait for the configured nodes to be rebooted one by one.

.Verification

To verify that the profile is set,  perform the following steps after the nodes are in the `Ready` state:

. Start a debug session for a configured node:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Set `/host` as the root directory within the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. View the `kubelet.conf` file:
+
[source,terminal]
----
sh-4.4# cat /etc/kubernetes/kubelet.conf
----
+
.Example output
[source,terminal]
----
  "kind": "KubeletConfiguration",
  "apiVersion": "kubelet.config.k8s.io/v1beta1",
#...
  "tlsCipherSuites": [
    "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
    "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
    "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
    "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
    "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256"
  ],
  "tlsMinVersion": "VersionTLS12",
#...
----
