---
title: "Updating managed clusters in a disconnected environment with PolicyGenerator resources and TALM"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-talm-updating-managed-policies-pg
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-talm-updating-managed-policies-pg
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Updating managed clusters in a disconnected environment with PolicyGenerator resources and TALM

[id="ztp-topology-aware-lifecycle-manager-pg"]
= Updating managed clusters in a disconnected environment with PolicyGenerator resources and TALM

You can use the {cgu-operator-first} to manage the software lifecycle of managed clusters that you have deployed using {ztp-first} and {cgu-operator-first}.
{cgu-operator} uses {rh-rhacm-first} {policy-gen-cr} policies to manage and control changes applied to target clusters.

For more information about the {cgu-operator-full}, see About the {cgu-operator-full}.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talo-platform-prepare-for-update-env-setup_{context}"]
= Setting up the disconnected environment

{cgu-operator} can perform both platform and Operator updates.

You must mirror both the platform image and Operator images that you want to update to in your mirror registry before you can use {cgu-operator} to update your disconnected clusters. Complete the following steps to mirror the images:

* For platform updates, you must perform the following steps:
+
. Mirror the desired OpenShift Container Platform image repository. Ensure that the desired platform image is mirrored by following the "Mirroring the OpenShift Container Platform image repository" procedure linked in the Additional resources. Save the contents of the `imageContentSources` section in the `imageContentSources.yaml` file:
+
.Example output
[source,yaml]
----
imageContentSources:
 - mirrors:
   - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
   source: quay.io/openshift-release-dev/ocp-release
 - mirrors:
   - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
   source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----

. Save the image signature of the desired platform image that was mirrored. You must add the image signature to the `{policy-gen-cr}` CR for platform updates. To get the image signature, perform the following steps:
+
.. Specify the desired OpenShift Container Platform tag by running the following command:
+
[source,terminal]
----
$ OCP_RELEASE_NUMBER=<release_version>
----
+
.. Specify the architecture of the cluster by running the following command:
+
[source,terminal]
----
$ ARCHITECTURE=<cluster_architecture> <1>
----
<1> Specify the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.
+
.. Get the release image digest from Quay by running the following command
+
[source,terminal]
----
$ DIGEST="$(oc adm release info quay.io/openshift-release-dev/ocp-release:${OCP_RELEASE_NUMBER}-${ARCHITECTURE} | sed -n 's/Pull From: .*@//p')"
----
+
.. Set the digest algorithm by running the following command:
+
[source,terminal]
----
$ DIGEST_ALGO="${DIGEST%%:*}"
----
+
.. Set the digest signature by running the following command:
+
[source,terminal]
----
$ DIGEST_ENCODED="${DIGEST#*:}"
----
+
.. Get the image signature from the mirror.openshift.com website by running the following command:
+
[source,terminal]
----
$ SIGNATURE_BASE64=$(curl -s "https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/${DIGEST_ALGO}=${DIGEST_ENCODED}/signature-1" | base64 -w0 && echo)
----
+
.. Save the image signature to the `checksum-<OCP_RELEASE_NUMBER>.yaml` file by running the following commands:
+
[source,terminal]
----
$ cat >checksum-${OCP_RELEASE_NUMBER}.yaml <<EOF
----
+
[source,terminal]
----
${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}
EOF
----

. Prepare the update graph. You have two options to prepare the update graph:
+
.. Use the OpenShift Update Service.
+
For more information about how to set up the graph on the hub cluster, see Deploy the operator for OpenShift Update Service and Build the graph data init container.
+
.. Make a local copy of the upstream graph. Host the update graph on an `http` or `https` server in the disconnected environment that has access to the managed cluster. To download the update graph, use the following command:
+
[source,terminal,subs="attributes+"]
----
$ curl -s https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable- -o ~/upgrade-graph_stable-
----
+
* For Operator updates, you must perform the following task:
+
** Mirror the Operator catalogs. Ensure that the desired operator images are mirrored by following the procedure in the "Mirroring Operator catalogs for use with disconnected clusters" section.

[role="_additional-resources"]
.Additional resources

* For more information about how to update {ztp-first}, see Upgrading {ztp}.

* For more information about how to mirror an OpenShift Container Platform image repository, see Mirroring the OpenShift Container Platform image repository.

* For more information about how to mirror Operator catalogs for disconnected clusters, see Mirroring Operator catalogs for use with disconnected clusters.

