---
title: "Image mode for OpenShift"
type: reference
domain: openshift
slug: machine-configuration-4-22-mco-coreos-layering
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/mco-coreos-layering
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Image mode for OpenShift

[id="mco-coreos-layering"]
= Image mode for OpenShift

[role="_abstract"]
You can extend the functionality of your base {op-system} image by layering additional images onto the base image. This layering does not modify the base {op-system} image. Instead, it creates a _custom layered image_ that includes all {op-system} functionality and adds additional functionality to specific nodes in the cluster.

// Paragraph taken from Mark Russell draft (6/2/25) blog: https://docs.google.com/document/d/1DMaBg--3ljVlv0jqLJ4KjjFvGRA6J9gmF67Yq37uKdQ/edit?tab=t.0
Image mode is a cloud-native approach to operating system management that treats your OS like a container image. You define your operating system configuration as code, build it as a unified image, and deploy it consistently across your entire fleet.

[id="coreos-layering-about_{context}"]
== About {image-mode-os-lower}

{image-mode-os-caps} allows you to customize the underlying node operating system on any of your cluster nodes. This helps keep everything up-to-date, including the node operating system and any added customizations such as specialized software.

You create a custom layered image by using a Containerfile and applying it to nodes by using a custom object. At any time, you can remove the custom layered image by deleting that custom object.

With {image-mode-os-lower}, you can install RPMs into your base image, and your custom content will be booted alongside {op-system}. The Machine Config Operator (MCO) can roll out these custom layered images and monitor these custom containers in the same way it does for the default {op-system} image. {image-mode-os-caps} gives you greater flexibility in how you manage your {op-system} nodes.

// NOTE from https://issues.redhat.com/browse/OCPBUGS-2214?focusedCommentId=21430101&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-21430101

[IMPORTANT]
====
Installing realtime kernel and extensions RPMs as custom layered content is not recommended. This is because these RPMs can conflict with RPMs installed by using a machine config. If there is a conflict, the MCO enters a `degraded` state when it tries to install the machine config RPM. You need to remove the conflicting extension from your machine config before proceeding.
====

When you apply the custom layered image to your cluster, you assume the responsibility for the package you applied with the custom layered image and any issues that might arise with the package.

There are three methods for deploying a custom layered image onto your nodes:

{image-mode-os-on-caps}:: With {image-mode-os-on-lower}, you create a `MachineOSConfig` object where you include the Containerfile and other parameters. The build is performed on your cluster and the resulting custom layered image is automatically pushed to your repository and applied to the machine config pool that you specified in the `MachineOSConfig` object. The entire process is performed completely within your cluster.

{image-mode-os-out-caps}:: With {image-mode-os-out-lower}, you create a Containerfile that references an OpenShift Container Platform image and the RPM that you want to apply, build the layered image in your own environment, and push the image to your repository. Then, in your cluster, create a `MachineConfig` object for the targeted node pool that points to the new image. The Machine Config Operator overrides the base {op-system} image, as specified by the `osImageURL` value in the associated machine config, and boots the new image.

During OpenShift Container Platform installation:: You can apply a pre-built custom layered image to specific nodes during OpenShift Container Platform installation.

[IMPORTANT]
====
For these methods, use the same base {op-system} image installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image used in your cluster.
====

[id="coreos-layering-examples_{context}"]
== Example Containerfiles

{image-mode-os-caps} allows you to use the following types of images to create custom layered images:

* *OpenShift Container Platform Hotfixes*. You can work with Customer Experience and Engagement (CEE) to obtain and apply Hotfix packages on top of your {op-system} image. In some instances, you might want a bug fix or enhancement before it is included in an official OpenShift Container Platform release. {image-mode-os-caps} allows you to easily add the Hotfix before it is officially released and remove the Hotfix when the underlying {op-system} image incorporates the fix.
+
[IMPORTANT]
====
Some Hotfixes require a Red Hat Support Exception and are outside of the normal scope of OpenShift Container Platform support coverage or life cycle policies.
====
+
Hotfixes are provided to you based on Red Hat Hotfix policy. Apply it on top of the base image and test that new custom layered image in a non-production environment. When you are satisfied that the custom layered image is safe to use in production, you can roll it out on your own schedule to specific node pools. For any reason, you can easily roll back the custom layered image and return to using the default {op-system}.
+
.Example on-cluster Containerfile to apply a Hotfix
[source,yaml]
----
containerfileArch: noarch
content: |-
  FROM configs AS final
  #Install hotfix package
  RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                    https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
      dnf clean all && \
      bootc container lint
----
+
.Example out-of-cluster Containerfile to apply a Hotfix
[source,yaml]
----
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
#Install hotfix package
RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                  https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
    dnf clean all && \
    bootc container lint
----
// https://issues.redhat.com/browse/OCPBUGS-42838

* *{op-system-base} packages*. You can download {op-system-base-full} packages from the Red Hat Customer Portal, such as chrony, firewalld, and iputils.
+
.Example out-of-cluster Containerfile to apply the rsyslog utility
[source,yaml,subs="attributes+"]
----
# Using a 4.18.0 image
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
# Install rsyslog package
RUN dnf install -y rsyslog && \
    bootc container lint
