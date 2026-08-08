---
title: "Using Operator Lifecycle Manager with {microshift-short}"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-operators-olm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-operators-olm
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using Operator Lifecycle Manager with {microshift-short}

[id="microshift-operators-olm"]
= Using Operator Lifecycle Manager with {microshift-short}

[role="_abstract"]
You can use Operator Lifecycle Manager (OLM) with {microshift-short} to install and run optional add-on Operators.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-olm-considerations_{context}"]
= Considerations for using OLM with {microshift-short}

[role="_abstract"]
You must consider the application of Operators and steps to use them when planning which ones you want to use with your {microshift-short} platform.

* Cluster Operators as applied in {ocp} are not used in {microshift-short}.
* You must create your own catalogs for the add-on Operators you want to use with your applications. Catalogs are not provided by default.
** Each catalog must have an accessible `CatalogSource` added to a node, so that the OLM catalog Operator can use the catalog for content.
* You must use the CLI to conduct OLM activities with {microshift-short}. The console and OperatorHub GUIs are not available.
** Use the Operator Package Manager `opm` CLI with a network-connected node, or for building catalogs for custom Operators that use an internal registry.
** To mirror your catalogs and Operators for disconnected or offline nodes, install the oc-mirror OpenShift CLI plugin.

[IMPORTANT]
====
Before using an Operator, verify with the provider that the Operator is supported on OpenShift Container Platform.
====

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-installing-olm-options_{context}"]
= Determining your OLM installation type

[role="_abstract"]
You can install Operator Lifecycle Manager (OLM) for use with {microshift-short} 4.16 or newer versions. There are different ways to install OLM for a {microshift-short} node, depending on your use case.

* You can install the `microshift-olm` RPM at the same time you install the {microshift-short} RPM on {op-system-base-full}.
* You can install the `microshift-olm` on an existing {microshift-short} . Restart the {microshift-short} service after installing OLM for the changes to apply.
* See the following links for specifics on each installation type:
** Installing the Operator Lifecycle Manager (OLM) from an RPM package
** Adding other packages to a blueprint

//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-olm-namespaces_{context}"]
= Namespace use in {microshift-short}

[role="_abstract"]
The `microshift-olm` RPM creates the three default namespaces: one for running Operator Lifecycle Manager (OLM), and two for catalog and Operator installation. You can create additional namespaces as needed for your use case.

[id="microshift-olm-default-namespaces_{context}"]
== Default namespaces

The following table lists the default namespaces and a brief description of how each namespace works.

.Default namespaces created by OLM for {microshift-short}
[cols="2",%autowidth]
|===
|*Default Namespace*
|*Details*

|`openshift-operator-lifecycle-manager`
|The OLM package manager runs in this namespace.

|`openshift-marketplace`
|The global namespace. Empty by default. To make the catalog source to be available globally to users in all namespaces, set the `openshift-marketplace` namespace in the catalog-source YAML.

|`openshift-operators`
|The default namespace where Operators run in {microshift-short}. Operators that reference catalogs in the `openshift-operators` namespace must have the *AllNamespaces* watch scope.
|===

[id="microshift-olm-custom-namespace_{context}"]
== Custom namespaces

If you want to use a catalog and Operator together in a single namespace, then you must create a custom namespace. After you create the namespace, you must create the catalog in that namespace. All Operators running in the custom namespace must have the same single-namespace watch scope.

//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-options-building-operator-catalogs_{context}"]
= About building Operator catalogs

[role="_abstract"]
To use Operator Lifecycle Manager (OLM) with {microshift-short}, you must build custom Operator catalogs that you can then manage with OLM. The standard catalogs that are included with {OCP} are not included with {microshift-short}.

[id="microshift-file-based-olm-catalogs_{context}"]
== File-based Operator catalogs

You can create catalogs for your custom Operators or filter catalogs of widely available Operators. You can combine both methods to create the catalogs needed for your specific use case. To run {microshift-short} with your own Operators and OLM, make a catalog by using the file-based catalog structure. For more information, see the following links:

* Managing custom catalogs
* Example catalog
* `opm` CLI reference

[IMPORTANT]
====
* When adding a catalog source to a cluster, set the `securityContextConfig` value to `restricted` in the `catalogSource.yaml` file. Ensure that your catalog can run with `restricted` permissions. For more information, see:

* Adding a catalog source to a cluster
====

//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-olm-deploy-operators_{context}"]
= How to deploy Operators using OLM

[role="_abstract"]
After you create and deploy your custom catalog, you must create a Subscription custom resource (CR) that can access the catalog and install the Operators you choose. Where Operators run depends on the namespace in which you create the Subscription CR.