* For more information about how to prepare the disconnected environment and mirroring the desired image repository, see Preparing the disconnected environment.

* For more information about update channels and releases, see Understanding update channels and releases.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talo-platform-update-{policy-gen-cr}_{context}"]
= Performing a platform update with {policy-gen-cr} CRs

You can perform a platform update with the {cgu-operator}.

.Prerequisites

* Install the {cgu-operator-first}.
* Update {ztp-first} to the latest version.
* Provision one or more managed clusters with {ztp}.
* Mirror the desired image repository.
* Log in as a user with `cluster-admin` privileges.
* Create {rh-rhacm} policies in the hub cluster.

.Procedure

. Create a `{policy-gen-cr}` CR for the platform update:

.. Save the following `{policy-gen-cr}` CR in the `du-upgrade.yaml` file:
+
--
.Example of `{policy-gen-cr}` for platform update

The `{policy-gen-cr}` CR generates two policies:

* The `du-upgrade-platform-upgrade-prep` policy does the preparation work for the platform update. It creates the `ConfigMap` CR for the desired release image signature, creates the image content source of the mirrored release image repository, and updates the cluster version with the desired update channel and the update graph reachable by the managed cluster in the disconnected environment.

* The `du-upgrade-platform-upgrade` policy is used to perform platform upgrade.
--

.. Add the `du-upgrade.yaml` file contents to the `kustomization.yaml` file located in the {ztp} Git repository for the `{policy-gen-cr}` CRs and push the changes to the Git repository.
+
ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.

.. Check the created policies by running the following command:
+
[source,terminal]
----
$ oc get policies -A | grep platform-upgrade
----

. Create the `ClusterGroupUpdate` CR for the platform update with the `spec.enable` field set to `false`.

.. Save the content of the platform update `ClusterGroupUpdate` CR with the `du-upgrade-platform-upgrade-prep` and the `du-upgrade-platform-upgrade` policies and the target clusters to the `cgu-platform-upgrade.yml` file, as shown in the following example:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-platform-upgrade
  namespace: default
spec:
  managedPolicies:
  - du-upgrade-platform-upgrade-prep
  - du-upgrade-platform-upgrade
  preCaching: false
  clusters:
  - spoke1
  remediationStrategy:
    maxConcurrency: 1
  enable: false
----

.. Apply the `ClusterGroupUpdate` CR to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-platform-upgrade.yml
----

. Optional: Pre-cache the images for the platform update.
.. Enable pre-caching in the `ClusterGroupUpdate` CR by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
--patch '{"spec":{"preCaching": true}}' --type=merge
----

.. Monitor the update process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the hub cluster:
+
[source,terminal]
----
$ oc get cgu cgu-platform-upgrade -o jsonpath='{.status.precaching.status}'
----

. Start the platform update:
.. Enable the `cgu-platform-upgrade` policy and disable pre-caching by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
--patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
----

.. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:
+
[source,terminal]
----
$ oc get policies --all-namespaces
----

[role="_additional-resources"]
.Additional resources

* For more information about mirroring the images in a disconnected environment, see Preparing the disconnected environment.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talo-operator-update-{policy-gen-cr}_{context}"]
= Performing an Operator update with {policy-gen-cr} CRs

You can perform an Operator update with the {cgu-operator}.

.Prerequisites

* Install the {cgu-operator-first}.
* Update {ztp-first} to the latest version.
* Provision one or more managed clusters with {ztp}.
* Mirror the desired index image, bundle images, and all Operator images referenced in the bundle images.
* Log in as a user with `cluster-admin` privileges.
* Create {rh-rhacm} policies in the hub cluster.

.Procedure

. Update the `{policy-gen-cr}` CR for the Operator update.
.. Update the `du-upgrade` `{policy-gen-cr}` CR with the following additional contents in the `du-upgrade.yaml` file:
+

.. This update generates one policy, `du-upgrade-operator-catsrc-policy`, to update the `redhat-operators-disconnected` catalog source with the new index images that contain the desired Operators images.
+
[NOTE]
====
If you want to use the image pre-caching for Operators and there are Operators from a different catalog source other than `redhat-operators-disconnected`,  you must perform the following tasks:

* Prepare a separate catalog source policy with the new index image or registry poll interval update for the different catalog source.
* Prepare a separate subscription policy for the desired Operators that are from the different catalog source.
====
+
For example, the desired SRIOV-FEC Operator is available in the `certified-operators` catalog source. To update the catalog source and the Operator subscription, add the following contents to generate two policies, `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy`:
+

