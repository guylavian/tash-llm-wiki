---
title: "Enabling Windows container workloads"
type: reference
domain: openshift
slug: windows-containers-4-22-enabling-windows-container-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/enabling-windows-container-workloads
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Enabling Windows container workloads

[id="enabling-windows-container-workloads"]
= Enabling Windows container workloads

[role="_abstract"]
Before adding Windows workloads to your cluster, you must install the Windows Machine Config Operator (WMCO), which is available in the OpenShift Container Platform software catalog. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster.

[NOTE]
====
Dual NIC is not supported on WMCO-managed Windows instances.
====

== Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

* You have installed the OpenShift CLI (`oc`).

* You have installed your cluster using one of the following infrastructures:

** Any installer-provisioned infrastructure
** A user-provisioned infrastructure with the `platform: none` field set in your `install-config.yaml` file

* You have configured hybrid networking with OVN-Kubernetes for your cluster. For more information, see "Configuring hybrid networking".

* You are running an OpenShift Container Platform cluster version 4.6.8 or later.

[NOTE]
====
Windows instances deployed by the WMCO are configured with the containerd container runtime. Because WMCO installs and manages the runtime, it is recommended that you do not manually install containerd on nodes.
====

For the comprehensive prerequisites for the Windows Machine Config Operator, see "Windows Machine Config Operator prerequisites".

[id="installing-the-wmco"]
== Installing the Windows Machine Config Operator

You can install the Windows Machine Config Operator using either the web console or OpenShift CLI (`oc`).

[NOTE]
====
Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes.
====

// Module included in the following assemblies:
//
// * windows_containers/enabling-windows-container-workloads.adoc

[id="installing-wmco-using-web-console_{context}"]
= Installing the Windows Machine Config Operator using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to install the Windows Machine Config Operator (WMCO).

[NOTE]
====
Dual NIC is not supported on WMCO-managed Windows instances.
====

.Procedure

. From the *Administrator* perspective in the OpenShift Container Platform web console, navigate to the *Ecosystem* -> *Software Catalog* page.

. Use the *Filter by keyword* box to search for `Windows Machine Config Operator` in the catalog. Click the *Windows Machine Config Operator* tile.

. Review the information about the Operator and click *Install*.

. On the *Install Operator* page:

.. Select the *stable* channel as the *Update Channel*. The *stable* channel enables the latest stable release of the WMCO to be installed.

.. The *Installation Mode* is preconfigured because the WMCO must be available in a single namespace only.

.. Choose the *Installed Namespace* for the WMCO. The default Operator recommended namespace is `openshift-windows-machine-config-operator`.

.. Click the *Enable Operator recommended cluster monitoring on the Namespace* checkbox to enable cluster monitoring for the WMCO.

.. Select an *Approval Strategy*.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.
+
//TODO add image of Installation page when official Operator is available.
+
. Click *Install*. The WMCO is now listed on the *Installed Operators* page.
+
[NOTE]
====
The WMCO is installed automatically into the namespace you defined, like `openshift-windows-machine-config-operator`.
====

. Verify that the *Status* shows *Succeeded* to confirm successful installation of the WMCO.

// Module included in the following assemblies:
//
// * windows_containers/enabling-windows-container-workloads.adoc

[id="installing-wmco-using-cli_{context}"]
= Installing the Windows Machine Config Operator using the CLI

[role="_abstract"]
You can use the OpenShift CLI (`oc`) to install the Windows Machine Config Operator (WMCO).

[NOTE]
====
Dual NIC is not supported on WMCO-managed Windows instances.
====

.Procedure

. Create a namespace for the WMCO.

.. Create a `Namespace` object YAML file for the WMCO. For example, `wmco-namespace.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-windows-machine-config-operator
  labels:
    openshift.io/cluster-monitoring: "true"
----
where

`metadata.name`:: Specifies the namespace to create the secret. You should deploy the WMCO in the `openshift-windows-machine-config-operator` namespace.
`metadata.labels`:: Specifies the label required for enabling cluster monitoring for the WMCO.

.. Create the namespace:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f wmco-namespace.yaml
----

. Create the Operator group for the WMCO.

.. Create an `OperatorGroup` object YAML file. For example, `wmco-og.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
spec:
  targetNamespaces:
  - openshift-windows-machine-config-operator
