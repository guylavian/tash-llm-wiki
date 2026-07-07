---
title: "Using Kustomize manifests to deploy applications"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-applications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-applications
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using Kustomize manifests to deploy applications

[id="applications-with-microshift"]
= Using Kustomize manifests to deploy applications

[role="_abstract"]
You can use the `kustomize` configuration management tool with application manifests to deploy applications on {microshift-short}.

Read through the following procedures for an example of how Kustomize works in {microshift-short}.

// Module included in the following assemblies:
//
// * microshift//running_applications/microshift-applications.adoc

[id="microshift-manifests-overview_{context}"]
= How Kustomize works with manifests to deploy applications

[role="_abstract"]
The `kustomize` configuration management tool is integrated with {microshift-short}. You can use Kustomize and the {oc-first} together to apply customizations to your application manifests and deploy those applications to a {microshift-short} node.

* A `kustomization.yaml` file is a specification of resources plus customizations.
* Kustomize uses a `kustomization.yaml` file to load a resource, such as an application, then applies any changes you want to that application manifest and produces a copy of the manifest with the changes overlaid.
* Using a manifest copy with an overlay keeps the original configuration file for your application intact, while enabling you to deploy iterations and customizations of your applications efficiently.
* You can then deploy the application in your {microshift-short} node with an `oc` command.

[NOTE]
====
At each system start, {microshift-short} deletes the manifests found in the `delete` subdirectories and then applies the manifest files found in the manifest directories to the node.
====

[id="how-microshift-uses-manifests"]
== How {microshift-short} uses manifests
At every start, {microshift-short} searches the following manifest directories for Kustomize manifest files:

* `/etc/microshift/manifests`
* `/etc/microshift/manifests.d/++*++`
* `/usr/lib/microshift/`
* `/usr/lib/microshift/manifests.d/++*++`

{microshift-short} automatically runs the equivalent of the `kubectl apply -k` command to apply the manifests to the node if any of the following file types exists in the searched directories:

* `kustomization.yaml`
* `kustomization.yml`
* `Kustomization`

This automatic loading from multiple directories means you can manage {microshift-short} workloads with the flexibility of having different workloads run independently of each other.

.{microshift-short} manifest directories

[cols="2",options="header"]
|===
|Location
|Intent

|`/etc/microshift/manifests`
|Read-write location for configuration management systems or development.

|`/etc/microshift/manifests.d/*`
|Read-write location for configuration management systems or development.

|`/usr/lib/microshift/manifests`
|Read-only location for embedding configuration manifests on OSTree-based systems.

|`/usr/lib/microshift/manifestsd./*`
|Read-only location for embedding configuration manifests on OSTree-based systems.
|===

// Module included in the following assemblies:
//
// * microshift//running_applications/microshift-applications.adoc

[id="microshift-manifests-override-paths_{context}"]
= Override the list of manifest paths

[role="_abstract"]
You can override the list of default manifest paths by using a new single path, or by using a new glob pattern for multiple files.

Use the following procedure to customize your manifest paths.

.Procedure

. Override the list of default paths by inserting your own values and running one of the following commands:

.. Set `manifests.kustomizePaths` to `<++"++/opt/alternate/path++"++>` in the configuration file for a single path.

.. Set `kustomizePaths` to `,++"++/opt/alternative/path.d/++*"++.` in the configuration file for a glob pattern.
+
[source,terminal,subs="+quotes"]
----
manifests:
    kustomizePaths:
        - _<location>_
----
+
Replace `_<location>_` with the path to the manifest directory. Set each location entry to an exact path by using `++"++/opt/alternate/path++"++` or a glob pattern by using `++"++/opt/alternative/path.d/++*"++`.

. To disable loading manifests, set the configuration option to an empty list.
+
[source,terminal]
----
manifests:
    kustomizePaths: []
----
+
[NOTE]
====
The configuration file overrides the defaults entirely. If the `kustomizePaths` value is set, only the values in the configuration file are used. Setting the value to an empty list disables manifest loading.
====

[role="_additional-resources"]
.Additional resources
* Deleting or updating Kustomize manifest resources

// Module included in the following assemblies:
//
// * microshift/running_applications/microshift-applications.adoc

[id="microshift-applying-manifests-example_{context}"]
= Using manifests example

[role="_abstract"]
You can automatically deploy a BusyBox container on {microshift-short} by using `kustomize` manifests in the `/etc/microshift/manifests` directory.

.Procedure
. Create the BusyBox manifest files by running the following commands:
+
.. Define the directory location:
+
[source,terminal]
----
$ MANIFEST_DIR=/etc/microshift/manifests
----
+
.. Make the directory:
+
[source,terminal]
----
$ sudo mkdir -p ${MANIFEST_DIR}
----
+
.. Place the YAML file in the directory:
+
[source,text]
----
sudo tee ${MANIFEST_DIR}/busybox.yaml &>/dev/null <<EOF
apiVersion: v1
kind: Namespace
metadata:
  name: busybox
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: busybox
  namespace: busybox-deployment
spec:
  selector:
    matchLabels:
      app: busybox
  template:
    metadata:
      labels:
        app: busybox
    spec:
      containers:
      - name: busybox
        image: BUSYBOX_IMAGE
        command: [ "/bin/sh", "-c", "while true ; do date; sleep 3600; done;" ]
EOF
----

. Next, create the `kustomize` manifest files by running the following commands:
+
.. Place the YAML file in the directory:
+
[source,text]
----
sudo tee ${MANIFEST_DIR}/kustomization.yaml &>/dev/null <<EOF
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: busybox
resources:
  - busybox.yaml
images:
  - name: BUSYBOX_IMAGE
    newName: busybox:1.35
EOF
----

. Restart {microshift-short} to apply the manifests by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
+
. Apply the manifests and start the `busybox` pod by running the following command:
+
[source,terminal]
----
$ oc get pods -n busybox
----
