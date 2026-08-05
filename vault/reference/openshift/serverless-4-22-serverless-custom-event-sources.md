---
title: "Custom event sources"
type: reference
domain: openshift
slug: serverless-4-22-serverless-custom-event-sources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-custom-event-sources
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Custom event sources

[id="serverless-custom-event-sources"]
= Custom event sources

If you need to ingress events from an event producer that is not included in Knative, or from a producer that emits events which are not in the `CloudEvent` format, you can do this by creating a custom event source. You can create a custom event source by using one of the following methods:

* Use a `PodSpecable` object as an event source, by creating a sink binding.
* Use a container as an event source, by creating a container source.

// sinkbinding intro
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-sinkbinding-intro_{context}"]
= Sink binding

The `SinkBinding` object supports decoupling event production from delivery addressing. Sink binding is used to connect _event producers_ to an event consumer, or _sink_. An event producer is a Kubernetes resource that embeds a `PodSpec` template and produces events. A sink is an addressable Kubernetes object that can receive events.

The `SinkBinding` object injects environment variables into the `PodTemplateSpec` of the sink, which means that the application code does not need to interact directly with the Kubernetes API to locate the event destination. These environment variables are as follows:

`K_SINK`:: The URL of the resolved sink.
`K_CE_OVERRIDES`:: A JSON object that specifies overrides to the outbound event.

[NOTE]
====
The `SinkBinding` object currently does not support custom revision names for services.
====
// YAML
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-sinkbinding-yaml_{context}"]
= Creating a sink binding by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe event sources declaratively and in a reproducible manner. To create a sink binding by using YAML, you must create a YAML file that defines an `SinkBinding` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving and Knative Eventing are installed on the cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. To check that sink binding is set up correctly, create a Knative event display service, or event sink, that dumps incoming messages to its log.

.. Create a service YAML file:
+
.Example service YAML file
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: event-display
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
.. Create the service:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create a sink binding instance that directs events to the service.

.. Create a sink binding YAML file:
+
.Example service YAML file
[source,yaml]
----
apiVersion: sources.knative.dev/v1alpha1
kind: SinkBinding
metadata:
  name: bind-heartbeat
spec:
  subject:
    apiVersion: batch/v1
    kind: Job <1>
    selector:
      matchLabels:
        app: heartbeat-cron

  sink:
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: event-display
----
<1> In this example, any Job with the label `app: heartbeat-cron` will be bound to the event sink.

.. Create the sink binding:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create a `CronJob` object.

.. Create a cron job YAML file:
+
.Example cron job YAML file
[source,yaml]
----
apiVersion: batch/v1
kind: CronJob
metadata:
  name: heartbeat-cron
spec:
  # Run every minute
  schedule: "* * * * *"
  jobTemplate:
    metadata:
      labels:
        app: heartbeat-cron
        bindings.knative.dev/include: "true"
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: single-heartbeat
              image: quay.io/openshift-knative/heartbeats:latest
              args:
                - --period=1
              env:
                - name: ONE_SHOT
                  value: "true"
                - name: POD_NAME
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.name
                - name: POD_NAMESPACE
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.namespace
----
+
[IMPORTANT]
====
To use sink binding, you must manually add a `bindings.knative.dev/include=true` label to your Knative resources.

For example, to add this label to a `CronJob` resource, add the following lines to the `Job` resource YAML definition:

[source,yaml]
----
  jobTemplate:
    metadata:
      labels:
        app: heartbeat-cron
        bindings.knative.dev/include: "true"
----

====
+
.. Create the cron job:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Check that the controller is mapped correctly by entering the following command and inspecting the output:
+
[source,terminal]
----
$ oc get sinkbindings.sources.knative.dev bind-heartbeat -oyaml
----
+
.Example output
[source,yaml]
----
spec:
  sink:
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: event-display
      namespace: default
  subject:
    apiVersion: batch/v1
    kind: Job
    namespace: default
    selector:
      matchLabels:
        app: heartbeat-cron
----

.Verification

You can verify that the Kubernetes events were sent to the Knative event sink by looking at the message dumper function logs.

. Enter the command:
+
[source,terminal]
----
$ oc get pods
----

. Enter the command:
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
  type: dev.knative.eventing.samples.heartbeat
  source: https://knative.dev/eventing-contrib/cmd/heartbeats/#event-test/mypod
  id: 2b72d7bf-c38f-4a98-a433-608fbcdd2596
  time: 2019-10-18T15:23:20.809775386Z
  contenttype: application/json
