---
title: "Creating an API server source"
type: reference
domain: openshift
slug: serverless-4-22-serverless-apiserversource
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-apiserversource
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Creating an API server source

[id="serverless-apiserversource"]
= Creating an API server source

The API server source is an event source that can be used to connect an event sink, such as a Knative service, to the Kubernetes API server. The API server source watches for Kubernetes events and forwards them to the Knative Eventing broker.

// dev console
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-apiserversource.adoc

[id="odc-creating-apiserversource_{context}"]
= Creating an API server source by using the web console

After Knative Eventing is installed on your cluster, you can create an API server source by using the web console. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create an event source.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. In the *Developer* perspective, navigate to *+Add* → *Event Source*. The  *Event Sources* page is displayed.
. Optional: If you have multiple providers for your event sources, select the required provider from the *Providers* list to filter the available event sources from the provider.
. Select *ApiServerSource* and then click *Create Event Source*. The  *Create Event Source* page is displayed.
. Configure the *ApiServerSource* settings by using the *Form view* or *YAML view*:
+
[NOTE]
====
You can switch between the *Form view* and *YAML view*. The data is persisted when switching between the views.
====
.. Enter `v1` as the *APIVERSION* and `Event` as the *KIND*.
// .. Select *Resource* as the *Mode*. *Mode* is the mode that the receive adapter controller runs in. `Ref` sends only the reference to the resource. `Resource` sends the full resource.
// TODO: clarify what this is used for. Out of scope for this PR since not required.
.. Select the *Service Account Name* for the service account that you created.
.. Select the *Sink* for the event source. A *Sink* can be either a *Resource*, such as a channel, broker, or service, or a *URI*.
. Click *Create*.

.Verification

* After you have created the API server source, you will see it connected to the service it is sinked to in the *Topology* view.
+
image::toplogy-odc-apiserver.png[ApiServerSource Topology view]

[NOTE]
====
If a URI sink is used, modify the URI by right-clicking on *URI sink* -> *Edit URI*.
====

.Deleting the API server source

. Navigate to the *Topology* view.
. Right-click the API server source and select *Delete ApiServerSource*.
+
image::delete-apiserversource-odc.png[Delete the ApiServerSource]
// kn commands
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-apiserversource.adoc
// * serverless/reference/kn-eventing-ref.adoc

[id="apiserversource-kn_{context}"]
= Creating an API server source by using the Knative CLI

You can use the `kn source apiserver create` command to create an API server source by using the `kn` CLI. Using the `kn` CLI to create an API server source provides a more streamlined and intuitive user interface than modifying YAML files directly.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have installed the OpenShift CLI (`oc`).
* You have installed the Knative (`kn`) CLI.

.Procedure

. Create an API server source that has an event sink. In the following example, the sink is a broker:
+
[source,terminal]
----
$ kn source apiserver create <event_source_name> --sink broker:<broker_name> --resource "event:v1" --service-account <service_account_name> --mode Resource
----
// need to revisit these docs and give better tutorial examples with different sinks; out of scope for the current PR

. To check that the API server source is set up correctly, create a Knative service that dumps incoming messages to its log:
+
[source,terminal]
----
$ kn service create <service_name> --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----

. If you used a broker as an event sink, create a trigger to filter events from the `default` broker to the service:
+
[source,terminal]
----
$ kn trigger create <trigger_name> --sink ksvc:<service_name>
----

. Create events by launching a pod in the default namespace:
+
[source,terminal]
----
$ oc create deployment hello-node --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----

. Check that the controller is mapped correctly by inspecting the output generated by the following command:
+
[source,terminal]
----
$ kn source apiserver describe <source_name>
----
+
.Example output
[source,terminal]
----
Name:                mysource
Namespace:           default
Annotations:         sources.knative.dev/creator=developer, sources.knative.dev/lastModifier=developer
Age:                 3m
ServiceAccountName:  events-sa
Mode:                Resource
Sink:
  Name:       default
  Namespace:  default
  Kind:       Broker (eventing.knative.dev/v1)
Resources:
  Kind:        event (v1)
  Controller:  false
Conditions:
  OK TYPE                     AGE REASON
  ++ Ready                     3m
  ++ Deployed                  3m
  ++ SinkProvided              3m
  ++ SufficientPermissions     3m
  ++ EventTypesProvided        3m
----

.Verification

You can verify that the Kubernetes events were sent to Knative by looking at the message dumper function logs.

. Get the pods:
+
[source,terminal]
----
$ oc get pods
----

. View the message dumper function logs for the pods:
+
[source,terminal]
----
$ oc logs $(oc get pod -o name | grep event-display) -c user-container
----
+
.Example output
[source,terminal]
----
☁️  cloudevents.Event
Validation: valid
Context Attributes,
  specversion: 1.0
  type: dev.knative.apiserver.resource.update
  datacontenttype: application/json
  ...
Data,
  {
    "apiVersion": "v1",
    "involvedObject": {
      "apiVersion": "v1",
      "fieldPath": "spec.containers{hello-node}",
      "kind": "Pod",
      "name": "hello-node",
      "namespace": "default",
       .....
    },
    "kind": "Event",
    "message": "Started container",
    "metadata": {
      "name": "hello-node.159d7608e3a3572c",
      "namespace": "default",
      ....
    },
    "reason": "Started",
    ...
  }
