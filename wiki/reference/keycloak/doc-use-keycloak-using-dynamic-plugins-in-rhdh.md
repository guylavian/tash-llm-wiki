---
title: "Chapter 4. Use Keycloak - Red Hat Developer Hub 1.9 Using dynamic plugins in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-use-keycloak-using-dynamic-plugins-in-rhdh
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.9/html/using_dynamic_plugins_in_red_hat_developer_hub/use-keycloak_using-dynamic-plugins-in-rhdh
guide: using_dynamic_plugins_in_red_hat_developer_hub
documentKind: "Documentation"
---

# Chapter 4. Use Keycloak - Red Hat Developer Hub 1.9 Using dynamic plugins in Red Hat Developer Hub

Chapter 4. Use Keycloak
The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities:
- Synchronization of Keycloak users in a realm.
- Synchronization of Keycloak groups and their users in a realm.
After configuring the plugin successfully, the plugin imports the users and groups each time when started.
Note
If you set up a schedule, users and groups will also be imported.
Procedure
- In Red Hat Developer Hub, go to the Catalog page.
- Select User from the entity type filter to display the list of imported users.
- Browse the list of users displayed on the page.
- Select a user to view detailed information imported from Keycloak.
- To view groups, select Group from the entity type filter.
- Browse the list of groups shown on the page.
- From the list of groups, select a group to view the information imported from Keycloak.