# Copy your custom configuration in
ADD remote.conf /etc/rsyslog.d/remote.conf
----

* *Third-party packages*. You can download and install RPMs from third-party organizations, such as the following types of packages:
+
--
** Bleeding edge drivers and kernel enhancements to improve performance or add capabilities.
** Forensic client tools to investigate possible and actual break-ins.
** Security agents.
** Inventory agents that provide a coherent view of the entire cluster.
** SSH Key management packages.
--
+
.Example on-cluster Containerfile to apply a third-party package from EPEL
[source,yaml]
----
FROM configs AS final

#Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf install -y htop && \
    dnf clean all && \
    bootc container lint
----
+
.Example out-of-cluster Containerfile to apply a third-party package from EPEL
[source,yaml,subs="attributes+"]
----
# Get {op-system} base image of target cluster `oc adm release info --image-for rhel-coreos`
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

#Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf install -y htop && \
    dnf clean all && \
    bootc container lint
----
+
This Containerfile installs the {op-system-base} fish program. Because fish requires additional {op-system-base} packages, the image must be built on an entitled {op-system-base} host. For {op-system-base} entitlements to work, you must copy the `etc-pki-entitlement` secret into the `openshift-machine-config-operator` namespace.
+
.Example on-cluster Containerfile to apply a third-party package that has {op-system-base} dependencies
[source,yaml]
----
FROM configs AS final

# RHEL entitled host is needed here to access RHEL packages
# Install fish as third party package from EPEL
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
    dnf clean all && \
    bootc container lint
----
+
.Example out-of-cluster Containerfile to apply a third-party package that has {op-system-base} dependencies
[source,yaml,subs="attributes+"]
----
# Get {op-system} base image of target cluster `oc adm release info --image-for rhel-coreos`
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

# {op-system-base} entitled host is needed here to access {op-system-base} packages
# Install fish as third party package from EPEL
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
    dnf clean all && \
    bootc container lint
----

After you create the machine config, the Machine Config Operator (MCO) performs the following steps:

. Renders a new machine config for the specified pool or pools.
. Performs cordon and drain operations on the nodes in the pool or pools.
. Writes the rest of the machine config parameters onto the nodes.
. Applies the custom layered image to the node.
. Reboots the node using the new image.

[IMPORTANT]
====
It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.
====

// Module included in the following assemblies:
//
// * machine_configuration/mco-coreos-layering.adoc

[id="coreos-layering-configuring-on_{context}"]
= About {image-mode-os-on-lower}

You can use the {image-mode-os-lower} on-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR), as described in "Using {image-mode-os-on-caps} to apply a custom layered image".

When you create the object, the Machine Config Operator (MCO) creates a `MachineOSBuild` object and a builder pod. The process also creates transient objects, such as config maps, which are cleaned up after the build is complete. The `MachineOSBuild` object and the associated `builder-*` pod use the same naming scheme, `<MachineOSConfig_CR_name>-<hash>`, for example:

.Example `MachineOSBuild` object
[source,terminal]
----
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      True        False         False
----

.Example builder pod
[source,terminal]
----
NAME                                                      READY   STATUS      RESTARTS        AGE
build-layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae      2/2     Running     0               11m
----

You should not need to interact with these new objects or the `machine-os-builder` pod. However, you can use all of these resources for troubleshooting, if necessary.

When the build is complete, the MCO pushes the new custom layered image to your repository and rolls the image out to the nodes in the associated machine config pool. You can see the digested image pull spec for the new custom layered image in the `MachineOSConfig` object. This is now the active image pull spec for this `MachineOSConfig`.

.Example digested image pull spec
[source,terminal]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
  labels:
    machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
  name: layered-image
# ...
status:
  currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
----

[TIP]
====
You can test a `MachineOSBuild` object to make sure it builds correctly without rolling out the custom layered image to active nodes by using a custom machine config pool that contains non-production nodes. Alternatively, you can use a custom machine config pool that has no nodes. The `MachineOSBuild` object builds even if there are no nodes for the MCO to deploy the custom layered image onto.
====

You can apply a custom layered image to any machine config pool in your cluster, including the control plane, worker, or custom pools.

[NOTE]
====
For {sno} clusters, you can apply a custom layered image to the control plane node only.
====

In the case of a build failure, for example due to network issues or an invalid secret, the MCO retries the build three additional times before the job fails. The MCO creates a different build pod for each build attempt. Note that the MCO automatically removes these build pods after a short period of time. Also, the affected machine config pool reports a build failure through the `ImageBuildDegraded` status condition. You can use the build pod logs to troubleshoot any build failures.

.Example failed `MachineOSBuild` object
[source,terminal]
----
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      False        False        True     12m
----

You can manually rebuild your custom layered image by either modifying your `MachineOSConfig` object or applying an annotation to the `MachineOSConfig` object. For more information, see "Rebuilding an on-cluster custom layered image".

If you used a custom machine config pool to apply an on-cluster layered image to a node, you can remove the custom layered image from the node and revert to the base image. For more information, see "Reverting an on-cluster layered node".

