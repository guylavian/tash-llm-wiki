---
title: "Updating {ztp}"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-updating-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-updating-gitops
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Updating {ztp}

[id="ztp-updating-gitops"]
= Updating {ztp}

You can update the {ztp-first} infrastructure independently from the hub cluster, {rh-rhacm-first}, and the managed OpenShift Container Platform clusters.

[NOTE]
====
You can update the {gitops-title} Operator when new versions become available. When updating the {ztp} plugin, review the updated files in the reference configuration and ensure that the changes meet your requirements.
====

[role="_additional-resources"]
.Additional resources

* Configuring managed cluster policies by using PolicyGenerator resources

* Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-updating-gitops-ztp_{context}"]
= Overview of the {ztp} update process

You can update {ztp-first} for a fully operational hub cluster running an earlier version of the {ztp} infrastructure. The update process avoids impact on managed clusters.

[NOTE]
====
Any changes to policy settings, including adding recommended content, results in updated policies that must be rolled out to the managed clusters and reconciled.
====

At a high level, the strategy for updating the {ztp} infrastructure is as follows:

. Label all existing clusters with the `ztp-done` label.

. Stop the ArgoCD applications.

. Install the new {ztp} tools.

. Update required content and optional changes in the Git repository.

. Enable pulling the ISO images for the desired OpenShift Container Platform version.

. Update and restart the application configuration.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-preparing-for-the-gitops-ztp-upgrade_{context}"]
= Preparing for the upgrade

Use the following procedure to prepare your site for the {ztp-first} upgrade.

.Procedure

. Get the latest version of the {ztp} container that has the custom resources (CRs) used to configure {gitops-title} for use with {ztp}.

