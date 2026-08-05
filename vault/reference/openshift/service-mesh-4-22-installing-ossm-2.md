---
title: "Installing Service Mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-installing-ossm-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/installing-ossm
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Installing Service Mesh

[id="installing-ossm-v1x"]
= Installing Service Mesh

Installing the {SMProductShortName} involves installing the OpenShift Elasticsearch, Jaeger, Kiali and {SMProductShortName} Operators, creating and managing a `ServiceMeshControlPlane` resource to deploy the control plane, and creating a `ServiceMeshMemberRoll` resource to specify the namespaces associated with the {SMProductShortName}.

[NOTE]
====
Mixer's policy enforcement is disabled by default. You must enable it to run policy tasks. See Update Mixer policy enforcement for instructions on enabling Mixer policy enforcement.
====

[NOTE]
====
Multi-tenant control plane installations are the default configuration.
====

[NOTE]
====
The {SMProductShortName} documentation uses `istio-system` as the example project, but you can deploy the service mesh to any project.
====

== Prerequisites
* Follow the Preparing to install {SMProductName} process.
* An account with the `cluster-admin` role.

The {SMProductShortName} installation process uses the software catalog to install the `ServiceMeshControlPlane` custom resource definition within the `openshift-operators` project. The {SMProductName} defines and monitors the `ServiceMeshControlPlane` related to the deployment, update, and deletion of the control plane.

Starting with {SMProductName} {SMProductVersion1x}, you must install the OpenShift Elasticsearch Operator, the Jaeger Operator, and the Kiali Operator before the {SMProductName} Operator can install the control plane.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc

[id="ossm-operator-install-elasticsearch_{context}"]
= Installing the {es-op}

The default {JaegerName} deployment uses in-memory storage because it is designed to be installed quickly for those evaluating {DTProductName}, giving demonstrations, or using {JaegerName} in a test environment. If you plan to use {JaegerName} in production, you must install and configure a persistent storage option, in this case, Elasticsearch.

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You have access to the cluster as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

[WARNING]
====
Do not install Community versions of the Operators. Community Operators are not supported.
====

[NOTE]
====
If you have already installed the {es-op} as part of OpenShift Logging, you do not need to install the {es-op} again. The {JaegerName} Operator creates the Elasticsearch instance using the installed {es-op}.
====

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

. Navigate to *Ecosystem* -> *Software Catalog*.

. Type *Elasticsearch* into the filter box to locate the {es-op}.

. Click the *{es-op}* provided by Red Hat to display information about the Operator.

. Click *Install*.

. On the *Install Operator* page, select the *stable* Update Channel. This automatically updates your Operator as new versions are released.

. Accept the default *All namespaces on the cluster (default)*. This installs the Operator in the default `openshift-operators-redhat` project and makes the Operator available to all projects in the cluster.
+
[NOTE]
====
The Elasticsearch installation requires the *openshift-operators-redhat* namespace for the {es-op}. The other {DTProductName} Operators are installed in the `openshift-operators` namespace.
====
+

. Accept the default *Automatic* approval strategy. By accepting the default, when a new version of this Operator is available, Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without human intervention. If you select *Manual* updates, when a newer version of an Operator is available, OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the Operator updated to the new version.
+
[NOTE]
====
The *Manual* approval strategy requires a user with appropriate credentials to approve the Operator install and subscription process.
====

. Click *Install*.

. On the *Installed Operators* page, select the `openshift-operators-redhat` project. Wait for the *InstallSucceeded* status of the {es-op} before continuing.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc

[id="ossm-jaeger-operator-install_{context}"]
= Installing the {JaegerOperator} Operator

You can install the {JaegerOperator} Operator through the software catalog.

By default, the Operator is installed in the `openshift-operators` project.

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You have access to the cluster as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.
* If you require persistent storage, you must install the {es-op} before installing the {JaegerOperator} Operator.

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

. Navigate to *Ecosystem* -> *Software Catalog*.

. Search for the {JaegerOperator} Operator by entering *distributed tracing platform* in the search field.

. Select the *{JaegerOperator}* Operator, which is *provided by Red Hat*, to display information about the Operator.

. Click *Install*.

. For the *Update channel* on the *Install Operator* page, select *stable* to automatically update the Operator when new versions are released.
//If you select a maintenance channel, for example, *Stable*, you will receive bug fixes and security patches for the length of the support cycle for that version.

. Accept the default *All namespaces on the cluster (default)*. This installs the Operator in the default `openshift-operators` project and makes the Operator available to all projects in the cluster.

