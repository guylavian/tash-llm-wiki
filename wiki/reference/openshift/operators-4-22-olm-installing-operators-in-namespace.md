---
title: "Installing Operators in your namespace"
type: reference
domain: openshift
slug: operators-4-22-olm-installing-operators-in-namespace
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-installing-operators-in-namespace
version: 4.22
family: operators
documentKind: "Documentation"
---

# Installing Operators in your namespace

[id="olm-installing-operators-in-namespace"]
= Installing Operators in your namespace

If a cluster administrator has delegated Operator installation permissions to your account, you can install and subscribe an Operator to your namespace in a self-service manner.

[id="olm-installing-operators-in-namespace-prereqs"]
== Prerequisites

* A cluster administrator must add certain permissions to your OpenShift Container Platform user account to allow self-service Operator installation to a namespace. See Allowing non-cluster administrators to install Operators for details.

* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the `OperatorHub` custom resource (CR) as shown in _Configuring OpenShift Container Platform to use Red Hat Operators_.

// Module included in the following assemblies:
//
// * operators/user/olm-installing-operators-in-namespace.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc
// * post_installation_configuration/preparing-for-users.adoc
//
// Module watched for changes by Ecosystem Catalog team:
// https://projects.engineering.redhat.com/projects/RHEC/summary

[id="olm-installing-operators-from-software-catalog_{context}"]
= About Operator installation from the software catalog

The software catalog is a user interface for discovering Operators; it works in conjunction with Operator Lifecycle Manager (OLM), which installs and manages Operators on a cluster.

As a cluster administrator, you can install an Operator from the software catalog by using the OpenShift Container Platform
web console or CLI. Subscribing an Operator to one or more namespaces makes the Operator available to developers on your cluster.

As a `dedicated-admin`, you can install an Operator from the software catalog by using the OpenShift Container Platform web console or CLI. Subscribing an Operator to one or more namespaces makes the Operator available to developers on your cluster.

As a user with the proper permissions, you can install an Operator from the software catalog by using the OpenShift Container Platform web console or CLI.

During installation, you must determine the following initial settings for the Operator:

Installation Mode:: Choose *All namespaces on the cluster (default)* to have the Operator installed on all namespaces or choose individual namespaces, if available, to only install the Operator on selected namespaces. This example chooses *All namespaces...* to make the Operator available to all users and projects.
Installation Mode:: Choose a specific namespace in which to install the Operator.

Update Channel:: If an Operator is available through multiple channels, you can choose which channel you want to subscribe to. For example, to deploy from the *stable* channel, if available, select it from the list.

Approval Strategy:: You can choose automatic or manual updates.
+
If you choose automatic updates for an installed Operator, when a new version of that Operator is available in the selected channel, Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without human intervention.
+
If you select manual updates, when a newer version of an Operator is available, OLM creates an update request. As a
cluster administrator,
`dedicated-admin`,
you must then manually approve that update request to have the Operator updated to the new version.

* Understanding the software catalog

// Module included in the following assemblies:
//
// * operators/user/olm-installing-operators-in-namespace.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc
// * post_installation_configuration/preparing-for-users.adoc
//
// Module watched for changes by Ecosystem Catalog team:
// https://projects.engineering.redhat.com/projects/RHEC/summary

// Add additional ifevals here, but before context == olm-adding-operators-to-a-cluster
//ifeval::["{context}" != "olm-adding-operators-to-a-cluster"]

// Keep this ifeval last

[id="olm-installing-from-software-catalog-using-web-console_{context}"]
= Installing from the software catalog by using the web console

You can install and subscribe to an Operator from software catalog by using the OpenShift Container Platform web console.

.Prerequisites

* Access to an OpenShift Container Platform cluster using an account with
`cluster-admin` permissions.
the `dedicated-admin` role.

* Access to an OpenShift Container Platform cluster using an account with Operator installation permissions.

.Procedure