----

.Deleting the API server source

. Delete the trigger:
+
[source,terminal]
----
$ kn trigger delete <trigger_name>
----

. Delete the event source:
+
[source,terminal]
----
$ kn source apiserver delete <source_name>
----

. Delete the service account, cluster role, and cluster binding:
+
[source,terminal]
----
$ oc delete -f authentication.yaml
----
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-event-sinks.adoc
// * serverless/eventing/event-sources/serverless-apiserversource.adoc
// * serverless/eventing/event-sources/serverless-custom-event-sources.adoc
// * serverless/develop/serverless-kafka-developer.adoc
// * serverless/reference/kn-flags-reference.adoc

[id="specifying-sink-flag-kn_{context}"]
= Knative CLI sink flag

When you create an event source by using the Knative (`kn`) CLI, you can specify a sink where events are sent to from that resource by using the `--sink` flag. The sink can be any addressable or callable resource that can receive incoming events from other resources.

The following example creates a sink binding that uses a service, `\http://event-display.svc.cluster.local`, as the sink:

.Example command using the sink flag
[source,terminal]
----
$ kn source binding create bind-heartbeat \
  --namespace sinkbinding-example \
  --subject "Job:batch/v1:app=heartbeat-cron" \
  --sink http://event-display.svc.cluster.local \ <1>
  --ce-override "sink=bound"
----
<1> `svc` in `\http://event-display.svc.cluster.local` determines that the sink is a Knative service. Other default sink prefixes include `channel`, and `broker`.
// YAML
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-apiserversource.adoc

[id="apiserversource-yaml_{context}"]
= Creating an API server source by using YAML files

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe event sources declaratively and in a reproducible manner. To create an API server source by using YAML, you must create a YAML file that defines an `ApiServerSource` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have created the `default` broker in the same namespace as the one defined in the API server source YAML file.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create an API server source as a YAML file:
+
[source,yaml]
----
apiVersion: sources.knative.dev/v1alpha1
kind: ApiServerSource
metadata:
  name: testevents
spec:
  serviceAccountName: events-sa
  mode: Resource
  resources:
    - apiVersion: v1
      kind: Event
  sink:
    ref:
      apiVersion: eventing.knative.dev/v1
      kind: Broker
      name: default
----

. Apply the `ApiServerSource` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. To check that the API server source is set up correctly, create a Knative service as a YAML file that dumps incoming messages to its log:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: event-display
  namespace: default
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----

. Apply the `Service` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create a `Trigger` object as a YAML file that filters events from the `default` broker to the service created in the previous step:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Trigger
metadata:
  name: event-display-trigger
  namespace: default
spec:
  broker: default
  subscriber:
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: event-display
----

. Apply the `Trigger` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create events by launching a pod in the default namespace:
+
[source,terminal]
----
$ oc create deployment hello-node --image=quay.io/openshift-knative/knative-eventing-sources-event-display
----

. Check that the controller is mapped correctly, by entering the following command and inspecting the output:
+
[source,terminal]
----
$ oc get apiserversource.sources.knative.dev testevents -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: sources.knative.dev/v1alpha1
kind: ApiServerSource
metadata:
  annotations:
  creationTimestamp: "2020-04-07T17:24:54Z"
  generation: 1
  name: testevents
  namespace: default
  resourceVersion: "62868"
  selfLink: /apis/sources.knative.dev/v1alpha1/namespaces/default/apiserversources/testevents2
  uid: 1603d863-bb06-4d1c-b371-f580b4db99fa
spec:
  mode: Resource
  resources:
  - apiVersion: v1
    controller: false
    controllerSelector:
      apiVersion: ""
      kind: ""
      name: ""
      uid: ""
    kind: Event
    labelSelector: {}
  serviceAccountName: events-sa
  sink:
    ref:
      apiVersion: eventing.knative.dev/v1
      kind: Broker
      name: default
----

.Verification

To verify that the Kubernetes events were sent to Knative, you can look at the message dumper function logs.

. Get the pods by entering the following command:
+
[source,terminal]
----
$ oc get pods
----
. View the message dumper function logs for the pods by entering the following command:
+
[source,terminal]
----
$ oc logs $(oc get pod -o name | grep event-display) -c user-container
----
+
.Example output
[source,terminal]
----
☁️  cloudevents.Event
Validation: valid
Context Attributes,
  specversion: 1.0
  type: dev.knative.apiserver.resource.update
  datacontenttype: application/json
  ...
Data,
  {
    "apiVersion": "v1",
    "involvedObject": {
      "apiVersion": "v1",
      "fieldPath": "spec.containers{hello-node}",
      "kind": "Pod",
      "name": "hello-node",
      "namespace": "default",
       .....
    },
    "kind": "Event",
    "message": "Started container",
    "metadata": {
      "name": "hello-node.159d7608e3a3572c",
      "namespace": "default",
      ....
    },
    "reason": "Started",
    ...
  }
----

.Deleting the API server source

. Delete the trigger:
+
[source,terminal]
----
$ oc delete -f trigger.yaml
----

. Delete the event source:
+
[source,terminal]
----
$ oc delete -f k8s-events.yaml
----

. Delete the service account, cluster role, and cluster binding:
+
[source,terminal]
----
$ oc delete -f authentication.yaml
----
