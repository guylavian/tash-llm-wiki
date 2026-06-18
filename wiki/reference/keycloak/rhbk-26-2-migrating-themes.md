---
title: "Chapter 7. Migrating custom themes - Red Hat build of Keycloak 26.2 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-migrating-themes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/migration_guide/migrating-themes
guide: migration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 7. Migrating custom themes - Red Hat build of Keycloak 26.2 Migration Guide

Chapter 7. Migrating custom themes
7.1. New Admin Console
The new Admin Console (keycloak.v2) is built using React. The old Admin Console (keycloak) was built with AngularJS 1.x, which reached end-of-life a while ago. Thus, there is no migration path from the old console or any theme that extends it. The base theme Admin Console is also not supported for the same reason.
7.2. New Account Console
The new Account Console (keycloak.v2) is built using React, providing a better user experience. The old Account Console (keycloak) was built with basic server-side templating. Thus, there is no migration path from the old console or any theme that extends it.
7.3. Migrating login themes
Themes are used to configure the look and feel of login pages and the Account Console.
When creating or updating custom themes, especially when overriding templates, it may be useful to use the built-in templates as a reference. These templates are in ${KC_HOME}/lib/lib/main/org.keycloak.keycloak-themes-${KC_VERSION}.jar
, which can be opened using any standard ZIP archive tool.
When running the server in development mode using start-dev
, themes are not cached so that you can easily work on them without a need to restart the server when making changes.
To install custom themes, you can choose from packaging your theme files as a JAR file and deploy it to the ${KC_HOME}/providers
directory, or copy files directly to the ${KC_HOME}/themes
directory. In both cases, see the Server Developer Guide for more details about the file and directory structure expected by the server.
