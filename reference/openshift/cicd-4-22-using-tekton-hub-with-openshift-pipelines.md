---
title: "Using Tekton Hub with {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-using-tekton-hub-with-openshift-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/using-tekton-hub-with-openshift-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Using Tekton Hub with {pipelines-shortname}

[id="using-tekton-hub-with-openshift-pipelines"]
= Using Tekton Hub with {pipelines-shortname}

[role="_abstract"]
{tekton-hub} helps you discover, search, and share reusable tasks and pipelines for your CI/CD workflows. A public instance of {tekton-hub} is available at hub.tekton.dev. Cluster administrators can also install and deploy a custom instance of {tekton-hub} by modifying the configurations in the `TektonHub` custom resource (CR).

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="installing-and-deploying-tekton-hub-on-an-openshift-cluster_{context}"]
= Installing and deploying {tekton-hub} on a OpenShift Container Platform cluster

[role="_abstract"]
{tekton-hub} is an optional component; cluster administrators cannot install it using the `TektonConfig` custom resource (CR). To install and manage {tekton-hub}, use the `TektonHub` CR.

You can install {tekton-hub} on your cluster using two modes:

* _Without_ login authorization and ratings for {tekton-hub} artifacts
* _with_ login authorization and ratings for {tekton-hub} artifacts

[NOTE]
====
If you are using Github Enterprise or Gitlab Enterprise, install and deploy {tekton-hub} in the same network as the enterprise server. For example, if the enterprise server is running behind a VPN, deploy {tekton-hub} on a cluster that is also behind the VPN.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="installing-tekton-hub-without-login-and-rating_{context}"]
= Installing {tekton-hub} without login and rating

[role="_abstract"]
You can install {tekton-hub} on your cluster automatically with default configuration. When using the default configuration, {tekton-hub} does not support login with authorization and ratings for {tekton-hub} artifacts.

[discrete]
.Prerequisites
* Ensure that the {pipelines-title} Operator is installed in the default `openshift-pipelines` namespace on the cluster.

[discrete]
.Procedure

. Create a `TektonHub` CR similar to the following example.
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines <1>
  db:                      # Optional: If you want to use custom database
    secret: tekton-hub-db  # Name of db secret should be `tekton-hub-db`

  categories:              # Optional: If you want to use custom categories
    - Automation
    - Build Tools
    - CLI
    - Cloud
    - Code Quality
    - ...

  catalogs:                # Optional: If you want to use custom catalogs
    - name: tekton
      org: tektoncd
      type: community
      provider: github
      url: https://github.com/tektoncd/catalog
      revision: main

  scopes:                   # Optional: If you want to add new users
    - name: agent:create
      users: [abc, qwe, pqr]
    - name: catalog:refresh
      users: [abc, qwe, pqr]
    - name: config:refresh
      users: [abc, qwe, pqr]

  default:                   # Optional: If you want to add custom default scopes
    scopes:
      - rating:read
      - rating:write

  api:
    catalogRefreshInterval: 30m <2>
----
<1> The namespace in which {tekton-hub} must be installed; default is `openshift-pipelines`.
<2> The time interval after which the catalog refreshes automatically. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`). The default interval is 30 minutes.
+
[NOTE]
====
If you do not provide custom values for the optional fields in the `TektonHub` CR, the default values configured in the {tekton-hub} API config map is used.
====

. Apply the `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="installing-tekton-hub-with-login-and-rating_{context}"]
= Installing {tekton-hub} with login and rating

[role="_abstract"]
You can install {tekton-hub} on your cluster with custom configuration that supports login with authorization and ratings for {tekton-hub} artifacts.

[discrete]
.Prerequisites
* Ensure that the {pipelines-title} Operator is installed in the default `openshift-pipelines` namespace on the cluster.

[discrete]
.Procedure

. Create an OAuth application with your Git repository hosting provider, and note the Client ID and Client Secret. The supported providers are GitHub, GitLab, and BitBucket.

** For a GitHub OAuth application, set the Homepage URL and the Authorization callback URL as `<auth-route>`.