. Navigate in the web console to the *Ecosystem* -> *Software Catalog* page.

. Scroll or type a keyword into the *Filter by keyword* box to find the Operator you want. For example, type `{filter-type}` to find the {filter-operator} Operator.
+
You can also filter options by *Infrastructure Features*. For example, select *Disconnected* if you want to see Operators that work in disconnected environments, also known as restricted network environments.

. Select the Operator to display additional information.
+
[NOTE]
====
Choosing a Community Operator warns that Red Hat does not certify Community Operators; you must acknowledge the warning before continuing.
====

. Read the information about the Operator and click *Install*.

. On the *Install Operator* page, configure your Operator installation:

.. If you want to install a specific version of an Operator, select an *Update channel* and *Version* from the lists. You can browse the various versions of an Operator across any channels it might have, view the metadata for that channel and version, and select the exact version you want to install.
+
[NOTE]
====
The version selection defaults to the latest version for the channel selected. If the latest version for the channel is selected, the *Automatic* approval strategy is enabled by default. Otherwise, *Manual* approval is required when not installing the latest version for the selected channel.

Installing an Operator with *Manual* approval causes all Operators installed within the namespace to function with the *Manual* approval strategy and all Operators are updated together. If you want to update Operators independently, install Operators into separate namespaces.
====

.. Confirm the installation mode for the Operator:
*** *All namespaces on the cluster (default)* installs the Operator in the default `openshift-operators` namespace to watch and be made available to all namespaces in the cluster. This option is not always available.
*** *A specific namespace on the cluster* allows you to choose a specific, single namespace in which to install the Operator. The Operator will only watch and be made available for use in this single namespace.
.. Choose a specific, single namespace in which to install the Operator. The Operator will only watch and be made available for use in this single namespace.

.. For clusters on cloud providers with token authentication enabled:
+
--
* If the cluster uses {aws-short} {sts-full} (*STS Mode* in the web console), enter the Amazon Resource Name (ARN) of the AWS IAM role of your service account in the *role ARN* field. To create the role's ARN, follow the procedure described in Preparing AWS account.
.. For clusters on cloud providers with token authentication enabled:
+
--
* If the cluster uses {aws-short} {sts-full} (*STS Mode* in the web console), enter the Amazon Resource Name (ARN) of the AWS IAM role of your service account in the *role ARN* field. To create the role's ARN, follow the procedure described in Preparing AWS account.

* If the cluster uses {entra-first} (*Workload Identity / Federated Identity Mode* in the web console), add the client ID, tenant ID, and subscription ID in the appropriate fields.

* If the cluster uses {gcp-wid-first} (*{gcp-wid-short} / Federated Identity Mode* in the web console), add the project number, pool ID, provider ID, and service account email in the appropriate fields.
--

.. For *Update approval*, select either the *Automatic* or *Manual* approval strategy.
+
[IMPORTANT]
====
If the web console shows that the cluster uses {aws-short} {sts-short}, {entra-first}, or {gcp-wid-short}, you must set *Update approval* to *Manual*.

Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update.
====

. Click *Install* to make the Operator available to the selected namespaces on this OpenShift Container Platform cluster:

.. If you selected a *Manual* approval strategy, the upgrade status of the subscription remains *Upgrading* until you review and approve the install plan.
+
After approving on the *Install Plan* page, the subscription upgrade status moves to *Up to date*.

.. If you selected an *Automatic* approval strategy, the upgrade status should resolve to *Up to date* without intervention.

.Verification

* After the upgrade status of the subscription is *Up to date*, select *Ecosystem* -> *Installed Operators* to verify that the cluster service version (CSV) of the installed Operator eventually shows up. The *Status* should eventually resolve to *Succeeded* in the relevant namespace.
+
[NOTE]
====
For the *All namespaces...* installation mode, the status resolves to *Succeeded* in the `openshift-operators` namespace, but the status is *Copied* if you check in other namespaces.
====
+
If it does not:

** Check the logs in any pods in the `openshift-operators` project (or other relevant namespace if *A specific namespace...* installation mode was selected) on the *Workloads* -> *Pods* page that are reporting issues to troubleshoot further.

* When the Operator is installed, the metadata indicates which channel and version are installed.
+
[NOTE]
====
The *Channel* and *Version* dropdown menus are still available for viewing other version metadata in this catalog context.
====

// Module included in the following assemblies:
//
// * operators/user/olm-installing-operators-in-namespace.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc
// * post_installation_configuration/preparing-for-users.adoc
//
// Module watched for changes by Ecosystem Catalog team:
// https://projects.engineering.redhat.com/projects/RHEC/summary

[id="olm-installing-operator-from-software-catalog-using-cli_{context}"]
= Installing from the software catalog by using the CLI

Instead of using the OpenShift Container Platform web console, you can install an Operator from the software catalog by using the CLI. Use the `oc` command to create or update a `Subscription` object.

For `SingleNamespace` install mode, you must also ensure an appropriate Operator group exists in the related namespace. An Operator group, defined by an `OperatorGroup` object, selects target namespaces in which to generate required RBAC access for all Operators in the same namespace as the Operator group.

[TIP]
====
In most cases, the web console method of this procedure is preferred because it automates tasks in the background, such as handling the creation of `OperatorGroup` and `Subscription` objects automatically when choosing `SingleNamespace` mode.
====

.Prerequisites

* Access to your OpenShift Container Platform cluster using an account with
`cluster-admin` permissions.
the `dedicated-admin` role.

* Access to your OpenShift Container Platform cluster using an account with Operator installation permissions.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. View the list of Operators available to the cluster from the software catalog:
+
[source,terminal]
----
$ oc get packagemanifests -n openshift-marketplace
----
+
.Example output
[%collapsible]
====
[source,terminal]
----
NAME                               CATALOG               AGE
3scale-operator                    Red Hat Operators     91m
advanced-cluster-management        Red Hat Operators     91m
amq7-cert-manager                  Red Hat Operators     91m
# ...
couchbase-enterprise-certified     Certified Operators   91m
crunchy-postgres-operator          Certified Operators   91m
mongodb-enterprise                 Certified Operators   91m
# ...
etcd                               Community Operators   91m
jaeger                             Community Operators   91m
kubefed                            Community Operators   91m
# ...
----
====
+
Note the catalog for your desired Operator.

. Inspect your desired Operator to verify its supported install modes and available channels:
+
[source,terminal]
----
$ oc describe packagemanifests <operator_name> -n openshift-marketplace
----
+
.Example output
[%collapsible]
====
[source,terminal]
----
# ...
Kind:         PackageManifest
# ...
      Install Modes: <1>
        Supported:  true
        Type:       OwnNamespace
        Supported:  true
        Type:       SingleNamespace
        Supported:  false
        Type:       MultiNamespace
        Supported:  true
        Type:       AllNamespaces
# ...
    Entries:
      Name:       example-operator.v3.7.11
      Version:    3.7.11
      Name:       example-operator.v3.7.10
      Version:    3.7.10
    Name:         stable-3.7 <2>
# ...
   Entries:
      Name:         example-operator.v3.8.5
      Version:      3.8.5
      Name:         example-operator.v3.8.4
      Version:      3.8.4
    Name:           stable-3.8 <2>
  Default Channel:  stable-3.8 <3>
----
<1> Indicates which install modes are supported.
<2> Example channel names.
<3> The channel selected by default if one is not specified.
====
+
[TIP]
====
You can print an Operator's version and channel information in YAML format by running the following command:

[source,terminal]
----
$ oc get packagemanifests <operator_name> -n <catalog_namespace> -o yaml
----
====

. If more than one catalog is installed in a namespace, run the following command to look up the available versions and channels of an Operator from a specific catalog:
+
[source,terminal]
----
$ oc get packagemanifest \
   --selector=catalog=<catalogsource_name> \
   --field-selector metadata.name=<operator_name> \
   -n <catalog_namespace> -o yaml
