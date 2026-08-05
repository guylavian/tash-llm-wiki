---
title: "Tutorial: Deploying an application by using the web console"
type: reference
domain: openshift
slug: tutorials-4-22-dev-app-web-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console
version: 4.22
family: tutorials
documentKind: "Documentation"
---

# Tutorial: Deploying an application by using the web console

[id="dev-app-web-console"]
= Tutorial: Deploying an application by using the web console

[role="_abstract"]
To learn how to stand up an application on OpenShift Container Platform by using the web console, follow the provided tutorial. In this tutorial, you will deploy the services that are required for an application that displays a map of national parks across the world.

To complete this tutorial, you will perform the following steps:

. Create a project for the application.
+
This step allows your application to be isolated from other cluster user's workloads.

. Grant view permissions.
+
This step grants `view` permissions to interact with the OpenShift API to help discover services and other resources running within the project.

. Deploy the front-end application.
+
This step deploys the `parksmap` front-end application, exposes it externally, and scales it up to two instances.

. Deploy the back-end application.
+
This step deploys the `nationalparks` back-end application and exposes it externally.

. Deploy the database application.
+
This step deploys the `mongodb-nationalparks` MongoDB database, loads data into the database, and sets up the necessary credentials to access the database.

After you complete these steps, you can view the national parks application in a web browser.

[id="prerequisites_{context}"]
== Prerequisites

Before you start this tutorial, ensure that you have the following required prerequisites:

* You have access to a test OpenShift Container Platform cluster.
+
If your organization does not have a cluster to test on, you can request access to the Developer Sandbox to get a trial of OpenShift Container Platform.

* You have the appropriate permissions, such as the `cluster-admin` cluster role, to create a project and applications within it.
+
If you do not have the required permissions, contact your cluster administrator. You need the `self-provisioner` role to create a project and the `admin` role on the project to modify resources in that project.
+
If you are using Developer Sandbox, a project is created for you with the required permissions.

* You have logged in to the OpenShift Container Platform web console.

// Creating a new project
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-creating-new-project_{context}"]
= Creating a project

[role="_abstract"]
Create a new project to contain all required resources and application components for the tutorial.

A _project_ enables a community of users to organize and manage their content in isolation. Projects are OpenShift Container Platform extensions to Kubernetes namespaces. Projects have additional features that enable user self-provisioning. Each project has its own set of objects, policies, constraints, and service accounts.

Cluster administrators can allow developers to create their own projects. In most cases, you automatically have access to your own projects. Administrators can grant access to other projects as needed.

This procedure creates a new project called `user-getting-started`. You will use this project throughout the rest of this tutorial.

[IMPORTANT]
====
If you are using Developer Sandbox to complete this tutorial, skip this procedure. A project has already been created for you.
====

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.

.Procedure

. Navigate to *Home* -> *Projects*.
. Click *Create Project*.
. In the *Name* field, enter `user-getting-started`.
. Click *Create*.

[role="_additional-resources"]
.Additional resources
* Viewing a project by using the web console

// Granting view permissions
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-granting-permissions_{context}"]
= Granting view permissions

[role="_abstract"]
Configure the necessary permissions for the application to access the required cluster resources.

OpenShift Container Platform automatically creates several service accounts in every project. The `default` service account takes responsibility for running the pods. OpenShift Container Platform uses and injects this service account into every pod that launches.

By default, the `default` service account has limited permissions to interact with the OpenShift API.

As a requirement of the application, you must assign the `view` role to the `default` service account to allow it to communicate with the OpenShift API to learn about pods, services, and resources within the project.

.Prerequisites

* You have `cluster-admin` or project-level `admin` privileges.

.Procedure

. Navigate to *User Management* -> *RoleBindings*.
. Click *Create binding*.
. In the *Name* field, enter `sa-user-account`.
. In the *Namespace* field, search for and select `user-getting-started`.
+
[IMPORTANT]
====
If you are using a different project, select the name of your project.
====
. In the *Role name* field, search for and select `view`.
. Under *Subject*, select `ServiceAccount`.
. In the *Subject namespace* field, search for and select `user-getting-started`.
+
[IMPORTANT]
====
If you are using a different project, select the name of your project.
====
. In the *Subject name* field, enter `default`.
. Click *Create*.