** For a GitLab OAuth application, set the `REDIRECT_URI` as `<auth-route>/auth/gitlab/callback`.

** For a BitBucket OAuth application, set the `Callback URL` as `<auth-route>`.

. Edit the `<tekton_hub_root>/config/02-api/20-api-secret.yaml` file to include the {tekton-hub} API secrets. For example:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: tekton-hub-api
  namespace: openshift-pipelines
type: Opaque
stringData:
  GH_CLIENT_ID: <1>
  GH_CLIENT_SECRET: <2>
  GL_CLIENT_ID: <3>
  GL_CLIENT_SECRET: <4>
  BB_CLIENT_ID: <5>
  BB_CLIENT_SECRET: <6>
  JWT_SIGNING_KEY: <7>
  ACCESS_JWT_EXPIRES_IN: <8>
  REFRESH_JWT_EXPIRES_IN: <9>
  AUTH_BASE_URL: <10>
  GHE_URL: <11>
  GLE_URL: <12>
----
<1> The Client ID from the GitHub OAuth application.
<2> The Client Secret from the GitHub OAuth application.
<3> The Client ID from the GitLab OAuth application.
<4> The Client Secret from the GitLab OAuth application.
<5> The Client ID from the BitBucket OAuth application.
<6> The Client Secret from the BitBucket OAuth application.
<7> A long, random string used to sign the JSON Web Token (JWT) created for users.
<8> Add the time limit after which the access token expires. For example, `1m`, where m denotes minutes. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`).
<9> Add the time limit after which the refresh token expires. For example, `1m`, where `m` denotes minutes. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`). Ensure that the expiry time set for token refresh is greater than the expiry time set for token access.
<10> Route URL for the OAuth application.
<11> GitHub Enterprise URL, if you are authenticating using GitHub Enterprise. Do not provide the URL to the catalog as a value for this field.
<12> GitLab Enterprise URL, if you are authenticating using GitLab Enterprise. Do not provide the URL to the catalog as a value for this field.
+
[NOTE]
====
You can delete the unused fields for the Git repository hosting service providers that are irrelevant to your deployment.
====

. Create a `TektonHub` CR similar to the following example.
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines <1>
  db: <2>
    secret: tekton-hub-db <3>

  categories: <4>
    - Automation
    - Build Tools
    - CLI
    - Cloud
    - Code Quality
      ...

  catalogs: <5>
    - name: tekton
      org: tektoncd
      type: community
      provider: github
      url: https://github.com/tektoncd/catalog
      revision: main

  scopes: <6>
    - name: agent:create
      users: [<username>]
    - name: catalog:refresh
      users: [<username>]
    - name: config:refresh
      users: [<username>]

  default: <7>
    scopes:
      - rating:read
      - rating:write

  api:
    catalogRefreshInterval: 30m <8>
----
<1> The namespace in which {tekton-hub} must be installed; default is `openshift-pipelines`.
<2> Optional: Custom database, such as a Crunchy Postgres database.
<3> The name of the database secret must be `tekton-hub-db`.
<4> Optional: Customized categories for tasks and pipelines in {tekton-hub}.
<5> Optional: Customized catalogs for {tekton-hub}.
<6> Optional: Additional users. You can metion multiple users, such as `[<username_1>, <username_2>, <username_3>]`.
<7> Optional: Customized default scopes.
<8> The time interval after which the catalog refreshes automatically. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`). The default interval is 30 minutes.
+
[NOTE]
====
If you do not provide custom values for the optional fields in the `TektonHub` CR, the default values configured in the {tekton-hub} API config map is used.
====

. Apply the `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="using-a-custom-database-in-tekton-hub_{context}"]
= Optional: Using a custom database in {tekton-hub}

[role="_abstract"]
Cluster administrators can use a custom database with {tekton-hub}, instead of the default PostgreSQL database installed by the Operator. You can associate a custom database at the time of installation, and use it with the `db-migration`, `api`, and `ui` interfaces provided by {tekton-hub}. Alternatively, you can associate a custom database with {tekton-hub} even after the installation with the default database is complete.

[discrete]
.Procedure