.. Remove the specified subscriptions channels in the common `{policy-gen-cr}` CR, if they exist. The default subscriptions channels from the {ztp} image are used for the update.
+
[NOTE]
====
The default channel for the Operators applied through {ztp}  is `stable`, except for the `performance-addon-operator`. As of OpenShift Container Platform 4.11, the `performance-addon-operator` functionality was moved to the `node-tuning-operator`. For the 4.10 release, the default channel for PAO is `v4.10`. You can also specify the default channels in the common `{policy-gen-cr}` CR.
====

.. Push the `{policy-gen-cr}` CRs updates to the {ztp} Git repository.
+
ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.

.. Check the created policies by running the following command:
+
[source,terminal]
----
$ oc get policies -A | grep -E "catsrc-policy|subscription"
----

. Apply the required catalog source updates before starting the Operator update.

.. Save the content of the `ClusterGroupUpgrade` CR named `operator-upgrade-prep` with the catalog source policies and the target managed clusters to the `cgu-operator-upgrade-prep.yml` file:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-operator-upgrade-prep
  namespace: default
spec:
  clusters:
  - spoke1
  enable: true
  managedPolicies:
  - du-upgrade-operator-catsrc-policy
  remediationStrategy:
    maxConcurrency: 1
----

.. Apply the policy to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-operator-upgrade-prep.yml
----

.. Monitor the update process. Upon completion, ensure that the policy is compliant by running the following command:
+
[source,terminal]
----
$ oc get policies -A | grep -E "catsrc-policy"
----

. Create the `ClusterGroupUpgrade` CR for the Operator update with the `spec.enable` field set to `false`.
.. Save the content of the Operator update `ClusterGroupUpgrade` CR with the `du-upgrade-operator-catsrc-policy` policy and the subscription policies created from the common `{policy-gen-cr}` and the target clusters to the `cgu-operator-upgrade.yml` file, as shown in the following example:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-operator-upgrade
  namespace: default
spec:
  managedPolicies:
  - du-upgrade-operator-catsrc-policy <1>
  - common-subscriptions-policy <2>
  preCaching: false
  clusters:
  - spoke1
  remediationStrategy:
    maxConcurrency: 1
  enable: false
----
<1> The policy is needed by the image pre-caching feature to retrieve the operator images from the catalog source.
<2> The policy contains Operator subscriptions. If you have followed the structure and content of the reference `PolicyGenTemplates`, all Operator subscriptions are grouped into the `common-subscriptions-policy` policy.
+
[NOTE]
====
One `ClusterGroupUpgrade` CR can only pre-cache the images of the desired Operators defined in the subscription policy from one catalog source included in the `ClusterGroupUpgrade` CR. If the desired Operators are from different catalog sources, such as in the example of the SRIOV-FEC Operator, another `ClusterGroupUpgrade` CR must be created with `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy` policies for the SRIOV-FEC Operator images pre-caching and update.
====

.. Apply the `ClusterGroupUpgrade` CR to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-operator-upgrade.yml
----

. Optional: Pre-cache the images for the Operator update.

.. Before starting image pre-caching, verify the subscription policy is `NonCompliant` at this point by running the following command:
+
[source,terminal]
----
$ oc get policy common-subscriptions-policy -n <policy_namespace>
----
+
.Example output
+
[source,terminal]
----
NAME                          REMEDIATION ACTION   COMPLIANCE STATE     AGE
common-subscriptions-policy   inform               NonCompliant         27d
----