[IMPORTANT]
====
Operators that you are managing with Operator Lifecycle Manager (OLM) have a watch scope. For example, some Operators only support watching their own namespace, while others support watching every namespace in the node. All Operators installed in a given namespace must have the same watch scope.
====

[id="microshift-olm-operators-connection-details_{context}"]
== Connectivity and OLM Operator deployment

You can deplpy Operators anywhere a catalog is running.

* For a node that is connected to the internet, mirroring images is not required. Images can be pulled over the network.
* For restricted networks in which {microshift-short} has access to an internal network only, images must be mirrored to an internal registry.
* For use cases in which a {microshift-short} node is completely offline, all images must be embedded into an `osbuild` blueprint or a Containerfile.
//osbuild is removed with RHEL 10/MS 4.21

//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-OLM-deploy-Operators_{context}"]
= Adding OLM-based Operators to a networked node using the global namespace

[role="_abstract"]
To deploy different Operators to different namespaces, follow the basic steps to use configuration files to install an Operator that uses the global namespace.

For a {microshift-short} node that has network connectivity, Operator Lifecycle Manager (OLM) can access sources hosted on remote registries.

[NOTE]
====
To use an Operator installed in a different namespace, or in more than one namespace, make sure that both the catalog source and the Subscription CR that references the Operator are running in the `openshift-marketplace` namespace.
====

.Prerequisites

* The {oc-first} is installed.
* Operator Lifecycle Manager (OLM) is installed.
* You created a custom catalog in the global namespace.

.Procedure

. Confirm that OLM is running by using the following command:
+
[source,terminal]
----
$ oc -n openshift-operator-lifecycle-manager get pod -l app=olm-operator
----
+
.Example output
[source,terminal]
----
NAME                            READY   STATUS    RESTARTS   AGE
olm-operator-85b5c6786-n6kbc    1/1     Running   0          2m24s
----

. Confirm that the OLM catalog Operator is running by using the following command:
+
[source,terminal]
----
$ oc -n openshift-operator-lifecycle-manager get pod -l app=catalog-operator
----
+
.Example output
[source,terminal]
----
NAME                                READY   STATUS    RESTARTS   AGE
catalog-operator-5fc7f857b6-tj8cf   1/1     Running   0          2m33s
----
+
[NOTE]
====
The following steps assume you are using the global namespace, `openshift-marketplace`. The catalog must run in the same namespace as the Operator. The Operator must support the *AllNamespaces* mode.
====

. Create the `CatalogSource` object by using the following example YAML:
+
.Example catalog source YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: operatorhubio-catalog
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  image: quay.io/operatorhubio/catalog:latest
  displayName: Community Operators
  publisher: OperatorHub.io
  grpcPodConfig:
    securityContextConfig: restricted
  updateStrategy:
    registryPoll:
      interval: 60m
----
+
where:

`metadata.namespace`:: Specifies the global namespace. Setting the `metadata.namespace` to `openshift-marketplace` enables the catalog to run in all namespaces. Subscriptions in any namespace can reference catalogs created in the `openshift-marketplace` namespace.

`spec.displayName`:: Specifies that the Community Operators are not installed by default with OLM for {microshift-short}. Listed here for example only.

`grpcPodConfig.securityContextConfig`:: Specifies the value of `securityContextConfig` must be set to `restricted` for {microshift-short}.

. Apply the `CatalogSource` configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<catalog_source.yaml>_
----
+
Replace `_<catalog_-_source.yaml>_` with your catalog source configuration file name. In this example, `catalogsource.yaml` is used.
+
.Example output
[source,terminal]
----
catalogsource.operators.coreos.com/operatorhubio-catalog created
----

. To verify that the catalog source is applied, check for the `READY` state by using the following command:
+
[source,terminal]
----
$ oc describe catalogsources.operators.coreos.com -n openshift-marketplace operatorhubio-catalog
----
+
.Example output
[source,terminal]
----
Name:         operatorhubio-catalog
Namespace:    openshift-marketplace
Labels:       <none>
Annotations:  <none>
API Version:  operators.coreos.com/v1alpha1
Kind:         CatalogSource
Metadata:
  Creation Timestamp:  2024-01-31T09:55:31Z
  Generation:          1
  Resource Version:    1212
  UID:                 4edc1a96-83cd-4de9-ac8c-c269ca895f3e
