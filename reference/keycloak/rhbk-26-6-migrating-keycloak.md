---
title: "Chapter 8. Migrating upstream Keycloak to Red Hat build of Keycloak 26.6 - Red Hat build of Keycloak 26.6 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-migrating-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/migration_guide/migrating-keycloak
guide: migration_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Starting with version 22, minimal differences exist between Red Hat build of Keycloak and upstream Keycloak. The following differences exist: For upstream Keycloak, the distribution artifacts are on keycloak.org; for Red Hat build of Keycloak, the distribution artifacts are on the Red Hat customer portal. Oracle and MSSQL database drivers are bundled with upstream Keycloak, but not bundled with Re…"
---

# Chapter 8. Migrating upstream Keycloak to Red Hat build of Keycloak 26.6 - Red Hat build of Keycloak 26.6 Migration Guide

Chapter 8. Migrating upstream Keycloak to Red Hat build of Keycloak 26.6
Starting with version 22, minimal differences exist between Red Hat build of Keycloak and upstream Keycloak. The following differences exist:
- For upstream Keycloak, the distribution artifacts are on keycloak.org; for Red Hat build of Keycloak, the distribution artifacts are on the Red Hat customer portal.
- Oracle and MSSQL database drivers are bundled with upstream Keycloak, but not bundled with Red Hat build of Keycloak. See Configuring the database for detailed steps on how to install those drivers.
- The GELF log handler is not available in Red Hat build of Keycloak.
The migration process depends on the version of Keycloak to be migrated and the type of Keycloak installation. See the following sections for details.
8.1. Matching Keycloak version
The migration process depends on the version of Keycloak to be migrated.
- If your Keycloak project version matches the Red Hat build of Keycloak version, migrate Keycloak by using the Red Hat build of Keycloak artifacts on the Red Hat customer portal.
- If your Keycloak project version is an older version, use the Keycloak Upgrading Guide to upgrade Keycloak to match the Red Hat build of Keycloak version. Then, migrate Keycloak using the artifacts on the Red Hat customer portal.
- If your Keycloak project version is greater than the Red Hat build of Keycloak version, you cannot migrate to Red Hat build of Keycloak. Instead, create a new deployment of Red Hat build of Keycloak or wait for a future Red Hat build of Keycloak release.
8.2. Migration based on type of Keycloak installation
Once you have a matching version of Keycloak, migrate Keycloak based on the type of installation.
- If you installed Keycloak from a ZIP distribution, migrate Keycloak by using the artifacts on the Red Hat customer portal.
- If you deployed the Keycloak Operator, uninstall it and install the Red Hat build of Keycloak Operator by using the Operator guide. The CRs are compatible between upstream Keycloak and Red Hat build of Keycloak.
- If you created a custom server container image, rebuild it by using the Red Hat build of Keycloak image. See Running Keycloak in a Container.
