---
title: "Customizing labels and annotations"
type: reference
domain: openshift
slug: serverless-4-22-customize-labels-annotations-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/customize-labels-annotations-routes
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Customizing labels and annotations

[id="customize-labels-annotations-routes"]
= Customizing labels and annotations

OpenShift Container Platform routes support the use of custom labels and annotations, which you can configure by modifying the `metadata` spec of a Knative service. Custom labels and annotations are propagated from the service to the Knative route, then to the Knative ingress, and finally to the OpenShift Container Platform route.

// Module included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/customize-labels-annotations-routes.adoc

[id="serverless-customize-labels-annotations-routes_{context}"]
= Customizing labels and annotations for OpenShift Container Platform routes

.Prerequisites

* You must have the {ServerlessOperatorName} and Knative Serving installed on your OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a Knative service that contains the label or annotation that you want to propagate to the OpenShift Container Platform route:
** To create a service by using YAML:
+
.Example service created by using YAML
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: <service_name>
  labels:
    <label_name>: <label_value>
  annotations:
    <annotation_name>: <annotation_value>
...
----
** To create a service by using the Knative (`kn`) CLI, enter:
+
.Example service created by using a `kn` command
[source,terminal]
----
$ kn service create <service_name> \
  --image=<image> \
  --annotation <annotation_name>=<annotation_value> \
  --label <label_value>=<label_value>
----

. Verify that the OpenShift Container Platform route has been created with the annotation or label that you added by inspecting the output from the following command:
+
.Example command for verification
[source,terminal]
----
$ oc get routes.route.openshift.io \
     -l serving.knative.openshift.io/ingressName=<service_name> \ <1>
     -l serving.knative.openshift.io/ingressNamespace=<service_namespace> \ <2>
     -n knative-serving-ingress -o yaml \
         | grep -e "<label_name>: \"<label_value>\""  -e "<annotation_name>: <annotation_value>" <3>
----
<1> Use the name of your service.
<2> Use the namespace where your service was created.
<3> Use your values for the label and annotation names and values.
