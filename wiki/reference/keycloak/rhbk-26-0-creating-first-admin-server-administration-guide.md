---
title: "Chapter 2. Creating the first administrator - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-creating-first-admin-server-administration-guide
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/creating-first-admin_server_administration_guide
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "After installing Red Hat build of Keycloak, you need an administrator account that can act as a super admin with full permissions to manage Red Hat build of Keycloak. With this account, you can log in to the Red Hat build of Keycloak Admin Console where you create realms and users and register applications that are secured by Red Hat build of Keycloak. 2.1. Creating the account on the local host I…"
---

# Chapter 2. Creating the first administrator - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 2. Creating the first administrator
After installing Red Hat build of Keycloak, you need an administrator account that can act as a super admin with full permissions to manage Red Hat build of Keycloak. With this account, you can log in to the Red Hat build of Keycloak Admin Console where you create realms and users and register applications that are secured by Red Hat build of Keycloak.
2.1. Creating the account on the local host
If your server is accessible from localhost
, perform these steps.
Procedure
- In a web browser, go to the http://localhost:8080 URL.
Supply a username and password that you can recall.
Welcome page
2.2. Creating the account remotely
If you cannot access the server from a localhost
address or just want to start Red Hat build of Keycloak from the command line, use the KC_BOOTSTRAP_ADMIN_USERNAME
and KC_BOOTSTRAP_ADMIN_PASSWORD
environment variables to create an initial admin account.
For example:
export KC_BOOTSTRAP_ADMIN_USERNAME=<username>
export KC_BOOTSTRAP_ADMIN_PASSWORD=<password>
bin/kc.[sh|bat] start
