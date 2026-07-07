---
title: "Volume populators"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-vol-populators
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-vol-populators
version: 4.22
family: storage
documentKind: "Documentation"
---

# Volume populators

[id="persistent-storage-csi-vol-populators"]
= Volume populators

Volume Populators enable the automatic pre-loading of data into a volume during dynamic provisioning, instead of provisioning an empty volume.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vol-populators.adoc

[id="persistent-storage-csi-vol-populator_{context}"]
= Volume populators overview

In OpenShift Container Platform versions 4.12 through 4.19, the `dataSource` field in a persistent volume claim (PVC) spec provides volume populator capability. However, it is limited to using only PVCs and snapshots as the data source for populating volumes.

Starting with OpenShift Container Platform version 4.20, the `dataSourceRef` field is used instead. With the `dataSourceRef` field, you can use any appropriate custom resource (CR) as the data source to prepopulate a new volume.

[NOTE]
====
Volume populator functionality using the `dataSource` field is likely to be deprecated in future versions. If you have created any volume populators using this field, consider re-creating your volume populators to use the `dataSourceRef` field to avoid future issues.
====

Volume population is enabled by default and OpenShift Container Platform includes the installed `volume-data-source-validator` controller. However, OpenShift Container Platform does not ship with any volume populators.

== Creating volume populators

To create and use volume populators:

. Create a custom resource definition (CRD) for volume populators.

. Create a prepopulated volume using a volume populator.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vol-populators.adoc

[id="persistent-storage-csi-vol-populator-procedure-admin_{context}"]
= Creating CRDs for volume populators

The following procedure explains how to create an example "hello, world" custom resource definition (CRD) for a volume populator.

Users can then create instances of this CRD to populate persistent volume claims (PVCs).

.Prerequisites

* Access to the OpenShift Container Platform web console.

* Access to the cluster with cluster-admin privileges.

.Procedure

. Create a namespace for the logical grouping and operation of the populator, and related resources, using the following example YAML file:
+
.Example namespace YAML file
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: hello
----

. Create a CRD for your data source using the following example YAML file:
+
.Example CRD YAML file
[source,yaml]
----
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: hellos.hello.example.com
spec:
  group: hello.example.com
  names:
    kind: Hello
    listKind: HelloList
    plural: hellos
    singular: hello
  scope: Namespaced
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: Hello is a specification for a Hello resource
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object. Servers should convert recognized schemas to the latest
              internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents. Servers may infer this from the endpoint the client
              submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          spec:
            description: HelloSpec is the spec for a Hello resource
            properties:
              fileContents:
                type: string
              fileName:
                type: string
            required:
            - fileContents
            - fileName
            type: object
        required:
        - spec
        type: object
    served: true
    storage: true
----

. Deploy the controller by creating a `ServiceAccount`, `ClusterRole`, `ClusterRoleBindering`, and `Deployment` to run the logic that implements the population:

.. Create a service account for the populator using the following example YAML file:
+
.Example service account YAML file
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: hello-account
  namespace: hello <1>
----
<1> Reference the namespace that you created earlier.

.. Create a cluster role for the populator using the following example YAML file:
+
.Example cluster role YAML file
[source,yaml]
----
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hello-role
rules:
  - apiGroups: [hello.example.com]
    resources: [hellos]
    verbs: [get, list, watch]
----

.. Create a cluster role binding using the following example YAML file:
+
.Example cluster role binding YAML file
[source,yaml]
----
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hello-binding <1>
subjects:
  - kind: ServiceAccount
    name: hello-account <2>
    namespace: hello <3>
roleRef:
  kind: ClusterRole
  name: hello-role <4>
  apiGroup: rbac.authorization.k8s.io
----
<1> Role binding name.
<2> Reference the name of the service account that you created earlier.
<3> Reference the name of the namespace for the service account that you created earlier.
<4> Reference the cluster role you created earlier.

.. Create a Deployment for the populator using the following example YAML file:
+
.Example deployment YAML file
[source,yaml]
----
kind: Deployment
apiVersion: apps/v1
metadata:
  name: hello-populator
  namespace: hello <1>
spec:
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      serviceAccount: hello-account <2>
      containers:
        - name: hello
          image: registry.k8s.io/sig-storage/hello-populator:v1.0.1
          imagePullPolicy: IfNotPresent
          args:
            - --mode=controller
            - --image-name=registry.k8s.io/sig-storage/hello-populator:v1.0.1
            - --http-endpoint=:8080
          ports:
            - containerPort: 8080
              name: http-endpoint
              protocol: TCP
----
<1> Reference the namespace that you created earlier.
<2> Reference the service account that you created earlier.

