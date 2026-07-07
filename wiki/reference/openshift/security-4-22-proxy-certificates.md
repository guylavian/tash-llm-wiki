---
title: "Proxy certificates"
type: reference
domain: openshift
slug: security-4-22-proxy-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/proxy-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# Proxy certificates

// Module included in the following assemblies:
//
// security/certificates_types_descriptions/

[id="proxy-certificates"]
= Proxy certificates

[role="_abstract"]
Proxy certificates allow platform components to trust custom certificate authorities when making egress connections. Understanding proxy certificates helps you configure secure external access for services that require custom certificate authority (CA) trust bundles.

// Proxy cert purpose
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-purpose_{context}"]
= Proxy certificate purpose

[role="_abstract"]
Proxy certificates allow platform components to trust custom certificate authorities when making egress connections. Proxy certificates allow users to specify one or more custom certificate authority (CA) certificates used by platform components when making egress connections.

The `trustedCA` field of the Proxy object is a reference to a config map that contains a user-provided trusted certificate authority (CA) bundle. This bundle is merged with the {op-system-first} trust bundle and injected into the `truststore` of platform components that make egress HTTPS calls. For example, `image-registry-operator` calls an external image registry to download images. If `trustedCA` is not specified, only the {op-system} trust bundle is used for proxied HTTPS connections. Provide custom CA certificates to the {op-system} trust bundle if you want to use your own certificate infrastructure.

The `trustedCA` field should only be consumed by a proxy validator. The validator reads the certificate bundle from the required key `ca-bundle.crt`. The validator copies the bundle to a config map named `user-ca-bundle` in the `openshift-config-managed` namespace.

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-ca-bundle
  namespace: openshift-config
data:
  ca-bundle.crt: |
    -----BEGIN CERTIFICATE-----
    Custom CA certificate bundle.
    -----END CERTIFICATE-----
----

[role="_additional-resources"]
.Additional resources

* Configuring the cluster-wide proxy

// Proxy cert manage install
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-manage-install_{context}"]
= Managing proxy certificates during installation

[role="_abstract"]
Configure proxy-trusted CA certificates during OpenShift Container Platform installation using the `additionalTrustBundle` value in the installation program configuration.

The `additionalTrustBundle` value of the installation program configuration is used to specify any proxy-trusted CA certificates during installation.

.Procedure

. View the installation program configuration file by running the following command:
+
[source,terminal]
----
$ cat install-config.yaml
----
+
.Example output
[source,terminal]
----
...
proxy:
  httpProxy: http://<username:password@proxy.example.com:123/>
  httpsProxy: http://<username:password@proxy.example.com:123/>
  noProxy: <123.example.com,10.88.0.0/16>
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
   <MY_HTTPS_PROXY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
...
----
+
[NOTE]
====
Proxy certificates are managed by the system and not by users.
====

// Proxy location
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-location_{context}"]
= Proxy certificate location

[role="_abstract"]
The user-provided trust bundle is mounted into the file system of platform components that make egress HTTPS calls.

The user-provided trust bundle is represented as a config map. The config map is mounted into the file system of platform components that make egress HTTPS calls. Typically, Operators mount the config map to `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`, but mounting the config map is not required by the proxy. A proxy can modify or inspect the HTTPS connection. In either case, the proxy must generate and sign a new certificate for the connection.

Complete proxy support means connecting to the specified proxy and trusting any signatures the trust bundle has generated. Therefore, it is necessary to let the user specify a trusted root, such that any certificate chain connected to that trusted root is also trusted.

If you use the {op-system} trust bundle, place CA certificates in `/etc/pki/ca-trust/source/anchors`.

[role="_additional-resources"]
.Additional resources

* Using shared system certificates

// Proxy expiration
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-expiration_{context}"]
= Proxy certificate expiration

[role="_abstract"]
The CA administrator configures the expiration term for proxy certificates before they can be used by OpenShift Container Platform or {op-system}.

The user sets the expiration term of the user-provided trust bundle.

The default expiration term is defined by the CA certificate itsself. The CA administrator must configure the default expiration term for the certificate before the certificate can be used by OpenShift Container Platform or {op-system}.

[NOTE]
====
Red Hat does not monitor when CAs expire. Due to the long life of the CAs, this is generally not an issue. However, you might need to periodically update the trust bundle.
====

// Proxy services
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-services_{context}"]
= Services using proxy certificates

[role="_abstract"]
Platform components and services running on {op-system} nodes can use proxy certificates to establish trusted egress HTTPS connections.

By default, all platform components that make egress HTTPS calls use the {op-system} trust bundle. If `trustedCA` is defined, the trust certificate is also used.

Any service that is running on the {op-system} node is able to use the trust bundle of the node.

// Proxy customizations
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-customization_{context}"]
= Proxy certificate customization

[role="_abstract"]
Update proxy certificates by modifying the config map referenced by `trustedCA` or by using machine configs to write CA certificates to the {op-system} trust bundle.

Updating the user-provided trust bundle consists of completing one of the following tasks:

* Updating the PEM-encoded certificates in the config map referenced by `trustedCA`
* Creating a config map in the namespace `openshift-config` that contains the new trust bundle and updating `trustedCA` to reference the name of the new config map.

The mechanism for writing CA certificates to the {op-system} trust bundle is exactly the same as writing any other file to {op-system}, which is done through the use of machine configs. When the Machine Config Operator (MCO) applies the new machine config that contains the new CA certificates, the MCO runs the `update-ca-trust` program and restarts the CRI-O service on the {op-system} nodes. This update does not require a node reboot. Restarting the CRI-O service automatically updates the trust bundle with the new CA certificates. For example:

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 50-examplecorp-ca-cert
spec:
  config:
    ignition:
      version: 3.1.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_ca_certificate>
        mode: 0644
        overwrite: true
        path: /etc/pki/ca-trust/source/anchors/examplecorp-ca.crt
----

The `truststore` of machines must also support updating the `truststore` of nodes.

// Proxy customizations
// Module included in the following assemblies:
//
// security/certificates_types_descriptions/proxy-certificates

[id="proxy-cert-renewal_{context}"]
= Proxy certificate renewal

[role="_abstract"]
No Operators can auto-renew proxy certificates on {op-system} nodes. You might need to periodically update the trust bundle manually.

There are no Operators that can auto-renew certificates on the {op-system} nodes.

[NOTE]
====
Red Hat does not monitor when CAs expire. Due to the long life of CAs, this is generally not an issue. However, you might need to periodically update the trust bundle.
====
