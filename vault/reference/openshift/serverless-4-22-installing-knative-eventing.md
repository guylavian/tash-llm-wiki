---
title: "Installing Knative Eventing"
type: reference
domain: openshift
slug: serverless-4-22-installing-knative-eventing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/installing-knative-eventing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Installing Knative Eventing

[id="installing-knative-eventing"]
= Installing Knative Eventing

To use event-driven architecture on your cluster, install Knative Eventing. You can create Knative components such as event sources, brokers, and channels and then use them to send events to applications or external systems.

After you install the {ServerlessOperatorName}, you can install Knative Eventing by using the default settings, or configure more advanced settings in the `KnativeEventing` custom resource (CR). For more information about configuration options for the `KnativeEventing` CR, see Global configuration.

[IMPORTANT]
====
If you want to use {DTProductName} with {ServerlessProductName}, you must install and configure {DTProductName} before you install Knative Eventing.
====

// Module included in the following assemblies:
//
//  * /serverless/install/installing-knative-eventing.adoc

[id="serverless-install-eventing-web-console_{context}"]
= Installing Knative Eventing by using the web console

After you install the {ServerlessOperatorName}, install Knative Eventing by using the OpenShift Container Platform web console. You can install Knative Eventing by using the default settings or configure more advanced settings in the `KnativeEventing` custom resource (CR).

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* You have logged in to the OpenShift Container Platform web console.
* You have installed the {ServerlessOperatorName}.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators*.

. Check that the *Project* dropdown at the top of the page is set to *Project: knative-eventing*.

. Click *Knative Eventing* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Eventing* tab.

. Click *Create Knative Eventing*.

. In the *Create Knative Eventing* page, you can choose to configure the `KnativeEventing` object by using either the default form provided, or by editing the YAML.

* Using the form is recommended for simpler configurations that do not require full control of `KnativeEventing` object creation.
+
Optional. If you are configuring the `KnativeEventing` object using the form, make any changes that you want to implement for your Knative Eventing deployment.

. Click *Create*.
+
* Editing the YAML is recommended for more complex configurations that require full control of `KnativeEventing` object creation. You can access the YAML by clicking the *edit YAML* link in the top right of the *Create Knative Eventing* page.
+
Optional. If you are configuring the `KnativeEventing` object by editing the YAML, make any changes to the YAML that you want to implement for your Knative Eventing deployment.

. Click *Create*.

. After you have installed Knative Eventing, the `KnativeEventing` object is created, and you are automatically directed to the *Knative Eventing* tab. You will see the `knative-eventing` custom resource in the list of resources.

.Verification

. Click on the `knative-eventing` custom resource in the *Knative Eventing* tab.

. You are automatically directed to the *Knative Eventing Overview* page.
+
image::eventing-overview.png[Knative Eventing Overview page]

. Scroll down to look at the list of *Conditions*.

. You should see a list of conditions with a status of *True*, as shown in the example image.
+
image::eventing-conditions-true.png[Conditions]
+
[NOTE]
====
It may take a few seconds for the Knative Eventing resources to be created. You can check their status in the *Resources* tab.
====

. If the conditions have a status of *Unknown* or *False*, wait a few moments and then check again after you have confirmed that the resources have been created.
// Module included in the following assemblies:
//
// * /serverless/install/installing-knative-eventing.adoc

[id="serverless-install-eventing-yaml_{context}"]
= Installing Knative Eventing by using YAML

After you install the {ServerlessOperatorName}, you can install Knative Eventing by using the default settings, or configure more advanced settings in the `KnativeEventing` custom resource (CR). You can use the following procedure to install Knative Eventing by using YAML files and the `oc` CLI.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* You have installed the {ServerlessOperatorName}.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a file named `eventing.yaml`.
. Copy the following sample YAML into `eventing.yaml`:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
    name: knative-eventing
    namespace: knative-eventing
----
. Optional. Make any changes to the YAML that you want to implement for your Knative Eventing deployment.
. Apply the `eventing.yaml` file by entering:
+
[source,terminal]
----
$ oc apply -f eventing.yaml
----

.Verification

. Verify the installation is complete by entering the following command and observing the output:
+
[source,terminal]
----
$ oc get knativeeventing.operator.knative.dev/knative-eventing \
  -n knative-eventing \
  --template='{{range .status.conditions}}{{printf "%s=%s\n" .type .status}}{{end}}'
----
+
.Example output
[source,terminal]
----
InstallSucceeded=True
Ready=True
----
+
[NOTE]
====
It may take a few seconds for the Knative Eventing resources to be created.
====
. If the conditions have a status of `Unknown` or `False`, wait a few moments and then check again after you have confirmed that the resources have been created.
. Check that the Knative Eventing resources have been created by entering:
+
[source,terminal]
----
$ oc get pods -n knative-eventing
----
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
broker-controller-58765d9d49-g9zp6     1/1     Running   0          7m21s
eventing-controller-65fdd66b54-jw7bh   1/1     Running   0          7m31s
eventing-webhook-57fd74b5bd-kvhlz      1/1     Running   0          7m31s
imc-controller-5b75d458fc-ptvm2        1/1     Running   0          7m19s
imc-dispatcher-64f6d5fccb-kkc4c        1/1     Running   0          7m18s
----