. Create a secret named `tekton-hub-db` in the target namespace with the following keys:
* `POSTGRES_HOST`
* `POSTGRES_DB`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_PORT`
+
.Example: Custom database secrets
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: tekton-hub-db
  labels:
    app: tekton-hub-db
type: Opaque
stringData:
  POSTGRES_HOST: <The name of the host of the database>
  POSTGRES_DB: <Name of the database>
  POSTGRES_USER: <username>
  POSTGRES_PASSWORD: <password>
  POSTGRES_PORT: <The port that the database is listening on>
...
----
+
[NOTE]
====
The default target namespace is `openshift-pipelines`.
====

. In the `TektonHub` CR, set the value of the database secret attribute to `tekton-hub-db`.
+
.Example: Adding custom database secret
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines
  db:
    secret: tekton-hub-db
  api:
    hubConfigUrl: https://raw.githubusercontent.com/tektoncd/hub/main/config.yaml
    catalogRefreshInterval: 30m
...
----

. Use the updated `TektonHub` CR to associate the custom database with {tekton-hub}.

.. If you are associating the custom database at the time of installing {tekton-hub} on your cluster, apply the updated `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

.. Alternatively, if you are associating the custom database after the installation of {tekton-hub} is complete, replace the existing `TektonHub` CR with the updated `TektonHub` CR.
+
[source,terminal]
----
$ oc replace -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="installing-crunchy-postgres-database-and-tekton-hub_{context}"]
= Optional: Installing Crunchy Postgres database and {tekton-hub}

[role="_abstract"]
Cluster administrators can install the Crunchy Postgres database and configure {tekton-hub} to use it instead of the default database.

[discrete]
.Prerequisites

* Install the Crunchy Postgres Operator from the Operator Hub.
* Create a Postgres instance that initiates a Crunchy Postgres database.

[discrete]
.Procedure

. Get into the Crunchy Postgres pod.
+
.Example: Getting into the `test-instance1-m7hh-0` pod
[source,terminal]
----
$ oc exec -it -n openshift-operators test-instance1-m7hh-0 -- /bin/sh

Defaulting container name to database.
Use 'oc describe pod/test-instance1-m7hh-0 -n openshift-operators' to see all of the containers in this pod.
sh-4.4$ psql -U postgres
psql (14.4)
Type "help" for help.
----

. Find the `pg_hba.conf` file.
+
[source,terminal]
----
postgres=# SHOW hba_file;
         hba_file
--------------------------
 /pgdata/pg14/pg_hba.conf
(1 row)

postgres=#
----

. Exit from the database.

. Check if the `pg_hba.conf` file has the entry `host all all 0.0.0.0/0 md5`, required to access all incoming connections. In addition, add the entry at the end of the `pg_hba.conf` file.
+
.Example: `pg_hba.conf` file
[source,terminal]
----
sh-4.4$ cat /pgdata/pg14/pg_hba.conf

# Do not edit this file manually!
# It will be overwritten by Patroni!
local all "postgres" peer
hostssl replication "_crunchyrepl" all cert
hostssl "postgres" "_crunchyrepl" all cert
host all "_crunchyrepl" all reject
hostssl all all all md5
host  all  all 0.0.0.0/0 md5
----

. Save the `pg_hba.conf` file and reload the database.
+
[source,terminal]
----
sh-4.4$ psql -U postgres
psql (14.4)
Type "help" for help.

postgres=# SHOW hba_file;
         hba_file
--------------------------
 /pgdata/pg14/pg_hba.conf
(1 row)

postgres=# SELECT pg_reload_conf();
 pg_reload_conf
----------------
 t
(1 row)
----

. Exit the database.

. Decode the secret value of the Crunchy Postgres host.
+
.Example: Decode the secret value of a Crunchy Postgres host
[source,terminal]
----
$ echo 'aGlwcG8tcHJpbWFyeS5vcGVuc2hpZnQtb3BlcmF0b3JzLnN2YyA=' | base64 --decode
test-primary.openshift-operators.svc
----

