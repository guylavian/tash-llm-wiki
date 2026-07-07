---
title: "Adding services to a service mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-create-mesh
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-create-mesh
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Adding services to a service mesh

[id="ossm-create-mesh"]
= Adding services to a service mesh

A project contains services; however, the services are only available if you add the project to the service mesh.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-about-adding-namespace_{context}"]
= About adding projects to a service mesh

After installing the Operators and creating the `ServiceMeshControlPlane` resource, add one or more projects to the service mesh.

[NOTE]
====
In OpenShift Container Platform, a project is essentially a Kubernetes namespace with additional annotations, such as the range of user IDs that can be used in the project. Typically, the OpenShift Container Platform web console uses the term project, and the CLI uses the term namespace, but the terms are essentially synonymous.
====

You can add projects to an existing service mesh using either the OpenShift Container Platform web console or the CLI. There are three methods to add a project to a service mesh:

* Specifying the project name in the `ServiceMeshMemberRoll` resource.

* Configuring label selectors in the `spec.memberSelectors` field of the `ServiceMeshMemberRoll` resource.

* Creating the `ServiceMeshMember` resource in the project.

If you use the first method, then you must create the `ServiceMeshMemberRoll` resource.

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
// * service_mesh/v2x/ossm-create-mesh.adoc

[id="ossm-about-adding-projects-using-smmr_{context}"]
= About adding projects using the ServiceMeshMemberRoll resource

Using the `ServiceMeshMemberRoll` resource is the simplest way to add a project to a service mesh. To add a project, specify the project name in the `spec.members` field of the `ServiceMeshMemberRoll` resource. The `ServiceMeshMemberRoll` resource specifies which projects are controlled by the `ServiceMeshControlPlane` resource.

image::ossm-adding-project-using-smmr.png[Adding project using `ServiceMeshMemberRoll` resource image]

[NOTE]
====
Adding projects using this method requires the user to have the `update servicemeshmemberrolls` and the `update pods` privileges in the project that is being added.
====

* If you already have an application, workload, or service to add to the service mesh, see the following:
** Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the web console
** Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the CLI

* Alternatively, to install a sample application called Bookinfo and add it to a `ServiceMeshMemberRoll` resource, see the Bookinfo example application tutorial.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-add-project-member-roll-recourse-console_{context}"]
= Adding or removing projects from the mesh using the ServiceMeshMemberRoll resource with the web console

You can add or remove projects from the mesh using the `ServiceMeshMemberRoll` resource with the OpenShift Container Platform web console. You can add any number of projects, but a project can only belong to one mesh.

The `ServiceMeshMemberRoll` resource is deleted when its corresponding `ServiceMeshControlPlane` resource is deleted.

.Prerequisites

* An installed, verified {SMProductName} Operator.
* An existing `ServiceMeshMemberRoll` resource.
* The name of the project with the `ServiceMeshMemberRoll` resource.
* The names of the projects you want to add or remove from the mesh.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and choose the project where your `ServiceMeshControlPlane` resource is deployed from the list. For example `istio-system`.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Member Roll* tab.

. Click the `default` link.

. Click the YAML tab.

. Modify the YAML to add projects as members (or delete them to remove existing members). You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource.
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

. Click *Save*.

. Click *Reload*.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-add-project-member-roll-resource-cli_{context}"]
= Adding or removing projects from the mesh using ServiceMeshMemberRoll resource with the CLI

You can add one or more projects to the mesh using the `ServiceMeshMemberRoll` resource with the CLI. You can add any number of projects, but a project can only belong to one mesh.

The `ServiceMeshMemberRoll` resource is deleted when its corresponding `ServiceMeshControlPlane` resource is deleted.

.Prerequisites

* An installed, verified {SMProductName} Operator.
* An existing `ServiceMeshMemberRoll` resource.
* The name of the project with the `ServiceMeshMemberRoll` resource.
* The names of the projects you want to add or remove from the mesh.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Edit the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc edit smmr -n <controlplane-namespace>
----

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

. Save the file and exit the editor.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-mesh.adoc

[id="ossm-about-adding-projects-using-smm_{context}"]
= About adding projects using the ServiceMeshMember resource