----

.. Create the Operator group:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f wmco-og.yaml
----

. Subscribe the namespace to the WMCO.

.. Create a `Subscription` object YAML file. For example, `wmco-sub.yaml`:
+
[source,yaml, subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
spec:
  channel: "stable"
  installPlanApproval: "Automatic"
  name: "windows-machine-config-operator"
  source: "redhat-operators"
  sourceNamespace: "openshift-marketplace"
----
where:

`spec.channel`:: Specifies `stable` as the channel.
`spec.installPlanApproval`:: Specifies an approval strategy. You can set `Automatic` or `Manual`.
`spec.source`:: Specifies the `redhat-operators` catalog source, which contains the `windows-machine-config-operator` package manifests. If your OpenShift Container Platform is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator LifeCycle Manager (OLM).
`spec.sourceNamespace`:: Specifies the namespace of the catalog source. Use `openshift-marketplace` for the default software catalog sources.

.. Create the subscription:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f wmco-sub.yaml
----
+
The WMCO is now installed to the `openshift-windows-machine-config-operator`.

. Verify the WMCO installation:
+
[source,terminal]
----
$ oc get csv -n openshift-windows-machine-config-operator
----
+
.Example output
[source,terminal]
----
NAME                                    DISPLAY                           VERSION   REPLACES   PHASE
windows-machine-config-operator.2.0.0   Windows Machine Config Operator   2.0.0                Succeeded
----

// Module included in the following assemblies:
//
// * windows_containers/enabling-windows-container-workloads.adoc

[id="configuring-secret-for-wmco_{context}"]
= Configuring a secret for the Windows Machine Config Operator

[role="_abstract"]
Before you can use the Windows Machine Config Operator (WMCO), you must create a secret in the same WMCO namespace as your private key.

This secret is required to allow the WMCO to communicate with the Windows virtual machine (VM). Use a different private key than the one used when installing the cluster.

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You created a PEM-encoded file containing a private key by using a strong algorithm, such as ECDSA.
+
--
--

.Procedure

* Define the secret required to access the Windows VMs:
+
[source,terminal]
----
$ oc create secret generic cloud-private-key --from-file=private-key.pem=${HOME}/.ssh/<key> \
    -n openshift-windows-machine-config-operator
----
+
You must create the private key in the WMCO namespace, like `openshift-windows-machine-config-operator`.

// Module included in the following assemblies:
//
// windows_containers/enabling-windows-container-workloads.adoc

[id="wmco-configure-debug-logging_{context}"]
= Configuring debug-level logging for the Windows Machine Config Operator

[role="_abstract"]
You can edit the WMCO `Subscription` object to change the Windows Machine Config Operator (WMCO) log level to `debug`, if you need more verbose output.

By default, the WMCO is configured to use the `info` log level.

.Procedure

. Edit the `windows-machine-config-operator` subscription in the `windows-machine-config-operator` namespace by using the following command:
+
[source,terminal]
----
$ oc edit subscription windows-machine-config-operator -n openshift-windows-machine-config-operator
----

. Add the follwing parameters to the `.spec.config.env` stanza:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
# ...
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
# ...
spec:
# ...
  config:
    env:
    - name: ARGS
      value: --debugLogging
----
where:
+
--
`spec.config.env.name`:: Specifies a list of environment variables that must exist in all containers in the pod.
`spec.config.env.value`:: Specifies the `debug` level of verbosity for log messages.
--
+
You can revert to the default `info` log level by removing the `name` and `value` parameters that you added.

// Module included in the following assemblies:
//
// windows_containers/enabling-windows-container-workloads.adoc

[id="wmco-cluster-wide-proxy_{context}"]
= Using Windows containers in a proxy-enabled cluster

[role="_abstract"]
You can add Windows nodes and run workloads in a proxy-enabled cluster because Windows Machine Config Operator (WMCO) can consume and use the cluster-wide egress proxy when making external requests outside the cluster’s internal network.

Because of the support for the cluster-wide egress proxy, your Windows nodes can pull images from registries that are secured behind your proxy server or to make
requests to off-cluster services and services that use a custom public key infrastructure.

[NOTE]
====
The cluster-wide proxy affects system components only, not user workloads.
====

In proxy-enabled clusters, the WMCO is aware of the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` values that are set for the cluster. The WMCO periodically checks whether the proxy environment variables have changed. If there is a discrepancy, the WMCO reconciles and updates the proxy environment variables on the Windows instances.

Windows workloads created on Windows nodes in proxy-enabled clusters do not inherit proxy settings from the node by default, the same as with Linux nodes. Also, by default PowerShell sessions do not inherit proxy settings on Windows nodes in proxy-enabled clusters.

For more information on the cluster-wide proxy, see "Configuring the cluster-wide proxy".

// Module included in the following assemblies:
//
// windows_containers/enabling-windows-container-workloads.adoc

[id="wmco-disconnected-cluster_{context}"]
= Using Windows containers with a mirror registry

[role="_abstract"]
When using the Windows Machine Config Operator (WMCO), your Windows workloads can pull images from a registry mirror rather than from a public registry by using an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry.

A mirror registry has the following benefits:

* Avoids public registry outages
* Speeds up node and pod creation
* Pulls images from behind your organization's firewall

A mirror registry can also be used with a OpenShift Container Platform cluster in a disconnected, or air-gapped, network. A _disconnected network_ is a restricted network without direct internet connectivity. Because the cluster does not have access to the internet, any external container images cannot be referenced.

Using a mirror registry requires the following general steps:

* Create the mirror registry, using a tool such as {quay}.
* Create a container image registry credentials file.
* Copy the images from your online image repository to your mirror registry.

For information about these steps, see "About disconnected installation mirroring."

After creating the mirror registry and mirroring the images, you can use an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry without needing to update each of your pod specs. The IDMS and ITMS objects redirect requests to pull images from a repository on a source image registry and have it resolved by the mirror repository instead.

If changes are made to the IDMS or ITMS object, the WMCO automatically updates the appropriate `hosts.toml` file on your Windows nodes with the new information. Note that the WMCO sequentially updates each Windows node when mirror settings are changed. As such, the time required for these updates increases with the number of Windows nodes in the cluster.

Because Windows nodes configured by the WMCO rely on the containerd container runtime, the WMCO ensures that the containerd configuration files are up-to-date with the registry settings. For new nodes, these files are copied to the instances upon creation. For existing nodes, after activating the mirror registry, the registry controller uses SSH to access each node and copy the generated configuration files, replacing any existing files.

You can use a mirror registry with machine set or Bring-Your-Own-Host (BYOH) Windows nodes.

When using an IDMS or ITMS object to mirror container images on Windows nodes, take note of the following behaviors that differ from Linux nodes:

* Mirroring on Windows nodes works on the registry level, rather than on the image level used by Linux nodes. As such, Windows images mirrored by using IDMS or ITMS objects have specific naming requirements.
+
--
--

* A Windows node takes the ITMS object and uses it to configure registry-wide mirrors. In the following example, configuring `quay.io/remote-org/image` to mirror to `quay.io/my-org/image` results in the Windows node using that mirror for all images from `quay.io/remote-org`. As such, `quay.io/remote-org/image:tag` uses the `quay.io/my-org/image:tag` image, as expected, but another container using `quay.io/remote-org/different-image:tag`
would also try to use the `quay.io/remote-org/different-image:tag` mirror. This can cause unintended behavior if it is not accounted for.
+
For this reason, specify container images using a digest by an IDMS object instead of an ITMS object. Using a digest can prevent the wrong container image from being used, by ensuring that the image the container specifies and the image being pulled have the same digest.

// Module included in the following assemblies:
//
// * openshift_images/image-configuration.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update.adoc
// * windows_containers/enabling-windows-container-workloads.adoc

[id="images-configuration-registry-mirror_{context}"]
= Understanding image registry repository mirroring

[role="_abstract"]
By setting up container registry repository mirroring, you can perform the following tasks:

* Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry.
* Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used.

Repository mirroring in OpenShift Container Platform includes the following attributes:

* Image pulls are resilient to registry downtimes.
* Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images.
* A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried.
* The mirror information you enter is added to the `/etc/containers/registries.conf` file on every node in the OpenShift Container Platform cluster.
* The mirror information you enter is added to the appropriate `hosts.toml` containerd configuration file(s) on every Windows node in the OpenShift Container Platform cluster.
* When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node.

You can set up repository mirroring in the following ways:

* At OpenShift Container Platform installation:
+
By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company's firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment.

* After OpenShift Container Platform installation:
+
If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects:
+
** `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.
+
** `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.
// ICSP is not supported in WINC
+
** `ImageContentSourcePolicy` (ICSP). This object allows you to pull images from a mirrored registry by using digest specifications. The ICSP CR always falls back to the source registry if the mirrors do not work.
+
[IMPORTANT]
====
Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported. It will be removed in a future release and is not recommended for new deployments.

If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to a `ImageDigestMirrorSet` YAML files. For more information, see "Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring".
====

Each of these custom resource objects identify the following information:

* The source of the container image repository you want to mirror.
* A separate entry for each mirror repository you want to offer the content

Note the following actions and how they affect node drain behavior:

* If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node.
* If you create an ITMS CR object, the MCO drains and reboots the node.
* If you delete an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.
* If you modify an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.
+
[IMPORTANT]
====

====
* If you delete an ITMS or IDMS CR object, the MCO drains and reboots the node.
* If you modify an ITMS or IDMS CR object, the MCO drains and reboots the node.

For new clusters, you can use IDMS, ITMS, and ICSP CRs objects as needed. However, using IDMS and ITMS is recommended.

If you upgraded a cluster, any existing ICSP objects remain stable, and both IDMS and ICSP objects are supported. Workloads that use ICSP objects continue to function as expected. However, if you want to take advantage of the fallback policies introduced in the IDMS CRs, you can migrate current workloads to IDMS objects by using the `oc adm migrate icsp` command as shown in the *Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring* section that follows. Migrating to IDMS objects does not require a cluster reboot.

The Windows Machine Config Operator (WMCO) watches for changes to the IDMS and ITMS resources and generates a set of `hosts.toml` containerd configuration files, one file for each source registry, with those changes. The WMCO then updates any existing Windows nodes to use the new registry configuration.

[NOTE]
====
The IDMS and ITMS objects must be created before you can add Windows nodes using a mirrored registry.
====

// Module included in the following assemblies:
//
// * openshift_images/image-configuration.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update.adoc
// * windows_containers/enabling-windows-container-workloads.adoc

[id="images-configuration-registry-mirror-configuring_{context}"]
= Configuring image registry repository mirroring

[role="_abstract"]
You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry.

[IMPORTANT]
====
Windows images mirrored through `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects have specific naming requirements as described in "Using Windows containers with a mirror registry".
====

.Prerequisites
* Access to the cluster as a user with the `cluster-admin` role.
* Access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. Configure mirrored repositories, by either:
+
--
* Setting up a mirrored repository with {quay}. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using {quay}.

** {quay} Repository Mirroring

* Using a tool such as `skopeo` to copy images manually from the source repository to the mirrored repository.
+
For example, after installing the skopeo RPM package on a {op-system-base-full system}, use the `skopeo` command as shown in the following example:
+
[source,terminal]
----
$ skopeo copy --all \
docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \
docker://example.io/example/ubi-minimal
----
+
In this example, you have a container image registry named `example.io` and image repository named `example`. You want to copy the `ubi9/ubi-minimal` image from `registry.access.redhat.com` to `example.io`. After you create the mirrored registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository.
--
+
[IMPORTANT]
====
You must mirror the `mcr.microsoft.com/oss/kubernetes/pause:3.9` image. For example, you could use the following `skopeo` command to mirror the image:

[source,terminal]
----
$ skopeo copy \
docker://mcr.microsoft.com/oss/kubernetes/pause:3.9\
docker://example.io/oss/kubernetes/pause:3.9
----
====

. Log in to your OpenShift Container Platform cluster.

. Create a postinstallation mirror configuration custom resource (CR), by using one of the following examples:
//should note oc mirror v2 for users here; this set of docs contains mixed examples
* Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ImageDigestMirrorSet
metadata:
  name: ubi9repo
spec:
  imageDigestMirrors:
  - mirrors:
    - example.io/example/ubi-minimal
    - example.com/example2/ubi-minimal
    source: registry.access.redhat.com/ubi9/ubi-minimal
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.com/redhat
    source: registry.example.com/redhat
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.com
    source: registry.example.com
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net/image
    source: registry.example.com/example/myimage
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net
    source: registry.example.com/example
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net/registry-example-com
    source: registry.example.com
    mirrorSourcePolicy: AllowContactingSource
----

* Create an `ImageContentSourcePolicy` custom resource, replacing the source and mirrors with your own registry and repository pairs and images:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: mirror-ocp
spec:
  repositoryDigestMirrors:
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-release
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----
+
where:
+
`- mirror.registry.com:443/ocp/release`:: Specifies the name of the mirror image registry and repository.
`source: quay.io/openshift-release-dev/ocp-release`:: Specifies the online registry and repository containing the content that is mirrored.

. Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ImageDigestMirrorSet
metadata:
  name: ubi9repo
spec:
  imageDigestMirrors:
  - mirrors:
    - example.io/example/ubi-minimal
    - example.com/example2/ubi-minimal
    source: registry.access.redhat.com/ubi9/ubi-minimal
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.com
    source: registry.redhat.io
    mirrorSourcePolicy: NeverContactSource
  - mirrors:
    - docker.io
    source: docker-mirror.internal
    mirrorSourcePolicy: AllowContactingSource
----

. Create the new object by running the following command:
+
[source,terminal]
----
$ oc create -f registryrepomirror.yaml
----
+
After the object is created, the Machine Config Operator (MCO) drains the nodes for `ImageTagMirrorSet` objects only. The MCO does not drain the nodes for `ImageDigestMirrorSet` and `ImageContentSourcePolicy` objects.

. To check that the mirrored configuration settings are applied, do the following on one of the nodes.

.. List your nodes:
+
[source,terminal]
----
$ oc get node
----
+
.Example output
[source,terminal]
----
NAME                           STATUS                     ROLES    AGE  VERSION
worker-1.compute.local         Ready                      worker   7m   v1.35.4
master-1.compute.local         Ready                      master   11m  v1.35.4
master-2.compute.local         Ready                      master   11m  v1.35.4
worker-2.compute.local         Ready                      worker   7m   v1.35.4
worker-3.compute.local         Ready                      worker   7m   v1.35.4
master-3.compute.local         Ready                      master   11m  v1.35.4
----

.. Start the debugging process to access the node:
+
[source,terminal]
----
$ oc debug node/worker-1.compute.local
----
+
.Example output
[source,terminal]
----
Starting pod/worker-1.compute.local-debug ...
To use host binaries, run `chroot /host`
----

.. Change your root directory to `/host`:
+
[source,terminal]
----
sh-4.2# chroot /host
----

.. Check the `/etc/containers/registries.conf` file to make sure the changes were made:
+
[source,terminal]
----
sh-4.2# cat /etc/containers/registries.conf
----
+
The following output represents a `registries.conf` file where postinstallation mirror configuration CRs are applied.
+
.Example output
[source,terminal]
----
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]
short-name-mode = ""

