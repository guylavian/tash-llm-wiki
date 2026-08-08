---
title: "{cert-manager-operator} release notes"
type: reference
domain: openshift
slug: security-4-22-cert-manager-operator-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-operator-release-notes
version: 4.22
family: security
documentKind: "Documentation"
---

# {cert-manager-operator} release notes

[id="cert-manager-operator-release-notes"]
= {cert-manager-operator} release notes

[role="_abstract"]
The {cert-manager-operator} is a cluster-wide service that provides application certificate lifecycle management.

These release notes track the development of {cert-manager-operator}.

For more information, see About the {cert-manager-operator}.

[id="cert-manager-operator-release-notes-1-19-0_{context}"]
== {cert-manager-operator} 1.19.0

Issued: 2026-04-20

The following advisories are available for the {cert-manager-operator} 1.19.0:

* RHBA-2026:9064
* RHBA-2026:9024
* RHBA-2026:8953
* RHBA-2026:9025
* RHBA-2026:8956

Version `v1.19.4` of the {cert-manager-operator} is based on the upstream cert-manager version `v1.19.4`. For more information, see the cert-manager project release notes for v1.19.4.

[id="cert-manager-operator-1-19-0-features-enhancements_{context}"]
=== New features and enhancements

Distribution of trust bundles with the trust manager operand (Technology Preview)::
In this release, the {cert-manager-operator} adds support for the trust-manager operand as a Technology Preview feature. You can now install the trust-manager operand to automate the secure distribution of trust bundles, such as certificate authority (CA) certificates, to application namespaces across your cluster. For more information, see Distributing certificates by using trust-manager operand.

Support for configuring the certificate request backoff duration::
In this release, the {cert-manager-operator} adds support for the `--certificate-request-minimum-backoff-duration` flag. With this flag, you can configure the minimum backoff period for certificate requests by override the default configuration. For more information, see Overridable arguments for the cert-manager components.

[id="cert-manager-operator-1-19-0-known-issues_{context}"]
=== Fixed issues

* Before this update, the *ClusterIssuer* form view lacked an option to remove the self-signed field. As a consequence, you could not create issuer types other than self-signed. With this release, the form view sets the certificate authority (CA) as the default issuer type. As a result, you can switch to other issuer types by using the form view. (OCPBUGS-65620)
