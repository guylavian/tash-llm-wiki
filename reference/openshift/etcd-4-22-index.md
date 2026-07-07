---
title: "Kubernetes Key Management Service (KMS) v2 on {product-title}"
type: reference
domain: openshift
slug: etcd-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/index
version: 4.22
family: etcd
documentKind: "Documentation"
---

# Kubernetes Key Management Service (KMS) v2 on {product-title}

[id="kms_v2_index"]
= Kubernetes Key Management Service (KMS) v2 on OpenShift Container Platform

[role="_abstract"]
You can configure Kubernetes Key Management Service (KMS) v2 on OpenShift Container Platform to centralize encryption key management and meet regulatory compliance requirements.

// About the {KMS}
// Module included in the following assemblies:
//
// * etcd/KMS_v2/index.adoc

[id="kms-about_{context}"]
= About {KMS} encryption

[role="_abstract"]
{KMS} uses external Key Management Services to encrypt etcd data and centralize key management.

{KMS} provides:

* Customer-managed encryption keys that never leave the external KMS
* Centralized key management and auditing
* Regulatory compliance support

[id="kms-encrypted-resources_{context}"]
== Encrypted resources

When you enable KMS encryption, OpenShift Container Platform encrypts the following sensitive resources in etcd:

* Secrets
* ConfigMaps
* Routes
* OAuth access tokens
* OAuth authorize tokens

[NOTE]
====
Resource types, namespaces, and object names are not encrypted.
====

[role="_additional-resources"]
.Additional resources

* Using a KMS provider for data encryption

// KMS Technology Preview phases
// Module included in the following assemblies:
//
// * etcd/KMS_v2/index.adoc

[id="kms-technology-preview-phases_{context}"]
= KMS Technology Preview limitations

[role="_abstract"]
Review the current limitations of {KMS} to plan deployments and avoid unsupported configurations in OpenShift Container Platform 4.21 or later.

[id="kms-current-limitations_{context}"]
== Current limitations

* Plugins require manual installation on each control plane node
* Plugins must listen at `unix:///var/run/kmsplugin/kms.sock`
* Only one KMS plugin can run at a time
* KMS-to-KMS migration requires intermediate migration to `identity` or `aescbc`

[role="_additional-resources"]
[id="additional-resources_kms-v2-index"]
== Additional resources

* Enabling features using feature gates
* Using a KMS provider for data encryption
* HashiCorp Vault Transit Secrets Engine
* Use Vault as a Kubernetes KMS provider
