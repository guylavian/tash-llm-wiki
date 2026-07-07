---
title: "Enabling sidecar injection"
type: reference
domain: openshift
slug: service-mesh-4-22-prepare-to-deploy-applications-ossm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/prepare-to-deploy-applications-ossm
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Enabling sidecar injection

[id="deploying-applications-ossm-v1x"]
= Deploying applications on Service Mesh

When you deploy an application into the {SMProductShortName}, there are several differences between the behavior of applications in the upstream community version of Istio and the behavior of applications within a {SMProductName} installation.

== Prerequisites

* Review Comparing {SMProductName} and upstream Istio community installations

* Review Installing {SMProductName}

// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-control-plane-templates-1x_{context}"]
= Creating control plane templates

You can create reusable configurations with `ServiceMeshControlPlane` templates. Individual users can extend the templates they create with their own configurations. Templates can also inherit configuration information from other templates. For example, you can create an accounting control plane for the accounting team and a marketing control plane for the marketing team. If you create a development template and a production template, members of the marketing team and the accounting team can extend the development and production templates with team specific customization.

When you configure control plane templates, which follow the same syntax as the `ServiceMeshControlPlane`, users inherit settings in a hierarchical fashion. The Operator is delivered with a `default` template with default settings for {SMProductName}. To add custom templates you must create a ConfigMap named `smcp-templates` in the `openshift-operators` project and mount the ConfigMap in the Operator container at `/usr/local/share/istio-operator/templates`.

[id="ossm-create-configmap_{context}"]
== Creating the ConfigMap
TODO
Write a  ConfigMap overview/definition

Follow this procedure to create the ConfigMap.

.Prerequisites

* An installed, verified {SMProductShortName} Operator.
* An account with the `cluster-admin` role.
* Location of the Operator deployment.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI as a cluster administrator.

. From the CLI, run this command to create the ConfigMap named `smcp-templates` in the `openshift-operators` project and replace `<templates-directory>` with the location of the `ServiceMeshControlPlane` files on your local disk:
+
[source,terminal]
----
$ oc create configmap --from-file=<templates-directory> smcp-templates -n openshift-operators
----

. Locate the Operator ClusterServiceVersion name.
+
[source,terminal]
----
$ oc get clusterserviceversion -n openshift-operators | grep 'Service Mesh'
----
+
.Example output
[source,terminal]
----
maistra.v1.0.0            Red Hat OpenShift Service Mesh   1.0.0                Succeeded
----

. Edit the Operator cluster service version to instruct the Operator to use the `smcp-templates` ConfigMap.
+
[source,terminal]
----
$ oc edit clusterserviceversion -n openshift-operators maistra.v1.0.0
----

. Add a volume mount and volume to the Operator deployment.
+
[source,yaml]
----
deployments:
  - name: istio-operator
    spec:
      template:
        spec:
          containers:
            volumeMounts:
              - name: discovery-cache
                mountPath: /home/istio-operator/.kube/cache/discovery
              - name: smcp-templates
                mountPath: /usr/local/share/istio-operator/templates/
          volumes:
            - name: discovery-cache
              emptyDir:
                medium: Memory
            - name: smcp-templates
              configMap:
                name: smcp-templates
...
----
. Save your changes and exit the editor.

. You can now use the `template` parameter in the `ServiceMeshControlPlane` to specify a template.
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
metadata:
  name: minimal-install
spec:
  template: default
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
// * service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-automatic-sidecar-injection_{context}"]
= Enabling automatic sidecar injection

When deploying an application, you must opt-in to injection by configuring the label `sidecar.istio.io/inject` in `spec.template.metadata.labels` to `true` in the `deployment` object. Opting in ensures that the sidecar injection does not interfere with other OpenShift Container Platform features such as builder pods used by numerous frameworks within the OpenShift Container Platform ecosystem.

.Prerequisites

* Identify the namespaces that are part of your service mesh and the deployments that need automatic sidecar injection.