You can modify an on-custom layered image as needed, to install additional packages, remove existing packages, change repositories, update secrets, or other similar changes, by editing the MachineOSConfig object. For more information, see "Modifying a custom layered image".

[id="coreos-layering-configuring-on-limitations_{context}"]
== {image-mode-os-on-caps} known limitations

Note the following limitations when working with the on-cluster layering feature:

* {image-mode-os-on-caps} is not supported on multi-architecture compute machines.
* Using multiple `MachineOSConfig` objects on the same machine config pool is not supported. You need a separate `MachineOSConfig` CR for each machine config pool where you want to use a distinct custom layered image.
* If you scale up a machine set that uses a custom layered image, the nodes reboot two times. The first, when the node is initially created with the base image and a second time when the custom layered image is applied.
* Node disruption policies are not supported on nodes with a custom layered image. However, the following machine configuration changes do not cause a new image build or the reboot of a node with an on-cluster custom layered image:
** Modifying the configuration files in the `/var` or `/etc` directory
** Adding or modifying a systemd service
** Changing SSH keys
** Removing mirroring rules from `ICSP`, `ITMS`, and `IDMS` objects
** Changing the trusted CA, by updating the `user-ca-bundle` configmap in the `openshift-config` namespace
* The following machine configuration changes do cause a new image build and a node reboot:
** Changing the kernel arguments
** Changing the `OSImageURL` parameter
** Adding or removing extensions

* The images used in creating custom layered images take up space in your push registry. Always be aware of the free space in your registry and prune the images as needed. You can automatically remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image. Note that the credentials provided by the registry push secret must also grant permission to delete an image from the registry. For more information, see "Removing an on-cluster custom layered image".

.Additional resources
* Using the {image-mode-os-on-lower} to apply a custom layered image
* Removing an on-cluster custom layered image
* Pausing the machine config pools
* Rebuilding an on-cluster custom layered image
* Reverting an on-cluster custom layered image
* Modifying a custom layered image
* About checking machine config node status

// Module included in the following assemblies:
//
// * machine_configuration/mco-coreos-layering.adoc

[id="coreos-layering-configuring-on-proc_{context}"]
= Using the {image-mode-os-on-lower} to apply a custom layered image

To apply a custom layered image to your cluster by using the on-cluster build process, create a `MachineOSConfig` custom resource (CR) that specifies the following parameters:

* the Containerfile to build
* the machine config pool to associate the build
* where the final image should be pushed and pulled from
* the push and pull secrets to use

You can create only one `MachineOSConfig` CR for each machine config pool.

.Prerequisites

* You have the pull secret in the `openshift-machine-config-operator` namespace that the Machine Config Operator (MCO) needs in order to pull the base operating system image from your repository. By default, the MCO uses the cluster global pull secret, which it synchronizes into the `openshift-machine-config-operator` namespace. You can add your pull secret to the OpenShift Container Platform global pull secret or you can use a different pull secret. For information on modifying the global pull secret, see "Updating the global cluster pull secret".

* You have the push secret of the registry that the MCO needs to push the new custom layered image to. The credentials provided by the secret must also grant permission to delete an image from the registry.
+
[NOTE]
====
In a disconnected environment, ensure that the disconnected cluster can access the registry where you want to push the image. Image mirroring applies only to pulling images.
====

* You have the pull secret that your nodes need to pull the new custom layered image from your registry. This should be a different secret than the one used to push the image to the repository.

* You are familiar with how to configure a Containerfile. Instructions on how to create a Containerfile are beyond the scope of this documentation.

* Optional: You have a separate machine config pool for the nodes where you want to apply the custom layered image. One benefit to having a custom machine config pool for the nodes it that you can easily revert to the base image, if needed. For more information, see "Reverting an on-cluster layered node".

.Procedure

. Create a `MachineOSconfig` object:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1 <1>
kind: MachineOSConfig
metadata:
  name: layered-image <2>
spec:
  machineConfigPool:
    name: layered-image <3>
  containerFile: # <4>
  - containerfileArch: NoArch <5>
    content: |-
      FROM configs AS final
      RUN dnf install -y cowsay && \
        dnf clean all && \
        bootc container lint
  imageBuilder: # <6>
    imageBuilderType: Job
  baseImagePullSecret: # <7>
    name: global-pull-secret-copy
  renderedImagePushSpec: image-registry.openshift-image-registry.svc:5000/openshift/os-image:latest  # <8>
  renderedImagePushSecret: # <9>
    name: builder-dockercfg-mtcl23
----
<1> Specifies the `machineconfiguration.openshift.io/v1` API that is required for `MachineConfig` CRs.
<2> Specifies a name for the `MachineOSConfig` object. The name must match the name of the associated machine config pool. This name is used with other {image-mode-os-on-lower} resources. The examples in this documentation use the name `layered-image`.
<3> Specifies the name of the machine config pool associated with the nodes where you want to deploy the custom layered image. The examples in this documentation use the `layered-image` machine config pool.
<4> Specifies the Containerfile to configure the custom layered image.
<5> Specifies the architecture this containerfile is to be built for: `ARM64`, `AMD64`, `PPC64LE`, `S390X`, or `NoArch`. The default is `NoArch`, which defines a Containerfile that can be applied to any architecture.
<6> Specifies the name of the image builder to use. This must be `Job`, which is a reference to the `job` object that is managing the image build.
<7> Optional: Specifies the name of the pull secret that the MCO needs to pull the base operating system image from the registry. By default, the global pull secret is used.
<8> Specifies the image registry to push the newly-built custom layered image to. This can be any registry that your cluster has access to in the `host[:port][/namespace]/name` or `svc_name.namespace.svc[:port]/repository/name:<tag>` format. This example uses the internal OpenShift Container Platform registry. You can specify a mirror registry if you cluster is properly configured to use a mirror registry.
<9> Specifies the name of the push secret that the MCO needs to push the newly-built custom layered image to that registry.

