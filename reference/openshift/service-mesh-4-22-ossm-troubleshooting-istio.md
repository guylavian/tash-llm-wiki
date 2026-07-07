---
title: "Troubleshooting your service mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-troubleshooting-istio
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-troubleshooting-istio
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Troubleshooting your service mesh

[id="ossm-troubleshooting"]
= Troubleshooting your service mesh

This section describes how to identify and resolve common problems in {SMProductName}. Use the following sections to help troubleshoot and debug problems when deploying {SMProductName} on OpenShift Container Platform.

// The following include statements pull in the module files that comprise the assembly.

// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc
// * service_mesh/v2x/ossm-troubleshooting.adoc

[id="ossm-versions_{context}"]
= Understanding Service Mesh versions

In order to understand what version of {SMProductName} you have deployed on your system, you need to understand how each of the component versions is managed.

* *Operator* version - The most current Operator version is {SMProductVersion}. The Operator version number only indicates the version of the currently installed Operator. Because the {SMProductName} Operator supports multiple versions of the {SMProductShortName} control plane, the version of the Operator does not determine the version of your deployed `ServiceMeshControlPlane` resources.
+
[IMPORTANT]
====
Upgrading to the latest Operator version automatically applies patch updates, but does not automatically upgrade your {SMProductShortName} control plane to the latest minor version.
====
+
* *ServiceMeshControlPlane* version - The `ServiceMeshControlPlane` version determines what version of {SMProductName} you are using. The value of the `spec.version` field in the `ServiceMeshControlPlane` resource controls the architecture and configuration settings that are used to install and deploy {SMProductName}. When you create the {SMProductShortName} control plane you can set the version in one of two ways:

** To configure in the Form View, select the version from the *Control Plane Version* menu.

** To configure in the YAML View, set the value for `spec.version` in the YAML file.

Operator Lifecycle Manager (OLM) does not manage {SMProductShortName} control plane upgrades, so the version number for your Operator and `ServiceMeshControlPlane` (SMCP) may not match, unless you have manually upgraded your SMCP.

== Troubleshooting Operator installation

In addition to the information in this section, be sure to review the following topics:

* What are Operators?

* Operator Lifecycle Management concepts.

* OpenShift Operator troubleshooting section.

* OpenShift installation troubleshooting section.

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-validating-operators_{context}"]
= Validating Operator installation

//The Operator installation steps include verifying the Operator status in the OpenShift console.

When you install the {SMProductName} Operators, OpenShift automatically creates the following objects as part of a successful Operator installation:

* config maps
* custom resource definitions
* deployments
* pods
* replica sets
* roles
* role bindings
* secrets
* service accounts
* services

.From the OpenShift Container Platform console

You can verify that the Operator pods are available and running by using the OpenShift Container Platform console.

. Navigate to *Workloads* -> *Pods*.
. Select the `openshift-operators` namespace.
. Verify that the following pods exist and have a status of `running`:
** `istio-operator`
** `jaeger-operator`
** `kiali-operator`
. Select the `openshift-operators-redhat` namespace.
. Verify that the `elasticsearch-operator` pod exists and has a status of `running`.

.From the command line

. Verify the Operator pods are available and running in the `openshift-operators` namespace with the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-operators
----
+
.Example output
[source,terminal]
----
NAME                               READY   STATUS    RESTARTS   AGE
istio-operator-bb49787db-zgr87     1/1     Running   0          15s
jaeger-operator-7d5c4f57d8-9xphf   1/1     Running   0          2m42s
kiali-operator-f9c8d84f4-7xh2v     1/1     Running   0          64s
----
+
. Verify the Elasticsearch operator with the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-operators-redhat
----
+
.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
elasticsearch-operator-d4f59b968-796vq     1/1     Running   0          15s
----

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-troubleshooting-operators_{context}"]
= Troubleshooting service mesh Operators

If you experience Operator issues:

* Verify your Operator subscription status.
* Verify that you did not install a community version of the Operator, instead of the supported Red Hat version.
* Verify that you have the `cluster-admin` role to install {SMProductName}.
* Check for any errors in the Operator pod logs if the issue is related to installation of Operators.

[NOTE]
====
You can install Operators only through the OpenShift console, the software catalog is not accessible from the command line.
====

== Viewing Operator pod logs

You can view Operator logs by using the `oc logs` command. Red Hat may request logs to help resolve support cases.

.Procedure

* To view Operator pod logs, enter the command:
+
[source,terminal]
----
$ oc logs -n openshift-operators <podName>
----
+
For example,
+
[source,terminal]
----
$ oc logs -n openshift-operators istio-operator-bb49787db-zgr87
----

//If your pod fails to start, you may need to use the `--previous` option to see the logs of the last attempt.

== Troubleshooting the control plane

The Service Mesh _control plane_ is composed of Istiod, which consolidates several previous control plane components (Citadel, Galley, Pilot) into a single binary. Deploying the `ServiceMeshControlPlane` also creates the other components that make up {SMProductName} as described in the architecture topic.

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-validating-smcp_{context}"]
= Validating the Service Mesh control plane installation

When you create the {SMProductShortName} control plane, the {SMProductShortName} Operator uses the parameters that you have specified in the `ServiceMeshControlPlane` resource file to do the following:

* Creates the Istio components and deploys the following pods:
** `istiod`
** `istio-ingressgateway`
** `istio-egressgateway`
** `grafana`
** `prometheus`
* Calls the Kiali Operator to create Kaili deployment based on configuration in either the SMCP or the Kiali custom resource.
+
[NOTE]
====
You view the Kiali components under the Kiali Operator, not the {SMProductShortName} Operator.
====
+
* Calls the {JaegerName} Operator to create {JaegerShortName} components based on configuration in either the SMCP or the Jaeger custom resource.
+
[NOTE]
====
You view the Jaeger components under the {JaegerName} Operator and the Elasticsearch components under the Red Hat Elasticsearch Operator, not the {SMProductShortName} Operator.
====
+
.From the OpenShift Container Platform console

You can verify the {SMProductShortName} control plane installation in the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.
. Select the `istio-system` namespace.
. Select the {SMProductName} Operator.
.. Click the *Istio Service Mesh Control Plane* tab.
.. Click the name of your control plane, for example `basic`.
.. To view the resources created by the deployment, click the *Resources* tab. You can use the filter to narrow your view, for example, to check that all the *Pods* have a status of `running`.
.. If the SMCP status indicates any problems, check the `status:` output in the YAML file for more information.

. Navigate back to *Ecosystem* -> *Installed Operators*.
. Select the OpenShift Elasticsearch Operator.
.. Click the *Elasticsearch* tab.
.. Click the name of the deployment, for example `elasticsearch`.
.. To view the resources created by the deployment, click the *Resources* tab. .
.. If the `Status` column any problems, check the `status:` output on the *YAML* tab for more information.

. Navigate back to *Ecosystem* -> *Installed Operators*.
. Select the {JaegerName} Operator.
.. Click the *Jaeger* tab.
.. Click the name of your deployment, for example `jaeger`.
.. To view the resources created by the deployment, click the *Resources* tab.
.. If the `Status` column indicates any problems, check the `status:` output on the *YAML* tab for more information.

. Navigate to *Ecosystem* -> *Installed Operators*.
. Select the Kiali Operator.
.. Click the *Istio Service Mesh Control Plane* tab.
.. Click the name of your deployment, for example `kiali`.
.. To view the resources created by the deployment, click the *Resources* tab.
.. If the `Status` column any problems, check the `status:` output on the *YAML* tab for more information.

.From the command line