// Module is included in the following assemblies:
//
// serverless/install/installing-knative-eventing.adoc

[id="serverless-install-kafka-odc_{context}"]
= Installing Knative broker for Apache Kafka

The Knative broker implementation for Apache Kafka provides integration options for you to use supported versions of the Apache Kafka message streaming platform with {ServerlessProductName}. Knative broker for Apache Kafka functionality is available in an {ServerlessProductName} installation if you have installed the `KnativeKafka` custom resource.

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Eventing on your cluster.
* You have access to a Red Hat AMQ Streams cluster.
* Install the OpenShift CLI (`oc`) if you want to use the verification steps.

// OCP
* You have cluster administrator permissions on OpenShift Container Platform.

// OSD and ROSA
* You have cluster or dedicated administrator permissions on OpenShift Container Platform.

* You are logged in to the OpenShift Container Platform web console.

.Procedure

. In the *Administrator* perspective, navigate to *Ecosystem* -> *Installed Operators*.

. Check that the *Project* dropdown at the top of the page is set to *Project: knative-eventing*.

. In the list of *Provided APIs* for the {ServerlessOperatorName}, find the *Knative Kafka* box and click *Create Instance*.

. Configure the *KnativeKafka* object in the *Create Knative Kafka* page.
+
[IMPORTANT]
====
To use the Kafka channel, source, broker, or sink on your cluster, you must toggle the *enabled* switch for the options you want to use to *true*. These switches are set to *false* by default. Additionally, to use the Kafka channel, broker, or sink you must specify the bootstrap servers.
====
+
.Example `KnativeKafka` custom resource
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
    name: knative-kafka
    namespace: knative-eventing
spec:
    channel:
        enabled: true <1>
        bootstrapServers: <bootstrap_servers> <2>
    source:
        enabled: true <3>
    broker:
        enabled: true <4>
        defaultConfig:
            bootstrapServers: <bootstrap_servers> <5>
            numPartitions: <num_partitions> <6>
            replicationFactor: <replication_factor> <7>
    sink:
        enabled: true <8>
----
<1> Enables developers to use the `KafkaChannel` channel type in the cluster.
<2> A comma-separated list of bootstrap servers from your AMQ Streams cluster.
<3> Enables developers to use the `KafkaSource` event source type in the cluster.
<4> Enables developers to use the Knative broker implementation for Apache Kafka in the cluster.
<5> A comma-separated list of bootstrap servers from your Red Hat AMQ Streams cluster.
<6> Defines the number of partitions of the Kafka topics, backed by the `Broker` objects. The default is `10`.
<7> Defines the replication factor of the Kafka topics, backed by the `Broker` objects. The default is `3`.
<8> Enables developers to use a Kafka sink in the cluster.
+
[NOTE]
====
The `replicationFactor` value must be less than or equal to the number of nodes of your Red Hat AMQ Streams cluster.
====

.. Using the form is recommended for simpler configurations that do not require full control of *KnativeKafka* object creation.

.. Editing the YAML is recommended for more complex configurations that require full control of *KnativeKafka* object creation. You can access the YAML by clicking the *Edit YAML* link in the top right of the *Create Knative Kafka* page.

. Click *Create* after you have completed any of the optional configurations for Kafka. You are automatically directed to the *Knative Kafka* tab where *knative-kafka* is in the list of resources.

.Verification

. Click on the *knative-kafka* resource in the *Knative Kafka* tab. You are automatically directed to the *Knative Kafka Overview* page.

. View the list of *Conditions* for the resource and confirm that they have a status of *True*.
+
image::knative-kafka-overview.png[Kafka Knative Overview page showing Conditions]
+
If the conditions have a status of *Unknown* or *False*, wait a few moments to refresh the page.

. Check that the Knative broker for Apache Kafka resources have been created:
+
[source,terminal]
----
$ oc get pods -n knative-eventing
----
+
.Example output
[source,terminal]
----
NAME                                        READY   STATUS    RESTARTS   AGE
kafka-broker-dispatcher-7769fbbcbb-xgffn    2/2     Running   0          44s
kafka-broker-receiver-5fb56f7656-fhq8d      2/2     Running   0          44s
kafka-channel-dispatcher-84fd6cb7f9-k2tjv   2/2     Running   0          44s
kafka-channel-receiver-9b7f795d5-c76xr      2/2     Running   0          44s
kafka-controller-6f95659bf6-trd6r           2/2     Running   0          44s
kafka-source-dispatcher-6bf98bdfff-8bcsn    2/2     Running   0          44s
kafka-webhook-eventing-68dc95d54b-825xs     2/2     Running   0          44s
----

[id="next-steps_installing-knative-eventing"]
== Next steps

* If you want to use Knative services you can install Knative Serving.
