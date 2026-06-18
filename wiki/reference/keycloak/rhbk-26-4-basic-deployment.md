---
title: "Chapter 2. Basic Red Hat build of Keycloak deployment - Red Hat build of Keycloak 26.4 Operator Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-basic-deployment
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/operator_guide/basic-deployment-
guide: operator_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 2. Basic Red Hat build of Keycloak deployment - Red Hat build of Keycloak 26.4 Operator Guide

Chapter 2. Basic Red Hat build of Keycloak deployment
Install Red Hat build of Keycloak using the Operator.
2.1. Performing a basic Red Hat build of Keycloak deployment
This chapter describes how to perform a basic Red Hat build of Keycloak Deployment on OpenShift using the Operator.
2.1.1. Preparing for deployment
Once the Red Hat build of Keycloak Operator is installed and running in the cluster namespace, you can set up the other deployment prerequisites.
- Database
- Hostname
- TLS Certificate and associated keys
2.1.1.1. Database
A database should be available and accessible from the cluster namespace where Red Hat build of Keycloak is installed. For a list of supported databases, see Configuring the database. The Red Hat build of Keycloak Operator does not manage the database and you need to provision it yourself. Consider verifying your cloud provider offering or using a database operator.
For development purposes, you can use an ephemeral PostgreSQL pod installation. To provision it, follow the approach below:
Create YAML file example-postgres.yaml
:
apiVersion: apps/v1
kind: StatefulSet
metadata:
name: postgresql-db
spec:
serviceName: postgresql-db-service
selector:
matchLabels:
app: postgresql-db
replicas: 1
template:
metadata:
labels:
app: postgresql-db
spec:
containers:
- name: postgresql-db
image: postgres:15
volumeMounts:
- mountPath: /data
name: cache-volume
env:
- name: POSTGRES_USER
value: testuser
- name: POSTGRES_PASSWORD
value: testpassword
- name: PGDATA
value: /data/pgdata
- name: POSTGRES_DB
value: keycloak
volumes:
- name: cache-volume
emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
name: postgres-db
spec:
selector:
app: postgresql-db
type: LoadBalancer
ports:
- port: 5432
targetPort: 5432
Apply the changes:
oc apply -f example-postgres.yaml
2.1.1.2. Hostname
For a production ready installation, you need a hostname that can be used to contact Red Hat build of Keycloak. See Configuring the hostname (v2) for the available configurations.
For development purposes, this chapter will use test.keycloak.org
.
When running on OpenShift, with ingress enabled, and with the spec.ingress.classname set to openshift-default, you may leave the spec.hostname.hostname unpopulated in the Keycloak CR. The operator will assign a default hostname to the stored version of the CR similar to what would be created by an OpenShift Route without an explicit host - that is ingress-namespace.appsDomain If the appsDomain changes, or should you need a different hostname for any reason, then update the Keycloak CR.
If you set the hostname-admin
, or the deprecated hostname-admin-url
, even if you enable ingress, no ingress will be created specifically for admin access. Admin access via a separate hostname is generally expected to have access restrictions, which are not currently expressible via the Keycloak CR. Also the default ingress does not prevent accessing admin endpoints, so you may not want to enable ingress handling via the Keycloak CR at all when you have a separate hostname for admin endpoints.
2.1.1.3. TLS Certificate and key
See your Certification Authority to obtain the certificate and the key.
For development purposes, you can enter this command to obtain a self-signed certificate:
openssl req -subj '/CN=test.keycloak.org/O=Test Keycloak./C=US' -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
You should install it in the cluster namespace as a Secret by entering this command:
oc create secret tls example-tls-secret --cert certificate.pem --key key.pem
2.1.2. Deploying Red Hat build of Keycloak
To deploy Red Hat build of Keycloak, you create a Custom Resource (CR) based on the Keycloak Custom Resource Definition (CRD).
Consider storing the Database credentials in a separate Secret. Enter the following commands:
oc create secret generic keycloak-db-secret \
--from-literal=username=[your_database_username] \
--from-literal=password=[your_database_password]
You can customize several fields using the Keycloak CRD. For a basic deployment, you can stick to the following approach:
Create YAML file example-kc.yaml
:
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
proxy:
headers: xforwarded # double check your reverse proxy sets and overwrites the X-Forwarded-* headers
Apply the changes:
oc apply -f example-kc.yaml
To check that the Red Hat build of Keycloak instance has been provisioned in the cluster, check the status of the created CR by entering the following command:
oc get keycloaks/example-kc -o go-template='{{range .status.conditions}}CONDITION: {{.type}}{{"\n"}} STATUS: {{.status}}{{"\n"}} MESSAGE: {{.message}}{{"\n"}}{{end}}'
When the deployment is ready, look for output similar to the following:
CONDITION: Ready
STATUS: true
MESSAGE:
CONDITION: HasErrors
STATUS: false
MESSAGE:
CONDITION: RollingUpdate
STATUS: false
MESSAGE:
2.1.3. Accessing the Red Hat build of Keycloak deployment
The Red Hat build of Keycloak deployment can be exposed through a basic Ingress accessible through the provided hostname.
On installations with multiple default IngressClass instances or when running on OpenShift 4.12+ you should provide an ingressClassName by setting ingress
spec with className
property to the desired class name:
Edit YAML file example-kc.yaml
:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
...
ingress:
className: openshift-default
The operator annotates the Ingress to match expectations for TLS passthrough or TLS termination on OpenShift with the default IngressClass. See below for more on TLS termination.
2.1.3.1. Proxy modes with the basic Ingress
The operator annotates the Ingress to match expectations for TLS termination or passthrough on OpenShift with the default IngressClass. For this reason TLS reencryption is not yet considered supported by basic Ingress, but you may be able to specify the tlsSecret
on both the http
and ingress
specs as a starting point. You should double check the requirements of your IngressClass and platform to see if additional Ingress or Service annotations are needed in your desired scenario.
TLS passthrough is shown in the preceding example-kc
example. It is enabled when you associate a tlsSecret
with the http
configuration and leave Ingress enabled without specifying a tlsSecret
on it.
TLS termination, or edge mode, is enabled by associating a tlsSecret
with the ingress
spec and by enabling HTTP access.
Example TLS Termination YAML:
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
httpEnabled: true
ingress:
tlsSecret: example-tls-secret
hostname:
hostname: test.keycloak.org
proxy:
headers: xforwarded # double check your reverse proxy sets and overwrites the X-Forwarded-* headers
2.1.3.2. Custom Access
If the default ingress does not fit your use case, disable it by setting ingress
spec with enabled
property to false
value:
Edit YAML file example-kc.yaml
:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
...
ingress:
enabled: false
Apply the changes:
oc apply -f example-kc.yaml
You can then provide an alternative ingress resource pointing to the service <keycloak-cr-name>-service
. For example, on OpenShift you are not allowed to use wildcard certificates on passthrough Routes with HTTP/2 enabled. A Keycloak CR on OpenShift with TLS enabled using a wildcard certificate with the default IngressClass creates such a Route. In this case, you must disable the built-in ingress with .spec.ingress.enabled: false
. Access may then be provided by creating a reencrypt Route instead:
$ oc create route reencrypt --service=<keycloak-cr-name>-service --cert=<configured-certificate> --key=<certificate-key> --dest-ca-cert=<ca-certificate> --ca-cert=<ca-certificate> --hostname=<hostname>
For debugging and development purposes, consider directly connecting to the Red Hat build of Keycloak service using a port forward. For example, enter this command:
oc port-forward service/example-kc-service 8443:8443
2.1.3.3. Configuring the reverse proxy settings matching your Ingress Controller
The Operator supports configuring which of the reverse proxy headers should be accepted by server, which includes Forwarded
and X-Forwarded-*
headers.
If you Ingress implementation sets and overwrites either Forwarded
or X-Forwarded-*
headers, you can reflect that in the Keycloak CR as follows:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
...
proxy:
headers: forwarded|xforwarded
If the proxy.headers
field is not specified, the Operator falls back to legacy behaviour by implicitly setting proxy=passthrough
by default. This results in deprecation warnings in the server log. This fallback will be removed in a future release.
When using the proxy.headers
field, make sure your Ingress properly sets and overwrites the Forwarded
or X-Forwarded-*
headers respectively. To set these headers, consult the documentation for your Ingress Controller. Consider configuring it for either reencrypt or edge TLS termination as passthrough TLS doesn’t allow the Ingress to modify the requests headers. Misconfiguration will leave Red Hat build of Keycloak exposed to security vulnerabilities.
For more details refer to the Configuring a reverse proxy guide.
2.1.4. Accessing the Admin Console
When deploying Red Hat build of Keycloak, the operator generates an arbitrary initial admin username
and password
and stores those credentials as a basic-auth Secret object in the same namespace as the CR.
Change the default admin credentials and enable MFA in Red Hat build of Keycloak before going to production.
To fetch the initial admin credentials, you have to read and decode the Secret. The Secret name is derived from the Keycloak CR name plus the fixed suffix -initial-admin
. To get the username and password for the example-kc
CR, enter the following commands:
oc get secret example-kc-initial-admin -o jsonpath='{.data.username}' | base64 --decode
oc get secret example-kc-initial-admin -o jsonpath='{.data.password}' | base64 --decode
You can use those credentials to access the Admin Console or the Admin REST API.
2.1.5. Security Considerations
Anyone with the ability to create or edit Keycloak or KeycloakRealmImport CRs should be a namespace level admin.
Setting the Keycloak CR image requires a high degree of trust as whatever image is running will at least have access to any Secrets used for environment variables.
Similarly the unsupported podTemplate gives the ability to deploy alternative workloads which may be granted the same permissions as the operator itself - which includes the ability to access Secrets in the namespace.
