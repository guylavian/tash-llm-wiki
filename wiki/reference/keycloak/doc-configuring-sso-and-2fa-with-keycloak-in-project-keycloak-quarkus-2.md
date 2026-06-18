---
title: "Chapter 5. Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite - Red Hat Satellite 6.19 Configuring authentication for Red Hat Satellite users"
type: reference
domain: keycloak
slug: doc-configuring-sso-and-2fa-with-keycloak-in-project-keycloak-quarkus-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html/configuring_authentication_for_red_hat_satellite_users/configuring-sso-and-2fa-with-keycloak-in-project_keycloak-quarkus
guide: configuring_authentication_for_red_hat_satellite_users
documentKind: "Documentation"
---

# Chapter 5. Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite - Red Hat Satellite 6.19 Configuring authentication for Red Hat Satellite users

Chapter 5. Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite
Red Hat build of Keycloak is an open-source identity and access management solution that provides various authentication features. You can integrate Satellite Server with your existing Red Hat build of Keycloak server to delegate user authentication and authorization to Red Hat build of Keycloak.
Red Hat build of Keycloak users can log in using the following login methods:
- User name and password in Satellite web UI
- User name and password in Hammer CLI
Red Hat build of Keycloak users cannot use both Satellite web UI and Hammer CLI authentication in Satellite at the same time.
- Time-based one-time password (TOTP), an implementation of two-factor authentication (2FA)
5.1. Prerequisites for configuring Satellite with Red Hat build of Keycloak authentication
Your Satellite Server and Red Hat build of Keycloak server must meet the following requirements before you configure Red Hat build of Keycloak authentication.
On your Satellite Server:
Install the packages required for registering a Red Hat build of Keycloak client:
# satellite-maintain packages install mod_auth_openidc keycloak-httpd-client-install python3-lxml
Check which
keycloak-httpd-client-install
version is installed:# rpm --query keycloak-httpd-client-install
On the Red Hat build of Keycloak side, ensure you meet the following requirements:
If
keycloak-httpd-client-install
version 1.2 or earlier is installed on your Satellite Server, make sure to use the appropriate context path:-
You can use a Red Hat build of Keycloak server that has been initialized with the
--http-relative-path=/auth
context path. To access a Red Hat build of Keycloak server initialized with--http-relative-path=/auth
from its web UI, go tohttps://rhbk.example.com:8443/auth
. -
If you want to use a different context path, make manual adjustments after the initialization with
/auth
or configure theforeman-openidc_oidc_keycloak_Foreman_Realm.conf
file of the HTTPd service manually. For more information about configuring a different context path, see the Red Hat build of Keycloak Administration Guide.
-
You can use a Red Hat build of Keycloak server that has been initialized with the
-
If
keycloak-httpd-client-install
version 1.3 or later is installed, your Red Hat build of Keycloak server does not need to be initialized with the--http-relative-path=/auth
context path. - Your Red Hat build of Keycloak server uses HTTPS instead of HTTP.
- If the certificates or the CA are self-signed, they have been added to the end-user certificate truststore.
- Your Red Hat build of Keycloak account has administrative privileges.
-
A realm is created on the Red Hat build of Keycloak server for Satellite user accounts, for example
Satellite_Realm
. - User accounts have been imported or added to Red Hat build of Keycloak. For more information on importing or creating users, see the Red Hat build of Keycloak Administration Guide.
5.2. Registering Satellite as a client of Red Hat build of Keycloak
To allow Red Hat build of Keycloak users to authenticate to Satellite, you must register Satellite as a client of Red Hat build of Keycloak on your Satellite Server. This configuration requires selecting and configuring the authentication method: Satellite web UI access or Hammer CLI access.
Perform these steps on your Satellite Server.
Procedure
Choose the authentication method you want Red Hat build of Keycloak users to use when authenticating to Satellite:
If you want users to authenticate by using the Satellite web UI:
Create a client for Satellite. Use
foreman-openidc
as the application name.# keycloak-httpd-client-install --app-name foreman-openidc \ --keycloak-server-url "https://rhbk.example.com:8443" \ --keycloak-admin-username "admin" \ --keycloak-realm "Satellite_Realm" \ --keycloak-admin-realm master \ --keycloak-auth-role root-admin \ -t openidc -l /users/extlogin --force
Configure Satellite to use Red Hat build of Keycloak as an authentication source for Satellite web UI:
# satellite-installer --foreman-keycloak true \ --foreman-keycloak-app-name "foreman-openidc" \ --foreman-keycloak-realm "Satellite_Realm"
If you want users to authenticate by using the Hammer CLI:
Create a client for Satellite. Use
hammer-openidc
as the application name.# keycloak-httpd-client-install --app-name hammer-openidc \ --keycloak-server-url "https://rhbk.example.com:8443" \ --keycloak-admin-username "admin" \ --keycloak-realm "Satellite_Realm" \ --keycloak-admin-realm master \ --keycloak-auth-role root-admin \ -t openidc -l /users/extlogin --force
Configure Satellite to use Red Hat build of Keycloak as an authentication source for Hammer CLI:
# satellite-installer --foreman-keycloak true \ --foreman-keycloak-app-name "hammer-openidc" \ --foreman-keycloak-realm "Satellite_Realm"
Restart the
httpd
service:# systemctl restart httpd
5.3. Configuring the Satellite client in Red Hat build of Keycloak
On the Red Hat build of Keycloak side, you must configure the Satellite client with valid redirect URIs and mappers. This includes setting the appropriate client authentication mode, redirect URIs, and necessary mappers to support Satellite web UI or Hammer CLI authentication.
Perform these steps in the Red Hat build of Keycloak web UI.
Procedure
- Go to the realm created for Satellite users.
- Navigate to Clients and click the Satellite client.
On the Settings tab for the Satellite client, configure the access type and redirect addresses:
If you are configuring a client that will provide Satellite web UI authentication:
- Enable Client authentication.
-
You will see a pre-defined URI:
https://satellite.example.com/users/extlogin/redirect_uri
. Do not change or remove this URI. -
Add another URI below the pre-defined URI:
https://satellite.example.com/users/extlogin
If you are configuring a client that will provide Hammer CLI authentication:
- Ensure Client authentication is disabled.
-
You will see a pre-defined URI:
https://satellite.example.com/users/extlogin/redirect_uri
. Do not change or remove this URI. -
Add another URI below the pre-defined URI:
urn:ietf:wg:oauth:2.0:oob
On the Client Scopes tab for the Satellite client, locate the client scope dedicated to the Satellite client named
client-name-dedicated
. Start editing the client scope.On the Mappers tab for
client-name-dedicated
, add a new mapper by configuration. Select the Audience mapper type.- From the Included Client Audience list, select the Satellite client.
- Enable Add to ID token.
- Click Save.
Add another mapper by configuration. Select the Group Membership mapper type. This adds a group mapper so that you can specify authorization in Satellite based on group membership.
- In the Token Claim Name field, enter groups.
- Disable Full group path.
- Click Save.
Additional resources
5.4. Configuring a Satellite client to provide Satellite web UI authentication with Red Hat build of Keycloak
If you are configuring a client that will provide Satellite web UI authentication to your Satellite deployment, delegate authentication to the Red Hat build of Keycloak server and add Red Hat build of Keycloak as an external authentication source in Satellite.
Perform these steps in the Satellite web UI.
Prerequisites
- Ensure that the Client authentication setting in the Satellite client in the Red Hat build of Keycloak web UI is enabled. For more information, see Section 5.3, “Configuring the Satellite client in Red Hat build of Keycloak”.
Procedure
- In the Satellite web UI, navigate to Administer > Settings.
On the Authentication tab, configure the following settings:
-
Authorize login delegation: Set to
Yes
. -
Authorize login delegation auth source user autocreate: Set to
External
. -
Login delegation logout URL: Set to
https://satellite.example.com/users/extlogout
. -
OIDC Algorithm: For example, set to
RS256
. - OIDC Audience: Set to the client ID for Red Hat build of Keycloak.
OIDC Issuer:
-
Set to
https://rhbk.example.com:8443/realms/Satellite_Realm
if you initialized your Red Hat build of Keycloak server without the--http-relative-path=/auth
context path. -
Set to
https://rhbk.example.com:8443/auth/realms/Satellite_Realm
if you initialized your Red Hat build of Keycloak server with the--http-relative-path=/auth
context path.
-
Set to
OIDC JWKs URL:
-
Set to
https://rhbk.example.com:8443/realms/Satellite_Realm/protocol/openid-connect/certs
if you initialized your Red Hat build of Keycloak server without the--http-relative-path=/auth
context path. -
Set to
https://rhbk.example.com:8443/auth/realms/Satellite_Realm/protocol/openid-connect/certs
if you initialized your Red Hat build of Keycloak server with the--http-relative-path=/auth
context path.
-
Set to
-
Authorize login delegation: Set to
Navigate to Administer > Authentication Sources.
- From the External menu, select Edit.
- On the Locations tab, add the locations that you want to be able to use the Red Hat build of Keycloak authentication source.
- On the Organizations tab, add the organizations that you want to be able to use the Red Hat build of Keycloak authentication source.
- Click Submit.
5.5. Configuring a Satellite client to provide Hammer CLI authentication with Red Hat build of Keycloak
If you are configuring a client that will provide Hammer CLI authentication to your Satellite deployment, delegate authentication to the Red Hat build of Keycloak server and add Red Hat build of Keycloak as an external authentication source in Satellite.
Perform these steps on the Satellite client registered to Red Hat build of Keycloak.
Prerequisites
- Ensure that the Client authentication setting in the Satellite client in the Red Hat build of Keycloak web UI is disabled. For more information, see Section 5.3, “Configuring the Satellite client in Red Hat build of Keycloak”.
-
If you initialized your Red Hat build of Keycloak server without the
--http-relative-path=/auth
context path, obtain the values to configure Satellite settings from the following URL:https://rhbk.example.com:8443/realms/Satellite_Realm/.well-known/openid-configuration
. Replace Satellite_Realm with the name of the Red Hat build of Keycloak realm created for your Satellite Server. -
If you initialized your Red Hat build of Keycloak server with the
--http-relative-path=/auth
context path, obtain the values to configure Satellite settings from the following URL:https://rhbk.example.com:8443/auth/realms/Satellite_Realm/.well-known/openid-configuration
. Replace Satellite_Realm with the name of the Red Hat build of Keycloak realm created for your Satellite Server.
Procedure
Set the login delegation to
true
so that users can authenticate using the Open IDC protocol:$ hammer settings set --name authorize_login_delegation --value true
Set the login delegation logout URL:
$ hammer settings set --name login_delegation_logout_url \ --value https://satellite.example.com/users/extlogout
Set the algorithm for encoding: For example, to use the
RS256
algorithm:$ hammer settings set --name oidc_algorithm --value 'RS256'
Add the value for the Hammer client in the Open IDC audience:
$ hammer settings set --name oidc_audience \ --value "['satellite.example.com-hammer-openidc']"
Set the value for the Open IDC issuer:
If you initialized your Red Hat build of Keycloak server without the
--http-relative-path=/auth
context path:$ hammer settings set --name oidc_issuer \ --value "https://rhbk.example.com:8443/realms/Satellite_Realm"
If you initialized your Red Hat build of Keycloak server with the
--http-relative-path=/auth
context path:$ hammer settings set --name oidc_issuer \ --value "https://rhbk.example.com:8443/auth/realms/Satellite_Realm"
Set the value for Open IDC Java Web Token (JWT):
If you initialized your Red Hat build of Keycloak server without the
--http-relative-path=/auth
context path:$ hammer settings set --name oidc_jwks_url \ --value "https://rhbk.example.com:8443/realms/Satellite_Realm/protocol/openid-connect/certs"
If you initialized your Red Hat build of Keycloak server with the
--http-relative-path=/auth
context path:$ hammer settings set --name oidc_jwks_url \ --value "https://rhbk.example.com:8443/auth/realms/Satellite_Realm/protocol/openid-connect/certs"
Retrieve the ID of the Red Hat build of Keycloak authentication source:
$ hammer auth-source external list
Set the location and organization:
$ hammer auth-source external update \ --id My_Authentication_Source_ID \ --location-ids My_Location_ID \ --organization-ids My_Organization_ID
5.6. Configuring Satellite with Red Hat build of Keycloak for TOTP authentication
If you want users to authenticate with time-based one-time passwords (TOTP), configure an OTP policy for the Satellite realm in Red Hat build of Keycloak.
Procedure
- In the Red Hat build of Keycloak web UI, navigate to the Satellite realm.
- Navigate to Authentication.
- On the Policies tab, click the OTP Policy tab. Ensure that the Supported Applications field includes FreeOTP or Google Authenticator.
- Configure the OTP settings to suit your requirements.
- On Required Actions tab, enable the Set as default action setting for the Configure OTP action.
5.7. Configuring group mapping for Red Hat build of Keycloak authentication
Optionally, to implement the role-based access control (RBAC), create a group in Satellite, assign a role to this group, and map an Red Hat build of Keycloak group to the Satellite group. Anyone in the given group in Red Hat build of Keycloak will log in under the corresponding Satellite group.
For example, you can configure users of the Satellite-admin user group defined in Active Directory to authenticate as users with administrator privileges on Satellite.
If you do not configure group mapping, every user will receive the Default role permissions.
Procedure
- In the Satellite web UI, navigate to Administer > User Groups.
Click Create User Group.
- In the Name field, enter a name for the user group. Enter a name that is different from the Active Directory user group name.
- Do not add any users or user groups to the new group in Satellite web UI.
- On the Roles tab, select Administer.
On the External Groups tab, click Add external user group.
- In the Name field, enter the name of the Active Directory group.
- From the Auth Source drop-down menu, select EXTERNAL.
- Click Submit.
5.8. Logging in to Satellite configured with Red Hat build of Keycloak as an authentication source
With Red Hat build of Keycloak configured as an authentication source for Satellite, users defined in a Red Hat build of Keycloak realm can log in to Satellite Server. The available login methods depend on how you configured integration between Red Hat build of Keycloak and Satellite.
Procedure
-
To authenticate to the Satellite web UI, in your browser, go to
https://satellite.example.com
and enter your credentials. To authenticate to the Satellite web UI by using Red Hat build of Keycloak TOTP:
- In your browser, log in to Satellite. Satellite redirects you to the Red Hat build of Keycloak login screen.
- Enter your username and password, and click Log In.
- On your first login attempt, Red Hat build of Keycloak requests you to configure your client by scanning the bar code and entering your PIN. Once authenticated, your browser redirects you back to Satellite and logs you in.
To authenticate to the Satellite CLI with Hammer:
Ensure that Hammer is configured to enforce session usage in
~/.hammer/cli.modules.d/foreman.yml
::foreman: :use_sessions: true
Initiate an authentication session with
hammer auth login oauth
:If you initialized your Red Hat build of Keycloak server without the
--http-relative-path=/auth
context path:$ hammer auth login oauth \ --oidc-token-endpoint 'https://rhbk.example.com:8443/realms/Satellite_realm/protocol/openid-connect/token' \ --oidc-authorization-endpoint 'https://rhbk.example.com:8443' \ --oidc-client-id 'satellite.example.com-hammer-openidc' \ --oidc-redirect-uri urn:ietf:wg:oauth:2.0:oob
If you initialized your Red Hat build of Keycloak server with the
--http-relative-path=/auth
context path:$ hammer auth login oauth \ --oidc-token-endpoint 'https://rhbk.example.com:8443/auth/realms/Satellite_realm/protocol/openid-connect/token' \ --oidc-authorization-endpoint 'https://rhbk.example.com:8443/auth' \ --oidc-client-id 'satellite.example.com-hammer-openidc' \ --oidc-redirect-uri urn:ietf:wg:oauth:2.0:oob
To authenticate to the Satellite CLI with Hammer by using Red Hat build of Keycloak TOTP:
Ensure that Hammer is configured to enforce session usage in
~/.hammer/cli.modules.d/foreman.yml
::foreman: :use_sessions: true
Initiate an authentication session by using
--two-factor
withhammer auth login oauth
:$ hammer auth login oauth \ --two-factor \ --oidc-token-endpoint 'https://rhbk.example.com:8443/auth/realms/Satellite_realm/protocol/openid-connect/token' \ --oidc-authorization-endpoint 'https://rhbk.example.com:8443/auth' \ --oidc-client-id 'satellite.example.com-hammer-openidc' \ --oidc-redirect-uri urn:ietf:wg:oauth:2.0:oob
- You will be prompted to enter a success code. To retrieve the success code, navigate to the URL that the command returns.
- Enter the success code in CLI.