.Procedure

. To find your deployments use the `oc get` command.
+
[source,terminal]
----
$ oc get deployment -n <namespace>
----
+
For example, to view the `Deployment` YAML file for the 'ratings-v1' microservice in the `bookinfo` namespace, use the following command to see the resource in YAML format.
+
[source,terminal]
----
oc get deployment -n bookinfo ratings-v1 -o yaml
----
+
. Open the application's `Deployment` YAML file in an editor.

. Add `spec.template.metadata.labels.sidecar.istio/inject` to your Deployment YAML file and set `sidecar.istio.io/inject` to `true` as shown in the following example.
+
.Example snippet from bookinfo deployment-ratings-v1.yaml
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ratings-v1
  namespace: bookinfo
  labels:
    app: ratings
    version: v1
spec:
  template:
    metadata:
      labels:
        sidecar.istio.io/inject: 'true'
----
+
[NOTE]
====
Using the `annotations` parameter when enabling automatic sidecar injection is deprecated and is replaced by using the `labels` parameter.
====
+
. Save the `Deployment` YAML file.

. Add the file back to the project that contains your app.
+
[source,terminal]
----
$ oc apply -n <namespace> -f deployment.yaml
----
+
In this example, `bookinfo` is the name of the project that contains the `ratings-v1` app and `deployment-ratings-v1.yaml` is the file you edited.
+
[source,terminal]
----
$ oc apply -n bookinfo -f deployment-ratings-v1.yaml
----
+
. To verify that the resource uploaded successfully, run the following command.
+
[source,terminal]
----
$ oc get deployment -n <namespace> <deploymentName> -o yaml
----
+
For example,
+
[source,terminal]
----
$ oc get deployment -n bookinfo ratings-v1 -o yaml
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
// * service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-sidecar-injection-env-var_{context}"]
= Setting proxy environment variables through annotations

Configuration for the Envoy sidecar proxies is managed by the `ServiceMeshControlPlane`.

You can set environment variables for the sidecar proxy for applications by adding pod annotations to the deployment in the `injection-template.yaml` file. The environment variables are injected to the sidecar.

.Example injection-template.yaml
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource
spec:
  replicas: 7
  selector:
    matchLabels:
      app: resource
  template:
    metadata:
      annotations:
        sidecar.maistra.io/proxyEnv: "{ \"maistra_test_env\": \"env_value\", \"maistra_test_env_2\": \"env_value_2\" }"
----

[WARNING]
====
You should never include `maistra.io/` labels and annotations when creating your own custom resources.  These labels and annotations indicate that the resources are generated and managed by the Operator. If you are copying content from an Operator-generated resource when creating your own resources, do not include labels or annotations that start with `maistra.io/`.  Resources that include these labels or annotations will be overwritten or deleted by the Operator during the next reconciliation.
====

// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-mixer-policy-1x_{context}"]
= Updating Mixer policy enforcement

In previous versions of {SMProductName}, Mixer's policy enforcement was enabled by default. Mixer policy enforcement is now disabled by default. You must enable it before running policy tasks.

.Prerequisites
* Access to the OpenShift CLI (`oc`).

[NOTE]
====
The examples use `istio-system` as the control plane namespace. Replace this value with the namespace where you deployed the Service Mesh Control Plane (SMCP).
====

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Run this command to check the current Mixer policy enforcement status:
+
[source,terminal]
----
$ oc get cm -n istio-system istio -o jsonpath='{.data.mesh}' | grep disablePolicyChecks
----

. If `disablePolicyChecks: true`, edit the {SMProductShortName} ConfigMap:
+
[source,terminal]
----
$ oc edit cm -n istio-system istio
----

. Locate `disablePolicyChecks: true` within the ConfigMap and change the value to `false`.

. Save the configuration and exit the editor.

. Re-check the Mixer policy enforcement status to ensure it is set to `false`.

