---
title: "Installing the {ServerlessOperatorName}"
type: reference
domain: openshift
slug: serverless-4-22-install-serverless-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/install-serverless-operator
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Installing the {ServerlessOperatorName}

[id="install-serverless-operator"]
= Installing the {ServerlessOperatorName}

Installing the {ServerlessOperatorName} enables you to install and use Knative Serving, Knative Eventing, and the Knative broker for Apache Kafka on a OpenShift Container Platform cluster. The {ServerlessOperatorName} manages Knative custom resource definitions (CRDs) for your cluster and enables you to configure them without directly modifying individual config maps for each component.

// universal install doc
// Module included in the following assemblies:
//
// * /serverless/install/install-serverless-operator.adoc

[id="serverless-install-web-console_{context}"]
= Installing the {ServerlessOperatorName} from the web console

You can install the {ServerlessOperatorName} from the software catalog by using the OpenShift Container Platform web console. Installing this Operator enables you to install and use Knative components.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* Your cluster has the Marketplace capability enabled or the Red Hat Operator catalog source configured manually.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have logged in to the OpenShift Container Platform web console.

.Procedure

. In the OpenShift Container Platform web console, navigate to the *Ecosystem* -> *Software Catalog* page.

. Scroll, or type the keyword *Serverless* into the *Filter by keyword* box to find the {ServerlessOperatorName}.

. Review the information about the Operator and click *Install*.

. On the *Install Operator* page:

.. The *Installation Mode* is *All namespaces on the cluster (default)*. This mode installs the Operator in the default `openshift-serverless` namespace to watch and be made available to all namespaces in the cluster.

.. The *Installed Namespace* is `openshift-serverless`.

.. Select the *stable* channel as the *Update Channel*. The *stable* channel will enable installation of the latest stable release of the {ServerlessOperatorName}.

.. Select *Automatic* or *Manual* approval strategy.

. Click *Install* to make the Operator available to the selected namespaces on this OpenShift Container Platform cluster.

. From the *Catalog* -> *Operator Management* page, you can monitor the {ServerlessOperatorName} subscription's installation and upgrade progress.

.. If you selected a *Manual* approval strategy, the subscription's upgrade status will remain *Upgrading* until you review and approve its install plan. After approving on the *Install Plan* page, the subscription upgrade status moves to *Up to date*.

.. If you selected an *Automatic* approval strategy, the upgrade status should resolve to *Up to date* without intervention.

.Verification

After the Subscription's upgrade status is *Up to date*, select *Catalog* -> *Installed Operators* to verify that the {ServerlessOperatorName} eventually shows up and its *Status* ultimately resolves to *InstallSucceeded* in the relevant namespace.

If it does not:

. Switch to the *Catalog* -> *Operator Management* page and inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.

. Check the logs in any pods in the `openshift-serverless` project on the *Workloads* -> *Pods* page that are reporting issues to troubleshoot further.

[IMPORTANT]
====
If you want to use {DTProductName} with {ServerlessProductName}, you must install and configure {DTProductName} before you install Knative Serving or Knative Eventing.
====

// Module included in the following assemblies:
//
// * /serverless/install/install-serverless-operator.adoc

[id="serverless-install-cli_{context}"]
= Installing the {ServerlessOperatorName} from the CLI

You can install the {ServerlessOperatorName} from the software catalog by using the CLI. Installing this Operator enables you to install and use Knative components.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* Your cluster has the Marketplace capability enabled or the Red Hat Operator catalog source configured manually.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have logged in to the OpenShift Container Platform cluster.

.Procedure
. Create a YAML file containing `Namespace`, `OperatorGroup`, and `Subscription` objects to subscribe a namespace to the {ServerlessOperatorName}. For example, create the file `serverless-subscription.yaml` with the following content:
+
.Example subscription
[source,yaml]
----
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-serverless
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: serverless-operators
  namespace: openshift-serverless
spec: {}
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: serverless-operator
  namespace: openshift-serverless
spec:
  channel: stable <1>
  name: serverless-operator <2>
  source: redhat-operators <3>
  sourceNamespace: openshift-marketplace <4>
----
<1> The channel name of the Operator. The `stable` channel enables installation of the most recent stable version of the {ServerlessOperatorName}.
<2> The name of the Operator to subscribe to. For the {ServerlessOperatorName}, this is always `serverless-operator`.
<3> The name of the CatalogSource that provides the Operator. Use `redhat-operators` for the default software catalog sources.
<4> The namespace of the CatalogSource. Use `openshift-marketplace` for the default software catalog sources.

. Create the `Subscription` object:
+
----
$ oc apply -f serverless-subscription.yaml
----

.Verification
Check that the cluster service version (CSV) has reached the `Succeeded` phase:

.Example command
[source,yaml]
----
$ oc get csv
----

.Example output
[source,yaml]
----
NAME                          DISPLAY                        VERSION   REPLACES                      PHASE
serverless-operator.v1.25.0   Red Hat OpenShift Serverless   1.25.0    serverless-operator.v1.24.0   Succeeded
----

[IMPORTANT]
====
If you want to use {DTProductName} with {ServerlessProductName}, you must install and configure {DTProductName} before you install Knative Serving or Knative Eventing.
====

[id="serverless-configuration"]
== Global configuration

The {ServerlessOperatorName} manages the global configuration of a Knative installation, including propagating values from the `KnativeServing` and `KnativeEventing` custom resources to system config maps. Any updates to config maps which are applied manually are overwritten by the Operator. However, modifying the Knative custom resources allows you to set values for these config maps.

Knative has multiple config maps that are named with the prefix `config-`. All Knative config maps are created in the same namespace as the custom resource that they apply to. For example, if the `KnativeServing` custom resource is created in the `knative-serving` namespace, all Knative Serving config maps are also created in this namespace.

The `spec.config` in the Knative custom resources have one `<name>` entry for each config map, named `config-<name>`, with a value which is be used for the config map `data`.

[id="additional-resources_knative-serving-CR-config"]
[role="_additional-resources"]
== Additional resources
* Managing resources from custom resource definitions
* Understanding persistent storage
* Configuring a custom PKI

[id="next-steps_install-serverless-operator"]
== Next steps

* After the {ServerlessOperatorName} is installed, you can install Knative Serving or install Knative Eventing.
