---
title: "Configuring TLS security profiles"
type: reference
domain: openshift
slug: security-4-22-tls-security-profiles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/tls-security-profiles
version: 4.22
family: security
documentKind: "Documentation"
---

# Configuring TLS security profiles

[id="tls-security-profiles"]
= Configuring TLS security profiles

TLS security profiles provide a way for servers to regulate which ciphers a client can use when connecting to the server. This ensures that OpenShift Container Platform components use cryptographic libraries that do not allow known insecure protocols, ciphers, or algorithms.

Cluster administrators can choose which TLS security profile to use for each of the following components:

* the Ingress Controller
* the control plane
+
This includes the Kubernetes API server, Kubernetes controller manager, Kubernetes scheduler, OpenShift API server, OpenShift OAuth API server, OpenShift OAuth server, etcd, the Machine Config Operator, and the Machine Config Server.
+
// NOTE: OpenShift controller manager are not included

* the kubelet, when it acts as an HTTP server for the Kubernetes API server

// Understanding TLS security profiles
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

// Viewing TLS security profile details
// Module included in the following assemblies:
//
// * security/tls-security-profiles.adoc

[id="tls-profiles-view-details_{context}"]
= Viewing TLS security profile details

You can view the minimum TLS version and ciphers for the predefined TLS security profiles for each of the following components: Ingress Controller, control plane, and kubelet.

[IMPORTANT]
====
The effective configuration of minimum TLS version and list of ciphers for a profile might differ between components.
====

.Procedure

* View details for a specific TLS security profile:
+
[source,terminal]
----
$ oc explain <component>.spec.tlsSecurityProfile.<profile> <1>
----
<1> For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`. For `<profile>`, specify `old`, `intermediate`, or `custom`.
+
For example, to check the ciphers included for the `intermediate` profile for the control plane:
+
[source,terminal]
----
$ oc explain apiserver.spec.tlsSecurityProfile.intermediate
----
+
.Example output
[source,terminal]
----
KIND:     APIServer
VERSION:  config.openshift.io/v1

DESCRIPTION:
    intermediate is a TLS security profile based on:
    https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
    and looks like this (yaml):
    ciphers: - TLS_AES_128_GCM_SHA256 - TLS_AES_256_GCM_SHA384 -
    TLS_CHACHA20_POLY1305_SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 -
    ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 -
    ECDHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-CHACHA20-POLY1305 -
    ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-AES128-GCM-SHA256 -
    DHE-RSA-AES256-GCM-SHA384 minTLSVersion: TLSv1.2
----

* View all details for the `tlsSecurityProfile` field of a component:
+
[source,terminal]
----
$ oc explain <component>.spec.tlsSecurityProfile <1>
----
<1> For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`.
+
For example, to check all details for the `tlsSecurityProfile` field for the Ingress Controller:
+
[source,terminal]
----
$ oc explain ingresscontroller.spec.tlsSecurityProfile
----
+
.Example output
[source,terminal]
----
KIND:     IngressController
VERSION:  operator.openshift.io/v1

RESOURCE: tlsSecurityProfile <Object>

DESCRIPTION:
     ...

FIELDS:
   custom	<>
     custom is a user-defined TLS security profile. Be extremely careful using a
     custom profile as invalid configurations can be catastrophic. An example
     custom profile looks like this:
     ciphers: - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 -
     ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 minTLSVersion:
     TLSv1.1

   intermediate	<>
     intermediate is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
     and looks like this (yaml):
     ... <1>

   modern	<>
     modern is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility and
     looks like this (yaml):
     ... <2>
     NOTE: Currently unsupported.

   old	<>
     old is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility
     and looks like this (yaml):
     ... <3>

   type	<string>
     ...
----
<1> Lists ciphers and minimum version for the `intermediate` profile here.
<2> Lists ciphers and minimum version for the `modern` profile here.
<3> Lists ciphers and minimum version for the `old` profile here.

// Configuring for ingress
// Module included in the following assemblies:
//
// * security/tls-profiles.adoc

[id="tls-profiles-ingress-configuring_{context}"]
= Configuring the TLS security profile for the Ingress Controller

To configure a TLS security profile for an Ingress Controller, edit the `IngressController` custom resource (CR) to specify a predefined or custom TLS security profile. If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server.

.Sample `IngressController` CR that configures the `Old` TLS security profile
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
----

The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for Ingress Controllers.

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `IngressController` custom resource (CR) under `Status.Tls Profile` and the configured TLS security profile under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed under both parameters.

[NOTE]
====
The HAProxy Ingress Controller image supports TLS `1.3` and the `Modern` profile.