[[registry]]
  prefix = ""
  location = "registry.access.redhat.com/ubi9/ubi-minimal"

  [[registry.mirror]]
    location = "example.io/example/ubi-minimal"
    pull-from-mirror = "digest-only"

  [[registry.mirror]]
    location = "example.com/example/ubi-minimal"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com"

  [[registry.mirror]]
    location = "mirror.example.net/registry-example-com"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/example"

  [[registry.mirror]]
    location = "mirror.example.net"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/example/myimage"

  [[registry.mirror]]
    location = "mirror.example.net/image"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com"

  [[registry.mirror]]
    location = "mirror.example.com"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/redhat"

  [[registry.mirror]]
    location = "mirror.example.com/redhat"
    pull-from-mirror = "digest-only"
[[registry]]
  prefix = ""
  location = "registry.access.redhat.com/ubi9/ubi-minimal"
  blocked = true

  [[registry.mirror]]
    location = "example.io/example/ubi-minimal-tag"
    pull-from-mirror = "tag-only"
----
+
where:

`\[[registry]].location = "registry.access.redhat.com/ubi9/ubi-minimal"`:: The repository listed in a pull spec.
`\[[registry.mirror]].location = "example.io/example/ubi-minimal"`:: Indicates the mirror for that repository.
`\[[registry.mirror]].pull-from-mirror = "digest-only"`:: Means that the image pull from the mirror is a digest reference image.
`\[[registry]].blocked = true`:: Indicates that the `NeverContactSource` parameter is set for this repository.
`\[[registry.mirror]].pull-from-mirror = "tag-only"`:: Indicates that the image pull from the mirror is a tag reference image.
.. Check that the WMCO generated a `hosts.toml` file for each registry on each Windows instance. For the previous example IDMS object, there should be three files in the following file structure:
+
[source,terminal]
----
$ tree $config_path
----
+
[source,terminal]
.Example output
----
C:/k/containerd/registries/
|── registry.access.redhat.com
|   └── hosts.toml
|── mirror.example.com
|   └── hosts.toml
└── docker.io
    └── hosts.toml:
