---
title: "Chapter 2. Red Hat single sign-on and Red Hat build of Keycloak for the 3scale API Management Admin Portal - Red Hat 3scale API Management 2.15 Admin Portal Guide"
type: reference
domain: keycloak
slug: doc-admin-portal-sso-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_3scale_api_management/2.15/html/admin_portal_guide/admin-portal-sso
guide: admin_portal_guide
documentKind: "Documentation"
abstract: "This guide provides information about how to configure and use Red Hat single sign-on and Red Hat build of Keycloak with the 3scale API Management Admin Portal. 2.1. Enable Red Hat single sign-on, Red Hat build of Keycloak or Auth0 member authentication 3scale supports single sign-on (SS0) authentication for your members and administrators. The 3scale Admin Portal supports the following SSO provid…"
---

# Chapter 2. Red Hat single sign-on and Red Hat build of Keycloak for the 3scale API Management Admin Portal - Red Hat 3scale API Management 2.15 Admin Portal Guide

Chapter 2. Red Hat single sign-on and Red Hat build of Keycloak for the 3scale API Management Admin Portal
This guide provides information about how to configure and use Red Hat single sign-on and Red Hat build of Keycloak with the 3scale API Management Admin Portal.
2.1. Enable Red Hat single sign-on, Red Hat build of Keycloak or Auth0 member authentication
3scale supports single sign-on (SS0) authentication for your members and administrators.
The 3scale Admin Portal supports the following SSO providers, each which support a number of identity brokering and member federation options:
You can enable multiple SSO member authentication types.
Only users that have been added to Red Hat single sign-on, Red Hat build of Keycloak or Auth0 will be able to access your 3scale Admin Portal through SSO. If you want to further restrict the access by either roles or user groups you should refer to the corresponding step by step tutorials on the Red Hat single sign-on, Red Hat build of Keycloak or Auth0 support portals.
Once you have established SSO through your chosen provider, you must configure it and enable it on the 3scale Admin Portal.
2.1.1. Single sign-on prerequisites
- A single sign-on instance and realm configured as described under the Developer Portal authentication section of the documentation.
2.1.2. Auth0 prerequisites
- An Auth0 Subscription and account.
2.1.3. Enable Red Hat single sign-on
As an administrator, perform the following steps in the 3scale Admin Portal to enable Red Hat single sign-on, Red Hat build of Keycloak or Auth0:
- Ensure your preferred SSO provider, highlighted in the prerequisites, is properly configured.
Navigate to SSO Integrations in the Account Settings:
- Click the gear icon in the upper right corner of the page
- Navigate to Account Settings (gear icon) > Users > SSO Integrations, and click Create a new SSO integration.
- Select your SSO provider from the dropdown list.
Enter the required information, provided when you configured your SSO:
- Client
- Client Secret
- Realm or Site
- Click Create Authentication Provider
If, during testing, you encounter a callback URL mismatch, add the callback URL shown in the error message to your Auth0 allowed callback URLs.
2.2. Using Red Hat single sign-on and Red Hat build of Keycloak with 3scale API Management
Once you have configured SSO, members can sign on using the account credentials in connected Identity Providers (IdPs).
Follow these steps to log in to the 3scale API Management Admin Portal using SSO:
Navigate to your 3scale login page:
https://<organization>-admin.3scale.net/p/login
- Authorize 3scale with your IdP
- If necessary, complete sign up by entering any needed information
Once you successfully sign up, you will have a member account under the application programming interface (API) provider organization, and you will be automatically logged in.
2.3. Redirecting a 3scale login to a Red Hat single sign-on or Red Hat build of Keycloak option
This section describes the redirection to an IdP login window via Red Hat single sign-on. As a 3scale API Management administrator, complete these steps to have your 3scale account accessible through an optional SSO login page.
2.3.1. Prerequisites
- 3scale 2.15
- A Red Hat single sign-on or Red Hat build of Keycloak instance and realm configured as described under the Configuring Red Hat single sign-on section of the Developer Portal documentation.
Before you can integrate Red Hat single sign-on and Red Hat build of Keycloak with 3scale, you must have a working Red Hat single sign-on or Red Hat build of Keycloak instance. Refer to the Red Hat single sign-on documentation for installation instructions: Installing Red Hat single sign-on 7.6 or Red Hat build of Keycloak 24.0 Server guide.
2.3.2. Required steps
- Access and follow the instructions for setting up Red Hat single sign-on under the Red Hat single sign-on and Red Hat build of Keycloak for the 3scale Admin Portal section of the 3scale documentation.
Provide your Red Hat single sign-on or Red Hat build of Keycloak administrator with your 3scale URL that will form the basis for a redirect within single sign-on for your secure logon. Use the following URL format:
https://<organization>-admin.3scale.net/auth/<system_name>/bounce
<system_name>
can be fetched via the SSO Integration detail page of the Admin Portal:https://<organization>.3scale.net/p/admin/account/authentication_providers/<ID>
keycloak_0123456aaaaa
can also be found via the SSO Integration detail page in theCallback URL for OAuth flow test
field, which looks like the following:https://<organization>.3scale.net/auth/keycloak_0123456aaaaa/callback