Extensions,
  beats: true
  heart: yes
  the: 42
Data,
  {
    "id": 1,
    "label": ""
  }
----
// kn commands
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-sinkbinding-kn_{context}"]
= Creating a sink binding by using the Knative CLI

You can use the `kn source binding create` command to create a sink binding by using the Knative (`kn`) CLI. Using the Knative CLI to create event sources provides a more streamlined and intuitive user interface than modifying YAML files directly.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* Install the Knative (`kn`) CLI.
* Install the OpenShift CLI (`oc`).

[NOTE]
====
The following procedure requires you to create YAML files.

If you change the names of the YAML files from those used in the examples, you must ensure that you also update the corresponding CLI commands.
====

.Procedure

. To check that sink binding is set up correctly, create a Knative event display service, or event sink, that dumps incoming messages to its log:
+
[source,terminal]
----
$ kn service create event-display --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----

. Create a sink binding instance that directs events to the service:
+
[source,terminal]
----
$ kn source binding create bind-heartbeat --subject Job:batch/v1:app=heartbeat-cron --sink ksvc:event-display
----

. Create a `CronJob` object.

.. Create a cron job YAML file:
+
.Example cron job YAML file
[source,yaml]
----
apiVersion: batch/v1
kind: CronJob
metadata:
  name: heartbeat-cron
spec:
  # Run every minute
  schedule: "* * * * *"
  jobTemplate:
    metadata:
      labels:
        app: heartbeat-cron
        bindings.knative.dev/include: "true"
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: single-heartbeat
              image: quay.io/openshift-knative/heartbeats:latest
              args:
                - --period=1
              env:
                - name: ONE_SHOT
                  value: "true"
                - name: POD_NAME
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.name
                - name: POD_NAMESPACE
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.namespace
----
+
[IMPORTANT]
====
To use sink binding, you must manually add a `bindings.knative.dev/include=true` label to your Knative CRs.

For example, to add this label to a `CronJob` CR, add the following lines to the `Job` CR YAML definition:

[source,yaml]
----
  jobTemplate:
    metadata:
      labels:
        app: heartbeat-cron
        bindings.knative.dev/include: "true"
----

====
+
.. Create the cron job:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Check that the controller is mapped correctly by entering the following command and inspecting the output:
+
[source,terminal]
----
$ kn source binding describe bind-heartbeat
----
+
.Example output
[source,terminal]
----
Name:         bind-heartbeat
Namespace:    demo-2
Annotations:  sources.knative.dev/creator=minikube-user, sources.knative.dev/lastModifier=minikub ...
Age:          2m
Subject:
  Resource:   job (batch/v1)
  Selector:
    app:      heartbeat-cron
Sink:
  Name:       event-display
  Resource:   Service (serving.knative.dev/v1)

Conditions:
  OK TYPE     AGE REASON
  ++ Ready     2m
----

.Verification

You can verify that the Kubernetes events were sent to the Knative event sink by looking at the message dumper function logs.

* View the message dumper function logs by entering the following commands:
+
[source,terminal]
----
$ oc get pods
----
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
  type: dev.knative.eventing.samples.heartbeat
  source: https://knative.dev/eventing-contrib/cmd/heartbeats/#event-test/mypod
  id: 2b72d7bf-c38f-4a98-a433-608fbcdd2596
  time: 2019-10-18T15:23:20.809775386Z
  contenttype: application/json
Extensions,
  beats: true
  heart: yes
  the: 42
Data,
  {
    "id": 1,
    "label": ""
  }
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
// ODC
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-sinkbinding-odc_{context}"]
= Creating a sink binding by using the web console

After Knative Eventing is installed on your cluster, you can create a sink binding by using the web console. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create an event source.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Create a Knative service to use as a sink:

.. In the *Developer* perspective, navigate to *+Add* -> *YAML*.
.. Copy the example YAML:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: event-display
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
.. Click *Create*.

. Create a `CronJob` resource that is used as an event source and sends an event every minute.

.. In the *Developer* perspective, navigate to *+Add* -> *YAML*.
.. Copy the example YAML:
+
[source,yaml]
----
apiVersion: batch/v1
kind: CronJob
metadata:
  name: heartbeat-cron