This CONCEPT module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-config-network-policy_{context}"]

== Setting the correct network policy

{SMProductShortName} creates network policies in the {SMProductShortName} control plane and member namespaces to allow traffic between them. Before you deploy, consider the following conditions to ensure the services in your service mesh that were previously exposed through an OpenShift Container Platform route.

* Traffic into the service mesh must always go through the ingress-gateway for Istio to work properly.
* Deploy services external to the service mesh in separate namespaces that are not in any service mesh.
* Non-mesh services that need to be deployed within a service mesh enlisted namespace should label their deployments `maistra.io/expose-route: "true"`, which ensures OpenShift Container Platform routes to these services still work.

This CONCEPT module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-tutorial-bookinfo-overview_{context}"]
= Bookinfo example application

The Bookinfo example application allows you to test your {SMProductName} {SMProductVersion} installation on OpenShift Container Platform.

The Bookinfo application displays information about a book, similar to a single catalog entry of an online book store. The application displays a page that describes the book, book details (ISBN, number of pages, and other information), and book reviews.

The Bookinfo application consists of these microservices:

* The `productpage` microservice calls the `details` and `reviews` microservices to populate the page.
* The `details` microservice contains book information.
* The `reviews` microservice contains book reviews. It also calls the `ratings` microservice.
* The `ratings` microservice contains book ranking information that accompanies a book review.

There are three versions of the reviews microservice:

* Version v1 does not call the `ratings` Service.
* Version v2 calls the `ratings` Service and displays each rating as one to five black stars.
* Version v3 calls the `ratings` Service and displays each rating as one to five red stars.

This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-tutorial-bookinfo-install_{context}"]
= Installing the Bookinfo application

This tutorial walks you through how to create a sample application by creating a project, deploying the Bookinfo application to that project, and viewing the running application in {SMProductShortName}.

.Prerequisites

* OpenShift Container Platform 4.1 or higher installed.
* {SMProductName} {SMProductVersion} installed.
* Access to the OpenShift CLI (`oc`).
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

[NOTE]
====
The Bookinfo sample application cannot be installed on {ibm-z-name} and {ibm-power-name}.
====

[NOTE]
====
The commands in this section assume the {SMProductShortName} control plane project is `istio-system`.  If you installed the control plane in another namespace, edit each command before you run it.
====

.Procedure

. Click *Home* -> *Projects*.

. Click *Create Project*.

. Enter `bookinfo` as the *Project Name*, enter a *Display Name*, and enter a *Description*, then click *Create*.
+
** Alternatively, you can run this command from the CLI to create the `bookinfo` project.
+
[source,terminal]
----
$ oc new-project bookinfo
----
+
. Click *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and use the {SMProductShortName} control plane namespace. In this example, use `istio-system`.

. Click the *{SMProductName}* Operator.

. Click the *Istio Service Mesh Member Roll* tab.

.. If you have already created a Istio Service Mesh Member Roll, click the name, then click the YAML tab to open the YAML editor.

.. If you have not created a `ServiceMeshMemberRoll`, click *Create ServiceMeshMemberRoll*.
+
. Click *Members*, then enter the name of your project in the *Value* field.
+
. Click *Create* to save the updated Service Mesh Member Roll.
+
.. Or, save the following example to a YAML file.
+
.Bookinfo ServiceMeshMemberRoll example servicemeshmemberroll-default.yaml
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
spec:
  members:
  - bookinfo
