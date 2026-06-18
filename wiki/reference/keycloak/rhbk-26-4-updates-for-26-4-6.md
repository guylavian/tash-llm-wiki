---
title: "Chapter 9. Updates for 26.4.6 - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-updates-for-26-4-6
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/updates_for_26_4_6
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide. Also, this release includes a change to filtering of LDAP referrals to mitigate a CVE. 9.1. Filtering of LDAP referrals This release adds filtering of LDAP referrals by default. This change enhances security and aligns with best practices for LDAP configurations. If this change is una…"
---

# Chapter 9. Updates for 26.4.6 - Red Hat build of Keycloak 26.4 Release Notes

Chapter 9. Updates for 26.4.6
This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide. Also, this release includes a change to filtering of LDAP referrals to mitigate a CVE.
9.1. Filtering of LDAP referrals
This release adds filtering of LDAP referrals by default. This change enhances security and aligns with best practices for LDAP configurations. If this change is unacceptable, you can disable LDAP referrals in all LDAP providers in all realms.
9.2. Deprecated: Filtering of LDAP referrals
The option spi-storage—ldap—secure-referral
to disable filtering referrals is deprecated. When this feature is removed in a future release, filtering will be enforced.
9.3. CVE fix
- CVE-2025-13467 An authenticated realm administrator can configure the LDAP User Federation provider to connect to a malicious LDAP server. By setting the connectionUrl parameter and enabling Referral: follow, the Keycloak server can be forced to deserialize an untrusted Java object from a malicious RMI server during a user sync action.