. Run the following command to see if the {SMProductShortName} control plane pods are available and running, where `istio-system` is the namespace where you installed the SMCP.
+
[source,terminal]
----
$ oc get pods -n istio-system
----
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
grafana-6776785cfc-6fz7t               2/2     Running   0          102s
istio-egressgateway-5f49dd99-l9ppq     1/1     Running   0          103s
istio-ingressgateway-6dc885c48-jjd8r   1/1     Running   0          103s
istiod-basic-6c9cc55998-wg4zq          1/1     Running   0          2m14s
jaeger-6865d5d8bf-zrfss                2/2     Running   0          100s
kiali-579799fbb7-8mwc8                 1/1     Running   0          46s
prometheus-5c579dfb-6qhjk              2/2     Running   0          115s
----
+
. Check the status of the {SMProductShortName} control plane deployment by using the following command. Replace `istio-system` with the namespace where you deployed the SMCP.
+
[source,terminal]
----
$ oc get smcp -n istio-system
----
+
The installation has finished successfully when the STATUS column is `ComponentsReady`.
+
.Example output
[source,terminal]
----
NAME    READY   STATUS            PROFILES      VERSION   AGE
basic   10/10   ComponentsReady   ["default"]   2.1.3     4m2s
----

+
If you have modified and redeployed your {SMProductShortName} control plane, the status should read `UpdateSuccessful`.
+
.Example output
[source,terminal]
----
NAME            READY     STATUS             TEMPLATE   VERSION   AGE
basic-install   10/10     UpdateSuccessful   default     v1.1     3d16h
----
+
. If the SMCP status indicates anything other than `ComponentsReady` check the `status:` output in the SCMP resource for more information.
+
[source,terminal]
----
$ oc describe smcp <smcp-name> -n <controlplane-namespace>
----
+
.Example output
+
[source,terminal]
----
$ oc describe smcp basic -n istio-system
----
+
. Check the status of the Jaeger deployment with the following command, where `istio-system` is the namespace where you deployed the SMCP.
+
[source,terminal]
----
$ oc get jaeger -n istio-system
----
+
.Example output
[source,terminal]
----
NAME     STATUS    VERSION   STRATEGY   STORAGE   AGE
jaeger   Running   1.30.0    allinone   memory    15m
----
+
. Check the status of the Kiali deployment with the following command, where `istio-system` is the namespace where you deployed the SMCP.
+
[source,terminal]
----
$ oc get kiali -n istio-system
----
+
.Example output
[source,terminal]
----
NAME    AGE
kiali   15m
----

Module included in the following assemblies:
* service_mesh/v2x/ossm-observability.adoc
* service_mesh/v2x/ossm-troubleshooting-istio.adoc

[id="ossm-accessing-kiali-console_{context}"]
= Accessing the Kiali console

You can view your application's topology, health, and metrics in the Kiali console. If your service is experiencing problems, the Kiali console lets you view the data flow through your service. You can view insights about the mesh components at different levels, including abstract applications, services, and workloads. Kiali also provides an interactive graph view of your namespace in real time.

To access the Kiali console you must have {SMProductName} installed, Kiali installed and configured.

The installation process creates a route to access the Kiali console.

If you know the URL for the Kiali console, you can access it directly.  If you do not know the URL, use the following directions.

.Procedure for administrators

. Log in to the OpenShift Container Platform web console with an administrator role.

. Click *Home* -> *Projects*.

. On the *Projects* page, if necessary, use the filter to find the name of your project.

. Click the name of your project, for example, `bookinfo`.

. On the *Project details* page, in the *Launcher* section, click the *Kiali* link.

. Log in to the Kiali console with the same user name and password that you use to access the OpenShift Container Platform console.
+
When you first log in to the Kiali Console, you see the *Overview* page which displays all the namespaces in your service mesh that you have permission to view.
+
If you are validating the console installation and namespaces have not yet been added to the mesh, there might not be any data to display other than `istio-system`.

.Procedure for developers

. Log in to the OpenShift Container Platform web console with a developer role.

. Click *Project*.