.. Create the `MachineOSConfig` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. If necessary, when the `MachineOSBuild` object has been created and is in the `READY` state, modify the node spec for the nodes where you want to use the new custom layered image:
+
.. Check that the `MachineOSBuild` object is ready, by running the following command:
+
[source,terminal]
----
$ oc get machineosbuild
----
+
When the `SUCCEEDED` value is `True`, the build is complete:
+
.Example output showing that the `MachineOSBuild` object is ready
[source,terminal]
----
NAME                                                     PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-ad5a3cad36303c363cf458ab0524e7c0-builder   False      False      True        False         False    43s
----

.. Edit the nodes where you want to deploy the custom layered image by adding a label for the machine config pool you specified in the `MachineOSConfig` object:
+
[source,terminal]
----
$ oc label node <node_name> 'node-role.kubernetes.io/<mcp_name>='
----
+
--
where:

node-role.kubernetes.io/<mcp_name>=:: Specifies a node selector that identifies the nodes to deploy the custom layered image.
--
+
When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the new custom layered image.

.Verification

. Verify that the new pods are ready by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-machine-config-operator
----
+
.Example output
[source,terminal]
----
NAME                                                                    READY   STATUS    RESTARTS   AGE
build-layered-image-ad5a3cad36303c363cf458ab0524e7c0-hxrws              2/2     Running   0          2m40s # <1>
# ...
machine-os-builder-6fb66cfb99-zcpvq                                     1/1     Running   0          2m42s # <2>
----
<1> This is the build pod where the custom layered image is building, named in the `build-<MachineOSConfig_CR_name>-<hash>` format.
<2> This pod can be used for troubleshooting.

. Verify the custom layered image build by running a command similar to the following:
+
[source,terminal]
----
$ oc get machineconfigpool <mcp_name> -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  labels:
    machineconfiguration.openshift.io/mco-built-in: ""
    pools.operator.machineconfiguration.openshift.io/layered: ""
  name: layered
# ...
status:
# ...
  conditions
# ...
  - lastTransitionTime: "2025-09-09T13:43:35Z"
    message: 'Failed to build OS image for pool worker (MachineOSBuild: worker-2d03dc921ff0c242c5892a3ef1ed1608):
      Failed: Build Failed'
    reason: BuildFailed
    status: "True" <1>
    type: ImageBuildDegraded
----
<1> Indicates whether the custom layered image build failed. If `False`, the build succeeded. If `True`, the build failed. You can use the build pod logs to troubleshoot any build failures.

. Verify the current stage of your layered build by running the following command:
+
[source,terminal]
----
$ oc get machineosbuilds
----
+
.Example output
[source,terminal]
----
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-ad5a3cad36303c363cf458ab0524e7c0   False      True       False       False         False    12m <1>
----
<1> The `MachineOSBuild` is named in the `<MachineOSConfig_CR_name>-<hash>` format.
+
The build is complete when `BUILDING` is `False` and `SUCCEEDED` is `True`.

. When the build is complete, verify that the image has been applied to the nodes in the affected pool by running a command similar to the following:
+
[source,terminal]
----
$ oc describe machineconfignode/<machine_config_node_name>
----
+
--
--
+
--
--

. Verify that the `MachineOSConfig` object contains a reference to the new custom layered image by running the following command:
+
[source,terminal]
----
$ oc describe machineosconfig <object_name>
----
+
.Example digested image pull spec
[source,terminal]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
  labels:
    machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
  name: layered-image
# ...
status:
  currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754 <1>
----
<1> Digested image pull spec for the new custom layered image.

. Verify that the appropriate nodes are using the new custom layered image:

.. Start a debug session as root for a control plane node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

.. Set `/host` as the root directory within the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

.. Run the `rpm-ostree status` command to view that the custom layered image is in use:
+
[source,terminal]
----
sh-5.1# rpm-ostree status
----
+
.Example output
[source,terminal]
----
# ...
Deployments:
* ostree-unverified-registry:image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
                   Digest: sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754 <1>
                  Version: 419.94.202502100215-0 (2025-02-12T19:20:44Z)
----
<1> Digested image pull spec for the new custom layered image.

.Additional resources
* Updating the global cluster pull secret
* Reverting an on-cluster custom layered image
* Enabling features using feature gates

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-configuring-on-modifying_{context}"]
= Modifying an on-cluster custom layered image

