---
title: "Zero Trust Workload Identity Manager overview"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-overview
version: 4.22
family: security
documentKind: "Documentation"
---

# Zero Trust Workload Identity Manager overview

[id="zero-trust-manager-overview"]
= Zero Trust Workload Identity Manager overview

[role="_abstract"]
The {zero-trust-full} is an OpenShift Container Platform Operator that manages the lifecycle of SPIFFE Runtime Environment (SPIRE) components. It enables workload identity management based on the Secure Production Identity Framework for Everyone (SPIFFE) standard, providing cryptographically verifiable identities (SVIDs) to workloads running in OpenShift Container Platform clusters.

The following are  components of the {zero-trust-full} architecture:

// about spiffe
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-overview.adoc

[id="zero-trust-manager-about-spiffe_{context}"]
= SPIFFE

[role="_abstract"]
Establish trust between software workloads in distributed systems with {spiffe-full}. SPIFFE assigns unique IDs to workloads, allowing workloads to verify identities and communicate securely. This ensures secure authentication across dynamic environments.

The SPIFFE IDs are contained in the {svid-full}. SVIDs are used by workloads to verify their identity to other workloads so that the workloads can communicate with each other. The two main SVID formats are:

* X.509-SVIDs: X.509 certificates where the SPIFFE ID is embedded in the Subject Alternative Name (SAN) field.
* JWT-SVIDs: JSON Web Tokens (JWTs) where the SPIFFE ID is included as the `sub` claim.

For more information, see SPIFFE Overview.

// about spire
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-overview.adoc

[id="zero-trust-manager-about-spire_{context}"]
= SPIRE Server

[role="_abstract"]
The SPIRE Server is the central management component of SPIRE that issues SPIFFE identities and maintains the registration database for a trust domain.

[role="_additional-resources"]
.Additional resources

* About the SPIRE Server

// about agent
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-overview.adoc

[id="zero-trust-manager-about-agent_{context}"]
= SPIRE Agent

[role="_abstract"]
The SPIRE Agent performs workload attestation to ensure that workloads receive a verified identity when requesting authentication through the SPIFFE Workload API. The agent uses configured workload attestor plugins to verify these identities.

SPIRE and the SPIRE Agent perform node attestation via node plugins. The plugins are used to verify the identity of the node on which the agent is running. For more information, see About the SPIRE Agent.

// about attestation
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-overview.adoc

[id="zero-trust-manager-about-attestation_{context}"]
= Attestation

[role="_abstract"]
The attestation process verifies the identity of nodes and workloads before issuing SPIFFE IDs. By comparing attributes against defined selectors, this process ensures that only legitimate entities within the trust domain receive cryptographic credentials.

The two main types of attestation in SPIFFE/SPIRE are:

* Node attestation: verifies the identity of a machine or a node on a system, before a SPIRE Agent running on that node can be trusted to request identities for workloads.

* Workload attestation: verifies the identity of an application or service running on an attested node before the SPIRE Agent on that node can provide it with a SPIFFE ID and SVID.

For more information, see Attestation.