[role="_additional-resources"]
.Additional resources
* RBAC overview

// Deploying the front-end application
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-deploying-first-image_{context}"]
= Deploying the front-end application

[role="_abstract"]
Deploy the front-end application that provides the external-facing web component for the tutorial.

The simplest way to deploy an application in OpenShift Container Platform is to run a provided container image.

The following procedure deploys `parksmap`, which is the front-end component of the `national-parks-app` application. The web application displays an interactive map of the locations of national parks across the world.

.Procedure

. From the *Quick create* (image:fa-plus-circle.png[title="Quick create menu"]) menu in the upper right corner, click *Container images*.
. Select *Image name from external registry* and enter `quay.io/openshiftroadshow/parksmap:latest`.
. Scroll to the *General* section.
. In the *Application name* field, enter `national-parks-app`.
. In the *Name* field, ensure that the value is `parksmap`.
. Scroll to the *Deploy* section.
. In the *Resource type* field, ensure that *Deployment* is selected.
. In the *Advanced options* section, ensure that *Create a route* is selected.
+
By default, services running on OpenShift Container Platform are not accessible externally. You must select this option to create a route so that external clients can access your service.

. Click the *Labels* hyperlink.
+
The application code requires certain labels to be set.

. Add the following labels to the text area and press Enter after each key/value pair:

** `app=national-parks-app`
** `component=parksmap`
** `role=frontend`

. Click *Create*.
+
You are redirected to the *Topology* page where you can see the `parksmap` deployment in the `national-parks-app` application.

[role="_additional-resources"]
.Additional resources
* Viewing the topology of your application

// Viewing pod details
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-examining-pod_{context}"]
= Viewing pod details

[role="_abstract"]
Retrieve detailed pod information to confirm the running status and resource configuration of the applications in this tutorial.

OpenShift Container Platform uses the Kubernetes concept of a _pod_, which is one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, and managed.
Pods are the rough equivalent of a machine instance, physical or virtual, to a container.

The *Overview* panel enables you to access many features of the `parksmap` deployment. The *Details* and *Resources* tabs enable you to scale application pods and check the status of builds, services, and routes.

.Prerequisites

* You have deployed the `parksmap` front-end application.

.Procedure

. Navigate to *Workloads* -> *Topology*.
. Click the `parksmap` deployment in the `national-parks-app` application.
+
.Parksmap deployment
image::getting-started-examine-pod.png[Topology view of parksmap deployment]
+
This opens an overview panel with the following tabs:

** *Details*: View details about your deployment, edit certain settings, and scale your deployment.

** *Resources*: View details for the pods, services, and routes associated with your deployment.

** *Observe*: View metrics and events for your deployment.

. To view the logs for a pod, select the *Resources* tab and click *View logs* next to the `parksmap` pod.

[role="_additional-resources"]
.Additional resources
* Interacting with applications and components
* Scaling application pods and checking builds and routes
* Labels and annotations used for the Topology view

// Scaling up the deployment
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-scaling-app_{context}"]
= Scaling up the application

[role="_abstract"]
Scale the application deployment up or down to meet workload demands.

In Kubernetes, a `Deployment` object defines how an application deploys. In most cases when you deploy an application, OpenShift Container Platform creates the `Pod`, `Service`, `ReplicaSet`, and `Deployment` resources for you.

When you deploy the `parksmap` image, a deployment resource is created. In this example, only one pod is deployed. You might want to scale up your application to keep up with user demand or to ensure that your application is always running even if one pod is down.

The following procedure scales the `parksmap` deployment to use two instances.

.Prerequisites

* You have deployed the `parksmap` front-end application.

.Procedure

