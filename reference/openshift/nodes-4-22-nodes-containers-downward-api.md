---
title: "Allowing containers to consume API objects"
type: reference
domain: openshift
slug: nodes-4-22-nodes-containers-downward-api
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-containers-downward-api
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Allowing containers to consume API objects

[id="nodes-containers-downward-api"]
= Allowing containers to consume API objects

[role="_abstract"]
You can use the _Downward API_ to allow containers to consume information about API objects, such as the pod's name, namespace, and resource values, without coupling to OpenShift Container Platform by using environment variables or a volume plugin.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-projected-volumes-about_{context}"]
= Expose pod information to Containers using the Downward API

[role="_abstract"]
You can review the following tables to learn what information the Downward API contains, including the pod's name, project, and resource values. Your containers can consume this
information by using environment variables or a volume plugin.

Fields within the pod are selected using the `FieldRef` API type. `FieldRef`
has two fields:

[options="header"]
|===
|Field |Description

|`fieldPath`
|The path of the field to select, relative to the pod.

|`apiVersion`
|The API version to interpret the `fieldPath` selector within.
|===

Currently, the valid selectors in the v1 API include:

[options="header"]
|===
|Selector |Description

|`metadata.name`
|The pod's name. This is supported in both environment variables and volumes.

|`metadata.namespace`
|The pod's namespace.This is supported in both environment variables and volumes.

|`metadata.labels`
|The pod's labels. This is only supported in volumes and not in environment variables.

|`metadata.annotations`
|The pod's annotations. This is only supported in volumes and not in environment variables.

|`status.podIP`
|The pod's IP. This is only supported in environment variables and not volumes.
|===

The `apiVersion` field, if not specified, defaults to the API version of the
enclosing pod template.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-values_{context}"]
= Understanding how to consume container values using the downward API

[role="_abstract"]
Your containers can consume API values by using environment variables or a volume plugin.

Depending on the method you choose, containers can consume:

* Pod name

* Pod project/namespace

* Pod annotations

* Pod labels

Annotations and labels are available using only a volume plugin.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-values-envars_{context}"]
= Consuming container values using environment variables

[role="_abstract"]
When using environment variables in a container, you can specify that the variable's value should come from a `FieldRef` source instead of the literal value specified.

Only constant attributes of the pod can be consumed this way, because environment
variables cannot be updated after a process is started in a way that allows the
process to be notified that the value of a variable has changed. The following fields
are supported for using with environment variables:

- Pod name
- Pod project/namespace

.Procedure

. Create a new pod spec that contains the environment variables you want the container to consume:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: env-test-container
      image: gcr.io/google_containers/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: MY_POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: MY_POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Never
# ...
----
where:

`spec.containers.env.valueFrom.fieldRef.fieldPath`:: Specifies that the environment variable gets its value from the specified pod value, either `metadata.name` for the pod name or `metadata.namespace` for the pod namespace, instead of a literal value specified by a `value` field.

.. Create the pod from the `pod.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

.Verification

* Check the container logs for the `MY_POD_NAME` and `MY_POD_NAMESPACE`
values:
+
[source,terminal]
----
$ oc logs -p dapi-env-test-pod
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-values-plugin_{context}"]
= Consuming container values using a volume plugin

[role="_abstract"]
Your containers can consume Downward API values by using a volume plugin.

Containers can consume the following values:

* Pod name

* Pod project/namespace

* Pod annotations

* Pod labels

The following procedure show how to use the volume plugin.

.Procedure

. Create a new pod spec that contains the environment variables you want the container to consume:

.. Create a `volume-pod.yaml` file similar to the following:
+
[source,yaml]
----
kind: Pod
apiVersion: v1
metadata:
  labels:
    zone: us-east-coast
    cluster: downward-api-test-cluster1
    rack: rack-123
  name: dapi-volume-test-pod
  annotations:
    annotation1: "345"
    annotation2: "456"
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: volume-test-container
      image: gcr.io/google_containers/busybox
      command: ["sh", "-c", "cat /tmp/etc/pod_labels /tmp/etc/pod_annotations"]
      volumeMounts:
        - name: podinfo
          mountPath: /tmp/etc
          readOnly: false
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  volumes:
  - name: podinfo
    downwardAPI:
      defaultMode: 420
      items:
      - fieldRef:
          fieldPath: metadata.name
        path: pod_name
      - fieldRef:
          fieldPath: metadata.namespace
        path: pod_namespace
      - fieldRef:
          fieldPath: metadata.labels
        path: pod_labels
      - fieldRef:
          fieldPath: metadata.annotations
        path: pod_annotations
  restartPolicy: Never
# ...
----

.. Create the pod from the `volume-pod.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f volume-pod.yaml
----

