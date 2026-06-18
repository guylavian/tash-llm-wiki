---
title: "Chapter 1. Getting started - Red Hat build of Keycloak 26.2 Getting Started Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-getting-started-zip
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/getting_started_guide/getting-started-zip-
guide: getting_started_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 1. Getting started - Red Hat build of Keycloak 26.2 Getting Started Guide

Chapter 1. Getting started
Get started with Red Hat build of Keycloak on a physical or virtual server.
1.1. Before you start
Make sure your machine or container platform can provide sufficient memory and CPU for your desired usage of Red Hat build of Keycloak. See Concepts for sizing CPU and memory resources for more on how to get started with production sizing.
Make sure you have OpenJDK 21 installed.
1.2. Download Red Hat build of Keycloak
Download Red Hat build of Keycloak from the Red Hat website and extract it.
After extracting this file, you should have a directory that is named rhbk-26.2.15
.
1.3. Start Red Hat build of Keycloak
-
From a terminal, open the
rhbk-26.2.15
directory. Enter the following command:
On Linux, run:
bin/kc.sh start-dev
On Windows, run:
bin\kc.bat start-dev
Using the start-dev
option, you are starting Red Hat build of Keycloak in development mode. In this mode, you can try out Red Hat build of Keycloak for the first time to get it up and running quickly. This mode offers convenient defaults for developers, such as for developing a new Red Hat build of Keycloak theme.
1.4. Create an admin user
Red Hat build of Keycloak has no default admin user. You need to create an admin user before you can start Keycloak.
- Open http://localhost:8080/.
- Fill in the form with your preferred username and password.
1.5. Log in to the Admin Console
- Go to the Red Hat build of Keycloak Admin Console.
- Log in with the username and password you created earlier.
1.6. Create a realm
A realm in Red Hat build of Keycloak is equivalent to a tenant. Each realm allows an administrator to create isolated groups of applications and users. Initially, Red Hat build of Keycloak includes a single realm, called master
. Use this realm only for managing Red Hat build of Keycloak and not for managing any applications.
Use these steps to create the first realm.
- Open the Red Hat build of Keycloak Admin Console.
- Click Create Realm next to Current realm.
-
Enter
myrealm
in the Realm name field. - Click Create.
Figure 1.1. Add realm
1.7. Create a user
Initially, the realm has no users. Use these steps to create a user:
- Verify that you are still in the myrealm realm, which is next to Current realm.
- Click Users in the left-hand menu.
- Click Create new user.
Fill in the form with the following values:
-
Username:
myuser
- First name: any first name
- Last name: any last name
-
Username:
- Click Create.
Figure 1.2. Create user
This user needs a password to log in. To set the initial password:
- Click Credentials at the top of the page.
- Fill in the Set password form with a password.
- Toggle Temporary to Off so that the user does not need to update this password at the first login.
Figure 1.3. Set password
1.8. Log in to the Account Console
You can now log in to the Account Console to verify this user is configured correctly.
- Open the Red Hat build of Keycloak Account Console.
-
Log in with
myuser
and the password you created earlier.
As a user in the Account Console, you can manage your account including modifying your profile, adding two-factor authentication, and including identity provider accounts.
1.9. Secure the first application
To secure the first application, you start by registering the application with your Red Hat build of Keycloak instance:
- Open the Red Hat build of Keycloak Admin Console.
- Click myrealm next to Current realm.
- Click Clients.
- Click Create client
Fill in the form with the following values:
-
Client type:
OpenID Connect
Client ID:
myclient
Figure 1.4. Add client
-
Client type:
- Click Next
- Confirm that Standard flow is enabled.
- Click Next.
Make these changes under Login settings.
-
Set Valid redirect URIs to
https://www.keycloak.org/app/*
-
Set Web origins to
https://www.keycloak.org
-
Set Valid redirect URIs to
- Click Save.
Figure 1.5. Update client
To confirm the client was created successfully, you can use the SPA testing application on the Keycloak website.
- Open https://www.keycloak.org/app/.
- Click Save to use the default configuration.
- Click Sign in to authenticate to this application using the Red Hat build of Keycloak server you started earlier.
1.10. Taking the next step
Before you run Red Hat build of Keycloak in production, consider the following actions:
- Switch to a production ready database such as PostgreSQL.
- Configure SSL with your own certificates.
- Switch the admin password to a more secure password.
For more information, see the Server Configuration Guide.
