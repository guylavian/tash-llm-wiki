---
title: "Adding annotations to functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-annotations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-annotations
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Adding annotations to functions

[id="serverless-functions-attributes"]
= Adding annotations to functions

You can add Kubernetes annotations to a deployed Serverless function. Annotations enable you to attach arbitrary metadata to a function, for example, a note about the function's purpose. Annotations are added to the `annotations` section of the `func.yaml` configuration file.

There are two limitations of the function annotation feature:

* After a function annotation propagates to the corresponding Knative service on the cluster, it cannot be removed from the service by deleting it from the `func.yaml` file. You must remove the annotation from the Knative service by modifying the YAML file of the service directly, or by using the OpenShift Container Platform web console.

* You cannot set annotations that are set by Knative, for example, the `autoscaling` annotations.

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-annotations.adoc

[id="serverless-functions-adding-annotations_{context}"]
= Adding annotations to a function

You can add annotations to a function. Similar to a label, an annotation is defined as a key-value map. Annotations are useful, for example, for providing metadata about a function, such as the function's author.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For every annotation that you want to add, add the following YAML to the `annotations` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
annotations:
  <annotation_name>: "<annotation_value>" <1>
----
<1> Substitute `<annotation_name>: "<annotation_value>"` with your annotation.
+
For example, to indicate that a function was authored by Alice, you might include the following annotation:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
annotations:
  author: "alice@example.com"
----

. Save the configuration.

The next time you deploy your function to the cluster, the annotations are added to the corresponding Knative service.