. Navigate to *Workloads* -> *Topology* and click the `parksmap` deployment.
. Select the *Details* tab.
. Use the up arrow to scale the pod to two instances.
+
.Scaling application
image::getting-started-scaling-pod.png[Scaling pod to two instances]
+
[TIP]
====
You can use the down arrow to scale your deployment back down to one pod instance.
====

[role="_additional-resources"]
.Additional resources
* Recommended practices for scaling the cluster

// Deploying the back-end application
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-deploying-python-app_{context}"]
= Deploying the back-end application

[role="_abstract"]
Deploy the back-end application that provides the service that queries the database to return the national park data required for your application.

The following procedure deploys `nationalparks`, which is the back-end component for the `national-parks-app` application. The Python application performs 2D geo-spatial queries against a MongoDB database to locate and return map coordinates of all national parks in the world.

.Prerequisites

* You have deployed the `parksmap` front-end application.

.Procedure

. From the *Quick create* (image:fa-plus-circle.png[title="Quick create menu"]) menu in the upper right corner, click *Import from Git*.
. In the *Git Repo URL* field, enter [x-]`https://github.com/openshift-roadshow/nationalparks-py.git`.
+
A builder image is automatically detected, but the import strategy defaults to Dockerfile instead of Python.

. Change the import strategy:

.. Click *Edit Import Strategy*.
.. Select *Builder Image*.
.. Select *Python*.

. Scroll to the *General* section.
. In the *Application* field, ensure that the value is `national-parks-app`.
. In the *Name* field, enter `nationalparks`.
. Scroll to the *Deploy* section.
. In the *Resource type* field, ensure that *Deployment* is selected.
. In the *Advanced options* section, ensure that *Create a route* is selected.
+
By default, services running on OpenShift Container Platform are not accessible externally. You must select this option to create a route so that external clients can access your service.

. Click the *Labels* hyperlink.
+
The application code requires certain labels to be set.

. Add the following labels to the text area and press Enter after each key/value pair:

** `app=national-parks-app`
** `component=nationalparks`
** `role=backend`
** `type=parksmap-backend`

. Click *Create*.
+
You are redirected to the *Topology* page where you can see the `nationalparks` deployment in the `national-parks-app` application.

.Verification

. Navigate to *Workloads* -> *Topology*.
. Click the `nationalparks` deployment in the `national-parks-app` application.
. Click the *Resources* tab.
+
Wait for the build to complete successfully.

[role="_additional-resources"]
.Additional resources
* Adding services to your application
* Importing a codebase from Git to create an application

// Deploying the database application
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-connecting-database_{context}"]
= Deploying the database application

[role="_abstract"]
Deploy a MongoDB database application to contain the information that your application requires. For this tutorial, you will deploy a database application called `mongodb-nationalparks` that holds the national park location information.

.Prerequisites

* You have deployed the `parksmap` front-end application.
* You have deployed the `nationalparks` back-end application.

.Procedure

. From the *Quick create* (image:fa-plus-circle.png[title="Quick create menu"]) menu in the upper right corner, click *Container images*.
. Select *Image name from external registry* and enter `registry.redhat.io/rhmap47/mongodb`.
. In the *Runtime icon* field, search for and select `mongodb`.
. Scroll to the *General* section.
. In the *Application name* field, enter `national-parks-app`.
. In the *Name* field, enter `mongodb-nationalparks`.
. Scroll to the *Deploy* section.
. In the *Resource type* field, ensure that *Deployment* is selected.
. Click *Show advanced Deployment option*.
. Under *Environment variables (runtime only)*, add the following names and values:
+
.Environment variable names and values
[cols="1,1"]
|===
|Name |Value

|`MONGODB_USER`|`mongodb`
|`MONGODB_PASSWORD`|`mongodb`
|`MONGODB_DATABASE`|`mongodb`
|`MONGODB_ADMIN_PASSWORD`|`mongodb`
|===
+
[TIP]
====
Click *Add value* to add each additional environment variable.
====

. In the *Advanced options* section, clear *Create a route*.
+
The database application does not need to be accessed externally, so a route is not required.

