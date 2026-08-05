---
title: "Mapping volumes using projected volumes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-containers-projected-volumes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-containers-projected-volumes
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Mapping volumes using projected volumes

[id="nodes-containers-projected-volumes"]
= Mapping volumes using projected volumes

[role="_abstract"]
You can centralize sensitive information and environment metadata for your applications by using projected volumes to map multiple configuration sources, such as secrets and config maps, into a single directory. Having a single directory makes it easier for your applications to access that information.

The following types of volume sources can be projected:

* Secrets

* Config Maps

* Downward API

[NOTE]
====
All sources are required to be in the same namespace as the pod.
====

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-projected-volumes.adoc

[id="nodes-containers-projected-volumes-about_{context}"]
= Understanding projected volumes

[role="_abstract"]
To simplify data management within your pods, you can use projected volumes to map multiple configuration sources, such as secrets and config maps, into a single directory. By using a single directory, you make it easier for your applications to access sensitive information and environment metadata easier.

You can use projected volumes to map any combination of the volume sources into a single directory, allowing the user to perform the following actions:

* Automatically populate a single volume with the keys from multiple secrets, config maps, and with downward API information,
so that you can synthesize a single directory with various sources of information.
* Populate a single volume with the keys from multiple secrets, config maps, and with downward API information,
explicitly specifying paths for each item, so that you can have full control over the contents of that volume.

[IMPORTANT]
====
When the `RunAsUser` permission is set in the security context of a Linux-based pod, the projected files have the correct permissions set, including container user ownership. However, when the Windows equivalent `RunAsUsername` permission is set in a Windows pod, the kubelet is unable to correctly set ownership on the files in the projected volume.

Therefore, the `RunAsUsername` permission set in the security context of a Windows pod is not honored for Windows projected volumes running in OpenShift Container Platform.
====

The following general scenarios show how you can use projected volumes.

Config map, secrets, Downward API::
Projected volumes allow you to deploy containers with configuration data that includes passwords.
An application using these resources could be deploying {rh-openstack-first} on Kubernetes. The configuration data might have to be assembled differently depending on if the services are going to be used for production or for testing. If a pod is labeled with production or testing, the downward API selector `metadata.labels` can be used to produce the correct {rh-openstack} configs.

Config map + secrets::
Projected volumes allow you to deploy containers involving configuration data and passwords.
For example, you might execute a config map with some sensitive encrypted tasks that are decrypted using a vault password file.

ConfigMap + Downward API::
Projected volumes allow you to generate a config including the pod name (available via the `metadata.name` selector). This application can then pass the pod name along with requests to easily determine the source without using IP tracking.

Secrets + Downward API::
Projected volumes allow you to use a secret as a public key to encrypt the namespace of the pod (available via the `metadata.namespace` selector).
This example allows the Operator to use the application to deliver the namespace information securely without using an encrypted transport.

The following are examples of `Pod` specs for creating projected volumes.

.Pod with a secret, a Downward API, and a config map

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: container-test
    image: busybox
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  volumes:
  - name: all-in-one
    projected:
      defaultMode: 0400
      sources:
      - secret:
          name: mysecret
          items:
            - key: username
              path: my-group/my-username
      - downwardAPI:
          items:
            - path: "labels"
              fieldRef:
                fieldPath: metadata.labels
            - path: "cpu_limit"
              resourceFieldRef:
                containerName: container-test
                resource: limits.cpu
      - configMap:
          name: myconfigmap
          items:
            - key: config
              path: my-group/my-config
              mode: 0777
----
where:

--
`spec.containers.volumeMounts`:: Specifies a section for each container that needs the secret.
`spec.containers.volumeMounts.mountPath`:: Specifies a path to an unused directory where the secret will appear.
`spec.containers.volumeMounts.readOnly`:: When `true`, specifies that the volume mount is `readOnly`.
`spec.containers.volumes`:: Specifies a `volumes` block to list each projected volume source.
`spec.containers.volumes.name`:: Specifies a name for the volume.
`spec.containers.volumes.projected.defaultMode`:: Specifies the execute permission on the files.
`spec.containers.volumes.projected.sources.secret.name`:: Specifies a secret. Enter the name of the secret object. Each secret you want to use must be listed.
`spec.containers.volumes.projected.sources.secret.items.path`:: Specifies the path to the secrets file under the `mountPath`. Here, the secrets file is in *_/projected-volume/my-group/my-username_*.
`spec.containers.volumes.projected.defaultMode.downwardAPI`:: Specifies a Downward API source.
`spec.containers.volumes.projected.defaultMode.configMap`:: Specifies a ConfigMap source.
`spec.containers.volumes.projected.defaultMode.configMap.items.mode`:: Specifies the mode for the specific projection.
--

[NOTE]
====
If there are multiple containers in the pod, each container needs a `volumeMounts` section, but only one `volumes` section is needed.
====

.Pod with multiple secrets with a non-default permission mode set

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: container-test
    image: busybox
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  volumes:
  - name: all-in-one
    projected:
      defaultMode: 0755
      sources:
      - secret:
          name: mysecret
          items:
            - key: username
              path: my-group/my-username
      - secret:
          name: mysecret2
          items:
            - key: password
              path: my-group/my-password
              mode: 511
----