.Verification

* Check the container logs and verify the presence of the configured fields by using the following command:
+
[source,terminal]
----
$ oc logs -p dapi-volume-test-pod
----
+
.Example output
[source,terminal]
----
cluster=downward-api-test-cluster1
rack=rack-123
zone=us-east-coast
annotation1=345
annotation2=456
kubernetes.io/config.source=api
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-resources-api_{context}"]
= Understanding how to consume container resources using the Downward API

[role="_abstract"]
When creating pods, you can use the Downward API to inject information about
computing resource requests and limits so that image and application authors can
correctly create an image for specific environments.

You can do this using environment variable or a volume plugin.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-resources-envars_{context}"]
= Consuming container resources using environment variables

[role="_abstract"]
When creating pods, you can use the Downward API to inject information about
computing resource requests and limits by using environment variables that
correspond to the contents of the `resources` field in the `*spec.container*`
field.

[NOTE]
====
If the resource limits are not included in the container configuration, the
downward API defaults to the node's CPU and memory allocatable values.
====

.Procedure

. Create a new pod spec that contains the resources you want to inject:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox:1.24
      command: [ "/bin/sh", "-c", "env" ]
      resources:
        requests:
          memory: "32Mi"
          cpu: "125m"
        limits:
          memory: "64Mi"
          cpu: "250m"
      env:
        - name: MY_CPU_REQUEST
          valueFrom:
            resourceFieldRef:
              resource: requests.cpu
        - name: MY_CPU_LIMIT
          valueFrom:
            resourceFieldRef:
              resource: limits.cpu
        - name: MY_MEM_REQUEST
          valueFrom:
            resourceFieldRef:
              resource: requests.memory
        - name: MY_MEM_LIMIT
          valueFrom:
            resourceFieldRef:
              resource: limits.memory
# ...
----

.. Create the pod from the `pod.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-resources-plugin_{context}"]
= Consuming container resources using a volume plugin

[role="_abstract"]
When creating pods, you can use the Downward API to inject information about
computing resource requests and limits by using a volume plugin to describe the desired resources that correspond to the
`spec.resources` field.

[NOTE]
====
If the resource limits are not included in the container configuration, the
Downward API defaults to the node's CPU and memory allocatable values.
====

.Procedure

. Create a new pod spec that contains the resources you want to inject:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  containers:
    - name: client-container
      image: gcr.io/google_containers/busybox:1.24
      command: ["sh", "-c", "while true; do echo; if [[ -e /etc/cpu_limit ]]; then cat /etc/cpu_limit; fi; if [[ -e /etc/cpu_request ]]; then cat /etc/cpu_request; fi; if [[ -e /etc/mem_limit ]]; then cat /etc/mem_limit; fi; if [[ -e /etc/mem_request ]]; then cat /etc/mem_request; fi; sleep 5; done"]
      resources:
        requests:
          memory: "32Mi"
          cpu: "125m"
        limits:
          memory: "64Mi"
          cpu: "250m"
      volumeMounts:
        - name: podinfo
          mountPath: /etc
          readOnly: false
  volumes:
    - name: podinfo
      downwardAPI:
        items:
          - path: "cpu_limit"
            resourceFieldRef:
              containerName: client-container
              resource: limits.cpu
          - path: "cpu_request"
            resourceFieldRef:
              containerName: client-container
              resource: requests.cpu
          - path: "mem_limit"
            resourceFieldRef:
              containerName: client-container
              resource: limits.memory
          - path: "mem_request"
            resourceFieldRef:
              containerName: client-container
              resource: requests.memory
# ...
----

.. Create the pod from the `*_volume-pod.yaml_*` file by using the following command:
+
[source,terminal]
----
$ oc create -f volume-pod.yaml
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-secrets_{context}"]
= Consuming secrets using the Downward API

[role="_abstract"]
When creating pods, you can use the downward API to inject secrets
so image and application authors can create an image
for specific environments.

.Procedure

. Create a secret to inject:

.. Create a `secret.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
data:
  password: <password>
  username: <username>
