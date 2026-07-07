---
title: "Supported compliance profiles"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-supported-profiles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-supported-profiles
version: 4.22
family: security
documentKind: "Documentation"
---

# Supported compliance profiles

[id="compliance-operator-supported-profiles"]
= Supported compliance profiles

There are several profiles available as part of the Compliance Operator (CO)
installation. While you can use the following profiles to assess gaps in a
cluster, usage alone does not infer or guarantee compliance with a particular
profile and is not an auditor.

In order to be compliant or certified under these various standards, you need
to engage an authorized auditor such as a Qualified Security Assessor (QSA),
Joint Authorization Board (JAB), or other industry recognized regulatory
authority to assess your environment. You are required to work with an
authorized auditor to achieve compliance with a standard.

For more information on compliance support for all Red{nbsp}Hat products, see Product Compliance.

[IMPORTANT]
====
The Compliance Operator might report incorrect results on some managed platforms, such as OpenShift Dedicated and Azure Red Hat OpenShift. For more information, see the Red Hat Knowledgebase Solution #6983418.
====

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-supported-profiles.adoc

[id="compliance-supported-profiles_{context}"]
= Compliance profiles

The Compliance Operator provides profiles to meet industry standard benchmarks.

[NOTE]
====
The following tables reflect the latest available profiles in the Compliance Operator. The only supported versions of CIS and DISA STIG profiles will be the latest. Our recommendation to customers is to use `ocp4-cis` and `ocp4-cis-node`, `ocp4-stig`, and `ocp4-stig-node`, which always point to the latest version.
====

[id="cis-profiles_{context}"]
== CIS compliance profiles

.Supported CIS compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-cis ^[1]^
|CIS Red{nbsp}Hat OpenShift Container Platform Benchmark v1.9.0
|Platform
|CIS Benchmarks &#8482; ^[4]^
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|

|ocp4-cis-1-9^[3]^
|CIS Red{nbsp}Hat OpenShift Container Platform Benchmark v1.9.0
|Platform
|CIS Benchmarks &#8482; ^[4]^
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|

|ocp4-cis-node ^[1]^
|CIS Red{nbsp}Hat OpenShift Container Platform Benchmark v1.9.0
|Node ^[2]^
|CIS Benchmarks &#8482; ^[4]^
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-cis-node-1-9^[3]^
|CIS Red{nbsp}Hat OpenShift Container Platform Benchmark v1.9.0
|Node ^[2]^
|CIS Benchmarks &#8482; ^[4]^
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|===
[.small]
1. The  `ocp4-cis` and `ocp4-cis-node` profiles maintain the most up-to-date version of the CIS benchmark as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as CIS v1.9.0, use the `ocp4-cis-1-9` and `ocp4-cis-node-1-9` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.
3. All earlier CIS profiles are superceded by CIS v1.9.0. It is recommended to apply the latest profile to your environment.
4. To locate the CIS OpenShift Container Platform v4 Benchmark, go to  CIS Benchmarks and click *Download Latest CIS Benchmark*, where you can then register to download the benchmark.

[id="bsi-profiles_{context}"]
== BSI Profile Support

.Supported BSI compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-bsi ^[1]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Platform
|BSI Basic Protection Compendium
|`x86_64`
|

|ocp4-bsi-node ^[1]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Node ^[2]^
|BSI Basic Protection Compendium
|`x86_64`
|

|rhcos4-bsi ^[1]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Node ^[2]^
|BSI Basic Protection Compendium
|`x86_64`
|

|ocp4-bsi-2022 ^[3]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Platform
|BSI Basic Protection Compendium
|`x86_64`
|

|ocp4-bsi-node-2022 ^[3]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Node ^[2]^
|BSI Basic Protection Compendium
|`x86_64`
|

|rhcos4-bsi-2022 ^[3]^
|BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4
|Node ^[2]^
|BSI Basic Protection Compendium
|`x86_64`
|

|===
[.small]
1. The  `ocp4-bsi`, `ocp4-bsi-node`, and `rhcos4-bsi` profiles maintain the most up-to-date version of the BSI Basic Protection Profile as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as BSI 2022, use the `ocp4-bsi-2022`, `ocp4-bsi-node-2022` or `rhcos4-bsi-2022` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.
3. Edition 2022 is the latest available English edition of the BSI IT-Grundschutz (Basic Protection) compendium. There were no changes for Building Blocks SYS.1.6 and APP.4.4, SYS.1.1, and SYS.1.3 in the latest published German compendium (edition 2023).

For more information, see *BSI Quick Check*.

[id="e8-profiles_{context}"]
== Essential Eight compliance profiles

.Supported Essential Eight compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-e8
|Australian Cyber Security Centre (ACSC) Essential Eight
|Platform
|ACSC Hardening Linux Workstations and Servers
|`x86_64`
|

|rhcos4-e8
|Australian Cyber Security Centre (ACSC) Essential Eight
|Node
|ACSC Hardening Linux Workstations and Servers
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|===

[id="fedramp-high-profiles_{context}"]
== FedRAMP High compliance profiles