You can modify an on-cluster custom layered image, as needed. This allows you to install additional packages, remove existing packages, change the pull or push repositories, update secrets, or other similar changes. You can edit the `MachineOSConfig` object, apply changes to the YAML file that created the `MachineOSConfig` object, or create a new YAML file for that purpose.

If you modify and apply the `MachineOSConfig` object YAML or create a new YAML file, the YAML overwrites any changes you made directly to the `MachineOSConfig` object itself.

.Prerequisites

* You have opted in to {image-mode-os-on-lower} by creating a `MachineOSConfig` object.

.Procedure

* Modify an object to update the associated custom layered image:

.. Edit the `MachineOSConfig` object to modify the custom layered image. The following example adds the `rngd` daemon to nodes that already have the tree package that was installed using a custom layered image.
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  name: layered-image
spec:
  machineConfigPool:
    name: layered-image
  containerFile:
  - containerfileArch: noarch
    content: |- <1>
      FROM configs AS final

      RUN rpm-ostree install rng-tools && \
          systemctl enable rngd && \
          rpm-ostree cleanup -m && \
          bootc container lint

      RUN rpm-ostree install tree && \
          bootc container lint
  imageBuilder:
    imageBuilderType: PodImageBuilder
  baseImagePullSecret:
    name: global-pull-secret-copy <2>
  renderedImagePushspec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images:latest <3>
  renderedImagePushSecret:  <4>
    name: new-secret-name
----
<1> Optional: Modify the Containerfile, for example to add or remove packages.
<2> Optional: Update the secret needed to pull the base operating system image from the registry.
<3> Optional: Modify the image registry to push the newly built custom layered image to.
<4> Optional: Update the secret needed to push the newly built custom layered image to the registry.
+
When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base {op-system-first} image. If your changes modify a secret only, no new build is triggered and no reboot is performed.

.Verification

. Verify that the new `MachineOSBuild` object was created by using the following command:
+
[source,terminal]
----
$ oc get machineosbuild
----
+
.Example output
[source,terminal]
----
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-a5457b883f5239cdcb71b57e1a30b6ef   False      False      True        False         False    4d17h
layered-image-f91f0f5593dd337d89bf4d38c877590b   False      True       False       False         False    2m41s <1>
----
<1> The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building. When the `SUCCEEDED` column reports `True`, the build is complete.

. You can watch as the new machine config is rolled out to the nodes by using the following command:
+
[source,terminal]
----
$ oc get machineconfigpools
----
+
.Example output
[source,terminal]
----
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      3h38m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     True       False      2              2                   2                     0                      3h38m <1>
----
<1> The value `FALSE` in the `UPDATED` column indicates that the `MachineOSBuild` object is building. When the `UPDATED` column reports `FALSE`, the new custom layered image has rolled out to the nodes.

. When the node is back in the `Ready` state, check that the changes were applied:

.. Open an `oc debug` session to the node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

.. Set `/host` as the root directory within the debug shell by running the following command:
+
[source,terminal]
----
sh-5.1# chroot /host
----

.. Use an appropriate command to verify that change was applied. The following examples shows that the `rngd` daemon was installed:
+
[source,terminal]
----
sh-5.1# rpm -qa |grep rng-tools
----
+
.Example output
[source,terminal]
----
rng-tools-6.17-3.fc41.x86_64
----
+
[source,terminal]
----
sh-5.1# rngd -v
----
+
.Example output
[source,terminal]
----
rngd 6.16
----

.Additional resources
* Pausing the machine config pools

Hiding extensions, not in 4.18. Maybe 4.19?

.Additional resources
* Adding extensions to RHCOS
* Pausing the machine config pools

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-configuring-on-rebuild_{context}"]
= Rebuilding an on-cluster custom layered image

In situations where you want to rebuild an on-cluster custom layered image, you can either modify your `MachineOSConfig` object or add an annotation to the `MachineOSConfig` object. Both of these actions trigger an automatic rebuild of the object. For example, you could perform a rebuild if the you change the Containerfile or need to update the `osimageurl` location in a machine config.

After you add the annotation, the Machine Config Operator (MCO) deletes the current `MachineOSBuild` object and creates a new one in its place. When the build process is complete, the MCO automatically removes the annotation.

.Prerequisites

* You have opted-in to {image-mode-os-on-lower} by creating a `MachineOSConfig` object.

.Procedure

* Edit the `MachineOSConfig` object to add the `machineconfiguration.openshift.io/rebuild` annotation by using the following command:
+
[source,terminal]
----
$ oc edit MachineOSConfig <object_name>
----
+
.Example `MachineOSConfig` object
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
    machineconfiguration.openshift.io/rebuild: "" <1>
# ...
  name: layered-image
# ...
----
<1> Add this annotation to trigger a rebuild of the custom layered image.

.Verification

* Check that the `MachineOSBuild` object is building by using the following command:
+
[source,terminal]
----
$ oc get machineosbuild
----
+
.Example output
[source,terminal]
----
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-d6b929a29c6dbfa8e4007c8069a2fd08   False      True       False       False         False    2m41s <1>
----
<1> The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building.

* Edit the `MachineOSConfig` object to verify that the MCO removed the `machineconfiguration.openshift.io/rebuild` annotation by using the following command:
+
[source,terminal]
----
$ oc edit MachineOSConfig <object_name>
----
+
.Example `MachineOSConfig` object
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
# ...
  name: layered-image
