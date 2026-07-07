---
title: "User-provided certificates for the API server"
type: reference
domain: openshift
slug: security-4-22-user-provided-certificates-for-api-server
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/user-provided-certificates-for-api-server
version: 4.22
family: security
documentKind: "Documentation"
---

# User-provided certificates for the API server

[id="cert-types-user-provided-certificates-for-the-api-server"]
= User-provided certificates for the API server

== Purpose

The API server is accessible by clients external to the cluster at `api.<cluster_name>.<base_domain>`. You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. The administrator must set a custom default certificate to be used by the API server when serving content.

== Location

The user-provided certificates must be provided in a `kubernetes.io/tls` type `Secret` in the `openshift-config` namespace. Update the API server cluster configuration, the `apiserver/cluster` resource, to enable the use of the user-provided certificate.

== Management

User-provided certificates are managed by the user.

== Expiration

API server client certificate expiration is less than five minutes.

User-provided certificates are managed by the user.

== Customization

Update the secret containing the user-managed certificate as needed.

[role="_additional-resources"]
== Additional resources

* Adding API server certificates