.. Enable pre-caching in the `ClusterGroupUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
--patch '{"spec":{"preCaching": true}}' --type=merge
----

.. Monitor the process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the managed cluster:
+
[source,terminal]
----
$ oc get cgu cgu-operator-upgrade -o jsonpath='{.status.precaching.status}'
----

.. Check if the pre-caching is completed before starting the update by running the following command:
+
[source,terminal]
----
$ oc get cgu -n default cgu-operator-upgrade -ojsonpath='{.status.conditions}' | jq
----
+
.Example output
+
[source,json]
----
[
    {
      "lastTransitionTime": "2022-03-08T20:49:08.000Z",
      "message": "The ClusterGroupUpgrade CR is not enabled",
      "reason": "UpgradeNotStarted",
      "status": "False",
      "type": "Ready"
    },
    {
      "lastTransitionTime": "2022-03-08T20:55:30.000Z",
      "message": "Precaching is completed",
      "reason": "PrecachingCompleted",
      "status": "True",
      "type": "PrecachingDone"
    }
]
----

. Start the Operator update.

.. Enable the `cgu-operator-upgrade` `ClusterGroupUpgrade` CR and disable pre-caching to start the Operator update by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
--patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
----

.. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:
+
[source,terminal]
----
$ oc get policies --all-namespaces
----

[role="_additional-resources"]
.Additional resources

* For more information about updating {ztp}, see Upgrading {ztp}.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="cnf-topology-aware-lifecycle-manager-operator-troubleshooting-{policy-gen-cr}_{context}"]
= Troubleshooting missed Operator updates with {policy-gen-cr} CRs

In some scenarios, {cgu-operator-first} might miss Operator updates due to an out-of-date policy compliance state.

After a catalog source update, it takes time for the Operator Lifecycle Manager (OLM) to update the subscription status. The status of the subscription policy might continue to show as compliant while {cgu-operator} decides whether remediation is needed. As a result, the Operator specified in the subscription policy does not get upgraded.

To avoid this scenario, add another catalog source configuration to the `{policy-gen-cr}` and specify this configuration in the subscription for any Operators that require an update.

.Procedure

. Add a catalog source configuration in the `{policy-gen-cr}` resource:
+

. Update the `Subscription` resource to point to the new configuration for Operators that require an update:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: operator-subscription
  namespace: operator-namspace
# ...
spec:
  source: redhat-operators-disconnected-v2 <1>
# ...
----
<1> Enter the name of the additional catalog source configuration that you defined in the `{policy-gen-cr}` resource.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talo-operator-and-platform-update_{context}"]
= Performing a platform and an Operator update together

You can perform a platform and an Operator update at the same time.

.Prerequisites

* Install the {cgu-operator-first}.
* Update {ztp-first} to the latest version.
* Provision one or more managed clusters with {ztp}.
* Log in as a user with `cluster-admin` privileges.
* Create {rh-rhacm} policies in the hub cluster.

.Procedure

. Create the `{policy-gen-cr}` CR for the updates by following the steps described in the "Performing a platform update" and "Performing an Operator update" sections.

. Apply the prep work for the platform and the Operator update.

.. Save the content of the `ClusterGroupUpgrade` CR with the policies for platform update preparation work, catalog source updates, and target clusters to the `cgu-platform-operator-upgrade-prep.yml` file, for example:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-platform-operator-upgrade-prep
  namespace: default
spec:
  managedPolicies:
  - du-upgrade-platform-upgrade-prep
  - du-upgrade-operator-catsrc-policy
  clusterSelector:
  - group-du-sno
  remediationStrategy:
    maxConcurrency: 10
  enable: true
----

.. Apply the `cgu-platform-operator-upgrade-prep.yml` file to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-platform-operator-upgrade-prep.yml
----

.. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:
+
[source,terminal]
----
$ oc get policies --all-namespaces
----

. Create the `ClusterGroupUpdate` CR for the platform and the Operator update with the `spec.enable` field set to `false`.
.. Save the contents of the platform and Operator update `ClusterGroupUpdate` CR with the policies and the target clusters to the `cgu-platform-operator-upgrade.yml` file, as shown in the following example:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-du-upgrade
  namespace: default
spec:
  managedPolicies:
  - du-upgrade-platform-upgrade <1>
  - du-upgrade-operator-catsrc-policy <2>
  - common-subscriptions-policy <3>
  preCaching: true
  clusterSelector:
  - group-du-sno
  remediationStrategy:
    maxConcurrency: 1
  enable: false
----
<1> This is the platform update policy.
<2> This is the policy containing the catalog source information for the Operators to be updated. It is needed for the pre-caching feature to determine which Operator images to download to the managed cluster.
<3> This is the policy to update the Operators.

.. Apply the `cgu-platform-operator-upgrade.yml` file to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-platform-operator-upgrade.yml
----

. Optional: Pre-cache the images for the platform and the Operator update.
.. Enable pre-caching in the `ClusterGroupUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
--patch '{"spec":{"preCaching": true}}' --type=merge
----

.. Monitor the update process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the managed cluster:
+
[source,terminal]
----
$ oc get jobs,pods -n openshift-talm-pre-cache
----

