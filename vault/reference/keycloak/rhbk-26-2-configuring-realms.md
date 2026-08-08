---
title: "Chapter 3. Configuring realms - Red Hat build of Keycloak 26.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-configuring-realms
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_administration_guide/configuring-realms
guide: server_administration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Once you have an administrative account for the Admin Console, you can configure realms. A realm is a space where you manage objects, including users, applications, roles, and groups. A user belongs to and logs into a realm. One Red Hat build of Keycloak deployment can define, store, and manage as many realms as there is space for in the database. 3.1. Using the Admin Console You configure realms …"
---

# Chapter 3. Configuring realms - Red Hat build of Keycloak 26.2 Server Administration Guide

Chapter 3. Configuring realms
Once you have an administrative account for the Admin Console, you can configure realms. A realm is a space where you manage objects, including users, applications, roles, and groups. A user belongs to and logs into a realm. One Red Hat build of Keycloak deployment can define, store, and manage as many realms as there is space for in the database.
3.1. Using the Admin Console
You configure realms and perform most administrative tasks in the Red Hat build of Keycloak Admin Console.
Prerequisites
To use the Admin Console, you need an administrator account.
- If no administrators exist, see Creating the first administrator.
- If other administrators exist, ask an administrator to provide an account with privileges to manage realms.
Procedure
Go to the URL for the Admin Console.
For example, for localhost, use this URL: http://localhost:8080/admin/
Enter the username and password you created on the Welcome Page or through environment variables as described in Creating the initial admin user.
Login page
This action displays the Admin Console.
Admin Console
Note the menus and other options that you can use:
- Click the Current realm to see if other realms are available to be managed.
- Click Create realm to create another realm that you can manage.
- Click the top right list to view your account or log out.
Click Realm settings in the menu to see the fields and options for this realm.
Click a question mark ? icon to show the definition of a field such as Frontend URL.
Realm settings
Export files from the Admin Console are not suitable for backups or data transfer between servers. Only boot-time exports are suitable for backups or data transfer between servers.
3.2. The master realm
In the Admin Console, two types of realms exist:
-
Master realm
- This realm was created for you when you first started Red Hat build of Keycloak. It contains the administrator account you created at the first login. Use the master realm only to create and manage the realms in your system. -
Other realms
- These realms are created by the administrator in the master realm. In these realms, administrators manage the users in your organization and the applications they need. The applications are owned by the users.
Realms and applications
Realms are isolated from one another and can only manage and authenticate the users that they control. Following this security model helps prevent accidental changes and follows the tradition of permitting user accounts access to only those privileges and powers necessary for the successful completion of their current task.
Additional resources
- See Dedicated Realm Admin Consoles if you want to disable the master realm and define administrator accounts within any new realm you create. Each realm has its own dedicated Admin Console that you can log into with local accounts.
3.3. Creating a realm
You create a realm to provide a management space where you can create users and give them permissions to use applications. At first login, you are typically in the master realm, the top-level realm from which you create other realms.
When deciding what realms you need, consider the kind of isolation you want to have for your users and applications. For example, you might create a realm for the employees of your company and a separate realm for your customers. Your employees would log into the employee realm and only be able to visit internal company applications. Customers would log into the customer realm and only be able to interact with customer-facing apps.
Procedure
- In the Admin Console, click Create Realm next to Current realm.
- Enter a name for the realm.
Click Create.
Create realm
The current realm is now set to the realm you just created. You can switch between realms by clicking the realm name in the menu.
3.4. Configuring SSL for a realm
Each realm has an associated SSL Mode, which defines the SSL/HTTPS requirements for interacting with the realm. Browsers and applications that interact with the realm honor the SSL/HTTPS requirements defined by the SSL Mode or they cannot interact with the server.
Procedure
- Click Realm settings in the menu.
Click the General tab.
General tab
Set Require SSL to one of the following SSL modes:
-
External requests Users can interact with Red Hat build of Keycloak without SSL so long as they stick to private IPv4 addresses such as
localhost
,127.0.0.1
,10.x.x.x
,192.168.x.x
,172.16.x.x
or IPv6 link-local and unique-local addresses. If you try to access Red Hat build of Keycloak without SSL from a non-private IP address, you will get an error. - None Red Hat build of Keycloak does not require SSL. This choice applies only in development when you are experimenting and do not plan to support this deployment.
- All requests Red Hat build of Keycloak requires SSL for all IP addresses.
-
External requests Users can interact with Red Hat build of Keycloak without SSL so long as they stick to private IPv4 addresses such as
3.5. Configuring email for a realm
Red Hat build of Keycloak sends emails to users to verify their email addresses, when they forget their passwords, or when an administrator needs to receive notifications about a server event. To enable Red Hat build of Keycloak to send emails, you provide Red Hat build of Keycloak with your SMTP server settings.
Procedure
- Click Realm settings in the menu.
Click the Email tab.
Email tab
- Fill in the fields and toggle the switches as needed.
Template
- From
- From denotes the address used for the From SMTP-Header for the emails sent.
- From display name
- From display name allows to configure a user-friendly email address aliases (optional). If not set the plain From email address will be displayed in email clients.
- Reply to
- Reply to denotes the address used for the Reply-To SMTP-Header for the mails sent (optional). If not set the plain From email address will be used.
- Reply to display name
- Reply to display name allows to configure a user-friendly email address aliases (optional). If not set the plain Reply To email address will be displayed.
- Envelope from
- Envelope from denotes the Bounce Address used for the Return-Path SMTP-Header for the mails sent (optional).
Connection & Authentication
- Host
- Host denotes the SMTP server hostname used for sending emails.
- Port
- Port denotes the SMTP server port.
- Encryption
- Tick one of these checkboxes to support sending emails for recovering usernames and passwords, especially if the SMTP server is on an external network. You will most likely need to change the Port to 465, the default port for SSL/TLS.
- Authentication
- Set this switch to ON if your SMTP server requires authentication.
- Username
- All authentication-mechanisms require a username.
- Authentication Type
- Choose the kind of authentication: 'password' or 'token'.
- Password
- Only needed when Authentication Type 'password' is selected. Supply the Password. The value of the Password field can refer a value from an external vault.
- Auth Token URL
- Only needed when Authentication Type 'token' is selected. Supply the Auth Token URL that is used to fetch a token via client credentials grant.
- Auth Token Scope
- Only needed when Authentication Type 'token' is selected. Supply the Auth Token Scope that is used to fetch a token from the Auth Token URL.
- Auth Token ClientId
- Only needed when Authentication Type 'token' is selected. Supply the Auth ClientId that is used to fetch a token from the Auth Token URL.
- Auth Token Client Secret
- Only needed when Authentication Type 'token' is selected. Supply the Auth Client Secret that authenticates the client to fetch a token from the Auth Token URL. The value of the Auth Client Secret field can refer a value from an external vault.
- Allow UTF-8
Enable to UTF-8-encode email address when sending them to the server. This should only be enabled if the mail server supports UTF-8 via the SMTPUTF8 extension. If disabled, domain names containing non-ASCII characters will be encoded using punycode, and addresses containing non-ASCII characters in the local part of the address will return an error.
If you do not enable this option, take additional measures to prevent non-ASCII characters in users' email addresses:
- Verifying that no email addresses of existing users have non-ASCII characters in the local part of the email address.
-
Updating the validation of email addresses to prevent non-ASCII characters in the local part of the email address, for example, by adding a regex pattern validation in the user profile for the email address field similar to
\p{ASCII}*@.*
with an error message similar toLocal part of the address must contain only ASCII characters
.
3.6. Configuring themes
For a given realm, you can change the appearance of any UI in Red Hat build of Keycloak by using themes.
Procedure
- Click Realm settings in the menu.
Click the Themes tab.
Themes tab
Pick the theme you want for each UI category and click Save.
- Login theme
- Username password entry, OTP entry, new user registration, and other similar screens related to login.
- Account theme
- The console used by the user to manage his or her account.
- Admin console theme
- The skin of the Red Hat build of Keycloak Admin Console.
- Email theme
- Whenever Red Hat build of Keycloak has to send out an email, it uses templates defined in this theme to craft the email.
Additional resources
- The Server Developer Guide describes how to create a new theme or modify existing ones.
3.7. Enabling internationalization
Every UI screen is internationalized in Red Hat build of Keycloak. The default language is English, but you can choose which locales you want to support and what the default locale will be.
Procedure
- Click Realm Settings in the menu.
- Click the Localization tab.
- Enable Internationalization.
Select the languages you will support.
Localization tab
The next time a user logs in, that user can choose a language on the login page to use for the login screens, Account Console, and Admin Console.
Additional resources
- The Server Developer Guide explains how you can offer additional languages. All internationalized texts which are provided by the theme can be overwritten by realm-specific texts on the Localization tab.
3.7.1. User locale selection
A locale selector provider suggests the best locale on the information available. However, it is often unknown who the user is. For this reason, the previously authenticated user’s locale is remembered in a persisted cookie.
The logic for selecting the locale uses the first of the following that is available:
- User selected - when the user has selected a locale using the drop-down locale selector
- User profile - when there is an authenticated user and the user has a preferred locale set
- Client selected - passed by the client using for example ui_locales parameter
- Cookie - last locale selected on the browser
- Accepted language - locale from Accept-Language header
- Realm default
- If none of the above, fall back to English
When a user is authenticated an action is triggered to update the locale in the persisted cookie mentioned earlier. If the user has actively switched the locale through the locale selector on the login pages the users locale is also updated at this point.
If you want to change the logic for selecting the locale, you have an option to create custom LocaleSelectorProvider
. For details, please refer to the Server Developer Guide.
3.8. Controlling login options
Red Hat build of Keycloak includes several built-in login page features.
3.8.1. Enabling forgot password
If you enable Forgot password
, users can reset their login credentials if they forget their passwords or lose their OTP generator.
Procedure
- Click Realm settings in the menu.
Click the Login tab.
Login tab
Toggle Forgot password to ON.
A
Forgot Password?
link displays in your login pages.Forgot password link
-
Specify
Host
andFrom
in the Email tab in order for Red Hat build of Keycloak to be able to send the reset email. Click this link to bring users where they can enter their username or email address and receive an email with a link to reset their credentials.
Forgot password page
The text sent in the email is configurable. See Server Developer Guide for more information.
When users click the email link, Red Hat build of Keycloak asks them to update their password, and if they have set up an OTP generator, Red Hat build of Keycloak asks them to reconfigure the OTP generator. For security reasons, the flow forces federated users to login again after the reset credentials and keeps internal database users logged in if the same authentication session (same browser) is used. Depending on the security requirements of your organization, you can change the default behavior.
To change this behavior, perform these steps:
Procedure
- Click Authentication in the menu.
- Click the Flows tab.
Select the Reset Credentials flow.
Reset credentials flow
If you do not want to reset the OTP, set the
Reset - Conditional OTP
sub-flow requirement to Disabled.Send Reset Email Configuration
If you want to change default behavior for the force login option, click the Send Reset Email settings icon in the flow, define an Alias, and select the best Force login after reset option for you (
true
, always force re-authentication,false
, keep the user logged in if the same browser was used,only-federated
, default value that forces login again only for federated users).- Click Authentication in the menu.
- Click the Required actions tab.
Ensure Update Password is enabled.
Required Actions
3.8.2. Enabling Remember Me
A logged-in user closing their browser destroys their session, and that user must log in again. You can set Red Hat build of Keycloak to keep the user’s login session open if that user clicks the Remember Me checkbox upon login. This action turns the login cookie from a session-only cookie to a persistence cookie.
Procedure
- Click Realm settings in the menu.
- Click the Login tab.
Toggle the Remember Me switch to On.
Login tab
When you save this setting, a
remember me
checkbox displays on the realm’s login page.Remember Me
Note that disabling the "Remember me" option will invalidate all sessions created with the "Remember me" checkbox selected during login, requiring users to log in again. Any refresh tokens related to these sessions will also become invalid. Note also that the sessions will not be invalidated immediately when the switch is disabled, but only when a cookie or token associated with an invalid session is used. This means that disabling and then re-enabling the "Remember me" switch cannot be used to invalidate old sessions.
3.8.3. ACR to Level of Authentication (LoA) Mapping
In the general settings of a realm, you can define which Authentication Context Class Reference (ACR)
value is mapped to which Level of Authentication (LoA)
. The ACR can be any value, whereas the LoA must be numeric. The acr claim can be requested in the claims
or acr_values
parameter sent in the OIDC request and it is also included in the access token and ID token. The mapped number is used in the authentication flow conditions.
Mapping can be also specified at the client level in case that particular client needs to use different values than realm. However, a best practice is to stick to realm mappings.
For further details see Step-up Authentication and the official OIDC specification.
3.8.4. Update Email Workflow (UpdateEmail)
With this workflow, users will have to use an UPDATE_EMAIL action to change their own email address.
The action is associated with a single email input form. If the realm has email verification disabled, this action will allow to update the email without verification. If the realm has email verification enabled, the action will send an email update action token to the new email address without changing the account email. Only the action token triggering will complete the email update.
Applications are able to send their users to the email update form by leveraging UPDATE_EMAIL as an AIA (Application Initiated Action).
UpdateEmail is Technology Preview and is not fully supported. This feature is disabled by default.
To enable start the server with --features=preview
or --features=update-email
If you enable this feature and you are migrating from a previous version, enable the Update Email required action in your realms. Otherwise, users cannot update their email addresses.
3.9. Configuring realm keys
The authentication protocols that are used by Red Hat build of Keycloak require cryptographic signatures and sometimes encryption. Red Hat build of Keycloak uses asymmetric key pairs, a private and public key, to accomplish this.
Red Hat build of Keycloak has a single active key pair at a time, but can have several passive keys as well. The active key pair is used to create new signatures, while the passive key pair can be used to verify previous signatures. This makes it possible to regularly rotate the keys without any downtime or interruption to users.
When a realm is created, a key pair and a self-signed certificate is automatically generated.
Procedure
- Click Realm settings in the menu.
- Click Keys.
- Select Passive keys from the filter dropdown to view passive keys.
- Select Disabled keys from the filter dropdown to view disabled keys.
A key pair can have the status Active
, but still not be selected as the currently active key pair for the realm. The selected active pair which is used for signatures is selected based on the first key provider sorted by priority that is able to provide an active key pair.
3.9.1. Rotating keys
We recommend that you regularly rotate keys. Start by creating new keys with a higher priority than the existing active keys. You can instead create new keys with the same priority and making the previous keys passive.
Once new keys are available, all new tokens and cookies will be signed with the new keys. When a user authenticates to an application, the SSO cookie is updated with the new signature. When OpenID Connect tokens are refreshed new tokens are signed with the new keys. Eventually, all cookies and tokens use the new keys and after a while the old keys can be removed.
The frequency of deleting old keys is a tradeoff between security and making sure all cookies and tokens are updated. Consider creating new keys every three to six months and deleting old keys one to two months after you create the new keys. If a user was inactive in the period between the new keys being added and the old keys being removed, that user will have to re-authenticate.
Rotating keys also applies to offline tokens. To make sure they are updated, the applications need to refresh the tokens before the old keys are removed.
3.9.2. Adding a generated key pair
Use this procedure to generate a key pair including a self-signed certificate.
Procedure
- Select the realm in the Admin Console.
- Click Realm settings in the menu.
- Click the Keys tab.
- Click the Providers tab.
- Click Add provider and select rsa-generated.
- Enter a number in the Priority field. This number determines if the new key pair becomes the active key pair. The highest number makes the key pair active.
- Select a value for AES Key size.
- Click Save.
Changing the priority for a provider will not cause the keys to be re-generated, but if you want to change the keysize you can edit the provider and new keys will be generated.
3.9.3. Rotating keys by extracting a certificate
You can rotate keys by extracting a certificate from an RSA generated key pair and using that certificate in a new keystore.
Prerequisites
- A generated key pair
Procedure
- Select the realm in the Admin Console.
- Click Realm Settings.
Click the Keys tab.
A list of Active keys appears.
On a row with an RSA key, click Certificate under Public Keys.
The certificate appears in text form.
Save the certificate to a file and enclose it in these lines.
----Begin Certificate---- <Output> ----End Certificate----
- Use the keytool command to convert the key file to PEM Format.
Remove the current RSA public key certificate from the keystore.
keytool -delete -keystore <keystore>.jks -storepass <password> -alias <key>
Import the new certificate into the keystore
keytool -importcert -file domain.crt -keystore <keystore>.jks -storepass <password> -alias <key>
Rebuild the application.
mvn clean install wildfly:deploy
3.9.4. Adding an existing key pair and certificate
To add a key pair and certificate obtained elsewhere select Providers
and choose rsa
from the dropdown. You can change the priority to make sure the new key pair becomes the active key pair.
Prerequisites
- A private key file. The file must be PEM formatted.
Procedure
- Select the realm in the Admin Console.
- Click Realm settings.
- Click the Keys tab.
- Click the Providers tab.
- Click Add provider and select rsa.
- Enter a number in the Priority field. This number determines if the new key pair becomes the active key pair.
- Click Browse… beside Private RSA Key to upload the private key file.
- If you have a signed certificate for your private key, click Browse… beside X509 Certificate to upload the certificate file. Red Hat build of Keycloak automatically generates a self-signed certificate if you do not upload a certificate.
- Click Save.
3.9.5. Loading keys from a Java Keystore
To add a key pair and certificate stored in a Java Keystore file on the host select Providers
and choose java-keystore
from the dropdown. You can change the priority to make sure the new key pair becomes the active key pair.
For the associated certificate chain to be loaded it must be imported to the Java Keystore file with the same Key Alias
used to load the key pair.
Procedure
- Select the realm in the Admin Console.
- Click Realm settings in the menu.
- Click the Keys tab.
- Click the Providers tab.
- Click Add provider and select java-keystore.
- Enter a number in the Priority field. This number determines if the new key pair becomes the active key pair.
-
Enter the desired Algorithm. Note that the algorithm should match the key type (for example
RS256
requires a RSA private key,ES256
a EC private key orAES
an AES secret key). - Enter a value for Keystore. Path to the keystore file.
- Enter the Keystore Password. The option can refer a value from an external vault.
-
Enter a value for Keystore Type (
JKS
,PKCS12
orBCFKS
). - Enter a value for the Key Alias to load from the keystore.
- Enter the Key Password. The option can refer a value from an external vault.
-
Enter a value for Key Use (
sig
for signing orenc
for encryption). Note that the use should match the algorithm type (for exampleRS256
issig
butRSA-OAEP
isenc
) - Click Save.
Not all the keystore types support all types of keys. For example, JKS
in all modes and PKCS12
in fips mode (BCFIPS
provider) cannot store secret key entries.
3.9.6. Making keys passive
Procedure
- Select the realm in the Admin Console.
- Click Realm settings in the menu.
- Click the Keys tab.
- Click the Providers tab.
- Click the provider of the key you want to make passive.
- Toggle Active to Off.
- Click Save.
3.9.7. Disabling keys
Procedure
- Select the realm in the Admin Console.
- Click Realm settings in the menu.
- Click the Keys tab.
- Click the Providers tab.
- Click the provider of the key you want to make passive.
- Toggle Enabled to Off.
- Click Save.
3.9.8. Compromised keys
Red Hat build of Keycloak has the signing keys stored just locally and they are never shared with the client applications, users or other entities. However, if you think that your realm signing key was compromised, you should first generate new key pair as described above and then immediately remove the compromised key pair.
Alternatively, you can delete the provider from the Providers
table.
Procedure
- Click Clients in the menu.
- Click security-admin-console.
- Scroll down to the Access settings section.
- Fill in the Admin URL field.
- Click the Advanced tab.
- Click Set to now in the Revocation section.
- Click Push.
Pushing the not-before policy ensures that client applications do not accept the existing tokens signed by the compromised key. The client application is forced to download new key pairs from Red Hat build of Keycloak also so the tokens signed by the compromised key will be invalid.
REST and confidential clients must set Admin URL so Red Hat build of Keycloak can send clients the pushed not-before policy request.