# ...
----

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-configuring-on-revert_{context}"]
= Reverting an on-cluster custom layered image

If you applied an on-cluster layered image to a node in a custom machine config pool (MCP), you can remove the custom layered image from the node and revert to the base image.

To revert the node, remove the node from the custom MCP by removing the custom machine config pool label from the node. After you remove the label, the Machine Config Operator (MCO) reboots the node with the cluster base {op-system-first} image, overriding the custom layered image.

[IMPORTANT]
====
Before you remove the label, make sure the node is associated with another MCP.
====

.Prerequisites

* You have opted-in to {image-mode-os-on-caps} by creating a `MachineOSConfig` object.
* You have applied a `MachineOSConfig` object to a node in a custom machine config pool.

.Procedure

* Remove the label from the node by using the following command:
+
[source,terminal]
----
$ oc label node/<node_name> node-role.kubernetes.io/<mcp_name>-
----
+
When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base {op-system-first} image.

.Verification

* Verify that the custom layered image is removed by performing any of the following checks:

** Check that the worker machine config pool is updating with the previous machine config:
+
[source,terminal]
----
$ oc get mcp
----
+
.Sample output
[source,terminal]
----
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
layered   rendered-layered-e8c8bc1de69777325003e80bc0c04b82   True      False      False      0              0                   0                     0                      4h20m <1>
master    rendered-master-50d7bc27ee8b9ca2250383f0647ade7f    True      False      False      3              3                   3                     0                      5h39m
worker    rendered-worker-e8c8bc1de69777325003e80bc0c04b82    True      False      False      3              3                   3                     0                      5h39m <2>
----
<1> The custom machine config pool no longer has any nodes.
<2> When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config.

** Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                         STATUS                     ROLES                  AGE   VERSION
ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
----

** When the node is back in the `Ready` state, check that the node is using the base image:
+
. Open an `oc debug` session to the node. For example:
+
[source,terminal]
----
$ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
----
+
. Set `/host` as the root directory within the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. Run the `rpm-ostree status` command to view that the base image is in use:
+
[source,terminal]
----
sh-4.4# rpm-ostree status
----
+
.Example output
+
----
State: idle
Deployments:
* ostree-unverified-registry:registry.build05.ci.openshift.org/ci-ln-qd0hmqk/stable@sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                   Digest: sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                  Version: 419.96.202501202201-0 (2025-01-20T22:06:13Z)
----

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-configuring-on-remove_{context}"]
= Removing an on-cluster custom layered image

To prevent the custom layered images from taking up excessive space in your registry, you can automatically remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image.

The credentials provided by the registry push secret that you added to the `MachineOSBuild` object must grant the permission for deleting an image from the registry. If the delete permission is not provided, the image is not removed when you delete the `MachineOSBuild` object.

The custom layered image is not deleted if the image is either currently in use on a node or is desired by the nodes, as indicated by the `machineconfiguration.openshift.io/currentImage` or `machineconfiguration.openshift.io/desiredImage` annotations on the node, which are added to the node when you create the `MachineOSConfig` object.

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-configuring_{context}"]
= Using {image-mode-os-out-caps} to apply a custom layered image

You can use the {image-mode-os-lower} out-of-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR).

When you create the object, the Machine Config Operator (MCO) reboots those nodes with the new custom layered image, overriding the base {op-system-first} image.

To apply a custom layered image to your cluster, you must have the custom layered image in a repository that your cluster can access. Then, create a `MachineConfig` object that points to the custom layered image. You need a separate `MachineConfig` object for each machine config pool that you want to configure.

[IMPORTANT]
====
As soon as you apply an out-of-cluster custom image to your cluster, you effectively _take ownership_ of your custom layered images and those nodes. OpenShift Container Platform no longer automatically updates any node that uses the custom layered image. You become responsible for maintaining and updating your nodes as appropriate. If you roll back the custom layer, OpenShift Container Platform resumes automatically updating the node. See the "Updating with a RHCOS custom layered image" for important information about updating nodes that use a custom layered image.
====

.Prerequisites

* You must create a custom layered image that is based on an OpenShift Container Platform image digest, not a tag.
+
[NOTE]
====
You should use the same base {op-system} image that is installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image being used in your cluster.
====
+
For example, the following Containerfile creates a custom layered image from an OpenShift Container Platform  image and overrides the kernel package with one from CentOS 9 Stream:
+
.Example Containerfile for a custom layer image
[source,yaml,subs="+attributes"]
----
# Using a .0 image
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256... <1>
#Install hotfix rpm
RUN rpm-ostree override replace http://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/Packages/kernel-{,core-,modules-,modules-core-,modules-extra-}5.14.0-295.el9.x86_64.rpm && \ <2>
    rpm-ostree cleanup -m && \
    bootc container lint
----
<1> Specifies the {op-system} base image of your cluster.
<2> Replaces the kernel packages.
+
[NOTE]
====
Instructions on how to create a Containerfile are beyond the scope of this documentation.
====