.. Check if the pre-caching is completed before starting the update by running the following command:
+
[source,terminal]
----
$ oc get cgu cgu-du-upgrade -ojsonpath='{.status.conditions}'
----

. Start the platform and Operator update.
.. Enable the `cgu-du-upgrade` `ClusterGroupUpgrade` CR to start the platform and the Operator update by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
--patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
----

.. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:
+
[source,terminal]
----
$ oc get policies --all-namespaces
----
+
[NOTE]
====
The CRs for the platform and Operator updates can be created from the beginning by configuring the setting to `spec.enable: true`. In this case, the update starts immediately after pre-caching completes and there is no need to manually enable the CR.

Both pre-caching and the update create extra resources, such as policies, placement bindings, placement rules, managed cluster actions, and managed cluster view, to help complete the procedures. Setting the `afterCompletion.deleteObjects` field to `true` deletes all these resources after the updates complete.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talm-pao-update-{policy-gen-cr}_{context}"]
= Removing Performance Addon Operator subscriptions from deployed clusters with {policy-gen-cr} CRs

In earlier versions of OpenShift Container Platform, the Performance Addon Operator provided automatic, low latency performance tuning for applications. In OpenShift Container Platform 4.11 or later, these functions are part of the Node Tuning Operator.

Do not install the Performance Addon Operator on clusters running OpenShift Container Platform 4.11 or later. If you upgrade to OpenShift Container Platform 4.11 or later, the Node Tuning Operator automatically removes the Performance Addon Operator.

[NOTE]
====
You need to remove any policies that create Performance Addon Operator subscriptions to prevent a re-installation of the Operator.
====

The reference DU profile includes the Performance Addon Operator in the `{policy-gen-cr}` CR `{policy-prefix}common-ranGen.yaml`. To remove the subscription from deployed managed clusters, you must update `{policy-prefix}common-ranGen.yaml`.

[NOTE]
====
If you install Performance Addon Operator 4.10.3-5 or later on OpenShift Container Platform 4.11 or later, the Performance Addon Operator detects the cluster version and automatically hibernates to avoid interfering with the Node Tuning Operator functions. However, to ensure best performance, remove the Performance Addon Operator from your OpenShift Container Platform 4.11 clusters.
====

.Prerequisites

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for ArgoCD.

* Update to OpenShift Container Platform 4.11 or later.

* Log in as a user with `cluster-admin` privileges.

.Procedure

. Change the `complianceType` to `mustnothave` for the Performance Addon Operator namespace, Operator group, and subscription in the `{policy-prefix}common-ranGen.yaml` file.
+
[source,yaml]
----
----

. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The status of the `common-subscriptions-policy` policy changes to `Non-Compliant`.

. Apply the change to your target clusters by using the {cgu-operator-full}. For more information about rolling out configuration changes, see the "Additional resources" section.

. Monitor the process. When the status of the `common-subscriptions-policy` policy for a target cluster  is `Compliant`, the Performance Addon Operator has been removed from the cluster. Get the status of the `common-subscriptions-policy` by running the following command:
+
[source,terminal]
----
$ oc get policy -n ztp-common common-subscriptions-policy
----

. Delete the Performance Addon Operator namespace, Operator group and subscription CRs from `{rangen-yaml-path}` in the `{policy-prefix}common-ranGen.yaml` file.

. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The policy remains compliant.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talm-prechache-user-specified-images-concept_{context}"]
= Pre-caching user-specified images with {cgu-operator} on {sno} clusters

You can pre-cache application-specific workload images on {sno} clusters before upgrading your applications.

You can specify the configuration options for the pre-caching jobs using the following custom resources (CR):

* `PreCachingConfig` CR
* `ClusterGroupUpgrade` CR

[NOTE]
====
All fields in the `PreCachingConfig` CR are optional.
====

.Example PreCachingConfig CR
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: exampleconfig-ns
spec:
  overrides: <1>
    platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    operatorsIndexes:
      - registry.example.com:5000/custom-redhat-operators:1.0.0
    operatorsPackagesAndChannels:
      - local-storage-operator: stable
      - ptp-operator: stable
      - sriov-network-operator: stable
  spaceRequired: 30 Gi <2>
  excludePrecachePatterns: <3>
    - aws
    - vsphere
  additionalImages: <4>
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
----
<1>  By default, {cgu-operator} automatically populates the `platformImage`, `operatorsIndexes`, and the `operatorsPackagesAndChannels` fields from the policies of the managed clusters. You can specify values to override the default {cgu-operator}-derived values for these fields.
<2> Specifies the minimum required disk space on the cluster. If unspecified, {cgu-operator} defines a default value for OpenShift Container Platform images. The disk space field must include an integer value and the storage unit. For example: `40 GiB`, `200 MB`, `1 TiB`.
<3> Specifies the images to exclude from pre-caching based on image name matching.
<4> Specifies the list of additional images to pre-cache.