. Create a volume populator to register the `kind:Hello` resource as a valid data source for the volume using the following example YAML file:
+
.Example volume populator YAML file
[source,yaml]
----
kind: VolumePopulator
apiVersion: populator.storage.k8s.io/v1beta1
metadata:
  name: hello-populator <1>
sourceKind:
  group: hello.example.com
  kind: Hello
----
<1> Volume populator name.
+
PVCs that use an unregistered populator generate an event: "The datasource for this PVC does not match any registered VolumePopulator", indicating that the PVC might not be provisioned because you are using an unknown (unregistered) populator.

.Next steps
* You can now create CR instances of this CRD to populate PVCs.

For information about how to prepopulate volumes using a volume populator, see Creating prepoluated volumes with volume populators.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vol-populators.adoc

[id="persistent-storage-csi-vol-populator-procedure_{context}"]
= Creating prepopulated volumes using volume populators

The following procedure explains how to create a prepopulated persistent volume claim (PVC)  using the example `hellos.hello.example.com` Custom Resource Definition (CRD) created previously.

In this example, rather than using an actual data source, you are creating a file called "example.txt" that contains the string "Hello, world!" in the root directory of the volume. For a real-world implementation, you need to create your own volume populator.

.Prerequisites

* You are logged in to a running OpenShift Container Platform cluster.

* There is an existing custom resource definition (CRD) for volume populators.

* OpenShift Container Platform does not ship with any volume populators. You *must* create your own volume populator.

.Procedure

. Create a Custom Resource (CR) instance of the `Hello` CRD with the text "Hello, World!" passed in as `fileContents` parameter by running the following command:
+
[source,terminal]
----
$ oc apply -f  - <<EOF
apiVersion: hello.example.com/v1alpha1
kind: Hello
metadata:
  name: example-hello
spec:
  fileName: example.txt
  fileContents: Hello, world!
EOF
----

. Create a PVC that references the Hello CR similar to the following example file:
+
.Example PVC YAML file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: example-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Mi
  dataSourceRef: <1>
    apiGroup: hello.example.com
    kind: Hello
    name: example-hello <2>
  volumeMode: Filesystem
----
<1> The `dataSourceRef` field specifies the data source for the PVC.
<2> The name of the CR that you are using as the data source. In this example, 'example-hello'.

.Verification

. After a few minutes, ensure that the PVC is created and in the `Bound` status by running the following command:
+
[source,terminal]
----
$ oc get pvc example-pvc -n hello <1>
----
<1> In this example, the name of the PVC is `example-pvc`.
+
.Example output
[source,terminal]
----
NAME          STATUS    VOLUME        CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
example-pvc   Bound     my-pv         10Mi       ReadWriteOnce  gp3-csi        <unset>                 14s
----

. Create a job that reads from the PVC to verify that the data source information was applied using the following example file:
+
.Example job YAML file
[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
  name: example-job
spec:
  template:
    spec:
      containers:
        - name: example-container
          image: busybox:latest
          command:
            - cat
            - /mnt/example.txt <1>
          volumeMounts:
            - name: vol
              mountPath: /mnt
      restartPolicy: Never
      volumes:
        - name: vol
          persistentVolumeClaim:
            claimName: example-pvc <2>
----
<1> The location and name of the file with the "Hello, world!" text.
<2> The name of the PVC you created in Step 2. In this example, `example-pvc`.

. Start the job by running the following command:
+
[source,terminal]
----
$ oc run example-job --image=busybox --command -- sleep 30 --restart=OnFailure
----
+
.Example output
[source,terminal]
----
pod/example-job created
----

. Wait for the job, and all of its dependencies, to finish by running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=Complete pod/example-job
----

. Verify the contents collected by the job by running the following command:
+
[source,terminal]
----
$ oc logs job/example-job
----
+
.Expected output
+
[source,terminal]
----
Hello, world!
----

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vol-populators.adoc

[id="persistent-storage-csi-vol-populator-uninstall_{context}"]
= Uninstalling volume populators

The following procedure explains how to uninstall volume populators.

.Prerequisites

* Access to the OpenShift Container Platform web console.

* Access to the cluster with cluster-admin privileges.

.Procedure

To uninstall volume populators, delete in reverse order all objects installed in the procedures under:

. Section _Creating prepopulated volumes using volume populators_.

. Section _Creating CRDs for volume populators_.
+
Be sure to remove the `VolumePopulator` instance.

// TP features should be excluded from OSD and ROSA. When this feature is GA, it can be included in the OSD/ROSA docs, but with a warning that it is available as of version 4.x
//This features is GA in OCP 4.20
