---
title: "Token authentication for Operators on cloud providers"
type: reference
domain: openshift
slug: operators-4-22-osdk-token-auth
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/osdk-token-auth
version: 4.22
family: operators
documentKind: "Documentation"
---

# Token authentication for Operators on cloud providers

[id="osdk-token-auth"]
= Token authentication for Operators on cloud providers

Many cloud providers can enable authentication by using account tokens that provide short-term, limited-privilege security credentials.

OpenShift Container Platform includes the Cloud Credential Operator (CCO) to manage cloud provider credentials as custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with any specific permissions required.

Previously, on clusters where the CCO is in _manual mode_, Operators managed by Operator Lifecycle Manager (OLM) often provided detailed instructions in the OperatorHub for how users could manually provision any required cloud credentials.

Starting in OpenShift Container Platform 4.14, the CCO can detect when it is running on clusters enabled to use short-term credentials on certain cloud providers. It can then semi-automate provisioning certain credentials, provided that the Operator author has enabled their Operator to support the updated CCO.

[role="_additional-resources"]
.Additional resources

* About the Cloud Credential Operator
* CCO-based workflow for OLM-managed Operators with AWS STS
* CCO-based workflow for OLM-managed Operators with {entra-first}
* CCO-based workflow for OLM-managed Operators with {gcp-wid-short}