A `ServiceMeshMember` resource provides a way to add a project to a service mesh without modifying the `ServiceMeshMemberRoll` resource. To add a project, create a `ServiceMeshMember` resource in the project that you want to add to the service mesh. When the {SMProductShortName} Operator processes the `ServiceMeshMember` object, the project appears in the `status.members` list of the `ServiceMeshMemberRoll` resource. Then, the services that reside in the project are made available to the mesh.

image::ossm-adding-project-using-smm.png[Adding project using `ServiceMeshMember` resource image]

The mesh administrator must grant each mesh user permission to reference the `ServiceMeshControlPlane` resource in the `ServiceMeshMember` resource. With this permission in place, a mesh user can add a project to a mesh even when that user does not have direct access rights for the service mesh project or the `ServiceMeshMemberRoll` resource. For more information, see Creating the {SMProductName} members.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-create-mesh.adoc

[id="ossm-adding-project-using-smm-resource-console_{context}"]
= Adding a project to the mesh using the ServiceMeshMember resource with the web console

You can add one or more projects to the mesh using the `ServiceMeshMember` resource with the OpenShift Container Platform web console.

.Prerequisites
* You have installed the {SMProductName} Operator.
* You know the name of the `ServiceMeshControlPlane` resource and the name of the project that the resource belongs to.
* You know the name of the project you want to add to the mesh.
* A service mesh administrator must explicitly grant access to the service mesh. Administrators can grant users permissions to access the mesh by assigning them the `mesh-user` `Role` using a `RoleBinding` or `ClusterRoleBinding`. For more information, see _Creating the {SMProductName} members_.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and choose the project that you want to add to the mesh from the drop-down list. For example, `istio-system`.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Member* tab.

. Click *Create ServiceMeshMember*

. Accept the default name for the `ServiceMeshMember`.

. Click to expand *ControlPlaneRef*.

. In the *Namespace* field, select the project that the `ServiceMeshControlPlane` resource belongs to. For example, `istio-system`.

. In the *Name* field, enter the name of the `ServiceMeshControlPlane` resource that this namespace belongs to. For example, `basic`.

. Click *Create*.

.Verification

. Confirm the `ServiceMeshMember` resource was created and that the project was added to the mesh by using the following steps:

.. Click the resource name, for example, `default`.
.. View the *Conditions* section shown at the end of the screen.
.. Confirm that the `Status` of the `Reconciled` and `Ready` conditions is `True`.
+
If the `Status` is `False`, see the `Reason` and `Message` columns for more information.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-create-mesh.adoc

[id="ossm-adding-project-using-smm-resource-cli_{context}"]
= Adding a project to the mesh using the ServiceMeshMember resource with the CLI

You can add one or more projects to the mesh using the `ServiceMeshMember` resource with the CLI.

.Prerequisites
* You have installed the {SMProductName} Operator.
* You know the name of the `ServiceMeshControlPlane` resource and the name of the project it belongs to.
* You know the name of the project you want to add to the mesh.
* A service mesh administrator must explicitly grant access to the service mesh. Administrators can grant users permissions to access the mesh by assigning them the `mesh-user` `Role` using a `RoleBinding` or `ClusterRoleBinding`. For more information, see _Creating the {SMProductName} members_.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Create the YAML file for the `ServiceMeshMember` manifest. The manifest adds the `my-application` project to the service mesh that was created by the `ServiceMeshControlPlane` resource deployed in the `istio-system` namespace:
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMember
metadata:
  name: default
  namespace: my-application
spec:
  controlPlaneRef:
    namespace: istio-system
    name: basic
----

. Apply the YAML file to create the `ServiceMeshMember` resource:
+
[source,terminal]
----
$ oc apply -f <file-name>
----

.Verification

* Verify that the namespace is part of the mesh by running the following command. Confirm the that the value `True` appears in the `READY` column.
+
[source,terminal]
----
$ oc get smm default -n my-application
----
+
.Example output
[source,terminal]
----
NAME      CONTROL PLANE        READY   AGE
default   istio-system/basic   True    2m11s
----

