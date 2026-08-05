---
title: "Aggregated API client certificates"
type: reference
domain: openshift
slug: security-4-22-aggregated-api-client-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/aggregated-api-client-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# Aggregated API client certificates

[id="cert-types-aggregated-api-client-certificates"]
= Aggregated API client certificates

== Purpose

Aggregated API client certificates are used to authenticate the KubeAPIServer when connecting to the Aggregated API Servers.

== Management

These certificates are managed by the system and not the user.

== Expiration
This CA is valid for 30 days.

The managed client certificates are valid for 30 days.

CA and client certificates are rotated automatically through the use of controllers.

== Customization

You cannot customize the aggregated API server certificates.
