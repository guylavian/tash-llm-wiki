---
title: "Chapter 5. Configuring Ansible Automation Platform Central Authentication Generic OIDC settings and Red Hat SSO/keycloak for Red Hat SSO and Ansible Automation Platform - Red Hat Ansible Automation Platform 2.4 Installing and configuring central authentication for the Ansible Automation Platform"
type: reference
domain: keycloak
slug: doc-configuring-central-auth-generic-oidc-settings
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/installing_and_configuring_central_authentication_for_the_ansible_automation_platform/configuring-central-auth-generic-oidc-settings
guide: installing_and_configuring_central_authentication_for_the_ansible_automation_platform
documentKind: "Documentation"
---

# Chapter 5. Configuring Ansible Automation Platform Central Authentication Generic OIDC settings and Red Hat SSO/keycloak for Red Hat SSO and Ansible Automation Platform - Red Hat Ansible Automation Platform 2.4 Installing and configuring central authentication for the Ansible Automation Platform

Chapter 5. Configuring Ansible Automation Platform Central Authentication Generic OIDC settings and Red Hat SSO/keycloak for Red Hat SSO and Ansible Automation Platform
Ansible Automation Platform Central Authentication allows for the setting of generic OIDC settings and Red Hat SSO/keycloak for Red Hat SSO and Ansible Automation Platform.
5.1. Prerequisites
- You are able to log in as an admin user.
5.2. Configuring Central Authentication Generic OIDC settings
Procedure
Log in to RH-SSO as admin.
NoteIf you have an existing realm you may go to step 6.
- Add Realm.
- Enter Name and click .
- Click the Clients tab.
- Enter name and click .
-
From the navigation panel, select
. -
From the navigation panel, select
. - In the Root URL field, enter your Ansible Automation Platform server IP or hostname.
- In the Valid Redirect field, enter your Ansible Automation Platform server IP or hostname. If not in production, set to *.
- In the Web origins field, enter your Ansible Automation Platform server IP or hostname. If not in production, set to *.
Click the Credentials tab.
NoteKeep track of the Secret to be used later.
- Log in to Ansible Automation Platform Controller as admin.
- From the navigation panel, select .
- Select Generic OIDC settings from the list of Authentication options.
- Click .
- In the OIDC Key field, enter the name of your client from step 5.
- In the OIDC Secret field, enter the secret saved from step 8.
- In the OIDC Provider URL field, enter your keycloak server URL and port.
- Click .
OIDC should appear as an option for login. Click
and it will redirect you to the SSO server for login and redirection back to Ansible Automation Platform.