. On the *Project Details* page, if necessary, use the filter to find the name of your project.

. Click the name of your project, for example, `bookinfo`.

. On the *Project* page, in the *Launcher* section, click the *Kiali* link.

. Click *Log In With OpenShift*.

Module included in the following assemblies:
* service_mesh/v2x/ossm-observability.adoc
* service_mesh/v2x/ossm-troubleshooting-istio.adoc

[id="ossm-accessing-jaeger-console_{context}"]
= Accessing the Jaeger console

To access the Jaeger console you must have {SMProductName} installed, {JaegerName} installed and configured.

The installation process creates a route to access the Jaeger console.

If you know the URL for the Jaeger console, you can access it directly.  If you do not know the URL, use the following directions.

[IMPORTANT]
====
Starting with {SMProductName} 2.5, {JaegerName} and {es-op} have been deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to {JaegerName}, you can use {TempoName} instead.
====

.Procedure from OpenShift console
. Log in to the OpenShift Container Platform web console as a user with cluster-admin rights. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

. Navigate to *Networking* -> *Routes*.

. On the *Routes* page, select the {SMProductShortName} control plane project, for example `istio-system`, from the *Namespace* menu.
+
The *Location* column displays the linked address for each route.
+
. If necessary, use the filter to find the `jaeger` route.  Click the route *Location* to launch the console.

. Click *Log In With OpenShift*.

.Procedure from Kiali console

. Launch the Kiali console.

. Click *Distributed Tracing* in the left navigation pane.

. Click *Log In With OpenShift*.

.Procedure from the CLI

. Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
----
+
. To query for details of the route using the command line, enter the following command. In this example, `istio-system` is the {SMProductShortName} control plane namespace.
+
[source,terminal]
----
$ oc get route -n istio-system jaeger -o jsonpath='{.spec.host}'
----
+
. Launch a browser and navigate to ``\https://<JAEGER_URL>``, where `<JAEGER_URL>` is the route that you discovered in the previous step.

. Log in using the same user name and password that you use to access the {Product-title} console.

. If you have added services to the service mesh and have generated traces, you can use the filters and *Find Traces* button to search your trace data.
+
If you are validating the console installation, there is no trace data to display.

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-troubleshooting-smcp_{context}"]
= Troubleshooting the Service Mesh control plane

If you are experiencing issues while deploying the Service Mesh control plane,

* Ensure that the `ServiceMeshControlPlane` resource is installed in a project that is separate from your services and Operators. This documentation uses the `istio-system` project as an example, but you can deploy your control plane in any project as long as it is separate from the project that contains your Operators and services.

* Ensure that the `ServiceMeshControlPlane` and `Jaeger` custom resources are deployed in the same project. For example, use the `istio-system` project for both.

//* If you selected to install the Elasticsearch Operator in a specific namespace in the cluster instead of selecting *All namespaces in on the cluster (default)*, then OpenShift could not automatically copy the Operator to the istio-system namespace and the {JaegerName} Operator could not call the Elasticsearch Operator during the installation?

//The steps for deploying the service mesh control plane (SMCP) include verifying the deployment in the OpenShift console.

== Troubleshooting the data plane

The _data plane_ is a set of intelligent proxies that intercept and control all inbound and outbound network communications between services in the service mesh.

{SMProductName} relies on a proxy sidecar within the application’s pod to provide service mesh capabilities to the application.

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-troubleshooting-injection_{context}"]
= Troubleshooting sidecar injection

{SMProductName} does not automatically inject proxy sidecars to pods. You must opt in to sidecar injection.

== Troubleshooting Istio sidecar injection

Check to see if automatic injection is enabled in the Deployment for your application. If automatic injection for the Envoy proxy is enabled, there should be a `sidecar.istio.io/inject:"true"` annotation in the `Deployment` resource under `spec.template.metadata.annotations`.

== Troubleshooting Jaeger agent sidecar injection

