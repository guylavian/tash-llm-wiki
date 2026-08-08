---
title: "Describe triggers from the command line"
type: reference
domain: openshift
slug: serverless-4-22-describe-triggers-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/describe-triggers-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Describe triggers from the command line

[id="describe-triggers-cli"]
= Describe triggers from the command line

Using the Knative (`kn`) CLI to describe triggers provides a streamlined and intuitive user interface.

// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/describe-triggers-cli.adoc

[id="kn-trigger-describe_{context}"]
= Describing a trigger by using the Knative CLI

You can use the `kn trigger describe` command to print information about existing triggers in your cluster by using the Knative CLI.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a trigger.

.Procedure

* Enter the command:
+
[source,terminal]
----
$ kn trigger describe <trigger_name>
----
+
.Example output
[source,terminal]
----
Name:         ping
Namespace:    default
Labels:       eventing.knative.dev/broker=default
Annotations:  eventing.knative.dev/creator=kube:admin, eventing.knative.dev/lastModifier=kube:admin
Age:          2m
Broker:       default
Filter:
  type:       dev.knative.event

Sink:
  Name:       edisplay
  Namespace:  default
  Resource:   Service (serving.knative.dev/v1)

Conditions:
  OK TYPE                  AGE REASON
  ++ Ready                  2m
  ++ BrokerReady            2m
  ++ DependencyReady        2m
  ++ Subscribed             2m
  ++ SubscriberResolved     2m
----
