---
title: "Chapter 4. Advanced Concepts - Red Hat Single Sign-On 7.2 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-2-advanced-concepts
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/red_hat_single_sign-on_for_openshift/advanced_concepts
version: 7.2
family: rhsso
documentKind: "Documentation"
abstract: "These cover additional configuration topics, such as seting up keystores and a truststore for the RH-SSO server, creating an administrator account, an overview of available RH-SSO client registration methods, and guidance on configuring clustering. 4.1. Requirements and Deploying Passthrough TLS Termination RH-SSO Templates 4.1.1. Preparing the Deployment Log in to the OpenShift CLI with a user th…"
---

# Chapter 4. Advanced Concepts - Red Hat Single Sign-On 7.2 Red Hat Single Sign-On for OpenShift

Chapter 4. Advanced Concepts
These cover additional configuration topics, such as seting up keystores and a truststore for the RH-SSO server, creating an administrator account, an overview of available RH-SSO client registration methods, and guidance on configuring clustering.
4.1. Requirements and Deploying Passthrough TLS Termination RH-SSO Templates
4.1.1. Preparing the Deployment
Log in to the OpenShift CLI with a user that holds the cluster:admin role.
Create a new project:
$ oc new-project sso-app-demo
Add the
view
role to thedefault
service account. This enables the service account to view all the resources in the sso-app-demo namespace, which is necessary for managing the cluster.$ oc policy add-role-to-user view system:serviceaccount:$(oc project -q):default
4.1.2. Creating HTTPS and JGroups Keystores, and Truststore for the RH-SSO Server
The RH-SSO application templates using passthrough TLS termination require:
- An HTTPS keystore used for encryption of https traffic,
- The JGroups keystore used for encryption of JGroups communications between nodes in the cluster, and
- RH-SSO server truststore used for securing the RH-SSO requests
the RH-SSO for OpenShift image to be deployed properly.
The RH-SSO application templates using re-encryption TLS termination do not require or expect the aforementioned HTTPS and JGroups keystores and RH-SSO server truststore to be prepared beforehand. The templates use OpenShift’s internal service serving x509 certificate secrets to automatically create the HTTPS and JGroups keystores. The RH-SSO server truststore is also created automatically, containing the /var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt CA certificate file, which is used to create these cluster certificates. Moreover, the truststore for the RH-SSO server is pre-populated with the all known, trusted CA certificate files found in the Java system path.
The openssl toolkit is used in the following example to generate a CA certificate to sign the HTTPS keystore, and create a truststore for the RH-SSO server. keytool, a package included with the Java Development Kit, is then utilized to the generate self-signed certificates for these keystores.
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
Import the CA certificate into a new RH-SSO server truststore:
Provide mykeystorepass
as the truststore password. Reply yes
to Trust this certificate? [no]:
question:
$ keytool -import -file xpaas.crt -alias xpaas.ca -keystore truststore.jks
4.1.3. Secrets
OpenShift uses objects called secrets to hold sensitive information, such as passwords or keystores.
Create the secrets for the HTTPS and JGroups keystores, and RH-SSO server truststore, generated in the previous section.
$ oc secret new sso-app-secret keystore.jks jgroups.jceks truststore.jks
Link these secrets to the default service account, which is used to run RH-SSO pods.
$ oc secrets link default sso-app-secret
4.1.4. Deploying the Chosen RH-SSO Passthrough TLS Template via OpenShift CLI
After the aforementioned keystores and secrets are created, deploy some of the available passthrough TLS termination as follows:
For simplicity, the values of SSO_ADMIN_USERNAME, SSO_ADMIN_PASSWORD, HTTPS_PASSWORD, JGROUPS_ENCRYPT_PASSWORD, and SSO_TRUSTSTORE_PASSWORD variables in the following command have been chosen to match the default values of the respective parameters of the sso72-https RH-SSO application template.
For production environments, Red Hat recommends that you consult the on-site policy, specific to your organization for guidance on how to generate sufficiently strong user name and password for the administrator user account of the RH-SSO server, and passwords for the HTTPS and JGroups keystores, and the truststore of the RH-SSO server.
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
$ oc new-app --template=sso72-https \
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
--> Deploying template "openshift/sso72-https" to project sso-app-demo
Red Hat Single Sign-On 7.2 (Ephemeral with passthrough TLS)
---------
An example RH-SSO 7 application. For more information about using this template, see https://github.com/jboss-openshift/application-templates.
A new RH-SSO service has been created in your project. The admin username/password for accessing the master realm via the RH-SSO console is admin/redhat. Please be sure to create the following secrets: "sso-app-secret" containing the keystore.jks file used for serving secure content; "sso-app-secret" containing the jgroups.jceks file used for securing JGroups communications; "sso-app-secret" containing the truststore.jks file used for securing RH-SSO requests.
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
* RH-SSO Administrator Username=admin
* RH-SSO Administrator Password=redhat
* RH-SSO Realm=demorealm
* RH-SSO Service Username=
* RH-SSO Service Password=
* RH-SSO Trust Store=truststore.jks
* RH-SSO Trust Store Password=mykeystorepass
* RH-SSO Trust Store Secret=sso-app-secret
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
4.1.5. Accessing the Administrator Console of the RH-SSO Pod
After the template got deployed, identify the available routes:
$ oc get routes
| NAME | HOST/PORT | PATH | SERVICES | PORT | TERMINATION | WILDCARD |
|---|---|---|---|---|---|---|
| secure-sso | secure-sso-sso-app-demo.openshift.example.com | secure-sso | <all> | passthrough | None | |
| sso | sso-sso-app-demo.openshift.example.com | sso | <all> | None |
and access the RH-SSO administrator console at:
- https://secure-sso-sso-app-demo.openshift.example.com/auth/admin
- http://sso-sso-app-demo.openshift.example.com/auth/admin
using the administrator account.
4.2. Creating Administrator Account for Red Hat Single Sign-On Server
Red Hat Single Sign-On does not provide any pre-configured management account out of the box. This administrator account is necessary for logging into the master
realm’s management console and perform server maintenance operations such as, creating realms or users, or registering applications intended to be secured by Red Hat Single Sign-On.
The administrator account can be created:
- By providing values for the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters, when deploying the RH-SSO application template, or
- By a remote shell session to particular RH-SSO pod, if the RH-SSO for OpenShift image is deployed without an application template.
Red Hat Single Sign-On allows an initial administrator account to be created via the Welcome Page web form, but only if the Welcome Page is accessed from localhost; this method of administrator account creation is not applicable for the RH-SSO for OpenShift image.
4.2.1. Creating RH-SSO Administrator Account via Template Parameters
When deploying RH-SSO application template, SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD parameters denote the username and password of the RH-SSO server’s administrator account to be created for the master
realm.
Both of these parameters are required. If not specified, they are auto generated and displayed as an OpenShift instructional message when the template is instantiated.
The lifespan of the RH-SSO server’s administrator account depends upon the the storage type used to store the RH-SSO server’s database:
- For an in-memory database mode (sso72-https and sso72-x509-https templates) the account exists throughout the lifecycle of the particular RH-SSO pod (stored account data is lost upon pod destruction),
- For an ephemeral database mode (sso72-mysql and sso72-postgresql templates) the account exists throughout the lifecycle of the database pod (even if the RH-SSO pod is destructed, the stored account data is preserved under the assumption that the database pod is still running),
- For persistent database mode (sso72-mysql-persistent, sso72-x509-mysql-persistent, sso72-postgresql-persistent, and sso72-x509-postgresql-persistent templates) the account exists throughout the lifecycle of the persistent medium used to hold the database data. This means that the stored account data is preserved even when both the RH-SSO and the database pods are destructed.
It is a common practice to deploy an RH-SSO application template to get the corresponding OpenShift deployment config for the application, and then reuse that deployment config multiple times (every time a new RH-SSO application needs to be instantiated).
In the case of ephemeral or persistent database mode, after creating the RH_SSO server’s administrator account, remove the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables from the deployment config before deploying new RH-SSO applications.
Run the following commands to prepare the previously created deployment config of the RH-SSO application for reuse after the administrator account has been created:
Identify the deployment config of the RH-SSO application.
$ oc get dc -o name deploymentconfig/sso deploymentconfig/sso-mysql
Clear the SSO_ADMIN_USERNAME and SSO_ADMIN_PASSWORD variables setting.
$ oc env dc/sso -e SSO_ADMIN_USERNAME="" SSO_ADMIN_PASSWORD=""
4.2.2. Creating RH-SSO Administrator Account via Remote Shell Session to RH-SSO Pod
Run following commands to create an administrator account for the master
realm of the RH-SSO server, when deploying the RH-SSO for OpenShift image directly from the image stream (without the template), after the RH-SSO application pod has been started:
Identify the RH-SSO application pod.
$ oc get pods NAME READY STATUS RESTARTS AGE sso-12-pt93n 1/1 Running 0 1m sso-mysql-6-d97pf 1/1 Running 0 2m
Open a remote shell session to the RH-SSO for OpenShift container.
$ oc rsh sso-12-pt93n sh-4.2$
Create the RH-SSO server administrator account for the
master
realm at the command line with theadd-user-keycloak.sh
script.sh-4.2$ cd /opt/eap/bin/ sh-4.2$ ./add-user-keycloak.sh -r master -u sso_admin -p sso_password Added 'sso_admin' to '/opt/eap/standalone/configuration/keycloak-add-user.json', restart server to load user
NoteThe
sso_admin
/sso_password
credentials in the example above are for demonstration purposes only. Refer to the password policy applicable within your organization for guidance on how to create a secure user name and password.Restart the underlying JBoss EAP server instance to load the newly added user account. Wait for the server to restart properly.
sh-4.2$ ./jboss-cli.sh --connect ':reload' { "outcome" => "success", "result" => undefined }
WarningWhen restarting the server it is important to restart just the JBoss EAP process within the running RH-SSO container, and not the whole container. This is because restarting the whole container will recreate it from scratch, without the RH-SSO server administration account for the
master
realm.-
Log in to the
master
realm’s administration console of the RH-SSO server using the the credentials created in the steps above. In the browser, navigate to http://sso-<project-name>.<hostname>/auth/admin for the RH-SSO web server, or to https://secure-sso-<project-name>.<hostname>/auth/admin for the encrypted RH-SSO web server, and specify the user name and password used to create the administrator user.
4.3. Deployment Process
Once deployed, the sso72-https and sso72-x509-https templates create a single pod that contains both the database and the RH-SSO servers. The sso72-mysql, sso72-mysql-persistent, sso72-x509-mysql-persistent, sso72-postgresql, sso72-postgresql-persistent, and sso72-x509-postgresql-persistent templates create two pods, one for the database server and one for the RH-SSO web server.
After the RH-SSO web server pod has started, it can be accessed from its custom configured hostnames, or from the default hostnames:
- http://sso-<project-name>.<hostname>/auth/admin: for the RH-SSO web server, and
- https://secure-sso-<project-name>.<hostname>/auth/admin: for the encrypted RH-SSO web server.
Use the administrator user credentials to log in into the master
realm’s administration console.
4.4. RH-SSO Clients
Clients are RH-SSO entities that request user authentication. A client can be an application requesting RH-SSO to provide user authentication, or it can make requests for access tokens to start services on behalf of an authenticated user. See the Managing Clients chapter of the Red Hat Single Sign-On documentation for more information.
RH-SSO provides OpenID-Connect and SAML client protocols.
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
4.4.1. Automatic and Manual RH-SSO Client Registration Methods
A client application can be automatically registered to an RH-SSO realm by using credentials passed in variables specific to the eap64-sso-s2i, eap70-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates.
Alternatively, you can manually register the client application by configuring and exporting the RH-SSO client adapter and including it in the client application configuration.
4.4.1.1. Automatic RH-SSO Client Registration
Automatic RH-SSO client registration is determined by RH-SSO environment variables specific to the eap64-sso-s2i, eap70-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates. The RH-SSO credentials supplied in the template are then used to register the client to the RH-SSO realm during deployment of the client application.
The RH-SSO environment variables included in the eap64-sso-s2i, eap70-sso-s2i, eap71-sso-s2i, and datavirt63-secure-s2i templates are:
| Variable | Description |
|---|---|
| HOSTNAME_HTTP | Custom hostname for http service route. Leave blank for default hostname of <application-name>.<project>.<default-domain-suffix> |
| HOSTNAME_HTTPS | Custom hostname for https service route. Leave blank for default hostname of <application-name>.<project>.<default-domain-suffix> |
| SSO_URL | The RH-SSO web server authentication address: https://secure-sso-<project-name>.<hostname>/auth |
| SSO_REALM | The RH-SSO realm created for this procedure. |
| SSO_USERNAME | The name of the realm management user. |
| SSO_PASSWORD | The password of the user. |
| SSO_PUBLIC_KEY | The public key generated by the realm. It is located in the Keys tab of the Realm Settings in the RH-SSO console. |
| SSO_BEARER_ONLY | If set to true, the OpenID Connect client is registered as bearer-only. |
| SSO_ENABLE_CORS | If set to true, the RH-SSO adapter enables Cross-Origin Resource Sharing (CORS). |
If the RH-SSO client uses the SAML protocol, the following additional variables need to be configured:
| Variable | Description |
|---|---|
| SSO_SAML_KEYSTORE_SECRET | Secret to use for access to SAML keystore. The default is sso-app-secret. |
| SSO_SAML_KEYSTORE | Keystore filename in the SAML keystore secret. The default is keystore.jks. |
| SSO_SAML_KEYSTORE_PASSWORD | Keystore password for SAML. The default is mykeystorepass. |
| SSO_SAML_CERTIFICATE_NAME | Alias for keys/certificate to use for SAML. The default is jboss. |
See Example Workflow: Automatically Registering EAP Application in RH-SSO with OpenID-Connect Client for an end-to-end example of the automatic client registration method using an OpenID-Connect client.
4.4.1.2. Manual RH-SSO Client Registration
Manual RH-SSO client registration is determined by the presence of a deployment file in the client application’s ../configuration/ directory. These files are exported from the client adapter in the RH-SSO web console. The name of this file is different for OpenID-Connect and SAML clients:
| OpenID-Connect | ../configuration/secure-deployments |
| SAML | ../configuration/secure-saml-deployments |
These files are copied to the RH-SSO adapter configuration section in the standalone-openshift.xml at when the application is deployed.
There are two methods for passing the RH-SSO adapter configuration to the client application:
- Modify the deployment file to contain the RH-SSO adapter configuration so that it is included in the standalone-openshift.xml file at deployment, or
- Manually include the OpenID-Connect keycloak.json file, or the SAML keycloak-saml.xml file in the client application’s ../WEB-INF directory.
See Example Workflow: Manually Configure an Application to Use RH-SSO Authentication, Using SAML Client for an end-to-end example of the manual RH-SSO client registration method using a SAML client.
4.5. Limitations
OpenShift does not currently accept OpenShift role mapping from external providers. If RH-SSO is used as an authentication gateway for OpenShift, users created in RH-SSO must have the roles added using the OpenShift Administrator oadm policy
command.
For example, to allow an RH-SSO-created user to view a project namespace in OpenShift:
oadm policy add-role-to-user view <user-name> -n <project-name>
