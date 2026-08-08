---
title: "Zero Trust Workload Identity Manager components"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-components
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-components
version: 4.22
family: security
documentKind: "Documentation"
---

# Zero Trust Workload Identity Manager components

[id="zero-trust-manager-components"]
= Zero Trust Workload Identity Manager components

[role="_abstract"]
Review the components available in the initial release of {zero-trust-full} to understand the architecture. These components provide the foundation for identifying and securing your workloads.

// about csi driver
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zer-trust-manager-features.adoc

[id="zero-trust-manager-about-csi-driver_{context}"]
= SPIFFE CSI Driver

[role="_abstract"]
The SPIFFE Container Storage Interface (CSI) driver helps pods securely obtain their {svid-full} by delivering the Workload API socket. By using Kubernetes ephemeral inline volumes, the driver simplifies how applications request temporary storage for identity management.

When the pod starts, the Kubelet calls the SPIFFE CSI driver to provision and mount a volume into the pod's containers. The SPIFFE CSI driver mounts a directory that contains the SPIFFE Workload API into the pod. Applications in the pod then communicate with the Workload API to obtain their SVIDs. The driver guarantees that each SVID is unique.

// about oidc provider
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zer-trust-manager-features.adoc

[id="zero-trust-manager-about-oidc-provider_{context}"]
= SPIRE OpenID Connect Discovery Provider

[role="_abstract"]
Use the SPIRE OpenID Connect (OIDC) Discovery Provider to integrate SPIRE workload identities with OIDC-compliant systems. This component exposes endpoints for token verification. It helps ensure compatibility between SPIRE-issued credentials and external APIs requiring standard OIDC tokens.

While SPIRE primarily issues identities for workloads, additional workload-related claims can be embedded into JWT-SVIDs through the configuration of SPIRE, which these claims to be included in the token and verified by OIDC-compliant clients.

// about controller manager
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zer-trust-manager-features.adoc

[id="zero-trust-manager-about-controller-manager_{context}"]
= SPIRE Controller Manager

[role="_abstract"]
Use the SPIRE Controller Manager to automate workload registration with custom resource definitions (CRDs). The manager monitors pods and CRDs to create, update, or delete entries on the SPIRE Server. This process helps ensure that your SPIRE entries accurately reflect your active resources.

The SPIRE Controller Manager is designed to be deployed on the same pod as the SPIRE Server. The manager communicates with the SPIRE Server API using a private UNIX Domain Socket within a shared volume.

// about telemetry
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zer-trust-manager-features.adoc

[id="zero-trust-manager-server-agent-telemetry_{context}"]
= SPIRE Server and Agent telemetry

[role="_abstract"]
Use the SPIRE Controller Manager to register workloads by using custom resource definitions (CRDs). The manager monitors pods and CRDs for changes and triggers a reconciliation process. This process creates, updates, or deletes SPIRE Server entries to help ensure they match your configuration.

// about the workflow
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-overview.adoc

[id="zero-trust-manager-how-it-works_{context}"]
= About the {zero-trust-full} workflow

[role="_abstract"]
Understand the high-level workflow of {zero-trust-full} to help you manage secure identities. This process relies on SPIRE components and custom resource definitions (CRDs) to validate nodes and workloads.

The following is a high-level workflow of the {zero-trust-full} within the Red{nbsp}Hat OpenShift cluster.

. The SPIRE, SPIRE Agent, SPIFFE CSI Driver, and the SPIRE OIDC Discovery Provider operands are deployed and managed by {zero-trust-full} via associated customer resource definitions (CRDs).

. Watches are then registered for relevant Kubernetes resources and the necessary SPIRE CRDs are applied to the cluster.

. The CR for the ZeroTrustWorkloadIdentityManager resource named `cluster` is deployed and managed by a controller.

. To deploy the SPIRE Server, SPIRE Agent, SPIFFE CSI Driver, and SPIRE OIDC Discovery Provider, you need to create a custom resource of a each certain type and name it `cluster`. The custom resource types are as follows:

* SPIRE Server - `SpireServer`

* SPIRE Agent - `SpireAgent`

* SPIFFE CSI Driver - `SpiffeCSIDriver`

* SPIRE OIDC discovery provider - `SpireOIDCDiscoveryProvider`

. When a node starts, the SPIRE Agent initializes, and connects to the SPIRE Server.

. The SPIRE Agent begins the node attestation process. The agent collects information on the node's identity such as label name and namespace. The agent securely provides the information it gathered through the attestation to the SPIRE Server.

. The SPIRE Server then evaluates this information against its configured attestation policies and registration entries. If successful, the server generates an agent SVID and the Trust Bundle (CA Certificate) and securely sends this back to the SPIRE Agent.

. A workload starts on the node and needs a secure identity. The workload connects to the agent's Workload API and requests a SVID.

. The SPIRE Agent receives the request and begins a workload attestation to gather information about the workload.

. After the SPIRE Agent gathers the information, the information is sent to the SPIRE Server and the server checks its configured registration entries.

. The SPIRE Agent receives the workload SVID and Trust Bundle and passes it on to the workload. The workload can now present their SVIDs to other SPIFFE-aware devices to communicate with them.

[role="_additional-resources"]
.Additional resources
* Registering workloads

* SPIFFE Concepts

* SPIRE Use Cases
