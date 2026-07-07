---
title: "EmptyDir volumes"
type: reference
domain: openshift
slug: serverless-4-22-empty-dir
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/empty-dir
version: 4.22
family: serverless
documentKind: "Documentation"
---

# EmptyDir volumes

[id="empty-dir"]
= EmptyDir volumes

`emptyDir` volumes are empty volumes that are created when a pod is created, and are used to provide temporary working disk space. `emptyDir` volumes are deleted when the pod they were created for is deleted.

// enable emptydirs
// Module included in the following assemblies:
//
// * serverless/knative-serving/config-applications/serverless-configuration.adoc

[id="serverless-config-emptydir_{context}"]
= Configuring the EmptyDir extension
// should probably be a procedure doc, but this is out of scope for the abstracts PR

The `kubernetes.podspec-volumes-emptydir` extension controls whether `emptyDir` volumes can be used with Knative Serving. To enable using `emptyDir` volumes, you must modify the `KnativeServing` custom resource (CR) to include the following YAML:

.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    features:
      kubernetes.podspec-volumes-emptydir: enabled
...
----