. Click *Create*.
+
You are redirected to the *Topology* page where you can see the `mongodb-nationalparks` deployment in the `national-parks-app` application.

// Providing access to the database by creating a secret
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-creating-secret_{context}"]
= Providing access to the database by creating a secret

[role="_abstract"]
Create a `Secret` resource to securely provide the back-end application with the sensitive database connection credentials.

The `nationalparks` application needs information, such as the database name, username, and passwords, to access the MongoDB database. However, because this information is sensitive, you should not store it directly in the pod.

You can use a _secret_ to store sensitive information, and share that secret with workloads.

`Secret` objects provide a mechanism to hold sensitive information such as passwords, OpenShift Container Platform client configuration files, and private source repository credentials. Secrets decouple sensitive content from the pods. You can mount secrets into containers by using a volume plugin or by passing the secret in as an environment variable. The system can then use secrets to provide the pod with the sensitive information.

The following procedure creates the `nationalparks-mongodb-parameters` secret and mounts it to the `nationalparks` workload.

.Prerequisites

* You have deployed the `nationalparks` back-end application.
* You have deployed the `mongodb-nationalparks` database application.

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. Click *Create* -> *Key/value secret*.
. In the *Secret name* field, enter `nationalparks-mongodb-parameters`.
. Enter the following values for *Key* and *Value*:
+
.Secret keys and values
[cols="1,1"]
|===
|Key |Value

|`DATABASE_SERVICE_NAME`|`mongodb-nationalparks`
|`MONGODB_USER`|`mongodb`
|`MONGODB_PASSWORD`|`mongodb`
|`MONGODB_DATABASE`|`mongodb`
|`MONGODB_ADMIN_PASSWORD`|`mongodb`
|===
+
[TIP]
====
Click *Add key/value* to add each additional key/value pair.
====

. Click *Create*.
. Click *Add Secret to workload*.
. From the *Add this secret to workload* list, select `nationalparks`.

. Click *Save*.
+
This change in configuration triggers a new rollout of the `nationalparks` deployment with the environment variables properly injected.

[role="_additional-resources"]
.Additional resources
* Understanding secrets

// Loading data into the database
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-load-data-output_{context}"]
= Loading data into the database

[role="_abstract"]
After you have deployed the `mongodb-nationalparks` database application, load the national park location information into the database.

.Prerequisites

* You have deployed the `nationalparks` back-end application.
* You have deployed the `mongodb-nationalparks` database application.

.Procedure

. Navigate to *Workloads* -> *Topology*.
. Click the `nationalparks` deployment and select the *Resources* tab.
. Copy the *Location* URL from your route.
. Paste the URL into your web browser and add the following at the end of the URL:
+
[source,text]
----
/ws/data/load
----
+
For example:
+
[source,text]
----
https://nationalparks-user-getting-started.apps.cluster.example.com/ws/data/load
----
+
.Example output
[source,text]
----
Items inserted in database: 2893
----

// Viewing the application in a web browser
// Module included in the following assemblies:
//
// * tutorials/dev-app-web-console.adoc

[id="getting-started-web-console-view_{context}"]
= Viewing the application in a web browser

[role="_abstract"]
After you have deployed the necessary applications and loaded data into the database, you are now ready view your application through a browser. You can access the application by opening the URL for the front-end application.

.Prerequisites

* You have deployed the `parksmap` front-end application.
* You have deployed the `nationalparks` back-end application.
* You have deployed the `mongodb-nationalparks` database application.
* You have loaded the data into the `mongodb-nationalparks` database.

.Procedure

. Navigate to *Workloads* -> *Topology*.
. Click the *Open URL* link from the `parksmap` deployment.
+
.National parks across the world
image::getting-started-parksmap-url.png[Opening the URL for the parksmap deployment]

. Verify that your web browser displays a map of the national parks across the world.
+
.National parks across the world
image::getting-started-map-national-parks.png[Map of the national parks across the world]
+
If you allow the application to access your location, the map will center on your location.