. Create a secret named `tekton-hub-db` in the target namespace with the following keys:
* `POSTGRES_HOST`
* `POSTGRES_DB`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_PORT`

+
.Example: Custom database secrets
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: tekton-hub-db
  labels:
    app: tekton-hub-db
type: Opaque
stringData:
  POSTGRES_HOST: test-primary.openshift-operators.svc
  POSTGRES_DB: test
  POSTGRES_USER: <username>
  POSTGRES_PASSWORD: <password>
  POSTGRES_PORT: '5432'
...
----

+
[NOTE]
====
The default target namespace is `openshift-pipelines`.
====

. In the `TektonHub` CR, set the value of the database secret attribute to `tekton-hub-db`.
+
.Example: Adding custom database secret
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines
  db:
    secret: tekton-hub-db
...
----

. Use the updated `TektonHub` CR to associate the custom database with {tekton-hub}.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain a steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="migrating-tekton-hub-data-to-an-existing-crunchy-postgres-database_{context}"]
= Optional: Migrating {tekton-hub} data to an existing Crunchy Postgres database

[role="_abstract"]
{tekton-hub} supports the use of Crunchy Postgres as a custom database. For a preinstalled {tekton-hub} with default database, cluster administrators can use Crunchy Postgres as a custom database after migrating the {tekton-hub} data from the internal or default database to the external Crunchy Postgres database.

[discrete]
.Procedure

. Dump the existing data from the internal or default database into a file in the pod.
+
.Example: Dump data
[source,terminal]
----
$ pg_dump -Ft -h localhost -U postgres hub -f /tmp/hub.dump
----
+
. Copy the file containing the data dump to your local system.
+
.Command format
[source,terminal]
----
$ oc cp -n <namespace> <podName>:<path-to-hub.dump> <path-to-local-system>
----
+
.Example
[source,terminal]
----
$ oc cp -n openshift-pipelines tekton-hub-db-7d6d888c67-p7mdr:/tmp/hub.dump /home/test_user/Downloads/hub.dump
----
+
. Copy the file that contains the data dump from the local system to the pod running the external Crunchy Postgres database.
+
.Command format
[source,terminal]
----
$ oc cp -n <namespace> <path-to-local-system> <podName>:<path-to-hub.dump>
----
+
.Example
[source,terminal]
----
$ oc cp -n openshift-operators /home/test_user/Downloads/hub.dump test-instance1-spnz-0:/tmp/hub.dump
----
+
. Restore the data in the Crunchy Postgres database.
+
.Command format
[source,terminal]
----
$ pg_restore -d <database-name> -h localhost -U postgres <path-where-file-is-copied>
----
+
.Example
[source,terminal]
----
$ pg_restore -d test -h localhost -U postgres /tmp/hub.dump
----
+
. Get into the Crunchy Postgres pod.
.Example: Get into the `test-instance1-m7hh-0` pod
+
[source,terminal]
----
$ oc exec -it -n openshift-operators test-instance1-m7hh-0 -- /bin/sh

Defaulting container name to database.
Use 'oc describe pod/test-instance1-m7hh-0 -n openshift-operators' to see all of the containers in this pod.
sh-4.4$ psql -U postgres
psql (14.4)
Type "help" for help.
----
+
. Find the `pg_hba.conf` file.
+
[source,terminal]
----
postgres=# SHOW hba_file;
         hba_file
--------------------------
 /pgdata/pg14/pg_hba.conf
(1 row)

postgres=#
----
+
. Exit from the database.
+
. Check if the `pg_hba.conf` file has the entry `host all all 0.0.0.0/0 md5`, which is necessary for accessing all incoming connections. If necessary, add the entry at the end of the `pg_hba.conf` file.
+
.Example: `pg_hba.conf` file
[source,terminal]
----
sh-4.4$ cat /pgdata/pg14/pg_hba.conf

# Do not edit this file manually!
# It will be overwritten by Patroni!
local all "postgres" peer
hostssl replication "_crunchyrepl" all cert
hostssl "postgres" "_crunchyrepl" all cert
host all "_crunchyrepl" all reject
hostssl all all all md5
host  all  all 0.0.0.0/0 md5
----
+
. Save the `pg_hba.conf` file and reload the database.
+
[source,terminal]
----
sh-4.4$ psql -U postgres
psql (14.4)
Type "help" for help.

postgres=# SHOW hba_file;
         hba_file
--------------------------
 /pgdata/pg14/pg_hba.conf
(1 row)

postgres=# SELECT pg_reload_conf();
 pg_reload_conf
----------------
 t
(1 row)
----
+
. Exit the database.
. Verify that a secret named `tekton-hub-db` in the target namespace has the following keys:
* `POSTGRES_HOST`
* `POSTGRES_DB`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_PORT`
+
.Example: Custom database secrets
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: tekton-hub-db
  labels:
    app: tekton-hub-db
