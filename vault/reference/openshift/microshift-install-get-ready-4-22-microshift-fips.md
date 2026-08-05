---
title: "Using FIPS mode with {microshift-short}"
type: reference
domain: openshift
slug: microshift-install-get-ready-4-22-microshift-fips
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_get_ready/microshift-fips
version: 4.22
family: microshift_install_get_ready
documentKind: "Documentation"
---

# Using FIPS mode with {microshift-short}

[id="microshift-fips"]
= Using FIPS mode with {microshift-short}

[role="_abstract"]
You must enable FIPS mode for RPM-based installations of {microshift-short} on {op-system-base-full} {op-system-version-major} to ensure that your edge deployments comply with security mandates.

The following considerations apply when enabling FIPS mode:

* To enable FIPS mode in {microshift-short} containers, the worker machine kernel must be enabled to run in FIPS mode before the machine starts.
* Using FIPS with {op-system-ostree-first} images is not supported.
* Using FIPS with image mode for {op-system-base} is not supported.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-fips.adoc

[id="microshift-fips-rpm-system_{context}"]
= FIPS mode with {op-system-base} RPM-based installations

[role="_abstract"]
Using FIPS with {microshift-short} requires enabling the cryptographic module self-checks in your {op-system-base-full} installation. After the host operating system has been configured to start with the FIPS modules, {microshift-short} containers are automatically enabled to run in FIPS mode.

* When {op-system-base} is started in FIPS mode, {microshift-short} core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 validation on only the x86_64 architectures.

* You must enable FIPS mode when you install {op-system-base} {op-system-version-major} on the machines that you plan to use as worker machines.
+
[IMPORTANT]
====
Because FIPS must be enabled before the operating system that your node uses starts for the first time, you cannot enable FIPS after you deploy a node.
====

* {microshift-short} uses a FIPS-compatible Golang compiler.

* FIPS is supported in the CRI-O container runtime.

[id="microshift-fips-limitations_{context}"]
== Limitations

* TLS implementation FIPS support is not complete.

* The FIPS implementation does not offer a single function that both computes hash functions and validates the keys that are based on that hash. This limitation continues to be evaluated for improvement in future {microshift-short} releases.

[id="additional-resources_microshift-fips_{context}"]
[role="_additional-resources"]
== Additional resources
* Switching RHEL to FIPS mode
