---
title: "Adding Operators to a cluster"
type: reference
domain: openshift
slug: operators-4-22-olm-adding-operators-to-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-adding-operators-to-cluster
version: 4.22
family: operators
documentKind: "Documentation"
---

# Adding Operators to a cluster

[id="olm-adding-operators-to-a-cluster"]
= Adding Operators to a cluster

// Assembly and included modules watched for changes by Ecosystem Catalog team:
// https://projects.engineering.redhat.com/projects/RHEC/summary

Using Operator Lifecycle Manager (OLM),
cluster administrators can install OLM-based Operators to an OpenShift Container Platform cluster.
administrators with the `dedicated-admin` role can install OLM-based Operators to a OpenShift Container Platform cluster.

[NOTE]
====
For information on how OLM handles updates for installed Operators colocated in the same namespace, as well as an alternative method for installing Operators with custom global Operator groups, see Multitenancy and Operator colocation.
====

[id="olm-adding-operators-to-a-cluster-prereqs"]
== Prerequisites

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

[role="_additional-resources"]
.Additional resources

* Understanding the software catalog

// Installing from OperatorHub by using the CLI
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

[role="_additional-resources"]
.Additional resources

* Manually approving a pending Operator update

// Installing from OperatorHub by using the CLI
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

* About Operator groups
* Installing global Operators in custom namespaces
* Manually approving a pending Operator update

// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-preparing-operators-multitenant_{context}"]
= Preparing for multiple instances of an Operator for multitenant clusters

As a cluster administrator,
As an administrator with the `dedicated-admin` role,
you can add multiple instances of an Operator for use in multitenant clusters. This is an alternative solution to either using the standard *All namespaces* install mode, which can be considered to violate the principle of least privilege, or the *Multinamespace* mode, which is not widely adopted. For more information, see "Operators in multitenant clusters".

In the following procedure, the _tenant_ is a user or group of users that share common access and privileges for a set of deployed workloads. The _tenant Operator_ is the instance of an Operator that is intended for use by only that tenant.

.Prerequisites

* You have access to the cluster as a user with the `dedicated-admin` role.
* All instances of the Operator you want to install must be the same version across a given cluster.
+
[IMPORTANT]
====
For more information on this and other limitations, see "Operators in multitenant clusters".
====

.Procedure

// In OSD/ROSA, dedicated-admins can't create namespaces directly but can create projects.
. Before installing the Operator, create a namespace for the tenant Operator that is separate from the tenant's namespace. For example, if the tenant's namespace is `team1`, you might create a `team1-operator` namespace:

.. Define a `Namespace` resource and save the YAML file, for example, `team1-operator.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: team1-operator
----

.. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create -f team1-operator.yaml
----
// Slightly different step for OSD/ROSA since dedicated-admins can't create namespaces directly.
. Before installing the Operator, create a namespace for the tenant Operator that is separate from the tenant's namespace. You can do this by creating a project. For example, if the tenant's namespace is `team1`, you might create a `team1-operator` project:
+
[source,terminal]
----
$ oc new-project team1-operator
----

. Create an Operator group for the tenant Operator scoped to the tenant's namespace, with only that one namespace entry in the `spec.targetNamespaces` list:

.. Define an `OperatorGroup` resource and save the YAML file, for example, `team1-operatorgroup.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: team1-operatorgroup
  namespace: team1-operator
spec:
  targetNamespaces:
  - team1 <1>
----
<1> Define only the tenant's namespace in the `spec.targetNamespaces` list.

.. Create the Operator group by running the following command:
+
[source,terminal]
----
$ oc create -f team1-operatorgroup.yaml
----

.Next steps

* Install the Operator in the tenant Operator namespace. This task is more easily performed by using the software catalog in the web console instead of the CLI; for a detailed procedure, "Installing from software catalog using the web console".
+
[NOTE]
====
After completing the Operator installation, the Operator resides in the tenant Operator namespace and watches the tenant namespace, but neither the Operator's pod nor its service account are visible or usable by the tenant.
====

[role="_additional-resources"]
.Additional resources

* Operators in multitenant clusters

// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-installing-global-namespaces_{context}"]
= Installing global Operators in custom namespaces

