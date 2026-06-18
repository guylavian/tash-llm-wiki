---
title: "Chapter 12. Updates for 26.2.6 - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-updates-for-26-2-6
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/updates_for_26_2_6
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 12. Updates for 26.2.6 - Red Hat build of Keycloak 26.2 Release Notes

Chapter 13. Updates for 26.2.6
This release contains several fixed issues, a change to the rights to assign admin roles, and other notable changes, which are described in the Upgrading Guide.
13.1. Restrict admin role mappings to server administrators
To enhance security, only users with the admin
role in the master
realm (server admins) can assign admin roles. This ensures that critical permissions cannot be delegated by realm-level administrators.
