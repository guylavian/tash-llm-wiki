---
title: "Chapter 5. Reference - Red Hat Single Sign-On 7.5 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-5-reference
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.5/html/red_hat_single_sign-on_for_openshift/reference
version: 7.5
family: rhsso
documentKind: "Documentation"
abstract: "5.1. Artifact repository mirrors A repository in Maven holds build artifacts and dependencies of various types (all the project jars, library jar, plugins or any other project specific artifacts). It also specifies locations from where to download artifacts from, while performing the S2I build. Besides using central repositories, it is a common practice for organizations to deploy a local custom r…"
---

# Chapter 5. Reference - Red Hat Single Sign-On 7.5 Red Hat Single Sign-On for OpenShift

Chapter 5. Reference
5.1. Artifact repository mirrors
A repository in Maven holds build artifacts and dependencies of various types (all the project jars, library jar, plugins or any other project specific artifacts). It also specifies locations from where to download artifacts from, while performing the S2I build. Besides using central repositories, it is a common practice for organizations to deploy a local custom repository (mirror).
Benefits of using a mirror are:
- Availability of a synchronized mirror, which is geographically closer and faster.
- Ability to have greater control over the repository content.
- Possibility to share artifacts across different teams (developers, CI), without the need to rely on public servers and repositories.
- Improved build times.
Often, a repository manager can serve as local cache to a mirror. Assuming that the repository manager is already deployed and reachable externally at http://10.0.0.1:8080/repository/internal/, the S2I build can then use this manager by supplying the MAVEN_MIRROR_URL
environment variable to the build configuration of the application using the following procedure:
Procedure
Identify the name of the build configuration to apply
MAVEN_MIRROR_URL
variable against.$ oc get bc -o name buildconfig/sso
Update build configuration of
sso
with aMAVEN_MIRROR_URL
environment variable.$ oc set env bc/sso \ -e MAVEN_MIRROR_URL="http://10.0.0.1:8080/repository/internal/" buildconfig "sso" updated
Verify the setting.
$ oc set env bc/sso --list # buildconfigs sso MAVEN_MIRROR_URL=http://10.0.0.1:8080/repository/internal/
- Schedule new build of the application.
During application build, you will notice that Maven dependencies are pulled from the repository manager, instead of the default public repositories. Also, after the build is finished, you will see that the mirror is filled with all the dependencies that were retrieved and used during the build.
5.2. Environment variables
5.2.1. Information environment variables
The following information environment variables are designed to convey information about the image and should not be modified by the user:
| Variable Name | Description | Example Value |
|---|---|---|
| AB_JOLOKIA_AUTH_OPENSHIFT | - | true |
| AB_JOLOKIA_HTTPS | - | true |
| AB_JOLOKIA_PASSWORD_RANDOM | - | true |
| JBOSS_IMAGE_NAME | Image name, same as "name" label. | rh-sso-7/sso75-openshift-rhel8 |
| JBOSS_IMAGE_VERSION | Image version, same as "version" label. | 7.5 |
| JBOSS_MODULES_SYSTEM_PKGS | - | org.jboss.logmanager,jdk.nashorn.api |
5.2.2. Configuration environment variables
Configuration environment variables are designed to conveniently adjust the image without requiring a rebuild, and should be set by the user as desired.
| Variable Name | Description | Example Value |
|---|---|---|
| AB_JOLOKIA_AUTH_OPENSHIFT |
Switch on client authentication for OpenShift TLS communication. The value of this parameter can be a relative distinguished name which must be contained in a presented client’s certificate. Enabling this parameter will automatically switch Jolokia into https communication mode. The default CA cert is set to | true |
| AB_JOLOKIA_CONFIG |
If set uses this file (including path) as Jolokia JVM agent properties (as described in Jolokia’s reference manual). If not set, the | /opt/jolokia/custom.properties |
| AB_JOLOKIA_DISCOVERY_ENABLED | Enable Jolokia discovery. Defaults to false. | true |
| AB_JOLOKIA_HOST | Host address to bind to. Defaults to 0.0.0.0. | 127.0.0.1 |
| AB_JOLOKIA_HTTPS |
Switch on secure communication with https. By default self-signed server certificates are generated if no serverCert configuration is given in AB_JOLOKIA_OPTS. NOTE: If the values is set to an empty string, https is turned | true |
| AB_JOLOKIA_ID | Agent ID to use ($HOSTNAME by default, which is the container id). | openjdk-app-1-xqlsj |
| AB_JOLOKIA_OFF |
If set disables activation of Jolokia (i.e. echos an empty value). By default, Jolokia is enabled. NOTE: If the values is set to an empty string, https is turned | true |
| AB_JOLOKIA_OPTS |
Additional options to be appended to the agent configuration. They should be given in the format | backlog=20 |
| AB_JOLOKIA_PASSWORD | Password for basic authentication. By default authentication is switched off. | mypassword |
| AB_JOLOKIA_PASSWORD_RANDOM | If set, a random value is generated for AB_JOLOKIA_PASSWORD, and it is saved in the /opt/jolokia/etc/jolokia.pw file. | true |
| AB_JOLOKIA_PORT | Port to use (Default: 8778). | 5432 |
| AB_JOLOKIA_USER | User for basic authentication. Defaults to jolokia. | myusername |
| CONTAINER_CORE_LIMIT | A calculated core limit as described in CFS Bandwidth Control. | 2 |
| GC_ADAPTIVE_SIZE_POLICY_WEIGHT | The weighting given to the current Garbage Collection (GC) time versus previous GC times. | 90 |
| GC_MAX_HEAP_FREE_RATIO | Maximum percentage of heap free after GC to avoid shrinking. | 40 |
| GC_MAX_METASPACE_SIZE | The maximum metaspace size. | 100 |
| GC_TIME_RATIO_MIN_HEAP_FREE_RATIO | Minimum percentage of heap free after GC to avoid expansion. | 20 |
| GC_TIME_RATIO | Specifies the ratio of the time spent outside the garbage collection (for example, the time spent for application execution) to the time spent in the garbage collection. | 4 |
| JAVA_DIAGNOSTICS | Set this to get some diagnostics information to standard out when things are happening. | true |
| JAVA_INITIAL_MEM_RATIO |
This is used to calculate a default initial heap memory based the maximal heap memory. The default is 100 which means 100% of the maximal heap is used for the initial heap size. You can skip this mechanism by setting this value to 0 in which case no | 100 |
| JAVA_MAX_MEM_RATIO |
It is used to calculate a default maximal heap memory based on a containers restriction. If used in a Docker container without any memory constraints for the container then this option has no effect. If there is a memory constraint then | 40 |
| JAVA_OPTS_APPEND | Server startup options. | -Dkeycloak.migration.action=export -Dkeycloak.migration.provider=dir -Dkeycloak.migration.dir=/tmp |
| MQ_SIMPLE_DEFAULT_PHYSICAL_DESTINATION |
For backwards compatability, set to true to use | false |
| OPENSHIFT_KUBE_PING_LABELS | Clustering labels selector. | app=sso-app |
| OPENSHIFT_KUBE_PING_NAMESPACE | Clustering project namespace. | myproject |
| SCRIPT_DEBUG |
If set to | true |
| SSO_ADMIN_PASSWORD |
Password of the administrator account for the | adm-password |
| SSO_ADMIN_USERNAME |
Username of the administrator account for the | admin |
| SSO_HOSTNAME |
Custom hostname for the Red Hat Single Sign-On server. Not set by default. If not set, the | rh-sso-server.openshift.example.com |
| SSO_REALM | Name of the realm to be created in the Red Hat Single Sign-On server if this environment variable is provided. | demo |
| SSO_SERVICE_PASSWORD | The password for the Red Hat Single Sign-On service user. | mgmt-password |
| SSO_SERVICE_USERNAME | The username used to access the Red Hat Single Sign-On service. This is used by clients to create the application client(s) within the specified Red Hat Single Sign-On realm. This user is created if this environment variable is provided. | sso-mgmtuser |
| SSO_TRUSTSTORE | The name of the truststore file within the secret. | truststore.jks |
| SSO_TRUSTSTORE_DIR | Truststore directory. | /etc/sso-secret-volume |
| SSO_TRUSTSTORE_PASSWORD | The password for the truststore and certificate. | mykeystorepass |
| SSO_TRUSTSTORE_SECRET | The name of the secret containing the truststore file. Used for sso-truststore-volume volume. | truststore-secret |
Available application templates for Red Hat Single Sign-On for OpenShift can combine the aforementioned configuration variables with common OpenShift variables (for example APPLICATION_NAME or SOURCE_REPOSITORY_URL), product specific variables (e.g. HORNETQ_CLUSTER_PASSWORD), or configuration variables typical to database images (e.g. POSTGRESQL_MAX_CONNECTIONS) yet. All of these different types of configuration variables can be adjusted as desired to achieve the deployed Red Hat Single Sign-On-enabled application will align with the intended use case as much as possible. The list of configuration variables, available for each category of application templates for Red Hat Single Sign-On-enabled applications, is described below.
5.2.3. Template variables for all Red Hat Single Sign-On images
| Variable | Description |
|---|---|
| APPLICATION_NAME | The name for the application. |
| DB_MAX_POOL_SIZE | Sets xa-pool/max-pool-size for the configured datasource. |
| DB_TX_ISOLATION | Sets transaction-isolation for the configured datasource. |
| DB_USERNAME | Database user name. |
| HOSTNAME_HTTP | Custom hostname for http service route. Leave blank for default hostname, e.g.: <application-name>.<project>.<default-domain-suffix>. |
| HOSTNAME_HTTPS | Custom hostname for https service route. Leave blank for default hostname, e.g.: <application-name>.<project>.<default-domain-suffix>. |
| HTTPS_KEYSTORE | The name of the keystore file within the secret. If defined along with HTTPS_PASSWORD and HTTPS_NAME, enable HTTPS and set the SSL certificate key file to a relative path under $JBOSS_HOME/standalone/configuration. |
| HTTPS_KEYSTORE_TYPE | The type of the keystore file (JKS or JCEKS). |
| HTTPS_NAME | The name associated with the server certificate (e.g. jboss). If defined along with HTTPS_PASSWORD and HTTPS_KEYSTORE, enable HTTPS and set the SSL name. |
| HTTPS_PASSWORD | The password for the keystore and certificate (e.g. mykeystorepass). If defined along with HTTPS_NAME and HTTPS_KEYSTORE, enable HTTPS and set the SSL key password. |
| HTTPS_SECRET | The name of the secret containing the keystore file. |
| IMAGE_STREAM_NAMESPACE | Namespace in which the ImageStreams for Red Hat Middleware images are installed. These ImageStreams are normally installed in the openshift namespace. You should only need to modify this if you’ve installed the ImageStreams in a different namespace/project. |
| JGROUPS_CLUSTER_PASSWORD | JGroups cluster password. |
| JGROUPS_ENCRYPT_KEYSTORE | The name of the keystore file within the secret. |
| JGROUPS_ENCRYPT_NAME | The name associated with the server certificate (e.g. secret-key). |
| JGROUPS_ENCRYPT_PASSWORD | The password for the keystore and certificate (e.g. password). |
| JGROUPS_ENCRYPT_SECRET | The name of the secret containing the keystore file. |
| SSO_ADMIN_USERNAME |
Username of the administrator account for the |
| SSO_ADMIN_PASSWORD |
Password of the administrator account for the |
| SSO_REALM | Name of the realm to be created in the Red Hat Single Sign-On server if this environment variable is provided. |
| SSO_SERVICE_USERNAME | The username used to access the Red Hat Single Sign-On service. This is used by clients to create the application client(s) within the specified Red Hat Single Sign-On realm. This user is created if this environment variable is provided. |
| SSO_SERVICE_PASSWORD | The password for the Red Hat Single Sign-On service user. |
| SSO_TRUSTSTORE | The name of the truststore file within the secret. |
| SSO_TRUSTSTORE_SECRET | The name of the secret containing the truststore file. Used for sso-truststore-volume volume. |
| SSO_TRUSTSTORE_PASSWORD | The password for the truststore and certificate. |
5.2.4. Template variables specific to sso75-postgresql, sso75-postgresql-persistent, and sso75-x509-postgresql-persistent
| Variable | Description |
|---|---|
| DB_USERNAME | Database user name. |
| DB_PASSWORD | Database user password. |
| DB_JNDI | Database JNDI name used by application to resolve the datasource, e.g. java:/jboss/datasources/postgresql |
| POSTGRESQL_MAX_CONNECTIONS | The maximum number of client connections allowed. This also sets the maximum number of prepared transactions. |
| POSTGRESQL_SHARED_BUFFERS | Configures how much memory is dedicated to PostgreSQL for caching data. |
5.2.5. Template variables for general eap64 and eap71 S2I images
| Variable | Description |
|---|---|
| APPLICATION_NAME | The name for the application. |
| ARTIFACT_DIR | Artifacts directory. |
| AUTO_DEPLOY_EXPLODED | Controls whether exploded deployment content should be automatically deployed. |
| CONTEXT_DIR | Path within Git project to build; empty for root project directory. |
| GENERIC_WEBHOOK_SECRET | Generic build trigger secret. |
| GITHUB_WEBHOOK_SECRET | GitHub trigger secret. |
| HORNETQ_CLUSTER_PASSWORD | HornetQ cluster administrator password. |
| HORNETQ_QUEUES | Queue names. |
| HORNETQ_TOPICS | Topic names. |
| HOSTNAME_HTTP | Custom host name for http service route. Leave blank for default host name, e.g.: <application-name>.<project>.<default-domain-suffix>. |
| HOSTNAME_HTTPS | Custom host name for https service route. Leave blank for default host name, e.g.: <application-name>.<project>.<default-domain-suffix>. |
| HTTPS_KEYSTORE_TYPE | The type of the keystore file (JKS or JCEKS). |
| HTTPS_KEYSTORE | The name of the keystore file within the secret. If defined along with HTTPS_PASSWORD and HTTPS_NAME, enable HTTPS and set the SSL certificate key file to a relative path under $JBOSS_HOME/standalone/configuration. |
| HTTPS_NAME | The name associated with the server certificate (e.g. jboss). If defined along with HTTPS_PASSWORD and HTTPS_KEYSTORE, enable HTTPS and set the SSL name. |
| HTTPS_PASSWORD | The password for the keystore and certificate (e.g. mykeystorepass). If defined along with HTTPS_NAME and HTTPS_KEYSTORE, enable HTTPS and set the SSL key password. |
| HTTPS_SECRET | The name of the secret containing the keystore file. |
| IMAGE_STREAM_NAMESPACE | Namespace in which the ImageStreams for Red Hat Middleware images are installed. These ImageStreams are normally installed in the openshift namespace. You should only need to modify this if you’ve installed the ImageStreams in a different namespace/project. |
| JGROUPS_CLUSTER_PASSWORD | JGroups cluster password. |
| JGROUPS_ENCRYPT_KEYSTORE | The name of the keystore file within the secret. |
| JGROUPS_ENCRYPT_NAME | The name associated with the server certificate (e.g. secret-key). |
| JGROUPS_ENCRYPT_PASSWORD | The password for the keystore and certificate (e.g. password). |
| JGROUPS_ENCRYPT_SECRET | The name of the secret containing the keystore file. |
| SOURCE_REPOSITORY_REF | Git branch/tag reference. |
| SOURCE_REPOSITORY_URL | Git source URI for application. |
5.2.6. Template variables specific to eap64-sso-s2i and eap71-sso-s2i for automatic client registration
| Variable | Description |
|---|---|
| SSO_URL | Red Hat Single Sign-On server location. |
| SSO_REALM | Name of the realm to be created in the Red Hat Single Sign-On server if this environment variable is provided. |
| SSO_USERNAME | The username used to access the Red Hat Single Sign-On service. This is used to create the application client(s) within the specified Red Hat Single Sign-On realm. This should match the SSO_SERVICE_USERNAME specified through one of the sso75- templates. |
| SSO_PASSWORD | The password for the Red Hat Single Sign-On service user. |
| SSO_PUBLIC_KEY | Red Hat Single Sign-On public key. Public key is recommended to be passed into the template to avoid man-in-the-middle security attacks. |
| SSO_SECRET | The Red Hat Single Sign-On client secret for confidential access. |
| SSO_SERVICE_URL | Red Hat Single Sign-On service location. |
| SSO_TRUSTSTORE_SECRET | The name of the secret containing the truststore file. Used for sso-truststore-volume volume. |
| SSO_TRUSTSTORE | The name of the truststore file within the secret. |
| SSO_TRUSTSTORE_PASSWORD | The password for the truststore and certificate. |
| SSO_BEARER_ONLY | Red Hat Single Sign-On client access type. |
| SSO_DISABLE_SSL_CERTIFICATE_VALIDATION | If true SSL communication between EAP and the Red Hat Single Sign-On Server is insecure (i.e. certificate validation is disabled with curl) |
| SSO_ENABLE_CORS | Enable CORS for Red Hat Single Sign-On applications. |
5.2.7. Template variables specific to eap64-sso-s2i and eap71-sso-s2i for automatic client registration with SAML clients
| Variable | Description |
|---|---|
| SSO_SAML_CERTIFICATE_NAME | The name associated with the server certificate. |
| SSO_SAML_KEYSTORE_PASSWORD | The password for the keystore and certificate. |
| SSO_SAML_KEYSTORE | The name of the keystore file within the secret. |
| SSO_SAML_KEYSTORE_SECRET | The name of the secret containing the keystore file. |
| SSO_SAML_LOGOUT_PAGE | Red Hat Single Sign-On logout page for SAML applications. |
5.3. Exposed ports
| Port Number | Description |
|---|---|
| 8443 | HTTPS |
| 8778 | Jolokia monitoring |
