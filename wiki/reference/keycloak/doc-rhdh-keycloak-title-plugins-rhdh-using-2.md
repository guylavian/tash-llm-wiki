---
title: "Chapter 4. Using Keycloak - Red Hat Developer Hub 1.7 Using dynamic plugins in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-rhdh-keycloak-title-plugins-rhdh-using-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.7/html/using_dynamic_plugins_in_red_hat_developer_hub/rhdh-keycloak_title-plugins-rhdh-using
guide: using_dynamic_plugins_in_red_hat_developer_hub
documentKind: "Documentation"
---

# Chapter 4. Using Keycloak - Red Hat Developer Hub 1.7 Using dynamic plugins in Red Hat Developer Hub

Chapter 4. Using Keycloak
The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities:
- Synchronization of Keycloak users in a realm.
- Synchronization of Keycloak groups and their users in a realm.
4.1. Importing users and groups in Developer Hub using the Keycloak plugin
After configuring the plugin successfully, the plugin imports the users and groups each time when started.
If you set up a schedule, users and groups will also be imported.
Procedure
- in Red Hat Developer Hub, go to the Catalog page.
- Select User from the entity type filter to display the list of imported users.
- Browse the list of users displayed on the page.
- Select a user to view detailed information imported from Keycloak.
- To view groups, select Group from the entity type filter.
- Browse the list of groups shown on the page.
- From the list of groups, select a group to view the information imported from Keycloak.
