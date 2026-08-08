---
title: "kn service commands in offline mode"
type: reference
domain: openshift
slug: serverless-4-22-kn-service-offline
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kn-service-offline
version: 4.22
family: serverless
documentKind: "Documentation"
---

# kn service commands in offline mode

[id="kn-service-offline"]
= kn service commands in offline mode

// offline mode
// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

[id="kn-service-offline-about_{context}"]
= About the Knative CLI offline mode

When you execute `kn service` commands, the changes immediately propagate to the cluster. However, as an alternative, you can execute `kn service` commands in offline mode. When you create a service in offline mode, no changes happen on the cluster, and instead the service descriptor file is created on your local machine.

After the descriptor file is created, you can manually modify it and track it in a version control system. You can also propagate changes to the cluster by using the `kn service create -f`, `kn service apply -f`, or `oc apply -f` commands on the descriptor files.
// Once `update` works, add it here and make it into a list

The offline mode has several uses:

* You can manually modify the descriptor file before using it to make changes on the cluster.
* You can locally track the descriptor file of a service in a version control system. This enables you to reuse the descriptor file in places other than the target cluster, for example in continuous integration (CI) pipelines, development environments, or demos.
* You can examine the created descriptor files to learn about Knative services. In particular, you can see how the resulting service is influenced by the different arguments passed to the `kn` command.

The offline mode has its advantages: it is fast, and does not require a connection to the cluster. However, offline mode lacks server-side validation. Consequently, you cannot, for example, verify that the service name is unique or that the specified image can be pulled.
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