* Because the process for building a custom layered image is performed outside of the cluster, you must use the `--authfile /path/to/pull-secret` option with Podman or Buildah. Alternatively, to have the pull secret read by these tools automatically, you can add it to one of the default file locations: `~/.docker/config.json`, `$XDG_RUNTIME_DIR/containers/auth.json`, `~/.docker/config.json`, or `~/.dockercfg`. Refer to the `containers-auth.json` man page for more information.

* You must push the custom layered image to a repository that your cluster can access.

.Procedure

. Create a machine config file.

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker <1>
  name: os-layer-custom
spec:
  osImageURL: quay.io/my-registry/custom-image@sha256... <2>
----
<1> Specifies the machine config pool to deploy the custom layered image.
<2> Specifies the path to the custom layered image in the repository.

.. Create the `MachineConfig` object:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
+
[IMPORTANT]
====
It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.
====

.Verification

You can verify that the custom layered image is applied by performing any of the following checks:

. Check that the worker machine config pool has rolled out with the new machine config:

.. Check that the new machine config is created:
+
[source,terminal]
----
$ oc get mc
----
+
.Sample output
[source,terminal]
----
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
00-master                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
00-worker                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-master-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-master-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-worker-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-worker-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-master-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-master-ssh                                                                                 3.2.0             98m
99-worker-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-worker-ssh                                                                                 3.2.0             98m
os-layer-custom                                                                                                 10s <1>
rendered-master-15961f1da260f7be141006404d17d39b   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
rendered-worker-5aff604cb1381a4fe07feaf1595a797e   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
rendered-worker-5de4837625b1cbc237de6b22bc0bc873   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             4s  <2>
----
<1> New machine config
<2> New rendered machine config

.. Check that the `osImageURL` value in the new machine config points to the expected image:
+
[source,terminal]
----
$ oc describe mc rendered-worker-5de4837625b1cbc237de6b22bc0bc873
----
+
.Example output
[source,terminal,subs="attributes+"]
----
Name:         rendered-worker-5de4837625b1cbc237de6b22bc0bc873
Namespace:
Labels:       <none>
Annotations:  machineconfiguration.openshift.io/generated-by-controller-version: 5bdb57489b720096ef912f738b46330a8f577803
              machineconfiguration.openshift.io/release-image-version: .0-ec.3
API Version:  machineconfiguration.openshift.io/v1
Kind:         MachineConfig
...
  Os Image URL: quay.io/my-registry/custom-image@sha256...
----

.. Check that the associated machine config pool is updated with the new machine config:
+
[source,terminal]
----
$ oc get mcp
----
+
.Sample output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-15961f1da260f7be141006404d17d39b   True      False      False      3              3                   3                     0                      39m
worker   rendered-worker-5de4837625b1cbc237de6b22bc0bc873   True      False      False      3              0                   0                     0                      39m <1>
----
<1> When the `UPDATING` field is `True`, the machine config pool is updating with the new machine config. In this case, you will not see the new machine config listed in the output. When the field becomes `False`, the worker machine config pool has rolled out to the new machine config.

.. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                         STATUS                     ROLES                  AGE   VERSION
ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
----

. When the node is back in the `Ready` state, check that the node is using the custom layered image:

.. Open an `oc debug` session to the node. For example:
+
[source,terminal]
----
$ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
----

.. Set `/host` as the root directory within the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

.. Run the `rpm-ostree status` command to view that the custom layered image is in use:
+
[source,terminal]
----
sh-4.4# sudo rpm-ostree status
----
+
.Example output
+
----
State: idle
Deployments:
* ostree-unverified-registry:quay.io/my-registry/...
                   Digest: sha256:...
----

.Additional resources
Updating with a {op-system} custom layered image

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-removing_{context}"]
= Reverting an out-of-cluster node

You can revert an out-of-cluster custom layered image from the nodes in specific machine config pools. The Machine Config Operator (MCO) reboots those nodes with the cluster base {op-system-first} image, overriding the custom layered image.

To remove a {op-system-first} custom layered image from your cluster, you need to delete the machine config that applied the image.

.Procedure

* Delete the machine config that applied the custom layered image.
+
[source,terminal]
----
$ oc delete mc os-layer-custom
----
+
After deleting the machine config, the nodes reboot.

.Verification

You can verify that the custom layered image is removed by performing any of the following checks:

. Check that the worker machine config pool is updating with the previous machine config:
+
[source,terminal]
----
$ oc get mcp
----
+
.Sample output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-6faecdfa1b25c114a58cf178fbaa45e2   True      False      False      3              3                   3                     0                      39m
worker   rendered-worker-6b000dbc31aaee63c6a2d56d04cd4c1b   False     True       False      3              0                   0                     0                      39m <1>
----
<1> When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config.

. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                         STATUS                     ROLES                  AGE   VERSION
ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
----

. When the node is back in the `Ready` state, check that the node is using the base image:

.. Open an `oc debug` session to the node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

.. Set `/host` as the root directory within the debug shell by running the following command:
+
[source,terminal]
----
sh-5.1# chroot /host
----

.. Run the `rpm-ostree status` command to view that the custom layered image is in use:
+
[source,terminal]
----
sh-5.1# sudo rpm-ostree status
----
+
.Example output
+
----
State: idle
Deployments:
* ostree-unverified-registry:podman pull quay.io/openshift-release-dev/ocp-release@sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
                   Digest: sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