.Example ClusterGroupUpgrade CR with PreCachingConfig CR reference
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
spec:
  preCaching: true <1>
  preCachingConfigRef:
    name: exampleconfig <2>
    namespace: exampleconfig-ns <3>
----
<1> The `preCaching` field set to `true` enables the pre-caching job.
<2> The `preCachingConfigRef.name` field specifies the `PreCachingConfig` CR that you want to use.
<3> The `preCachingConfigRef.namespace` specifies the namespace of the `PreCachingConfig` CR that you want to use.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talm-prechache-user-specified-images-preparing-crs_{context}"]
= Creating the custom resources for pre-caching

You must create the `PreCachingConfig` CR before or concurrently with the `ClusterGroupUpgrade` CR.

. Create the `PreCachingConfig` CR with the list of additional images you want to pre-cache.
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: default <1>
spec:
[...]
  spaceRequired: 30Gi <2>
  additionalImages:
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
----
<1> The `namespace` must be accessible to the hub cluster.
<2> It is recommended to set the minimum disk space required field to ensure that there is sufficient storage space for the pre-cached images.

. Create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` and specify the `PreCachingConfig` CR created in the previous step:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
  namespace: default
spec:
  clusters:
  - sno1
  - sno2
  preCaching: true
  preCachingConfigRef:
  - name: exampleconfig
    namespace: default
  managedPolicies:
    - du-upgrade-platform-upgrade
    - du-upgrade-operator-catsrc-policy
    - common-subscriptions-policy
  remediationStrategy:
    timeout: 240
----

+
[WARNING]
====
Once you install the images on the cluster, you cannot change or delete them.
====

+
. When you want to start pre-caching the images, apply the `ClusterGroupUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu.yaml
----

{cgu-operator} verifies the `ClusterGroupUpgrade` CR.

From this point, you can continue with the {cgu-operator} pre-caching workflow.

[NOTE]
====
All sites are pre-cached concurrently.
====

.Verification

. Check the pre-caching status on the hub cluster where the `ClusterUpgradeGroup` CR is applied by running the following command:
+
[source,terminal]
----
$ oc get cgu <cgu_name> -n <cgu_namespace> -oyaml
----

+
.Example output
[source,yaml]
----
  precaching:
    spec:
      platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
      operatorsIndexes:
        - registry.example.com:5000/custom-redhat-operators:1.0.0
      operatorsPackagesAndChannels:
        - local-storage-operator: stable
        - ptp-operator: stable
        - sriov-network-operator: stable
      excludePrecachePatterns:
        - aws
        - vsphere
      additionalImages:
        - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
        - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
        - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
      spaceRequired: "30"
    status:
      sno1: Starting
      sno2: Starting
----

+
The pre-caching configurations are validated by checking if the managed policies exist.
Valid configurations of the `ClusterGroupUpgrade` and the `PreCachingConfig` CRs result in the following statuses:

+
.Example output of valid CRs
[source,yaml]
----
- lastTransitionTime: "2023-01-01T00:00:01Z"
  message: All selected clusters are valid
  reason: ClusterSelectionCompleted
  status: "True"
  type: ClusterSelected
- lastTransitionTime: "2023-01-01T00:00:02Z"
  message: Completed validation
  reason: ValidationCompleted
  status: "True"
  type: Validated
- lastTransitionTime: "2023-01-01T00:00:03Z"
  message: Precaching spec is valid and consistent
  reason: PrecacheSpecIsWellFormed
  status: "True"
  type: PrecacheSpecValid
- lastTransitionTime: "2023-01-01T00:00:04Z"
  message: Precaching in progress for 1 clusters
  reason: InProgress
  status: "False"
  type: PrecachingSucceeded
----

