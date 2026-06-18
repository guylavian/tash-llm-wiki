---
title: "Chapter 4. Migrating Templates deployments on Openshift - Red Hat build of Keycloak 26.4 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-migrating-openshift
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/migration_guide/migrating-openshift
guide: migration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 4. Migrating Templates deployments on Openshift - Red Hat build of Keycloak 26.4 Migration Guide

Chapter 4. Migrating Templates deployments on Openshift
OpenShift templates were deprecated and removed from the Red Hat build of Keycloak container images. Using the Operator is the recommended alternative for deploying Red Hat build of Keycloak on OpenShift.
OpenShift 3.x is no longer supported.
You will generally need to create a Keycloak CR (of the Red Hat build of Keycloak Operator) that references an externally managed database. The PostgreSQL database with relevant templates is managed by a DeploymentConfig. You initially retain the application_name-postgresql
DeploymentConfig that was created by the template. The PostgreSQL database instance created by the DeploymentConfig will be usable by the Red Hat build of Keycloak Operator.
This guide does not include directions for migrating from this instance to a self-managed database, either by an operator or your cloud provider.
The Red Hat build of Keycloak Operator does not manage a database and it is required to have a database provisioned and managed separately.
4.1. Migrating deployments with the internal H2 database
The following are the affected templates:
- sso76-ocp3-https
- sso76-ocp4-https
- sso76-ocp3-x509-https
- sso76-ocp4-x509-https
These templates rely upon the devel database and are not supported for production use.
4.2. Migrating deployments with ephemeral PostgreSQL database
The following are the affected templates:
- sso76-ocp3-postgresql
- sso76-ocp4-postgresql
This template creates a PostgreSQL database without persistent storage, which is only recommended for development purposes.
4.3. Migrating deployments with persistent PostgreSQL database
The following are the affected templates:
- sso76-ocp3-postgresql-persistent
- sso76-ocp4-postgresql-persistent
- sso76-ocp3-x509-postgresql-persistent
- sso76-ocp4-x509-postgresql-persistent
Prerequisites
- The previous instance of Red Hat Single Sign-On 7.6 was shut down so that it does not use the same database instance that will be used by Red Hat build of Keycloak .
- Database backup was created.
- You reviewed the Release Notes.
Procedure
- Install Red Hat build of Keycloak Operator to the namespace.
Create new CRs and related Secrets.
Manually migrate your template based Red Hat Single Sign-On 7.6 configuration to your new Kecyloak CR. See the following examples for suggested mappings between Template parameters and Keycloak CR fields.
This example shows the Operator CR fields for Red Hat build of Keycloak.
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: name: rhbk spec: instances: 1 db: vendor: postgres host: postgres-db usernameSecret: name: keycloak-db-secret key: username passwordSecret: name: keycloak-db-secret key: password http: tlsSecret: sso-x509-https-secret
This example shows the DeploymentConfig for a Red Hat Single Sign-On 7.6 Template
apiVersion: apps.openshift.io/v1 kind: DeploymentConfig metadata: name: rhsso spec: replicas: 1 template: spec: volumes: - name: sso-x509-https-volume secret: secretName: sso-x509-https-secret defaultMode: 420 containers: volumeMounts: - name: sso-x509-https-volume readOnly: true env: - name: DB_SERVICE_PREFIX_MAPPING value: postgres-db=DB - name: DB_USERNAME value: username - name: DB_PASSWORD value: password
4.4. Keycloak CR field names
The following tables refer to fields of Keycloak CR by a JSON path notation. For example, .spec
refers to the spec
field. Note that spec.unsupported
is a Technology Preview field. It is more an indication that eventually that functionality will be achievable by other CR fields. Parameters marked in bold are supported by both the passthrough and reencrypt templates.
4.4.1. General Parameter Migration
| Red Hat Single Sign-On 7.6 | Red Hat build of Keycloak 26.4 |
|---|---|
| APPLICATION_NAME | .metadata.name |
| IMAGE_STREAM_NAMESPACE | N/A - the image is controlled by the operator or you main use spec.image to specify a custom image |
| SSO_ADMIN_USERNAME |
Defaults to admin, can be configured by |
| SSO_ADMIN_PASSWORD |
Created by the operator during the initial reconciliation, can be configured by |
| MEMORY_LIMIT |
|
| SSO_SERVICE_PASSWORD, SSO_SERVICE_USERNAME |
|
| SSO_TRUSTSTORE, SSO_TRUSTSTORE_PASSWORD, SSO_TRUSTSTORE_SECRET |
|
| SSO_REALM | Not needed if you are reusing the existing database. An alternative is the RealmImport CR. |
4.4.2. Database Deployment Parameter Migration
POSTGRESQL_IMAGE_STREAM_TAG, POSTGRESQL_MAX_CONNECTIONS, VOLUME_CAPACITY and POSTGRESQL_SHARED_BUFFERS will need to be migrated to whatever replacement you have chosen creating the database deployment.
4.4.3. Database Connection Parameter Migration
| Red Hat Single Sign-On 7.6 | Red Hat build of Keycloak 26.4 |
|---|---|
| DB_VENDOR |
|
| DB_DATABASE |
|
| DB_MIN_POOL_SIZE |
|
| DB_MAX_POOL_SIZE |
|
| DB_TX_ISOLATION |
may be set by the |
| DB_USERNAME |
|
| DB_PASSWORD |
|
| DB_JNDI | No longer applicable |
4.4.4. Networking Parameter Migration
| Red Hat Single Sign-On 7.6 | Red Hat build of Keycloak 26.4 |
|---|---|
| HOSTNAME_HTTP |
|
| HOSTNAME_HTTPS |
|
| SSO_HOSTNAME |
|
| HTTPS_SECRET |
|
| HTTPS_KEYSTORE HTTPS_KEYSTORE_TYPE HTTPS_NAME HTTPS_PASSWORD |
No longer applicable. The secret referenced by |
| X509_CA_BUNDLE |
|
Note that the Red Hat build of Keycloak Operator does not currently support a way to configure the TLS termination. By default, the passthrough strategy is used. Therefore, the proxy option is not yet exposed as a first-class citizen option field, because it does not matter whether the passthrough or reencrypt strategy is used. However, if you need this option, you can replace the default Ingress Operator certificate and manually configure a Route in order to trust Red Hat build of Keycloak’s certificate.
The default behavior of the Red Hat build of Keycloak Operator can be then overridden by:
additionalOptions:
name: proxy
value: reencrypt
4.4.5. JGroups Parameter Migration
JGROUPS_ENCRYPT_SECRET, JGROUPS_ENCRYPT_KEYSTORE, JGROUPS_ENCRYPT_NAME, JGROUPS_ENCRYPT_PASSWORD, and JGROUPS_CLUSTER_PASSWORD have no first-class representation in the Keycloak CR. The default clustering with jdbc-ping
encrypts the communication by default.