type: kubernetes.io/basic-auth
----

.. Create the secret object from the `secret.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f secret.yaml
----

. Create a pod that references the `username` field from the above `Secret` object:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: env-test-container
      image: gcr.io/google_containers/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: MY_SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: username
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Never
# ...
----

.. Create the pod from the `pod.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

.Verification

* Check the container logs for the `MY_SECRET_USERNAME` value by using the following command:
+
[source,terminal]
----
$ oc logs -p dapi-env-test-pod
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-configmaps_{context}"]
= Consuming configuration maps using the Downward API

[role="_abstract"]
When creating pods, you can use the Downward API to inject configuration map values
so that image and application authors can create an image for specific environments.

.Procedure

. Create a config map with the values to inject:

.. Create a `*_configmap.yaml_*` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
data:
  mykey: myvalue
----

.. Create the config map from the `configmap.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f configmap.yaml
----

. Create a pod that references the above config map:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: env-test-container
      image: gcr.io/google_containers/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: MY_CONFIGMAP_VALUE
          valueFrom:
            configMapKeyRef:
              name: myconfigmap
              key: mykey
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Always
# ...
----

.. Create the pod from the `pod.yaml` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

.Verification

* Check the container's logs for the `MY_CONFIGMAP_VALUE` value by using the following command:
+
[source,terminal]
----
$ oc logs -p dapi-env-test-pod
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-envars_{context}"]
= Referencing environment variables

[role="_abstract"]
When creating pods, you can reference the value of a previously defined environment variable by using the `$()` syntax. By using this syntax, you can reference variables that you define within a pod configuration elsewhere in that configuration.

If the environment variable
reference cannot be resolved, the value will be left as the provided
string.

.Procedure

. Create a pod that references an existing environment variable:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: env-test-container
      image: gcr.io/google_containers/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: MY_EXISTING_ENV
          value: my_value
        - name: MY_ENV_VAR_REF_ENV
          value: $(MY_EXISTING_ENV)
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Never
# ...
----

.. Create the pod from the `*_pod.yaml_*` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

.Verification

* Check the container's logs for the `MY_ENV_VAR_REF_ENV` value by using the following command:
+
[source,terminal]
----
$ oc logs -p dapi-env-test-pod
----

// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

[id="nodes-containers-downward-api-container-escaping_{context}"]
= Escaping environment variable references

[role="_abstract"]
When creating a pod, you can escape an environment variable reference by using
a double dollar sign. The value will then be set to a single dollar sign version
of the provided value.

.Procedure

. Create a pod that references an existing environment variable:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: env-test-container
      image: gcr.io/google_containers/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: MY_NEW_ENV
          value: $$(SOME_OTHER_ENV)
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Never
# ...
----

.. Create the pod from the `*_pod.yaml_*` file by using the following command:
+
[source,terminal]
----
$ oc create -f pod.yaml
----

.Verification

* Check the container's logs for the `MY_NEW_ENV` value by using the following command:
+
[source,terminal]
----
$ oc logs -p dapi-env-test-pod
----
