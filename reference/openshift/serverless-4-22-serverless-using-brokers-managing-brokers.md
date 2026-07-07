---
title: "Managing brokers"
type: reference
domain: openshift
slug: serverless-4-22-serverless-using-brokers-managing-brokers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-using-brokers-managing-brokers
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Managing brokers

[id="serverless-using-brokers-managing-brokers"]
= Managing brokers

The Knative (`kn`) CLI provides commands that can be used to describe and list existing brokers.

// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-list-broker-kn_{context}"]
= Listing existing brokers by using the Knative CLI

Using the Knative (`kn`) CLI to list brokers provides a streamlined and intuitive user interface. You can use the `kn broker list` command to list existing brokers in your cluster by using the Knative CLI.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* List all existing brokers:
+
[source,terminal]
----
$ kn broker list
----
+
.Example output
[source,terminal]
----
NAME      URL                                                                     AGE   CONDITIONS   READY   REASON
default   http://broker-ingress.knative-eventing.svc.cluster.local/test/default   45s   5 OK / 5     True
----
// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-describe-broker-kn_{context}"]
= Describing an existing broker by using the Knative CLI

Using the Knative (`kn`) CLI to describe brokers provides a streamlined and intuitive user interface. You can use the `kn broker describe` command to print information about existing brokers in your cluster by using the Knative CLI.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* Describe an existing broker:
+
[source,terminal]
----
$ kn broker describe <broker_name>
----
+
.Example command using default broker
[source,terminal]
----
$ kn broker describe default
----
+
.Example output
[source,terminal]
----
Name:         default
Namespace:    default
Annotations:  eventing.knative.dev/broker.class=MTChannelBasedBroker, eventing.knative.dev/creato ...
Age:          22s

Address:
  URL:    http://broker-ingress.knative-eventing.svc.cluster.local/default/default

Conditions:
  OK TYPE                   AGE REASON
  ++ Ready                  22s
  ++ Addressable            22s
  ++ FilterReady            22s
  ++ IngressReady           22s
  ++ TriggerChannelReady    22s
----