type: Opaque
stringData:
  POSTGRES_HOST: test-primary.openshift-operators.svc
  POSTGRES_DB: test
  POSTGRES_USER: test
  POSTGRES_PASSWORD: woXOisU5>ocJiTF7y{{;1[Q(
  POSTGRES_PORT: '5432'
...
----
+
[NOTE]
====
The value of the `POSTGRES_HOST` field is encoded as a secret. You can decode the value of the Crunchy Postgres host by using the following example.

.Example: Decode the secret value of a Crunchy Postgres host
[source,terminal]
----
$ echo 'aGlwcG8tcHJpbWFyeS5vcGVuc2hpZnQtb3BlcmF0b3JzLnN2YyA=' | base64 --decode
test-primary.openshift-operators.svc
----
====
+
. Verify that in the `TektonHub` CR, the value of the database secret attribute is `tekton-hub-db`.
+
.Example: TektonHub CR with the name of the database secret
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines
  db:
    secret: tekton-hub-db
...
----
+
. To associate the external Crunchy Postgres database with {tekton-hub}, replace any existing `TektonHub` CR with the updated `TektonHub` CR.
+
[source,terminal]
----
$ oc replace -f <updated-tekton-hub-cr>.yaml
----
+
. Check the status of the {tekton-hub}. The updated `TektonHub` CR might take some time to attain a steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="updating-tekton-hub-with-custom-categories-and-catalogs_{context}"]
= Updating {tekton-hub} with custom categories and catalogs

[role="_abstract"]
Cluster administrators can update Tekton Hub with custom categories, catalogs, scopes, and default scopes that reflect the context of their organization.

[discrete]
.Procedure

. Optional: Edit the `categories`, `catalogs`, `scopes`, and `default:scopes` fields in the Tekton Hub CR.
+
[NOTE]
====
The default information for categories, catalog, scopes, and default scopes are pulled from the {tekton-hub} API config map. If you provide custom values in the `TektonHub` CR, it overrides the default values.
====

. Apply the {tekton-hub} CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Observe the {tekton-hub} status.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                  UIURL
hub    v1.9.0    True             https://api.route.url   https://ui.route.url
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="modifying-catalog-refresh-interval-tekton-hub_{context}"]
= Modifying the catalog refresh interval of {tekton-hub}

[role="_abstract"]
The default catalog refresh interval for {tekton-hub} is 30 minutes. Cluster administrators can modify the automatic catalog refresh interval by modifying the value of the `catalogRefreshInterval` field in the `TektonHub` CR.

[discrete]
.Procedure
. Modify the value of the `catalogRefreshInterval` field in the `TektonHub` CR.
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines <1>
  api:
    catalogRefreshInterval: 30m <2>
----
<1> The namespace where {tekton-hub} is installed; default is `openshift-pipelines`.
<2> The time interval after which the catalog refreshes automatically. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`). The default interval is 30 minutes.

. Apply the `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="adding-new-users-in-tekton-hub-configuration_{context}"]
= Adding new users in {tekton-hub} configuration

[role="_abstract"]
Cluster administrators can add new users to {tekton-hub} with different scopes.

[discrete]
.Procedure
. Modify the `TektonHub` CR to add new users with different scopes.
+
[source,yaml]
----
...
scopes:
  - name: agent:create
    users: [<username_1>, <username_2>] <1>
  - name: catalog:refresh
    users: [<username_3>, <username_4>]
  - name: config:refresh
    users: [<username_5>, <username_6>]

default:
  scopes:
    - rating:read
    - rating:write
...
----
<1> The usernames registered with the Git repository hosting service provider.
+
[NOTE]
====
A new user signing in to {tekton-hub} for the first time will have only the default scope. To activate additional scopes, ensure the user's username is added in the `scopes` field of the `TektonHub` CR.
====

. Apply the updated `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the {tekton-hub}. The updated `TektonHub` CR might take some time to attain a steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----

. Refresh the configuration.
+
[source,terminal]
----
$ curl -X POST -H "Authorization: <access-token>" \ <1>
    --header "Content-Type: application/json" \
    --data '{"force": true} \
    <api-route>/system/config/refresh
----
<1> The JWT token.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

[id="disabling-tekton-hub-authorization-after-upgrade_{context}"]
= Disabling {tekton-hub} authorization after upgrading the {pipelines-title} Operator from 1.7 to 1.8

[role="_abstract"]
When you install {tekton-hub} with {pipelines-title} Operator 1.8, the login authorization and ratings for the {tekton-hub} artifacts are disabled for the default installation. However, when you upgrade the Operator from 1.7 to 1.8, the instance of the {tekton-hub} on your cluster does not automatically disable the login authorization and ratings.

To disable login authorization and ratings for {tekton-hub} after upgrading the Operator from 1.7 to 1.8, perform the steps in the following procedure.

[discrete]
.Prerequisites
* Ensure that the {pipelines-title} Operator is installed in the default `openshift-pipelines` namespace on the cluster.

[discrete]
.Procedure

. Delete the existing {tekton-hub} API secret that you created while manually installing {tekton-hub} for Operator 1.7.
+
[source,terminal]
----
$ oc delete secret tekton-hub-api -n <targetNamespace> <1>
----
<1> The common namespace for the {tekton-hub} API secret and the {tekton-hub} CR. By default, the target namespace is `openshift-pipelines`.

. Delete the `TektonInstallerSet` object for the {tekton-hub} API.
+
[source,terminal]
----
$ oc get tektoninstallerset -o name | grep tekton-hub-api | xargs oc delete
----
+
[NOTE]
====
After deletion, the Operator automatically creates a new {tekton-hub} API installer set.
====
+
Wait and check the status of the {tekton-hub}. Proceed to the next steps when the `READY` column displays `True`.
+
[source,terminal]
----
$ oc get tektonhub hub
----
+
.Sample output
[source,terminal]
----
NAME   VERSION        READY   REASON   APIURL                                                                                                  UIURL
hub    1.8.0          True             https://tekton-hub-api-openshift-pipelines.apps.example.com   https://tekton-hub-ui-openshift-pipelines.apps.example.com

----

. Delete the `ConfigMap` object for the {tekton-hub} UI.
+
[source,terminal]
----
$ oc delete configmap tekton-hub-ui -n <targetNamespace> <1>
----
<1> The common namespace for the {tekton-hub} UI and the {tekton-hub} CR. By default, the target namespace is `openshift-pipelines`.

. Delete the `TektonInstallerSet` object for the {tekton-hub} UI.
+
[source,terminal]
----
$ oc get tektoninstallerset -o name | grep tekton-hub-ui | xargs oc delete
----
+
[NOTE]
====
After deletion, the Operator automatically creates a new {tekton-hub} UI installer set.
====
+
Wait and check the status of the {tekton-hub}. Proceed to the next steps when the `READY` column displays `True`.
+
[source,terminal]
----
$ oc get tektonhub hub
----
+
.Sample output
[source,terminal]
----
NAME   VERSION        READY   REASON   APIURL                                                                                                  UIURL
hub    1.8.0          True             https://tekton-hub-api-openshift-pipelines.apps.example.com   https://tekton-hub-ui-openshift-pipelines.apps.example.com

----

[role="_additional-resources"]
[id="additional-resources-tekton-hub"]
== Additional resources

* GitHub repository of Tekton Hub

* Installing {pipelines-shortname}

* {pipelines-title} release notes
