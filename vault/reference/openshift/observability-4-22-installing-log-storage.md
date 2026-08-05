---
title: "Installing log storage"
type: reference
domain: openshift
slug: observability-4-22-installing-log-storage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/installing-log-storage
version: 4.22
family: observability
documentKind: "Documentation"
---

# Installing log storage

[id="installing-log-storage"]
= Installing log storage

You can use the {oc-first} or the OpenShift Container Platform web console to deploy a log store on your OpenShift Container Platform cluster.

[id="installing-log-storage-loki"]
== Deploying a Loki log store

You can use the {loki-op} to deploy an internal Loki log store on your OpenShift Container Platform cluster.
After install the {loki-op}, you must configure Loki object storage by creating a secret, and create a `LokiStack` custom resource (CR).

// Module is included in the following assemblies:
// * observability/logging/log_storage/installing-log-storage.adoc
// * network_observability/installing-operators.adoc

[id="loki-deployment-sizing_{context}"]
= Loki deployment sizing

Sizing for Loki follows the format of `1x.<size>` where the value `1x` is number of instances and `<size>` specifies performance capabilities.

[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====

.Loki sizing
[cols="1h,4*",options="header"]
|===
|
|1x.demo
|1x.extra-small
|1x.small
|1x.medium

|Data transfer
|Demo use only
|100GB/day
|500GB/day
|2TB/day

|Queries per second (QPS)
|Demo use only
|1-25 QPS at 200ms
|25-50 QPS at 200ms
|25-75 QPS at 200ms

|Replication factor
|None
|2
|2
|2

|Total CPU requests
|None
|14 vCPUs
|34 vCPUs
|54 vCPUs

|Total CPU requests if using the ruler
|None
|16 vCPUs
|42 vCPUs
|70 vCPUs

|Total memory requests
|None
|31Gi
|67Gi
|139Gi

|Total memory requests if using the ruler
|None
|35Gi
|83Gi
|171Gi

|Total disk requests
|40Gi
|430Gi
|430Gi
|590Gi

|Total disk requests if using the ruler
|80Gi
|750Gi
|750Gi
|910Gi
|===

// Loki console install
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-gui-install_{context}"]
= Installing {logging-uc} and the {loki-op} using the web console

To install and configure logging on your OpenShift Container Platform cluster, an Operator such as {loki-op} for log storage must be installed first. This can be done from the software catalog within the web console.

.Prerequisites

* You have access to a supported object store (AWS S3, {gcp-full} Storage, Azure, Swift, Minio, {rh-storage}).
* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, go to *Ecosystem* -> *Software Catalog*.

. Type {loki-op} in the *Filter by keyword* field. Click *{loki-op}* in the list of available Operators, and then click *Install*.
+
[IMPORTANT]
====
The Community {loki-op} is not supported by Red{nbsp}Hat.
====

. Select *stable* or *stable-x.y* as the *Update channel*.
+
--
--
+
The {loki-op} must be deployed to the global operator group namespace `openshift-operators-redhat`, so the *Installation mode* and *Installed Namespace* are already selected. If this namespace does not already exist, it is created for you.

. Select *Enable Operator-recommended cluster monitoring on this namespace.*
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the `Namespace` object. You must select this option to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. For *Update approval* select *Automatic*, then click *Install*.
+
If the approval strategy in the subscription is set to *Automatic*, the update process initiates as soon as a new Operator version is available in the selected channel. If the approval strategy is set to *Manual*, you must manually approve pending updates.

. Install the Red{nbsp}Hat OpenShift Logging Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Choose  *Red{nbsp}Hat OpenShift Logging* from the list of available Operators, and click *Install*.

.. Ensure that the *A specific namespace on the cluster* is selected under *Installation Mode*.

.. Ensure that *Operator recommended namespace* is *openshift-logging* under *Installed Namespace*.

.. Select *Enable Operator recommended cluster monitoring on this namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object.
You must select this option to ensure that cluster monitoring
scrapes the `openshift-logging` namespace.

.. Select *stable-5.y* as the *Update Channel*.

.. Select an *Approval Strategy*.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

. Go to the *Ecosystem* -> *Installed Operators* page. Click the *All instances* tab.

. From the *Create new* drop-down list, select *LokiStack*.

. Select *YAML view*, and then use the following template to create a `LokiStack` CR:
+
--
.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging # <2>
spec:
  size: 1x.small # <3>
  storage:
    schemas:
    - version: v13
      effectiveDate: "<yyyy>-<mm>-<dd>"
    secret:
      name: logging-loki-s3 # <4>
      type: s3 # <5>
      credentialMode: # <6>
  storageClassName: <storage_class_name> # <7>
  tenants:
    mode: openshift-logging # <8>
----
<1> Use the name `logging-loki`.
<2> You must specify the `openshift-logging` namespace.
<3> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<4> Specify the name of your log store secret.
<5> Specify the corresponding storage type.
<6> Optional field, logging 5.9 and later. Supported user configured values are as follows: static is the default authentication mode available for all supported object storage types using credentials stored in a Secret. token for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. token-cco is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<7> Specify the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
<8> LokiStack defaults to running in multi-tenant mode, which cannot be modified. One tenant is provided for each log type: audit, infrastructure, and application logs. This enables access control for individual users and user groups to different log streams.
--
+
[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====

. Click *Create*.

. Create an OpenShift Logging instance:

.. Switch to the *Administration* -> *Custom Resource Definitions* page.

.. On the *Custom Resource Definitions* page, click *ClusterLogging*.

.. On the *Custom Resource Definition details* page, select *View Instances* from the *Actions* menu.

.. On the *ClusterLoggings* page, click *Create ClusterLogging*.
+
You might have to refresh the page to load the data.

.. In the YAML field, replace the code with the following:
+
--
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance # <1>
  namespace: openshift-logging # <2>
spec:
  collection:
    type: vector
  logStore:
    lokistack:
      name: logging-loki
    retentionPolicy:
      application:
        maxAge: 7d
      audit:
        maxAge: 7d
      infra:
        maxAge: 7d
    type: lokistack
  visualization:
    type: ocp-console
    ocpConsole:
      logsLimit: 15

  managementState: Managed
----
<1> Name must be `instance`.
<2> Namespace must be `openshift-logging`.
--

.Verification

. Go to *Ecosystem* -> *Installed Operators*.
. Make sure the *openshift-logging* project is selected.
. In the *Status* column, verify that you see green checkmarks with *InstallSucceeded* and the text *Up to date*.

[NOTE]
====
An Operator might display a `Failed` status before the installation finishes. If the Operator install completes with an `InstallSucceeded` message, refresh the page.
====
// Module included in the following assemblies:
//
// * list assemblies

[id="loki-create-object-storage-secret-console_{context}"]
= Creating a secret for Loki object storage by using the web console

To configure Loki object storage, you must create a secret. You can create a secret by using the OpenShift Container Platform web console.

.Prerequisites

* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.
* You installed the {loki-op}.

.Procedure

. Go to *Workloads* -> *Secrets* in the *Administrator* perspective of the OpenShift Container Platform web console.

. From the *Create* drop-down list, select *From YAML*.

. Create a secret that uses the `access_key_id` and `access_key_secret` fields to specify your credentials and the `bucketnames`, `endpoint`, and `region` fields to define the object storage location. AWS is used in the following example:
+
.Example `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: logging-loki-s3
  namespace: openshift-logging
stringData:
  access_key_id: AKIAIOSFODNN7EXAMPLE
  access_key_secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  bucketnames: s3-bucket-name
  endpoint: https://s3.eu-central-1.amazonaws.com
  region: eu-central-1
----

[role="_additional-resources"]
.Additional resources
* Loki object storage

[id="installing-log-storage-loki-sts"]
== Deploying a Loki log store on a cluster that uses short-term credentials

For some storage providers, you can use the CCO utility (`ccoctl`) during installation to implement short-term credentials. These credentials are created and managed outside the OpenShift Container Platform cluster. Manual mode with short-term credentials for components.

[NOTE]
====
Short-term credential authentication must be configured during a new installation of {loki-op}, on a cluster that uses this credentials strategy. You cannot configure an existing cluster that uses a different credentials strategy to use this feature.
====

// Module included in the following assemblies:
// * logging/log_storage/installing-log-storage.adoc

[id="logging-identity-federation_{context}"]
= Workload identity federation
Workload identity federation enables authentication to cloud-based log stores using short-lived tokens.

.Prerequisites
* OpenShift Container Platform 4.14 and later
* {logging-uc} 5.9 and later

.Procedure
* If you use the OpenShift Container Platform web console to install the {loki-op}, clusters that use short-lived tokens are automatically detected. You are prompted to create roles and supply the data required for the {loki-op} to create a `CredentialsRequest` object, which populates a secret.

* If you use the {oc-first} to install the {loki-op}, you must manually create a subscription object using the appropriate template for your storage provider, as shown in the following examples. This authentication strategy is only supported for the storage providers indicated.

.Azure sample subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: loki-operator
  namespace: openshift-operators-redhat
spec:
  channel: "stable-5.9"
  installPlanApproval: Manual
  name: loki-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    env:
      - name: CLIENTID
        value: <your_client_id>
      - name: TENANTID
        value: <your_tenant_id>
      - name: SUBSCRIPTIONID
        value: <your_subscription_id>
      - name: REGION
        value: <your_region>
----

.AWS sample subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: loki-operator
  namespace: openshift-operators-redhat
spec:
  channel: "stable-5.9"
  installPlanApproval: Manual
  name: loki-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    env:
    - name: ROLEARN
      value: <role_ARN>
----

// Module included in the following assemblies:
//
// * logging/log_storage/installing-log-storage.adoc

[id="logging-create-loki-cr-console_{context}"]
= Creating a LokiStack custom resource by using the web console

You can create a `LokiStack` custom resource (CR) by using the OpenShift Container Platform web console.

.Prerequisites

* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.
* You installed the {loki-op}.

.Procedure

. Go to the *Ecosystem* -> *Installed Operators* page. Click the *All instances* tab.

. From the *Create new* drop-down list, select *LokiStack*.

. Select *YAML view*, and then use the following template to create a `LokiStack` CR:
// tag::pre-5.9[]
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging
spec:
  size: 1x.small # <2>
  storage:
    schemas:
    - version: v12
      effectiveDate: '2022-06-01'
    secret:
      name: logging-loki-s3 # <3>
      type: s3 # <4>
      credentialMode: static #
  storageClassName: <storage_class_name> # <5>
  tenants:
    mode: openshift-logging
----
<1> Use the name `logging-loki`.
<2> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<3> Specify the secret used for your log storage.
<4> Specify the corresponding storage type.
<5> Enter the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
// end::pre-5.9[]

// tag::5.9[]
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging
spec:
  size: 1x.small # <2>
  storage:
    schemas:
      - effectiveDate: '2023-10-15'
        version: v13
    secret:
      name: logging-loki-s3 # <3>
      type: s3 # <4>
      credentialMode: # <5>
  storageClassName: <storage_class_name> # <6>
  tenants:
    mode: openshift-logging
----
<1> Use the name `logging-loki`.
<2> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<3> Specify the secret used for your log storage.
<4> Specify the corresponding storage type.
<5> Optional field, {logging} 5.9 and later. Supported user configured values are as follows: `static` is the default authentication mode available for all supported object storage types using credentials stored in a Secret. `token` for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. `token-cco` is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<6> Enter the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
// end::5.9[]

// Loki CLI install
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-cli-install_{context}"]
= Installing {logging-uc} and the {loki-op} using the CLI

To install and configure logging on your OpenShift Container Platform cluster, an Operator such as {loki-op} for log storage must be installed first. This can be done from the OpenShift Container Platform CLI.

.Prerequisites

* You have administrator permissions.
* You installed the {oc-first}.
* You have access to a supported object store. For example: AWS S3, {gcp-full} Storage, Azure, Swift, Minio, or {rh-storage}.

.Procedure

--
--

. Create a `Namespace` object for {loki-op}:
+
.Example `Namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-operators-redhat # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true" # <2>
----
<1> You must specify the `openshift-operators-redhat` namespace. To prevent possible conflicts with metrics, you should configure the Prometheus Cluster Monitoring stack to scrape metrics from the `openshift-operators-redhat` namespace and not the `openshift-operators` namespace. The `openshift-operators` namespace might contain community Operators, which are untrusted and could publish a metric with the same name as an OpenShift Container Platform metric, which would cause conflicts.
<2> A string value that specifies the label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object for {loki-op}:
+
.Example `Subscription` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: loki-operator
  namespace: openshift-operators-redhat # <1>
spec:
  channel: stable # <2>
  name: loki-operator
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-operators-redhat` namespace.
<2> Specify `stable`, or `stable-5.<y>` as the channel.
<3> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator Lifecycle Manager (OLM).

. Apply the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `namespace` object for the {clo}:
+
.Example `namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-logging # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-logging: "true"
    openshift.io/cluster-monitoring: "true" # <2>
----
<1> The Red{nbsp}Hat OpenShift Logging Operator is only deployable to the `openshift-logging` namespace.
<2> A string value that specifies the label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create an `OperatorGroup` object
+
.Example `OperatorGroup` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  targetNamespaces:
  - openshift-logging
----
<1> You must specify the `openshift-logging` namespace.

. Apply the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  channel: stable # <2>
  name: cluster-logging
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-logging` namespace.
<2> Specify `stable`, or `stable-5.<y>` as the channel.
<3> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the CatalogSource object you created when you configured the Operator Lifecycle Manager (OLM).

. Apply the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `LokiStack` CR:
+
.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging # <2>
spec:
  size: 1x.small # <3>
  storage:
    schemas:
    - version: v13
      effectiveDate: "<yyyy>-<mm>-<dd>"
    secret:
      name: logging-loki-s3 # <4>
      type: s3 # <5>
      credentialMode: # <6>
  storageClassName: <storage_class_name> # <7>
  tenants:
    mode: openshift-logging # <8>
----
<1> Use the name `logging-loki`.
<2> You must specify the `openshift-logging` namespace.
<3> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<4> Specify the name of your log store secret.
<5> Specify the corresponding storage type.
<6> Optional field, logging 5.9 and later. Supported user configured values are as follows: `static` is the default authentication mode available for all supported object storage types using credentials stored in a Secret. `token` for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. `token-cco` is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<7> Specify the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
<8> LokiStack defaults to running in multi-tenant mode, which cannot be modified. One tenant is provided for each log type: audit, infrastructure, and application logs. This enables access control for individual users and user groups to different log streams.

. Apply the `LokiStack CR` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `ClusterLogging` CR object:
+
.Example ClusterLogging CR object
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance # <1>
  namespace: openshift-logging # <2>
spec:
  collection:
    type: vector
  logStore:
    lokistack:
      name: logging-loki
    retentionPolicy:
      application:
        maxAge: 7d
      audit:
        maxAge: 7d
      infra:
        maxAge: 7d
    type: lokistack
  visualization:
    type: ocp-console
    ocpConsole:
      logsLimit: 15
  managementState: Managed
----
<1> Name must be `instance`.
<2> Namespace must be `openshift-logging`.

. Apply the `ClusterLogging CR` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Verify the installation by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-logging
----
+
.Example output
[source,terminal]
----
$ oc get pods -n openshift-logging
NAME                                               READY   STATUS    RESTARTS   AGE
cluster-logging-operator-fb7f7cf69-8jsbq           1/1     Running   0          98m
collector-222js                                    2/2     Running   0          18m
collector-g9ddv                                    2/2     Running   0          18m
collector-hfqq8                                    2/2     Running   0          18m
collector-sphwg                                    2/2     Running   0          18m
collector-vv7zn                                    2/2     Running   0          18m
collector-wk5zz                                    2/2     Running   0          18m
logging-view-plugin-6f76fbb78f-n2n4n               1/1     Running   0          18m
lokistack-sample-compactor-0                       1/1     Running   0          42m
lokistack-sample-distributor-7d7688bcb9-dvcj8      1/1     Running   0          42m
lokistack-sample-gateway-5f6c75f879-bl7k9          2/2     Running   0          42m
lokistack-sample-gateway-5f6c75f879-xhq98          2/2     Running   0          42m
lokistack-sample-index-gateway-0                   1/1     Running   0          42m
lokistack-sample-ingester-0                        1/1     Running   0          42m
lokistack-sample-querier-6b7b56bccc-2v9q4          1/1     Running   0          42m
lokistack-sample-query-frontend-84fb57c578-gq2f7   1/1     Running   0          42m
----
// Module included in the following assemblies:
//
// * list assemblies

[id="loki-create-object-storage-secret-cli_{context}"]
= Creating a secret for Loki object storage by using the CLI

To configure Loki object storage, you must create a secret. You can do this by using the {oc-first}.

.Prerequisites

* You have administrator permissions.
* You installed the {loki-op}.
* You installed the {oc-first}.

.Procedure

* Create a secret in the directory that contains your certificate and key files by running the following command:
+
[source,terminal]
----
$ oc create secret generic -n openshift-logging <your_secret_name> \
 --from-file=tls.key=<your_key_file>
 --from-file=tls.crt=<your_crt_file>
 --from-file=ca-bundle.crt=<your_bundle_file>
 --from-literal=username=<your_username>
 --from-literal=password=<your_password>
----

[NOTE]
====
Use generic or opaque secrets for best results.
====

.Verification

* Verify that a secret was created by running the following command:
+
[source,terminal]
----
$ oc get secrets
----

[role="_additional-resources"]
.Additional resources
* Loki object storage

// Module included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-create-loki-cr-cli_{context}"]
= Creating a LokiStack custom resource by using the CLI

You can create a `LokiStack` custom resource (CR) by using the {oc-first}.

.Prerequisites

* You have administrator permissions.
* You installed the {loki-op}.
* You installed the {oc-first}.

.Procedure

. Create a `LokiStack` CR:
// tag::pre-5.9[]
+
--
.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  size: 1x.small # <1>
  storage:
    schemas:
    - version: v12
      effectiveDate: "2022-06-01"
    secret:
      name: logging-loki-s3 # <2>
      type: s3 # <3>
  storageClassName: <storage_class_name> # <4>
  tenants:
    mode: openshift-logging
----
<1> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<2> Specify the name of your log store secret.
<3> Specify the type of your log store secret.
<4> Specify the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.

[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====

// end::pre-5.9[]

// tag::5.9[]

.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging
spec:
  size: 1x.small # <2>
  storage:
    schemas:
      - effectiveDate: '2023-10-15'
        version: v13
    secret:
      name: logging-loki-s3 # <3>
      type: s3 # <4>
      credentialMode: # <5>
  storageClassName: <storage_class_name> # <6>
  tenants:
    mode: openshift-logging
----
<1> Use the name `logging-loki`.
<2> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<3> Specify the secret used for your log storage.
<4> Specify the corresponding storage type.
<5> Optional field, {logging} 5.9 and later. Supported user configured values are as follows: `static` is the default authentication mode available for all supported object storage types using credentials stored in a Secret. `token` for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. `token-cco` is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<6> Enter the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
// end::5.9[]

. Apply the `LokiStack` CR by running the following command:

.Verification

* Verify the installation by listing the pods in the `openshift-logging` project by running the following command and observing the output:
+
[source,terminal]
----
$ oc get pods -n openshift-logging
----
+
Confirm that you see several pods for components of the {logging}, similar to the following list:
+
.Example output
[source,terminal]
----
NAME                                           READY   STATUS    RESTARTS   AGE
cluster-logging-operator-78fddc697-mnl82       1/1     Running   0          14m
collector-6cglq                                2/2     Running   0          45s
collector-8r664                                2/2     Running   0          45s
collector-8z7px                                2/2     Running   0          45s
collector-pdxl9                                2/2     Running   0          45s
collector-tc9dx                                2/2     Running   0          45s
collector-xkd76                                2/2     Running   0          45s
logging-loki-compactor-0                       1/1     Running   0          8m2s
logging-loki-distributor-b85b7d9fd-25j9g       1/1     Running   0          8m2s
logging-loki-distributor-b85b7d9fd-xwjs6       1/1     Running   0          8m2s
logging-loki-gateway-7bb86fd855-hjhl4          2/2     Running   0          8m2s
logging-loki-gateway-7bb86fd855-qjtlb          2/2     Running   0          8m2s
logging-loki-index-gateway-0                   1/1     Running   0          8m2s
logging-loki-index-gateway-1                   1/1     Running   0          7m29s
logging-loki-ingester-0                        1/1     Running   0          8m2s
logging-loki-ingester-1                        1/1     Running   0          6m46s
logging-loki-querier-f5cf9cb87-9fdjd           1/1     Running   0          8m2s
logging-loki-querier-f5cf9cb87-fp9v5           1/1     Running   0          8m2s
logging-loki-query-frontend-58c579fcb7-lfvbc   1/1     Running   0          8m2s
logging-loki-query-frontend-58c579fcb7-tjf9k   1/1     Running   0          8m2s
logging-view-plugin-79448d8df6-ckgmx           1/1     Running   0          46s
----

// Loki object storage
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage_{context}"]
= Loki object storage

The {loki-op} supports AWS S3, as well as other S3 compatible object stores such as Minio and {rh-storage}. Azure, GCS, and Swift are also supported.

The recommended nomenclature for Loki storage is `logging-loki-_<your_storage_provider>_`.

The following table shows the `type` values within the `LokiStack` custom resource (CR) for each storage provider. For more information, see the section on your storage provider.

[options="header"]
.Secret type quick reference
|===
| Storage provider          | Secret `type` value
| AWS                       | s3
| Azure                     | azure
| {gcp-full}              | gcs
| Minio                     | s3
| OpenShift Data Foundation | s3
| Swift                     | swift
|===

// create object storage
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage-aws_{context}"]
= AWS storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You created a bucket on AWS.
* You created an AWS IAM Policy and IAM User.

.Procedure

* Create an object storage secret with the name `logging-loki-aws` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-aws \
  --from-literal=bucketnames="<bucket_name>" \
  --from-literal=endpoint="<aws_bucket_endpoint>" \
  --from-literal=access_key_id="<aws_access_key_id>" \
  --from-literal=access_key_secret="<aws_access_key_secret>" \
  --from-literal=region="<aws_region_of_your_bucket>"
----

[id="AWS_storage_STS_{context}"]
== AWS storage for STS enabled clusters

If your cluster has STS enabled, the Cloud Credential Operator (CCO) supports short-term authentication using AWS tokens.

You can create the Loki object storage secret manually by running the following command:
[source,terminal,subs="+quotes"]
----
$ oc -n openshift-logging create secret generic "logging-loki-aws" \
  --from-literal=bucketnames="<s3_bucket_name>" \
  --from-literal=region="<bucket_region>" \
  --from-literal=audience="<oidc_audience>" <1>
----
<1> Optional annotation, default value is `openshift`.
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage-azure_{context}"]
= Azure storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You created a bucket on Azure.

.Procedure

* Create an object storage secret with the name `logging-loki-azure` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-azure \
  --from-literal=container="<azure_container_name>" \
  --from-literal=environment="<azure_environment>" \ # <1>
  --from-literal=account_name="<azure_account_name>" \
  --from-literal=account_key="<azure_account_key>"
----
<1> Supported environment values are `AzureGlobal`, `AzureChinaCloud`, `AzureGermanCloud`, or `AzureUSGovernment`.

[id="azure_storage_workload_id_{context}"]
== Azure storage for {entra-first} enabled clusters

If your cluster has {entra-first} enabled, the Cloud Credential Operator (CCO) supports short-term authentication using {entra-short}.

You can create the Loki object storage secret manually by running the following command:

[source,terminal,subs="+quotes"]
----
$ oc -n openshift-logging create secret generic logging-loki-azure \
--from-literal=environment="<azure_environment>" \
--from-literal=account_name="<storage_account_name>" \
--from-literal=container="<container_name>"
----
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage-gcp_{context}"]
= {gcp-full} storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You created a project on {gcp-first}.
* You created a bucket in the same project.
* You created a service account in the same project for {gcp-short} authentication.

.Procedure

. Copy the service account credentials received from {gcp-short} into a file called `key.json`.

. Create an object storage secret with the name `logging-loki-gcs` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-gcs \
  --from-literal=bucketname="<bucket_name>" \
  --from-file=key.json="<path/to/key.json>"
----
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage-minio_{context}"]
= Minio storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You have Minio deployed on your cluster.
* You created a bucket on Minio.

.Procedure

* Create an object storage secret with the name `logging-loki-minio` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-minio \
  --from-literal=bucketnames="<bucket_name>" \
  --from-literal=endpoint="<minio_bucket_endpoint>" \
  --from-literal=access_key_id="<minio_access_key_id>" \
  --from-literal=access_key_secret="<minio_access_key_secret>"
----
// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc

[id="logging-loki-storage-odf_{context}"]
= {rh-storage} storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You deployed {rh-storage}.
* You configured your {rh-storage} cluster for object storage.

.Procedure

. Create an `ObjectBucketClaim` custom resource in the `openshift-logging` namespace:
+
[source,yaml]
----
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: loki-bucket-odf
  namespace: openshift-logging
spec:
  generateBucketName: loki-bucket-odf
  storageClassName: openshift-storage.noobaa.io
----

. Get bucket properties from the associated `ConfigMap` object by running the following command:
+
[source,terminal]
----
BUCKET_HOST=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_HOST}')
BUCKET_NAME=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_NAME}')
BUCKET_PORT=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_PORT}')
----

. Get bucket access key from the associated secret by running the following command:
+
[source,terminal]
----
ACCESS_KEY_ID=$(oc get -n openshift-logging secret loki-bucket-odf -o jsonpath='{.data.AWS_ACCESS_KEY_ID}' | base64 -d)
SECRET_ACCESS_KEY=$(oc get -n openshift-logging secret loki-bucket-odf -o jsonpath='{.data.AWS_SECRET_ACCESS_KEY}' | base64 -d)
----

. Create an object storage secret with the name `logging-loki-odf` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create -n openshift-logging secret generic logging-loki-odf \
--from-literal=access_key_id="<access_key_id>" \
--from-literal=access_key_secret="<secret_access_key>" \
--from-literal=bucketnames="<bucket_name>" \
--from-literal=endpoint="https://<bucket_host>:<bucket_port>"
----
// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-storage-swift_{context}"]
= Swift storage

.Prerequisites

* You installed the {loki-op}.
* You installed the {oc-first}.
* You created a https://docs.openstack.org/newton/user-guide/cli-swift-create-containers.html[bucket] on Swift.

.Procedure

* Create an object storage secret with the name `logging-loki-swift` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-swift \
  --from-literal=auth_url="<swift_auth_url>" \
  --from-literal=username="<swift_usernameclaim>" \
  --from-literal=user_domain_name="<swift_user_domain_name>" \
  --from-literal=user_domain_id="<swift_user_domain_id>" \
  --from-literal=user_id="<swift_user_id>" \
  --from-literal=password="<swift_password>" \
  --from-literal=domain_id="<swift_domain_id>" \
  --from-literal=domain_name="<swift_domain_name>" \
  --from-literal=container_name="<swift_container_name>"
----

* You can optionally provide project-specific data, region, or both by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-swift \
  --from-literal=auth_url="<swift_auth_url>" \
  --from-literal=username="<swift_usernameclaim>" \
  --from-literal=user_domain_name="<swift_user_domain_name>" \
  --from-literal=user_domain_id="<swift_user_domain_id>" \
  --from-literal=user_id="<swift_user_id>" \
  --from-literal=password="<swift_password>" \
  --from-literal=domain_id="<swift_domain_id>" \
  --from-literal=domain_name="<swift_domain_name>" \
  --from-literal=container_name="<swift_container_name>" \
  --from-literal=project_id="<swift_project_id>" \
  --from-literal=project_name="<swift_project_name>" \
  --from-literal=project_domain_id="<swift_project_domain_id>" \
  --from-literal=project_domain_name="<swift_project_domain_name>" \
  --from-literal=region="<swift_region>"
----

[id="installing-log-storage-es"]
== Deploying an Elasticsearch log store

You can use the {es-op} to deploy an internal Elasticsearch log store on your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying.adoc

[id="logging-es-storage-considerations_{context}"]
= Storage considerations for Elasticsearch

A persistent volume is required for each Elasticsearch deployment configuration. On OpenShift Container Platform this is achieved using persistent volume claims (PVCs).

[NOTE]
====
If you use a local volume for persistent storage, do not use a raw block volume, which is described with `volumeMode: block` in the `LocalVolume` object. Elasticsearch cannot use raw block volumes.
====

The OpenShift Elasticsearch Operator names the PVCs using the Elasticsearch resource name.

Fluentd ships any logs from *systemd journal* and **/var/log/containers/*.log** to Elasticsearch.

Elasticsearch requires sufficient memory to perform large merge operations. If it does not have enough memory, it becomes unresponsive. To avoid this problem, evaluate how much application log data you need, and allocate approximately double that amount of free storage capacity.

By default, when storage capacity is 85% full, Elasticsearch stops allocating new data to the node. At 90%, Elasticsearch attempts to relocate existing shards from that node to other nodes if possible. But if no nodes have a free capacity below 85%, Elasticsearch effectively rejects creating new indices and becomes RED.

[NOTE]
====
These low and high watermark values are Elasticsearch defaults in the current release. You can modify these default values. Although the alerts use the same default values, you cannot change these values in the alerts.
====
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying.adoc

[id="logging-install-es-operator_{context}"]
= Installing the OpenShift Elasticsearch Operator by using the web console

The OpenShift Elasticsearch Operator creates and manages the Elasticsearch cluster used by OpenShift Logging.

.Prerequisites

* Elasticsearch is a memory-intensive application. Each Elasticsearch node needs at least 16GB of memory for both memory requests and limits, unless you specify otherwise in the `ClusterLogging` custom resource.
+
The initial set of OpenShift Container Platform nodes might not be large enough to support the Elasticsearch cluster. You must add additional nodes to the OpenShift Container Platform cluster to run with the recommended or higher memory, up to a maximum of 64GB for each Elasticsearch node.
+
Elasticsearch nodes can operate with a lower memory setting, though this is not recommended for production environments.

* Ensure that you have the necessary persistent storage for Elasticsearch. Note that each Elasticsearch node
requires its own storage volume.
+
[NOTE]
====
If you use a local volume for persistent storage, do not use a raw block volume, which is described with `volumeMode: block` in the `LocalVolume` object. Elasticsearch cannot use raw block volumes.
====

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.
. Click *OpenShift Elasticsearch Operator* from the list of available Operators, and click *Install*.
. Ensure that the *All namespaces on the cluster* is selected under *Installation mode*.
. Ensure that *openshift-operators-redhat* is selected under *Installed Namespace*.
+
You must specify the `openshift-operators-redhat` namespace. The `openshift-operators` namespace might contain Community Operators, which are untrusted and could publish a metric with the same name as OpenShift Container Platform metric, which would cause conflicts.

. Select *Enable operator recommended cluster monitoring on this namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the `Namespace` object. You must select this option to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Select *stable-5.x* as the *Update channel*.
. Select an *Update approval* strategy:
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

. Click *Install*.

.Verification

. Verify that the OpenShift Elasticsearch Operator installed by switching to the *Ecosystem* -> *Installed Operators* page.
. Ensure that *OpenShift Elasticsearch Operator* is listed in all projects with a *Status* of *Succeeded*.
// Module included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="cluster-logging-deploy-es-cli_{context}"]
= Installing the {es-op} by using the CLI

You can use the {oc-first} to install the {es-op}.

.Prerequisites

* Ensure that you have the necessary persistent storage for Elasticsearch. Note that each Elasticsearch node requires its own storage volume.
+
[NOTE]
====
If you use a local volume for persistent storage, do not use a raw block volume, which is described with `volumeMode: block` in the `LocalVolume` object. Elasticsearch cannot use raw block volumes.
====
+
Elasticsearch is a memory-intensive application. By default, OpenShift Container Platform installs three Elasticsearch nodes with memory requests and limits of 16 GB. This initial set of three OpenShift Container Platform nodes might not have enough memory to run Elasticsearch within your cluster. If you experience memory issues that are related to Elasticsearch, add more Elasticsearch nodes to your cluster rather than increasing the memory on existing nodes.

* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in "Obtaining the installation program" in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the `OperatorHub` custom resource (CR) as shown in *Configuring OpenShift Container Platform to use Red Hat Operators*.

* You have administrator permissions.
* You have installed the {oc-first}.

.Procedure

. Create a `Namespace` object as a YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-operators-redhat <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true" <2>
----
<1> You must specify the `openshift-operators-redhat` namespace. To prevent possible conflicts with metrics, configure the Prometheus Cluster Monitoring stack to scrape metrics from the `openshift-operators-redhat` namespace and not the `openshift-operators` namespace. The `openshift-operators` namespace might contain community Operators, which are untrusted and could publish a metric with the same name as
 a ROSA
 an OpenShift Container Platform
metric, which would cause conflicts.
<2> String. You must specify this label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create an `OperatorGroup` object  as a YAML file:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-operators-redhat
  namespace: openshift-operators-redhat <1>
spec: {}
----
<1> You must specify the `openshift-operators-redhat` namespace.

. Apply the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object to subscribe the namespace to the {es-op}:
+
.Example Subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: elasticsearch-operator
  namespace: openshift-operators-redhat <1>
spec:
  channel: stable-x.y <2>
  installPlanApproval: Automatic <3>
  source: redhat-operators <4>
  sourceNamespace: openshift-marketplace
  name: elasticsearch-operator
----
<1> You must specify the `openshift-operators-redhat` namespace.
<2> Specify `stable`, or `stable-x.y` as the channel. See the following note.
<3> `Automatic` allows the Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. `Manual` requires a user with appropriate credentials to approve the Operator update.
<4> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster,
specify the name of the `CatalogSource` object created when you configured the Operator Lifecycle Manager (OLM).
+
[NOTE]
====
Specifying `stable` installs the current version of the latest stable release. Using `stable` with `installPlanApproval: "Automatic"` automatically upgrades your Operators to the latest stable major and minor release.

Specifying `stable-x.y` installs the current minor version of a specific major release. Using `stable-x.y` with `installPlanApproval: "Automatic"` automatically upgrades your Operators to the latest stable minor release within the major release.
====

. Apply the subscription by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
+
The {es-op} is installed to the `openshift-operators-redhat` namespace and copied to each project in the cluster.

.Verification

. Run the following command:
+
[source,terminal]
----
$ oc get csv -n --all-namespaces
----

. Observe the output and confirm that pods for the {es-op} exist in each namespace
+
.Example output
[source,terminal]
----
NAMESPACE                                          NAME                            DISPLAY                            VERSION          REPLACES                        PHASE
default                                            elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
kube-node-lease                                    elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
kube-public                                        elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
kube-system                                        elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
non-destructive-test                               elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
openshift-apiserver-operator                       elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
openshift-apiserver                                elasticsearch-operator.v5.8.1   OpenShift Elasticsearch Operator   5.8.1            elasticsearch-operator.v5.8.0   Succeeded
...
----

// configuring log store in the clusterlogging CR
// Module included in the following assemblies:
//
// * logging/cluster-logging-deploying.adoc
// * logging/cluster-logging-loki.adoc

[id="configuring-log-storage-cr_{context}"]
= Configuring log storage

You can configure which log storage type your {logging} uses by modifying the `ClusterLogging` custom resource (CR).

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo} and an internal log store that is either the LokiStack or Elasticsearch.
* You have created a `ClusterLogging` CR.

.Procedure

. Modify the `ClusterLogging` CR `logStore` spec:
+
.`ClusterLogging` CR example
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
# ...
spec:
# ...
  logStore:
    type: <log_store_type> <1>
    elasticsearch: <2>
      nodeCount: <integer>
      resources: {}
      storage: {}
      redundancyPolicy: <redundancy_type> <3>
    lokistack: <4>
      name: {}
# ...
----
<1> Specify the log store type. This can be either `lokistack` or `elasticsearch`.
<2> Optional configuration options for the Elasticsearch log store.
<3> Specify the redundancy type. This value can be `ZeroRedundancy`, `SingleRedundancy`, `MultipleRedundancy`, or `FullRedundancy`.
<4> Optional configuration options for LokiStack.
+
.Example `ClusterLogging` CR to specify LokiStack as the log store
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance
  namespace: openshift-logging
spec:
  managementState: Managed
  logStore:
    type: lokistack
    lokistack:
      name: logging-loki
# ...
----

. Apply the `ClusterLogging` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
