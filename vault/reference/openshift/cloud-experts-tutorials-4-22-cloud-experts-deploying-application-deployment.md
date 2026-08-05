---
title: "Tutorial: Deploying an application"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-deployment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-deployment
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Deploying an application

[id="cloud-experts-deploying-application-deployment"]
= Tutorial: Deploying an application

[role="_abstract"]
You can deploy the OSToy application by creating and storing the images for the front-end and back-end microservice containers in an image repository. You can then create Kubernetes deployments to deploy the application.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-retrieving-login_{context}"]
= Retrieving the login command

[role="_abstract"]
To deploy your application, you need to get the CLI login command.

.Procedure
. If you are not logged in to the CLI, access your cluster with the web console.

. Click the dropdown arrow next to your login name in the upper right, and select *Copy Login Command*.
+
image::4-cli-login.png[CLI login screen]
+
A new tab opens.

. Select your authentication method.

. Click *Display Token*.

. Copy the command under *Log in with this token*.

. From your terminal, paste and run the copied command. If the login is successful, you will see the following confirmation message:
+
[source,terminal]
----
$ oc login --token=<your_token> --server=https://api.osd4-demo.abc1.p1.openshiftapps.com:6443
Logged into "https://api.myrosacluster.abcd.p1.openshiftapps.com:6443" as "rosa-user" using the token provided.

You don't have any projects. You can try to create a new project, by running

oc new-project <project name>
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-creating-project-cli_{context}"]
= Creating a new project by using the CLI

[role="_abstract"]
You can use the {oc-first} tool to create your project for this tutorial.

.Procedure
. Create a new project named `ostoy` in your cluster by running following command:
+
[source,terminal]
----
$ oc new-project ostoy
----
+
**Example output**
+
[source,terminal]
----
Now using project "ostoy" on server "https://api.myrosacluster.abcd.p1.openshiftapps.com:6443".
----

. *Optional*: Alternatively, create a unique project name by running the following command:
+
[source,terminal]
----
$ oc new-project ostoy-$(uuidgen | cut -d - -f 2 | tr '[:upper:]' '[:lower:]')
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-creating-project-ui_{context}"]
= Creating a new project by using the web console

[role="_abstract"]
You can create your project using {cluster-manager}.

.Procedure
. From the web console, click *Home -> Projects*.

. On the *Projects* page, click create *Create Project*.
+
image::4-createnewproj.png[The project creation screen]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-backend-microservice_{context}"]
= Deploying the back-end microservice

[role="_abstract"]
The microservice serves internal web requests and returns a JSON object containing the current hostname and a randomly generated color string.

.Procedure
* Deploy the microservice by running the following command from your terminal:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-microservice-deployment.yaml
----
+
**Example output**
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-microservice-deployment.yaml
deployment.apps/ostoy-microservice created
service/ostoy-microservice-svc created
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-frontend-microservice_{context}"]
= Deploying the front-end service

[role="_abstract"]
The front-end deployment uses the Node.js front-end for the application and additional Kubernetes objects.

The `ostoy-frontend-deployment.yaml` file shows that front-end deployment defines the following features:

- Persistent volume claim
- Deployment object
- Service
- Route
- Configmaps
- Secrets

.Procedure
* Deploy the application front-end and create all of the objects by entering the following command:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-frontend-deployment.yaml
----
+
**Example output**
+
[source,terminal]
----
persistentvolumeclaim/ostoy-pvc created
deployment.apps/ostoy-frontend created
service/ostoy-frontend-svc created
route.route.openshift.io/ostoy-route created
configmap/ostoy-configmap-env created
secret/ostoy-secret-env created
configmap/ostoy-configmap-files created
secret/ostoy-secret created
----
+
You should see all objects created successfully.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-get-route_{context}"]
= Getting the route

[role="_abstract"]
You must get the route to access the application.

.Procedure
* Get the route to your application by running the following command:
+
[source,terminal]
----
$ oc get route
----
+
**Example output**
+
[source,terminal]
----
NAME          HOST/PORT                                                 PATH   SERVICES             PORT    TERMINATION   WILDCARD
ostoy-route   ostoy-route-ostoy.apps.<your-rosa-cluster>.abcd.p1.openshiftapps.com          ostoy-frontend-svc   <all>                 None
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-deployment.adoc

[id="cloud-experts-deploying-application-deployment-view-application_{context}"]
= Viewing the application

[role="_abstract"]
After launching your application, you can view the application from your browser.

.Procedure
. Copy the `ostoy-route-ostoy.apps.<your-rosa-cluster>.abcd.p1.openshiftapps.com` URL output from the previous step.
. Paste the copied URL into your web browser and press enter. You should see the homepage of your application. If the page does not load, make sure you use `http` and not `https`.
+
image::4-ostoy-homepage.png[OStoy application homepage]
