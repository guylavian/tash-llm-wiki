---
title: "Chapter 16. Removed features - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-removed
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/removed
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "The following features have been removed from this release. 16.1. jboss.site.name and jboss.node.name Both system properties have been used internally within Keycloak and have not been part of the official documentation. Red Hat build of Keycloak will fail to start if those are present. Instead, use the command line option spi-cache-embedded-default-site-name as jboss.site.name replacement, and sp…"
---

# Chapter 16. Removed features - Red Hat build of Keycloak 26.4 Release Notes

Chapter 16. Removed features
The following features have been removed from this release.
16.1. jboss.site.name and jboss.node.name
Both system properties have been used internally within Keycloak and have not been part of the official documentation. Red Hat build of Keycloak will fail to start if those are present.
Instead, use the command line option spi-cache-embedded-default-site-name
as jboss.site.name
replacement, and spi-cache-embedded-default-node-name
as jboss.node.name
replacement. See All provider configuration for more details on these options.
16.2. KeycloakSessionTask.useExistingSession method
KeycloakSessionTask.useExistingSession
was only useful to private server logic. Now that this logic has been refined, no need exists for this method.
In previous releases, there was a default implementation in the interface returning false
and it is unlikely that it was overwritten in implementations.