----
+
[IMPORTANT]
====
If you do not specify the Operator's catalog, running the `oc get packagemanifest` and `oc describe packagemanifest` commands might return a package from an unexpected catalog if the following conditions are met:

* Multiple catalogs are installed in the same namespace.
* The catalogs contain the same Operators or Operators with the same name.
====

. If the Operator you intend to install supports the `AllNamespaces` install mode, and you choose to use this mode, skip this step, because the `openshift-operators` namespace already has an appropriate Operator group in place by default, called `global-operators`.
+
If the Operator you intend to install supports the `SingleNamespace` install mode, and you choose to use this mode, you must ensure an appropriate Operator group exists in the related namespace. If one does not exist, you can create create one by following these steps:
+
[IMPORTANT]
====
You can only have one Operator group per namespace. For more information, see "Operator groups".
====
+
.. Create an `OperatorGroup` object YAML file, for example `operatorgroup.yaml`, for `SingleNamespace` install mode:
+
.Example `OperatorGroup` object for `SingleNamespace` install mode
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: <operatorgroup_name>
  namespace: <namespace> <1>
spec:
  targetNamespaces:
  - <namespace> <1>
----
<1> For `SingleNamespace` install mode, use the same `<namespace>` value for both the `metadata.namespace` and `spec.targetNamespaces` fields.
+
.. Create the `OperatorGroup` object:
+
[source,terminal]
----
$ oc apply -f operatorgroup.yaml
----

. Create a `Subscription` object to subscribe a namespace to an Operator:
+
.. Create a YAML file for the `Subscription` object, for example `subscription.yaml`:
+
[NOTE]
====
If you want to subscribe to a specific version of an Operator, set the `startingCSV` field to the desired version and set the `installPlanApproval` field to `Manual` to prevent the Operator from automatically upgrading if a later version exists in the catalog. For details, see the following "Example `Subscription` object with a specific starting Operator version".
====
+
.Example `Subscription` object
[%collapsible]
====
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: <subscription_name>
  namespace: <namespace_per_install_mode> <1>
spec:
  channel: <channel_name> <2>
  name: <operator_name> <3>
  source: <catalog_name> <4>
  sourceNamespace: <catalog_source_namespace> <5>
  config:
    env: <6>
    - name: ARGS
      value: "-v=10"
    envFrom: <7>
    - secretRef:
        name: license-secret
    volumes: <8>
    - name: <volume_name>
      configMap:
        name: <configmap_name>
    volumeMounts: <9>
    - mountPath: <directory_name>
      name: <volume_name>
    tolerations: <10>
    - operator: "Exists"
    resources: <11>
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    nodeSelector: <12>
      foo: bar
----
<1> For default `AllNamespaces` install mode usage, specify the `openshift-operators` namespace. Alternatively, you can specify a custom global namespace, if you have created one. For `SingleNamespace` install mode usage, specify the relevant single namespace.
<2> Name of the channel to subscribe to.
<3> Name of the Operator to subscribe to.
<4> Name of the catalog source that provides the Operator.
<5> Namespace of the catalog source. Use `openshift-marketplace` for the default software catalog sources.
<6> The `env` parameter defines a list of environment variables that must exist in all containers in the pod created by OLM.
<7> The `envFrom` parameter defines a list of sources to populate environment variables in the container.
<8> The `volumes` parameter defines a list of volumes that must exist on the pod created by OLM.
<9> The `volumeMounts` parameter defines a list of volume mounts that must exist in all containers in the pod created by OLM. If a `volumeMount` references a `volume` that does not exist, OLM fails to deploy the Operator.
<10> The `tolerations` parameter defines a list of tolerations for the pod created by OLM.
<11> The `resources` parameter defines resource constraints for all the containers in the pod created by OLM.
<12> The `nodeSelector` parameter defines a `NodeSelector` for the pod created by OLM.
====
+
.Example `Subscription` object with a specific starting Operator version
[%collapsible]
====
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: example-operator
  namespace: example-operator
