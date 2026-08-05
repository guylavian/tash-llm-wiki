---
title: "Chapter 3. Performing advanced procedures - Red Hat Single Sign-On 7.5 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-5-performing-advanced-procedures
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.5/html/red_hat_single_sign-on_for_openshift/performing_advanced_procedures
version: 7.5
family: rhsso
documentKind: "Documentation"
abstract: "This chapter describes advanced procedures, such as setting up keystores and a truststore for the Red Hat Single Sign-On server, creating an administrator account, as well as an overview of available Red Hat Single Sign-On client registration methods, and guidance on configuring clustering. 3.1. Deploying passthrough TLS termination templates You can deploy using these templates. They require HTTP…"
---

# Chapter 3. Performing advanced procedures - Red Hat Single Sign-On 7.5 Red Hat Single Sign-On for OpenShift

Chapter 3. Performing advanced procedures
This chapter describes advanced procedures, such as setting up keystores and a truststore for the Red Hat Single Sign-On server, creating an administrator account, as well as an overview of available Red Hat Single Sign-On client registration methods, and guidance on configuring clustering.
3.1. Deploying passthrough TLS termination templates
You can deploy using these templates. They require HTTPS, JGroups keystores and the Red Hat Single Sign-On server truststore to already exist, and therefore can be used to instantiate the Red Hat Single Sign-On server pod using your custom HTTPS, JGroups keystores and Red Hat Single Sign-On server truststore.
3.1.1. Preparing the deployment
Procedure
- Log in to the OpenShift CLI with a user that holds the cluster:admin role.
Create a new project:
$ oc new-project sso-app-demo
Add the
view
role to thedefault
service account. This enables the service account to view all the resources in the sso-app-demo namespace, which is necessary for managing the cluster.$ oc policy add-role-to-user view system:serviceaccount:$(oc project -q):default
3.1.2. Creating HTTPS and JGroups Keystores, and Truststore for the Red Hat Single Sign-On Server
In this procedure, the openssl toolkit is used to generate a CA certificate to sign the HTTPS keystore, and create a truststore for the Red Hat Single Sign-On server. The keytool, a package included with the Java Development Kit, is then used to generate self-signed certificates for these keystores.
The Red Hat Single Sign-On application templates using re-encryption TLS termination do not require or expect the HTTPS and JGroups keystores and Red Hat Single Sign-On server truststore to be prepared beforehand.
If you want to provision the Red Hat Single Sign-On server using existing HTTPS / JGroups keystores, use some of the passthrough templates instead.
The re-encryption templates use OpenShift’s internal service serving x509 certificate secrets to automatically create the HTTPS and JGroups keystores.
The Red Hat Single Sign-On server truststore is also created automatically, containing the /var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt CA certificate file, which is used to create these cluster certificates. Moreover, the truststore for the Red Hat Single Sign-On server is pre-populated with the all known, trusted CA certificate files found in the Java system path.
Prerequisites
The Red Hat Single Sign-On application templates using passthrough TLS termination require the following to be deployed:
- An HTTPS keystore used for encryption of https traffic,
- The JGroups keystore used for encryption of JGroups communications between nodes in the cluster, and
- Red Hat Single Sign-On server truststore used for securing the Red Hat Single Sign-On requests
For production environments Red Hat recommends that you use your own SSL certificate purchased from a verified Certificate Authority (CA) for SSL-encrypted connections (HTTPS).
See the JBoss Enterprise Application Platform Security Guide for more information on how to create a keystore with self-signed or purchased SSL certificates.
Create the HTTPS keystore:
Procedure
Generate a CA certificate. Pick and remember the password. Provide identical password, when signing the certificate sign request with the CA certificate below:
$ openssl req -new -newkey rsa:4096 -x509 -keyout xpaas.key -out xpaas.crt -days 365 -subj "/CN=xpaas-sso-demo.ca"
Generate a private key for the HTTPS keystore. Provide
mykeystorepass
as the keystore password:$ keytool -genkeypair -keyalg RSA -keysize 2048 -dname "CN=secure-sso-sso-app-demo.openshift.example.com" -alias jboss -keystore keystore.jks
Generate a certificate sign request for the HTTPS keystore. Provide
mykeystorepass
as the keystore password:$ keytool -certreq -keyalg rsa -alias jboss -keystore keystore.jks -file sso.csr
Sign the certificate sign request with the CA certificate. Provide the same password that was used to generate the CA certificate:
$ openssl x509 -req <(printf "subjectAltName=DNS:secure-sso-sso-app-demo.openshift.example.com") -CA xpaas.crt -CAkey xpaas.key -in sso.csr -out sso.crt -days 365 -CAcreateserial
NoteTo make the preceding command work on one line, the command includes the process substitution (
<() syntax
). Be sure that your current shell environment supports such syntax. Otherwise, you can encounter asyntax error near unexpected token `('
message.Import the CA certificate into the HTTPS keystore. Provide
mykeystorepass
as the keystore password. Replyyes
toTrust this certificate? [no]:
question:$ keytool -import -file xpaas.crt -alias xpaas.ca -keystore keystore.jks
Import the signed certificate sign request into the HTTPS keystore. Provide
mykeystorepass
as the keystore password:$ keytool -import -file sso.crt -alias jboss -keystore keystore.jks
Generate a secure key for the JGroups keystore:
Provide password
as the keystore password:
$ keytool -genseckey -alias secret-key -storetype JCEKS -keystore jgroups.jceks
Import the CA certificate into a new Red Hat Single Sign-On server truststore:
Provide mykeystorepass
as the truststore password. Reply yes
to Trust this certificate? [no]:
question:
$ keytool -import -file xpaas.crt -alias xpaas.ca -keystore truststore.jks
3.1.3. Creating secrets
Procedure
You create objects called secrets that OpenShift uses to hold sensitive information, such as passwords or keystores.
Create the secrets for the HTTPS and JGroups keystores, and Red Hat Single Sign-On server truststore, generated in the previous section.
$ oc create secret generic sso-app-secret --from-file=keystore.jks --from-file=jgroups.jceks --from-file=truststore.jks
Link these secrets to the default service account, which is used to run Red Hat Single Sign-On pods.
$ oc secrets link default sso-app-secret
3.1.4. Deploying a Passthrough TLS template using the OpenShift CLI
After you create keystores and secrets, deploy a passthrough TLS termination template by using the oc
command.
3.1.4.1. oc command guidelines
In the following oc
command, the values of SSO_ADMIN_USERNAME, SSO_ADMIN_PASSWORD, HTTPS_PASSWORD, JGROUPS_ENCRYPT_PASSWORD, and SSO_TRUSTSTORE_PASSWORD variables match the default values in the sso75-https Red Hat Single Sign-On application template.
For production environments, Red Hat recommends that you consult the on-site policy for your organization for guidance on generating a strong user name and password for the administrator user account of the Red Hat Single Sign-On server, and passwords for the HTTPS and JGroups keystores, and the truststore of the Red Hat Single Sign-On server.
Also, when you create the template, make the passwords match the passwords provided when you created the keystores. If you used a different username or password, modify the values of the parameters in your template to match your environment.
You can determine the alias names associated with the certificate by using the following keytool commands. The keytool is a package included with the Java Development Kit.
$ keytool -v -list -keystore keystore.jks | grep Alias
Enter keystore password: mykeystorepass
Alias name: xpaas.ca
Alias name: jboss
$ keytool -v -list -keystore jgroups.jceks -storetype jceks | grep Alias
Enter keystore password: password
Alias name: secret-key
The SSO_ADMIN_USERNAME, SSO_ADMIN_PASSWORD, and the SSO_REALM template parameters in the following command are optional.
3.1.4.2. Sample oc command
$ oc new-app --template=sso75-https \
-p HTTPS_SECRET="sso-app-secret" \
-p HTTPS_KEYSTORE="keystore.jks" \
-p HTTPS_NAME="jboss" \
-p HTTPS_PASSWORD="mykeystorepass" \
-p JGROUPS_ENCRYPT_SECRET="sso-app-secret" \
-p JGROUPS_ENCRYPT_KEYSTORE="jgroups.jceks" \
-p JGROUPS_ENCRYPT_NAME="secret-key" \
-p JGROUPS_ENCRYPT_PASSWORD="password" \
-p SSO_ADMIN_USERNAME="admin" \
-p SSO_ADMIN_PASSWORD="redhat" \
-p SSO_REALM="demorealm" \
-p SSO_TRUSTSTORE="truststore.jks" \
-p SSO_TRUSTSTORE_PASSWORD="mykeystorepass" \
-p SSO_TRUSTSTORE_SECRET="sso-app-secret"
--> Deploying template "openshift/sso75-https" to project sso-app-demo
Red Hat Single Sign-On 7.5.3 (Ephemeral with passthrough TLS)
---------
An example Red Hat Single Sign-On 7 application. For more information about using this template, see https://github.com/jboss-openshift/application-templates.
A new Red Hat Single Sign-On service has been created in your project. The admin username/password for accessing the master realm via the Red Hat Single Sign-On console is admin/redhat. Please be sure to create the following secrets: "sso-app-secret" containing the keystore.jks file used for serving secure content; "sso-app-secret" containing the jgroups.jceks file used for securing JGroups communications; "sso-app-secret" containing the truststore.jks file used for securing Red Hat Single Sign-On requests.
* With parameters:
* Application Name=sso
* Custom http Route Hostname=
* Custom https Route Hostname=
* Server Keystore Secret Name=sso-app-secret
* Server Keystore Filename=keystore.jks
* Server Keystore Type=
* Server Certificate Name=jboss
* Server Keystore Password=mykeystorepass
* Datasource Minimum Pool Size=
* Datasource Maximum Pool Size=
* Datasource Transaction Isolation=
* JGroups Secret Name=sso-app-secret
* JGroups Keystore Filename=jgroups.jceks
* JGroups Certificate Name=secret-key
* JGroups Keystore Password=password
* JGroups Cluster Password=yeSppLfp # generated
* ImageStream Namespace=openshift
* Red Hat Single Sign-On Administrator Username=admin
* Red Hat Single Sign-On Administrator Password=redhat
* Red Hat Single Sign-On Realm=demorealm
* Red Hat Single Sign-On Service Username=
* Red Hat Single Sign-On Service Password=
* Red Hat Single Sign-On Trust Store=truststore.jks
* Red Hat Single Sign-On Trust Store Password=mykeystorepass
* Red Hat Single Sign-On Trust Store Secret=sso-app-secret
* Container Memory Limit=1Gi
--> Creating resources ...
service "sso" created
service "secure-sso" created
service "sso-ping" created
route "sso" created
route "secure-sso" created
deploymentconfig "sso" created
--> Success
Run 'oc status' to view your app.
3.2. Customizing the Hostname for the Red Hat Single Sign-On Server
The hostname SPI introduced a flexible way to configure the hostname for the Red Hat Single Sign-On server. The default hostname provider one is default
. This provider provides enhanced functionality over the original request
provider which is now deprecated. Without additional settings, it uses the request headers to determine the hostname similarly to the original request
provider.
For configuration options of the default
provider, refer to the Server Installation and Configuration Guide. The frontendUrl
option can be configured via SSO_FRONTEND_URL
environment variable.
For backward compatibility, SSO_FRONTEND_URL
settings is ignored if SSO_HOSTNAME
is also set.
Another option of hostname provider is fixed
, which allows configuring a fixed hostname. The latter makes sure that only valid hostnames can be used and allows internal applications to invoke the Red Hat Single Sign-On server through an alternative URL.
Procedure
Run the following commands to set the fixed
hostname SPI provider for the Red Hat Single Sign-On server:
Deploy the Red Hat Single Sign-On for OpenShift image with SSO_HOSTNAME environment variable set to the desired hostname of the Red Hat Single Sign-On server.
$ oc new-app --template=sso75-x509-https \ -p SSO_HOSTNAME="rh-sso-server.openshift.example.com"
Identify the name of the route for the Red Hat Single Sign-On service.
$ oc get routes NAME HOST/PORT sso sso-sso-app-demo.openshift.example.com
Change the
host:
field to match the hostname specified as the value of the SSO_HOSTNAME environment variable above.NoteAdjust the
rh-sso-server.openshift.example.com
value in the following command as necessary.$ oc patch route/sso --type=json -p '[{"op": "replace", "path": "/spec/host", "value": "rh-sso-server.openshift.example.com"}]'
If successful, the previous command will return the following output:
route "sso" patched
3.3. Connecting to an external database
Red Hat Single Sign-On can be configured to connect to an external (to OpenShift cluster) database. In order to achieve this, you need to modify the sso-{database name}
Endpoints object to point to the proper address. The procedure is described in the OpenShift manual.
The easiest way to get started is to deploy Red Hat Single Sign-On from a template and then modify the Endpoints object. You might also need to update some of the datasource configuration variables in the DeploymentConfig. Once you’re done, just roll a new deployment out.
3.4. Using Custom JDBC Driver
To connect to any database, the JDBC driver for that database must be present and Red Hat Single Sign-On configured properly. Currently, the only JDBC driver available in the image is the PostgreSQL JDBC driver. For any other database, you need to extend the Red Hat Single Sign-On image with a custom JDBC driver and a CLI script to register it and set up the connection properties. The following steps illustrate how to do that, taking MariaDB driver as an example. Update the example for other database drivers accordingly.
Procedure
- Create an empty directory.
- Download the JDBC driver binaries into this directory.
Create a new
Dockerfile
file in this directory with the following contents. For other databases, replacemariadb-java-client-2.5.4.jar
with the filename of the respective driver:FROM rh-sso-7/sso75-openshift-rhel8:latest COPY sso-extensions.cli /opt/eap/extensions/ COPY mariadb-java-client-2.5.4.jar /opt/eap/extensions/jdbc-driver.jar
Create a new
sso-extensions.cli
file in this directory with the following contents. Update the values of the variables in italics according to the deployment needs:batch set DB_DRIVER_NAME=mariadb set DB_USERNAME=username set DB_PASSWORD=password set DB_DRIVER=org.mariadb.jdbc.Driver set DB_XA_DRIVER=org.mariadb.jdbc.MariaDbDataSource set DB_JDBC_URL=jdbc:mariadb://jdbc-host/keycloak set DB_EAP_MODULE=org.mariadb set FILE=/opt/eap/extensions/jdbc-driver.jar module add --name=$DB_EAP_MODULE --resources=$FILE --dependencies=javax.api,javax.resource.api /subsystem=datasources/jdbc-driver=$DB_DRIVER_NAME:add( \ driver-name=$DB_DRIVER_NAME, \ driver-module-name=$DB_EAP_MODULE, \ driver-class-name=$DB_DRIVER, \ driver-xa-datasource-class-name=$DB_XA_DRIVER \ ) /subsystem=datasources/data-source=KeycloakDS:remove() /subsystem=datasources/data-source=KeycloakDS:add( \ jndi-name=java:jboss/datasources/KeycloakDS, \ enabled=true, \ use-java-context=true, \ connection-url=$DB_JDBC_URL, \ driver-name=$DB_DRIVER_NAME, \ user-name=$DB_USERNAME, \ password=$DB_PASSWORD \ ) run-batch
In this directory, build your image by typing the following command, replacing the
project/name:tag
with arbitrary name.docker
can be used instead ofpodman
.$ podman build -t docker-registry-default/project/name:tag .
- After the build finishes, push your image to the registry used by OpenShift to deploy your image. Refer to the OpenShift guide for details.
If you want to use this image with the custom JDBC driver that you built in the previous step with the existing Red Hat Single Sign-On OpenShift DeploymentConfig that was previously created by some Red Hat Single Sign-On OpenShift template, you need to patch the DeploymentConfig definition. Enter the following command:
$ oc patch dc/sso --type=json -p '[{"op": "replace", "path": "/spec/triggers/0/imageChangeParams/from/name", "value": "sso75-openshift-rhel8-image-with-custom-jdbc-driver:latest"}]' "sso" patched
This command assumes the image stream name and tag combination of the Red Hat Single Sign-On image with the custom JDBC driver is "sso75-openshift-rhel8-image-with-custom-jdbc-driver:latest."
3.5. Creating the Administrator Account for Red Hat Single Sign-On Server
Red Hat Single Sign-On does not provide any pre-configured management account out of the box. This administrator account is necessary for logging into the master
realm’s management console and performing server maintenance operations such as creating realms or users or registering applications intended to be secured by Red Hat Single Sign-On.
The administrator account can be created:
- By providing values for the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters, when deploying the Red Hat Single Sign-On application template, or
- By a remote shell session to particular Red Hat Single Sign-On pod, if the Red Hat Single Sign-On for OpenShift image is deployed without an application template.
Red Hat Single Sign-On allows an initial administrator account to be created by the Welcome Page web form, but only if the Welcome Page is accessed from localhost; this method of administrator account creation is not applicable for the Red Hat Single Sign-On for OpenShift image.
3.5.1. Creating the Administrator Account using template parameters
When deploying Red Hat Single Sign-On application template, the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters denote the username and password of the Red Hat Single Sign-On server’s administrator account to be created for the master
realm.
Both of these parameters are required. If not specified, they are auto generated and displayed as an OpenShift instructional message when the template is instantiated.
The lifespan of the Red Hat Single Sign-On server’s administrator account depends upon the storage type used to store the Red Hat Single Sign-On server’s database:
- For an in-memory database mode (sso75-https and sso75-x509-https templates), the account exists throughout the lifecycle of the particular Red Hat Single Sign-On pod (stored account data is lost upon pod destruction),
- For an ephemeral database mode sso75-postgresql templates), the account exists throughout the lifecycle of the database pod. Even if the Red Hat Single Sign-On pod is destructed, the stored account data is preserved under the assumption that the database pod is still running,
- For persistent database mode (sso75-postgresql-persistent, and sso75-x509-postgresql-persistent templates), the account exists throughout the lifecycle of the persistent medium used to hold the database data. This means that the stored account data is preserved even when both the Red Hat Single Sign-On and the database pods are destructed.
It is a common practice to deploy an Red Hat Single Sign-On application template to get the corresponding OpenShift deployment config for the application, and then reuse that deployment config multiple times (every time a new Red Hat Single Sign-On application needs to be instantiated).
In the case of ephemeral or persistent database mode, after creating the RH_SSO server’s administrator account, remove the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables from the deployment config before deploying new Red Hat Single Sign-On applications.
Procedure
Run the following commands to prepare the previously created deployment config of the Red Hat Single Sign-On application for reuse after the administrator account has been created:
Identify the deployment config of the Red Hat Single Sign-On application.
$ oc get dc -o name deploymentconfig/sso deploymentconfig/sso-postgresql
Clear the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables setting.
$ oc set env dc/sso \ -e SSO_ADMIN_USERNAME="" \ -e SSO_ADMIN_PASSWORD=""
3.5.2. Creating the Administrator Account via a remote shell session to Red Hat Single Sign-On Pod
You use the following commands to create an administrator account for the master
realm of the Red Hat Single Sign-On server, when deploying the Red Hat Single Sign-On for OpenShift image directly from the image stream without using a template.
Prerequisite
- Red Hat Single Sign-On application pod has been started.
Procedure
Identify the Red Hat Single Sign-On application pod.
$ oc get pods NAME READY STATUS RESTARTS AGE sso-12-pt93n 1/1 Running 0 1m sso-postgresql-6-d97pf 1/1 Running 0 2m
Open a remote shell session to the Red Hat Single Sign-On for OpenShift container.
$ oc rsh sso-12-pt93n sh-4.2$
Create the Red Hat Single Sign-On server administrator account for the
master
realm at the command line with theadd-user-keycloak.sh
script.sh-4.2$ cd /opt/eap/bin/ sh-4.2$ ./add-user-keycloak.sh \ -r master \ -u sso_admin \ -p sso_password Added 'sso_admin' to '/opt/eap/standalone/configuration/keycloak-add-user.json', restart server to load user
NoteThe 'sso_admin' / 'sso_password' credentials in the example above are for demonstration purposes only. Refer to the password policy applicable within your organization for guidance on how to create a secure user name and password.
Restart the underlying JBoss EAP server instance to load the newly added user account. Wait for the server to restart properly.
sh-4.2$ ./jboss-cli.sh --connect ':reload' { "outcome" => "success", "result" => undefined }
WarningWhen restarting the server it is important to restart just the JBoss EAP process within the running Red Hat Single Sign-On container, and not the whole container. This is because restarting the whole container will recreate it from scratch, without the Red Hat Single Sign-On server administration account for the
master
realm.-
Log in to the
master
realm’s Admin Console of the Red Hat Single Sign-On server using the credentials created in the steps above. In the browser, navigate to http://sso-<project-name>.<hostname>/auth/admin for the Red Hat Single Sign-On web server, or to https://secure-sso-<project-name>.<hostname>/auth/admin for the encrypted Red Hat Single Sign-On web server, and specify the user name and password used to create the administrator user.
3.6. Customizing the default behavior of the Red Hat Single Sign-On image
You can change the default behavior of the Red Hat Single Sign-On image such as enabling TechPreview features or enabling debugging. This section describes how to make this change by using the JAVA_OPTS_APPEND variable.
Prerequisites
This procedure assumes that the Red Hat Single Sign-On for OpenShift image has been previously deployed using one of the following templates:
- sso75-postgresql
- sso75-postgresql-persistent
- sso75-x509-postgresql-persistent
Procedure
You can use the OpenShift web console or the CLI to change the default behavior.
If you use the OpenShift web console, you add the JAVA_OPTS_APPEND variable to the sso deployment config. For example, to enable TechPreview features, you set the variable as follows:
JAVA_OPTS_APPEND="-Dkeycloak.profile=preview"
If you use the CLI, use the following commands to enable TechPreview features when the Red Hat Single Sign-On pod was deployed using a template that is mentioned under Prerequisites.
Scale down the Red Hat Single Sign-On pod:
$ oc get dc -o name deploymentconfig/sso deploymentconfig/sso-postgresql $ oc scale --replicas=0 dc sso deploymentconfig "sso" scaled
NoteIn the preceding command,
sso-postgresql
appears because a PostgreSQL template was used to deploy the Red Hat Single Sign-On for OpenShift image.Edit the deployment config to set the JAVA_OPTS_APPEND variable. For example, to enable TechPreview features, you set the variable as follows:
$ oc env dc/sso -e "JAVA_OPTS_APPEND=-Dkeycloak.profile=preview"
Scale up the Red Hat Single Sign-On pod:
$ oc scale --replicas=1 dc sso deploymentconfig "sso" scaled
- Test a TechPreview feature of your choice.
3.7. Deployment process
Once deployed, the sso75-https and sso75-x509-https templates create a single pod that contains both the database and the Red Hat Single Sign-On servers. The sso75-postgresql, sso75-postgresql-persistent, and sso75-x509-postgresql-persistent templates create two pods, one for the database server and one for the Red Hat Single Sign-On web server.
After the Red Hat Single Sign-On web server pod has started, it can be accessed at its custom configured hostnames, or at the default hostnames:
- http://sso-<project-name>.<hostname>/auth/admin: for the Red Hat Single Sign-On web server, and
- https://secure-sso-<project-name>.<hostname>/auth/admin: for the encrypted Red Hat Single Sign-On web server.
Use the administrator user credentials to log in into the master
realm’s Admin Console.
3.8. Red Hat Single Sign-On clients
Clients are Red Hat Single Sign-On entities that request user authentication. A client can be an application requesting Red Hat Single Sign-On to provide user authentication, or it can be making requests for access tokens to start services on behalf of an authenticated user. See the Managing Clients chapter of the Red Hat Single Sign-On documentation for more information.
Red Hat Single Sign-On provides OpenID-Connect and SAML client protocols.
OpenID-Connect is the preferred protocol and uses three different access types:
- public: Useful for JavaScript applications that run directly in the browser and require no server configuration.
- confidential: Useful for server-side clients, such as EAP web applications, that need to perform a browser login.
- bearer-only: Useful for back-end services that allow bearer token requests.
It is required to specify the client type in the <auth-method> key of the application web.xml file. This file is read by the image at deployment. Set the value of <auth-method> element to:
- KEYCLOAK for the OpenID Connect client.
- KEYCLOAK-SAML for the SAML client.
The following is an example snippet for the application web.xml to configure an OIDC client:
...
<login-config>
<auth-method>KEYCLOAK</auth-method>
</login-config>
...
3.8.1. Automatic and manual Red Hat Single Sign-On client registration methods
A client application can be automatically registered to an Red Hat Single Sign-On realm by using credentials passed in variables specific to the eap64-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates.
Alternatively, you can manually register the client application by configuring and exporting the Red Hat Single Sign-On client adapter and including it in the client application configuration.
3.8.1.1. Automatic Red Hat Single Sign-On client registration
Automatic Red Hat Single Sign-On client registration is determined by Red Hat Single Sign-On environment variables specific to the eap64-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates. The Red Hat Single Sign-On credentials supplied in the template are then used to register the client to the Red Hat Single Sign-On realm during deployment of the client application.
The Red Hat Single Sign-On environment variables included in the eap64-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates are:
| Variable | Description |
|---|---|
| HOSTNAME_HTTP | Custom hostname for http service route. Leave blank for default hostname of <application-name>.<project>.<default-domain-suffix> |
| HOSTNAME_HTTPS | Custom hostname for https service route. Leave blank for default hostname of <application-name>.<project>.<default-domain-suffix> |
| SSO_URL | The Red Hat Single Sign-On web server authentication address: https://secure-sso-<project-name>.<hostname>/auth |
| SSO_REALM | The Red Hat Single Sign-On realm created for this procedure. |
| SSO_USERNAME | The name of the realm management user. |
| SSO_PASSWORD | The password of the user. |
| SSO_PUBLIC_KEY | The public key generated by the realm. It is located in the Keys tab of the Realm Settings in the Red Hat Single Sign-On console. |
| SSO_BEARER_ONLY | If set to true, the OpenID Connect client is registered as bearer-only. |
| SSO_ENABLE_CORS | If set to true, the Red Hat Single Sign-On adapter enables Cross-Origin Resource Sharing (CORS). |
If the Red Hat Single Sign-On client uses the SAML protocol, the following additional variables need to be configured:
| Variable | Description |
|---|---|
| SSO_SAML_KEYSTORE_SECRET | Secret to use for access to SAML keystore. The default is sso-app-secret. |
| SSO_SAML_KEYSTORE | Keystore filename in the SAML keystore secret. The default is keystore.jks. |
| SSO_SAML_KEYSTORE_PASSWORD | Keystore password for SAML. The default is mykeystorepass. |
| SSO_SAML_CERTIFICATE_NAME | Alias for keys/certificate to use for SAML. The default is jboss. |
See Example Workflow: Automatically Registering EAP Application in Red Hat Single Sign-On with OpenID-Connect Client for an end-to-end example of the automatic client registration method using an OpenID-Connect client.
3.8.1.2. Manual Red Hat Single Sign-On client registration
Manual Red Hat Single Sign-On client registration is determined by the presence of a deployment file in the client application’s ../configuration/ directory. These files are exported from the client adapter in the Red Hat Single Sign-On web console. The name of this file is different for OpenID-Connect and SAML clients:
| OpenID-Connect | ../configuration/secure-deployments |
| SAML | ../configuration/secure-saml-deployments |
These files are copied to the Red Hat Single Sign-On adapter configuration section in the standalone-openshift.xml at when the application is deployed.
There are two methods for passing the Red Hat Single Sign-On adapter configuration to the client application:
- Modify the deployment file to contain the Red Hat Single Sign-On adapter configuration so that it is included in the standalone-openshift.xml file at deployment, or
- Manually include the OpenID-Connect keycloak.json file, or the SAML keycloak-saml.xml file in the client application’s ../WEB-INF directory.
See Example Workflow: Manually Configure an Application to Use Red Hat Single Sign-On Authentication, Using SAML Client for an end-to-end example of the manual Red Hat Single Sign-On client registration method using a SAML client.
3.9. Using Red Hat Single Sign-On vault with OpenShift secrets
Several fields in the Red Hat Single Sign-On administration support obtaining the value of a secret from an external vault, see Server Administration Guide. The following example shows how to set up the file-based plaintext vault in OpenShift and set it up to be used for obtaining an SMTP password.
Procedure
Specify a directory for the vault using the SSO_VAULT_DIR environment variable. You can introduce the SSO_VAULT_DIR environment variable directly in the environment in your deployment configuration. It can also be included in the template by addding the following snippets at the appropriate places in the template:
"parameters": [ ... { "displayName": "RH-SSO Vault Secret directory", "description": "Path to the RH-SSO Vault directory.", "name": "SSO_VAULT_DIR", "value": "", "required": false } ... ] env: [ ... { "name": "SSO_VAULT_DIR", "value": "${SSO_VAULT_DIR}" } ... ]
NoteThe files plaintext vault provider will be configured only when you set SSO_VAULT_DIR environment variable.
Create a secret in your OpenShift cluster:
$ oc create secret generic rhsso-vault-secrets --from-literal=master_smtp-password=mySMTPPsswd
Mount a volume to your deployment config using the
${SSO_VAULT_DIR}
as the path. For a deployment that is already running:$ oc set volume dc/sso --add --mount-path=${SSO_VAULT_DIR} --secret-name=rhsso-vault-secrets
-
After a pod is created you can use a customized string within your Red Hat Single Sign-On configuration to refer to the secret. For example, for using
mySMTPPsswd
secret created in this tutorial, you can use${vault.smtp-password}
within themaster
realm in the configuration of the smtp password and it will be replaced bymySMTPPsswd
when used.
3.10. Limitations
OpenShift does not currently accept OpenShift role mapping from external providers. If Red Hat Single Sign-On is used as an authentication gateway for OpenShift, users created in Red Hat Single Sign-On must have the roles added using the OpenShift Administrator oc adm policy
command.
For example, to allow an Red Hat Single Sign-On-created user to view a project namespace in OpenShift:
$ oc adm policy add-role-to-user view <user-name> -n <project-name>
