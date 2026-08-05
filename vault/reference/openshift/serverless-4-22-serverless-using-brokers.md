---
title: "Creating brokers"
type: reference
domain: openshift
slug: serverless-4-22-serverless-using-brokers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-using-brokers
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Creating brokers

[id="serverless-using-brokers"]
= Creating brokers

Knative provides a default, channel-based broker implementation. This channel-based broker can be used for development and testing purposes, but does not provide adequate event delivery guarantees for production environments.

If a cluster administrator has configured your {ServerlessProductName} deployment to use Apache Kafka as the default broker type, creating a broker by using the default settings creates a Knative broker for Apache Kafka.

If your {ServerlessProductName} deployment is not configured to use the Knative broker for Apache Kafka as the default broker type, the channel-based broker is created when you use the default settings in the following procedures.

// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-create-broker-kn_{context}"]
= Creating a broker by using the Knative CLI

Brokers can be used in combination with triggers to deliver events from an event source to an event sink. Using the Knative (`kn`) CLI to create brokers provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn broker create` command to create a broker.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a broker:
+
[source,terminal]
----
$ kn broker create <broker_name>
----

.Verification

. Use the `kn` command to list all existing brokers:
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

. Optional: If you are using the OpenShift Container Platform web console, you can navigate to the *Topology* view in the *Developer* perspective, and observe that the broker exists:
+
image::odc-view-broker.png[View the broker in the web console Topology view]
// need to add separate docs for broker in ODC - out of scope for this PR
// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-creating-broker-annotation_{context}"]
= Creating a broker by annotating a trigger

Brokers can be used in combination with triggers to deliver events from an event source to an event sink. You can create a broker by adding the `eventing.knative.dev/injection: enabled` annotation to a `Trigger` object.

[IMPORTANT]
====
If you create a broker by using the `eventing.knative.dev/injection: enabled` annotation, you cannot delete this broker without cluster administrator permissions.
If you delete the broker without having a cluster administrator remove this annotation first, the broker is created again after deletion.
====

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Create a `Trigger` object as a YAML file that has the `eventing.knative.dev/injection: enabled` annotation:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Trigger
metadata:
  annotations:
    eventing.knative.dev/injection: enabled
  name: <trigger_name>
spec:
  broker: default
  subscriber: <1>
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: <service_name>
----
+
<1> Specify details about the event sink, or _subscriber_, that the trigger sends events to.

. Apply the `Trigger` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

.Verification

You can verify that the broker has been created successfully by using the `oc` CLI, or by observing it in the *Topology* view in the web console.

. Enter the following `oc` command to get the broker:
+
[source,terminal]
----
$ oc -n <namespace> get broker default
----
+
.Example output
[source,terminal]
----
NAME      READY     REASON    URL                                                                     AGE
default   True                http://broker-ingress.knative-eventing.svc.cluster.local/test/default   3m56s
----

. Optional: If you are using the OpenShift Container Platform web console, you can navigate to the *Topology* view in the *Developer* perspective, and observe that the broker exists:
+
image::odc-view-broker.png[View the broker in the web console Topology view]
// need to add separate docs for broker in ODC - out of scope for this PR
// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-creating-broker-labeling_{context}"]
= Creating a broker by labeling a namespace

Brokers can be used in combination with triggers to deliver events from an event source to an event sink. You can create the `default` broker automatically by labelling a namespace that you own or have write permissions for.

[NOTE]
====
Brokers created using this method are not removed if you remove the label. You must manually delete them.
====

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

* You have cluster or dedicated administrator permissions.

.Procedure

* Label a namespace with `eventing.knative.dev/injection=enabled`:
+
[source,terminal]
----
$ oc label namespace <namespace> eventing.knative.dev/injection=enabled
----

.Verification

You can verify that the broker has been created successfully by using the `oc` CLI, or by observing it in the *Topology* view in the web console.

. Use the `oc` command to get the broker:
+
[source,terminal]
----
$ oc -n <namespace> get broker <broker_name>
----
+
.Example command
[source,terminal]
----
$ oc -n default get broker default
----
+
.Example output
[source,terminal]
----
NAME      READY     REASON    URL                                                                     AGE
default   True                http://broker-ingress.knative-eventing.svc.cluster.local/test/default   3m56s
----

. Optional: If you are using the OpenShift Container Platform web console, you can navigate to the *Topology* view in the *Developer* perspective, and observe that the broker exists:
+
image::odc-view-broker.png[View the broker in the web console Topology view]
// need to add separate docs for broker in ODC - out of scope for this PR
// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-deleting-broker-injection_{context}"]
= Deleting a broker that was created by injection

If you create a broker by injection and later want to delete it, you must delete it manually. Brokers created by using a namespace label or trigger annotation are not deleted permanently if you remove the label or annotation.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Remove the `eventing.knative.dev/injection=enabled` label from the namespace:
+
[source,terminal]
----
$ oc label namespace <namespace> eventing.knative.dev/injection-
----
+
Removing the annotation prevents Knative from recreating the broker after you delete it.

. Delete the broker from the selected namespace:
+
[source,terminal]
----
$ oc -n <namespace> delete broker <broker_name>
----

.Verification

* Use the `oc` command to get the broker:
+
[source,terminal]
----
$ oc -n <namespace> get broker <broker_name>
----
+
.Example command
[source,terminal]
----
$ oc -n default get broker default
----
+
.Example output
[source,terminal]
----
No resources found.
Error from server (NotFound): brokers.eventing.knative.dev "default" not found
----
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-pingsource.adoc

[id="serverless-creating-a-broker-odc_{context}"]
= Creating a broker by using the web console

After Knative Eventing is installed on your cluster, you can create a broker by using the web console. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a broker.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName}, Knative Serving and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. In the *Developer* perspective, navigate to *+Add* -> *Broker*. The *Broker* page is displayed.

. Optional. Update the *Name* of the broker. If you do not update the name, the generated broker is named `default`.

. Click *Create*.

.Verification

You can verify that the broker was created by viewing broker components in the *Topology* page.

. In the *Developer* perspective, navigate to *Topology*.

. View the `mt-broker-ingress`, `mt-broker-filter`, and `mt-broker-controller` components.
+
image::serverless-verify-broker-odc.png[View the broker components in the Topology view]
// Brokers
// Module included in the following assemblies:
//
// * serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-creating-broker-admin-web-console_{context}"]
= Creating a broker by using the Administrator perspective

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

* You have cluster administrator permissions for OpenShift Container Platform.

* You have cluster or dedicated administrator permissions for OpenShift Container Platform.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Serverless* -> *Eventing*.
. In the *Create* list, select *Broker*. You will be directed to the *Create Broker* page.
. Optional: Modify the YAML configuration for the broker.
. Click *Create*.

[id="next-steps_serverless-using-brokers"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See Examples of configuring event delivery parameters.

[id="additional-resources_serverless-using-brokers"]
[role="_additional-resources"]
== Additional resources
* Configuring the default broker class
* Triggers
Event sources
* Event delivery