[NOTE]
====
The `defaultMode` can only be specified at the projected level and not for each
volume source. However, as illustrated above, you can explicitly set the `mode`
for each individual projection.
====

Pathing Considerations::

* Collisions Between Keys when Configured Paths are Identical. If you configure any keys with the same path, the pod spec will not be accepted as valid.
In the following example, the specified path for `mysecret` and `myconfigmap` are the same:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: container-test
    image: busybox
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  volumes:
  - name: all-in-one
    projected:
      sources:
      - secret:
          name: mysecret
          items:
            - key: username
              path: my-group/data
      - configMap:
          name: myconfigmap
          items:
            - key: config
              path: my-group/data
----

Consider the following situations related to the volume file paths.

* Collisions Between Keys without Configured Paths. The only run-time validation that can occur is when all the paths are known at pod creation, similar to the above scenario. Otherwise, when a conflict occurs the most recent specified resource overwrites anything preceding it
(this is true for resources that are updated after pod creation as well).

* Collisions when One Path is Explicit and the Other is Automatically Projected. If there is a collision due to a user-specified path matching data that is automatically projected,
the latter resource overwrites anything preceding it as before.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-projected-volumes.adoc

[id="nodes-containers-projected-volumes-creating_{context}"]
= Configuring a projected volume for a Pod

[role="_abstract"]
You can create projected volumes to map multiple configuration sources, such as secrets and config maps, into a single directory. Projected volumes centralize sensitive information and environment metadata for your applications into a single directory.

When creating projected volumes, consider the volume file path situations described in _Understanding projected volumes_.

The following example shows how to use a projected volume to mount an existing secret volume source. The steps can be used to create a user name and password secrets from local files. You then create a pod that runs one container, using a projected volume to mount the secrets into the same shared directory.

The user name and password values can be any valid string that is *base64* encoded.

The following example shows `admin` in base64:

[source,terminal]
----
$ echo -n "admin" | base64
----

.Example output
[source,terminal]
----
YWRtaW4=
----

The following example shows the password `1f2d1e2e67df` in base64:

[source,terminal]
----
$ echo -n "1f2d1e2e67df" | base64
----

.Example output
[source,terminal]
----
MWYyZDFlMmU2N2Rm
----

The following procedure uses a projected volume to mount an existing secret volume source.

.Procedure

. Create the secret:

.. Create a YAML file similar to the following, replacing the password and user information as appropriate:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  pass: MWYyZDFlMmU2N2Rm
  user: YWRtaW4=
----
+
.. Use the following command to create the secret:
+
[source,terminal]
----
$ oc create -f <secrets-filename>
----
+
For example:
+
[source,terminal]
----
$ oc create -f secret.yaml
----
+
.Example output
[source,terminal]
----
secret "mysecret" created
----

.. You can check that the secret was created using the following commands:
+
[source,terminal]
----
$ oc get secret <secret-name>
----
+
For example:
+
[source,terminal]
----
$ oc get secret mysecret
----
+
.Example output
[source,terminal]
----
NAME       TYPE      DATA      AGE
mysecret   Opaque    2         17h
----
+
[source,terminal]
----
$ oc get secret <secret-name> -o yaml
----
+
For example:
+
[source,terminal]
----
$ oc get secret mysecret -o yaml
----
+
[source,yaml]
----
apiVersion: v1
data:
  pass: MWYyZDFlMmU2N2Rm
  user: YWRtaW4=
kind: Secret
metadata:
  creationTimestamp: 2017-05-30T20:21:38Z
  name: mysecret
  namespace: default
  resourceVersion: "2107"
  selfLink: /api/v1/namespaces/default/secrets/mysecret
  uid: 959e0424-4575-11e7-9f97-fa163e4bd54c
type: Opaque
----

. Create a pod with a projected volume.

.. Create a YAML file similar to the following, including a `volumes` section:
+
[source,yaml]
----
kind: Pod
metadata:
  name: test-projected-volume
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: test-projected-volume
    image: busybox
    args:
    - sleep
    - "86400"
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  volumes:
  - name: all-in-one
    projected:
      sources:
      - secret:
          name: <my_secret>
----
+
Replace `<my_secret>` with the name of the secret you created.

.. Create the pod from the configuration file:
+
[source,terminal]
----
$ oc create -f <your_yaml_file>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f secret-pod.yaml
----
+
.Example output
[source,terminal]
----
pod "test-projected-volume" created
----

. Verify that the pod container is running, and then watch for changes to
the pod:
+
[source,terminal]
----
$ oc get pod <name>
----
+
For example:
+
[source,terminal]
----
$ oc get pod test-projected-volume
----
+
The output should appear similar to the following:
+
.Example output
[source,terminal]
----
NAME                    READY     STATUS    RESTARTS   AGE
test-projected-volume   1/1       Running   0          14s
----

. In another terminal, use the `oc exec` command to open a shell to the running container:
+
[source,terminal]
----
$ oc exec -it <pod> <command>
----
+
For example:
+
[source,terminal]
----
$ oc exec -it test-projected-volume -- /bin/sh
----

. In your shell, verify that the `projected-volumes` directory contains your projected sources:
+
[source,terminal]
----
/ # ls
----
+
.Example output
[source,terminal]
----
bin               home              root              tmp
dev               proc              run               usr
etc               projected-volume  sys               var
----
