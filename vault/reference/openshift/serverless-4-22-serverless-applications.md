---
title: "Serverless applications"
type: reference
domain: openshift
slug: serverless-4-22-serverless-applications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-applications
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Serverless applications

[id="serverless-applications"]
= Serverless applications

You can create a serverless application by using one of the following methods:

* Create a Knative service from the OpenShift Container Platform web console.
+
See Creating applications using the Developer perspective for more information.
* Create a Knative service by using the Knative (`kn`) CLI.
* Create and apply a Knative `Service` object as a YAML file, by using the `oc` CLI.

// create service using CLI
// Module included in the following assemblies:
//
// * serverless/develop/serverless-applications.adoc
// * serverless/reference/kn-serving-ref.adoc

[id="creating-serverless-apps-kn_{context}"]
= Creating serverless applications by using the Knative CLI

Using the Knative (`kn`) CLI to create serverless applications provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service create` command to create a basic serverless application.

.Prerequisites

* {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a Knative service:
+
[source,terminal]
----
$ kn service create <service-name> --image <image> --tag <tag-value>
----
+
Where:
+
** `--image` is the URI of the image for the application.
** `--tag` is an optional flag that can be used to add a tag to the initial revision that is created with the service.
+
.Example command
[source,terminal]
----
$ kn service create event-display \
    --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
+
.Example output
[source,terminal]
----
Creating service 'event-display' in namespace 'default':

  0.271s The Route is still working to reflect the latest desired specification.
  0.580s Configuration "event-display" is waiting for a Revision to become ready.
  3.857s ...
  3.861s Ingress has not yet been reconciled.
  4.270s Ready to serve.

Service 'event-display' created with latest revision 'event-display-bxshg-1' and URL:
http://event-display-default.apps-crc.testing
----

// create service using YAML
// Module included in the following assemblies:
//
// * serverless/develop/serverless-applications.adoc

[id="creating-serverless-apps-yaml_{context}"]
= Creating serverless applications using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe applications declaratively and in a reproducible manner. To create a serverless application by using YAML, you must create a YAML file that defines a Knative `Service` object, then apply it by using `oc apply`.

After the service is created and the application is deployed, Knative creates an immutable revision for this version of the application. Knative also performs network programming to create a route, ingress, service, and load balancer for your application and automatically scales your pods up and down based on traffic.

.Prerequisites

* {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file containing the following sample code:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: event-delivery
  namespace: default
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
          env:
            - name: RESPONSE
              value: "Hello Serverless!"
----
. Navigate to the directory where the YAML file is contained, and deploy the application by applying the YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

If you do not want to switch to the *Developer* perspective in the OpenShift Container Platform web console or use the Knative (`kn`) CLI or YAML files, you can create Knative components by using the *Administator* perspective of the OpenShift Container Platform web console.

// Create services as an admin
// Module included in the following assemblies:
//
// serverless/admin_guide/serverless-cluster-admin-serving.adoc

[id="creating-serverless-apps-admin-console_{context}"]
= Creating serverless applications using the Administrator perspective

After the service is created and the application is deployed, Knative creates an immutable revision for this version of the application. Knative also performs network programming to create a route, ingress, service, and load balancer for your application and automatically scales your pods up and down based on traffic.

.Prerequisites

To create serverless applications using the *Administrator* perspective, ensure that you have completed the following steps.

* The {ServerlessOperatorName} and Knative Serving are installed.
* You have logged in to the web console and are in the *Administrator* perspective.

.Procedure

. Navigate to the *Serverless* -> *Serving* page.
. In the *Create* list, select *Service*.
. Manually enter YAML or JSON definitions, or by dragging and dropping a file into the editor.
. Click *Create*.

// offline mode
// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc
// * serverless/develop/serverless-applications.adoc

[id="creating-an-offline-service_{context}"]
= Creating a service using offline mode

You can execute `kn service` commands in offline mode, so that no changes happen on the cluster, and instead the service descriptor file is created on your local machine. After the descriptor file is created, you can modify the file before propagating changes to the cluster.

.Prerequisites

* {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

. In offline mode, create a local Knative service descriptor file:
+
[source,terminal]
----
$ kn service create event-display \
    --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest \
    --target ./ \
    --namespace test
----
+
.Example output
[source,terminal]
----
Service 'event-display' created in namespace 'test'.
----
+
* The `--target ./` flag enables offline mode and specifies `./` as the directory for storing the new directory tree.
+
If you do not specify an existing directory, but use a filename, such as `--target my-service.yaml`, then no directory tree is created. Instead, only the service descriptor file `my-service.yaml` is created in the current directory.
+
The filename can have the `.yaml`, `.yml`, or `.json` extension. Choosing `.json` creates the service descriptor file in the JSON format.
+
* The `--namespace test` option places the new service in the `test` namespace.
+
If you do not use `--namespace`, and you are logged in to an OpenShift Container Platform cluster, the descriptor file is created in the current namespace. Otherwise, the descriptor file is created in the `default` namespace.

. Examine the created directory structure:
+
[source,terminal]
----
$ tree ./
----
+
.Example output
[source,terminal]
----
./
└── test
    └── ksvc
        └── event-display.yaml

2 directories, 1 file
----
+
* The current `./` directory specified with `--target` contains the new `test/` directory that is named after the specified namespace.
* The `test/` directory contains the `ksvc` directory, named after the resource type.
* The `ksvc` directory contains the descriptor file `event-display.yaml`, named according to the specified service name.

. Examine the generated service descriptor file:
+
[source,terminal]
----
$ cat test/ksvc/event-display.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  creationTimestamp: null
  name: event-display
  namespace: test
spec:
  template:
    metadata:
      annotations:
        client.knative.dev/user-image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
      creationTimestamp: null
    spec:
      containers:
      - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
        name: ""
        resources: {}
status: {}
----

. List information about the new service:
+
[source,terminal]
----
$ kn service describe event-display --target ./ --namespace test
----
+
.Example output
[source,terminal]
----
Name:       event-display
Namespace:  test
Age:
URL:

Revisions:

Conditions:
  OK TYPE    AGE REASON
----

* The `--target ./` option specifies the root directory for the directory structure containing namespace subdirectories.
+
Alternatively, you can directly specify a YAML or JSON filename with the `--target` option. The accepted file extensions are `.yaml`, `.yml`, and `.json`.
+
* The `--namespace` option specifies the namespace, which communicates to `kn` the subdirectory that contains the necessary service descriptor file.
+
If you do not use `--namespace`, and you are logged in to an OpenShift Container Platform cluster, `kn` searches for the service in the subdirectory that is named after the current namespace. Otherwise, `kn` searches in the `default/` subdirectory.

. Use the service descriptor file to create the service on the cluster:
+
[source,terminal]
----
$ kn service create -f test/ksvc/event-display.yaml
----
+
.Example output
[source,terminal]
----
Creating service 'event-display' in namespace 'test':

  0.058s The Route is still working to reflect the latest desired specification.
  0.098s ...
  0.168s Configuration "event-display" is waiting for a Revision to become ready.
 23.377s ...
 23.419s Ingress has not yet been reconciled.
 23.534s Waiting for load balancer to be ready
 23.723s Ready to serve.

Service 'event-display' created to latest revision 'event-display-00001' is available at URL:
http://event-display-test.apps.example.com
----

[id="additional-resources_serverless-applications"]
[role="_additional-resources"]
== Additional resources
* Knative Serving CLI commands
* Configuring JSON Web Token authentication for Knative services