----
+
The following output represents a `hosts.toml` containerd configuration file where the previous example IDMS object was applied.
+
[source,terminal]
.Example host.toml files
----
$ cat "$config_path"/registry.access.redhat.com/host.toml
server = "https://registry.access.redhat.com" # default fallback server since "AllowContactingSource" mirrorSourcePolicy is set

[host."https://example.io/example/ubi-minimal"]
 capabilities = ["pull"]

[host."https://example.com/example2/ubi-minimal"] # secondary mirror
 capabilities = ["pull"]

$ cat "$config_path"/registry.redhat.io/host.toml
# "server" omitted since "NeverContactSource" mirrorSourcePolicy is set

[host."https://mirror.example.com"]
 capabilities = ["pull"]

$ cat "$config_path"/docker.io/host.toml
server = "https://docker.io"

[host."https://docker-mirror.internal"]
 capabilities = ["pull", "resolve"] # resolve tags
----

.. Pull an image to the node from the source and check if it is resolved by the mirror.
+
[source,terminal]
----
sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
----

.Troubleshooting

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem:

* The first working mirror is used to supply the pulled image.
* The main registry is only used if no other mirror works.
* From the system context, the `Insecure` flags are used as fallback.
* The format of the `/etc/containers/registries.conf` file has changed recently. It is now version 2 and in TOML format.