spec:
  channel: stable-3.7
  installPlanApproval: Manual <1>
  name: example-operator
  source: custom-operators
  sourceNamespace: openshift-marketplace
  startingCSV: example-operator.v3.7.10 <2>
----
<1> Set the approval strategy to `Manual` in case your specified version is superseded by a later version in the catalog. This plan prevents an automatic upgrade to a later version and requires manual approval before the starting CSV can complete the installation.
<2> Set a specific version of an Operator CSV.
====
+
.. For clusters on cloud providers with token authentication enabled, such as {aws-first} {sts-first}, {entra-first}, or {gcp-wid-first}, configure your `Subscription` object by following these steps:
+
... Ensure the `Subscription` object is set to manual update approvals:
+
.Example `Subscription` object with manual update approvals
[%collapsible]
====
[source,yaml]
----
kind: Subscription
# ...
spec:
  installPlanApproval: Manual <1>
----
<1> Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update.
====
+
... Include the relevant cloud provider-specific fields in the `Subscription` object's `config` section:
+
If the cluster is in AWS STS mode, include the following fields:
+
.Example `Subscription` object with {aws-short} {sts-short} variables
[%collapsible]
====
[source,yaml]
----
kind: Subscription
# ...
spec:
  config:
    env:
    - name: ROLEARN
      value: "<role_arn>" <1>
----
<1> Include the role ARN details.
====
+
If the cluster is in {entra-short} mode, include the following fields:
+
.Example `Subscription` object with {entra-short} variables
[%collapsible]
====
[source,yaml]
----
kind: Subscription
# ...
spec:
 config:
   env:
   - name: CLIENTID
     value: "<client_id>" <1>
   - name: TENANTID
     value: "<tenant_id>" <2>
   - name: SUBSCRIPTIONID
     value: "<subscription_id>" <3>
----
<1> Include the client ID.
<2> Include the tenant ID.
<3> Include the subscription ID.
====
+
If the cluster is in {gcp-wid-short} mode, include the following fields:
+
.Example `Subscription` object with {gcp-wid-short} variables
[%collapsible]
====
[source,yaml]
----
kind: Subscription
# ...
spec:
 config:
   env:
   - name: AUDIENCE
     value: "<audience_url>" <1>
   - name: SERVICE_ACCOUNT_EMAIL
     value: "<service_account_email>" <2>
----
====
+
where:
+
`<audience>`:: Created in {gcp-short} by the administrator when they set up {gcp-wid-short}, the `AUDIENCE` value must be a preformatted URL in the following format:
+
[source,text]
----
//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/<pool_id>/providers/<provider_id>
----
`<service_account_email>`:: The `SERVICE_ACCOUNT_EMAIL` value is a {gcp-short} service account email that is impersonated during Operator operation, for example:
+
[source,text]
----
<service_account_name>@<project_id>.iam.gserviceaccount.com
----
+
.. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f subscription.yaml
----

. If you set the `installPlanApproval` field to `Manual`, manually approve the pending install plan to complete the Operator installation. For more information, see "Manually approving a pending Operator update".

At this point, OLM is now aware of the selected Operator. A cluster service version (CSV) for the Operator should appear in the target namespace, and APIs provided by the Operator should be available for creation.

.Verification

. Check the status of the `Subscription` object for your installed Operator by running the following command:
+
[source,terminal]
----
$ oc describe subscription <subscription_name> -n <namespace>
----

. If you created an Operator group for `SingleNamespace` install mode, check the status of the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc describe operatorgroup <operatorgroup_name> -n <namespace>
----

[role="_additional-resources"]
.Additional resources

* Operator groups
* Channel names

[role="_additional-resources"]
.Additional resources

* Manually approving a pending Operator update
