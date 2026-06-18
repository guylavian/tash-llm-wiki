---
title: "Chapter 18. Admin CLI - Red Hat Single Sign-On 7.6 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-admin-cli
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/server_administration_guide/admin_cli
guide: server_administration_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
abstract: "With Red Hat Single Sign-On, you can perform administration tasks from the command-line interface (CLI) by using the Admin CLI command-line tool. 18.1. Installing the Admin CLI Red Hat Single Sign-On packages the Admin CLI server distribution with the execution scripts in the bin directory. The Linux script is called kcadm.sh, and the script for Windows is called kcadm.bat. Add the Red Hat Single …"
---

# Chapter 18. Admin CLI - Red Hat Single Sign-On 7.6 Server Administration Guide

Chapter 18. Admin CLI
With Red Hat Single Sign-On, you can perform administration tasks from the command-line interface (CLI) by using the Admin CLI command-line tool.
18.1. Installing the Admin CLI
Red Hat Single Sign-On packages the Admin CLI server distribution with the execution scripts in the bin
directory.
The Linux script is called kcadm.sh
, and the script for Windows is called kcadm.bat
. Add the Red Hat Single Sign-On server directory to your PATH
to use the client from any location on your file system.
For example:
- Linux:
$ export PATH=$PATH:$KEYCLOAK_HOME/bin
$ kcadm.sh
- Windows:
c:\> set PATH=%PATH%;%KEYCLOAK_HOME%\bin
c:\> kcadm
You must set the KEYCLOAK_HOME
environment variable to the path where you extracted the Red Hat Single Sign-On Server distribution.
To avoid repetition, the rest of this document only uses Windows examples in places where the CLI differences are more than just in the kcadm
command name.
18.2. Using the Admin CLI
The Admin CLI makes HTTP requests to Admin REST endpoints. Access to the Admin REST endpoints requires authentication.
Consult the Admin REST API documentation for details about JSON attributes for specific endpoints.
Start an authenticated session by logging in. You can now perform create, read, update, and delete (CRUD) operations.
For example:
Linux:
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm demo --user admin --client admin $ kcadm.sh create realms -s realm=demorealm -s enabled=true -o $ CID=$(kcadm.sh create clients -r demorealm -s clientId=my_client -s 'redirectUris=["http://localhost:8980/myapp/*"]' -i) $ kcadm.sh get clients/$CID/installation/providers/keycloak-oidc-keycloak-json
Windows:
c:\> kcadm config credentials --server http://localhost:8080/auth --realm demo --user admin --client admin c:\> kcadm create realms -s realm=demorealm -s enabled=true -o c:\> kcadm create clients -r demorealm -s clientId=my_client -s "redirectUris=[\"http://localhost:8980/myapp/*\"]" -i > clientid.txt c:\> set /p CID=<clientid.txt c:\> kcadm get clients/%CID%/installation/providers/keycloak-oidc-keycloak-json
In a production environment, access Red Hat Single Sign-On by using
https:
to avoid exposing tokens. If a trusted certificate authority, included in Java’s default certificate truststore, has not issued a server’s certificate, prepare atruststore.jks
file and instruct the Admin CLI to use it.For example:
Linux:
$ kcadm.sh config truststore --trustpass $PASSWORD ~/.keycloak/truststore.jks
Windows:
c:\> kcadm config truststore --trustpass %PASSWORD% %HOMEPATH%\.keycloak\truststore.jks
18.3. Authenticating
When you log in with the Admin CLI, you specify:
- A server endpoint URL
- A realm
- A user name
Another option is to specify a clientId only, which creates a unique service account for you to use.
When you log in using a user name, use a password for the specified user. When you log in using a clientId, you need the client secret only, not the user password. You can also use the Signed JWT
rather than the client secret.
Ensure the account used for the session has the proper permissions to invoke Admin REST API operations. For example, the realm-admin
role of the realm-management
client can administer the realm of the user.
Two primary mechanisms are available for authentication. One mechanism uses kcadm config credentials
to start an authenticated session.
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
This mechanism maintains an authenticated session between the kcadm
command invocations by saving the obtained access token and its associated refresh token. It can maintain other secrets in a private configuration file. See the next chapter for more information.
The second mechanism authenticates each command invocation for the duration of the invocation. This mechanism increases the load on the server and the time spent on round trips obtaining tokens. The benefit of this approach is that it is unnecessary to save tokens between invocations, so nothing is saved to disk. Red Hat Single Sign-On uses this mode when the --no-config
argument is specified.
For example, when performing an operation, specify all the information required for authentication.
$ kcadm.sh get realms --no-config --server http://localhost:8080/auth --realm master --user admin --password admin
Run the kcadm.sh help
command for more information on using the Admin CLI.
Run the kcadm.sh config credentials --help
command for more information about starting an authenticated session.
18.4. Working with alternative configurations
By default, the Admin CLI maintains a configuration file named kcadm.config
. Red Hat Single Sign-On places this file in the user’s home directory. In Linux-based systems, the full pathname is $HOME/.keycloak/kcadm.config
. In Windows, the full pathname is %HOMEPATH%\.keycloak\kcadm.config
.
You can use the --config
option to point to a different file or location so you can maintain multiple authenticated sessions in parallel.
Perform operations tied to a single configuration file from a single thread.
Ensure the configuration file is invisible to other users on the system. It contains access tokens and secrets that must be private. Red Hat Single Sign-On creates the ~/.keycloak
directory and its contents automatically with proper access limits. If the directory already exists, Red Hat Single Sign-On does not update the directory’s permissions.
It is possible to avoid storing secrets inside a configuration file, but doing so is inconvenient and increases the number of token requests. Use the --no-config
option with all commands and specify the authentication information the config credentials
command requires with each invocation of kcadm
.
18.5. Basic operations and resource URIs
The Admin CLI can generically perform CRUD operations against Admin REST API endpoints with additional commands that simplify particular tasks.
The main usage pattern is listed here:
$ kcadm.sh create ENDPOINT [ARGUMENTS]
$ kcadm.sh get ENDPOINT [ARGUMENTS]
$ kcadm.sh update ENDPOINT [ARGUMENTS]
$ kcadm.sh delete ENDPOINT [ARGUMENTS]
The create
, get
, update
, and delete
commands map to the HTTP verbs POST
, GET
, PUT
, and DELETE
, respectively. ENDPOINT is a target resource URI and can be absolute (starting with http:
or https:
) or relative, that Red Hat Single Sign-On uses to compose absolute URLs in the following format:
SERVER_URI/admin/realms/REALM/ENDPOINT
For example, if you authenticate against the server http://localhost:8080/auth and realm is master
, using users
as ENDPOINT creates the http://localhost:8080/auth/admin/realms/master/users resource URL.
If you set ENDPOINT to clients
, the effective resource URI is http://localhost:8080/auth/admin/realms/master/clients.
Red Hat Single Sign-On has a realms
endpoint that is the container for realms. It resolves to:
SERVER_URI/admin/realms
Red Hat Single Sign-On has a serverinfo
endpoint. This endpoint is independent of realms.
When you authenticate as a user with realm-admin powers, you may need to perform commands on multiple realms. If so, specify the -r
option to tell the CLI which realm the command is to execute against explicitly. Instead of using REALM
as specified by the --realm
option of kcadm.sh config credentials
, the command uses TARGET_REALM
.
SERVER_URI/admin/realms/TARGET_REALM/ENDPOINT
For example:
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
$ kcadm.sh create users -s username=testuser -s enabled=true -r demorealm
In this example, you start a session authenticated as the admin
user in the master
realm. You then perform a POST call against the resource URL http://localhost:8080/auth/admin/realms/demorealm/users
.
The create
and update
commands send a JSON body to the server. You can use -f FILENAME
to read a pre-made document from a file. When you can use the -f -
option, Red Hat Single Sign-On reads the message body from the standard input. You can specify individual attributes and their values, as seen in the create users
example. Red Hat Single Sign-On composes the attributes into a JSON body and sends them to the server.
Several methods are available in Red Hat Single Sign-On to update a resource using the update
command. You can determine the current state of a resource and save it to a file, edit that file, and send it to the server for an update.
For example:
$ kcadm.sh get realms/demorealm > demorealm.json
$ vi demorealm.json
$ kcadm.sh update realms/demorealm -f demorealm.json
This method updates the resource on the server with the attributes in the sent JSON document.
Another method is to perform an on-the-fly update by using the -s, --set
options to set new values.
For example:
$ kcadm.sh update realms/demorealm -s enabled=false
This method sets the enabled
attribute to false
.
By default, the update
command performs a get
and then merges the new attribute values with existing values. In some cases, the endpoint may support the put
command but not the get
command. You can use the -n
option to perform a no-merge update, which performs a put
command without first running a get
command.
18.6. Realm operations
Creating a new realm
Use the create
command on the realms
endpoint to create a new enabled realm. Set the attributes to realm
and enabled
.
$ kcadm.sh create realms -s realm=demorealm -s enabled=true
Red Hat Single Sign-On disables realms by default. You can use a realm immediately for authentication by enabling it.
A description for a new object can also be in JSON format.
$ kcadm.sh create realms -f demorealm.json
You can send a JSON document with realm attributes directly from a file or pipe the document to standard input.
For example:
- Linux:
$ kcadm.sh create realms -f - << EOF
{ "realm": "demorealm", "enabled": true }
EOF
- Windows:
c:\> echo { "realm": "demorealm", "enabled": true } | kcadm create realms -f -
Listing existing realms
This command returns a list of all realms.
$ kcadm.sh get realms
Red Hat Single Sign-On filters the list of realms on the server to return realms a user can see only.
The list of all realm attributes can be verbose, and most users are interested in a subset of attributes, such as the realm name and the enabled status of the realm. You can specify the attributes to return by using the --fields
option.
$ kcadm.sh get realms --fields realm,enabled
You can display the result as comma-separated values.
$ kcadm.sh get realms --fields realm --format csv --noquotes
Getting a specific realm
Append a realm name to a collection URI to get an individual realm.
$ kcadm.sh get realms/master
Updating a realm
Use the
-s
option to set new values for the attributes when you do not want to change all of the realm’s attributes.For example:
$ kcadm.sh update realms/demorealm -s enabled=false
If you want to set all writable attributes to new values:
-
Run a
get
command. - Edit the current values in the JSON file.
Resubmit.
For example:
$ kcadm.sh get realms/demorealm > demorealm.json $ vi demorealm.json $ kcadm.sh update realms/demorealm -f demorealm.json
-
Run a
Deleting a realm
Run the following command to delete a realm:
$ kcadm.sh delete realms/demorealm
Turning on all login page options for the realm
Set the attributes that control specific capabilities to true
.
For example:
$ kcadm.sh update realms/demorealm -s registrationAllowed=true -s registrationEmailAsUsername=true -s rememberMe=true -s verifyEmail=true -s resetPasswordAllowed=true -s editUsernameAllowed=true
Listing the realm keys
Use the get
operation on the keys
endpoint of the target realm.
$ kcadm.sh get keys -r demorealm
Generating new realm keys
Get the ID of the target realm before adding a new RSA-generated key pair.
For example:
$ kcadm.sh get realms/demorealm --fields id --format csv --noquotes
Add a new key provider with a higher priority than the existing providers as revealed by
kcadm.sh get keys -r demorealm
.For example:
Linux:
$ kcadm.sh create components -r demorealm -s name=rsa-generated -s providerId=rsa-generated -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s 'config.priority=["101"]' -s 'config.enabled=["true"]' -s 'config.active=["true"]' -s 'config.keySize=["2048"]'
Windows:
c:\> kcadm create components -r demorealm -s name=rsa-generated -s providerId=rsa-generated -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s "config.priority=[\"101\"]" -s "config.enabled=[\"true\"]" -s "config.active=[\"true\"]" -s "config.keySize=[\"2048\"]"
Set the
parentId
attribute to the value of the target realm’s ID.The newly added key is now the active key, as revealed by
kcadm.sh get keys -r demorealm
.
Adding new realm keys from a Java Key Store file
Add a new key provider to add a new key pair pre-prepared as a JKS file.
For example, on:
Linux:
$ kcadm.sh create components -r demorealm -s name=java-keystore -s providerId=java-keystore -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s 'config.priority=["101"]' -s 'config.enabled=["true"]' -s 'config.active=["true"]' -s 'config.keystore=["/opt/keycloak/keystore.jks"]' -s 'config.keystorePassword=["secret"]' -s 'config.keyPassword=["secret"]' -s 'config.keyAlias=["localhost"]'
Windows:
c:\> kcadm create components -r demorealm -s name=java-keystore -s providerId=java-keystore -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s "config.priority=[\"101\"]" -s "config.enabled=[\"true\"]" -s "config.active=[\"true\"]" -s "config.keystore=[\"/opt/keycloak/keystore.jks\"]" -s "config.keystorePassword=[\"secret\"]" -s "config.keyPassword=[\"secret\"]" -s "config.keyAlias=[\"localhost\"]"
-
Ensure you change the attribute values for
keystore
,keystorePassword
,keyPassword
, andalias
to match your specific keystore. -
Set the
parentId
attribute to the value of the target realm’s ID.
Making the key passive or disabling the key
Identify the key you want to make passive.
$ kcadm.sh get keys -r demorealm
-
Use the key’s
providerId
attribute to construct an endpoint URI, such ascomponents/PROVIDER_ID
. Perform an
update
.For example:
Linux:
$ kcadm.sh update components/PROVIDER_ID -r demorealm -s 'config.active=["false"]'
Windows:
c:\> kcadm update components/PROVIDER_ID -r demorealm -s "config.active=[\"false\"]"
You can update other key attributes:
-
Set a new
enabled
value to disable the key, for example,config.enabled=["false"]
. -
Set a new
priority
value to change the key’s priority, for example,config.priority=["110"]
.
Deleting an old key
- Ensure the key you are deleting is inactive and you have disabled it. This action is to prevent existing tokens held by applications and users from failing.
Identify the key to delete.
$ kcadm.sh get keys -r demorealm
Use the
providerId
of the key to perform the delete.$ kcadm.sh delete components/PROVIDER_ID -r demorealm
Configuring event logging for a realm
Use the update
command on the events/config
endpoint.
The eventsListeners
attribute contains a list of EventListenerProviderFactory IDs, specifying all event listeners that receive events. Attributes are available that control built-in event storage, so you can query past events using the Admin REST API. Red Hat Single Sign-On has separate control over the logging of service calls (eventsEnabled
) and the auditing events triggered by the Admin Console or Admin REST API (adminEventsEnabled
). You can set up the eventsExpiration
event to expire to prevent your database from filling. Red Hat Single Sign-On sets eventsExpiration
to time-to-live expressed in seconds.
You can set up a built-in event listener that receives all events and logs the events through JBoss-logging. Using the org.keycloak.events
logger, Red Hat Single Sign-On logs error events as WARN
and other events as DEBUG
.
For example:
- Linux:
$ kcadm.sh update events/config -r demorealm -s 'eventsListeners=["jboss-logging"]'
- Windows:
c:\> kcadm update events/config -r demorealm -s "eventsListeners=[\"jboss-logging\"]"
For example:
You can turn on storage for all available ERROR events, not including auditing events, for two days so you can retrieve the events through Admin REST.
- Linux:
$ kcadm.sh update events/config -r demorealm -s eventsEnabled=true -s 'enabledEventTypes=["LOGIN_ERROR","REGISTER_ERROR","LOGOUT_ERROR","CODE_TO_TOKEN_ERROR","CLIENT_LOGIN_ERROR","FEDERATED_IDENTITY_LINK_ERROR","REMOVE_FEDERATED_IDENTITY_ERROR","UPDATE_EMAIL_ERROR","UPDATE_PROFILE_ERROR","UPDATE_PASSWORD_ERROR","UPDATE_TOTP_ERROR","VERIFY_EMAIL_ERROR","REMOVE_TOTP_ERROR","SEND_VERIFY_EMAIL_ERROR","SEND_RESET_PASSWORD_ERROR","SEND_IDENTITY_PROVIDER_LINK_ERROR","RESET_PASSWORD_ERROR","IDENTITY_PROVIDER_FIRST_LOGIN_ERROR","IDENTITY_PROVIDER_POST_LOGIN_ERROR","CUSTOM_REQUIRED_ACTION_ERROR","EXECUTE_ACTIONS_ERROR","CLIENT_REGISTER_ERROR","CLIENT_UPDATE_ERROR","CLIENT_DELETE_ERROR"]' -s eventsExpiration=172800
- Windows:
c:\> kcadm update events/config -r demorealm -s eventsEnabled=true -s "enabledEventTypes=[\"LOGIN_ERROR\",\"REGISTER_ERROR\",\"LOGOUT_ERROR\",\"CODE_TO_TOKEN_ERROR\",\"CLIENT_LOGIN_ERROR\",\"FEDERATED_IDENTITY_LINK_ERROR\",\"REMOVE_FEDERATED_IDENTITY_ERROR\",\"UPDATE_EMAIL_ERROR\",\"UPDATE_PROFILE_ERROR\",\"UPDATE_PASSWORD_ERROR\",\"UPDATE_TOTP_ERROR\",\"VERIFY_EMAIL_ERROR\",\"REMOVE_TOTP_ERROR\",\"SEND_VERIFY_EMAIL_ERROR\",\"SEND_RESET_PASSWORD_ERROR\",\"SEND_IDENTITY_PROVIDER_LINK_ERROR\",\"RESET_PASSWORD_ERROR\",\"IDENTITY_PROVIDER_FIRST_LOGIN_ERROR\",\"IDENTITY_PROVIDER_POST_LOGIN_ERROR\",\"CUSTOM_REQUIRED_ACTION_ERROR\",\"EXECUTE_ACTIONS_ERROR\",\"CLIENT_REGISTER_ERROR\",\"CLIENT_UPDATE_ERROR\",\"CLIENT_DELETE_ERROR\"]" -s eventsExpiration=172800
You can reset stored event types to all available event types. Setting the value to an empty list is the same as enumerating all.
$ kcadm.sh update events/config -r demorealm -s enabledEventTypes=[]
You can enable storage of auditing events.
$ kcadm.sh update events/config -r demorealm -s adminEventsEnabled=true -s adminEventsDetailsEnabled=true
You can get the last 100 events. The events are ordered from newest to oldest.
$ kcadm.sh get events --offset 0 --limit 100
You can delete all saved events.
$ kcadm delete events
Flushing the caches
Use the
create
command with one of these endpoints to clear caches:-
clear-realm-cache
-
clear-user-cache
-
clear-keys-cache
-
Set
realm
to the same value as the target realm.For example:
$ kcadm.sh create clear-realm-cache -r demorealm -s realm=demorealm $ kcadm.sh create clear-user-cache -r demorealm -s realm=demorealm $ kcadm.sh create clear-keys-cache -r demorealm -s realm=demorealm
Importing a realm from exported .json file
-
Use the
create
command on thepartialImport
endpoint. -
Set
ifResourceExists
toFAIL
,SKIP
, orOVERWRITE
. Use
-f
to submit the exported realm.json
file.For example:
$ kcadm.sh create partialImport -r demorealm2 -s ifResourceExists=FAIL -o -f demorealm.json
If the realm does not yet exist, create it first.
For example:
$ kcadm.sh create realms -s realm=demorealm2 -s enabled=true
18.7. Role operations
Creating a realm role
Use the roles
endpoint to create a realm role.
$ kcadm.sh create roles -r demorealm -s name=user -s 'description=Regular user with a limited set of permissions'
Creating a client role
- Identify the client.
Use the
get
command to list the available clients.$ kcadm.sh get clients -r demorealm --fields id,clientId
Create a new role by using the
clientId
attribute to construct an endpoint URI, such asclients/ID/roles
.For example:
$ kcadm.sh create clients/a95b6af3-0bdc-4878-ae2e-6d61a4eca9a0/roles -r demorealm -s name=editor -s 'description=Editor can edit, and publish any article'
Listing realm roles
Use the get
command on the roles
endpoint to list existing realm roles.
$ kcadm.sh get roles -r demorealm
You can use the get-roles
command also.
$ kcadm.sh get-roles -r demorealm
Listing client roles
Red Hat Single Sign-On has a dedicated get-roles
command to simplify the listing of realm and client roles. The command is an extension of the get
command and behaves the same as the get
command but with additional semantics for listing roles.
Use the get-roles
command by passing it the clientId (--cclientid
) option or the id
(--cid
) option to identify the client to list client roles.
For example:
$ kcadm.sh get-roles -r demorealm --cclientid realm-management
Getting a specific realm role
Use the get
command and the role name
to construct an endpoint URI for a specific realm role, roles/ROLE_NAME
, where user
is the existing role’s name.
For example:
$ kcadm.sh get roles/user -r demorealm
You can use the get-roles
command, passing it a role name (--rolename
option) or ID (--roleid
option).
For example:
$ kcadm.sh get-roles -r demorealm --rolename user
Getting a specific client role
Use the get-roles
command, passing it the clientId attribute (--cclientid
option) or ID attribute (--cid
option) to identify the client, and pass the role name (--rolename
option) or the role ID attribute (--roleid
) to identify a specific client role.
For example:
$ kcadm.sh get-roles -r demorealm --cclientid realm-management --rolename manage-clients
Updating a realm role
Use the update
command with the endpoint URI you used to get a specific realm role.
For example:
$ kcadm.sh update roles/user -r demorealm -s 'description=Role representing a regular user'
Updating a client role
Use the update
command with the endpoint URI that you used to get a specific client role.
For example:
$ kcadm.sh update clients/a95b6af3-0bdc-4878-ae2e-6d61a4eca9a0/roles/editor -r demorealm -s 'description=User that can edit, and publish articles'
Deleting a realm role
Use the delete
command with the endpoint URI that you used to get a specific realm role.
For example:
$ kcadm.sh delete roles/user -r demorealm
Deleting a client role
Use the delete
command with the endpoint URI that you used to get a specific client role.
For example:
$ kcadm.sh delete clients/a95b6af3-0bdc-4878-ae2e-6d61a4eca9a0/roles/editor -r demorealm
Listing assigned, available, and effective realm roles for a composite role
Use the get-roles
command to list assigned, available, and effective realm roles for a composite role.
To list assigned realm roles for the composite role, specify the target composite role by name (
--rname
option) or ID (--rid
option).For example:
$ kcadm.sh get-roles -r demorealm --rname testrole
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --effective
Use the
--available
option to list realm roles that you can add to the composite role.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --available
Listing assigned, available, and effective client roles for a composite role
Use the get-roles
command to list assigned, available, and effective client roles for a composite role.
To list assigned client roles for the composite role, you can specify the target composite role by name (
--rname
option) or ID (--rid
option) and client by the clientId attribute (--cclientid
option) or ID (--cid
option).For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management --effective
Use the
--available
option to list realm roles that you can add to the target composite role.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management --available
Adding realm roles to a composite role
Red Hat Single Sign-On provides an add-roles
command for adding realm roles and client roles.
This example adds the user
role to the composite role testrole
.
$ kcadm.sh add-roles --rname testrole --rolename user -r demorealm
Removing realm roles from a composite role
Red Hat Single Sign-On provides a remove-roles
command for removing realm roles and client roles.
The following example removes the user
role from the target composite role testrole
.
$ kcadm.sh remove-roles --rname testrole --rolename user -r demorealm
Adding client roles to a realm role
Red Hat Single Sign-On provides an add-roles
command for adding realm roles and client roles.
The following example adds the roles defined on the client realm-management
, create-client
, and view-users
, to the testrole
composite role.
$ kcadm.sh add-roles -r demorealm --rname testrole --cclientid realm-management --rolename create-client --rolename view-users
Adding client roles to a client role
Determine the ID of the composite client role by using the
get-roles
command.For example:
$ kcadm.sh get-roles -r demorealm --cclientid test-client --rolename operations
-
Assume that a client exists with a clientId attribute named
test-client
, a client role namedsupport
, and a client role namedoperations
which becomes a composite role that has an ID of "fc400897-ef6a-4e8c-872b-1581b7fa8a71". Use the following example to add another role to the composite role.
$ kcadm.sh add-roles -r demorealm --cclientid test-client --rid fc400897-ef6a-4e8c-872b-1581b7fa8a71 --rolename support
List the roles of a composite role by using the
get-roles --all
command.For example:
$ kcadm.sh get-roles --rid fc400897-ef6a-4e8c-872b-1581b7fa8a71 --all
Removing client roles from a composite role
Use the remove-roles
command to remove client roles from a composite role.
Use the following example to remove two roles defined on the client realm-management
, the create-client
role and the view-users
role, from the testrole
composite role.
$ kcadm.sh remove-roles -r demorealm --rname testrole --cclientid realm-management --rolename create-client --rolename view-users
Adding client roles to a group
Use the add-roles
command to add realm roles and client roles.
The following example adds the roles defined on the client realm-management
, create-client
and view-users
, to the Group
group (--gname
option). Alternatively, you can specify the group by ID (--gid
option).
See Group operations for more information.
$ kcadm.sh add-roles -r demorealm --gname Group --cclientid realm-management --rolename create-client --rolename view-users
Removing client roles from a group
Use the remove-roles
command to remove client roles from a group.
The following example removes two roles defined on the client realm management
, create-client
and view-users
, from the Group
group.
See Group operations for more information.
$ kcadm.sh remove-roles -r demorealm --gname Group --cclientid realm-management --rolename create-client --rolename view-users
18.8. Client operations
Creating a client
Run the
create
command on aclients
endpoint to create a new client.For example:
$ kcadm.sh create clients -r demorealm -s clientId=myapp -s enabled=true
Specify a secret if to set a secret for adapters to authenticate.
For example:
$ kcadm.sh create clients -r demorealm -s clientId=myapp -s enabled=true -s clientAuthenticatorType=client-secret -s secret=d0b8122f-8dfb-46b7-b68a-f5cc4e25d000
Listing clients
Use the get
command on the clients
endpoint to list clients.
This example filters the output to list only the id
and clientId
attributes:
$ kcadm.sh get clients -r demorealm --fields id,clientId
Getting a specific client
Use the client ID to construct an endpoint URI that targets a specific client, such as clients/ID
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm
Getting the current secret for a specific client
Use the client ID to construct an endpoint URI, such as clients/ID/client-secret
.
For example:
$ kcadm.sh get clients/$CID/client-secret
Generate a new secret for a specific client
Use the client ID to construct an endpoint URI, such as clients/ID/client-secret
.
For example:
$ kcadm.sh create clients/$CID/client-secret
Updating the current secret for a specific client
Use the client ID to construct an endpoint URI, such as clients/ID
.
For example:
$ kcadm.sh update clients/$CID -s "secret=newSecret"
Getting an adapter configuration file (keycloak.json) for a specific client
Use the client ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/keycloak-oidc-keycloak-json
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3/installation/providers/keycloak-oidc-keycloak-json -r demorealm
Getting a WildFly subsystem adapter configuration for a specific client
Use the client ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/keycloak-oidc-jboss-subsystem
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3/installation/providers/keycloak-oidc-jboss-subsystem -r demorealm
Getting a Docker-v2 example configuration for a specific client
Use the client ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/docker-v2-compose-yaml
.
The response is in .zip
format.
For example:
$ kcadm.sh get http://localhost:8080/auth/admin/realms/demorealm/clients/8f271c35-44e3-446f-8953-b0893810ebe7/installation/providers/docker-v2-compose-yaml -r demorealm > keycloak-docker-compose-yaml.zip
Updating a client
Use the update
command with the same endpoint URI that you use to get a specific client.
For example:
- Linux:
$ kcadm.sh update clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm -s enabled=false -s publicClient=true -s 'redirectUris=["http://localhost:8080/myapp/*"]' -s baseUrl=http://localhost:8080/myapp -s adminUrl=http://localhost:8080/myapp
- Windows:
c:\> kcadm update clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm -s enabled=false -s publicClient=true -s "redirectUris=[\"http://localhost:8080/myapp/*\"]" -s baseUrl=http://localhost:8080/myapp -s adminUrl=http://localhost:8080/myapp
Deleting a client
Use the delete
command with the same endpoint URI that you use to get a specific client.
For example:
$ kcadm.sh delete clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm
Adding or removing roles for client’s service account
A client’s service account is a user account with username service-account-CLIENT_ID
. You can perform the same user operations on this account as a regular account.
18.9. User operations
Creating a user
Run the create
command on the users
endpoint to create a new user.
For example:
$ kcadm.sh create users -r demorealm -s username=testuser -s enabled=true
Listing users
Use the users
endpoint to list users. The target user must change their password the next time they log in.
For example:
$ kcadm.sh get users -r demorealm --offset 0 --limit 1000
You can filter users by username
, firstName
, lastName
, or email
.
For example:
$ kcadm.sh get users -r demorealm -q email=google.com
$ kcadm.sh get users -r demorealm -q username=testuser
Filtering does not use exact matching. This example matches the value of the username
attribute against the *testuser*
pattern.
You can filter across multiple attributes by specifying multiple -q
options. Red Hat Single Sign-On returns users that match the condition for all the attributes only.
Getting a specific user
Use the user ID to compose an endpoint URI, such as users/USER_ID
.
For example:
$ kcadm.sh get users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm
Updating a user
Use the update
command with the same endpoint URI that you use to get a specific user.
For example:
- Linux:
$ kcadm.sh update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm -s 'requiredActions=["VERIFY_EMAIL","UPDATE_PROFILE","CONFIGURE_TOTP","UPDATE_PASSWORD"]'
- Windows:
c:\> kcadm update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm -s "requiredActions=[\"VERIFY_EMAIL\",\"UPDATE_PROFILE\",\"CONFIGURE_TOTP\",\"UPDATE_PASSWORD\"]"
Deleting a user
Use the delete
command with the same endpoint URI that you use to get a specific user.
For example:
$ kcadm.sh delete users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm
Resetting a user’s password
Use the dedicated set-password
command to reset a user’s password.
For example:
$ kcadm.sh set-password -r demorealm --username testuser --new-password NEWPASSWORD --temporary
This command sets a temporary password for the user. The target user must change the password the next time they log in.
You can use --userid
to specify the user by using the id
attribute.
You can achieve the same result using the update
command on an endpoint constructed from the one you used to get a specific user, such as users/USER_ID/reset-password
.
For example:
$ kcadm.sh update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2/reset-password -r demorealm -s type=password -s value=NEWPASSWORD -s temporary=true -n
The -n
parameter ensures that Red Hat Single Sign-On performs the PUT
command without performing a GET
command before the PUT
command. This is necessary because the reset-password
endpoint does not support GET
.
Listing assigned, available, and effective realm roles for a user
You can use a get-roles
command to list assigned, available, and effective realm roles for a user.
Specify the target user by user name or ID to list the user’s assigned realm roles.
For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --effective
Use the
--available
option to list realm roles that you can add to a user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --available
Listing assigned, available, and effective client roles for a user
Use a get-roles
command to list assigned, available, and effective client roles for a user.
Specify the target user by user name (
--uusername
option) or ID (--uid
option) and client by a clientId attribute (--cclientid
option) or an ID (--cid
option) to list assigned client roles for the user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management --effective
Use the
--available
option to list realm roles that you can add to a user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management --available
Adding realm roles to a user
Use an add-roles
command to add realm roles to a user.
Use the following example to add the user
role to user testuser
:
$ kcadm.sh add-roles --uusername testuser --rolename user -r demorealm
Removing realm roles from a user
Use a remove-roles
command to remove realm roles from a user.
Use the following example to remove the user
role from the user testuser
:
$ kcadm.sh remove-roles --uusername testuser --rolename user -r demorealm
Adding client roles to a user
Use an add-roles
command to add client roles to a user.
Use the following example to add two roles defined on the client realm management
, the create-client
role and the view-users
role, to the user testuser
.
$ kcadm.sh add-roles -r demorealm --uusername testuser --cclientid realm-management --rolename create-client --rolename view-users
Removing client roles from a user
Use a remove-roles
command to remove client roles from a user.
Use the following example to remove two roles defined on the realm management client:
$ kcadm.sh remove-roles -r demorealm --uusername testuser --cclientid realm-management --rolename create-client --rolename view-users
Listing a user’s sessions
- Identify the user’s ID,
-
Use the ID to compose an endpoint URI, such as
users/ID/sessions
. Use the
get
command to retrieve a list of the user’s sessions.For example:
$kcadm get users/6da5ab89-3397-4205-afaa-e201ff638f9e/sessions
Logging out a user from a specific session
- Determine the session’s ID as described earlier.
-
Use the session’s ID to compose an endpoint URI, such as
sessions/ID
. Use the
delete
command to invalidate the session.For example:
$ kcadm.sh delete sessions/d0eaa7cc-8c5d-489d-811a-69d3c4ec84d1
Logging out a user from all sessions
Use the user’s ID to construct an endpoint URI, such as users/ID/logout
.
Use the create
command to perform POST
on that endpoint URI.
For example:
$ kcadm.sh create users/6da5ab89-3397-4205-afaa-e201ff638f9e/logout -r demorealm -s realm=demorealm -s user=6da5ab89-3397-4205-afaa-e201ff638f9e
18.10. Group operations
Creating a group
Use the create
command on the groups
endpoint to create a new group.
For example:
$ kcadm.sh create groups -r demorealm -s name=Group
Listing groups
Use the get
command on the groups
endpoint to list groups.
For example:
$ kcadm.sh get groups -r demorealm
Getting a specific group
Use the group’s ID to construct an endpoint URI, such as groups/GROUP_ID
.
For example:
$ kcadm.sh get groups/51204821-0580-46db-8f2d-27106c6b5ded -r demorealm
Updating a group
Use the update
command with the same endpoint URI that you use to get a specific group.
For example:
$ kcadm.sh update groups/51204821-0580-46db-8f2d-27106c6b5ded -s 'attributes.email=["group@example.com"]' -r demorealm
Deleting a group
Use the delete
command with the same endpoint URI that you use to get a specific group.
For example:
$ kcadm.sh delete groups/51204821-0580-46db-8f2d-27106c6b5ded -r demorealm
Creating a subgroup
Find the ID of the parent group by listing groups. Use that ID to construct an endpoint URI, such as groups/GROUP_ID/children
.
For example:
$ kcadm.sh create groups/51204821-0580-46db-8f2d-27106c6b5ded/children -r demorealm -s name=SubGroup
Moving a group under another group
- Find the ID of an existing parent group and the ID of an existing child group.
-
Use the parent group’s ID to construct an endpoint URI, such as
groups/PARENT_GROUP_ID/children
. -
Run the
create
command on this endpoint and pass the child group’s ID as a JSON body.
For example:
$ kcadm.sh create groups/51204821-0580-46db-8f2d-27106c6b5ded/children -r demorealm -s id=08d410c6-d585-4059-bb07-54dcb92c5094 -s name=SubGroup
Get groups for a specific user
Use a user’s ID to determine a user’s membership in groups to compose an endpoint URI, such as users/USER_ID/groups
.
For example:
$ kcadm.sh get users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups -r demorealm
Adding a user to a group
Use the update
command with an endpoint URI composed of a user’s ID and a group’s ID, such as users/USER_ID/groups/GROUP_ID
, to add a user to a group.
For example:
$ kcadm.sh update users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups/ce01117a-7426-4670-a29a-5c118056fe20 -r demorealm -s realm=demorealm -s userId=b544f379-5fc4-49e5-8a8d-5cfb71f46f53 -s groupId=ce01117a-7426-4670-a29a-5c118056fe20 -n
Removing a user from a group
Use the delete
command on the same endpoint URI you use for adding a user to a group, such as users/USER_ID/groups/GROUP_ID
, to remove a user from a group.
For example:
$ kcadm.sh delete users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups/ce01117a-7426-4670-a29a-5c118056fe20 -r demorealm
Listing assigned, available, and effective realm roles for a group
Use a dedicated get-roles
command to list assigned, available, and effective realm roles for a group.
Specify the target group by name (
--gname
option), path (--gpath
option), or ID (--gid
option) to list assigned realm roles for the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --effective
Use the
--available
option to list realm roles that you can add to the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --available
Listing assigned, available, and effective client roles for a group
Use the get-roles
command to list assigned, available, and effective client roles for a group.
-
Specify the target group by name (
--gname
option) or ID (--gid
option), Specify the client by the clientId attribute (
--cclientid
option) or ID (--id
option) to list assigned client roles for the user.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management
Use the
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management --effective
Use the
--available
option to list realm roles that you can still add to the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management --available
18.11. Identity provider operations
Listing available identity providers
Use the serverinfo
endpoint to list available identity providers.
For example:
$ kcadm.sh get serverinfo -r demorealm --fields 'identityProviders(*)'
Red Hat Single Sign-On processes the serverinfo
endpoint similarly to the realms
endpoint. Red Hat Single Sign-On does not resolve the endpoint relative to a target realm because it exists outside any specific realm.
Listing configured identity providers
Use the identity-provider/instances
endpoint.
For example:
$ kcadm.sh get identity-provider/instances -r demorealm --fields alias,providerId,enabled
Getting a specific configured identity provider
Use the identity provider’s alias
attribute to construct an endpoint URI, such as identity-provider/instances/ALIAS
, to get a specific identity provider.
For example:
$ kcadm.sh get identity-provider/instances/facebook -r demorealm
Removing a specific configured identity provider
Use the delete
command with the same endpoint URI that you use to get a specific configured identity provider to remove a specific configured identity provider.
For example:
$ kcadm.sh delete identity-provider/instances/facebook -r demorealm
Configuring a Keycloak OpenID Connect identity provider
-
Use
keycloak-oidc
as theproviderId
when you create a new identity provider instance. Provide the
config
attributes:authorizationUrl
,tokenUrl
,clientId
, andclientSecret
.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=keycloak-oidc -s providerId=keycloak-oidc -s enabled=true -s 'config.useJwksUrl="true"' -s config.authorizationUrl=http://localhost:8180/auth/realms/demorealm/protocol/openid-connect/auth -s config.tokenUrl=http://localhost:8180/auth/realms/demorealm/protocol/openid-connect/token -s config.clientId=demo-oidc-provider -s config.clientSecret=secret
Configuring an OpenID Connect identity provider
Configure the generic OpenID Connect provider the same way you configure the Keycloak OpenID Connect provider, except you set the providerId
attribute value to oidc
.
Configuring a SAML 2 identity provider
-
Use
saml
as theproviderId
. -
Provide the
config
attributes:singleSignOnServiceUrl
,nameIDPolicyFormat
, andsignatureAlgorithm
.
For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=saml -s providerId=saml -s enabled=true -s 'config.useJwksUrl="true"' -s config.singleSignOnServiceUrl=http://localhost:8180/auth/realms/saml-broker-realm/protocol/saml -s config.nameIDPolicyFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent -s config.signatureAlgorithm=RSA_SHA256
Configuring a Facebook identity provider
-
Use
facebook
as theproviderId
. Provide the
config
attributes:clientId
andclientSecret
. You can find these attributes in the Facebook Developers application configuration page for your application. See see the facebook identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=facebook -s providerId=facebook -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=FACEBOOK_CLIENT_ID -s config.clientSecret=FACEBOOK_CLIENT_SECRET
Configuring a Google identity provider
-
Use
google
as theproviderId
. Provide the
config
attributes:clientId
andclientSecret
. You can find these attributes in the Google Developers application configuration page for your application. See the Google identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=google -s providerId=google -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=GOOGLE_CLIENT_ID -s config.clientSecret=GOOGLE_CLIENT_SECRET
Configuring a Twitter identity provider
-
Use
twitter
as theproviderId
. Provide the
config
attributesclientId
andclientSecret
. You can find these attributes in the Twitter Application Management application configuration page for your application. See the Twitter identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=google -s providerId=google -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=TWITTER_API_KEY -s config.clientSecret=TWITTER_API_SECRET
Configuring a GitHub identity provider
-
Use
github
as theproviderId
. Provide the
config
attributesclientId
andclientSecret
. You can find these attributes in the GitHub Developer Application Settings page for your application. See the Github identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=github -s providerId=github -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=GITHUB_CLIENT_ID -s config.clientSecret=GITHUB_CLIENT_SECRET
Configuring a LinkedIn identity provider
-
Use
linkedin
as theproviderId
. Provide the
config
attributesclientId
andclientSecret
. You can find these attributes in the LinkedIn Developer Console application page for your application. See the LinkedIn identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=linkedin -s providerId=linkedin -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=LINKEDIN_CLIENT_ID -s config.clientSecret=LINKEDIN_CLIENT_SECRET
Configuring a Microsoft Live identity provider
-
Use
microsoft
as theproviderId
. Provide the
config
attributesclientId
andclientSecret
. You can find these attributes in the Microsoft Application Registration Portal page for your application. See the Microsoft identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=microsoft -s providerId=microsoft -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=MICROSOFT_APP_ID -s config.clientSecret=MICROSOFT_PASSWORD
Configuring a Stack Overflow identity provider
-
Use
stackoverflow
command as theproviderId
. Provide the
config
attributesclientId
,clientSecret
, andkey
. You can find these attributes in the Stack Apps OAuth page for your application. See the Stack Overflow identity broker page for more information.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=stackoverflow -s providerId=stackoverflow -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=STACKAPPS_CLIENT_ID -s config.clientSecret=STACKAPPS_CLIENT_SECRET -s config.key=STACKAPPS_KEY
18.12. Storage provider operations
Configuring a Kerberos storage provider
-
Use the
create
command against thecomponents
endpoint. -
Specify the realm id as a value of the
parentId
attribute. -
Specify
kerberos
as the value of theproviderId
attribute, andorg.keycloak.storage.UserStorageProvider
as the value of theproviderType
attribute. For example:
$ kcadm.sh create components -r demorealm -s parentId=demorealmId -s id=demokerberos -s name=demokerberos -s providerId=kerberos -s providerType=org.keycloak.storage.UserStorageProvider -s 'config.priority=["0"]' -s 'config.debug=["false"]' -s 'config.allowPasswordAuthentication=["true"]' -s 'config.editMode=["UNSYNCED"]' -s 'config.updateProfileFirstLogin=["true"]' -s 'config.allowKerberosAuthentication=["true"]' -s 'config.kerberosRealm=["KEYCLOAK.ORG"]' -s 'config.keyTab=["http.keytab"]' -s 'config.serverPrincipal=["HTTP/localhost@KEYCLOAK.ORG"]' -s 'config.cachePolicy=["DEFAULT"]'
Configuring an LDAP user storage provider
-
Use the
create
command against thecomponents
endpoint. -
Specify
ldap
as the value of theproviderId
attribute, andorg.keycloak.storage.UserStorageProvider
as the value of theproviderType
attribute. -
Provide the realm ID as the value of the
parentId
attribute. Use the following example to create a Kerberos-integrated LDAP provider.
$ kcadm.sh create components -r demorealm -s name=kerberos-ldap-provider -s providerId=ldap -s providerType=org.keycloak.storage.UserStorageProvider -s parentId=3d9c572b-8f33-483f-98a6-8bb421667867 -s 'config.priority=["1"]' -s 'config.fullSyncPeriod=["-1"]' -s 'config.changedSyncPeriod=["-1"]' -s 'config.cachePolicy=["DEFAULT"]' -s config.evictionDay=[] -s config.evictionHour=[] -s config.evictionMinute=[] -s config.maxLifespan=[] -s 'config.batchSizeForSync=["1000"]' -s 'config.editMode=["WRITABLE"]' -s 'config.syncRegistrations=["false"]' -s 'config.vendor=["other"]' -s 'config.usernameLDAPAttribute=["uid"]' -s 'config.rdnLDAPAttribute=["uid"]' -s 'config.uuidLDAPAttribute=["entryUUID"]' -s 'config.userObjectClasses=["inetOrgPerson, organizationalPerson"]' -s 'config.connectionUrl=["ldap://localhost:10389"]' -s 'config.usersDn=["ou=People,dc=keycloak,dc=org"]' -s 'config.authType=["simple"]' -s 'config.bindDn=["uid=admin,ou=system"]' -s 'config.bindCredential=["secret"]' -s 'config.searchScope=["1"]' -s 'config.useTruststoreSpi=["ldapsOnly"]' -s 'config.connectionPooling=["true"]' -s 'config.pagination=["true"]' -s 'config.allowKerberosAuthentication=["true"]' -s 'config.serverPrincipal=["HTTP/localhost@KEYCLOAK.ORG"]' -s 'config.keyTab=["http.keytab"]' -s 'config.kerberosRealm=["KEYCLOAK.ORG"]' -s 'config.debug=["true"]' -s 'config.useKerberosForPasswordAuthentication=["true"]'
Removing a user storage provider instance
-
Use the storage provider instance’s
id
attribute to compose an endpoint URI, such ascomponents/ID
. Run the
delete
command against this endpoint.For example:
$ kcadm.sh delete components/3d9c572b-8f33-483f-98a6-8bb421667867 -r demorealm
Triggering synchronization of all users for a specific user storage provider
-
Use the storage provider’s
id
attribute to compose an endpoint URI, such asuser-storage/ID_OF_USER_STORAGE_INSTANCE/sync
. -
Add the
action=triggerFullSync
query parameter. Run the
create
command.For example:
$ kcadm.sh create user-storage/b7c63d02-b62a-4fc1-977c-947d6a09e1ea/sync?action=triggerFullSync
Triggering synchronization of changed users for a specific user storage provider
-
Use the storage provider’s
id
attribute to compose an endpoint URI, such asuser-storage/ID_OF_USER_STORAGE_INSTANCE/sync
. -
Add the
action=triggerChangedUsersSync
query parameter. Run the
create
command.For example:
$ kcadm.sh create user-storage/b7c63d02-b62a-4fc1-977c-947d6a09e1ea/sync?action=triggerChangedUsersSync
Test LDAP user storage connectivity
-
Run the
get
command on thetestLDAPConnection
endpoint. -
Provide query parameters
bindCredential
,bindDn
,connectionUrl
, anduseTruststoreSpi
. Set the
action
query parameter totestConnection
.For example:
$ kcadm.sh create testLDAPConnection -s action=testConnection -s bindCredential=secret -s bindDn=uid=admin,ou=system -s connectionUrl=ldap://localhost:10389 -s useTruststoreSpi=ldapsOnly
Test LDAP user storage authentication
-
Run the
get
command on thetestLDAPConnection
endpoint. -
Provide the query parameters
bindCredential
,bindDn
,connectionUrl
, anduseTruststoreSpi
. Set the
action
query parameter totestAuthentication
.For example:
$ kcadm.sh create testLDAPConnection -s action=testAuthentication -s bindCredential=secret -s bindDn=uid=admin,ou=system -s connectionUrl=ldap://localhost:10389 -s useTruststoreSpi=ldapsOnly
18.13. Adding mappers
Adding a hard-coded role LDAP mapper
-
Run the
create
command on thecomponents
endpoint. -
Set the
providerType
attribute toorg.keycloak.storage.ldap.mappers.LDAPStorageMapper
. -
Set the
parentId
attribute to the ID of the LDAP provider instance. Set the
providerId
attribute tohardcoded-ldap-role-mapper
. Ensure you provide a value ofrole
configuration parameter.For example:
$ kcadm.sh create components -r demorealm -s name=hardcoded-ldap-role-mapper -s providerId=hardcoded-ldap-role-mapper -s providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper -s parentId=b7c63d02-b62a-4fc1-977c-947d6a09e1ea -s 'config.role=["realm-management.create-client"]'
Adding an MS Active Directory mapper
-
Run the
create
command on thecomponents
endpoint. -
Set the
providerType
attribute toorg.keycloak.storage.ldap.mappers.LDAPStorageMapper
. -
Set the
parentId
attribute to the ID of the LDAP provider instance. Set the
providerId
attribute tomsad-user-account-control-mapper
.For example:
$ kcadm.sh create components -r demorealm -s name=msad-user-account-control-mapper -s providerId=msad-user-account-control-mapper -s providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper -s parentId=b7c63d02-b62a-4fc1-977c-947d6a09e1ea
Adding a user attribute LDAP mapper
-
Run the
create
command on thecomponents
endpoint. -
Set the
providerType
attribute toorg.keycloak.storage.ldap.mappers.LDAPStorageMapper
. -
Set the
parentId
attribute to the ID of the LDAP provider instance. Set the
providerId
attribute touser-attribute-ldap-mapper
.For example:
$ kcadm.sh create components -r demorealm -s name=user-attribute-ldap-mapper -s providerId=user-attribute-ldap-mapper -s providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper -s parentId=b7c63d02-b62a-4fc1-977c-947d6a09e1ea -s 'config."user.model.attribute"=["email"]' -s 'config."ldap.attribute"=["mail"]' -s 'config."read.only"=["false"]' -s 'config."always.read.value.from.ldap"=["false"]' -s 'config."is.mandatory.in.ldap"=["false"]'
Adding a group LDAP mapper
-
Run the
create
command on thecomponents
endpoint. -
Set the
providerType
attribute toorg.keycloak.storage.ldap.mappers.LDAPStorageMapper
. -
Set the
parentId
attribute to the ID of the LDAP provider instance. Set the
providerId
attribute togroup-ldap-mapper
.For example:
$ kcadm.sh create components -r demorealm -s name=group-ldap-mapper -s providerId=group-ldap-mapper -s providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper -s parentId=b7c63d02-b62a-4fc1-977c-947d6a09e1ea -s 'config."groups.dn"=[]' -s 'config."group.name.ldap.attribute"=["cn"]' -s 'config."group.object.classes"=["groupOfNames"]' -s 'config."preserve.group.inheritance"=["true"]' -s 'config."membership.ldap.attribute"=["member"]' -s 'config."membership.attribute.type"=["DN"]' -s 'config."groups.ldap.filter"=[]' -s 'config.mode=["LDAP_ONLY"]' -s 'config."user.roles.retrieve.strategy"=["LOAD_GROUPS_BY_MEMBER_ATTRIBUTE"]' -s 'config."mapped.group.attributes"=["admins-group"]' -s 'config."drop.non.existing.groups.during.sync"=["false"]' -s 'config.roles=["admins"]' -s 'config.groups=["admins-group"]' -s 'config.group=[]' -s 'config.preserve=["true"]' -s 'config.membership=["member"]'
Adding a full name LDAP mapper
-
Run the
create
command on thecomponents
endpoint. -
Set the
providerType
attribute toorg.keycloak.storage.ldap.mappers.LDAPStorageMapper
. -
Set the
parentId
attribute to the ID of the LDAP provider instance. Set the
providerId
attribute tofull-name-ldap-mapper
.For example:
$ kcadm.sh create components -r demorealm -s name=full-name-ldap-mapper -s providerId=full-name-ldap-mapper -s providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper -s parentId=b7c63d02-b62a-4fc1-977c-947d6a09e1ea -s 'config."ldap.full.name.attribute"=["cn"]' -s 'config."read.only"=["false"]' -s 'config."write.only"=["true"]'
18.14. Authentication operations
Setting a password policy
-
Set the realm’s
passwordPolicy
attribute to an enumeration expression that includes the specific policy provider ID and optional configuration. Use the following example to set a password policy to default values. The default values include:
- 27,500 hashing iterations
- at least one special character
- at least one uppercase character
- at least one digit character
-
not be equal to a user’s
username
be at least eight characters long
$ kcadm.sh update realms/demorealm -s 'passwordPolicy="hashIterations and specialChars and upperCase and digits and notUsername and length"'
- To use values different from defaults, pass the configuration in brackets.
Use the following example to set a password policy to:
- 25,000 hash iterations
- at least two special characters
- at least two uppercase characters
- at least two lowercase characters
- at least two digits
- be at least nine characters long
-
not be equal to a user’s
username
not repeat for at least four changes back
$ kcadm.sh update realms/demorealm -s 'passwordPolicy="hashIterations(25000) and specialChars(2) and upperCase(2) and lowerCase(2) and digits(2) and length(9) and notUsername and passwordHistory(4)"'
Obtaining the current password policy
You can get the current realm configuration by filtering all output except for the passwordPolicy
attribute.
For example, display passwordPolicy
for demorealm
.
$ kcadm.sh get realms/demorealm --fields passwordPolicy
Listing authentication flows
Run the get
command on the authentication/flows
endpoint.
For example:
$ kcadm.sh get authentication/flows -r demorealm
Getting a specific authentication flow
Run the get
command on the authentication/flows/FLOW_ID
endpoint.
For example:
$ kcadm.sh get authentication/flows/febfd772-e1a1-42fb-b8ae-00c0566fafb8 -r demorealm
Listing executions for a flow
Run the get
command on the authentication/flows/FLOW_ALIAS/executions
endpoint.
For example:
$ kcadm.sh get authentication/flows/Copy%20of%20browser/executions -r demorealm
Adding configuration to an execution
- Get execution for a flow.
- Note the ID of the flow.
-
Run the
create
command on theauthentication/executions/{executionId}/config
endpoint.
For example:
$ kcadm create "authentication/executions/a3147129-c402-4760-86d9-3f2345e401c7/config" -r examplerealm -b '{"config":{"x509-cert-auth.mapping-source-selection":"Match SubjectDN using regular expression","x509-cert-auth.regular-expression":"(.*?)(?:$)","x509-cert-auth.mapper-selection":"Custom Attribute Mapper","x509-cert-auth.mapper-selection.user-attribute-name":"usercertificate","x509-cert-auth.crl-checking-enabled":"","x509-cert-auth.crldp-checking-enabled":false,"x509-cert-auth.crl-relative-path":"crl.pem","x509-cert-auth.ocsp-checking-enabled":"","x509-cert-auth.ocsp-responder-uri":"","x509-cert-auth.keyusage":"","x509-cert-auth.extendedkeyusage":"","x509-cert-auth.confirmation-page-disallowed":""},"alias":"my_otp_config"}'
Getting configuration for an execution
- Get execution for a flow.
-
Note its
authenticationConfig
attribute, which contains the config ID. -
Run the
get
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm get "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm
Updating configuration for an execution
- Get the execution for the flow.
-
Get the flow’s
authenticationConfig
attribute. - Note the config ID from the attribute.
-
Run the
update
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm update "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm -b '{"id":"dd91611a-d25c-421a-87e2-227c18421833","alias":"my_otp_config","config":{"x509-cert-auth.extendedkeyusage":"","x509-cert-auth.mapper-selection.user-attribute-name":"usercertificate","x509-cert-auth.ocsp-responder-uri":"","x509-cert-auth.regular-expression":"(.*?)(?:$)","x509-cert-auth.crl-checking-enabled":"true","x509-cert-auth.confirmation-page-disallowed":"","x509-cert-auth.keyusage":"","x509-cert-auth.mapper-selection":"Custom Attribute Mapper","x509-cert-auth.crl-relative-path":"crl.pem","x509-cert-auth.crldp-checking-enabled":"false","x509-cert-auth.mapping-source-selection":"Match SubjectDN using regular expression","x509-cert-auth.ocsp-checking-enabled":""}}'
Deleting configuration for an execution
- Get execution for a flow.
-
Get the flows
authenticationConfig
attribute. - Note the config ID from the attribute.
-
Run the
delete
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm delete "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm
