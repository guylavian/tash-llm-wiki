---
title: "Understanding security for {product-title}"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-policy-process-security
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-policy-process-security
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# Understanding security for {product-title}

[id="rosa-policy-process-security"]
= Understanding security for OpenShift Container Platform

[role="_abstract"]
This document details the Red{nbsp}Hat, Amazon Web Services (AWS), and customer security responsibilities for the managed OpenShift Container Platform.

.Acronyms and terms
[cols="1,3a"]
|===
| Acroynm | Definition
|*AWS*
|Amazon Web Services
|* *CEE*
|Customer Experience and Engagement (Red{nbsp}Hat Support)
|* *CI/CD*
|Continuous Integration / Continuous Delivery
|* *CVE*
|Common Vulnerabilities and Exposures
|* *PVs*
|Persistent Volumes
|* *SRE*
|Red{nbsp}Hat Site Reliability Engineering
|* *VPC*
|Virtual Private Cloud
|===

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-process-security.adoc

[id="rosa-policy-security-regulation-compliance_{context}"]
= Security and regulation compliance

Security and regulation compliance includes tasks such as the implementation of security controls and compliance certification.

[id="rosa-policy-data-classification_{context}"]
== Data classification
Red{nbsp}Hat defines and follows a data classification standard to determine the sensitivity of data and highlight inherent risk to the confidentiality and integrity of that data while it is collected, used, transmitted, stored, and processed. Customer-owned data is classified at the highest level of sensitivity and handling requirements.

[id="rosa-policy-data-management_{context}"]
== Data management
OpenShift Container Platform (ROSA) uses AWS Key Management Service (KMS) to help securely manage keys for encrypted data. These keys are used for control plane, infrastructure, and worker data volumes that are encrypted by default. Persistent volumes (PVs) for customer applications also use AWS KMS for key management.

When a customer deletes their ROSA cluster, all cluster data is permanently deleted, including control plane data volumes and customer application data volumes, such as persistent volumes (PV).

[id="rosa-policy-vulnerability-management_{context}"]
== Vulnerability management
Red{nbsp}Hat performs periodic vulnerability scanning of ROSA using industry standard tools. Identified vulnerabilities are tracked to their remediation according to timelines based on severity. Vulnerability scanning and remediation activities are documented for verification by third-party assessors in the course of compliance certification audits.

[id="rosa-policy-network-security_{context}"]
== Network security

[id="rosa-policy-firewall-ddos-protection_{context}"]
=== Firewall and DDoS protection
Each ROSA cluster is protected by a secure network configuration using firewall rules for AWS Security Groups. ROSA customers are also protected against DDoS attacks with AWS Shield Standard.

[id="rosa-policy-private-clusters-network-connectivity_{context}"]
=== Private clusters and network connectivity
Customers can optionally configure their ROSA cluster endpoints, such as web console, API, and application router, to be made private so that the cluster control plane and applications are not accessible from the Internet. Red{nbsp}Hat SRE still requires Internet-accessible endpoints that are protected with IP allow-lists.

AWS customers can configure a private network connection to their ROSA cluster through technologies such as AWS VPC peering, AWS VPN, or AWS Direct Connect.

[id="rosa-policy-cluster-network-access_{context}"]
=== Cluster network access controls
Fine-grained network access control rules can be configured by customers, on a per-project basis, using `NetworkPolicy` objects and the
OVN-Kubernetes CNI.
OpenShift SDN.

[id="rosa-policy-penetration-testing_{context}"]
== Penetration testing
Red{nbsp}Hat performs periodic penetration tests against ROSA. Tests are performed by an independent internal team by using industry standard tools and best practices.

Any issues that may be discovered are prioritized based on severity. Any issues found belonging to open source projects are shared with the community for resolution.

[id="rosa-policy-compliance_{context}"]
== Compliance
OpenShift Container Platform follows common industry best practices for security and controls. The certifications are outlined in the following table.

.Security and control certifications for OpenShift Container Platform
[cols= "3,3",options="header"]
|===
| Compliance | {hcp-title-first}

| FIPS | Yes

| HIPAA Qualified^[1]^ | Yes

| ISO 27001 | Yes

| ISO 27017 | Yes

| ISO 27018 | Yes

| PCI DSS 4.0 | Yes

| SOC 1 Type 2 | Yes

| SOC 2 Type 2 | Yes

| SOC 3 | Yes

| FedRAMP High^[2]^ | Yes

|===
1. For more information about Red Hat's HIPAA Qualified ROSA offerings, see the HIPAA Overview.
2. For more information about ROSA on GovCloud, see  FedRAMP Marketplace ROSA Agency.

.Security and control certifications for OpenShift Container Platform
[cols= "3,3,3",options="header"]
|===
| Compliance | OpenShift Container Platform (ROSA)| {hcp-title-first}

| HIPAA Qualified^[1]^ | Yes | Yes

| ISO 27001 | Yes | Yes

| ISO 27017 | Yes | Yes

| ISO 27018 | Yes | Yes

| PCI DSS 4.0 | Yes | Yes

| SOC 1 Type 2 | Yes | Yes

| SOC 2 Type 2 | Yes | Yes

| SOC 3 | Yes | Yes

| FedRAMP High^[2]^ | Yes (GovCloud requisite) | Yes

|===
1. For more information about Red Hat's HIPAA Qualified ROSA offerings, see the HIPAA Overview.
2. For more information about ROSA on GovCloud, see  FedRAMP Marketplace ROSA Agency.

[role="_additional-resources"]
.Additional resources

* Red{nbsp}Hat Subprocessor List
* ROSA Responsibilities

* ROSA Service Definition
* Viewing audit logs
* ROSA with HCP Service Definition
* Adding additional constraints for IP-based AWS role assumption
