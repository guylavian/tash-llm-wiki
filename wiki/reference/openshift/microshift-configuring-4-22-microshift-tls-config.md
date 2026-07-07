---
title: "Configuring TLS security profiles"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-tls-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-tls-config
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Configuring TLS security profiles

[id="microshift-tls-config"]
= Configuring TLS security profiles

[role="_abstract"]
Use transport layer security (TLS) protocols to help prevent known insecure protocols, ciphers, or algorithms from accessing the applications you run on {microshift-short}.

// Module included in the following assemblies:
//
// * microshift_configurig/microshift_tls-config.adoc

[id="microshift-tls-config-con_{context}"]
= Using TLS with {microshift-short}

[role="_abstract"]
Transport layer security (TLS) profiles provide a way for servers to regulate which ciphers a client can use when connecting to the server. Using TLS helps to ensure that {microshift-short} applications use cryptographic libraries that do not allow known insecure protocols, ciphers, or algorithms. You can use either the TLS 1.2 or TLS 1.3 security profiles with {microshift-short}.

{microshift-short} API server cipher suites apply automatically to the following internal control plane components:

* API server
* Kubelet
* Kube controller manager
* Kube scheduler
* etcd
* Route controller manager

The API server uses the configured minimum TLS version and the associated cipher suites. If you leave the cipher suites parameter empty, the defaults for the configured minimum version are used automatically.

// Module included in the following assemblies:
//
// * microshift_configurig/microshift_tls-config.adoc

[id="microshift-tls-config-proc_{context}"]
= Configuring TLS for {microshift-short}

[role="_abstract"]
You can choose to use either the TLS 1.2 or TLS 1.3 security profiles with {microshift-short} for system hardening.

.Prerequisites

* You have access to the node as a root user.
* {microshift-short} has either not started for the first time, or is stopped.
* The {oc-first} is installed.
* The certificate authority has issued the custom certificates (CAs).

.Procedure

. Make a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, renaming it `config.yaml`.

. Keep the new {microshift-short} `config.yaml` in the `/etc/microshift/` directory. Your `config.yaml` file is read every time the {microshift-short} service starts.
+
[NOTE]
====
After you create it, the `config.yaml` file takes precedence over built-in settings.
====

. Optional: Use a configuration snippet if you are using an existing {microshift-short} YAML. See "Using configuration snippets" in the Additional resources section for more information.

. Replace the default values in the `tls` section of the {microshift-short} YAML with your valid values.
+
.Example TLS 1.2 configuration
[source,yaml]
----
apiServer:
# ...
  tls:
    cipherSuites:
    - <cipher_suite_1>
    - ...
    minVersion: VersionTLS12
# ...
----
+
where:

`apiServer.tls.cipherSuites`:: Defaults to the suites of the configured `minVersion`. If `minVersion` is not configured, the default value is TLS 1.2. You can specify the cipher suites you want to use from the list of supported cipher suites. All clients connecting to the API server must support the configured cipher suites or the connections fail during the TLS handshake phase. Be sure to add the CA certificate bundle to the list of CA certificates that the TLS client or server trusts.
`apiServer.tls.minVersion`:: Specify `VersionTLS12` or `VersionTLS13`.
+
[IMPORTANT]
====
When you choose TLS 1.3 as the minimum TLS version, only the default {microshift-short} cipher suites can be used. Additional cipher suites are not configurable. If other cipher suites to use with TLS 1.3 are configured, those suites are ignored and overwritten by the {microshift-short} defaults.
====

. Complete any other additional configurations that you require, then restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

// Module included in the following assemblies:
//
// * microshift_configurig/microshift_tls-config.adoc

[id="microshift-default-cipher-suites_{context}"]
= Default cipher suites

[role="_abstract"]
Default cipher suites are included with {microshift-short} for both TLS 1.2 and TLS 1.3. The cipher suites for TLS 1.3 cannot be customized.

[id="additional-resources_microshift-tls-config_{context}"]
[role="_additional-resources"]
== Additional resources

* Using configuration snippets
* Pod security authentication and authorization with SCC
* Node access with kubeconfig
* Configuring custom certificate authorities
