---
title: "Chapter 5. Client Registration CLI - Red Hat Single Sign-On 7.1 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-client-registration-cli
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/securing_applications_and_services_guide/client_registration_cli
guide: securing_applications_and_services_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
---

# Chapter 5. Client Registration CLI - Red Hat Single Sign-On 7.1 Securing Applications and Services Guide

Chapter 5. Client Registration CLI
Client Registration CLI is a Technology Preview feature and is not fully supported.
Client Registration CLI
is a command line interface tool that can be used by application developers to configure new clients to integrate with Red Hat Single Sign-On. It is specifically designed to interact with Red Hat Single Sign-On Client Registration REST endpoints.
It is necessary to create a new client configuration for each new application hosted on a unique hostname in order for Keycloak to be able to interact with the application (and vice-versa) and perform its function of providing a login page, SSO session management etc.
Client Registration CLI
allows you to configure application clients from a command line, and can be used in shell scripts as well.
To allow a particular user to use Client Registration CLI
a Red Hat Single Sign-On administrator will typically use Admin Console
to configure a new user, or configure a new client, and a client secret, to protect access to Client Registration REST API
.
5.1. Configuring a new regular user for use with Client Registration CLI
Login as admin
into Admin Console
(e.g. http://localhost:8080/auth/admin
). Select a realm you want to administer. If you want to use existing user, select it for edit, otherwise create a new user. Go to Role Mappings
tab. Under Client Roles
select realm-management
. Under Available Roles
select manage-client
for full set of client management permissions. Alternatively you can choose view-clients
for read-only or create-client
for ability to create new clients. These permissions grant user the capability to perform operations without the use of Initial Access Token
or Registration Access Token
.
It’s possible to not assign users any of realm-management
roles. In that case user can still login with Registration Client CLI
but will not be able to use it without having possession of an Initial Access Token
. Trying to perform any operations without it will result in 403 Forbidden
error.
Administrator can issue Initial Access Tokens
from Admin Console
by selecting Initial Access Token
tab under Realm Settings
.
5.2. Configuring a client for use with Client Registration CLI
By default the Client Registration CLI
identifies as admin-cli
client which is automatically configured for every new realm. No additional client configuration is required when using login with a username. You may wish to strengthen security by configuring the client Access Type
as Confidential
, and under Credentials
tab select ClientId and Secret
. When running kcreg config credentials
you would then also have to provide a secret e.g. by using --secret
.
If you want to use a separate client configuration for Registration Client CLI
then you can create a new client - for example you can call it reg-cli
. When running kcreg config credentials
you then need to specify a clientId
to use e.g. --client reg-cli
.
If you want to use a service account associated with the client, then you need to enable a service account. In Admin Client
you go to Clients
section, and select a client for edit. Then under Settings
first change Access Type
to Confidential
. Then toggle Service Accounts Enabled
setting to On
, and Save
the configuration.
Under Credentials
tab you can choose to configure either Client Id and Secret
, or Signed JWT
.
You can now avoid specifying user when using kcreg config credentials
and only provide a client secret or keystore info.
5.3. Installing Client Registration CLI
Client Registration CLI is packaged inside Keycloak Server distribution. You can find execution scripts inside bin
directory.
The Linux script is called kcreg.sh
, and the one for Windows is called kcreg.bat
.
In order to setup the client to be used from any location on the filesystem you may want to add Keycloak server directory to your PATH.
On Linux:
$ export PATH=$PATH:$KEYCLOAK_HOME/bin
$ kcreg.sh
On Windows:
c:\> set PATH=%PATH%;%KEYCLOAK_HOME%\bin
c:\> kcreg
5.4. Using Client Registration CLI
Usually a user will first start an authenticated session by providing credentials, then perform some CRUD operations.
For example on Linux:
$ kcreg.sh config credentials --server http://localhost:8080/auth --realm demo --user user --client reg-cli
$ kcreg.sh create -s clientId=my_client -s 'redirectUris=["http://localhost:8980/myapp/*"]'
$ kcreg.sh get my_client
Or on Windows:
c:\> kcreg config credentials --server http://localhost:8080/auth --realm demo --user user --client reg-cli
c:\> kcreg create -s clientId=my_client -s "redirectUris=[\"http://localhost:8980/myapp/*\"]"
c:\> kcreg get my_client
In a production environment Keycloak has to be accessed with https:
to avoid exposing tokens to network sniffers. If server’s certificate is not issued by one of the trusted CAs that are included in Java’s default certificate truststore, then you will need to prepare a truststore.jks file, and instruct Client Registration CLI
to use it.
For example on Linux:
$ kcreg.sh config truststore --trustpass $PASSWORD ~/.keycloak/truststore.jks
Or on Windows:
c:\> kcreg config truststore --trustpass %PASSWORD% %HOMEPATH%\.keycloak\truststore.jks
5.4.1. Logging In
When logging in with Client Registration CLI
you specify a server endpoint url, and a realm. Then you specify a username, or alternatively you can only specify a client id, which will result in special service account being used. In the first case, a password for the specified user has to be used at login. In the latter case there is no user password - only client secret or a Signed JWT
is used.
Regardless of the method, the account that logs in needs to have proper permissions in order to be able to perform client registration operations. Keep in mind that any account can only have permissions to manage clients within the same realm. If you need to manage different realms, you need to configure users in different realms with permissions to manage clients.
Client Registration CLI
by itself does not support configuring the users, for that you would need to use Admin Console
web interface or Admin Client CLI
once it’s available.
When kcreg
successfully logs in it receives authorization tokens and saves them into a private config file so they can be used for subsequent invocations. See next chapter for more info on configuration file.
See built-in help for more information on using Client Registration CLI
.
For example on Linux:
$ kcreg.sh help
Or on Windows:
c:\> kcreg help
See kcreg config credentials --help
for more information about starting an authenticated session.
5.4.2. Working with alternative configurations
By default, Client Registration CLI
automatically maintains a configuration file at a default location - .keycloak/kcreg.config
under user’s home directory.
You can use --config
option at any time to point to a different file / location. This way you can mantain multiple authenticated sessions in parallel. It is safest to perform operations tied to a single config file from a single thread.
Make sure to not make a config file visible to other users on the system as it contains access tokens, and secrets that should be kept private.
You may want to avoid storing any secrets at all inside a config file for the price of less convenience and having to do more token requests. In that case you can use --no-config
option with all your commands. You will have to specify all authentication info with each kcreg
invocation.
5.4.3. Initial Access and Registration Access Tokens
Client Registration CLI
can be used by developers who don’t have an account configured at Keycloak server they want to use. That’s possible when realm administrator issues developer an Initial Access Token
. It is up to realm administrator to decide how to issue and distribute these tokens. Admin can limit an Initial Access Token by maximum age, and a total number of clients that can be created with it. Many Initial Access Tokens can be created, and it’s up to realm administrator to distribute them.
Once a developer is in possession of Initial Access Token they can use it to create new clients without authenticating with kcreg config credentials
. Rather, Initial Access Token can be stored in configuration, or specified as part of kcreg create
command.
For example on Linux:
$ kcreg.sh config initial-token $TOKEN
$ kcreg.sh create -s clientId=myclient
or
$ kcreg.sh create -s clientId=myclient -t $TOKEN
On Windows:
c:\> kcreg config initial-token %TOKEN%
c:\> kcreg create -s clientId=myclient
or
c:\> kcreg create -s clientId=myclient -t %TOKEN%
When Initial Access Token is used, the server response will include a newly issued Registration Access Token for client that was just created. Any subsequent operation for that client needs to be performed by authenticating with that token.
Client Registration CLI
automatically uses its private configuration file to save, and make use of this token for each created client. As long as the same configuration file is used for all client operations, the developer will not need to authenticate in order to read, update, or delete a client they created.
You can read more about Initial Access and Registration Access Tokens in Client Registration chapter.
See kcreg config initial-token --help
and kcreg config registration-token --help
for more information on how to configure them with Client Registration CLI
.
5.4.4. Performing CRUD operations
After authenticating with credentials or configuring Initial Access Token, the first operation will usually be to create a new client.
We’ve seen the simplest command to create a new client already. Often we may want to use a prepared JSON file as a template, and set / override some of the attributes. For example, this is how you read a JSON file in default client configuration format, override any clientId it may contain with a new one, override / set any other attributes as well, and after successful creation print the new client configuration to standard output.
On Linux:
$ kcreg.sh create -s clientId=myclient -f client-template.json -s baseUrl=/myclient -s 'redirectUris=["/myclient/*"]' -o
On Windows:
C:\> kcreg create -s clientId=myclient -f client-template.json -s baseUrl=/myclient -s "redirectUris=[\"/myclient/*\"]" -o
See kcreg create --help
for more information about kcreg create
.
You can use kcreg attrs
to list the available attributes. Note, that many configuration attributes are not checked for validity or consistency. It is up to you to specify proper values. Also note, that you should not have any id
fields in your template or specify them as arguments to kcreg create
.
Once a new client is created you can retrieve it again by using kcreg get
.
On Linux:
$ kcreg.sh get myclient
On Windows:
C:\> kcreg get myclient
You can also get an adapter configuration which you can drop into your web application in order to integrate with Keycloak server.
On Linux:
$ kcreg.sh get myclient -e install
On Windows:
C:\> kcreg get myclient -e install
See kcreg get --help
for more information about kcreg get
.
It’s simple to update client configurations as well. There are two modes of updating.
One is to submit a complete new state to the server after getting current configuration, saving it into a file, editing it, and posting it back.
On Linux:
$ kcreg.sh get myclient > myclient.json
$ vi myclient.json
$ kcreg.sh update myclient -f myclient.json
On Windows:
C:\> kcreg get myclient > myclient.json
C:\> notepad myclient.json
C:\> kcreg update myclient -f myclient.json
Another is to get current client, set or delete fields on it, and post it back all in one single step.
On Linux:
$ kcreg.sh update myclient -s enabled=false -d redirectUris
On Windows:
C:\> kcreg update myclient -s enabled=false -d redirectUris
You can even use a file that contains only changes to be applied so you don’t have to specify too many values as arguments. In this case we specify --merge
to tell Client Registration CLI
that rather than treating mychanges.json as full new configuration, it should see it as a set of attributes to be applied over existing configuration.
On Linux:
$ kcreg.sh update myclient --merge -d redirectUris -f mychanges.json
On Windows:
C:\> kcreg update myclient --merge -d redirectUris -f mychanges.json
See kcreg update --help
for more information about kcreg update
.
You may sometimes also need to delete a client.
On Linux:
$ kcreg.sh delete myclient
On Windows:
C:\> kcreg delete myclient
See kcreg delete --help
for more information about kcreg delete
.
5.4.5. Refreshing Invalid Registration Access Tokens
When performing CRUD operation using no-config
mode Client Registration CLI
can no longer handle Registration Access Tokens for you. In that case it is possible to lose track of most recently issued Registration Access Token for a client, which makes it impossible to perform any further CRUD operations on that client without using credentials of an account with 'manage-clients' permissions.
If you have permissions you can reissue a new Registration Access Token for the client, and have it printed to stdout or saved to a config file of your choice. If not you have to ask realm administrator to reissue a new Registration Access Token for your client, and send it to you. You can then use the token by passing it to any CRUD command via --token
option. You can also use kcreg config registration-token
command to save the new token in configuration file, and have Client Registration CLI
automatically handle it for you from that point on.
See kcreg update-token --help
for more information about kcreg update-token
.
5.5. Troubleshooting
Q: When logging in I get an error:
Parameter client_assertion_type is missing [invalid_client]
A: Your client is configured with
Signed JWT
token credentials which means you have to use--keystore
parameter when logging in.