. Accept the default *Automatic* approval strategy.
+
[NOTE]
====
If you accept this default, the Operator Lifecycle Manager (OLM) automatically upgrades the running instance of this Operator when a new version of the Operator becomes available.

If you select *Manual* updates, the OLM creates an update request when a new version of the Operator becomes available. To update the Operator to the new version, you must then manually approve the update request as a cluster administrator. The *Manual* approval strategy requires a cluster administrator to manually approve Operator installation and subscription.
====

. Click *Install*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. On the *Installed Operators* page, select the `openshift-operators` project. Wait for the *Succeeded* status of the {JaegerOperator} Operator before continuing.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-install-kiali_{context}"]
= Installing the Kiali Operator

You must install the Kiali Operator for the {SMProductName} Operator to install the {SMProductShortName} control plane.

[WARNING]
====
Do not install Community versions of the Operators. Community Operators are not supported.
====

.Prerequisites

* Access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Software Catalog*.

. Type *Kiali* into the filter box to find the Kiali Operator.

. Click the *Kiali Operator* provided by Red Hat to display information about the Operator.

. Click *Install*.

. On the *Operator Installation* page, select the *stable* Update Channel.

. Select *All namespaces on the cluster (default)*. This installs the Operator in the default `openshift-operators` project and makes the Operator available to all projects in the cluster.

. Select the *Automatic* Approval Strategy.
+
[NOTE]
====
The Manual approval strategy requires a user with appropriate credentials to approve the Operator install and subscription process.
====

. Click *Install*.

. The *Installed Operators* page displays the Kiali Operator's installation progress.

// Module included in the following assemblies:
//
// - service_mesh/v1x/installing-ossm.adoc
// - service_mesh/v2x/installing-ossm.adoc

[id="ossm-install-ossm-operator_{context}"]
= Installing the Operators

To install {SMProductName}, you must install the {SMProductName} Operator. Repeat the procedure for each additional Operator you want to install.

Additional Operators include:

* {KialiProduct}
* {TempoOperator}

Deprecated additional Operators include:

[IMPORTANT]
====
Starting with {SMProductName} 2.5, {JaegerName} and {es-op} are deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for these features during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to {JaegerName}, you can use {TempoName} instead.
====

* {JaegerName}
* {es-op}

[NOTE]
====
If you have already installed the {es-op} as part of OpenShift {logging-uc}, you do not need to install the {es-op} again. The {JaegerName} Operator creates the Elasticsearch instance using the installed {es-op}.
====

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.
. Log in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

. Type the name of the Operator into the filter box and select the Red Hat version of the Operator. Community versions of the Operators are not supported.

. Click *Install*.

. On the *Install Operator* page for each Operator, accept  the default settings.

. Click *Install*. Wait until the Operator installs before repeating the steps for the next Operator you want to install.
+
* The {SMProductName} Operator installs in the `openshift-operators` namespace and is available for all namespaces in the cluster.
* The {KialiProduct} installs in the `openshift-operators` namespace and is available for all namespaces in the cluster.
* The {TempoOperator} installs in the `openshift-tempo-operator` namespace and is available for all namespaces in the cluster.
* The {JaegerName} installs in the `openshift-distributed-tracing` namespace and is available for all namespaces in the cluster.
+
[IMPORTANT]
====
Starting with {SMProductName} 2.5, {JaegerName} is deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to {JaegerName}, you can use {TempoName} instead.
====
+
* The {es-op} installs in the `openshift-operators-redhat` namespace and is available for all namespaces in the cluster.
+
[IMPORTANT]
====
Starting with {SMProductName} 2.5, {es-op} is deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed.
====

.Verification

* After all you have installed all four Operators, click *Ecosystem* -> *Installed Operators* to verify that your Operators are installed.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc

[id="ossm-control-plane-deploy-1x_{context}"]
= Deploying the {SMProductName} control plane

TODO - Flesh out how multitenancy affects this, link to control plate template topic.

The `ServiceMeshControlPlane` resource defines the configuration to be used during installation. You can deploy the default configuration provided by Red Hat or customize the `ServiceMeshControlPlane` file to fit your business needs.

You can deploy the {SMProductShortName} control plane by using the OpenShift Container Platform web console or from the command line using the `oc` client tool.

[id="ossm-control-plane-deploy-operatorhub_{context}"]
== Deploying the control plane from the web console

Follow this procedure to deploy the {SMProductName} control plane by using the web console.  In this example, `istio-system` is the name of the control plane project.

.Prerequisites