Check to see if automatic injection is enabled in the Deployment for your application. If automatic injection for the Jaeger agent is enabled, there should be a `sidecar.jaegertracing.io/inject:"true"` annotation in the `Deployment` resource.

For more information about sidecar injection, see Enabling automatic injection

// Module included in the following assemblies:
// * service_mesh/v2x/-ossm-troubleshooting-istio.adoc

[id="ossm-troubleshooting-proxy_{context}"]
= Troubleshooting Envoy proxy

The Envoy proxy intercepts all inbound and outbound traffic for all services in the service mesh. Envoy also collects and reports telemetry on the service mesh. Envoy is deployed as a sidecar to the relevant service in the same pod.

== Enabling Envoy access logs

Envoy access logs are useful in diagnosing traffic failures and flows, and help with end-to-end traffic flow analysis.

To enable access logging for all istio-proxy containers, edit the `ServiceMeshControlPlane` (SMCP) object to add a file name for the logging output.

.Procedure

. Log in to the OpenShift Container Platform CLI as a user with the cluster-admin role. Enter the following command. Then, enter your username and password when prompted.
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
----
+
. Change to the project where you installed the {SMProductShortName} control plane, for example `istio-system`.
+
[source,terminal]
----
$ oc project istio-system
----
+
. Edit the `ServiceMeshControlPlane` file.
+
[source,terminal]
----
$ oc edit smcp <smcp_name>
----
+
. As show in the following example, use `name` to specify the file name for the proxy log. If you do not specify a value for `name`, no log entries will be written.
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  proxy:
    accessLogging:
      file:
        name: /dev/stdout     #file name
----

For more information about troubleshooting pod issues, see Investigating pod issues

// Module included in the following assemblies:
//
// * security/compliance_operator/co-support.adoc
// * support/getting-support.adoc
// * distr_tracing/distributed-tracing-release-notes.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * osd_architecture/osd-support.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-0.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-1.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-2.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-3.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-4.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-5.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-6.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-7.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-8.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-9.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-3-0.adoc
// * microshift_support/microshift-getting-support.adoc

[id="support_{context}"]
= Getting support

[role="_abstract"]
If you experience difficulty with a procedure described in this documentation, or with OpenShift Container Platform in general, visit the Red Hat Customer Portal.

From the Customer Portal, you can:

* Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.
* Submit a support case to Red Hat Support.
* Access other product documentation.

To identify issues with your cluster, you can use {red-hat-lightspeed} in {cluster-manager-url}. {red-hat-lightspeed} provides details about issues and, if available, information on how to solve a problem.

// TODO: verify that these settings apply for Service Mesh and OpenShift virtualization, etc.
If you have a suggestion for improving this documentation or have found an
error, submit a Jira issue for the most relevant documentation component. Please provide specific details, such as the section name and OpenShift Container Platform version.

// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * microshift_support/microshift-getting-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-knowledgebase-about_{context}"]
= About the Red Hat Knowledgebase

[role="_abstract"]
The Red{nbsp}Hat Knowledgebase provides rich content aimed at helping you make the most of Red{nbsp}Hat's products and technologies. The Red{nbsp}Hat Knowledgebase consists of articles, product documentation, and videos outlining best practices on installing, configuring, and using Red Hat products. In addition, you can search for solutions to known issues, each providing concise root cause descriptions and remedial steps.

// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * microshift_support/microshift-getting-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-knowledgebase-search_{context}"]
= Searching the Red Hat Knowledgebase

[role="_abstract"]
In the event of an OpenShift Container Platform issue, you can perform an initial search to determine if a solution already exists within the Red Hat Knowledgebase.

.Prerequisites

* You have a Red Hat Customer Portal account.

.Procedure

. Log in to the Red Hat Customer Portal.

. Click *Search*.

. In the search field, input keywords and strings relating to the problem, including:
+
* OpenShift Container Platform components (such as *etcd*)
* Related procedure (such as *installation*)
* Warnings, error messages, and other outputs related to explicit failures