Spec:
  Display Name:  Community Operators
  Grpc Pod Config:
    Security Context Config:  restricted
  Image:                      quay.io/operatorhubio/catalog:latest
  Publisher:                  OperatorHub.io
  Source Type:                grpc
  Update Strategy:
    Registry Poll:
      Interval:  60m
Status:
  Connection State:
    Address:              operatorhubio-catalog.openshift-marketplace.svc:50051
    Last Connect:         2024-01-31T09:55:57Z
    Last Observed State:  READY
  Registry Service:
    Created At:         2024-01-31T09:55:31Z
    Port:               50051
    Protocol:           grpc
    Service Name:       operatorhubio-catalog
    Service Namespace:  openshift-marketplace
Events:                 <none>
----
+
The `Last Observed State` field reports the status as `READY`.

. Confirm that the catalog source is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-marketplace -l olm.catalogSource=operatorhubio-catalog
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
operatorhubio-catalog-x24nh   1/1     Running   0          59s
----

. Create a Subscription CR configuration file by using the following example YAML:
+
.Example Subscription custom resource YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-cert-manager
  namespace: openshift-operators
spec:
  channel: stable
  name: cert-manager
  source: operatorhubio-catalog
  sourceNamespace: openshift-marketplace
----
+
The `sourceNamespace` field defines the global namespace. Setting the `sourceNamespace` value to `openshift-marketplace` enables Operators to run in multiple namespaces if the catalog also runs in the `openshift-marketplace` namespace.

. Apply the Subscription CR configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<subscription_cr.yaml>_
----
+
Replace `_<subscription_cr.yaml>_` with your Subscription CR filename.
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com/my-cert-manager created
----

. You can create a configuration file for the specific Operand you want to use and apply it now.

.Verification

* Verify that your Operator is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-operators <1>
----
+
`openshift-operators` uses the namespace from the Subscription CR.
+
[NOTE]
====
Allow a minute or two for the Operator start.
====
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-7df8994ddb-4vrkr              1/1     Running   0          19s
cert-manager-cainjector-5746db8fd7-69442   1/1     Running   0          18s
cert-manager-webhook-f858bf58b-748nt       1/1     Running   0          18s
----

//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-olm.adoc

[id="microshift-OLM-deploy-Operators-specific-namespace_{context}"]
= Adding OLM-based Operators to a networked node in a specific namespace

[role="_abstract"]
You can specify a namespace for an Operator for a variety of reasons, such as security and resource isolation. For example, you can specify the namespace `olm-microshift`.

In the following example, the catalog is scoped and available in the global `openshift-marketplace` namespace. The Operator uses content from the global namespace, but runs only in the `olm-microshift` namespace. For a {microshift-short} node that has network connectivity, Operator Lifecycle Manager (OLM) can access sources hosted on remote registries.

[IMPORTANT]
====
All of the Operators installed in a specific namespace must have the same watch scope. In this case, the watch scope is *OwnNamespace*.
====

.Prerequisites

* The {oc-first} is installed.
* Operator Lifecycle Manager (OLM) is installed.
* You have created a custom catalog that is running in the global namespace.

.Procedure

. Confirm that OLM is running by using the following command:
+
[source,terminal]
----
$ oc -n openshift-operator-lifecycle-manager get pod -l app=olm-operator
----
+
.Example output
[source,terminal]
----
NAME                           READY   STATUS    RESTARTS   AGE
olm-operator-85b5c6786-n6kbc   1/1     Running   0          16m
----

. Confirm that the OLM catalog Operator is running by using the following command:
+
[source,terminal]
----
$ oc -n openshift-operator-lifecycle-manager get pod -l app=catalog-operator
----
+
.Example output
[source,terminal]
----
NAME                                READY   STATUS    RESTARTS   AGE
catalog-operator-5fc7f857b6-tj8cf   1/1     Running   0          16m
----

. Create a namespace by using the following example YAML:
+
.Example namespace YAML
[source,YAML]
----
apiVersion: v1
kind: Namespace
metadata:
  name: olm-microshift
----

. Apply the namespace configuration using the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<ns.yaml>_
----
+
Replace `_<ns.yaml>_` with the name of your namespace configuration file. In this example, `olm-microshift` is used.
+
.Example output
[source,terminal]
----
namespace/olm-microshift created
----

. Create the Operator group YAML by using the following example YAML:
+
.Example Operator group YAML
[source,yaml]
----
kind: OperatorGroup
apiVersion: operators.coreos.com/v1
metadata:
  name: og
  namespace: olm-microshift
spec:
  targetNamespaces:
  - olm-microshift
----
+
The `spec.targetNamespaces` field and values can be omitted for Operators using the global namespace.