[IMPORTANT]
====
Applying automatic remedations to any profile, such as `rhcos4-stig`, that uses the `service-sshd-disabled` rule, automatically disables the `sshd` service. This situation blocks SSH access to control plane nodes and compute nodes. To keep the SSH access enabled, create a `TailoredProfile` object and set the `rhcos4-service-sshd-disabled` rule value for the `disableRules` parameter.
====

.Supported FedRAMP High compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-high ^[1]^
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat OpenShift - Platform level
|Platform
|NIST SP-800-53 Release Search
|`x86_64`
|

|ocp4-high-node ^[1]^
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat OpenShift - Node level
|Node ^[2]^
|NIST SP-800-53 Release Search
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-high-node-rev-4
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat OpenShift - Node level
|Node ^[2]^
|NIST SP-800-53 Release Search
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-high-rev-4
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat OpenShift - Platform level
|Platform
|NIST SP-800-53 Release Search
|`x86_64`
|

|rhcos4-high ^[1]^
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat Enterprise Linux CoreOS
|Node
|NIST SP-800-53 Release Search
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|rhcos4-high-rev-4
|NIST 800-53 High-Impact Baseline for Red{nbsp}Hat Enterprise Linux CoreOS
|Node
|NIST SP-800-53 Release Search
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|===
[.small]
1. The  `ocp4-high`, `ocp4-high-node` and `rhcos4-high` profiles maintain the most up-to-date version of the FedRAMP High standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as FedRAMP high R4, use the `ocp4-high-rev-4` and `ocp4-high-node-rev-4` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.

[id="fedramp-moderate-profiles_{context}"]
== FedRAMP Moderate compliance profiles

.Supported FedRAMP Moderate compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-moderate ^[1]^
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat OpenShift - Platform level
|Platform
|NIST SP-800-53 Release Search
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|

|ocp4-moderate-node ^[1]^
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat OpenShift - Node level
|Node ^[2]^
|NIST SP-800-53 Release Search
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-moderate-node-rev-4
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat OpenShift - Node level
|Node ^[2]^
|NIST SP-800-53 Release Search
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-moderate-rev-4
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat OpenShift - Platform level
|Platform
|NIST SP-800-53 Release Search
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|

|rhcos4-moderate ^[1]^
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat Enterprise Linux CoreOS
|Node
|NIST SP-800-53 Release Search
|`x86_64`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|rhcos4-moderate-rev-4
|NIST 800-53 Moderate-Impact Baseline for Red{nbsp}Hat Enterprise Linux CoreOS
|Node
|NIST SP-800-53 Release Search
|`x86_64`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|===
[.small]
1. The  `ocp4-moderate`, `ocp4-moderate-node` and `rhcos4-moderate` profiles maintain the most up-to-date version of the FedRAMP Moderate standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as FedRAMP Moderate R4, use the `ocp4-moderate-rev-4` and `ocp4-moderate-node-rev-4` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.

[id="nerc-cip-profiles_{context}"]
== NERC-CIP compliance profiles

.Supported NERC-CIP compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-nerc-cip
|North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for the OpenShift Container Platform - Platform level
|Platform
|NERC CIP Standards
|`x86_64`
|

|ocp4-nerc-cip-node
|North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for the OpenShift Container Platform - Node level
|Node ^[1]^
|NERC CIP Standards
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|rhcos4-nerc-cip
|North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for Red{nbsp}Hat Enterprise Linux CoreOS
|Node
|NERC CIP Standards
|`x86_64`
|{product-rosa} with {hcp} (ROSA HCP)

|===
[.small]
1. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.

[id="pci-dss-profiles_{context}"]
== PCI-DSS compliance profiles

.Supported PCI-DSS compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-pci-dss ^[1]^
|PCI-DSS v4 Control Baseline for OpenShift Container Platform 4
|Platform
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `aarch64`
|

|ocp4-pci-dss-3-2 ^[3]^
|PCI-DSS v3.2.1 Control Baseline for OpenShift Container Platform 4
|Platform
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|

|ocp4-pci-dss-4-0
|PCI-DSS v4 Control Baseline for OpenShift Container Platform 4
|Platform
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `aarch64`
|

|ocp4-pci-dss-node ^[1]^
|PCI-DSS v4 Control Baseline for OpenShift Container Platform 4
|Node ^[2]^
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-pci-dss-node-3-2 ^[3]^
|PCI-DSS v3.2.1 Control Baseline for OpenShift Container Platform 4
|Node ^[2]^
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `s390x`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-pci-dss-node-4-0
|PCI-DSS v4 Control Baseline for OpenShift Container Platform 4
|Node ^[2]^
|PCI Security Standards &#174; Council Document Library
|`x86_64`
 `ppc64le`
 `aarch64`
|{product-rosa} with {hcp} (ROSA HCP)
|===