* The {SMProductName} Operator must be installed.
* Review the instructions for how to customize the {SMProductName} installation.
* An account with the `cluster-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Create a project named `istio-system`.

.. Navigate to *Home* -> *Projects*.

.. Click *Create Project*.

.. Enter `istio-system` in the *Name* field.

.. Click *Create*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. If necessary, select `istio-system` from the Project menu.  You may have to wait a few moments for the Operators to be copied to the new project.

. Click the {SMProductName} Operator.  Under *Provided APIs*, the Operator provides links to create two resource types:
** A `ServiceMeshControlPlane` resource
** A `ServiceMeshMemberRoll` resource

. Under *Istio Service Mesh Control Plane* click *Create ServiceMeshControlPlane*.

. On the *Create Service Mesh Control Plane* page, modify the YAML for the default `ServiceMeshControlPlane` template as needed.
+
[NOTE]
====
For additional information about customizing the control plane, see customizing the {SMProductName} installation. For production, you _must_ change the default Jaeger template.
====

. Click *Create* to create the control plane.  The Operator creates pods, services, and {SMProductShortName} control plane components based on your configuration parameters.

. Click the *Istio Service Mesh Control Plane* tab.

. Click the name of the new control plane.

. Click the *Resources* tab to see the {SMProductName} control plane resources the Operator created and configured.

[id="ossm-control-plane-deploy-cli_{context}"]
== Deploying the control plane from the CLI

Follow this procedure to deploy the {SMProductName} control plane the command line.

.Prerequisites

* The {SMProductName} Operator must be installed.
* Review the instructions for how to customize the {SMProductName} installation.
* An account with the `cluster-admin` role.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role.
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
----

. Create a project named `istio-system`.
+
[source,terminal]
----
$ oc new-project istio-system
----

. Create a `ServiceMeshControlPlane` file named `istio-installation.yaml` using the example found in "Customize the {SMProductName} installation". You can customize the values as needed to match your use case.  For production deployments you _must_ change the default Jaeger template.

. Run the following command to deploy the control plane:
+
[source,terminal]
----
$ oc create -n istio-system -f istio-installation.yaml
----
+
. Execute the following command to see the status of the control plane installation.
+
[source,terminal]
----
$ oc get smcp -n istio-system
----
+
The installation has finished successfully when the STATUS column is `ComponentsReady`.
+
----
NAME            READY   STATUS            PROFILES      VERSION   AGE
basic-install   11/11   ComponentsReady   ["default"]   v1.1.18   4m25s
----
+
. Run the following command to watch the progress of the Pods during the installation process:
+
----
$ oc get pods -n istio-system -w
----
+
You should see output similar to the following:
+
.Example output
[source,terminal]
----
NAME                                     READY   STATUS             RESTARTS   AGE
grafana-7bf5764d9d-2b2f6                 2/2     Running            0          28h
istio-citadel-576b9c5bbd-z84z4           1/1     Running            0          28h
istio-egressgateway-5476bc4656-r4zdv     1/1     Running            0          28h
istio-galley-7d57b47bb7-lqdxv            1/1     Running            0          28h
istio-ingressgateway-dbb8f7f46-ct6n5     1/1     Running            0          28h
istio-pilot-546bf69578-ccg5x             2/2     Running            0          28h
istio-policy-77fd498655-7pvjw            2/2     Running            0          28h
istio-sidecar-injector-df45bd899-ctxdt   1/1     Running            0          28h
istio-telemetry-66f697d6d5-cj28l         2/2     Running            0          28h
jaeger-896945cbc-7lqrr                   2/2     Running            0          11h
kiali-78d9c5b87c-snjzh                   1/1     Running            0          22h
prometheus-6dff867c97-gr2n5              2/2     Running            0          28h
----

For a multitenant installation, {SMProductName} supports multiple independent control planes within the cluster.  You can create reusable configurations with `ServiceMeshControlPlane` templates.  For more information, see Creating control plane templates.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-member-roll-create_{context}"]
= Creating the {SMProductName} member roll

The `ServiceMeshMemberRoll` lists the projects that belong to the {SMProductShortName} control plane. Only projects listed in the `ServiceMeshMemberRoll` are affected by the control plane. A project does not belong to a service mesh until you add it to the member roll for a particular control plane deployment.

You must create a `ServiceMeshMemberRoll` resource named `default` in the same project as the `ServiceMeshControlPlane`, for example `istio-system`.

[id="ossm-member-roll-create-console_{context}"]
== Creating the member roll from the web console

You can add one or more projects to the {SMProductShortName} member roll from the web console. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.

.Prerequisites
* An installed, verified {SMProductName} Operator.
* List of existing projects to add to the service mesh.

.Procedure

. Log in to the OpenShift Container Platform web console.

. If you do not already have services for your mesh, or you are starting from scratch, create a project for your applications. It must be different from the project where you installed the {SMProductShortName} control plane.

.. Navigate to *Home* -> *Projects*.

.. Enter a name in the *Name* field.

.. Click *Create*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and choose the project where your `ServiceMeshControlPlane` resource is deployed from the list, for example `istio-system`.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Member Roll* tab.

. Click *Create ServiceMeshMemberRoll*

. Click *Members*, then enter the name of your project in the *Value* field. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource.

. Click *Create*.

[id="ossm-member-roll-create-cli_{context}"]
== Creating the member roll from the CLI

You can add a project to the `ServiceMeshMemberRoll` from the command line.

.Prerequisites

* An installed, verified {SMProductName} Operator.
* List of projects to add to the service mesh.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI.
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
----

. If you do not already have services for your mesh, or you are starting from scratch, create a project for your applications. It must be different from the project where you installed the {SMProductShortName} control plane.
+
[source,terminal]
----
$ oc new-project <your-project>
----

. To add your projects as members, modify the following example YAML. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
.Example servicemeshmemberroll-default.yaml
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  members:
    # a list of projects joined into the service mesh
    - your-project-name
    - another-project-name
----

. Run the following command to upload and create the `ServiceMeshMemberRoll` resource in the `istio-system` namespace.
+
[source,terminal]
----
$ oc create -n istio-system -f servicemeshmemberroll-default.yaml
----

. Run the following command to verify the `ServiceMeshMemberRoll` was created successfully.
+
[source,terminal]
----
$ oc get smmr -n istio-system default
----
+
The installation has finished successfully when the `STATUS` column is `Configured`.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-member-roll-modify_{context}"]
= Adding or removing projects from the service mesh

You can add or remove projects from an existing {SMProductShortName} `ServiceMeshMemberRoll` resource using the web console.

* You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource.

* The `ServiceMeshMemberRoll` resource is deleted when its corresponding `ServiceMeshControlPlane` resource is deleted.

[id="ossm-member-roll-modify-console_{context}"]
== Adding or removing projects from the member roll using the web console

.Prerequisites
* An installed, verified {SMProductName} Operator.
* An existing `ServiceMeshMemberRoll` resource.
* Name of the project with the `ServiceMeshMemberRoll` resource.
* Names of the projects you want to add or remove from the mesh.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and choose the project where your `ServiceMeshControlPlane` resource is deployed from the list, for example `istio-system`.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Member Roll* tab.

. Click the `default` link.

. Click the YAML tab.

. Modify the YAML to add or remove projects as members. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource.

. Click *Save*.

. Click *Reload*.

[id="ossm-member-roll-modify-cli_{context}"]
== Adding or removing projects from the member roll using the CLI

You can modify an existing {SMProductShortName} member roll using the command line.

.Prerequisites

* An installed, verified {SMProductName} Operator.
* An existing `ServiceMeshMemberRoll` resource.
* Name of the project with the `ServiceMeshMemberRoll` resource.
* Names of the projects you want to add or remove from the mesh.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Edit the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc edit smmr -n <controlplane-namespace>
----
+

. Modify the YAML to add or remove projects as members. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource.

+
.Example servicemeshmemberroll-default.yaml

[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system #control plane project
spec:
  members:
    # a list of projects joined into the service mesh
    - your-project-name
    - another-project-name
----

== Manual updates

If you choose to update manually, the Operator Lifecycle Manager (OLM) controls the installation, upgrade, and role-based access control (RBAC) of Operators in a cluster. OLM runs by default in OpenShift Container Platform.
OLM uses CatalogSources, which use the Operator Registry API, to query for available Operators as well as upgrades for installed Operators.

* For more information about how OpenShift Container Platform handled upgrades, refer to the Operator Lifecycle Manager documentation.

// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
// * service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-update-app-sidecar_{context}"]
= Updating sidecar proxies

In order to update the configuration for sidecar proxies the application administrator must restart the application pods.

If your deployment uses automatic sidecar injection, you can update the pod template in the deployment by adding or modifying an annotation. Run the following command to redeploy the pods:

[source,terminal]
----
$ oc patch deployment/<deployment> -p '{"spec":{"template":{"metadata":{"annotations":{"kubectl.kubernetes.io/restartedAt": "'`date -Iseconds`'"}}}}}'
----

If your deployment does not use automatic sidecar injection, you must manually update the sidecars by modifying the sidecar container image specified in the deployment or pod, and then restart the pods.

== Next steps

* Prepare to deploy applications on {SMProductName}.