. Extract the `argocd/deployment` directory by using the following commands:
+
[source,terminal]
----
$ mkdir -p ./update
----
+
[source,terminal,subs="attributes+"]
----
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v extract /home/ztp --tar | tar x -C ./update
----
+
The `/update` directory contains the following subdirectories:
+
* `update/extra-manifest`: contains the source CR files that you package into a `ConfigMap` and reference in the `ClusterInstance` CR using the `extraManifestsRefs` field.
* `update/source-crs`: contains the source CR files that the `PolicyGenerator` or `PolicyGentemplate` CR uses to generate the {rh-rhacm-first} policies.
* `update/argocd/deployment`: contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure.
* `update/argocd/example`: contains example `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration.

. Update the `clusters-app.yaml` and `policies-app.yaml` files to reflect the name of your applications and the URL, branch, and path for your Git repository.
+
If the upgrade includes changes that results in obsolete policies, the obsolete policies should be removed prior to performing the upgrade.

. Diff the changes between the configuration and deployment source CRs in the `/update` folder and Git repo where you manage your fleet site CRs. Apply and push the required changes to your site repository.
+
[IMPORTANT]
====
When you update {ztp} to the latest version, you must apply the changes from the `update/argocd/deployment` directory to your site repository. Do not use older versions of the `argocd/deployment/` files.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-labeling-the-existing-clusters_{context}"]
= Labeling the existing clusters

To ensure that existing clusters remain untouched by the tool updates, label all existing managed clusters with the `ztp-done` label.

[NOTE]
====
This procedure only applies when updating clusters that were not provisioned with {cgu-operator-first}. Clusters that you provision with {cgu-operator} are automatically labeled with `ztp-done`.
====

.Procedure

. Find a label selector that lists the managed clusters that were deployed with {ztp-first}, such as `local-cluster!=true`:
+
[source,terminal]
----
$ oc get managedcluster -l 'local-cluster!=true'
----

. Ensure that the resulting list contains all the managed clusters that were deployed with {ztp}, and then use that selector to add the `ztp-done` label:
+
[source,terminal]
----
$ oc label managedcluster -l 'local-cluster!=true' ztp-done=
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-stopping-the-existing-gitops-ztp-applications_{context}"]
= Stopping the existing {ztp} applications

Removing the existing applications ensures that any changes to existing content in the Git repository are not rolled out until the new version of the tools is available.

Use the application files from the `deployment` directory. If you used custom names for the applications, update the names in these files first.

.Procedure

. Perform a non-cascaded delete on the `clusters` application to leave all generated resources in place:
+
[source,terminal]
----
$ oc delete -f update/argocd/deployment/clusters-app.yaml
----

. Perform a cascaded delete on the `policies` application to remove all previous policies:
+
[source,terminal]
----
$ oc patch -f policies-app.yaml -p '{"metadata": {"finalizers": ["resources-finalizer.argocd.argoproj.io"]}}' --type merge
----
+
[source,terminal]
----
$ oc delete -f update/argocd/deployment/policies-app.yaml
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-required-changes-to-the-git-repository_{context}"]
= Required changes to the Git repository

When upgrading the `ztp-site-generate` container from an earlier release of {ztp-first} to 4.10 or later, there are additional requirements for the contents of the Git repository. Existing content in the repository must be updated to reflect these changes.

[NOTE]
====
The following procedure assumes you are using `PolicyGenerator` resources instead of `PolicyGentemplate` resources for cluster policies management.
====

* Make required changes to `PolicyGenerator` files:
+
All `PolicyGenerator` files must be created in a `Namespace` prefixed with `ztp`. This ensures that the {ztp} application is able to manage the policy CRs generated by {ztp} without conflicting with the way {rh-rhacm-first} manages the policies internally.

* Add the `kustomization.yaml` file to the repository:
+
All `ClusterInstance` and `PolicyGenerator` CRs must be included in a `kustomization.yaml` file under their respective directory trees. For example:
+
[source,terminal]
----
├── acmpolicygenerator
│   ├── site1-ns.yaml
│   ├── site1.yaml
│   ├── site2-ns.yaml
│   ├── site2.yaml
│   ├── common-ns.yaml
│   ├── common-ranGen.yaml
│   ├── group-du-sno-ranGen-ns.yaml
│   ├── group-du-sno-ranGen.yaml
│   └── kustomization.yaml
└── clusterinstance
    ├── site1.yaml
    ├── site2.yaml
    └── kustomization.yaml
----
+
[NOTE]
====
The files listed in the `generator` sections must contain either `ClusterInstance` or `{policy-gen-cr}` CRs only. If your existing YAML files contain other CRs, for example, `Namespace`, these other CRs must be pulled out into separate files and listed in the `resources` section.
====
+
The `PolicyGenerator` kustomization file must contain all `PolicyGenerator` YAML files in the `generator` section and `Namespace` CRs in the `resources` section. For example:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

generators:
- acm-common-ranGen.yaml
- acm-group-du-sno-ranGen.yaml
- site1.yaml
- site2.yaml

resources:
- common-ns.yaml
- acm-group-du-sno-ranGen-ns.yaml
- site1-ns.yaml
- site2-ns.yaml
----
+
The `ClusterInstance` kustomization file must contain all `ClusterInstance` YAML files in the `generator` section and any other CRs in the resources:
+
[source,terminal]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

generators:
- site1.yaml
- site2.yaml
----

* Remove the `pre-sync.yaml` and `post-sync.yaml` files.
+
In OpenShift Container Platform 4.10 and later, the `pre-sync.yaml` and `post-sync.yaml` files are no longer required. The `update/deployment/kustomization.yaml` CR manages the policies deployment on the hub cluster.
+
[NOTE]
====
There is a set of `pre-sync.yaml` and `post-sync.yaml` files under both the `ClusterInstance` and `{policy-gen-cr}` trees.
====

* Review and incorporate recommended changes
+
Each release may include additional recommended changes to the configuration applied to deployed clusters. Typically these changes result in lower CPU use by the OpenShift platform, additional features, or improved tuning of the platform.
+
Review the reference `ClusterInstance` and `PolicyGenerator` CRs applicable to the types of cluster in your network. These examples can be found in the `argocd/example` directory extracted from the {ztp} container.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-installing-the-new-gitops-ztp-applications_{context}"]
= Installing the new {ztp} applications

Using the extracted `argocd/deployment` directory, and after ensuring that the applications point to your site Git repository, apply the full contents of the deployment directory. Applying the full contents of the directory ensures that all necessary resources for the applications are correctly configured.

.Procedure

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops-ztp.adoc

[id="ztp-pulling-ocp-images_{context}"]
= Pulling ISO images for the desired OpenShift Container Platform version

To pull ISO images for the desired OpenShift Container Platform version, update the `AgentServiceConfig` custom resource (CR) with references to the desired ISO and RootFS images that are hosted on the mirror registry HTTP server.

.Prerequisites

* You have installed the {oc-first}.

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have {rh-rhacm} with `MultiClusterHub` enabled.

* You have enabled the assisted service.

.Procedure

. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command:
+
[source,terminal]
----
$ oc edit AgentServiceConfig
----

. Update the `spec.osImages` field in the `AgentServiceConfig` CR:
+
[source,yaml,subs="attributes+"]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
 name: agent
spec:
# ...
  osImages:
    - cpuArchitecture: x86_64
      openshiftVersion: ""
      rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
      url: https://<host>/<path>/rhcos-live.x86_64.iso
----
+
where:
+
--
`<host>` :: Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server.
`<path>` :: Specifies the path to the image on the target mirror registry.
--

. Save and quit the editor to apply the changes.

[role="_additional-resources"]
.Additional resources

* Enabling the assisted service

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

[id="ztp-roll-out-the-configuration-changes_{context}"]
= Rolling out the {ztp} configuration changes

If any configuration changes were included in the upgrade due to implementing recommended changes, the upgrade process results in a set of policy CRs on the hub cluster in the `Non-Compliant` state. With the {ztp-first} version 4.10 and later `ztp-site-generate` container, these policies are set to `inform` mode and are not pushed to the managed clusters without an additional step by the user. This ensures that potentially disruptive changes to the clusters can be managed in terms of when the changes are made, for example, during a maintenance window, and how many clusters are updated concurrently.

To roll out the changes, create one or more `ClusterGroupUpgrade` CRs as detailed in the {cgu-operator} documentation. The CR must contain the list of `Non-Compliant` policies that you want to push out to the managed clusters as well as a list or selector of which clusters should be included in the update.

[role="_additional-resources"]
.Additional resources

* For information about the {cgu-operator-first}, see About the {cgu-operator-full} configuration.

* For information about creating `ClusterGroupUpgrade` CRs, see About the auto-created ClusterGroupUpgrade CR for {ztp}.