When installing Operators with the OpenShift Container Platform web console, the default behavior installs Operators that support the *All namespaces* install mode into the default `openshift-operators` global namespace. This can cause issues related to shared install plans and update policies between all Operators in the namespace. For more details on these limitations, see "Multitenancy and Operator colocation".

As a cluster administrator,
As an administrator with the `dedicated-admin` role,
you can bypass this default behavior manually by creating a custom global namespace and using that namespace to install your individual or scoped set of Operators and their dependencies.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

// In OSD/ROSA, dedicated-admins can't create namespaces directly but can create projects.
. Before installing the Operator, create a namespace for the installation of your desired Operator. This installation namespace will become the custom global namespace:

.. Define a `Namespace` resource and save the YAML file, for example, `global-operators.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: global-operators
----

.. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create -f global-operators.yaml
----
// Slightly different step for OSD/ROSA since dedicated-admins can't create namespaces directly.
. Before installing the Operator, create a namespace for the installation of your desired Operator. You can do this by creating a project. The namespace for this project will become the custom global namespace:
+
[source,terminal]
----
$ oc new-project global-operators
----

. Create a custom _global Operator group_, which is an Operator group that watches all namespaces:

.. Define an `OperatorGroup` resource and save the YAML file, for example, `global-operatorgroup.yaml`. Omit both the `spec.selector` and `spec.targetNamespaces` fields to make it a _global Operator group_, which selects all namespaces:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: global-operatorgroup
  namespace: global-operators
----
+
[NOTE]
====
The `status.namespaces` of a created global Operator group contains the empty string (`""`), which signals to a consuming Operator that it should watch all namespaces.
====

.. Create the Operator group by running the following command:
+
[source,terminal]
----
$ oc create -f global-operatorgroup.yaml
----

.Next steps

* Install the desired Operator in your custom global namespace. Because the web console does not populate the *Installed Namespace* menu during Operator installation with custom global namespaces, the install task can only be performed with the OpenShift CLI (`oc`). For a detailed installation procedure, see "Installing from OperatorHub by using the CLI".
+
[NOTE]
====
When you initiate the Operator installation, if the Operator has dependencies, the dependencies are also automatically installed in the custom global namespace. As a result, it is then valid for the dependency Operators to have the same update policy and shared install plans.
====

[role="_additional-resources"]
.Additional resources

* Multitenancy and Operator colocation

// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-pod-placement_{context}"]
= Pod placement of Operator workloads

By default, Operator Lifecycle Manager (OLM) places pods on arbitrary worker nodes when installing an Operator or deploying Operand workloads. As an administrator, you can use projects with a combination of node selectors, taints, and tolerations to control the placement of Operators and Operands to specific nodes.

Controlling pod placement of Operator and Operand workloads has the following prerequisites:

. Determine a node or set of nodes to target for the pods per your requirements. If available, note an existing label, such as `node-role.kubernetes.io/app`, that identifies the node or nodes. Otherwise, add a label, such as `myoperator`, by using a compute machine set or editing the node directly. You will use this label in a later step as the node selector on your project.
. If you want to ensure that only pods with a certain label are allowed to run on the nodes, while steering unrelated workloads to other nodes, add a taint to the node or nodes by using a compute machine set or editing the node directly. Use an effect that ensures that new pods that do not match the taint cannot be scheduled on the nodes. For example, a `myoperator:NoSchedule` taint ensures that new pods that do not match the taint are not scheduled onto that node, but existing pods on the node are allowed to remain.
. Create a project that is configured with a default node selector and, if you added a taint, a matching toleration.

At this point, the project you created can be used to steer pods towards the specified nodes in the following scenarios:

For Operator pods::
Administrators can create a `Subscription` object in the project as described in the following section. As a result, the Operator pods are placed on the specified nodes.

For Operand pods::
Using an installed Operator, users can create an application in the project, which places the custom resource (CR) owned by the Operator in the project. As a result, the Operand pods are placed on the specified nodes, unless the Operator is deploying cluster-wide objects or resources in other namespaces, in which case this customized pod placement does not apply.

[role="_additional-resources"]
.Additional resources
* Adding taints and tolerations manually to nodes or with compute machine sets
* Creating project-wide node selectors
* Creating a project with a node selector and toleration

// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-node-affinity.adoc
// * nodes/scheduling/nodes-scheduler-pod-affinity.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-overriding-operator-pod-affinity_{context}"]

= Controlling where an Operator is installed

= Using pod affinity and anti-affinity to control where an Operator is installed

= Using node affinity to control where an Operator is installed

[role="_abstract"]
You can use affinities to schedule an Operator pod on a specific node or set of nodes.

By default, when you install an Operator, OpenShift Container Platform installs the Operator pod on one of your compute nodes randomly. However, the following examples describe situations where you might want to schedule an Operator pod to a specific node or set of nodes:

* If an Operator requires a particular platform, such as `amd64` or `arm64`
* If an Operator requires a particular operating system, such as Linux or Windows
* If you want Operators that work together scheduled on the same host or on hosts located on the same rack
* If you want Operators dispersed throughout the infrastructure to avoid downtime due to network or hardware issues

You can control where an Operator pod is installed by adding node affinity, pod affinity, or pod anti-affinity constraints to the Operator's `Subscription` object. Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. Pod affinity enables you to ensure that related pods are scheduled to the same node. Pod anti-affinity allows you to prevent a pod from being scheduled on a node.

You can control where an Operator pod is installed by adding a pod affinity or anti-affinity to the Operator's `Subscription` object.

You can control where an Operator pod is installed by adding a node affinity constraints to the Operator's `Subscription` object.

The following examples show how to use node affinity or pod anti-affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:
The following examples show how to use node affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:

The following node affinity example places the Operator pod on a specific node:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-163-94.us-west-2.compute.internal
#...
----

This node affinity requires the Operator's pod be scheduled on a node named `ip-10-0-163-94.us-west-2.compute.internal`.

The following node affinity example places the Operator pod on a node with a specific platform:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/arch
              operator: In
              values:
              - arm64
            - key: kubernetes.io/os
              operator: In
              values:
              - linux
#...
----

This node affinity requires the Operator's pod be scheduled on a node with the `kubernetes.io/arch=arm64` and `kubernetes.io/os=linux` labels.

The following example shows how to use pod anti-affinity to prevent the installation the Custom Metrics Autoscaler Operator from any node that has pods with a specific label:

The following pod affinity example places the Operator pod on one or more specific nodes:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - test
          topologyKey: kubernetes.io/hostname
#...
----

This pod affinity places the Operator's pod on a node that has pods with the `app=test` label.

The following pod anti-affinity example prevents the Operator pod from one or more specific nodes:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: cpu
              operator: In
              values:
              - high
          topologyKey: kubernetes.io/hostname
#...
----

This pod anti-affinity prevents the Operator's pod from being scheduled on a node that has pods with the `cpu=high` label.

To control the placement of an Operator pod, complete the following steps.

.Procedure

. Install the Operator as usual.

. If needed, ensure that your nodes are labeled to properly respond to the affinity.

. Edit the Operator `Subscription` object to add an affinity:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-185-229.ec2.internal
#...
----
where:

`spec.config.affinity`:: Specifies a `nodeAffinity`, `podAffinity`, or `podAntiAffinity`. See the Additional resources section that follows for information about creating the affinity.
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-185-229.ec2.internal
#...
----
where:

`spec.config.affinity`:: Specifies a `nodeAffinity`.
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - ip-10-0-185-229.ec2.internal
            topologyKey: topology.kubernetes.io/zone
#...
----
where:

`spec.config.affinity`:: Specifies a `podAffinity` or `podAntiAffinity`.

.Verification

* To ensure that the pod is deployed on the specific node, run the following command:
+
[source,yaml]
----
$ oc get pods -o wide
----
+
.Example output
[source,terminal]
----
NAME                                                  READY   STATUS    RESTARTS   AGE   IP            NODE                           NOMINATED NODE   READINESS GATES
custom-metrics-autoscaler-operator-5dcc45d656-bhshg   1/1     Running   0          50s   10.131.0.20   ip-10-0-185-229.ec2.internal   <none>           <none>
----

[role="_additional-resources"]
.Additional resources

* Understanding pod affinity
* Understanding node affinity
// This xref points to a topic not currently included in the OSD and ROSA docs.
* Understanding how to update labels on nodes
