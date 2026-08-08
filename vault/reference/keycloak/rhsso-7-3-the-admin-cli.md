---
title: "Chapter 19. The Admin CLI - Red Hat Single Sign-On 7.3 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-3-the-admin-cli
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.3/html/server_administration_guide/the_admin_cli
guide: server_administration_guide
version: 7.3
family: rhsso
documentKind: "Documentation"
abstract: "In previous chapters, we described how to use the Red Hat Single Sign-On Admin Console to perform administrative tasks. You can also perform those tasks from the command-line interface (CLI) by using the Admin CLI command-line tool. 19.1. Installing the Admin CLI The Admin CLI is packaged inside Red Hat Single Sign-On Server distribution. You can find execution scripts inside the bin directory. Th…"
---

# Chapter 19. The Admin CLI - Red Hat Single Sign-On 7.3 Server Administration Guide

Chapter 19. The Admin CLI
In previous chapters, we described how to use the Red Hat Single Sign-On Admin Console to perform administrative tasks. You can also perform those tasks from the command-line interface (CLI) by using the Admin CLI command-line tool.
19.1. Installing the Admin CLI
The Admin CLI is packaged inside Red Hat Single Sign-On Server distribution. You can find execution scripts inside the bin
directory.
The Linux script is called kcadm.sh
, and the script for Windows is called kcadm.bat
.
You can add the Red Hat Single Sign-On server directory to your PATH
to use the client from any location on your file system.
For example, on:
- Linux:
$ export PATH=$PATH:$KEYCLOAK_HOME/bin
$ kcadm.sh
- Windows:
c:\> set PATH=%PATH%;%KEYCLOAK_HOME%\bin
c:\> kcadm
We assume the KEYCLOAK_HOME
environment (env) variable is set to the path where you extracted the Red Hat Single Sign-On Server distribution.
To avoid repetition, the rest of this document only gives Windows examples in places where the difference in the CLI is more than just in the kcadm
command name.
19.2. Using the Admin CLI
The Admin CLI works by making HTTP requests to Admin REST endpoints. Access to them is protected and requires authentication.
Consult the Admin REST API documentation for details about JSON attributes for specific endpoints.
Start an authenticated session by providing credentials, that is, logging in. You are ready to perform create, read, update, and delete (CRUD) operations.
For example, on
Linux:
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm demo --user admin --client admin $ kcadm.sh create realms -s realm=demorealm -s enabled=true -o $ CID=$(kcadm.sh create clients -r demorealm -s clientId=my_client -s 'redirectUris=["http://localhost:8980/myapp/*"]' -i) $ kcadm.sh get clients/$CID/installation/providers/keycloak-oidc-keycloak-json
Windows:
c:\> kcadm config credentials --server http://localhost:8080/auth --realm demo --user admin --client admin c:\> kcadm create realms -s realm=demorealm -s enabled=true -o c:\> kcadm create clients -r demorealm -s clientId=my_client -s "redirectUris=[\"http://localhost:8980/myapp/*\"]" -i > clientid.txt c:\> set /p CID=<clientid.txt c:\> kcadm get clients/%CID%/installation/providers/keycloak-oidc-keycloak-json
In a production environment, you must access Red Hat Single Sign-On with
https:
to avoid exposing tokens to network sniffers. If a server’s certificate is not issued by one of the trusted certificate authorities (CAs) that are included in Java’s default certificate truststore, prepare atruststore.jks
file and instruct the Admin CLI to use it.For example, on:
Linux:
$ kcadm.sh config truststore --trustpass $PASSWORD ~/.keycloak/truststore.jks
Windows:
c:\> kcadm config truststore --trustpass %PASSWORD% %HOMEPATH%\.keycloak\truststore.jks
19.3. Authenticating
When you log in with the Admin CLI, you specify a server endpoint URL and a realm, and then you specify a user name. Another option is to specify only a clientId, which results in using a special "service account". When you log in using a user name, you must use a password for the specified user. When you log in using a clientId, you only need the client secret, not the user password. You could also use Signed JWT
instead of the client secret.
Make sure the account used for the session has the proper permissions to invoke Admin REST API operations. For example, the realm-admin
role of the realm-management
client allows the user to administer the realm within which the user is defined.
There are two primary mechanisms for authentication. One mechanism uses kcadm config credentials
to start an authenticated session.
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
This approach maintains an authenticated session between the kcadm
command invocations by saving the obtained access token and the associated refresh token. It may also maintain other secrets in a private configuration file. See next chapter for more information on the configuration file.
The second approach only authenticates each command invocation for the duration of that invocation. This approach increases the load on the server and the time spent with roundtrips obtaining tokens. The benefit of this approach is not needing to save any tokens between invocations, which means nothing is saved to disk. This mode is used when the --no-config
argument is specified.
For example, when performing an operation, we specify all the information required for authentication.
$ kcadm.sh get realms --no-config --server http://localhost:8080/auth --realm master --user admin --password admin
Run the kcadm.sh help
command for more information on using the Admin CLI.
Run the kcadm.sh config credentials --help
command for more information about starting an authenticated session.
19.4. Working with alternative configurations
By default, the Admin CLI automatically maintains a configuration file called kcadm.config
located under the user’s home directory. In Linux-based systems, the full path name is $HOME/.keycloak/kcadm.config
. On Windows, the full path name is %HOMEPATH%\.keycloak\kcadm.config
. You can use the --config
option to point to a different file or location so you can maintain multiple authenticated sessions in parallel.
It is best to perform operations tied to a single configuration file from a single thread.
Make sure you do not make the configuration file visible to other users on the system. It contains access tokens and secrets that should be kept private. By default, the ~/.keycloak
directory and its content are created automatically with proper access limits. If the directory already exists, its permissions are not updated.
If your unique circumstances require you to avoid storing secrets inside a configuration file, you can do so. It will be less convenient and you will have to make more token requests. To not store secrets, use the --no-config
option with all your commands and specify all the authentication information needed by the config credentials
command with each kcadm
invocation.
19.5. Basic operations and resource URIs
The Admin CLI allows you to generically perform CRUD operations against Admin REST API endpoints with additional commands that simplify performing certain tasks.
The main usage pattern is listed below, where the create
, get
, update
, and delete
commands are mapped to the HTTP verbs POST
, GET
, PUT
, and DELETE
, respectively.
$ kcadm.sh create ENDPOINT [ARGUMENTS]
$ kcadm.sh get ENDPOINT [ARGUMENTS]
$ kcadm.sh update ENDPOINT [ARGUMENTS]
$ kcadm.sh delete ENDPOINT [ARGUMENTS]
ENDPOINT is a target resource URI and can either be absolute (starting with http:
or https:
) or relative, used to compose an absolute URL of the following format:
SERVER_URI/admin/realms/REALM/ENDPOINT
For example, if you authenticate against the server http://localhost:8080/auth and realm is master
, then using users
as ENDPOINT results in the resource URL http://localhost:8080/auth/admin/realms/master/users.
If you set ENDPOINT to clients
, the effective resource URI would be http://localhost:8080/auth/admin/realms/master/clients.
There is a realms
endpoint that is treated slightly differently because it is the container for realms. It resolves to:
SERVER_URI/admin/realms
There is also a serverinfo
endpoint, which is treated the same way because it is independent of realms.
When you authenticate as a user with realm-admin powers, you might need to perform commands on multiple realms. In that case, specify the -r
option to tell explicitly which realm the command should be executed against. Instead of using REALM
as specified via the --realm
option of kcadm.sh config credentials
, the TARGET_REALM
is used.
SERVER_URI/admin/realms/TARGET_REALM/ENDPOINT
For example,
$ kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
$ kcadm.sh create users -s username=testuser -s enabled=true -r demorealm
In this example, you start a session authenticated as the admin
user in the master
realm. You then perform a POST call against the resource URL http://localhost:8080/auth/admin/realms/demorealm/users
.
The create
and update
commands send a JSON body to the server by default. You can use -f FILENAME
to read a premade document from a file. When you can use -f -
option, the message body is read from standard input. You can also specify individual attributes and their values as seen in the previous create users
example. They are composed into a JSON body and sent to the server.
There are several ways to update a resource using the update
command. You can first determine the current state of a resource and save it to a file, and then edit that file and send it to the server for updating.
For example:
$ kcadm.sh get realms/demorealm > demorealm.json
$ vi demorealm.json
$ kcadm.sh update realms/demorealm -f demorealm.json
This method updates the resource on the server with all the attributes in the sent JSON document.
Another option is to perform an on-the-fly update using the -s, --set
options to set new values.
For example:
$ kcadm.sh update realms/demorealm -s enabled=false
That method only updates the enabled
attribute to false
.
By default, the update
command first performs a get
and then merges the new attribute values with existing values. This is the preferred behavior. In some cases, the endpoint may support the PUT
command but not the GET
command. You can use the -n
option to perform a "no-merge" update, which performs a PUT
command without first running a GET
command.
19.6. Realm operations
Creating a new realm
Use the create
command on the realms
endpoint to create a new enabled realm, and set the attributes to realm
and enabled
.
$ kcadm.sh create realms -s realm=demorealm -s enabled=true
A realm is not enabled by default. By enabling it, you can use a realm immediately for authentication.
A description for a new object can also be in a JSON format.
$ kcadm.sh create realms -f demorealm.json
You can send a JSON document with realm attributes directly from a file or piped to a standard input.
For example, on:
- Linux:
$ kcadm.sh create realms -f - << EOF
{ "realm": "demorealm", "enabled": true }
EOF
- Windows:
c:\> echo { "realm": "demorealm", "enabled": true } | kcadm create realms -f -
Listing existing realms
The following command returns a list of all realms.
$ kcadm.sh get realms
A list of realms is additionally filtered on the server to return only realms a user can see.
Returning the entire realm description often provides too much information. Most users are interested only in a subset of attributes, such as realm name and whether the realm is enabled. You can specify which attributes to return by using the --fields
option.
$ kcadm.sh get realms --fields realm,enabled
You can also display the result as comma separated values.
$ kcadm.sh get realms --fields realm --format csv --noquotes
Getting a specific realm
You append a realm name to a collection URI to get an individual realm.
$ kcadm.sh get realms/master
Updating a realm
Use the
-s
option to set new values for the attributes when you want to change only some of the realm’s attributes.For example:
$ kcadm.sh update realms/demorealm -s enabled=false
If you want to set all writable attributes with new values, run a
get
command, edit the current values in the JSON file, and resubmit.For example:
$ kcadm.sh get realms/demorealm > demorealm.json $ vi demorealm.json $ kcadm.sh update realms/demorealm -f demorealm.json
Deleting a realm
Run the following command to delete a realm.
$ kcadm.sh delete realms/demorealm
Turning on all login page options for the realm
Set the attributes controlling specific capabilities to true
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
.For example, on:
Linux:
$ kcadm.sh create components -r demorealm -s name=rsa-generated -s providerId=rsa-generated -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s 'config.priority=["101"]' -s 'config.enabled=["true"]' -s 'config.active=["true"]' -s 'config.keySize=["2048"]'
Windows:
c:\> kcadm create components -r demorealm -s name=rsa-generated -s providerId=rsa-generated -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s "config.priority=[\"101\"]" -s "config.enabled=[\"true\"]" -s "config.active=[\"true\"]" -s "config.keySize=[\"2048\"]"
Set the
parentId
attribute to the value of the target realm’s ID.The newly added key should now become the active key as revealed by
kcadm.sh get keys -r demorealm
.
Adding new realm keys from a Java Key Store file
Add a new key provider to add a new key pair already prepared as a JKS file on the server.
For example, on:
Linux:
$ kcadm.sh create components -r demorealm -s name=java-keystore -s providerId=java-keystore -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s 'config.priority=["101"]' -s 'config.enabled=["true"]' -s 'config.active=["true"]' -s 'config.keystore=["/opt/keycloak/keystore.jks"]' -s 'config.keystorePassword=["secret"]' -s 'config.keyPassword=["secret"]' -s 'config.alias=["localhost"]'
Windows:
c:\> kcadm create components -r demorealm -s name=java-keystore -s providerId=java-keystore -s providerType=org.keycloak.keys.KeyProvider -s parentId=959844c1-d149-41d7-8359-6aa527fca0b0 -s "config.priority=[\"101\"]" -s "config.enabled=[\"true\"]" -s "config.active=[\"true\"]" -s "config.keystore=[\"/opt/keycloak/keystore.jks\"]" -s "config.keystorePassword=[\"secret\"]" -s "config.keyPassword=[\"secret\"]" -s "config.alias=[\"localhost\"]"
-
Make sure to change the attribute values for
keystore
,keystorePassword
,keyPassword
, andalias
to match your specific keystore. -
Set the
parentId
attribute to the value of the target realm’s ID.
Making the key passive or disabling the key
Identify the key you want to make passive
$ kcadm.sh get keys -r demorealm
-
Use the key’s
providerId
attribute to construct an endpoint URI, such ascomponents/PROVIDER_ID
. Perform an
update
.For example, on:
Linux:
$ kcadm.sh update components/PROVIDER_ID -r demorealm -s 'config.active=["false"]'
Windows:
c:\> kcadm update components/PROVIDER_ID -r demorealm -s "config.active=[\"false\"]"
You can update other key attributes.
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
- Make sure the key you are deleting has been passive and disabled to prevent any existing tokens held by applications and users from abruptly failing to work.
Identify the key you want to make passive.
$ kcadm.sh get keys -r demorealm
Use the
providerId
of that key to perform a delete.$ kcadm.sh delete components/PROVIDER_ID -r demorealm
Configuring event logging for a realm
Use the update
command on the events/config
endpoint.
The eventsListeners
attribute contains a list of EventListenerProviderFactory IDs that specify all event listeners receiving events. Separately, there are attributes that control a built-in event storage, which allows querying past events via the Admin REST API. There is separate control over logging of service calls (eventsEnabled
) and auditing events triggered during Admin Console or Admin REST API (adminEventsEnabled
). You may want to set up expiry of old events so that your database does not fill up; eventsExpiration
is set to time-to-live expressed in seconds.
Here is an example of setting up a built-in event listener that receives all the events and logs them through jboss-logging. (Using a logger called org.keycloak.events
, error events are logged as WARN
, and others are logged as DEBUG
.)
For example, on:
- Linux:
$ kcadm.sh update events/config -r demorealm -s 'eventsListeners=["jboss-logging"]'
- Windows:
c:\> kcadm update events/config -r demorealm -s "eventsListeners=[\"jboss-logging\"]"
Here is an example of turning on storage of all available ERROR events—not including auditing events—for 2 days so they can be retrieved via Admin REST.
For example, on:
- Linux:
$ kcadm.sh update events/config -r demorealm -s eventsEnabled=true -s 'enabledEventTypes=["LOGIN_ERROR","REGISTER_ERROR","LOGOUT_ERROR","CODE_TO_TOKEN_ERROR","CLIENT_LOGIN_ERROR","FEDERATED_IDENTITY_LINK_ERROR","REMOVE_FEDERATED_IDENTITY_ERROR","UPDATE_EMAIL_ERROR","UPDATE_PROFILE_ERROR","UPDATE_PASSWORD_ERROR","UPDATE_TOTP_ERROR","VERIFY_EMAIL_ERROR","REMOVE_TOTP_ERROR","SEND_VERIFY_EMAIL_ERROR","SEND_RESET_PASSWORD_ERROR","SEND_IDENTITY_PROVIDER_LINK_ERROR","RESET_PASSWORD_ERROR","IDENTITY_PROVIDER_FIRST_LOGIN_ERROR","IDENTITY_PROVIDER_POST_LOGIN_ERROR","CUSTOM_REQUIRED_ACTION_ERROR","EXECUTE_ACTIONS_ERROR","CLIENT_REGISTER_ERROR","CLIENT_UPDATE_ERROR","CLIENT_DELETE_ERROR"]' -s eventsExpiration=172800
- Windows:
c:\> kcadm update events/config -r demorealm -s eventsEnabled=true -s "enabledEventTypes=[\"LOGIN_ERROR\",\"REGISTER_ERROR\",\"LOGOUT_ERROR\",\"CODE_TO_TOKEN_ERROR\",\"CLIENT_LOGIN_ERROR\",\"FEDERATED_IDENTITY_LINK_ERROR\",\"REMOVE_FEDERATED_IDENTITY_ERROR\",\"UPDATE_EMAIL_ERROR\",\"UPDATE_PROFILE_ERROR\",\"UPDATE_PASSWORD_ERROR\",\"UPDATE_TOTP_ERROR\",\"VERIFY_EMAIL_ERROR\",\"REMOVE_TOTP_ERROR\",\"SEND_VERIFY_EMAIL_ERROR\",\"SEND_RESET_PASSWORD_ERROR\",\"SEND_IDENTITY_PROVIDER_LINK_ERROR\",\"RESET_PASSWORD_ERROR\",\"IDENTITY_PROVIDER_FIRST_LOGIN_ERROR\",\"IDENTITY_PROVIDER_POST_LOGIN_ERROR\",\"CUSTOM_REQUIRED_ACTION_ERROR\",\"EXECUTE_ACTIONS_ERROR\",\"CLIENT_REGISTER_ERROR\",\"CLIENT_UPDATE_ERROR\",\"CLIENT_DELETE_ERROR\"]" -s eventsExpiration=172800
Here is an example of how to reset stored event types to all available event types; setting to empty list is the same as enumerating all.
$ kcadm.sh update events/config -r demorealm -s enabledEventTypes=[]
Here is an example of how to enable storage of auditing events.
$ kcadm.sh update events/config -r demorealm -s adminEventsEnabled=true -s adminEventsDetailsEnabled=true
Here is an example of how to get the last 100 events; they are ordered from newest to oldest.
$ kcadm.sh get events --offset 0 --limit 100
Here is an example of how to delete all saved events.
$ kcadm delete events
Flushing the caches
-
Use the
create
command and one of the following endpoints:clear-realm-cache
,clear-user-cache
, orclear-keys-cache
. Set
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
to one ofFAIL
,SKIP
,OVERWRITE
. Use
-f
to submit the exported realm.json
fileFor example:
$ kcadm.sh create partialImport -r demorealm2 -s ifResourceExists=FAIL -o -f demorealm.json
If realm does not yet exist, you first have to create it.
For example:
$ kcadm.sh create realms -s realm=demorealm2 -s enabled=true
19.7. Role operations
Creating a realm role
Use the roles
endpoint to create a realm role.
$ kcadm.sh create roles -r demorealm -s name=user -s 'description=Regular user with limited set of permissions'
Creating a client role
Identify the client first and then use the
get
command to list available clients when creating a client role.$ kcadm.sh get clients -r demorealm --fields id,clientId
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
You can also use the get-roles
command.
$ kcadm.sh get-roles -r demorealm
Listing client roles
There is a dedicated get-roles
command to simplify listing realm and client roles. It is an extension of the get
command and behaves the same with additional semantics for listing roles.
Use the get-roles
command, passing it either the clientId attribute (via the --cclientid
option) or id
(via the --cid
option) to identify the client to list client roles.
For example:
$ kcadm.sh get-roles -r demorealm --cclientid realm-management
Getting a specific realm role
Use the get
command and the role name
to construct an endpoint URI for a specific realm role: roles/ROLE_NAME
, where user
is the name of the existing role.
For example:
$ kcadm.sh get roles/user -r demorealm
You can also use the special get-roles
command, passing it a role name (via the --rolename
option) or ID (via the --roleid
option).
For example:
$ kcadm.sh get-roles -r demorealm --rolename user
Getting a specific client role
Use a dedicated get-roles
command, passing it either the clientId attribute (via the --cclientid
option) or ID (via the --cid
option) to identify the client, and passing it either the role name (via the --rolename
option) or ID (via the --roleid
) to identify a specific client role.
For example:
$ kcadm.sh get-roles -r demorealm --cclientid realm-management --rolename manage-clients
Updating a realm role
Use the update
command with the same endpoint URI that you used to get a specific realm role.
For example:
$ kcadm.sh update roles/user -r demorealm -s 'description=Role representing a regular user'
Updating a client role
Use the update
command with the same endpoint URI that you used to get a specific client role.
For example:
$ kcadm.sh update clients/a95b6af3-0bdc-4878-ae2e-6d61a4eca9a0/roles/editor -r demorealm -s 'description=User that can edit, and publish articles'
Deleting a realm role
Use the delete
command with the same endpoint URI that you used to get a specific realm role.
For example:
$ kcadm.sh delete roles/user -r demorealm
Deleting a client role
Use the delete
command with the same endpoint URI that you used to get a specific client role.
For example:
$ kcadm.sh delete clients/a95b6af3-0bdc-4878-ae2e-6d61a4eca9a0/roles/editor -r demorealm
Listing assigned, available, and effective realm roles for a composite role
Use a dedicated get-roles
command to list assigned, available, and effective realm roles for a composite role.
To list assigned realm roles for the composite role, you can specify the target composite role by either name (via the
--rname
option) or ID (via the--rid
option).For example:
$ kcadm.sh get-roles -r demorealm --rname testrole
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --effective
Use the
--available
option to list realm roles that can still be added to the composite role.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --available
Listing assigned, available, and effective client roles for a composite role
Use a dedicated get-roles
command to list assigned, available, and effective client roles for a composite role.
To list assigned client roles for the composite role, you can specify the target composite role by either name (via the
--rname
option) or ID (via the--rid
option) and client by either the clientId attribute (via the--cclientid
option) or ID (via the--cid
option).For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management --effective
Use the
--available
option to list realm roles that can still be added to the target composite role.For example:
$ kcadm.sh get-roles -r demorealm --rname testrole --cclientid realm-management --available
Adding realm roles to a composite role
There is a dedicated add-roles
command that can be used for adding realm roles and client roles.
The following example adds the user
role to the composite role testrole
.
$ kcadm.sh add-roles --rname testrole --rolename user -r demorealm
Removing realm roles from a composite role
There is a dedicated remove-roles
command that can be used to remove realm roles and client roles.
The following example removes the user
role from the target composite role testrole
.
$ kcadm.sh remove-roles --rname testrole --rolename user -r demorealm
Adding client roles to a realm role
Use a dedicated add-roles
command that can be used for adding realm roles and client roles.
The following example adds the roles defined on the client realm-management
- create-client
role and the view-users
role to the testrole
composite role.
$ kcadm.sh add-roles -r demorealm --rname testrole --cclientid realm-management --rolename create-client --rolename view-users
Adding client roles to a client role
Determine the ID of the composite client role by using the
get-roles
command.For example:
$ kcadm.sh get-roles -r demorealm --cclientid test-client --rolename operations
-
Assume that there is a client with a clientId attribute of
test-client
, a client role calledsupport
, and another client role calledoperations
, which becomes a composite role, that has an ID of "fc400897-ef6a-4e8c-872b-1581b7fa8a71". Use the following example to add another role to the composite role.
$ kcadm.sh add-roles -r demorealm --cclientid test-client --rid fc400897-ef6a-4e8c-872b-1581b7fa8a71 --rolename support
List the roles of a composite role by using the
get-roles --all
command.For example:
$ kcadm.sh get-roles --rid fc400897-ef6a-4e8c-872b-1581b7fa8a71 --all
Removing client roles from a composite role
Use a dedicated remove-roles
command to remove client roles from a composite role.
Use the following example to remove two roles defined on the client realm management
- create-client
role and the view-users
role from the testrole
composite role.
$ kcadm.sh remove-roles -r demorealm --rname testrole --cclientid realm-management --rolename create-client --rolename view-users
Adding client roles to a group
Use a dedicated add-roles
command that can be used for adding realm roles and client roles.
The following example adds the roles defined on the client realm-management
- create-client
role and the view-users
role to the Group
group (via the --gname
option). The group can alternatively be specified by ID (via the --gid
option).
See Group operations for more operations that can be performed to groups.
$ kcadm.sh add-roles -r demorealm --gname Group --cclientid realm-management --rolename create-client --rolename view-users
Removing client roles from a group
Use a dedicated remove-roles
command to remove client roles from a group.
Use the following example to remove two roles defined on the client realm management
- create-client
role and the view-users
role from the Group
group.
See Group operations for more operations that can be performed to groups.
$ kcadm.sh remove-roles -r demorealm --gname Group --cclientid realm-management --rolename create-client --rolename view-users
19.8. Client operations
Creating a client
Run the
create
command on aclients
endpoint to create a new client.For example:
$ kcadm.sh create clients -r demorealm -s clientId=myapp -s enabled=true
Specify a secret if you want to set a secret for adapters to authenticate.
For example:
$ kcadm.sh create clients -r demorealm -s clientId=myapp -s enabled=true -s clientAuthenticatorType=client-secret -s secret=d0b8122f-8dfb-46b7-b68a-f5cc4e25d000
Listing clients
Use the get
command on the clients
endpoint to list clients.
For example:
$ kcadm.sh get clients -r demorealm --fields id,clientId
This example filters the output to list only the id
and clientId
attributes.
Getting a specific client
Use a client’s ID to construct an endpoint URI that targets a specific client, such as clients/ID
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm
Getting the current secret for a specific client
Use a client’s ID to construct an endpoint URI, such as clients/ID/client-secret
.
For example:
$ kcadm.sh get clients/$CID/client-secret
Getting an adapter configuration file (keycloak.json) for a specific client
Use a client’s ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/keycloak-oidc-keycloak-json
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3/installation/providers/keycloak-oidc-keycloak-json -r demorealm
Getting a WildFly subsystem adapter configuration for a specific client
Use a client’s ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/keycloak-oidc-jboss-subsystem
.
For example:
$ kcadm.sh get clients/c7b8547f-e748-4333-95d0-410b76b3f4a3/installation/providers/keycloak-oidc-jboss-subsystem -r demorealm
Getting a Docker-v2 example configuration for a specific client
Use a client’s ID to construct an endpoint URI that targets a specific client, such as clients/ID/installation/providers/docker-v2-compose-yaml
.
Note that response will be in .zip
format.
For example:
$ kcadm.sh get http://localhost:8080/auth/admin/realms/demorealm/clients/8f271c35-44e3-446f-8953-b0893810ebe7/installation/providers/docker-v2-compose-yaml -r demorealm > keycloak-docker-compose-yaml.zip
Updating a client
Use the update
command with the same endpoint URI that you used to get a specific client.
For example, on:
- Linux:
$ kcadm.sh update clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm -s enabled=false -s publicClient=true -s 'redirectUris=["http://localhost:8080/myapp/*"]' -s baseUrl=http://localhost:8080/myapp -s adminUrl=http://localhost:8080/myapp
- Windows:
c:\> kcadm update clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm -s enabled=false -s publicClient=true -s "redirectUris=[\"http://localhost:8080/myapp/*\"]" -s baseUrl=http://localhost:8080/myapp -s adminUrl=http://localhost:8080/myapp
Deleting a client
Use the delete
command with the same endpoint URI that you used to get a specific client.
For example:
$ kcadm.sh delete clients/c7b8547f-e748-4333-95d0-410b76b3f4a3 -r demorealm
Adding or removing roles for client’s service account
Service account for the client is just a special kind of user account with username service-account-CLIENT_ID
. You can perform user operations on this account as if it was a regular user.
19.9. User operations
Creating a user
Run the create
command on the users
endpoint to create a new user.
For example:
$ kcadm.sh create users -r demorealm -s username=testuser -s enabled=true
Listing users
Use the users
endpoint to list users. The target user will have to change the password the next time they log in.
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
Filtering does not use exact matching. For example, the above example would match the value of the username
attribute against the *testuser*
pattern.
You can also filter across multiple attributes by specifying multiple -q
options, which return only users that match the condition for all the attributes.
Getting a specific user
Use a user’s ID to compose an endpoint URI, such as users/USER_ID
.
For example:
$ kcadm.sh get users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm
Updating a user
Use the update
command with the same endpoint URI that you used to get a specific user.
For example, on:
- Linux:
$ kcadm.sh update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm -s 'requiredActions=["VERIFY_EMAIL","UPDATE_PROFILE","CONFIGURE_TOTP","UPDATE_PASSWORD"]'
- Windows:
c:\> kcadm update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm -s "requiredActions=[\"VERIFY_EMAIL\",\"UPDATE_PROFILE\",\"CONFIGURE_TOTP\",\"UPDATE_PASSWORD\"]"
Deleting a user
Use the delete
command with the same endpoint URI that you used to get a specific user.
For example:
$ kcadm.sh delete users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2 -r demorealm
Resetting a user’s password
Use the dedicated set-password
command to reset a user’s password.
For example:
$ kcadm.sh set-password -r demorealm --username testuser --new-password NEWPASSWORD --temporary
That command sets a temporary password for the user. The target user will have to change the password the next time they log in.
You can use --userid
if you want to specify the user by using the id
attribute.
You can achieve the same result using the update
command on an endpoint constructed from the one you used to get a specific user, such as users/USER_ID/reset-password
.
For example:
$ kcadm.sh update users/0ba7a3fd-6fd8-48cd-a60b-2e8fd82d56e2/reset-password -r demorealm -s type=password -s value=NEWPASSWORD -s temporary=true -n
The last parameter (-n
) ensures that only the PUT
command is performed without a prior GET
command. It is necessary in this instance because the reset-password
endpoint does not support GET
.
Listing assigned, available, and effective realm roles for a user
You can use a dedicated get-roles
command to list assigned, available, and effective realm roles for a user.
Specify the target user by either user name or ID to list assigned realm roles for the user.
For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --effective
Use the
--available
option to list realm roles that can still be added to the user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --available
Listing assigned, available, and effective client roles for a user
Use a dedicated get-roles
command to list assigned, available, and effective client roles for a user.
Specify the target user by either a user name (via the
--uusername
option) or an ID (via the--uid
option) and client by either a clientId attribute (via the--cclientid
option) or an ID (via the--cid
option) to list assigned client roles for the user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management --effective
Use the
--available
option to list realm roles that can still be added to the user.For example:
$ kcadm.sh get-roles -r demorealm --uusername testuser --cclientid realm-management --available
Adding realm roles to a user
Use a dedicated add-roles
command to add realm roles to a user.
Use the following example to add the user
role to user testuser
.
$ kcadm.sh add-roles --uusername testuser --rolename user -r demorealm
Removing realm roles from a user
Use a dedicated remove-roles
command to remove realm roles from a user.
Use the following example to remove the user
role from the user testuser
.
$ kcadm.sh remove-roles --uusername testuser --rolename user -r demorealm
Adding client roles to a user
Use a dedicated add-roles
command to add client roles to a user.
Use the following example to add two roles defined on the client realm management
- create-client
role and the view-users
role to the user testuser
.
$ kcadm.sh add-roles -r demorealm --uusername testuser --cclientid realm-management --rolename create-client --rolename view-users
Removing client roles from a user
Use a dedicated remove-roles
command to remove client roles from a user.
Use the following example to remove two roles defined on the realm management client.
$ kcadm.sh remove-roles -r demorealm --uusername testuser --cclientid realm-management --rolename create-client --rolename view-users
Listing a user’s sessions
-
Identify the user’s ID, and then use it to compose an endpoint URI, such as
users/ID/sessions
. Use the
get
command to retrieve a list of the user’s sessions.For example:
$kcadm get users/6da5ab89-3397-4205-afaa-e201ff638f9e/sessions
Logging out a user from a specific session
- Determine the session’s ID as described above.
-
Use the session’s ID to compose an endpoint URI, such as
sessions/ID
. Use the
delete
command to invalidate the session.For example:
$ kcadm.sh delete sessions/d0eaa7cc-8c5d-489d-811a-69d3c4ec84d1
Logging out a user from all sessions
You need a user’s ID to construct an endpoint URI, such as users/ID/logout
.
Use the create
command to perform POST
on that endpoint URI.
For example:
$ kcadm.sh create users/6da5ab89-3397-4205-afaa-e201ff638f9e/logout -r demorealm -s realm=demorealm -s user=6da5ab89-3397-4205-afaa-e201ff638f9e
19.10. Group operations
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
command with the same endpoint URI that you used to get a specific group.
For example:
$ kcadm.sh update groups/51204821-0580-46db-8f2d-27106c6b5ded -s 'attributes.email=["group@example.com"]' -r demorealm
Deleting a group
Use the delete
command with the same endpoint URI that you used to get a specific group.
For example:
$ kcadm.sh delete groups/51204821-0580-46db-8f2d-27106c6b5ded -r demorealm
Creating a subgroup
Find the ID of the parent group by listing groups, and then use that ID to construct an endpoint URI, such as groups/GROUP_ID/children
.
For example:
$ kcadm.sh create groups/51204821-0580-46db-8f2d-27106c6b5ded/children -r demorealm -s name=SubGroup
Moving a group under another group
- Find the ID of an existing parent group and of an existing child group.
-
Use the parent group’s ID to construct an endpoint URI, such as
groups/PARENT_GROUP_ID/children
. -
Run the
create
command on this endpoint and pass the child group’s ID as a JSON body.
For example:
$ kcadm.sh create groups/51204821-0580-46db-8f2d-27106c6b5ded/children -r demorealm -s id=08d410c6-d585-4059-bb07-54dcb92c5094
Get groups for a specific user
Use a user’s ID to determine a user’s membership in groups to compose an endpoint URI, such as users/USER_ID/groups
.
For example:
$ kcadm.sh get users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups -r demorealm
Adding a user to a group
Use the update
command with an endpoint URI composed from user’s ID and a group’s ID, such as users/USER_ID/groups/GROUP_ID
, to add a user to a group.
For example:
$ kcadm.sh update users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups/ce01117a-7426-4670-a29a-5c118056fe20 -r demorealm -s realm=demorealm -s userId=b544f379-5fc4-49e5-8a8d-5cfb71f46f53 -s groupId=ce01117a-7426-4670-a29a-5c118056fe20 -n
Removing a user from a group
Use the delete
command on the same endpoint URI as used for adding a user to a group, such as users/USER_ID/groups/GROUP_ID
, to remove a user from a group.
For example:
$ kcadm.sh delete users/b544f379-5fc4-49e5-8a8d-5cfb71f46f53/groups/ce01117a-7426-4670-a29a-5c118056fe20 -r demorealm
Listing assigned, available, and effective realm roles for a group
Use a dedicated get-roles
command to list assigned, available, and effective realm roles for a group.
Specify the target group by name (via the
--gname
option), path (via the [command]--gpath
option), or ID (via the--gid
option) to list assigned realm roles for the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --effective
Use the
--available
option to list realm roles that can still be added to the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --available
Listing assigned, available, and effective client roles for a group
Use a dedicated get-roles
command to list assigned, available, and effective client roles for a group.
Specify the target group by either name (via the
--gname
option) or ID (via the--gid
option), and client by either the clientId attribute (via the [command]--cclientid
option) or ID (via the--id
option) to list assigned client roles for the user.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management
Use the additional
--effective
option to list effective realm roles.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management --effective
Use the
--available
option to list realm roles that can still be added to the group.For example:
$ kcadm.sh get-roles -r demorealm --gname Group --cclientid realm-management --available
19.11. Identity provider operations
Listing available identity providers
Use the serverinfo
endpoint to list available identity providers.
For example:
$ kcadm.sh get serverinfo -r demorealm --fields 'identityProviders(*)'
The serverinfo
endpoint is handled similarly to the realms
endpoint in that it is not resolved relative to a target realm because it exists outside any specific realm.
Listing configured identity providers
Use the identity-provider/instances
endpoint.
For example:
$ kcadm.sh get identity-provider/instances -r demorealm --fields alias,providerId,enabled
Getting a specific configured identity provider
Use the alias
attribute of the identity provider to construct an endpoint URI, such as identity-provider/instances/ALIAS
, to get a specific identity provider.
For example:
$ kcadm.sh get identity-provider/instances/facebook -r demorealm
Removing a specific configured identity provider
Use the delete
command with the same endpoint URI that you used to get a specific configured identity provider to remove a specific configured identity provider.
For example:
$ kcadm.sh delete identity-provider/instances/facebook -r demorealm
Configuring a Keycloak OpenID Connect identity provider
-
Use
keycloak-oidc
as theproviderId
when creating a new identity provider instance. Provide the
config
attributes:authorizationUrl
,tokenUrl
,clientId
, andclientSecret
.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=keycloak-oidc -s providerId=keycloak-oidc -s enabled=true -s 'config.useJwksUrl="true"' -s config.authorizationUrl=http://localhost:8180/auth/realms/demorealm/protocol/openid-connect/auth -s config.tokenUrl=http://localhost:8180/auth/realms/demorealm/protocol/openid-connect/token -s config.clientId=demo-oidc-provider -s config.clientSecret=secret
Configuring an OpenID Connect identity provider
Configure the generic OpenID Connect provider the same way you configure the Keycloak OpenID Connect provider, except that you set the providerId
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
. You can find these attributes in the Facebook Developers application configuration page for your application.For example:
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
. You can find these attributes in the Google Developers application configuration page for your application.For example:
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
. You can find these attributes in the Twitter Application Management application configuration page for your application.For example:
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
. You can find these attributes in the GitHub Developer Application Settings page for your application.For example:
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
. You can find these attributes in the LinkedIn Developer Console application page for your application.For example:
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
. You can find these attributes in the Microsoft Application Registration Portal page for your application.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=microsoft -s providerId=microsoft -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=MICROSOFT_APP_ID -s config.clientSecret=MICROSOFT_PASSWORD
Configuring a StackOverflow identity provider
-
Use
stackoverflow
command as theproviderId
. Provide the
config
attributesclientId
,clientSecret
, andkey
. You can find these attributes in the Stack Apps OAuth page for your application.For example:
$ kcadm.sh create identity-provider/instances -r demorealm -s alias=stackoverflow -s providerId=stackoverflow -s enabled=true -s 'config.useJwksUrl="true"' -s config.clientId=STACKAPPS_CLIENT_ID -s config.clientSecret=STACKAPPS_CLIENT_SECRET -s config.key=STACKAPPS_KEY
19.12. Storage provider operations
Configuring a Kerberos storage provider
-
Use the
create
command against thecomponents
endpoint. -
Specify realm id as a value of the
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
as a value of theproviderId
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
. Add the
action=triggerFullSync
query parameter and run thecreate
command.For example:
$ kcadm.sh create user-storage/b7c63d02-b62a-4fc1-977c-947d6a09e1ea/sync?action=triggerFullSync
Triggering synchronization of changed users for a specific user storage provider
-
Use the storage provider’s
id
attribute to compose an endpoint URI, such asuser-storage/ID_OF_USER_STORAGE_INSTANCE/sync
. Add the
action=triggerChangedUsersSync
query parameter and run thecreate
command.For example:
$ kcadm.sh create user-storage/b7c63d02-b62a-4fc1-977c-947d6a09e1ea/sync?action=triggerChangedUsersSync
Test LDAP user storage connectivity
-
Run the
get
command on thetestLDAPConnection
endpoint. Provide query parameters
bindCredential
,bindDn
,connectionUrl
, anduseTruststoreSpi
, and then set theaction
query parameter totestConnection
.For example:
$ kcadm.sh get testLDAPConnection -q action=testConnection -q bindCredential=secret -q bindDn=uid=admin,ou=system -q connectionUrl=ldap://localhost:10389 -q useTruststoreSpi=ldapsOnly
Test LDAP user storage authentication
-
Run the
get
command on thetestLDAPConnection
endpoint. Provide the query parameters
bindCredential
,bindDn
,connectionUrl
, anduseTruststoreSpi
, and then set theaction
query parameter totestAuthentication
.For example:
$ kcadm.sh get testLDAPConnection -q action=testAuthentication -q bindCredential=secret -q bindDn=uid=admin,ou=system -q connectionUrl=ldap://localhost:10389 -q useTruststoreSpi=ldapsOnly
19.13. Adding mappers
Adding a hardcoded role LDAP mapper
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
. Make sure to provide a value ofrole
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
19.14. Authentication operations
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
- If you want to use values different from defaults, pass the configuration in brackets.
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
Getting the current password policy
Get the current realm configuration and filter everything but the passwordPolicy
attribute.
Use the following example to display passwordPolicy
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
- Get execution for a flow, and take note of its ID
-
Run the
create
command on theauthentication/executions/{executionId}/config
endpoint.
For example:
$ kcadm create "authentication/executions/a3147129-c402-4760-86d9-3f2345e401c7/config" -r examplerealm -b '{"config":{"x509-cert-auth.mapping-source-selection":"Match SubjectDN using regular expression","x509-cert-auth.regular-expression":"(.*?)(?:$)","x509-cert-auth.mapper-selection":"Custom Attribute Mapper","x509-cert-auth.mapper-selection.user-attribute-name":"usercertificate","x509-cert-auth.crl-checking-enabled":"","x509-cert-auth.crldp-checking-enabled":false,"x509-cert-auth.crl-relative-path":"crl.pem","x509-cert-auth.ocsp-checking-enabled":"","x509-cert-auth.ocsp-responder-uri":"","x509-cert-auth.keyusage":"","x509-cert-auth.extendedkeyusage":"","x509-cert-auth.confirmation-page-disallowed":""},"alias":"my_otp_config"}'
Getting configuration for an execution
-
Get execution for a flow, and get its
authenticationConfig
attribute, containing the config ID. -
Run the
get
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm get "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm
Updating configuration for an execution
-
Get execution for a flow, and get its
authenticationConfig
attribute, containing the config ID. -
Run the
update
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm update "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm -b '{"id":"dd91611a-d25c-421a-87e2-227c18421833","alias":"my_otp_config","config":{"x509-cert-auth.extendedkeyusage":"","x509-cert-auth.mapper-selection.user-attribute-name":"usercertificate","x509-cert-auth.ocsp-responder-uri":"","x509-cert-auth.regular-expression":"(.*?)(?:$)","x509-cert-auth.crl-checking-enabled":"true","x509-cert-auth.confirmation-page-disallowed":"","x509-cert-auth.keyusage":"","x509-cert-auth.mapper-selection":"Custom Attribute Mapper","x509-cert-auth.crl-relative-path":"crl.pem","x509-cert-auth.crldp-checking-enabled":"false","x509-cert-auth.mapping-source-selection":"Match SubjectDN using regular expression","x509-cert-auth.ocsp-checking-enabled":""}}'
Deleting configuration for an execution
-
Get execution for a flow, and get its
authenticationConfig
attribute, containing the config ID. -
Run the
delete
command on theauthentication/config/ID
endpoint.
For example:
$ kcadm delete "authentication/config/dd91611a-d25c-421a-87e2-227c18421833" -r examplerealm
