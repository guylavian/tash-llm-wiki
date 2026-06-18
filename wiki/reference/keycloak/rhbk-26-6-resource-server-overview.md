---
title: "Chapter 3. Managing resource servers - Red Hat build of Keycloak 26.6 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-resource-server-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/authorization_services_guide/resource_server_overview
guide: authorization_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 3. Managing resource servers - Red Hat build of Keycloak 26.6 Authorization Services Guide

Chapter 3. Managing resource servers
According to the OAuth2 specification, a resource server is a server hosting the protected resources and capable of accepting and responding to protected resource requests.
In Red Hat build of Keycloak, resource servers are provided with a rich platform for enabling fine-grained authorization for their protected resources, where authorization decisions can be made based on different access control mechanisms.
Any client application can be configured to support fine-grained permissions. In doing so, you are conceptually turning the client application into a resource server.
3.1. Creating a client application
The first step to enable Red Hat build of Keycloak Authorization Services is to create the client application that you want to turn into a resource server.
Procedure
Click Clients.
Clients
On this page, click Create.
Add Client
-
Type the
Client ID
of the client. For example, my-resource-server. Type the
Root URL
for your application. For example:http://${host}:${port}/my-resource-server
Click Save. The client is created and the client Settings page opens. A page similar to the following is displayed:
Client Settings
3.2. Enabling authorization services
You can turn your OIDC client into a resource server and enable fine-grained authorization.
Procedure
- In the client settings page, scroll down to the Capability Config section.
- Toggle Authorization Enabled to On.
Click Save.
Enabling authorization services
A new Authorization tab is displayed for this client. Click the Authorization tab and a page similar to the following is displayed:
Resource server settings
The Authorization tab contains additional sub-tabs covering the different steps that you must follow to actually protect your application’s resources. Each tab is covered separately by a specific topic in this documentation. But here is a quick description about each one:
Settings
General settings for your resource server. For more details about this page see the Resource Server Settings section.
Resource
From this page, you can manage your application’s resources.
Authorization Scopes
From this page, you can manage scopes.
Policies
From this page, you can manage authorization policies and define the conditions that must be met to grant a permission.
Permissions
From this page, you can manage the permissions for your protected resources and scopes by linking them with the policies you created.
Evaluate
From this page, you can simulate authorization requests and view the result of the evaluation of the permissions and authorization policies you have defined.
Export Settings
From this page, you can export the authorization settings to a JSON file.
3.2.1. Resource server settings
On the Resource Server Settings page, you can configure the policy enforcement mode, allow remote resource management, and export the authorization configuration settings.
Policy Enforcement Mode
Specifies how policies are enforced when processing authorization requests sent to the server.
Enforcing
(default mode) Requests are denied by default even when there is no policy associated with a given resource.
Permissive
Requests are allowed even when there is no policy associated with a given resource.
Disabled
Disables the evaluation of all policies and allows access to all resources.
Decision Strategy
This configuration changes how the policy evaluation engine decides whether or not a resource or scope should be granted based on the outcome from all evaluated permissions.
Affirmative
means that at least one permission must evaluate to a positive decision in order grant access to a resource and its scopes.Unanimous
means that all permissions must evaluate to a positive decision in order for the final decision to be also positive. As an example, if two permissions for a same resource or scope are in conflict (one of them is granting access and the other is denying access), the permission to the resource or scope will be granted if the chosen strategy isAffirmative
. Otherwise, a single deny from any permission will also deny access to the resource or scope.Remote Resource Management
Specifies whether resources can be managed remotely by the resource server. If false, resources can be managed only from the administration console.
3.3. Export and import authorization configuration
The configuration settings for a resource server (or client) can be exported and downloaded. You can also import an existing configuration file for a resource server. Importing and exporting a configuration file is helpful when you want to create an initial configuration for a resource server or to update an existing configuration. The configuration file contains definitions for:
- Protected resources and scopes
- Policies
- Permissions
3.3.1. Exporting a configuration file
Procedure
- Click Clients in the menu.
- Click the client you created as a resource server.
Click the Export tab.
Export Settings
The configuration file is exported in JSON format and displayed in a text area, from which you can copy and paste. You can also click Download to download the configuration file and save it.
3.3.2. Importing a configuration file
You can import a configuration file for a resource server.
Procedure
Navigate to the Resource Server Settings page.
Import Settings
- Click Import and choose a file containing the configuration that you want to import.
