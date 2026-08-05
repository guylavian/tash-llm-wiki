---
title: "Configuring private connections"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-configuring-private-connections
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-configuring-private-connections
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Configuring private connections

[id="rosa-configuring-private-connections"]
= Configuring private connections

Private cluster access can be implemented to suit the needs of your OpenShift Container Platform environment.

.Procedure
. Access your OpenShift Container Platform AWS account and use one or more of the following methods to establish a private connection to your cluster:

- Configuring AWS VPC peering: Enable VPC peering to route network traffic between two private IP addresses.

- Configuring AWS VPN: Establish a Virtual Private Network to securely connect your private network to your Amazon Virtual Private Cloud.

- Configuring AWS Direct Connect: Configure AWS Direct Connect to establish a dedicated network connection between your private network and an AWS Direct Connect location.

+
// Link to ROSA Classic procedure.
. Configure a private cluster on OpenShift Container Platform.

// Link to ROSA HCP procedure. This can be included once the xref target is included in the ROSA HCP topic map.
// ifdef::openshift-rosa-hcp[]
// . Configure a private cluster on ROSA.
// endif::openshift-rosa-hcp[]