. Click the *Enter* key.

. Optional: Select the *OpenShift Container Platform* product filter.

. Optional: Select the *Documentation* content type filter.

// Module included in the following assemblies:
//
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * service_mesh/v2x/servicemesh-release-notes.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc

[id="ossm-about-collecting-ossm-data_{context}"]
= About collecting service mesh data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, including features and objects associated with {SMProductName}.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

* The OpenShift Container Platform CLI (`oc`) installed.

.Procedure

. To collect {SMProductName} data with `must-gather`, you must specify the {SMProductName} image.
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:{MaistraVersion}
----
+
. To collect {SMProductName} data for a specific {SMProductShortName} control plane namespace with `must-gather`, you must specify the {SMProductName} image and namespace. In this example, after `gather,` replace `<namespace>` with your {SMProductShortName} control plane namespace, such as `istio-system`.
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:{MaistraVersion} gather <namespace>
----
+
This creates a local directory that contains the following items:

* The Istio Operator namespace and its child objects
* All control plane namespaces and their children objects
* All namespaces and their children objects that belong to any service mesh
* All Istio custom resource definitions (CRD)
* All Istio CRD objects, such as VirtualServices, in a given namespace
* All Istio webhooks

For prompt support, supply diagnostic information for both OpenShift Container Platform and {SMProductName}.

// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-submitting-a-case_{context}"]
= Submitting a support case

[role="_abstract"]
Submit a support case to Red Hat Support to get help with issues you encounter with OpenShift Container Platform.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have access to the {cluster-manager-first}.
* You have a Red Hat Customer Portal account.
* You have a Red Hat Standard or Premium subscription.

.Procedure

. Log in to the *Customer Support* page of the Red Hat Customer Portal.

. Click *Get support*.

. On the *Cases* tab of the *Customer Support* page:

.. Optional: Change the pre-filled account and owner details if needed.

.. Select the appropriate category for your issue, such as *Bug or Defect*, and click *Continue*.

. Enter the following information:

.. In the *Summary* field, enter a concise but descriptive problem summary and further details about the symptoms being experienced, as well as your expectations.

.. Select *OpenShift Container Platform* from the *Product* drop-down menu.

.. Select ** from the *Version* drop-down.

. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. If the suggested articles do not address the issue, click *Continue*.

. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. The list is refined as you provide more information during the case creation process. If the suggested articles do not address the issue, click *Continue*.

. Ensure that the account information presented is as expected, and if not, amend accordingly.

. Check that the autofilled OpenShift Container Platform Cluster ID is correct. If it is not, manually obtain your cluster ID.
+
* To manually obtain your cluster ID using {cluster-manager-url}:
.. Navigate to *Cluster List*.
.. Click on the name of the cluster you need to open a support case for.
.. Find the value in the *Cluster ID* field of the *Details* section of the *Overview* tab.
+
* To manually obtain your cluster ID using the OpenShift Container Platform web console:
.. Navigate to *Home* -> *Overview*.
.. Find the value in the *Cluster ID* field of the *Details* section.
+
* Alternatively, it is possible to open a new support case through the OpenShift Container Platform web console and have your cluster ID autofilled.
.. From the toolbar, navigate to *(?) Help* -> *Open Support Case*.
.. The *Cluster ID* value is autofilled.
+
* To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command:
+
[source,terminal]
----
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
----

. Complete the following questions where prompted and then click *Continue*:
+
* What are you experiencing? What are you expecting to happen?
* Define the value or impact to you or the business.
* Where are you experiencing this behavior? What environment?
* When does this behavior occur? Frequency? Repeatedly? At certain times?

. Upload relevant diagnostic data files and click *Continue*.
It is recommended to include data gathered using the `oc adm must-gather` command as a starting point, plus any issue specific data that is not collected by that command.

. Input relevant case management details and click *Continue*.

. Preview the case details and click *Submit*.