The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `IngressController` CR in the `openshift-ingress-operator` project to configure the TLS security profile:
+
[source,terminal]
----
$ oc edit IngressController default -n openshift-ingress-operator
----

. Add the `spec.tlsSecurityProfile` field:
+
.Sample `IngressController` CR for a `Custom` profile
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    type: Custom <1>
    custom: <2>
      ciphers: <3>
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
 ...
----
<1> Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.
<2> Specify the appropriate field for the selected type:
* `old: {}`
* `intermediate: {}`
* `modern: {}`
* `custom:`
<3> For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

. Save the file to apply the changes.

.Verification

* Verify that the profile is set in the `IngressController` CR:
+
[source,terminal]
----
$ oc describe IngressController default -n openshift-ingress-operator
----
+
.Example output
[source,terminal]
----
Name:         default
Namespace:    openshift-ingress-operator
Labels:       <none>
Annotations:  <none>
API Version:  operator.openshift.io/v1
Kind:         IngressController
 ...
Spec:
 ...
  Tls Security Profile:
    Custom:
      Ciphers:
        ECDHE-ECDSA-CHACHA20-POLY1305
        ECDHE-RSA-CHACHA20-POLY1305
        ECDHE-RSA-AES128-GCM-SHA256
        ECDHE-ECDSA-AES128-GCM-SHA256
      Min TLS Version:  VersionTLS11
    Type:               Custom
 ...
----

// Configuring for the control plane
// Module included in the following assemblies:
//
// * security/tls-profiles.adoc

[id="tls-profiles-kubernetes-configuring_{context}"]
= Configuring the TLS security profile for the control plane

To configure a TLS security profile for the control plane, edit the `APIServer` custom resource (CR) to specify a predefined or custom TLS security profile. Setting the TLS security profile in the `APIServer` CR propagates the setting to the following control plane components:

* Kubernetes API server
* Kubernetes controller manager
* Kubernetes scheduler
* OpenShift API server
* OpenShift OAuth API server
* OpenShift OAuth server
* etcd
* Machine Config Operator
* Machine Config Server

If a TLS security profile is not configured, the default TLS security profile is `Intermediate`.

[NOTE]
====
The default TLS security profile for the Ingress Controller is based on the TLS security profile set for the API server.
====

.Sample `APIServer` CR that configures the `Old` TLS security profile
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: APIServer
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
----

The TLS security profile defines the minimum TLS version and the TLS ciphers required to communicate with the control plane components.

You can see the configured TLS security profile in the `APIServer` custom resource (CR) under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the default `APIServer` CR to configure the TLS security profile:
+
[source,terminal]
----
$ oc edit APIServer cluster
----

. Add the `spec.tlsSecurityProfile` field:
+
.Sample `APIServer` CR for a `Custom` profile
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  tlsSecurityProfile:
    type: Custom <1>
    custom: <2>
      ciphers: <3>
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
----
<1> Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.
<2> Specify the appropriate field for the selected type:
* `old: {}`
* `intermediate: {}`
* `modern: {}`
* `custom:`
<3> For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

. Save the file to apply the changes.

.Verification

* Verify that the TLS security profile is set in the `APIServer` CR:
+
[source,terminal]
----
$ oc describe apiserver cluster
----
+
.Example output
[source,terminal]
----
Name:         cluster
Namespace:
 ...
API Version:  config.openshift.io/v1
Kind:         APIServer
 ...
Spec:
  Audit:
    Profile:  Default
  Tls Security Profile:
    Custom:
      Ciphers:
        ECDHE-ECDSA-CHACHA20-POLY1305
        ECDHE-RSA-CHACHA20-POLY1305
        ECDHE-RSA-AES128-GCM-SHA256
        ECDHE-ECDSA-AES128-GCM-SHA256
      Min TLS Version:  VersionTLS11
    Type:               Custom
 ...
----
.Verification

* Verify that the TLS security profile is set in the `etcd` CR:
+
[source,terminal]
----
$ oc describe etcd cluster
----
+
.Example output
[source,terminal]
----
Name:         cluster
Namespace:
 ...
API Version:  operator.openshift.io/v1
Kind:         Etcd
 ...
Spec:
  Log Level:         Normal
  Management State:  Managed
  Observed Config:
    Serving Info:
      Cipher Suites:
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
        TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
      Min TLS Version:           VersionTLS12
 ...
----

* Verify that the TLS security profile is set in the Machine Config Server pod:
+
[source,terminal]
----
$ oc logs machine-config-server-5msdv -n openshift-machine-config-operator
----
+
.Example output
[source,terminal]
----
# ...
I0905 13:48:36.968688       1 start.go:51] Launching server with tls min version: VersionTLS12 & cipher suites [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256]
# ...
----

// Configuring for kubelet
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
