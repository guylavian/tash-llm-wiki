---
title: "Chapter 11. Controlling access to the Admin Console - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-admin-permissions
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/admin_permissions
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 11. Controlling access to the Admin Console - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 11. Controlling access to the Admin Console
Each realm created on the Red Hat build of Keycloak has a dedicated Admin Console from which that realm can be managed. The master
realm is a special realm that allows admins to manage more than one realm on the system. This chapter goes over all the scenarios for this.
11.1. Master realm access control
The master
realm in Red Hat build of Keycloak is a special realm and treated differently than other realms. Users in the Red Hat build of Keycloak master
realm can be granted permission to manage zero or more realms that are deployed on the Red Hat build of Keycloak server. When a realm is created, Red Hat build of Keycloak automatically creates various roles that grant fine-grain permissions to access that new realm. Access to The Admin Console and Admin REST endpoints can be controlled by mapping these roles to users in the master
realm. It’s possible to create multiple superusers, as well as users that can only manage specific realms.
11.1.1. Global roles
There are two realm-level roles in the master
realm. These are:
- admin
- create-realm
Users with the admin
role are superusers and have full access to manage any realm on the server. Users with the create-realm
role are allowed to create new realms. They will be granted full access to any new realm they create.
11.1.2. Realm specific roles
Admin users within the master
realm can be granted management privileges to one or more other realms in the system. Each realm in Red Hat build of Keycloak is represented by a client in the master
realm. The name of the client is <realm name>-realm
. These clients each have client-level roles defined which define varying level of access to manage an individual realm.
The roles available are:
- view-realm
- view-users
- view-clients
- view-events
- manage-realm
- manage-users
- create-client
- manage-clients
- manage-events
- view-identity-providers
- manage-identity-providers
- impersonation
Assign the roles you want to your users and they will only be able to use that specific part of the administration console.
Admins with the manage-users
role will only be able to assign admin roles to users that they themselves have. So, if an admin has the manage-users
role but doesn’t have the manage-realm
role, they will not be able to assign this role.
11.2. Dedicated realm admin consoles
Each realm has a dedicated Admin Console that can be accessed by going to the url /admin/{realm-name}/console
. Users within that realm can be granted realm management permissions by assigning specific user role mappings.
Each realm has a built-in client called realm-management
. You can view this client by going to the Clients
left menu item of your realm. This client defines client-level roles that specify permissions that can be granted to manage the realm.
- view-realm
- view-users
- view-clients
- view-events
- manage-realm
- manage-users
- create-client
- manage-clients
- manage-events
- view-identity-providers
- manage-identity-providers
- impersonation
Assign the roles you want to your users and they will only be able to use that specific part of the administration console.