. Apply the Operator group configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<og.yaml>_
----
+
Replace `_<og.yaml>_` with the name of your operator group configuration file.
+
.Example output
[source,terminal]
----
operatorgroup.operators.coreos.com/og created
----

. Create the `CatalogSource` object by using the following example YAML:
+
.Example catalog source YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: operatorhubio-catalog
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  image: quay.io/operatorhubio/catalog:latest
  displayName: Community Operators
  publisher: OperatorHub.io
  grpcPodConfig:
    securityContextConfig: restricted
  updateStrategy:
    registryPoll:
      interval: 60m
----
+
where:

`metadata.namespace`:: Specifies the global namespace. Setting the `metadata.namespace` to `openshift-marketplace` enables the catalog to run in all namespaces. Subscriptions CRs in any namespace can reference catalogs created in the `openshift-marketplace` namespace.

`spec.displayName`:: Specifies that the Community Operators are not installed by default with OLM for {microshift-short}. Listed here for example only.

`grpcPodConfig.securityContextConfig`:: Specifies the value of `securityContextConfig` must be set to `restricted` for {microshift-short}.

. Apply the `CatalogSource` configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<catalog_source.yaml>_
----
+
Replace `_<catalog_source.yaml>_` with your catalog source configuration file name.

. To verify that the catalog source is applied, check for the `READY` state by using the following command:
+
[source,terminal]
----
$ oc describe catalogsources.operators.coreos.com -n openshift-marketplace operatorhubio-catalog
----
+
.Example output
[source,terminal]
----
Name:         operatorhubio-catalog
Namespace:    openshift-marketplace
Labels:       <none>
Annotations:  <none>
API Version:  operators.coreos.com/v1alpha1
Kind:         CatalogSource
Metadata:
  Creation Timestamp:  2024-01-31T10:09:46Z
  Generation:          1
  Resource Version:    2811
  UID:                 60ce4a36-86d3-4921-b9fc-84d67c28df48
Spec:
  Display Name:  Community Operators
  Grpc Pod Config:
    Security Context Config:  restricted
  Image:                      quay.io/operatorhubio/catalog:latest
  Publisher:                  OperatorHub.io
  Source Type:                grpc
  Update Strategy:
    Registry Poll:
      Interval:  60m
Status:
  Connection State:
    Address:              operatorhubio-catalog.openshift-marketplace.svc:50051
    Last Connect:         2024-01-31T10:10:04Z
    Last Observed State:  READY
  Registry Service:
    Created At:         2024-01-31T10:09:46Z
    Port:               50051
    Protocol:           grpc
    Service Name:       operatorhubio-catalog
    Service Namespace:  openshift-marketplace
Events:                 <none>
----
+
The `Last Observed State` field reports the status as `READY`.

. Confirm that the catalog source is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-marketplace -l olm.catalogSource=operatorhubio-catalog
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
operatorhubio-catalog-j7sc8   1/1     Running   0          43s
----

. Create a Subscription CR configuration file by using the following example YAML:
+
.Example Subscription custom resource YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-gitlab-operator-kubernetes
  namespace: olm-microshift
spec:
  channel: stable
  name: gitlab-operator-kubernetes
  source: operatorhubio-catalog
  sourceNamespace: openshift-marketplace
----
+
where:

`metadata.namespace`:: Specifies the specific namespace. Operators reference the global namespace for content, but run in the `olm-microshift` namespace.

`spec.sourceNamespace`:: Specifies the global namespace. Subscriptions CRs in any namespace can reference catalogs created in the `openshift-marketplace` namespace.

. Apply the Subscription CR configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<subscription_cr.yaml>_
----
+
Replace `_<subscription_cr.yaml>_` with the name of the Subscription CR configuration file.
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com/my-gitlab-operator-kubernetes
----

. You can create a configuration file for the specific Operand you want to use and apply it now.

.Verification

* Verify that your Operator is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n olm-microshift
----
+
The `olm-microshift` uses the namespace from the Subscription CR.
+
[NOTE]
====
Allow a minute or two for the Operator start.
====
+
.Example output
[source,terminal]
----
NAME                                         READY   STATUS    RESTARTS   AGE
gitlab-controller-manager-69bb6df7d6-g7ntx   2/2     Running   0          3m24s
----

[id="Additional-resources_microshift-operators-oc-mirror_{context}"]
[role="_additional-resources"]
== Additional resources

* Operator Lifecycle Manager
* `opm` CLI reference
* Updating installed Operators
* Deleting Operators from a cluster using the CLI
