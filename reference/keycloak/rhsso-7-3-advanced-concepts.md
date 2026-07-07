---
title: "Chapter 4. Advanced Concepts - Red Hat Single Sign-On 7.3 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-3-advanced-concepts
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.3/html/red_hat_single_sign-on_for_openshift/advanced_concepts
version: 7.3
family: rhsso
documentKind: "Documentation"
abstract: "These cover additional configuration topics, such as seting up keystores and a truststore for the Red Hat Single Sign-On server, creating an administrator account, an overview of available Red Hat Single Sign-On client registration methods, and guidance on configuring clustering. 4.1. Requirements and Deploying Passthrough TLS Termination Red Hat Single Sign-On Templates 4.1.1. Preparing the Deplo…"
---

# Chapter 4. Advanced Concepts - Red Hat Single Sign-On 7.3 Red Hat Single Sign-On for OpenShift

Chapter 4. Advanced Concepts
These cover additional configuration topics, such as seting up keystores and a truststore for the Red Hat Single Sign-On server, creating an administrator account, an overview of available Red Hat Single Sign-On client registration methods, and guidance on configuring clustering.
4.1. Requirements and Deploying Passthrough TLS Termination Red Hat Single Sign-On Templates
4.1.1. Preparing the Deployment
Log in to the OpenShift CLI with a user that holds the cluster:admin role.
Create a new project:
$ oc new-project sso-app-demo
Add the
view
role to thedefault
service account. This enables the service account to view all the resources in the sso-app-demo namespace, which is necessary for managing the cluster.$ oc policy add-role-to-user view system:serviceaccount:$(oc project -q):default
4.1.2. Creating HTTPS and JGroups Keystores, and Truststore for the Red Hat Single Sign-On Server
The Red Hat Single Sign-On application templates using passthrough TLS termination require:
- An HTTPS keystore used for encryption of https traffic,
- The JGroups keystore used for encryption of JGroups communications between nodes in the cluster, and
- Red Hat Single Sign-On server truststore used for securing the Red Hat Single Sign-On requests
the Red Hat Single Sign-On for OpenShift image to be deployed properly.
The Red Hat Single Sign-On application templates using re-encryption TLS termination do not require or expect the aforementioned HTTPS and JGroups keystores and Red Hat Single Sign-On server truststore to be prepared beforehand. The templates use OpenShift’s internal service serving x509 certificate secrets to automatically create the HTTPS and JGroups keystores. The Red Hat Single Sign-On server truststore is also created automatically, containing the /var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt CA certificate file, which is used to create these cluster certificates. Moreover, the truststore for the Red Hat Single Sign-On server is pre-populated with all the known, trusted CA certificate files found in the Java system path.
The openssl toolkit is used in the following example to generate a CA certificate to sign the HTTPS keystore, and create a truststore for the Red Hat Single Sign-On server. keytool, a package included with the Java Development Kit, is then utilized to the generate self-signed certificates for these keystores.
For production environments Red Hat recommends that you use your own SSL certificate purchased from a verified Certificate Authority (CA) for SSL-encrypted connections (HTTPS).
See the JBoss Enterprise Application Platform Security Guide for more information on how to create a keystore with self-signed or purchased SSL certificates.
Create the HTTPS keystore:
Generate a CA certificate. Pick and remember the password. Provide identical password, when signing the certificate sign request with the CA certificate below:
$ openssl req -new -newkey rsa:4096 -x509 -keyout xpaas.key -out xpaas.crt -days 365 -subj "/CN=xpaas-sso-demo.ca"
Generate a CA certificate for the HTTPS keystore. Provide
mykeystorepass
as the keystore password:$ keytool -genkeypair -keyalg RSA -keysize 2048 -dname "CN=secure-sso-sso-app-demo.openshift.example.com" -alias jboss -keystore keystore.jks
Generate a certificate sign request for the HTTPS keystore. Provide
mykeystorepass
as the keystore password:$ keytool -certreq -keyalg rsa -alias jboss -keystore keystore.jks -file sso.csr
Sign the certificate sign request with the CA certificate. Provide the same password that was used to generate the CA certificate:
$ openssl x509 -req -CA xpaas.crt -CAkey xpaas.key -in sso.csr -out sso.crt -days 365 -CAcreateserial
Import the CA certificate into the HTTPS keystore. Provide
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
4.1.3. Secrets
OpenShift uses objects called secrets to hold sensitive information, such as passwords or keystores.
Create the secrets for the HTTPS and JGroups keystores, and Red Hat Single Sign-On server truststore, generated in the previous section.
$ oc secret new sso-app-secret keystore.jks jgroups.jceks truststore.jks
Link these secrets to the default service account, which is used to run Red Hat Single Sign-On pods.
$ oc secrets link default sso-app-secret
4.1.4. Deploying the Chosen Red Hat Single Sign-On Passthrough TLS Template via OpenShift CLI
After the aforementioned keystores and secrets are created, deploy some of the available passthrough TLS termination as follows:
For simplicity, the values of SSO_ADMIN_USERNAME, SSO_ADMIN_PASSWORD, HTTPS_PASSWORD, JGROUPS_ENCRYPT_PASSWORD, and SSO_TRUSTSTORE_PASSWORD variables in the following command have been chosen to match the default values of the respective parameters of the sso73-https Red Hat Single Sign-On application template.
For production environments, Red Hat recommends that you consult the on-site policy, specific to your organization for guidance on how to generate sufficiently strong user name and password for the administrator user account of the Red Hat Single Sign-On server, and passwords for the HTTPS and JGroups keystores, and the truststore of the Red Hat Single Sign-On server.
Be aware that the passwords provided when provisioning the template need to match the passwords provided when creating the keystores. If using different username and passwords, modify the values of respective template parameters as appropriate for your environment.
The following commands using the keytool, a package included with the Java Development Kit, can be used to determine the names associated with the certificate:
$ keytool -v -list -keystore keystore.jks | grep Alias
Enter keystore password: mykeystorepass
Alias name: xpaas.ca
Alias name: jboss
$ keytool -v -list -keystore jgroups.jceks -storetype jceks | grep Alias
Enter keystore password: password
Alias name: secret-key
Finally, the SSO_ADMIN_USERNAME, SSO_ADMIN_PASSWORD, and the SSO_REALM template parameters in the following command are optional.
$ oc new-app --template=sso73-https \
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
--> Deploying template "openshift/sso73-https" to project sso-app-demo
Red Hat Single Sign-On 7.3.8.GA (Ephemeral with passthrough TLS)
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
4.2. Customizing the Hostname for the Red Hat Single Sign-On Server
The hostname SPI introduced a flexible way to configure the hostname for the Red Hat Single Sign-On server. There are two built-in providers. The first is request
, which uses the request headers to determine the hostname. This is the default setting for Red Hat Single Sign-On for OpenShift image. The second is fixed
, which allows configuring a fixed hostname. The latter makes sure that only valid hostnames can be used and allows internal applications to invoke Red Hat Single Sign-On server through an alternative URL.
Run the following commands to set the fixed
hostname SPI provider for the Red Hat Single Sign-On server:
Deploy the Red Hat Single Sign-On for OpenShift image with SSO_HOSTNAME environment variable set to the desired hostname of the Red Hat Single Sign-On server.
$ oc new-app --template=sso-cd-x509-https \ -p SSO_HOSTNAME="rh-sso-server.openshift.example.com"
Identify the name of the route for the Red Hat Single Sign-On service.
$ oc get routes
Expand NAME HOST/PORT PATH SERVICES PORT TERMINATION WILDCARD sso
sso-sso-app-demo.openshift.example.com
sso
<all>
reencrypt
None
Change the
host:
field to match the hostname specified as the value of the SSO_HOSTNAME environment variable above.NoteAdjust the
rh-sso-server.openshift.example.com
value in the following command as necessary.$ oc patch route/sso --type=json -p '[{"op": "replace", "path": "/spec/host", "value": "rh-sso-server.openshift.example.com"}]'
If successful, the previous command will return the following output:
route "sso" patched
4.2.1. Connecting to an external database
Red Hat Single Sign-On can be configured to connect to an external (to OpenShift cluster) database. In order to achieve this, you need to modify the sso-{database name}
Endpoints object to point to the proper address. The procedure has been described in OpenShift manual.
Tip: The easiest way to get started is to deploy Red Hat Single Sign-On from a template and then modify the Endpoints object. You might also need to update some of the datasource configuration variables in the DeploymentConfig. Once you’re done, just roll a new deployment out.
4.3. Creating the Administrator Account for Red Hat Single Sign-On Server
Red Hat Single Sign-On does not provide any pre-configured management account out of the box. This administrator account is necessary for logging into the master
realm’s management console and perform server maintenance operations such as, creating realms or users, or registering applications intended to be secured by Red Hat Single Sign-On.
The administrator account can be created:
- By providing values for the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters, when deploying the Red Hat Single Sign-On application template, or
- By a remote shell session to particular Red Hat Single Sign-On pod, if the Red Hat Single Sign-On for OpenShift image is deployed without an application template.
Red Hat Single Sign-On allows an initial administrator account to be created via the Welcome Page web form, but only if the Welcome Page is accessed from localhost; this method of administrator account creation is not applicable for the Red Hat Single Sign-On for OpenShift image.
4.3.1. Creating the Administrator Account Using Template Parameters
When deploying Red Hat Single Sign-On application template, the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters denote the username and password of the Red Hat Single Sign-On server’s administrator account to be created for the master
realm.
Both of these parameters are required. If not specified, they are auto generated and displayed as an OpenShift instructional message when the template is instantiated.
The lifespan of the Red Hat Single Sign-On server’s administrator account depends upon the storage type used to store the Red Hat Single Sign-On server’s database:
- For an in-memory database mode (sso73-https and sso73-x509-https templates) the account exists throughout the lifecycle of the particular Red Hat Single Sign-On pod (stored account data is lost upon pod destruction),
- For an ephemeral database mode (sso73-mysql and sso73-postgresql templates) the account exists throughout the lifecycle of the database pod (even if the Red Hat Single Sign-On pod is destructed, the stored account data is preserved under the assumption that the database pod is still running),
- For persistent database mode (sso73-mysql-persistent, sso73-x509-mysql-persistent, sso73-postgresql-persistent, and sso73-x509-postgresql-persistent templates) the account exists throughout the lifecycle of the persistent medium used to hold the database data. This means that the stored account data is preserved even when both the Red Hat Single Sign-On and the database pods are destructed.
It is a common practice to deploy an Red Hat Single Sign-On application template to get the corresponding OpenShift deployment config for the application, and then reuse that deployment config multiple times (every time a new Red Hat Single Sign-On application needs to be instantiated).
In the case of ephemeral or persistent database mode, after creating the RH_SSO server’s administrator account, remove the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables from the deployment config before deploying new Red Hat Single Sign-On applications.
Run the following commands to prepare the previously created deployment config of the Red Hat Single Sign-On application for reuse after the administrator account has been created:
Identify the deployment config of the Red Hat Single Sign-On application.
$ oc get dc -o name deploymentconfig/sso deploymentconfig/sso-mysql
Clear the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables setting.
$ oc set env dc/sso \ -e SSO_ADMIN_USERNAME="" \ -e SSO_ADMIN_PASSWORD=""
4.3.2. Creating the Administrator Account via Remote Shell Session to Red Hat Single Sign-On Pod
Run following commands to create an administrator account for the master
realm of the Red Hat Single Sign-On server, when deploying the Red Hat Single Sign-On for OpenShift image directly from the image stream (without the template), after the Red Hat Single Sign-On application pod has been started:
Identify the Red Hat Single Sign-On application pod.
$ oc get pods NAME READY STATUS RESTARTS AGE sso-12-pt93n 1/1 Running 0 1m sso-mysql-6-d97pf 1/1 Running 0 2m
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
realm’s administration console of the Red Hat Single Sign-On server using the credentials created in the steps above. In the browser, navigate to http://sso-<project-name>.<hostname>/auth/admin for the Red Hat Single Sign-On web server, or to https://secure-sso-<project-name>.<hostname>/auth/admin for the encrypted Red Hat Single Sign-On web server, and specify the user name and password used to create the administrator user.
4.4. Deployment Process
Once deployed, the sso73-https and sso73-x509-https templates create a single pod that contains both the database and the Red Hat Single Sign-On servers. The sso73-mysql, sso73-mysql-persistent, sso73-x509-mysql-persistent, sso73-postgresql, sso73-postgresql-persistent, and sso73-x509-postgresql-persistent templates create two pods, one for the database server and one for the Red Hat Single Sign-On web server.
After the Red Hat Single Sign-On web server pod has started, it can be accessed at its custom configured hostnames, or at the default hostnames:
- http://sso-<project-name>.<hostname>/auth/admin: for the Red Hat Single Sign-On web server, and
- https://secure-sso-<project-name>.<hostname>/auth/admin: for the encrypted Red Hat Single Sign-On web server.
Use the administrator user credentials to log in into the master
realm’s administration console.
4.5. Red Hat Single Sign-On Clients
Clients are Red Hat Single Sign-On entities that request user authentication. A client can be an application requesting Red Hat Single Sign-On to provide user authentication, or it can be making requests for access tokens to start services on behalf of an authenticated user. See the Managing Clients chapter of the Red Hat Single Sign-On documentation for more information.
Red Hat Single Sign-On provides OpenID-Connect and SAML client protocols.
OpenID-Connect is the preferred protocol and utilizes three different access types:
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
4.5.1. Automatic and Manual Red Hat Single Sign-On Client Registration Methods
A client application can be automatically registered to an Red Hat Single Sign-On realm by using credentials passed in variables specific to the eap64-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates.
Alternatively, you can manually register the client application by configuring and exporting the Red Hat Single Sign-On client adapter and including it in the client application configuration.
4.5.1.1. Automatic Red Hat Single Sign-On Client Registration
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
4.5.1.2. Manual Red Hat Single Sign-On Client Registration
Manual Red Hat Single Sign-On client registration is determined by the presence of a deployment file in the client application’s ../configuration/ directory. These files are exported from the client adapter in the Red Hat Single Sign-On web console. The name of this file is different for OpenID-Connect and SAML clients:
| OpenID-Connect | ../configuration/secure-deployments |
| SAML | ../configuration/secure-saml-deployments |
These files are copied to the Red Hat Single Sign-On adapter configuration section in the standalone-openshift.xml at when the application is deployed.
There are two methods for passing the Red Hat Single Sign-On adapter configuration to the client application:
- Modify the deployment file to contain the Red Hat Single Sign-On adapter configuration so that it is included in the standalone-openshift.xml file at deployment, or
- Manually include the OpenID-Connect keycloak.json file, or the SAML keycloak-saml.xml file in the client application’s ../WEB-INF directory.
See Example Workflow: Manually Configure an Application to Use Red Hat Single Sign-On Authentication, Using SAML Client for an end-to-end example of the manual Red Hat Single Sign-On client registration method using a SAML client.
4.6. Limitations
OpenShift does not currently accept OpenShift role mapping from external providers. If Red Hat Single Sign-On is used as an authentication gateway for OpenShift, users created in Red Hat Single Sign-On must have the roles added using the OpenShift Administrator oc adm policy
command.
For example, to allow an Red Hat Single Sign-On-created user to view a project namespace in OpenShift:
$ oc adm policy add-role-to-user view <user-name> -n <project-name>
