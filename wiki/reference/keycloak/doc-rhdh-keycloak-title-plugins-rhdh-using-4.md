---
title: "Chapter 4. Using Keycloak - Red Hat Developer Hub 1.5 Using dynamic plugins in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-rhdh-keycloak-title-plugins-rhdh-using-4
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/using_dynamic_plugins_in_red_hat_developer_hub/rhdh-keycloak_title-plugins-rhdh-using
guide: using_dynamic_plugins_in_red_hat_developer_hub
documentKind: "Documentation"
---

# Chapter 4. Using Keycloak - Red Hat Developer Hub 1.5 Using dynamic plugins in Red Hat Developer Hub

Chapter 4. Using Keycloak
The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities:
- Synchronization of Keycloak users in a realm.
- Synchronization of Keycloak groups and their users in a realm.
4.1. Importing users and groups in Developer Hub using the Keycloak plugin
After configuring the plugin successfully, the plugin imports the users and groups each time when started.
If you set up a schedule, users and groups will also be imported.
After the first import is complete, you can select User to list the users from the catalog page:
You can see the list of users on the page:
When you select a user, you can see the information imported from Keycloak:
You can also select a group, view the list, and select or view the information imported from Keycloak for a group:
