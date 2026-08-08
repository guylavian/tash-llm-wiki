---
title: "Chapter 3. Migrating Operator deployments on Openshift - Red Hat build of Keycloak 26.2 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-migrating-operator
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/migration_guide/migrating-operator
guide: migration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "To adapt to the revamped server configuration, the Red Hat build of Keycloak Operator was completely recreated. The Operator provides full integration with Red Hat build of Keycloak, but it is not backward compatible with the Red Hat Single Sign-On 7.6 Operator. Using the new Operator requires creating a new Red Hat build of Keycloak deployment. For full details, see the Operator Guide. 3.1. Prere…"
---

# Chapter 3. Migrating Operator deployments on Openshift - Red Hat build of Keycloak 26.2 Migration Guide

Chapter 3. Migrating Operator deployments on Openshift
To adapt to the revamped server configuration, the Red Hat build of Keycloak Operator was completely recreated. The Operator provides full integration with Red Hat build of Keycloak, but it is not backward compatible with the Red Hat Single Sign-On 7.6 Operator. Using the new Operator requires creating a new Red Hat build of Keycloak deployment. For full details, see the Operator Guide.
3.1. Prerequisites
- The previous instance of Red Hat Single Sign-On 7.6 was shut down so that it does not use the same database instance that will be used by Red Hat build of Keycloak .
- In case the unsupported embedded database (that is managed by the Red Hat Single Sign-On 7.6 Operator)) was used, it has been converted to an external database that is provisioned by the user.
- Database backup was created.
- You reviewed the Release Notes.
3.2. Migration process
- Install Red Hat build of Keycloak Operator to the namespace.
- Create new CRs and related Secrets. Manually migrate your Red Hat Single Sign-On 7.6 configuration to your new Keycloak CR.
- If custom providers were used, migrate them and create a custom Red Hat build of Keycloak container image to include them.
- If custom themes were used, migrate them and create a custom Red Hat build of Keycloak container image to include them.
3.3. Migrating Keycloak CR
Keycloak CR now supports all server configuration options. All relevant options are available as first class citizen fields directly under the spec of the CR. All options in the CR follow the same naming conventions as the server options making the experience between bare metal and Operator deployments seamless.
Additionally, you can define any options that are missing from the CR in the additionalOptions
field such as SPI providers configuration. Another option is to use podTemplate
, a Technology Preview field, to modify the raw Kubernetes deployment pod template in case a supported alternative does not exist as a first class citizen field in the CR.
The following shows an example Keycloak CR to deploy Red Hat build of Keycloak through the Operator:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
instances: 1
db:
vendor: postgres
host: postgres-db
usernameSecret:
name: keycloak-db-secret
key: username
passwordSecret:
name: keycloak-db-secret
key: password
http:
tlsSecret: example-tls-secret
hostname:
hostname: test.keycloak.org
additionalOptions:
- name: spi-connections-http-client-default-connection-pool-size
value: 20
Notice the resemblance with CLI configuration:
./kc.sh start --db=postgres --db-url-host=postgres-db --db-username=user --db-password=pass --https-certificate-file=mycertfile --https-certificate-key-file=myprivatekey --hostname=test.keycloak.org --spi-connections-http-client-default-connection-pool-size=20
3.3.1. Migrating database configuration
Red Hat build of Keycloak can use the same database instance as was previously used by Red Hat Single Sign-On 7.6. The database schema will be migrated automatically the first time Red Hat build of Keycloak connects to it.
Migrating the embedded database managed by Red Hat Single Sign-On 7.6 Operator is not supported.
In the Red Hat Single Sign-On 7.6 Operator, the external database connection was configured using a Secret, for example:
apiVersion: v1
kind: Secret
metadata:
name: keycloak-db-secret
namespace: keycloak
labels:
app: sso
stringData:
POSTGRES_DATABASE: kc-db-name
POSTGRES_EXTERNAL_ADDRESS: my-postgres-hostname
POSTGRES_EXTERNAL_PORT: 5432
POSTGRES_USERNAME: user
POSTGRES_PASSWORD: pass
type: Opaque
In Red Hat build of Keycloak , the database is configured directly in the Keycloak CR with credentials referenced as Secrets, for example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
db:
vendor: postgres
host: my-postgres-hostname
port: 5432
usernameSecret:
name: keycloak-db-secret
key: username
passwordSecret:
name: keycloak-db-secret
key: password
...
apiVersion: v1
kind: Secret
metadata:
name: keycloak-db-secret
stringData:
username: "user"
password: "pass"
type: Opaque
3.3.1.1. Supported database vendors
Red Hat Single Sign-On 7.6 Operator supported only PostgreSQL databases, but the Red Hat build of Keycloak Operator supports all database vendors that are supported by the server.
3.3.2. Migrating TLS configuration
Red Hat Single Sign-On 7.6 Operator by default configured the server to use the TLS Secret generated by OpenShift CA. Red Hat build of Keycloak Operator does not make any assumptions around TLS to meet production best practices and requires users to provide their own TLS certificate and key pair, for example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
http:
tlsSecret: example-tls-secret
...
The expected format of the secret referred to in tlsSecret should use the standard Kubernetes TLS Secret (kubernetes.io/tls
) type.
The Red Hat Single Sign-On 7.6 Operator used the reencrypt TLS termination strategy by default on Route. Red Hat build of Keycloak Operator uses the passthrough strategy by default. Additionally, the Red Hat Single Sign-On 7.6 Operator supported configuring TLS termination. Red Hat build of Keycloak Operator does not support TLS termination in the current release.
If the default Operator-managed Route does not meet desired TLS configuration, a custom Route needs to be created by the user and the default one disabled as:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
ingress:
enabled: false
...
3.3.3. Using a custom image for extensions
To reflect best practices and support immutable containers, the Red Hat build of Keycloak Operator no longer supports specifying extensions in the Keycloak CR. In order to deploy an extension, an optimized custom image must be built. Keycloak CR now includes a dedicated field, image
, for specifying Red Hat build of Keycloak images, for example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
image: quay.io/my-company/my-keycloak:latest
...
When specifying a custom image, the Operator assumes it is already optimized and does not perform the costly optimization at each server start.
3.3.4. Upgrade strategy changed
The Red Hat Single Sign-On 7.6 Operator supported recreate and rolling strategies when performing a server upgrade. This approach was not practical. It was up to the user to choose if the Red Hat Single Sign-On 7.6 Operator should scale down the deployment before performing an upgrade and database migration. It was not clear to the users when the rolling strategy could be safely used.
Therefore, the Red Hat build of Keycloak Operator will by default perform the recreate strategy, which scales down the whole deployment before creating Pods with the new server container image to ensure only a single server version accesses the database.
Users can configure two alternative update strategies Auto and Explicit which allows rolling updates in some cases. Note that also with these update strategies, only a single server version must access the database at any time.
Additional resources
3.3.5. Health endpoint enabled by default
Red Hat build of Keycloak configures the server to expose health endpoints by default that are used by OpenShift probes. The endpoints are exposed on the management interface that uses a dedicated port (9000 by default) and is accessible from within OpenShift, but not exposed by the Operator as a Route.
3.3.6. Migrating advanced deployment options using Pod templates
The Red Hat Single Sign-On 7.6 Operator exposed multiple low-level fields for deployment configuration, such as volumes. Red Hat build of Keycloak Operator is more opinionated and does not expose most of these fields. However, it is still possible to configure any desired deployment fields specified as the podTemplate
, for example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
unsupported:
podTemplate:
metadata:
labels:
foo: "bar"
spec:
containers:
- volumeMounts:
- name: test-volume
mountPath: /mnt/test
volumes:
- name: test-volume
secret:
secretName: test-secret
...
The spec.unsupported.podTemplate
field is a Technology Preview feature. It offers only limited support as it exposes low-level configuration where full functionality has not been tested under all conditions. Whenever possible, use the fully supported first class citizen fields in the top level of the CR spec.
For example, instead of spec.unsupported.podTemplate.spec.imagePullSecrets
, use directly spec.imagePullSecrets
.
3.3.7. Connecting to an external instance is no longer supported
The Red Hat Single Sign-On 7.6 Operator supported connecting to an external instance of Red Hat Single Sign-On 7.6. For example, creating clients within an existing realm through Client CRs is no longer supported in the Red Hat build of Keycloak Operator.
3.3.8. Migrating Horizontal Pod Autoscaler enabled deployments
To use a Horizontal Pod Autoscaler (HPA) with Red Hat Single Sign-On 7.6, it was necessary to set the disableReplicasSyncing: true
field in the Keycloak CR and scale the server StatefulSet. This is no longer necessary as the Keycloak CR in Red Hat build of Keycloak Operator can be scaled directly by an HPA.
3.4. Migrating the Keycloak realm CR
The Realm CR was replaced by the Realm Import CR, which offers similar functionality and has a similar schema. The Realm Import CR offers only Realm bootstrapping and as such no longer supports Realm deletion. It also does not support updates, similarly to the previous Realm CR.
Full Realm representation is now included in the Realm Import CR, in comparison to the previous Realm CR that offered only a few selected fields.
Example of Red Hat Single Sign-On 7.6 Realm CR:
apiVersion: keycloak.org/v1alpha1
kind: KeycloakRealm
metadata:
name: example-keycloakrealm
spec:
instanceSelector:
matchLabels:
app: sso
realm:
id: "basic"
realm: "basic"
enabled: True
displayName: "Basic Realm"
Example of corresponding Red Hat build of Keycloak Realm Import CR:
apiVersion: k8s.keycloak.org/v2alpha1
kind: KeycloakRealmImport
metadata:
name: example-keycloakrealm
spec:
keycloakCRName: example-kc
realm:
id: "basic"
realm: "basic"
enabled: True
displayName: "Basic Realm"
3.5. Removed CRs
The Client and User CRs were removed from Red Hat build of Keycloak Operator. The lack of these CRs can be partially mitigated by the new Realm Import CR, which allows initial creation (but not updates or deletion) of virtually any realm resource. Adding support for Client CRs is planned for a future Red Hat build of Keycloak release, while User CRs are not currently a planned feature.
