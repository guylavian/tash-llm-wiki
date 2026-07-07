---
title: "Updating the CA bundle"
type: reference
domain: openshift
slug: security-4-22-updating-ca-bundle
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/updating-ca-bundle
version: 4.22
family: security
documentKind: "Documentation"
---

# Updating the CA bundle

[id="updating-ca-bundle"]
= Updating the CA bundle

// Module included in the following assemblies:
//
// * security/certificates/updating-ca-bundle.adoc

[id="ca-bundle-understanding_{context}"]
= Understanding the CA Bundle certificate

Proxy certificates allow users to specify one or more custom certificate authority (CA) used by platform components when making egress connections.

The `trustedCA` field of the Proxy object is a reference to a config map that contains a user-provided trusted certificate authority (CA) bundle. This bundle is merged with the {op-system-first} trust bundle and injected into the trust store of platform components that make egress HTTPS calls. For example, `image-registry-operator` calls an external image registry to download images. If `trustedCA` is not specified, only the {op-system} trust bundle is used for proxied HTTPS connections. Provide custom CA certificates to the {op-system} trust bundle if you want to use your own certificate infrastructure.

The `trustedCA` field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from required key `ca-bundle.crt` and copying it to a config map named `trusted-ca-bundle` in the `openshift-config-managed` namespace. The namespace for the config map referenced by `trustedCA` is `openshift-config`:

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

// Module included in the following assemblies:
//
// * security/certificates/updating-ca-bundle.adoc

[id="ca-bundle-replacing_{context}"]
= Replacing the CA Bundle certificate

.Procedure

. Create a config map that includes the root CA certificate used to sign the wildcard certificate:
+
[source,terminal]
----
$ oc create configmap custom-ca \
     --from-file=ca-bundle.crt=</path/to/example-ca.crt> \//<1>
     -n openshift-config
----
<1> `</path/to/example-ca.crt>` is the path to the CA certificate bundle on your local file system.

. Update the cluster-wide proxy configuration with the newly created config map:
+
[source,terminal]
----
$ oc patch proxy/cluster \
     --type=merge \
     --patch='{"spec":{"trustedCA":{"name":"custom-ca"}}}'
----

[role="_additional-resources"]
== Additional resources

* Replacing the default ingress certificate
* Enabling the cluster-wide proxy
* Proxy certificate customization