----
+
.. Run the following command to upload that file and create the `ServiceMeshMemberRoll` resource in the `istio-system` namespace.   In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
$ oc create -n istio-system -f servicemeshmemberroll-default.yaml
----
+
. Run the following command to verify the `ServiceMeshMemberRoll` was created successfully.
+
[source,terminal]
----
$ oc get smmr -n istio-system -o wide
----
+
The installation has finished successfully when the `STATUS` column is `Configured`.
+
[source,terminal]
----
NAME      READY   STATUS       AGE   MEMBERS
default   1/1     Configured   70s   ["bookinfo"]
----
. From the CLI, deploy the Bookinfo application in the _`bookinfo`_ project by applying the `bookinfo.yaml` file:
+
[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/platform/kube/bookinfo.yaml
----
+
You should see output similar to the following:
+
[source,terminal]
----
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
----
+
. Create the ingress gateway by applying the `bookinfo-gateway.yaml` file:
+
[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/bookinfo-gateway.yaml
----
+
You should see output similar to the following:
+
[source,terminal]
----
gateway.networking.istio.io/bookinfo-gateway created
virtualservice.networking.istio.io/bookinfo created
----
+
. Set the value for the `GATEWAY_URL` parameter:
+
[source,terminal]
----
$ export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
----

This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-tutorial-bookinfo-adding-destination-rules_{context}"]
= Adding default destination rules

Before you can use the Bookinfo application, you must first add default destination rules. There are two preconfigured YAML files, depending on whether or not you enabled mutual transport layer security (TLS) authentication.

.Procedure

. To add destination rules, run one of the following commands:
** If you did not enable mutual TLS:
+

[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/destination-rule-all.yaml
----
+
** If you enabled mutual TLS:
+

[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/destination-rule-all-mtls.yaml
----
+
You should see output similar to the following:
+
[source,terminal]
----
destinationrule.networking.istio.io/productpage created
destinationrule.networking.istio.io/reviews created
destinationrule.networking.istio.io/ratings created
destinationrule.networking.istio.io/details created
----

This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-tutorial-bookinfo-verify-install_{context}"]
= Verifying the Bookinfo installation

To confirm that the sample Bookinfo application was successfully deployed, perform the following steps.

.Prerequisites

* {SMProductName} installed.
* Complete the steps for installing the Bookinfo sample app.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure from CLI

. Verify that all pods are ready with this command:
+
[source,terminal]
----
$ oc get pods -n bookinfo
----
+
All pods should have a status of `Running`. You should see output similar to the following:
+
[source,terminal]
----
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-55b869668-jh7hb        2/2     Running   0          12m
productpage-v1-6fc77ff794-nsl8r   2/2     Running   0          12m
ratings-v1-7d7d8d8b56-55scn       2/2     Running   0          12m
reviews-v1-868597db96-bdxgq       2/2     Running   0          12m
reviews-v2-5b64f47978-cvssp       2/2     Running   0          12m
reviews-v3-6dfd49b55b-vcwpf       2/2     Running   0          12m
----
+
. Run the following command to retrieve the URL for the product page:
+
[source,terminal]
----
echo "http://$GATEWAY_URL/productpage"
----
. Copy and paste the output in a web browser to verify the Bookinfo product page is deployed.

.Procedure from Kiali web console

. Obtain the address for the Kiali web console.

.. Log in to the OpenShift Container Platform web console.

.. Navigate to *Networking* -> *Routes*.

.. On the *Routes* page, select the {SMProductShortName} control plane project, for example `istio-system`, from the *Namespace* menu.
+
The *Location* column displays the linked address for each route.
+

.. Click the link in the *Location* column for Kiali.

.. Click *Log In With OpenShift*. The Kiali *Overview* screen presents tiles for each project namespace.

. In Kiali, click *Graph*.

. Select bookinfo from the *Namespace* list, and App graph from the *Graph Type* list.

. Click *Display idle nodes* from the *Display* menu.
+
This displays nodes that are defined but have not received or sent requests. It can confirm that an application is properly defined, but that no request traffic has been reported.
+
image::ossm-kiali-graph-bookinfo.png[Kiali displaying bookinfo application]
+
* Use the *Duration* menu to increase the time period to help ensure older traffic is captured.
+
* Use the *Refresh Rate* menu to refresh traffic more or less often, or not at all.

. Click *Services*, *Workloads* or *Istio Config* to see list views of bookinfo components, and confirm that they are healthy.

This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

[id="ossm-tutorial-bookinfo-removing_{context}"]
= Removing the Bookinfo application

Follow these steps to remove the Bookinfo application.

.Prerequisites

* OpenShift Container Platform 4.1 or higher installed.
* {SMProductName} {SMProductVersion} installed.
* Access to the OpenShift CLI (`oc`).

[id="ossm-delete-bookinfo-project_{context}"]
== Delete the Bookinfo project

.Procedure

. Log in to the OpenShift Container Platform web console.

. Click to *Home* -> *Projects*.

. Click the `bookinfo` menu {kebab}, and then click *Delete Project*.

. Type `bookinfo` in the confirmation dialog box, and then click *Delete*.
+
** Alternatively, you can run this command using the CLI to create the `bookinfo` project.
+
[source,terminal]
----
$ oc delete project bookinfo
----

[id="ossm-remove-bookinfo-smmr_{context}"]
== Remove the Bookinfo project from the {SMProductShortName} member roll

.Procedure

. Log in to the OpenShift Container Platform web console.

. Click *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and choose `istio-system` from the list.

. Click the *Istio Service Mesh Member Roll* link under *Provided APIS* for the *{SMProductName}* Operator.

. Click the `ServiceMeshMemberRoll` menu {kebab} and select *Edit Service Mesh Member Roll*.

. Edit the default Service Mesh Member Roll YAML and remove `bookinfo` from the *members* list.
+
** Alternatively, you can run this command using the CLI to remove the `bookinfo` project from the `ServiceMeshMemberRoll`. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
$ oc -n istio-system patch --type='json' smmr default -p '[{"op": "remove", "path": "/spec/members", "value":["'"bookinfo"'"]}]'
----

. Click *Save* to update Service Mesh Member Roll.

This module is included in the following assemblies:
* service_mesh/v1x/ossm-observability.adoc
* service_mesh/v2x/ossm-observability.adoc

[id="generating-sample-traces-analyzing-trace-data_{context}"]
= Generating example traces and analyzing trace data

Jaeger is an open source distributed tracing system. With Jaeger, you can perform a trace that follows the path of a request through various microservices which make up an application. Jaeger is installed by default as part of the {SMProductShortName}.

This tutorial uses {SMProductShortName} and the Bookinfo sample application to demonstrate how you can use Jaeger to perform distributed tracing.

.Prerequisites

* OpenShift Container Platform 4.1 or higher installed.
* {SMProductName} {SMProductVersion} installed.
* Jaeger enabled during the installation.
* Bookinfo example application installed.

.Procedure

. After installing the Bookinfo sample application, send traffic to the mesh. Enter the following command several times.
+
[source,terminal]
----
$ curl "http://$GATEWAY_URL/productpage"
----
+
This command simulates a user visiting the `productpage` microservice of the application.

. In the OpenShift Container Platform console, navigate to *Networking* -> *Routes* and search for the Jaeger route, which is the URL listed under *Location*.
* Alternatively, use the CLI to query for details of the route. In this example, `istio-system` is the {SMProductShortName} control plane namespace:
+
[source,terminal]
----
$ export JAEGER_URL=$(oc get route -n istio-system jaeger -o jsonpath='{.spec.host}')
----
+
.. Enter the following command to reveal the URL for the Jaeger console. Paste the result in a browser and navigate to that URL.
+
[source,terminal]
----
echo $JAEGER_URL
----

. Log in using the same user name and password as you use to access the OpenShift Container Platform console.

. In the left pane of the Jaeger dashboard, from the *Service* menu, select *productpage.bookinfo* and click *Find Traces* at the bottom of the pane. A list of traces is displayed.

. Click one of the traces in the list to open a detailed view of that trace.  If you click the first one in the list, which is the most recent trace, you see the details that correspond to the latest refresh of the `/productpage`.
