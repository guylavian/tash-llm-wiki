---
title: "Setting up additional trusted certificate authorities for builds"
type: reference
domain: openshift
slug: cicd-4-22-setting-up-trusted-ca
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/setting-up-trusted-ca
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Setting up additional trusted certificate authorities for builds

[id="setting-up-trusted-ca"]
= Setting up additional trusted certificate authorities for builds

Use the following sections to set up additional certificate authorities (CA) to be trusted by builds when pulling images from an image registry.

The procedure requires a cluster administrator to create a `ConfigMap` and add additional CAs as keys in the `ConfigMap`.

* The `ConfigMap` must be created in the `openshift-config` namespace.
* `domain` is the key in the `ConfigMap` and `value` is the PEM-encoded certificate.
** Each CA must be associated with a domain. The domain format is `hostname[..port]`.
* The `ConfigMap` name must be set in the `image.config.openshift.io/cluster` cluster scoped configuration resource's `spec.additionalTrustedCA` field.
//* No longer needs single PEM bundle

// Module included in the following assemblies:
//
// * builds/setting-up-trusted-ca

[id="configmap-adding-ca_{context}"]
= Adding certificate authorities to the cluster

You can add certificate authorities (CA) to the cluster for use when pushing and pulling images with the following procedure.

.Prerequisites

* You must have cluster administrator privileges.
* You must have at least dedicated administrator privileges.
* You must have access to the public certificates of the registry, usually a `hostname/ca.crt` file located in the `/etc/docker/certs.d/` directory.

.Procedure

. Create a `ConfigMap` in the `openshift-config` namespace containing the trusted certificates for the registries that use self-signed certificates. For each CA file, ensure the key in the `ConfigMap` is the hostname of the registry in the `hostname[..port]` format:
+
[source,terminal]
----
$ oc create configmap registry-cas -n openshift-config \
--from-file=myregistry.corp.com..5000=/etc/docker/certs.d/myregistry.corp.com:5000/ca.crt \
--from-file=otherregistry.com=/etc/docker/certs.d/otherregistry.com/ca.crt
----

. Update the cluster image configuration:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-cas"}}}' --type=merge
----

[role="_additional-resources"]
== Additional resources

* Create a `ConfigMap`
* Secrets and `ConfigMaps`
* Configuring a custom PKI
