---
title: "Chapter 11. Automating client registration with the CLI - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-client-registration-cli
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/client-registration-cli-
guide: securing_applications_and_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Use the CLI to automate client registration. The Client Registration CLI is a command-line interface (CLI) tool for application developers to configure new clients in a self-service manner when integrating with Red Hat build of Keycloak. It is specifically designed to interact with Red Hat build of Keycloak Client Registration REST endpoints. It is necessary to create or obtain a client configurat…"
---

# Chapter 11. Automating client registration with the CLI - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide

Chapter 11. Automating client registration with the CLI
Use the CLI to automate client registration.
The Client Registration CLI is a command-line interface (CLI) tool for application developers to configure new clients in a self-service manner when integrating with Red Hat build of Keycloak. It is specifically designed to interact with Red Hat build of Keycloak Client Registration REST endpoints.
It is necessary to create or obtain a client configuration for any application to be able to use Red Hat build of Keycloak. You usually configure a new client for each new application hosted on a unique host name. When an application interacts with Red Hat build of Keycloak, the application identifies itself with a client ID so Red Hat build of Keycloak can provide a login page, single sign-on (SSO) session management, and other services.
You can configure application clients from a command line with the Client Registration CLI, and you can use it in shell scripts.
To allow a particular user to use Client Registration CLI
, the Red Hat build of Keycloak administrator typically uses the Admin Console to configure a new user with proper roles or to configure a new client and client secret to grant access to the Client Registration REST API.
11.1. Configuring a new regular user for use with Client Registration CLI
Procedure
-
Log in to the Admin Console (for example, http://localhost:8080) as
admin
. - Select a realm to administer.
- If you want to use an existing user, select that user to edit; otherwise, create a new user.
-
Select Role Mapping, Assign role. From the option list, click Filter by clients. In the search bar, type
manage-clients
. Select the role, or if you are in the master realm, select the one with NAME-realm, whereNAME
is the name of the target realm. You can grant access to any other realm to users in the master realm. - Click Assign to grant a full set of client management permissions. Another option is to choose view-clients for read-only or create-client to create new clients.
Select Available Roles, manage-client to grant a full set of client management permissions. Another option is to choose view-clients for read-only or create-client to create new clients.
NoteThese permissions grant the user the capability to perform operations without the use of Initial Access Token or Registration Access Token (see Using the client registration service for more information).
It is possible to not assign any realm-management
roles to a user. In that case, a user can still log in with the Client Registration CLI but cannot use it without an Initial Access Token. Trying to perform any operations without a token results in a 403 Forbidden error.
The administrator can issue Initial Access Tokens from the Admin Console in the Clients area on the Initial Access Token tab.
11.2. Configuring a client for use with the Client Registration CLI
By default, the server recognizes the Client Registration CLI as the admin-cli
client, which is configured automatically for every new realm. No additional client configuration is necessary when logging in with a user name.
Procedure
-
Create a client (for example,
reg-cli
) if you want to use a separate client configuration for the Client Registration CLI. - Uncheck Standard Flow Enabled.
- Strengthen the security by toggling Client authentication to On.
Choose the type of account that you want to use.
- If you want to use a service account associated with the client, check Service accounts roles.
- If you prefer to use a regular user account, check Direct access grants.
- Click Next.
- Click Save.
Click the Credentials tab.
Configure either
Client Id and Secret
orSigned JWT
.If you are using service account roles, click the Service Account Roles tab.
Select the roles to configure the access for the service account. For the details on what roles to select, see Section 11.1, “Configuring a new regular user for use with Client Registration CLI”.
- Click Save.
When you run the kcreg config credentials
, use the --secret
option to supply the configured secret.
-
Specify which
clientId
to use (for example,--client reg-cli
) when runningkcreg config credentials
. -
With the service account enabled, you can omit specifying the user when running
kcreg config credentials
and only provide the client secret or keystore information.
11.3. Installing the Client Registration CLI
The Client Registration CLI is packaged inside the Red Hat build of Keycloak Server distribution. You can find execution scripts inside the bin
directory. The Linux script is called kcreg.sh
, and the Windows script is called kcreg.bat
.
Add the Red Hat build of Keycloak server directory to your PATH
when setting up the client for use from any location on the file system.
For example, on:
- Linux:
$ export PATH=$PATH:$KEYCLOAK_HOME/bin
$ kcreg.sh
- Windows:
c:\> set PATH=%PATH%;%KEYCLOAK_HOME%\bin
c:\> kcreg
KEYCLOAK_HOME
refers to a directory where the Red Hat build of Keycloak Server distribution was unpacked.
11.4. Using the Client Registration CLI
Procedure
- Start an authenticated session by logging in with your credentials.
Run commands on the
Client Registration REST
endpoint.For example, on:
Linux:
$ kcreg.sh config credentials --server http://localhost:8080 --realm demo --user user --client reg-cli $ kcreg.sh create -s clientId=my_client -s 'redirectUris=["http://localhost:8980/myapp/*"]' $ kcreg.sh get my_client
Windows:
c:\> kcreg config credentials --server http://localhost:8080 --realm demo --user user --client reg-cli c:\> kcreg create -s clientId=my_client -s "redirectUris=[\"http://localhost:8980/myapp/*\"]" c:\> kcreg get my_client
NoteIn a production environment, Red Hat build of Keycloak has to be accessed with
https:
to avoid exposing tokens to network sniffers.
If a server’s certificate is not issued by one of the trusted certificate authorities (CAs) that are included in Java’s default certificate truststore, prepare a
truststore.jks
file and instruct the Client Registration CLI to use it.For example, on:
Linux:
$ kcreg.sh config truststore --trustpass $PASSWORD ~/.keycloak/truststore.jks
Windows:
c:\> kcreg config truststore --trustpass %PASSWORD% %HOMEPATH%\.keycloak\truststore.jks
11.4.1. Logging in
Procedure
- Specify a server endpoint URL and a realm when you log in with the Client Registration CLI.
-
Specify a user name or a client id, which results in a special service account being used. When using a user name, you must use a password for the specified user. When using a client ID, you use a client secret or a
Signed JWT
instead of a password.
Regardless of the login method, the account that logs in needs proper permissions to be able to perform client registration operations. Keep in mind that any account in a non-master realm can only have permissions to manage clients within the same realm. If you need to manage different realms, you can either configure multiple users in different realms, or you can create a single user in the master
realm and add roles for managing clients in different realms.
You cannot configure users with the Client Registration CLI. Use the Admin Console web interface or the Admin Client CLI to configure users. See Server Administration Guide for more details.
When kcreg
successfully logs in, it receives authorization tokens and saves them in a private configuration file so the tokens can be used for subsequent invocations. See Section 11.4.2, “Working with alternative configurations” for more information on configuration files.
See the built-in help for more information on using the Client Registration CLI.
For example, on:
- Linux:
$ kcreg.sh help
- Windows:
c:\> kcreg help
See kcreg config credentials --help
for more information about starting an authenticated session.
11.4.2. Working with alternative configurations
By default, the Client Registration CLI automatically maintains a configuration file at a default location, ./.keycloak/kcreg.config
, under the user’s home directory. You can use the --config
option to point to a different file or location to maintain multiple authenticated sessions in parallel. It is the safest way to perform operations tied to a single configuration file from a single thread.
Do not make the configuration file visible to other users on the system. The configuration file contains access tokens and secrets that should be kept private.
You might want to avoid storing secrets inside a configuration file by using the --no-config
option with all of your commands, even though it is less convenient and requires more token requests to do so. Specify all authentication information with each kcreg
invocation.
11.4.3. Initial Access and Registration Access Tokens
Developers who do not have an account configured at the Red Hat build of Keycloak server they want to use can use the Client Registration CLI. This is possible only when the realm administrator issues a developer an Initial Access Token. It is up to the realm administrator to decide how and when to issue and distribute these tokens. The realm administrator can limit the maximum age of the Initial Access Token and the total number of clients that can be created with it.
Once a developer has an Initial Access Token, the developer can use it to create new clients without authenticating with kcreg config credentials
. The Initial Access Token can be stored in the configuration file or specified as part of the kcreg create
command.
For example, on:
- Linux:
$ kcreg.sh config initial-token $TOKEN
$ kcreg.sh create -s clientId=myclient
or
$ kcreg.sh create -s clientId=myclient -t $TOKEN
- Windows:
c:\> kcreg config initial-token %TOKEN%
c:\> kcreg create -s clientId=myclient
or
c:\> kcreg create -s clientId=myclient -t %TOKEN%
When using an Initial Access Token, the server response includes a newly issued Registration Access Token. Any subsequent operation for that client needs to be performed by authenticating with that token, which is only valid for that client.
The Client Registration CLI automatically uses its private configuration file to save and use this token with its associated client. As long as the same configuration file is used for all client operations, the developer does not need to authenticate to read, update, or delete a client that was created this way.
See Using the client registration service for more information about Initial Access and Registration Access Tokens.
Run the kcreg config initial-token --help
and kcreg config registration-token --help
commands for more information on how to configure tokens with the Client Registration CLI.
11.4.4. Creating a client configuration
The first task after authenticating with credentials or configuring an Initial Access Token is usually to create a new client. Often you might want to use a prepared JSON file as a template and set or override some of the attributes.
The following example shows how to read a JSON file, override any client id it may contain, set any other attributes, and print the configuration to a standard output after successful creation.
- Linux:
$ kcreg.sh create -f client-template.json -s clientId=myclient -s baseUrl=/myclient -s 'redirectUris=["/myclient/*"]' -o
- Windows:
C:\> kcreg create -f client-template.json -s clientId=myclient -s baseUrl=/myclient -s "redirectUris=[\"/myclient/*\"]" -o
Run the kcreg create --help
for more information about the kcreg create
command.
You can use kcreg attrs
to list available attributes. Keep in mind that many configuration attributes are not checked for validity or consistency. It is up to you to specify proper values. Remember that you should not have any id fields in your template and should not specify them as arguments to the kcreg create
command.
11.4.5. Retrieving a client configuration
You can retrieve an existing client by using the kcreg get
command.
For example, on:
- Linux:
$ kcreg.sh get myclient
- Windows:
C:\> kcreg get myclient
You can also retrieve the client configuration as an adapter configuration file, which you can package with your web application.
For example, on:
- Linux:
$ kcreg.sh get myclient -e install > keycloak.json
- Windows:
C:\> kcreg get myclient -e install > keycloak.json
Run the kcreg get --help
command for more information about the kcreg get
command.
11.4.6. Modifying a client configuration
There are two methods for updating a client configuration.
One method is to submit a complete new state to the server after getting the current configuration, saving it to a file, editing it, and posting it back to the server.
For example, on:
- Linux:
$ kcreg.sh get myclient > myclient.json
$ vi myclient.json
$ kcreg.sh update myclient -f myclient.json
- Windows:
C:\> kcreg get myclient > myclient.json
C:\> notepad myclient.json
C:\> kcreg update myclient -f myclient.json
The second method fetches the current client, sets or deletes fields on it, and posts it back in one step.
For example, on:
- Linux:
$ kcreg.sh update myclient -s enabled=false -d redirectUris
- Windows:
C:\> kcreg update myclient -s enabled=false -d redirectUris
You can also use a file that contains only changes to be applied so you do not have to specify too many values as arguments. In this case, specify --merge
to tell the Client Registration CLI that rather than treating the JSON file as a full, new configuration, it should treat it as a set of attributes to be applied over the existing configuration.
For example, on:
- Linux:
$ kcreg.sh update myclient --merge -d redirectUris -f mychanges.json
- Windows:
C:\> kcreg update myclient --merge -d redirectUris -f mychanges.json
Run the kcreg update --help
command for more information about the kcreg update
command.
11.4.7. Deleting a client configuration
Use the following example to delete a client.
- Linux:
$ kcreg.sh delete myclient
- Windows:
C:\> kcreg delete myclient
Run the kcreg delete --help
command for more information about the kcreg delete
command.
11.4.8. Refreshing invalid Registration Access Tokens
When performing a create, read, update, and delete (CRUD) operation using the --no-config
mode, the Client Registration CLI cannot handle Registration Access Tokens for you. In that case, it is possible to lose track of the most recently issued Registration Access Token for a client, which makes it impossible to perform any further CRUD operations on that client without authenticating with an account that has manage-clients permissions.
If you have permissions, you can issue a new Registration Access Token for the client and have it printed to a standard output or saved to a configuration file of your choice. Otherwise, you have to ask the realm administrator to issue a new Registration Access Token for your client and send it to you. You can then pass it to any CRUD command via the --token
option. You can also use the kcreg config registration-token
command to save the new token in a configuration file and have the Client Registration CLI automatically handle it for you from that point on.
Run the kcreg update-token --help
command for more information about the kcreg update-token
command.
11.5. Troubleshooting
Q: When logging in, I get an error: Parameter client_assertion_type is missing [invalid_client].
A: This error means your client is configured with
Signed JWT
token credentials, which means you have to use the--keystore
parameter when logging in.
