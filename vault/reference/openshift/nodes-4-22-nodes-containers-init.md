---
title: "Using Init Containers to perform tasks before a pod is deployed"
type: reference
domain: openshift
slug: nodes-4-22-nodes-containers-init
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-containers-init
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Using Init Containers to perform tasks before a pod is deployed

[id="nodes-containers-init"]
= Using Init Containers to perform tasks before a pod is deployed

[role="_abstract"]
You can use _init containers_, which are specialized containers
that run before application containers and can contain utilities or setup scripts not present in an app image.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-init.adoc

[id="nodes-containers-init-about_{context}"]
= Understanding init containers

[role="_abstract"]
You can use an init container to perform tasks before the rest of a pod is deployed. You can use init containers to perform setup tasks that should be completed before the main application logic begins, such as environment preparation, dependency checks, or configuration generation.

A pod can have init containers in addition to application containers. Init containers allow you to reorganize setup scripts and binding code.

An init container can:

* Contain and run utilities that are not desirable to include in the app container image for security reasons.
* Contain utilities or custom code for setup that is not present in an app image. For example, there is no requirement to make an image FROM another image just to use a tool like sed, awk, python, or dig during setup.
* Use Linux namespaces so that they have different filesystem views from app containers, such as access to secrets that application containers are not able to access.

Because each init container must complete successfully before the next one is started, they provide an easy way to block or delay the startup of app containers until some set of preconditions are met.

For example, the following are some ways you can use init containers:

* Wait for a service to be created by using a shell command similar to the following:
+
[source,terminal]
----
for i in {1..100}; do sleep 1; if dig myservice; then exit 0; fi; done; exit 1
----

* Register this pod with a remote server from the Downward API by using a command similar to the following:
+
[source,terminal]
----
$ curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d ‘instance=$()&ip=$()’
----

* Delay starting the app container by using a command such as `sleep 60`.

* Clone a git repository into a volume.

* Place values into a configuration file and run a template tool to dynamically generate a configuration file for the main app container. For example, place the `POD_IP` value in a configuration and generate the main app configuration file using Jinja.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-init.adoc

[id="nodes-containers-init-creating_{context}"]
= Creating Init Containers

[role="_abstract"]
You create an init container by creating a pod spec that contains an `initContainers` configuration.

The following example outlines a simple pod which has two init containers. The first init continer waits for the `myservice` service to complete. After that, the second waits for `mydb` service to complete. After both init containers complete, the pod begins.

.Procedure

. Create the pod for the Init Container:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: myapp-container
    image: registry.access.redhat.com/ubi9/ubi:latest
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  initContainers:
  - name: init-myservice
    image: registry.access.redhat.com/ubi9/ubi:latest
    command: ['sh', '-c', 'until getent hosts myservice; do echo waiting for myservice; sleep 2; done;']
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  - name: init-mydb
    image: registry.access.redhat.com/ubi9/ubi:latest
    command: ['sh', '-c', 'until getent hosts mydb; do echo waiting for mydb; sleep 2; done;']
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
----

.. Create the pod by using the following command:
+
[source,terminal]
----
$ oc create -f myapp.yaml
----

.. View the status of the pod by using the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                          READY     STATUS              RESTARTS   AGE
myapp-pod                     0/1       Init:0/2            0          5s
----
+
The pod status, `Init:0/2`, indicates it is waiting for the two services.

. Create the `myservice` service.

.. Create a YAML file similar to the following:
+
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  name: myservice
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
----

.. Create the pod by using the following command:
+
[source,terminal]
----
$ oc create -f myservice.yaml
----

.. View the status of the pod by using the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                          READY     STATUS              RESTARTS   AGE
myapp-pod                     0/1       Init:1/2            0          5s
----
+
The pod status, `Init:1/2`, indicates it is waiting for one service, in this case the `mydb` service.

. Create the `mydb` service:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  name: mydb
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9377
----

.. Create the pod by using the following command:
+
[source,terminal]
----
$ oc create -f mydb.yaml
----

.. View the status of the pod by using the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                          READY     STATUS              RESTARTS   AGE
myapp-pod                     1/1       Running             0          2m
----
+
The pod status, `Running`, indicates that it is no longer waiting for the services and is running.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Init Containers (Kubernetes documentation)