[.small]
1. The  `ocp4-pci-dss` and `ocp4-pci-dss-node` profiles maintain the most up-to-date version of the PCI-DSS standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as PCI-DSS v3.2.1, use the `ocp4-pci-dss-3-2` and `ocp4-pci-dss-node-3-2` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.
3. PCI-DSS v3.2.1 is superceded by PCI-DSS v4. It is recommended to apply the latest profile to your environment.

[id="stig-profiles_{context}"]
== STIG compliance profiles

[IMPORTANT]
====
Applying automatic remedations to any profile, such as `rhcos4-stig`, that uses the `service-sshd-disabled` rule, automatically disables the `sshd` service. This situation blocks SSH access to control plane nodes and compute nodes. To keep the SSH access enabled, create a `TailoredProfile` object and set the `rhcos4-service-sshd-disabled` rule value for the `disableRules` parameter.
====

.Supported STIG compliance profiles
[cols="2,2,1,2,1,2", options="header"]

|===
|Profile
|Profile title
|Application
|Industry compliance benchmark
|Supported architectures
|Supported platforms

|ocp4-stig ^[1]^
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift^[3]^
|Platform
|DISA-STIG
|`x86_64`
 `ppc64le`
|

|ocp4-stig-node ^[1]^
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift^[3]^
|Node ^[2]^
|DISA-STIG
|`x86_64`
 `ppc64le`
|{product-rosa} with {hcp} (ROSA HCP)

|ocp4-stig-v2r3
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift V2R3
|Platform
|DISA-STIG
|`x86_64`
 `ppc64le`
|

|ocp4-stig-node-v2r3 ^[1]^
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift V2R3
|Node
|DISA-STIG
|`x86_64`
 `ppc64le`
|

|rhcos4-stig^[1]^
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift^[3]^
|Node
|DISA-STIG
|`x86_64`
 `ppc64le`
|{product-rosa} with {hcp} (ROSA HCP)

|rhcos4-stig-v2r3
|Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red{nbsp}Hat Openshift V2R3
|Node
|DISA-STIG
|`x86_64`
 `ppc64le`
|{product-rosa} with {hcp} (ROSA HCP)

|===
[.small]
1. The  `ocp4-stig`, `ocp4-stig-node` and `rhcos4-stig` profiles maintain the most up-to-date version of the DISA-STIG benchmark as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as DISA-STIG V2R3, use the `ocp4-stig-v2r3` and `ocp4-stig-node-v2r3` profiles.
2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_.
3. DISA-STIG V1R2 is superceded by DISA-STIG V2R3. It is recommended to apply the latest profile to your environment.

[id="compliance-extended-profiles_{context}"]
== About extended compliance profiles

Some compliance profiles have controls that require following industry best practices, resulting in some profiles extending others. Combining the Center for Internet Security (CIS) best practices with National Institute of Standards and Technology (NIST) security frameworks establishes a path to a secure and compliant environment.

For example, the NIST High-Impact and Moderate-Impact profiles extend the CIS profile to achieve compliance. As a result, extended compliance profiles eliminate the need to run both profiles in a single cluster.

.Profile extensions
[cols="50%,50%", options="header"]

|===
|Profile
|Extends

|ocp4-pci-dss
|ocp4-cis

|ocp4-pci-dss-node
|ocp4-cis-node

|ocp4-high
|ocp4-cis

|ocp4-high-node
|ocp4-cis-node

|ocp4-moderate
|ocp4-cis

|ocp4-moderate-node
|ocp4-cis-node

|ocp4-nerc-cip
|ocp4-moderate

|ocp4-nerc-cip-node
|ocp4-moderate-node
|===

// Module included in the following assemblies:
//
// * security/compliance_operator/co-concepts/compliance-operator-understanding.adoc
// * security/compliance_operator/co-scans/compliance-operator-supported-profiles.adoc

[id="compliance_profile_types_{context}"]
= Compliance Operator profile types

Compliance Operator rules are organized into profiles. Profiles can target the Platform or Nodes for OpenShift Container Platform, and some benchmarks include `rhcos4` Node profiles.

Platform:: Platform profiles evaluate your OpenShift Container Platform cluster components. For example, a Platform-level rule can confirm whether APIServer configurations are using strong encryption cyphers.

Node:: Node profiles evaluate the OpenShift or {op-system} configuration of each host. You can use two Node profiles: `ocp4` Node profiles and `rhcos4` Node profiles. The `ocp4` Node profiles evaluate the OpenShift configuration of each host. For example, they can confirm whether `kubeconfig` files have the correct permissions to meet a compliance standard. The `rhcos4` Node profiles evaluate the {op-system-first} configuration of each host. For example, they can confirm whether the SSHD service is configured to disable password logins.

[IMPORTANT]
====
For benchmarks that have Node and Platform profiles, such as PCI-DSS, you must run both profiles in your OpenShift Container Platform environment.

For benchmarks that have `ocp4` Platform, `ocp4` Node, and `rhcos4` Node profiles, such as FedRAMP High, you must run all three profiles in your OpenShift Container Platform environment.
====

[NOTE]
====
In a cluster with many Nodes, both `ocp4` Node and `rhcos4` Node scans might take a long time to complete.
====