----

// Module included in the following assemblies:
//
// * machine_configuration/mco-coreos-layering.adoc

[id="coreos-layering-install-time_{context}"]
= Applying a custom layered image during OpenShift Container Platform installation

[role="_abstract"]
You can use the standard OpenShift Container Platform installation process to apply a custom layered image to your nodes by adding a `MachineOSConfig` custom resource (CR) YAML and a push secret YAML to the `<installation_directory>/manifests/` directory. This allows you to use {image-mode-os-lower} to apply additional functionality to specific nodes upon cluster installation.

With {image-mode-os-lower}, you can extend the functionality of your base {op-system-first} image by layering additional images onto the base image. This layering does not modify the base RHCOS image. Instead, it creates a custom layered image that includes all {op-system} functionality and adds additional functionality to specific nodes in the cluster. For example, you can create custom layered images to apply hotfixes, RHEL packages, or third-party RPMs to the nodes your cluster.

For more information on {image-mode-os-lower}, see the "Additional resources" section.

After the installation, if you modify a machine config pool or update the OpenShift Container Platform version, the Machine Config Operator (MCO) builds and applies a new custom layered image, and pushes the updated image to your repository.

.Prerequisites

* You have a custom layered image in a repository that your cluster can access.
+
.Example containerFile for a custom layered image
[source,yaml]
----
FROM quay.io/centos/centos:stream9 AS centos
RUN dnf install -y epel-release

FROM [rhel-coreos image] AS configs
COPY --from=centos /etc/yum.repos.d /etc/yum.repos.d
COPY --from=centos /etc/pki/rpm-gpg/RPM-GPG-KEY-* /etc/pki/rpm-gpg/
RUN sed -i 's/\$stream/9-stream/g' /etc/yum.repos.d/centos*.repo && \
    rpm-ostree install cowsay && \
    ostree container commit
----

* You have a repository and any needed secret where the MCO can push any updated custom layered images.

.Procedure

. Create a YAML file for the push secret similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: push-secret
  namespace: openshift-machine-config-operator
data:
  .dockerconfigjson: secret
type: kubernetes.io/dockerconfigjson
----

. When the `manifests` directory is available, add the `MachineOSConfig` YAML to the directory by using a command similar to the following:
+
[source,terminal]
----
$ cp <file-name>.yaml manifests/
----
where:
+
`file-name`:: Specifies the YAML file for the `MachineOSConfig` object.

. Add the push secret YAML to the `manifests` directory by using a command similar to the following:
+
[source,terminal]
----
$ cp <file-name>.yaml manifests/
----
where:
+
`file-name`:: Specifies the YAML file for the push secret.

. Continue with the installation process as usual.

.Verification

* After the installation is complete, check that the `MachineOSConfig` object displays the `PreBuiltImageSeeded` status as `True` and contains a reference to the custom layered image by using the following command:
+
[source,terminal]
----
$ oc get machineosconfigs.machineconfiguration.openshift.io -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineOSConfig
  metadata:
    annotations:
      machineconfiguration.openshift.io/current-machine-os-build: worker-4cedbc10da849ae7019288febc3a2d17
# ...
  status:
    conditions:
    - lastTransitionTime: "2025-11-19T13:32:17Z"
      message: MachineOSConfig seeded with pre-built image "quay.io/myorg/custom-rhcos@sha256:abc123..."
      reason: PreBuiltImageSeeded
      status: "True"
      type: Seeded
    currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/layered-rhcos@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
----
where:
+
--
`items.status.conditions.reason.PreBuiltImageSeeded.True`:: Specifies that the associated nodes were created using your custom layered image.
`items.status.currentImagePullSpec`:: Specifies the digested image pull spec for the new custom layered image.
--

// Module included in the following assemblies:
//
// * machine_configuration/coreos-layering.adoc

[id="coreos-layering-updating_{context}"]
= Updating with a {op-system} custom layered image

When you configure {image-mode-os-lower}, OpenShift Container Platform no longer automatically updates the node pool that uses the custom layered image. You become responsible to manually update your nodes as appropriate.

To update a node that uses a custom layered image, follow these general steps:

. The cluster automatically upgrades to version x.y.z+1, except for the nodes that use the custom layered image.

. You could then create a new Containerfile that references the updated OpenShift Container Platform image and the RPM that you had previously applied.

. Create a new machine config that points to the updated custom layered image.

Updating a node with a custom layered image is not required. However, if that node gets too far behind the current OpenShift Container Platform version, you could experience unexpected results.

Sources:
https://docs.google.com/document/d/1Eow2IReNWqnIh5HvCfcKV2MWgHUmFKSnBkt2rH6_V_M/edit
https://hackmd.io/OKc5ZnN7SQm3myHaGqksBg
https://github.com/openshift/enhancements/blob/master/enhancements/ocp-coreos-layering/ocp-coreos-layering.md
https://docs.google.com/document/d/1RbfCJuL_NBaWvUmd9nmiG8-7MwzsvWHjrIS2LglCYM0/edit