* Alternatively, view the `ServiceMeshMemberRoll` resource to confirm that the `my-application` namespace is displayed in the `status.members` and `status.configuredMembers` fields of the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc describe smmr default -n istio-system
----
+
.Example output
[source,terminal]
----
Name:         default
Namespace:    istio-system
Labels:       <none>
# ...
Status:
# ...
  Configured Members:
    default
    my-application
# ...
  Members:
    default
    my-application
----

// Module included in the following assemblies:
//
// * service_mesh/v2x/create-mesh.adoc

[id="ossm-about-adding-projects-using-label-selectors_{context}"]
= About adding projects using label selectors

For cluster-wide deployments, you can use label selectors to add projects to the mesh. Label selectors specified in the `ServiceMeshMemberRoll` resource enable the {SMProductShortName} Operator to add or remove namespaces to or from the mesh based on namespace labels. Unlike other standard OpenShift Container Platform resources that you can use to specify a single label selector, you can use the `ServiceMeshMemberRoll` resource to specify multiple label selectors.

image::ossm-adding-project-using-label-selector.png[Adding project using label selector image]

If the labels for a namespace match any of the selectors specified in the `ServiceMeshMemberRoll` resource, then the namespace is included in the mesh.

[NOTE]
====
In OpenShift Container Platform, a project is essentially a Kubernetes namespace with additional annotations, such as the range of user IDs that can be used in the project. Typically, the OpenShift Container Platform web console uses the term _project_, and the CLI uses the term _namespace_, but the terms are essentially synonymous.
====

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-create-mesh.adoc

[id="ossm-adding-project-using-label-selectors-console_{context}"]
= Adding a project to the mesh using label selectors with the web console

You can use labels selectors to add a project to the {SMProductShortName} with the OpenShift Container Platform web console.

.Prerequisites
* You have installed the {SMProductName} Operator.
* The deployment has an existing `ServiceMeshMemberRoll` resource.
* You are logged in to the OpenShift Container Platform web console as `cluster-admin`.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.

.Procedure

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu, and from the drop-down list, select the project where your `ServiceMeshMemberRoll` resource is deployed. For example, *istio-system*.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Member Roll* tab.

. Click *Create ServiceMeshMember Roll*.

. Accept the default name for the `ServiceMeshMemberRoll`.

. In the *Labels* field, enter key-value pairs to define the labels that identify which namespaces to include in the service mesh. If a project namespace has either label specified by the selectors, then the project namespace is included in the service mesh. You do not need to include both labels.
+
For example, entering `mykey=myvalue` includes all namespaces with this label as part of the mesh. When the selector identifies a match, the project namespace is added to the service mesh.
+
Entering `myotherkey=myothervalue` includes all namespaces with this label as part of the mesh. When the selector identifies a match, the project namespace is added to the service mesh.

. Click *Create*.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-adding-project-using-label-selectors-cli_{context}"]
= Adding a project to the mesh using label selectors with the CLI

You can use label selectors to add a project to the {SMProductShortName} with the CLI.

.Prerequisites
* You have installed the {SMProductName} Operator.
* The deployment has an existing `ServiceMeshMemberRoll` resource.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Edit the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc edit smmr default -n istio-system
----
+
You can deploy the {SMProductShortName} control plane to any project provided that it is separate from the project that contains your services.

. Modify the YAML file to include namespace label selectors in the `spec.memberSelectors` field of the `ServiceMeshMemberRoll` resource.
+
[NOTE]
====
Instead of using the `matchLabels` field, you can also use the `matchExpressions` field in the selector.
====
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  memberSelectors: <1>
  - matchLabels: <2>
      mykey: myvalue <2>
  - matchLabels: <3>
      myotherkey: myothervalue <3>
----
<1> Contains the label selectors used to identify which project namespaces are included in the service mesh. If a project namespace has either label specified by the selectors, then the project namespace is included in the service mesh. The project namespace does not need both labels to be included.
<2> Specifies all namespaces with the `mykey=myvalue` label. When the selector identifies a match, the project namespace is added to the service mesh.
<3> Specifies all namespaces with the `myotherkey=myothervalue` label. When the selector identifies a match, the project namespace is added to the service mesh.

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

== Next steps

* To continue the installation process, you must enable sidecar injection.
