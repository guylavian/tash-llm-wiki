---
title: "Chapter 6. Updates for 26.4.9 - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-updates-for-26-4-9
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/updates_for_26_4_9
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This release contains several fixed issues and some notable changes. For details, see the Upgrading Guide. 6.1. CVE fixes CVE-2025-13881 The Admin API (/unmanagedAttributes) endpoint fails to respect the visibility configuration defined in the User Profile settings. CVE-2025-14559 This vulnerability allows the issuance of access and refresh tokens for disabled users via a business logic vulnerabil…"
---

# Chapter 6. Updates for 26.4.9 - Red Hat build of Keycloak 26.4 Release Notes

Chapter 6. Updates for 26.4.9
This release contains several fixed issues and some notable changes. For details, see the Upgrading Guide.
6.1. CVE fixes

- CVE-2025-13881 The Admin API (/unmanagedAttributes) endpoint fails to respect the visibility configuration defined in the User Profile settings.
- CVE-2025-14559 This vulnerability allows the issuance of access and refresh tokens for disabled users via a business logic vulnerability in the Token Exchange implementation when a privileged client invokes the token exchange flow.
- CVE-2025-14778 A Broken Access Control vulnerability exists in the UserManagedPermissionService (UMA Protection API).
- CVE-2026-1529 Organization invitation tokens in Keycloak are parsed without cryptographic signature verification during the registration flow.
- CVE-2026-1486 A vulnerability exists in the jwt-authorization-grant flow where the server fails to verify if an Identity Provider (IdP) is enabled before issuing tokens.
- CVE-2026-0871 An administrator with manage-users permission can modify unmanaged user attributes in Keycloak, even when the "Only administrators can view" setting is enabled.
- CVE-2026-0976 Keycloak accepts RFC-compliant matrix parameters (e.g., ;param) in path segments, while common reverse proxy configurations may ignore or mishandle them when enforcing access restrictions.