+
.Example of an invalid PreCachingConfig CR
[source,yaml]
----
Type:    "PrecacheSpecValid"
Status:  False,
Reason:  "PrecacheSpecIncomplete"
Message: "Precaching spec is incomplete: failed to get PreCachingConfig resource due to PreCachingConfig.ran.openshift.io "<pre-caching_cr_name>" not found"
----

. You can find the pre-caching job by running the following command on the managed cluster:
+
[source,terminal]
----
$ oc get jobs -n openshift-talo-pre-cache
----

+
.Example of pre-caching job in progress
[source,terminal]
----
NAME        COMPLETIONS       DURATION      AGE
pre-cache   0/1               1s            1s
----

. You can check the status of the pod created for the pre-caching job by running the following command:
+
[source,terminal]
----
$ oc describe pod pre-cache -n openshift-talo-pre-cache
----

+
.Example of pre-caching job in progress
[source,terminal]
----
Type        Reason              Age    From              Message
Normal      SuccesfulCreate     19s    job-controller    Created pod: pre-cache-abcd1
----

. You can get live updates on the status of the job by running the following command:
+
[source,terminal]
----
$ oc logs -f pre-cache-abcd1 -n openshift-talo-pre-cache
----

. To verify the pre-cache job is successfully completed, run the following command:
+
[source,terminal]
----
$ oc describe pod pre-cache -n openshift-talo-pre-cache
----

+
.Example of completed pre-cache job
[source,terminal]
----
Type        Reason              Age    From              Message
Normal      SuccesfulCreate     5m19s  job-controller    Created pod: pre-cache-abcd1
Normal      Completed           19s    job-controller    Job completed
----

. To verify that the images are successfully pre-cached on the {sno}, do the following:

.. Enter into the node in debug mode:
+
[source,terminal]
----
$ oc debug node/cnfdf00.example.lab
----

.. Change root to `host`:
+
[source,terminal]
----
$ chroot /host/
----

.. Search for the desired images:
+
[source,terminal]
----
$ sudo podman images | grep <operator_name>
----

[role="_additional-resources"]
.Additional resources

* For more information about the {cgu-operator} precaching workflow, see Using the container image precache feature.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

[id="talo-precache-autocreated-cgu-for-ztp_{context}"]
= About the auto-created ClusterGroupUpgrade CR for {ztp}

{cgu-operator} has a controller called `ManagedClusterForCGU` that monitors the `Ready` state of the `ManagedCluster` CRs on the hub cluster and creates the `ClusterGroupUpgrade` CRs for {ztp-first}.

For any managed cluster in the `Ready` state without a `ztp-done` label applied, the `ManagedClusterForCGU` controller automatically creates a `ClusterGroupUpgrade` CR in the `ztp-install` namespace with its associated {rh-rhacm} policies that are created during the {ztp} process. {cgu-operator} then remediates the set of configuration policies that are listed in the auto-created `ClusterGroupUpgrade` CR to push the configuration CRs to the managed cluster.

If there are no policies for the managed cluster at the time when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is created. Upon completion of the `ClusterGroupUpgrade` the managed cluster is labeled as `ztp-done`. If there are policies that you want to apply for that managed cluster, manually create a `ClusterGroupUpgrade` as a day-2 operation.

.Example of an auto-created `ClusterGroupUpgrade` CR for {ztp}

[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  generation: 1
  name: spoke1
  namespace: ztp-install
  ownerReferences:
  - apiVersion: cluster.open-cluster-management.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: ManagedCluster
    name: spoke1
    uid: 98fdb9b2-51ee-4ee7-8f57-a84f7f35b9d5
  resourceVersion: "46666836"
  uid: b8be9cd2-764f-4a62-87d6-6b767852c7da
spec:
  actions:
    afterCompletion:
      addClusterLabels:
        ztp-done: "" <1>
      deleteClusterLabels:
        ztp-running: ""
      deleteObjects: true
    beforeEnable:
      addClusterLabels:
        ztp-running: "" <2>
  clusters:
  - spoke1
  enable: true
  managedPolicies:
  - common-spoke1-config-policy
  - common-spoke1-subscriptions-policy
  - group-spoke1-config-policy
  - spoke1-config-policy
  - group-spoke1-validator-du-policy
  preCaching: false
  remediationStrategy:
    maxConcurrency: 1
    timeout: 240
----
<1> Applied to the managed cluster when {cgu-operator} completes the cluster configuration.
<2> Applied to the managed cluster when {cgu-operator} starts deploying the configuration policies.
