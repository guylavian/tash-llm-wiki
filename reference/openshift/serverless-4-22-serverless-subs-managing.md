---
title: "Managing subscriptions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-subs-managing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-subs-managing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Managing subscriptions

[id="serverless-subs-managing"]
= Managing subscriptions

// describe subs
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-describe-subs-kn_{context}"]
= Describing subscriptions by using the Knative CLI

You can use the `kn subscription describe` command to print information about a subscription in the terminal by using the Knative (`kn`) CLI. Using the Knative CLI to describe subscriptions provides a more streamlined and intuitive user interface than viewing YAML files directly.

.Prerequisites

* You have installed the Knative (`kn`) CLI.
* You have created a subscription in your cluster.

.Procedure

* Describe a subscription:
+
[source,terminal]
----
$ kn subscription describe <subscription_name>
----
+
.Example output
[source,terminal]
----
Name:            my-subscription
Namespace:       default
Annotations:     messaging.knative.dev/creator=openshift-user, messaging.knative.dev/lastModifier=min ...
Age:             43s
Channel:         Channel:my-channel (messaging.knative.dev/v1)
Subscriber:
  URI:           http://edisplay.default.example.com
Reply:
  Name:          default
  Resource:      Broker (eventing.knative.dev/v1)
DeadLetterSink:
  Name:          my-sink
  Resource:      Service (serving.knative.dev/v1)

Conditions:
  OK TYPE                  AGE REASON
  ++ Ready                 43s
  ++ AddedToChannel        43s
  ++ ChannelReady          43s
  ++ ReferencesResolved    43s
----
// list subs
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-list-subs-kn_{context}"]
= Listing subscriptions by using the Knative CLI

You can use the `kn subscription list` command to list existing subscriptions on your cluster by using the Knative (`kn`) CLI. Using the Knative CLI to list subscriptions provides a streamlined and intuitive user interface.

.Prerequisites

* You have installed the Knative (`kn`) CLI.

.Procedure

* List subscriptions on your cluster:
+
[source,terminal]
----
$ kn subscription list
----
+
.Example output
[source,terminal]
----
NAME             CHANNEL             SUBSCRIBER           REPLY   DEAD LETTER SINK   READY   REASON
mysubscription   Channel:mychannel   ksvc:event-display                              True
----
// . Optional: List subscriptions in YAML format:
// +
// [source,terminal]
// ----
// $ kn subscription list -o yaml
// ----
// Add this step once I have an example output, optional so non urgent
// update subs
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-update-subscriptions-kn_{context}"]
= Updating subscriptions by using the Knative CLI

You can use the `kn subscription update` command as well as the appropriate flags to update a subscription from the terminal by using the Knative (`kn`) CLI. Using the Knative CLI to update subscriptions provides a more streamlined and intuitive user interface than updating YAML files directly.

.Prerequisites

* You have installed the Knative (`kn`) CLI.
* You have created a subscription.

.Procedure

* Update a subscription:
+
[source,terminal]
----
$ kn subscription update <subscription_name> \
  --sink <sink_prefix>:<sink_name> \ <1>
  --sink-dead-letter <sink_prefix>:<sink_name> <2>
----
<1> `--sink` specifies the updated target destination to which the event should be delivered. You can specify the type of the sink by using one of the following prefixes:
`ksvc`:: A Knative service.
`channel`:: A channel that should be used as destination. Only default channel types can be referenced here.
`broker`:: An Eventing broker.
<2> Optional: `--sink-dead-letter` is an optional flag that can be used to specify a sink which events should be sent to in cases where events fail to be delivered. For more information, see the {ServerlessProductName} _Event delivery_ documentation.
+
.Example command
[source,terminal]
----
$ kn subscription update mysubscription --sink ksvc:event-display
----