spec:
  # Run every minute
  schedule: "*/1 * * * *"
  jobTemplate:
    metadata:
      labels:
        app: heartbeat-cron
        bindings.knative.dev/include: true <1>
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: single-heartbeat
              image: quay.io/openshift-knative/heartbeats
              args:
              - --period=1
              env:
                - name: ONE_SHOT
                  value: "true"
                - name: POD_NAME
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.name
                - name: POD_NAMESPACE
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.namespace
----
<1> Ensure that you include the `bindings.knative.dev/include: true` label. The default namespace selection behavior of {ServerlessProductName} uses inclusion mode.
.. Click *Create*.

. Create a sink binding in the same namespace as the service created in the previous step, or any other sink that you want to send events to.

.. In the *Developer* perspective, navigate to *+Add* -> *Event Source*. The  *Event Sources* page is displayed.
.. Optional: If you have multiple providers for your event sources, select the required provider from the *Providers* list to filter the available event sources from the provider.
.. Select *Sink Binding* and then click *Create Event Source*. The *Create Event Source* page is displayed.
+
[NOTE]
====
You can configure the *Sink Binding* settings by using the *Form view* or *YAML view* and can switch between the views. The data is persisted when switching between the views.
====
+
.. In the *apiVersion* field enter `batch/v1`.
.. In the *Kind* field enter `Job`.
+
[NOTE]
====
The `CronJob` kind is not supported directly by {ServerlessProductName} sink binding, so the *Kind* field must target the `Job` objects created by the cron job, rather than the cron job object itself.
====
.. Select a *Sink*. This can be either a *Resource* or a *URI*. In this example, the `event-display` service created in the previous step is used as the *Resource* sink.
.. In the *Match labels* section:
... Enter `app` in the *Name* field.
... Enter `heartbeat-cron` in the *Value* field.
+
[NOTE]
====
The label selector is required when using cron jobs with sink binding, rather than the resource name. This is because jobs created by a cron job do not have a predictable name, and contain a randomly generated string in their name. For example, `hearthbeat-cron-1cc23f`.
====
.. Click *Create*.

.Verification

You can verify that the sink binding, sink, and cron job have been created and are working correctly by viewing the *Topology* page and pod logs.

. In the *Developer* perspective, navigate to *Topology*.

. View the sink binding, sink, and heartbeats cron job.
+
image::verify-sinkbinding-odc.png[View the sink binding and service in the Topology view]

. Observe that successful jobs are being registered by the cron job once the sink binding is added. This means that the sink binding is successfully reconfiguring the jobs created by the cron job.

. Browse the logs of the `event-display` service pod to see events produced by the heartbeats cron job.
// Reference
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-sinkbinding-reference_{context}"]
= Sink binding reference
// this section probably needs a rewrite / restructure; feels like multiple modules maybe for a larger ref doc. Out of scope for this PR.

You can use a `PodSpecable` object as an event source by creating a sink binding. You can configure multiple parameters when creating a `SinkBinding` object.

`SinkBinding` objects support the following parameters:

[cols=3*,options="header"]
|===
|Field
|Description
|Required or optional

|`apiVersion`
|Specifies the API version, for example `sources.knative.dev/v1`.
|Required

|`kind`
|Identifies this resource object as a `SinkBinding` object.
|Required

|`metadata`
|Specifies metadata that uniquely identifies the `SinkBinding` object. For example, a `name`.
|Required

|`spec`
|Specifies the configuration information for this `SinkBinding` object.
|Required

|`spec.sink`
|A reference to an object that resolves to a URI to use as the sink.
|Required

|`spec.subject`
|References the resources for which the runtime contract is augmented by binding implementations.
|Required

|`spec.ceOverrides`
|Defines overrides to control the output format and modifications to the event sent to the sink.
|Optional

|===

[id="serverless-sinkbinding-reference-subject-parameters_{context}"]
== Subject parameter

The `Subject` parameter references the resources for which the runtime contract is augmented by binding implementations. You can configure multiple fields for a `Subject` definition.

The `Subject` definition supports the following fields:

[cols=3*,options="header"]
|===
|Field
|Description
|Required or optional

|`apiVersion`
|API version of the referent.
|Required

|`kind`
|Kind of the referent.
|Required

|`namespace`
|Namespace of the referent. If omitted, this defaults to the namespace of the object.
|Optional

|`name`
|Name of the referent.
|Do not use if you configure `selector`.

|`selector`
|Selector of the referents.
|Do not use if you configure `name`.

|`selector.matchExpressions`
|A list of label selector requirements.
|Only use one of either `matchExpressions` or `matchLabels`.

|`selector.matchExpressions.key`
|The label key that the selector applies to.
|Required if using `matchExpressions`.

|`selector.matchExpressions.operator`
|Represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.
|Required if using `matchExpressions`.

