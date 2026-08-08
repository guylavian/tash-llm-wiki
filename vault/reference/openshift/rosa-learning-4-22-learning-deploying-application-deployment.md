---
title: "Deploying the OSToy application with Kubernetes"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-application-deployment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-application-deployment
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Deploying the OSToy application with Kubernetes

[id="learning-deploying-application-deployment"]
= Deploying the OSToy application with Kubernetes

[role="_abstract"]
Deploy your application to the cluster by creating a container image, storing it in an image repository, and defining a Deployment object. Managing these components allows you to reliably run and scale your workloads.

Deploying an application involves the following steps:

* Create the images for the front-end and back-end microservice containers
* Store the container images in an image repository
* Create the Kubernetes Deployment object for the application
* Deploy the application

[NOTE]
====
This workshop focuses on application deployment and has users run a remote file which uses an existing image.
====

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-retrieving-login_{context}"]
= Retrieving the login command

[role="_abstract"]
Before creating a cluster, you must log in to the {rosa-cli-first}. Install the {rosa-cli} by completing the workshop on creating a cluster.

.Procedure
. Confirm you are logged in to the {rosa-cli} by running the following command:
+
[source,terminal]
----
rosa whoami
----
+
If you are logged in to the command-line interface, skip to "Creating a new project". If you are not logged in to the command-line interface, continue this procedure.

. Access your cluster with the web console.

. Click the dropdown arrow next to your login name in the upper right corner, and select *Copy Login Command*.
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
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-new-project-cli_{context}"]
= Creating a new project using the CLI

[role="_abstract"]
You can use {oc-first} to create a new project.

.Procedure
* Create a new project named `ostoy` in your cluster by running following command:
+
[source,terminal]
----
$ oc new-project ostoy
----
+
*For example*:
+
[source,terminal]
----
Now using project "ostoy" on server "https://api.myrosacluster.abcd.p1.openshiftapps.com:6443".
----

** *Optional*: Create a unique project name by running the following command:
+
[source,terminal]
----
$ oc new-project ostoy-$(uuidgen | cut -d - -f 2 | tr '[:upper:]' '[:lower:]')
----
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-new-project-ui_{context}"]
= Creating a new project using the web console

[role="_abstract"]
You can use {cluster-manager} to create a new project.

.Procedure
. From the web console, click *Home -> Projects*.

. On the *Projects* page, click create *Create Project*.
+
image::4-createnewproj.png[The project creation screen]

. In the *Create Project* box, enter a project name in the *Name* field.

. Click *Create*.
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-backend-microservice_{context}"]
= Deploying the back-end microservice

[role="_abstract"]
You can deploy a microservice to start the OSToy backend processes. The microservice serves internal web requests and returns a JSON object containing the current hostname and a randomly generated color string.

.Procedure
* Deploy the microservice by running the following command:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-microservice-deployment.yaml
----
+
*For example*:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-microservice-deployment.yaml
deployment.apps/ostoy-microservice created
service/ostoy-microservice-svc created
----
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-frontend-microservice_{context}"]
= Deploying the front-end microservice

[role="_abstract"]
The front-end deployment uses the Node.js front-end for the application and additional Kubernetes objects. Front-end deployment defines the following features:

* Persistent volume claim
* Deployment object
* Service
* Route
* ConfigMaps
* Secrets

.Procedure
* Deploy the application front-end and create the objects by running the following command:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/yaml/ostoy-frontend-deployment.yaml
----
+
*For example*:
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
All objects should create successfully.
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-obtain-route_{context}"]
= Obtain the route to your application

[role="_abstract"]
To access the OSToy application, obtain the route by using the {oc-first}.

.Procedure
* Get the route to your application by running the following command:
+
[source,terminal]
----
$ oc get route
----
+
*For example*:
+
[source,terminal]
----
NAME          HOST/PORT                                                 PATH   SERVICES             PORT    TERMINATION   WILDCARD
ostoy-route   ostoy-route-ostoy.apps.<your-rosa-cluster>.abcd.p1.openshiftapps.com          ostoy-frontend-svc   <all>                 None
----
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-deployment.adoc
[id="learning-deploying-application-deployment-viewing-application_{context}"]
= Viewing the application

[role="_abstract"]
After you deploy OSToy, you can view the application by accessing its URL.

.Procedure
. Copy the `ostoy-route-ostoy.apps.<your-rosa-cluster>.abcd.p1.openshiftapps.com` URL output from the previous step.
. Paste the copied URL into your web browser and press enter. You should see the homepage of your application. If the page does not load, make sure you used `http` and not `https`.
+
image::4-ostoy-homepage.png[OStoy application homepage]
