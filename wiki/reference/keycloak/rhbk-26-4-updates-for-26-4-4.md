---
title: "Chapter 11. Updates for 26.4.4 - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-updates-for-26-4-4
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/updates_for_26_4_4
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 11. Updates for 26.4.4 - Red Hat build of Keycloak 26.4 Release Notes

Chapter 11. Updates for 26.4.4
This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide. Also, an additional feature is deprecated.
11.1. Deprecated: Accepting HTTP requests with non-normalized paths
The http-accept-non-normalized-paths
option was introduced to restore the previous behavior where Red Hat build of Keycloak accepted non-normalized URLs.
Because this behavior can be problematic for URL filtering, it is deprecated and will be removed in a future release.
