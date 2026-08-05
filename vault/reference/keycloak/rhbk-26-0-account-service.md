---
title: "Chapter 17. Account Console - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-account-service
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/account-service
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "Red Hat build of Keycloak users can manage their accounts through the Account Console. They can configure their profiles, add two-factor authentication, include identity provider accounts, and oversee device activity. Additional resources The Account Console can be configured in terms of appearance and language preferences. An example is adding additional attributes to the Personal info page. For …"
---

# Chapter 17. Account Console - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 17. Account Console
Red Hat build of Keycloak users can manage their accounts through the Account Console. They can configure their profiles, add two-factor authentication, include identity provider accounts, and oversee device activity.
17.1. Accessing the Account Console
Procedure
- Make note of the realm name and IP address for the Red Hat build of Keycloak server where your account exists.
- In a web browser, enter a URL in this format: server-root/realms/{realm-name}/account.
- Enter your login name and password.
Account Console
17.2. Configuring ways to sign in
You can sign in to this console using basic authentication (a login name and password) or two-factor authentication. For two-factor authentication, use one of the following procedures.
17.2.1. Two-factor authentication with OTP
Prerequisites
- OTP is a valid authentication mechanism for your realm.
Procedure
- Click Account security in the menu.
- Click Signing in.
Click Set up Authenticator application.
Signing in
- Follow the directions that appear on the screen to use your mobile device as your OTP generator.
- Scan the QR code in the screen shot into the OTP generator on your mobile device.
- Log out and log in again.
- Respond to the prompt by entering an OTP that is provided on your mobile device.
17.2.2. Two-factor authentication with WebAuthn
Prerequisites
- WebAuthn is a valid two-factor authentication mechanism for your realm. Please follow the WebAuthn section for more details.
Procedure
- Click Account Security in the menu.
- Click Signing In.
Click Set up a Passkey.
Signing In
- Prepare your Passkey. How you prepare this key depends on the type of Passkey you use. For example, for a USB based Yubikey, you may need to put your key into the USB port on your laptop.
- Click Register to register your Passkey.
- Log out and log in again.
- Assuming authentication flow was correctly set, a message appears asking you to authenticate with your Passkey as second factor.
17.2.3. Passwordless authentication with WebAuthn
Prerequisites
- WebAuthn is a valid passwordless authentication mechanism for your realm. Please follow the Passwordless WebAuthn section for more details.
Procedure
- Click Account Security in the menu.
- Click Signing In.
Click Set up a Passkey in the Passwordless section.
Signing In
- Prepare your Passkey. How you prepare this key depends on the type of Passkey you use. For example, for a USB based Yubikey, you may need to put your key into the USB port on your laptop.
- Click Register to register your Passkey.
- Log out and log in again.
- Assuming authentication flow was correctly set, a message appears asking you to authenticate with your Passkey as second factor. You no longer need to provide your password to log in.
17.3. Viewing device activity
You can view the devices that are logged in to your account.
Procedure
- Click Account security in the menu.
- Click Device activity.
- Log out a device if it looks suspicious.
Devices
17.4. Adding an identity provider account
You can link your account with an identity broker. This option is often used to link social provider accounts.
Procedure
- Log into the Admin Console.
- Click Identity providers in the menu.
- Select a provider and complete the fields.
- Return to the Account Console.
- Click Account security in the menu.
- Click Linked accounts.
The identity provider you added appears in this page.
Linked Accounts
17.5. Accessing other applications
The Applications menu item shows users which applications you can access. In this case, only the Account Console is available.
Applications
17.6. Viewing group memberships
You can view the groups you are associated with by clicking the Groups menu. If you select Direct membership checkbox, you will see only the groups you are direct associated with.
Prerequisites
- You need to have the view-groups account role for being able to view Groups menu.
View group memberships