|`selector.matchExpressions.values`
|An array of string values. If the `operator` parameter value is `In` or `NotIn`, the values array must be non-empty. If the `operator` parameter value is `Exists` or `DoesNotExist`, the values array must be empty. This array is replaced during a strategic merge patch.
|Required if using `matchExpressions`.

|`selector.matchLabels`
|A map of key-value pairs. Each key-value pair in the `matchLabels` map is equivalent to an element of `matchExpressions`, where the key field is `matchLabels.<key>`, the `operator` is `In`, and the `values` array contains only `matchLabels.<value>`.
|Only use one of either `matchExpressions` or `matchLabels`.

|===

.Subject parameter examples

Given the following YAML, the `Deployment` object named `mysubject` in the `default` namespace is selected:

[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: SinkBinding
metadata:
  name: bind-heartbeat
spec:
  subject:
    apiVersion: apps/v1
    kind: Deployment
    namespace: default
    name: mysubject
  ...
----

Given the following YAML, any `Job` object with the label `working=example` in the `default` namespace is selected:

[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: SinkBinding
metadata:
  name: bind-heartbeat
spec:
  subject:
    apiVersion: batch/v1
    kind: Job
    namespace: default
    selector:
      matchLabels:
        working: example
  ...
----

Given the following YAML, any `Pod` object with the label `working=example` or `working=sample` in the `default` namespace is selected:

[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: SinkBinding
metadata:
  name: bind-heartbeat
spec:
  subject:
    apiVersion: v1
    kind: Pod
    namespace: default
    selector:
      - matchExpression:
        key: working
        operator: In
        values:
          - example
          - sample
  ...
----

[id="serverless-sinkbinding-reference-cloudevent-overrides_{context}"]
== CloudEvent overrides

A `ceOverrides` definition provides overrides that control the CloudEvent's output format and modifications sent to the sink. You can configure multiple fields for the `ceOverrides` definition.

A `ceOverrides` definition supports the following fields:

[cols=3*,options="header"]
|===
|Field
|Description
|Required or optional

|`extensions`
|Specifies which attributes are added or overridden on the outbound event. Each `extensions` key-value pair is set independently on the event as an attribute extension.
|Optional

|===

[NOTE]
====
Only valid `CloudEvent` attribute names are allowed as extensions. You cannot set the spec defined attributes from the extensions override configuration. For example, you can not modify the `type` attribute.
====

.CloudEvent Overrides example
[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: SinkBinding
metadata:
  name: bind-heartbeat
spec:
  ...
  ceOverrides:
    extensions:
      extra: this is an extra attribute
      additional: 42
----

This sets the `K_CE_OVERRIDES` environment variable on the `subject`:

.Example output
[source,terminal]
----
{ "extensions": { "extra": "this is an extra attribute", "additional": "42" } }
----

[id="serverless-sinkbinding-reference-include-label_{context}"]
== The include label

To use a sink binding, you need to do assign the `bindings.knative.dev/include: "true"` label to either the resource or the namespace that the resource is included in. If the resource definition does not include the label, a cluster administrator can attach it to the namespace by running:

[source,terminal]
----
$ oc label namespace <namespace> bindings.knative.dev/include=true
----

[id="serverless-custom-event-sources-containersource"]
== Container source

Container sources create a container image that generates events and sends events to a sink. You can use a container source to create a custom event source, by creating a container image and a `ContainerSource` object that uses your image URI.

// intro
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-containersource-guidelines_{context}"]
= Guidelines for creating a container image

Two environment variables are injected by the container source controller: `K_SINK` and `K_CE_OVERRIDES`. These variables are resolved from the `sink` and `ceOverrides` spec, respectively. Events are sent to the sink URI specified in the `K_SINK` environment variable. The message must be sent as a `POST` using the `CloudEvent` HTTP format.

.Example container images

The following is an example of a heartbeats container image:

[source,go]
----
package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"

	duckv1 "knative.dev/pkg/apis/duck/v1"

	cloudevents "github.com/cloudevents/sdk-go/v2"
	"github.com/kelseyhightower/envconfig"
)

type Heartbeat struct {
	Sequence int    `json:"id"`
	Label    string `json:"label"`
}

var (
	eventSource string
	eventType   string
	sink        string
	label       string
	periodStr   string
)

func init() {
	flag.StringVar(&eventSource, "eventSource", "", "the event-source (CloudEvents)")
	flag.StringVar(&eventType, "eventType", "dev.knative.eventing.samples.heartbeat", "the event-type (CloudEvents)")
	flag.StringVar(&sink, "sink", "", "the host url to heartbeat to")
	flag.StringVar(&label, "label", "", "a special label")
	flag.StringVar(&periodStr, "period", "5", "the number of seconds between heartbeats")
}

type envConfig struct {
	// Sink URL where to send heartbeat cloud events
	Sink string `envconfig:"K_SINK"`

	// CEOverrides are the CloudEvents overrides to be applied to the outbound event.
	CEOverrides string `envconfig:"K_CE_OVERRIDES"`

	// Name of this pod.
	Name string `envconfig:"POD_NAME" required:"true"`

	// Namespace this pod exists in.
	Namespace string `envconfig:"POD_NAMESPACE" required:"true"`

	// Whether to run continuously or exit.
	OneShot bool `envconfig:"ONE_SHOT" default:"false"`
}

func main() {
	flag.Parse()

	var env envConfig
	if err := envconfig.Process("", &env); err != nil {
		log.Printf("[ERROR] Failed to process env var: %s", err)
		os.Exit(1)
	}

	if env.Sink != "" {
		sink = env.Sink
	}

	var ceOverrides *duckv1.CloudEventOverrides
	if len(env.CEOverrides) > 0 {
		overrides := duckv1.CloudEventOverrides{}
		err := json.Unmarshal([]byte(env.CEOverrides), &overrides)
		if err != nil {
			log.Printf("[ERROR] Unparseable CloudEvents overrides %s: %v", env.CEOverrides, err)
			os.Exit(1)
		}
		ceOverrides = &overrides
	}

	p, err := cloudevents.NewHTTP(cloudevents.WithTarget(sink))
	if err != nil {
		log.Fatalf("failed to create http protocol: %s", err.Error())
	}

	c, err := cloudevents.NewClient(p, cloudevents.WithUUIDs(), cloudevents.WithTimeNow())
	if err != nil {
		log.Fatalf("failed to create client: %s", err.Error())
	}

	var period time.Duration
	if p, err := strconv.Atoi(periodStr); err != nil {
		period = time.Duration(5) * time.Second
	} else {
		period = time.Duration(p) * time.Second
	}

	if eventSource == "" {
		eventSource = fmt.Sprintf("https://knative.dev/eventing-contrib/cmd/heartbeats/#%s/%s", env.Namespace, env.Name)
		log.Printf("Heartbeats Source: %s", eventSource)
	}

	if len(label) > 0 && label[0] == '"' {
		label, _ = strconv.Unquote(label)
	}
	hb := &Heartbeat{
		Sequence: 0,
		Label:    label,
	}
	ticker := time.NewTicker(period)
	for {
		hb.Sequence++

		event := cloudevents.NewEvent("1.0")
		event.SetType(eventType)
		event.SetSource(eventSource)
		event.SetExtension("the", 42)
		event.SetExtension("heart", "yes")
		event.SetExtension("beats", true)

		if ceOverrides != nil && ceOverrides.Extensions != nil {
			for n, v := range ceOverrides.Extensions {
				event.SetExtension(n, v)
			}
		}

		if err := event.SetData(cloudevents.ApplicationJSON, hb); err != nil {
			log.Printf("failed to set cloudevents data: %s", err.Error())
		}

		log.Printf("sending cloudevent to %s", sink)
		if res := c.Send(context.Background(), event); !cloudevents.IsACK(res) {
			log.Printf("failed to send cloudevent: %v", res)
		}

		if env.OneShot {
			return
		}

		// Wait for next tick
		<-ticker.C
	}
}
----

The following is an example of a container source that references the previous heartbeats container image:

[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: ContainerSource
metadata:
  name: test-heartbeats
spec:
  template:
    spec:
      containers:
        # This corresponds to a heartbeats image URI that you have built and published
        - image: gcr.io/knative-releases/knative.dev/eventing/cmd/heartbeats
          name: heartbeats
          args:
            - --period=1
          env:
            - name: POD_NAME
              value: "example-pod"
            - name: POD_NAMESPACE
              value: "event-test"
  sink:
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: example-service
...
----
// kn
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-custom-event-sources.adoc
// * serverless/reference/kn-eventing-ref.adoc

[id="serverless-kn-containersource_{context}"]
= Creating and managing container sources by using the Knative CLI
// needs to be revised as separate procedure modules; out of scope for this PR

You can use the `kn source container` commands to create  and manage container sources by using the Knative (`kn`) CLI. Using the Knative CLI to create event sources provides a more streamlined and intuitive user interface than modifying YAML files directly.

.Create a container source
[source,terminal]
----
$ kn source container create <container_source_name> --image <image_uri> --sink <sink>
----

.Delete a container source
[source,terminal]
----
$ kn source container delete <container_source_name>
----

.Describe a container source
[source,terminal]
----
$ kn source container describe <container_source_name>
----

.List existing container sources
[source,terminal]
----
$ kn source container list
----

.List existing container sources in YAML format
[source,terminal]
----
$ kn source container list -o yaml
----

.Update a container source

This command updates the image URI for an existing container source:

[source,terminal]
----
$ kn source container update <container_source_name> --image <image_uri>
----
// ODC
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-odc-create-containersource_{context}"]
= Creating a container source by using the web console

After Knative Eventing is installed on your cluster, you can create a container source by using the web console. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create an event source.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. In the *Developer* perspective, navigate to *+Add* → *Event Source*. The  *Event Sources* page is displayed.

. Select *Container Source* and then click *Create Event Source*. The  *Create Event Source* page is displayed.

. Configure the *Container Source* settings by using the *Form view* or *YAML view*:
+
[NOTE]
====
You can switch between the *Form view* and *YAML view*. The data is persisted when switching between the views.
====
.. In the *Image* field, enter the URI of the image that you want to run in the container created by the container source.
.. In the *Name* field, enter the name of the image.
.. Optional: In the *Arguments* field, enter any arguments to be passed to the container.
// Optional? Add options and what they mean.
// Same for env variables...
.. Optional: In the *Environment variables* field, add any environment variables to set in the container.
.. In the *Sink* section, add a sink where events from the container source are routed to. If you are using the *Form* view, you can choose from the following options:
... Select *Resource* to use a channel, broker, or service as a sink for the event source.
... Select *URI* to specify where the events from the container source are routed to.

. After you have finished configuring the container source, click *Create*.
// Reference
// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

[id="serverless-containersource-reference_{context}"]
= Container source reference

You can use a container as an event source, by creating a `ContainerSource` object. You can configure multiple parameters when creating a `ContainerSource` object.

`ContainerSource` objects support the following fields:

[cols=3*,options="header"]
|===
|Field
|Description
|Required or optional

|`apiVersion`
|Specifies the API version, for example `sources.knative.dev/v1`.
|Required

|`kind`
|Identifies this resource object as a `ContainerSource` object.
|Required

|`metadata`
|Specifies metadata that uniquely identifies the `ContainerSource` object. For example, a `name`.
|Required

|`spec`
|Specifies the configuration information for this `ContainerSource` object.
|Required

|`spec.sink`
|A reference to an object that resolves to a URI to use as the sink.
|Required

|`spec.template`
|A `template` spec for the `ContainerSource` object.
|Required

|`spec.ceOverrides`
|Defines overrides to control the output format and modifications to the event sent to the sink.
|Optional

|===

.Template parameter example
[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: ContainerSource
metadata:
  name: test-heartbeats
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/heartbeats:latest
          name: heartbeats
          args:
            - --period=1
          env:
            - name: POD_NAME
              value: "mypod"
            - name: POD_NAMESPACE
              value: "event-test"
  ...
----

[id="serverless-containersource-reference-cloudevent-overrides_{context}"]
== CloudEvent overrides

A `ceOverrides` definition provides overrides that control the CloudEvent's output format and modifications sent to the sink. You can configure multiple fields for the `ceOverrides` definition.

A `ceOverrides` definition supports the following fields:

[cols=3*,options="header"]
|===
|Field
|Description
|Required or optional

|`extensions`
|Specifies which attributes are added or overridden on the outbound event. Each `extensions` key-value pair is set independently on the event as an attribute extension.
|Optional

|===

[NOTE]
====
Only valid `CloudEvent` attribute names are allowed as extensions. You cannot set the spec defined attributes from the extensions override configuration. For example, you can not modify the `type` attribute.
====

.CloudEvent Overrides example
[source,yaml]
----
apiVersion: sources.knative.dev/v1
kind: ContainerSource
metadata:
  name: test-heartbeats
spec:
  ...
  ceOverrides:
    extensions:
      extra: this is an extra attribute
      additional: 42
----

This sets the `K_CE_OVERRIDES` environment variable on the `subject`:

.Example output
[source,terminal]
----
{ "extensions": { "extra": "this is an extra attribute", "additional": "42" } }
----