//do we need this ifeval?

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

[id="nodes-nodes-rebooting-gracefully_{context}"]
= Rebooting a node gracefully

[role="_abstract"]
You can perform a graceful restart of a node, where all workloads are moved to other nodes, without data loss or service disruption.

The Windows Machine Config Operator (WMCO) minimizes node reboots whenever possible. However, certain operations and updates require a reboot to ensure that changes are applied correctly and securely. To safely reboot your Windows nodes, use the graceful reboot process. For information on gracefully rebooting a standard OpenShift Container Platform node, see "Rebooting a node gracefully" in the Nodes documentation.

Before rebooting a node, it is recommended to backup etcd data to avoid any data loss on the node.

[NOTE]
====
For {sno} clusters that require users to perform the `oc login` command rather than having the certificates in `kubeconfig` file to manage the cluster, the `oc adm` commands might not be available after cordoning and draining the node. This is because the `openshift-oauth-apiserver` pod is not running due to the cordon. You can use SSH to access the nodes as indicated in the following procedure.

In a {sno} cluster, pods cannot be rescheduled when cordoning and draining. However, doing so gives the pods, especially your workload pods, time to properly stop and release associated resources.
====

The following procedure demonstrates how to perform a graceful restart of a node.

.Procedure

. Mark the node as unschedulable:
+
[source,terminal]
----
$ oc adm cordon <node1>
----

