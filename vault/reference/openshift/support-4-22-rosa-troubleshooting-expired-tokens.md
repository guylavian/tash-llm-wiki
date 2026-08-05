---
title: "Troubleshooting expired tokens"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-expired-tokens
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-expired-tokens
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting expired tokens

[id="rosa-troubleshooting-expired-tokens"]
= Troubleshooting expired tokens

[role="_abstract"]
Troubleshoot expired offline access tokens that prevent access to your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-expired-tokens.adoc

[id="rosa-troubleshooting-expired-offline-access-tokens_{context}"]
= Troubleshooting expired offline access tokens

[role="_abstract"]
If you use the OpenShift Container Platform (ROSA) CLI, `rosa`, and your api.openshift.com offline access token expires, an error message is displayed. This happens when sso.redhat.com invalidates the token.

The following example shows the output:

[source,terminal]
----
Can't get tokens ....
Can't get access tokens ....
----

.Procedure
* Generate a new offline access token at the following URL. The {cluster-manager-url} URL generates a new offline access token every time you visit it.