. Drain the node to remove all the running pods:
+
[source,terminal]
----
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force
----
+
You might receive errors that pods associated with custom pod disruption budgets (PDB) cannot be evicted.
+
.Example error
[source,terminal]
----
error when evicting pods/"rails-postgresql-example-1-72v2w" -n "rails" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
----
+
In this case, run the drain command again, adding the `disable-eviction` flag, which bypasses the PDB checks:
+
[source,terminal]
----
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
----

. Access the node in debug mode:
+
[source,terminal]
----
$ oc debug node/<node1>
----

. Change your root directory to `/host`:
+
[source,terminal]
----
$ chroot /host
----

. Restart the node:
+
[source,terminal]
----
$ systemctl reboot
----
+
In a moment, the node enters the `NotReady` state.
+
[NOTE]
====
With some {sno} clusters, the `oc` commands might not be available after you cordon and drain the node because the `openshift-oauth-apiserver` pod is not running. You can use SSH to connect to the node and perform the reboot.

[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain>
----

[source,terminal]
----
$ sudo systemctl reboot
----
====
. SSH into the Windows node and enter PowerShell by running the following command:
+
[source,terminal]
----
C:\> powershell
----

. Restart the node by running the following command:
+
[source,terminal]
----
C:\>  Restart-Computer -Force
----

. Windows nodes on Amazon Web Services (AWS) do not return to `READY` state after a graceful reboot due to an inconsistency with the EC2 instance metadata routes and the Host Network Service (HNS) networks.
+
After the reboot, SSH into any Windows node on AWS and add the route by running the following command in a shell prompt:
+
[source,terminal]
----
C:\> route add 169.254.169.254 mask 255.255.255.0 <gateway_ip>
----
+
where:
+
--
`169.254.169.254`:: Specifies the address of the EC2 instance metadata endpoint.
`255.255.255.255`:: Specifies the network mask of the EC2 instance metadata endpoint.
`<gateway_ip>`:: Specifies the corresponding IP address of the gateway in the Windows instance, which you can find by running the following command:
+
[source,terminal]
----
C:\> ipconfig | findstr /C:"Default Gateway"
----
--

. After the reboot is complete, mark the node as schedulable by running the following command:
+
[source,terminal]
----
$ oc adm uncordon <node1>
----
+
[NOTE]
====
With some {sno} clusters, the `oc` commands might not be available after you cordon and drain the node because the `openshift-oauth-apiserver` pod is not running. You can use SSH to connect to the node and uncordon it.

[source,terminal]
----
$ ssh core@<target_node>
----

[source,terminal]
----
$ sudo oc adm uncordon <node> --kubeconfig /etc/kubernetes/static-pod-resources/kube-apiserver-certs/secrets/node-kubeconfigs/localhost.kubeconfig
----
====

. Verify that the node is ready:
+
[source,terminal]
----
$ oc get node <node1>
----
+
.Example output
[source,terminal]
----
NAME    STATUS  ROLES    AGE     VERSION
<node1> Ready   worker   6d22h   v1.18.3+b0068a8
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Windows Machine Config Operator prerequisites
* Configuring hybrid networking
* Configuring the cluster-wide proxy
* About disconnected installation mirroring
* Using Windows containers with a mirror registry
* Rebooting a OpenShift Container Platform node gracefully
* Backing up etcd data
* Generating a key pair for cluster node SSH access
* Adding Operators to a cluster
