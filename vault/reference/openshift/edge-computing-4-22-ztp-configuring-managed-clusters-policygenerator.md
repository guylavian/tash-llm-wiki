---
title: "Configuring managed cluster policies by using PolicyGenerator resources"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-configuring-managed-clusters-policygenerator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-configuring-managed-clusters-policygenerator
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Configuring managed cluster policies by using PolicyGenerator resources

[id="ztp-configuring-managed-clusters-policygenerator"]
= Configuring managed cluster policies by using PolicyGenerator resources

[role="_abstract"]
You can customize how {rh-rhacm-first} uses `{policy-gen-cr}` CRs to generate `Policy` CRs that configure the managed clusters that you provision.

Using {rh-rhacm} and `{policy-gen-cr}` CRs is the recommended approach for managing policies and deploying them to managed clusters.
This replaces the use of `PolicyGenTemplate` CRs for this purpose.
For more information about `{policy-gen-cr}` resources, see the {rh-rhacm} Policy Generator documentation.

// Module included in the following assemblies:
//
// * edge_computing/ztp-configuring-managed-clusters-policygenerator.adoc

[id="ztp-comparing-pgt-and-rhacm-pg-patching-strategies_{context}"]
= Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

`PolicyGenerator` custom resources (CRs) and `PolicyGenTemplate` CRs can be used in {ztp} to generate {rh-rhacm} policies for managed clusters.

There are advantages to using `PolicyGenerator` CRs over `PolicyGenTemplate` CRs when it comes to patching OpenShift Container Platform resources with {ztp}.
Using the {rh-rhacm} `PolicyGenerator` API provides a generic way of patching resources which is not possible with `PolicyGenTemplate` resources.

The `PolicyGenerator` API is a part of the Open Cluster Management standard, while the `PolicyGenTemplate` API is not.
A comparison of `PolicyGenerator` and `PolicyGenTemplate` resource patching and placement strategies are described in the following table.

.Comparison of {rh-rhacm} PolicyGenerator and PolicyGenTemplate patching
[cols="1,2", width="90%", options="header"]
|====
|PolicyGenerator patching
|PolicyGenTemplate patching

|Uses Kustomize strategic merges for merging resources.
For more information see Declarative Management of Kubernetes Objects Using Kustomize.
|Works by replacing variables with their values as defined by the patch.
This is less flexible than Kustomize merge strategies.

|Supports `ManagedClusterSet` and `Binding` resources.
|Does not support `ManagedClusterSet` and `Binding` resources.

|Relies only on patching, no embedded variable substitution is required.
|Overwrites variable values defined in the patch.

|Does not support merging lists in merge patches.
Replacing a list in a merge patch is supported.
|Merging and replacing lists is supported in a limited fashion - you can only merge one object in the list.

|Does not currently support the OpenAPI specification for resource patching.
This means that additional directives are required in the patch to merge content that does not follow a schema, for example, `PtpConfig` resources.
|Works by replacing fields and values with values as defined by the patch.

|Requires additional directives, for example, `$patch: replace` in the patch to merge content that does not follow a schema.
|Substitutes fields and values defined in the source CR with values defined in the patch, for example `$name`.

|Can patch the `Name` and `Namespace` fields defined in the reference source CR, but only if the CR file has a single object.
|Can patch the `Name` and `Namespace` fields defined in the reference source CR.
|====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-the-policygentemplate_{context}"]
= About the {policy-gen-cr} CRD

The `{policy-gen-cr}` custom resource definition (CRD) tells the `PolicyGen` policy generator what custom resources (CRs) to include in the cluster configuration, how to combine the CRs into the generated policies, and what items in those CRs need to be updated with overlay content.

The following example shows a `{policy-gen-cr}` CR (`{policy-prefix}common-du-ranGen.yaml`) extracted from the `ztp-site-generate` reference container. The `{policy-prefix}common-du-ranGen.yaml` file defines two {rh-rhacm-first} policies. The policies manage a collection of configuration CRs, one for each unique value of `policyName` in the CR. `{policy-prefix}common-du-ranGen.yaml` creates a single placement binding and a placement rule to bind the policies to clusters based on the labels listed in the `{binding-field}` section.

.Example {policy-gen-cr} CR - {policy-prefix}common-ranGen.yaml

A `{policy-gen-cr}` CR can be constructed with any number of included CRs. Apply the following example CR in the hub cluster to generate a policy containing a single CR:

[source,yaml]
----
----

Using the source file `PtpConfigSlave.yaml` as an example, the file defines a `PtpConfig` CR. The generated policy for the `PtpConfigSlave` example is named `group-du-sno-config-policy`. The `PtpConfig` CR defined in the generated `group-du-sno-config-policy` is named `du-ptp-slave`. The `spec` defined in `PtpConfigSlave.yaml` is placed under `du-ptp-slave` along with the other `spec` items defined under the source file.

The following example shows the `group-du-sno-config-policy` CR:

[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-pgt-config-best-practices_{context}"]
= Recommendations when customizing {policy-gen-cr} CRs

Consider the following best practices when customizing site configuration `{policy-gen-cr}` custom resources (CRs):

* Use as few policies as are necessary. Using fewer policies requires less resources. Each additional policy creates increased CPU load for the hub cluster and the deployed managed cluster. CRs are combined into policies based on the `policyName` field in the `{policy-gen-cr}` CR. CRs in the same `{policy-gen-cr}` which have the same value for `policyName` are managed under a single policy.

* In disconnected environments, use a single catalog source for all Operators by configuring the registry as a single index containing all Operators. Each additional `CatalogSource` CR on the managed clusters increases CPU usage.

* Reduce the overall time taken until the cluster is ready to deploy applications by including `MachineConfig` CRs as extra manifests in the installation. To do this, package `MachineConfig` CRs in a `ConfigMap` CR. Reference the `ConfigMap` CRs in the `extraManifestsRefs` field in the `ClusterInstance` CR.

* `{policy-gen-cr}` CRs should override the channel field to explicitly identify the desired version. This ensures that changes in the source CR during upgrades does not update the generated subscription.

* The default setting for `policyDefaults.consolidateManifests` is `true`. This is the recommended setting for DU profile. Setting it to `false` might impact large scale deployments.

* The default setting for `policyDefaults.orderPolicies` is `false`. This is the recommended setting for DU profile.
After the cluster installation is complete and a cluster becomes `Ready`, {cgu-operator} creates a `ClusterGroupUpgrade` CR corresponding to this cluster.
The `ClusterGroupUpgrade` CR contains a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave` annotation.
If you use the `{policy-gen-cr}` CR to change the order of the policies, conflicts might occur and the configuration might not be applied.

[role="_additional-resources"]
.Additional resources

* For recommendations about scaling clusters with {rh-rhacm}, see Performance and scalability.

[NOTE]
====
When managing large numbers of spoke clusters on the hub cluster, minimize the number of policies to reduce resource consumption.

Grouping multiple configuration CRs into a single or limited number of policies is one way to reduce the overall number of policies on the hub cluster. When using the common, group, and site hierarchy of policies for managing site configuration, it is especially important to combine site-specific configuration into a single policy.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-policygentemplates-for-ran_{context}"]
= {policy-gen-cr} CRs for RAN deployments

Use `{policy-gen-cr}` custom resources (CRs) to customize the configuration applied to the cluster by using the {ztp-first} pipeline. The `{policy-gen-cr}` CR allows you to generate one or more policies to manage the set of configuration CRs on your fleet of clusters. The `{policy-gen-cr}` CR identifies the set of managed CRs, bundles them into policies, builds the policy wrapping around those CRs, and associates the policies with clusters by using label binding rules.

The reference configuration, obtained from the {ztp} container, is designed to provide a set of critical features and node tuning settings that ensure the cluster can support the stringent performance and resource utilization constraints typical of RAN (Radio Access Network) Distributed Unit (DU) applications. Changes or omissions from the baseline configuration can affect feature availability, performance, and resource utilization. Use the reference `{policy-gen-cr}` CRs as the basis to create a hierarchy of configuration files tailored to your specific site requirements.

The baseline `{policy-gen-cr}` CRs that are defined for RAN DU cluster configuration can be extracted from the {ztp} `ztp-site-generate` container. See "Preparing the {ztp} site configuration repository" for further details.

The `{policy-gen-cr}` CRs can be found in the `./{argocd-folder}` folder. The reference architecture has common, group, and site-specific configuration CRs. Each `{policy-gen-cr}` CR refers to other CRs that can be found in the `./out/source-crs` folder.

The `{policy-gen-cr}` CRs relevant to RAN cluster configuration are described below. Variants are provided for the group `{policy-gen-cr}` CRs to account for differences in single-node, three-node compact, and standard cluster configurations. Similarly, site-specific configuration variants are provided for single-node clusters and multi-node (compact or standard) clusters. Use the group and site-specific configuration variants that are relevant for your deployment.

.{policy-gen-cr} CRs for RAN deployments
[cols=2*, options="header"]
|====
|{policy-gen-cr} CR
|Description

|`{policy-prefix}example-multinode-site.yaml`
|Contains a set of CRs that get applied to multi-node clusters. These CRs configure SR-IOV features typical for RAN installations.

|`{policy-prefix}example-sno-site.yaml`
|Contains a set of CRs that get applied to {sno} clusters. These CRs configure SR-IOV features typical for RAN installations.

|`{policy-prefix}common-mno-ranGen.yaml`
|Contains a set of common RAN policy configuration that get applied to multi-node clusters.

|`{policy-prefix}common-ranGen.yaml`
|Contains a set of common RAN CRs that get applied to all clusters. These CRs subscribe to a set of operators providing cluster features typical for RAN as well as baseline cluster tuning.

|`{policy-prefix}group-du-3node-ranGen.yaml`
|Contains the RAN policies for three-node clusters only.

|`{policy-prefix}group-du-sno-ranGen.yaml`
|Contains the RAN policies for single-node clusters only.

|`{policy-prefix}group-du-standard-ranGen.yaml`
|Contains the RAN policies for standard three control-plane clusters.

|`{policy-prefix}group-du-3node-validator-ranGen.yaml`
|`{policy-gen-cr}` CR used to generate the various policies required for three-node clusters.

|`{policy-prefix}group-du-standard-validator-ranGen.yaml`
|`{policy-gen-cr}` CR used to generate the various policies required for standard clusters.

|`{policy-prefix}group-du-sno-validator-ranGen.yaml`
|`{policy-gen-cr}` CR used to generate the various policies required for {sno} clusters.
|====

[role="_additional-resources"]
.Additional resources

* Preparing the {ztp} site configuration repository

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-customizing-a-managed-site-using-pgt_{context}"]
= Customizing a managed cluster with {policy-gen-cr} CRs

Use the following procedure to customize the policies that get applied to the managed cluster that you provision using the {ztp-first} pipeline.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You configured the hub cluster for generating the required installation and policy CRs.

* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

.Procedure

. Create a `{policy-gen-cr}` CR for site-specific configuration CRs.

.. Choose the appropriate example for your CR from the `{argocd-folder}` folder, for example, `{policy-prefix}example-sno-site.yaml` or `{policy-prefix}example-multinode-site.yaml`.

.. Change the `{binding-field}` field in the example file to match the site-specific label included in the `ClusterInstance` CR. In the example `ClusterInstance` file, the site-specific label is `sites: example-sno`.
+
[NOTE]
====
Ensure that the labels defined in your `{policy-gen-cr}` `{binding-field}` field correspond to the labels that are defined in the related managed clusters `ClusterInstance` CR.
====

.. Change the content in the example file to match the desired configuration.

. Optional: Create a `{policy-gen-cr}` CR for any common configuration CRs that apply to the entire fleet of clusters.

.. Select the appropriate example for your CR from the `{argocd-folder}` folder, for example, `{policy-prefix}common-ranGen.yaml`.

.. Change the content in the example file to match the required configuration.

. Optional: Create a `{policy-gen-cr}` CR for any group configuration CRs that apply to the certain groups of clusters in the fleet.
+
Ensure that the content of the overlaid spec files matches your required end state. As a reference, the `out/source-crs` directory contains the full list of source-crs available to be included and overlaid by your {policy-gen-cr} templates.
+
[NOTE]
====
Depending on the specific requirements of your clusters, you might need more than a single group policy per cluster type, especially considering that the example group policies each have a single `PerformancePolicy.yaml` file that can only be shared across a set of clusters if those clusters consist of identical hardware configurations.
====

.. Select the appropriate example for your CR from the `{argocd-folder}` folder, for example, `{policy-prefix}group-du-sno-ranGen.yaml`.

.. Change the content in the example file to match the required configuration.

. Optional. Create a validator inform policy `{policy-gen-cr}` CR to signal when the {ztp} installation and configuration of the deployed cluster is complete. For more information, see "Creating a validator inform policy".

. Define all the policy namespaces in a YAML file similar to the example `{argocd-folder}/ns.yaml` file.
+
[IMPORTANT]
====
Do not include the `Namespace` CR in the same file with the `{policy-gen-cr}` CR.
====

. Add the `{policy-gen-cr}` CRs and `Namespace` CR to the `kustomization.yaml` file in the generators section, similar to the example shown in `{argocd-folder}kustomization.yaml`.

. Commit the `{policy-gen-cr}` CRs, `Namespace` CR, and associated `kustomization.yaml` file in your Git repository and push the changes.
+
The ArgoCD pipeline detects the changes and begins the managed cluster deployment. You can push the changes to the `ClusterInstance` CR and the `{policy-gen-cr}` CR simultaneously.

[role="_additional-resources"]
.Additional resources

* Signalling {ztp} cluster deployment completion with validator inform policies

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-monitoring-policy-deployment-progress_{context}"]
= Monitoring managed cluster policy deployment progress

The ArgoCD pipeline uses `{policy-gen-cr}` CRs in Git to generate the {rh-rhacm} policies and then sync them to the hub cluster. You can monitor the progress of the managed cluster policy synchronization after the assisted service installs OpenShift Container Platform on the managed cluster.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. The {cgu-operator-first} applies the configuration policies that are bound to the cluster.
+
After the cluster installation is complete and the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR corresponding to this cluster, with a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave annotations`, is automatically created by the {cgu-operator}. The cluster's policies are applied in the order listed in `ClusterGroupUpgrade` CR.
+
You can monitor the high-level progress of configuration policy reconciliation by using the following commands:
+
[source,terminal]
----
$ export CLUSTER=<clusterName>
----
+
[source,terminal]
----
$ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[-1:]}' | jq
----
+
.Example output
[source,terminal]
----
{
  "lastTransitionTime": "2022-11-09T07:28:09Z",
  "message": "Remediating non-compliant policies",
  "reason": "InProgress",
  "status": "True",
  "type": "Progressing"
}
----

. You can monitor the detailed cluster policy compliance status by using the {rh-rhacm} dashboard or the command line.

.. To check policy compliance by using `oc`, run the following command:
+
[source,terminal]
----
$ oc get policies -n $CLUSTER
----
+
.Example output
[source,terminal]
----
NAME                                                     REMEDIATION ACTION   COMPLIANCE STATE   AGE
ztp-common.common-config-policy                          inform               Compliant          3h42m
ztp-common.common-subscriptions-policy                   inform               NonCompliant       3h42m
ztp-group.group-du-sno-config-policy                     inform               NonCompliant       3h42m
ztp-group.group-du-sno-validator-du-policy               inform               NonCompliant       3h42m
ztp-install.example1-common-config-policy-pjz9s          enforce              Compliant          167m
ztp-install.example1-common-subscriptions-policy-zzd9k   enforce              NonCompliant       164m
ztp-site.example1-config-policy                          inform               NonCompliant       3h42m
ztp-site.example1-perf-policy                            inform               NonCompliant       3h42m
----

.. To check policy status from the {rh-rhacm} web console, perform the following actions:

... Click *Governance* -> *Find policies*.
... Click on a cluster policy to check its status.

When all of the cluster policies become compliant, {ztp} installation and configuration for the cluster is complete. The `ztp-done` label is added to the cluster.

In the reference configuration, the final policy that becomes compliant is the one defined in the `*-du-validator-policy` policy. This policy, when compliant on a cluster, ensures that all cluster configuration, Operator installation, and Operator configuration is complete.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-coordinating-reboots-for-config-changes_{context}"]
= Coordinating reboots for configuration changes

You can use {cgu-operator-full} (TALM) to coordinate reboots across a fleet of spoke clusters when configuration changes require a reboot, such as deferred tuning changes. {cgu-operator} reboots all nodes in the targeted `MachineConfigPool` on the selected clusters when the reboot policy is applied.

Instead of rebooting nodes after each individual change, you can apply all configuration updates through policies and then trigger a single, coordinated reboot.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have deployed and configured {cgu-operator}.

.Procedure

. Generate the configuration policies by creating a `PolicyGenerator` custom resource (CR). You can use one of the following sample manifests:

* `out/argocd/example/acmpolicygenerator/acm-example-sno-reboot`
* `out/argocd/example/acmpolicygenerator/acm-example-multinode-reboot`

. Update the `policyDefaults.placement.labelSelector` field in the `PolicyGenerator` CR to target the clusters that you want to reboot. Modify other fields as necessary for your use case.
+
If you are coordinating a reboot to apply a deferred tuning change, ensure the `MachineConfigPool` in the reboot policy matches the value specified in the `spec.recommend` field in the `Tuned` object.

. Apply the `PolicyGenerator` CR to generate and apply the configuration policies. For detailed steps, see "Customizing a managed cluster with PolicyGenerator CRs".

. After ArgoCD completes syncing the policies, create and apply the `ClusterGroupUpgrade` (CGU) CR.
+
.Example CGU custom resource configuration
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: reboot
  namespace: default
spec:
  clusterLabelSelectors:
  - matchLabels: <1>
# ...
  enable: true
  managedPolicies: <2>
  - example-reboot
  remediationStrategy:
    timeout: 300 <3>
    maxConcurrency: 10
# ...
----
<1> Configure the labels that match the clusters you want to reboot.
<2> Add all required configuration policies before the reboot policy. {cgu-operator} applies the configuration changes as specified in the policies, in the order they are listed.
<3> Specify the timeout in seconds for the entire upgrade across all selected clusters. Set this field by considering the worst-case scenario.

. After you apply the CGU custom resource, {cgu-operator} rolls out the configuration policies in order. Once all policies are compliant, it applies the reboot policy and triggers a reboot of all nodes in the specified `MachineConfigPool`.

.Verification

. Monitor the CGU rollout status.
+
You can monitor the rollout of the CGU custom resource on the hub by checking the status. Verify the successful rollout of the reboot by running the following command:
+
[source,terminal]
----
oc get cgu -A
----
+
.Example output
[source,terminal]
----
NAMESPACE   NAME     AGE   STATE       DETAILS
default     reboot   1d    Completed   All clusters are compliant with all the managed policies
----

. Verify successful reboot on a specific node.
+
To confirm that the reboot was successful on a specific node, check the status of the `MachineConfigPool` (MCP) for the node by running the following command:
+
[source,terminal]
----
oc get mcp master

----
+
.Example output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-be5785c3b98eb7a1ec902fef2b81e865   True      False      False      3              3                   3                     0                      72d
----

[role="_additional-resources"]
.Additional resources

* Customizing a managed cluster with PolicyGenerator CRs

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-validating-the-generation-of-configuration-policy-crs_{context}"]
= Validating the generation of configuration policy CRs

`Policy` custom resources (CRs) are generated in the same namespace as the `{policy-gen-cr}` from which they are created. The same troubleshooting flow applies to all policy CRs generated from a `{policy-gen-cr}` regardless of whether they are `ztp-common`, `ztp-group`, or `ztp-site` based, as shown using the following commands:

[source,terminal]
----
$ export NS=<namespace>
----

[source,terminal]
----
$ oc get policy -n $NS
----

The expected set of policy-wrapped CRs should be displayed.

If the policies failed synchronization, use the following troubleshooting steps.

.Procedure

. To display detailed information about the policies, run the following command:
+
[source,terminal]
----
$ oc describe -n openshift-gitops application policies
----

. Check for `Status: Conditions:` to show the error logs. For example, setting an invalid `sourceFile` entry to `fileName:` generates the error shown below:
+
[source,text]
----
Status:
  Conditions:
    Last Transition Time:  2021-11-26T17:21:39Z
    Message:               rpc error: code = Unknown desc = `kustomize build /tmp/https___git.com/ran-sites/policies/ --enable-alpha-plugins` failed exit status 1: 2021/11/26 17:21:40 Error could not find test.yaml under source-crs/: no such file or directory Error: failure in plugin configured via /tmp/kust-plugin-config-52463179; exit status 1: exit status 1
    Type:  ComparisonError
----

. Check for `Status: Sync:`. If there are log errors at `Status: Conditions:`, the `Status: Sync:` shows `Unknown` or `Error`:
+
[source,text]
----
Status:
  Sync:
    Compared To:
      Destination:
        Namespace:  policies-sub
        Server:     https://kubernetes.default.svc
      Source:
        Path:             policies
        Repo URL:         https://git.com/ran-sites/policies/.git
        Target Revision:  master
    Status:               Error
----

. When {rh-rhacm-first} recognizes that policies apply to a `ManagedCluster` object, the policy CR objects are applied to the cluster namespace. Check to see if the policies were copied to the cluster namespace:
+
[source,terminal]
----
$ oc get policy -n $CLUSTER
----
+
.Example output
+
[source,terminal]
----
NAME                                         REMEDIATION ACTION   COMPLIANCE STATE   AGE
ztp-common.common-config-policy              inform               Compliant          13d
ztp-common.common-subscriptions-policy       inform               Compliant          13d
ztp-group.group-du-sno-config-policy         inform               Compliant          13d
ztp-group.group-du-sno-validator-du-policy   inform               Compliant          13d
ztp-site.example-sno-config-policy           inform               Compliant          13d
----
+
{rh-rhacm} copies all applicable policies into the cluster namespace. The copied policy names have the format: `<{policy-gen-cr}.Namespace>.<{policy-gen-cr}.Name>-<policyName>`.

. Check the placement rule for any policies not copied to the cluster namespace. The `matchSelector` in the `{placement-rule-cr}` for those policies should match labels on the `ManagedCluster` object:
+
[source,terminal,subs="attributes+"]
----
$ oc get {placement-rule-cr} -n $NS
----

. Note the `{placement-rule-cr}` name appropriate for the missing policy, common, group, or site, using the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {placement-rule-cr} -n $NS <placement_rule_name> -o yaml
----
+
* The status-decisions should include your cluster name.
* The key-value pair of the `matchSelector` in the spec must match the labels on your managed cluster.

. Check the labels on the `ManagedCluster` object by using the following command:
+
[source,terminal]
----
$ oc get ManagedCluster $CLUSTER -o jsonpath='{.metadata.labels}' | jq
----

. Check to see what policies are compliant by using the following command:
+
[source,terminal]
----
$ oc get policy -n $CLUSTER
----
+
If the `Namespace`, `OperatorGroup`, and `Subscription` policies are compliant but the Operator configuration policies are not, it is likely that the Operators did not install on the managed cluster. This causes the Operator configuration policies to fail to apply because the CRD is not yet applied to the spoke.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-restarting-policies-reconciliation_{context}"]
= Restarting policy reconciliation

You can restart policy reconciliation when unexpected compliance issues occur, for example, when the `ClusterGroupUpgrade` custom resource (CR) has timed out.

.Procedure

. A `ClusterGroupUpgrade` CR is generated in the namespace `ztp-install` by the {cgu-operator-full} after the managed cluster becomes `Ready`:
+
[source,terminal]
----
$ export CLUSTER=<clusterName>
----
+
[source,terminal]
----
$ oc get clustergroupupgrades -n ztp-install $CLUSTER
----

. If there are unexpected issues and the policies fail to become complaint within the configured timeout (the default is 4 hours), the status of the `ClusterGroupUpgrade` CR shows `UpgradeTimedOut`:
+
[source,terminal]
----
$ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Ready")]}'
----

. A `ClusterGroupUpgrade` CR in the `UpgradeTimedOut` state automatically restarts its policy reconciliation every hour. If you have changed your policies, you can start a retry immediately by deleting the existing `ClusterGroupUpgrade` CR. This triggers the automatic creation of a new `ClusterGroupUpgrade` CR that begins reconciling the policies immediately:
+
[source,terminal]
----
$ oc delete clustergroupupgrades -n ztp-install $CLUSTER
----

Note that when the `ClusterGroupUpgrade` CR completes with status `UpgradeCompleted` and the managed cluster has the label `ztp-done` applied, you can make additional configuration changes by using `{policy-gen-cr}`. Deleting the existing `ClusterGroupUpgrade` CR will not make the {cgu-operator} generate a new CR.

At this point, {ztp} has completed its interaction with the cluster and any further interactions should be treated as an update and a new `ClusterGroupUpgrade` CR created for remediation of the policies.

[role="_additional-resources"]
.Additional resources

* For information about using {cgu-operator-first} to construct your own `ClusterGroupUpgrade` CR, see About the ClusterGroupUpgrade CR.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-removing-content-from-managed-clusters_{context}"]
= Changing applied managed cluster CRs using policies

You can remove content from a custom resource (CR) that is deployed in a managed cluster through a policy.

By default, all `Policy` CRs created from a `{policy-gen-cr}` CR have the `complianceType` field set to `musthave`.
A `musthave` policy without the removed content is still compliant because the CR on the managed cluster has all the specified content.
With this configuration, when you remove content from a CR, {cgu-operator} removes the content from the policy but the content is not removed from the CR on the managed cluster.

With the `complianceType` field to `mustonlyhave`, the policy ensures that the CR on the cluster is an exact match of what is specified in the policy.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have deployed a managed cluster from a hub cluster running {rh-rhacm}.

* You have installed {cgu-operator-full} on the hub cluster.

.Procedure

. Remove the content that you no longer need from the affected CRs. In this example, the `disableDrain: false` line was removed from the `SriovOperatorConfig` CR.
+
.Example CR

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  configDaemonNodeSelector:
    "node-role.kubernetes.io/$mcp": ""
  disableDrain: true
  enableInjector: true
  enableOperatorWebhook: true
----

. Change the `complianceType` of the affected policies to `mustonlyhave` in the `{policy-prefix}group-du-sno-ranGen.yaml` file.
+
.Example YAML
[source,yaml]
----
- fileName: SriovOperatorConfig.yaml
  policyName: "config-policy"
  complianceType: mustonlyhave
# ...
policyDefaults:
  complianceType: "mustonlyhave"
# ...
policies:
  - name: config-policy
    policyAnnotations:
      ran.openshift.io/ztp-deploy-wave: ""
    manifests:
      - path: source-crs/SriovOperatorConfig.yaml
----

. Create a `ClusterGroupUpdates` CR and specify the clusters that must receive the CR changes::
+
.Example ClusterGroupUpdates CR
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-remove
  namespace: default
spec:
  managedPolicies:
    - ztp-group.group-du-sno-config-policy
  enable: false
  clusters:
  - spoke1
  - spoke2
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
  batchTimeoutAction:
----

. Create the `ClusterGroupUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc create -f cgu-remove.yaml
----

. When you are ready to apply the changes, for example, during an appropriate maintenance window, change the value of the `spec.enable` field to `true` by running the following command:
+
[source,terminal]
----
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-remove \
--patch '{"spec":{"enable":true}}' --type=merge
----

.Verification

. Check the status of the policies by running the following command:
+
[source,terminal]
----
$ oc get <kind> <changed_cr_name>
----

+
.Example output
[source,terminal]
----
NAMESPACE   NAME                                                   REMEDIATION ACTION   COMPLIANCE STATE   AGE
default     cgu-ztp-group.group-du-sno-config-policy               enforce                                 17m
default     ztp-group.group-du-sno-config-policy                   inform               NonCompliant       15h
----

+
When the `COMPLIANCE STATE` of the policy is `Compliant`, it means that the CR is updated and the unwanted content is removed.

. Check that the policies are removed from the targeted clusters by running the following command on the managed clusters:
+
[source,terminal]
----
$ oc get <kind> <changed_cr_name>
----

+
If there are no results, the CR is removed from the managed cluster.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-definition-of-done-for-ztp-installations_{context}"]
= Indication of done for {ztp} installations

{ztp-first} simplifies the process of checking the {ztp} installation status for a cluster. The {ztp} status moves through three phases: cluster installation, cluster configuration, and {ztp} done.

Cluster installation phase::
The cluster installation phase is shown by the `ManagedClusterJoined` and  `ManagedClusterAvailable` conditions in the `ManagedCluster` CR . If the `ManagedCluster` CR does not have these conditions, or the condition is set to `False`, the cluster is still in the installation phase. Additional details about installation are available from the `AgentClusterInstall` and `ClusterDeployment` CRs. For more information, see "Troubleshooting {ztp}".

Cluster configuration phase::
The cluster configuration phase is shown by a `ztp-running` label applied the `ManagedCluster` CR for the cluster.

{ztp} done::
Cluster installation and configuration is complete in the {ztp} done phase. This is shown by the removal of the `ztp-running` label and addition of the `ztp-done` label to the `ManagedCluster` CR. The `ztp-done` label shows that the configuration has been applied and the baseline DU configuration has completed cluster tuning.
+
The change to the {ztp} done state is conditional on the compliant state of a {rh-rhacm-first} validator inform policy. This policy captures the existing criteria for a completed installation and validates that it moves to a compliant state only when {ztp} provisioning of the managed cluster is complete.
+
The validator inform policy ensures the configuration of the cluster is fully applied and Operators have completed their initialization. The policy validates the following:
+
* The target `MachineConfigPool` contains the expected entries and has finished updating. All nodes are available and not degraded.

* The SR-IOV Operator has completed initialization as indicated by at least one `SriovNetworkNodeState` with `syncStatus: Succeeded`.

* The PTP Operator daemon set exists.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-configuring-managed-clusters-policies.adoc

[id="ztp-configuring-open-api-schema-for-patching_{context}"]
= Configuring an OpenAPI schema for patching list fields by using the PolicyGenerator CR

[role="_abstract"]
You can configure an OpenAPI schema in the `PolicyGenerator` custom resource (CR) to control how list fields are merged when patching non-core Kubernetes objects.

By default, patching list fields can replace entire lists when the resource does not define merge behavior. An OpenAPI schema defines how list items are uniquely identified and merged during policy generation.

.Prerequisites

* You have created a `PolicyGenerator` CR.
* You have access to a running cluster if you need to generate a schema.

.Procedure

. Obtain an OpenAPI schema for the resources that you want to patch:

.. If an OpenAPI schema is available for the custom resource that you want to patch, use that schema file.
.. If a schema is not available, generate it from an active cluster by running the following command:
+
[source,bash]
----
kustomize openapi fetch
----

. Edit the generated schema file to keep only the resource definitions that you need to patch.
+
Removing unrelated definitions simplifies the schema and reduces maintenance effort.

. Define merge behavior for list fields that you want to patch. For each list of objects that you want to patch, add fields that specify how list items are uniquely identified and merged. For example:
+
[source,yaml]
----
"x-kubernetes-patch-merge-key": "name"
"x-kubernetes-patch-strategy": "merge"
----
+
* `x-kubernetes-patch-merge-key` specifies the field that uniquely identifies an object in the list.
  For example, setting this field to `name` uses the `name` field to identify list items.
* `x-kubernetes-patch-strategy` specifies how the patch is applied to the identified list item. The following are the supported values:
** `merge`: Merges the fields from the patch into the existing list item.
** `replace`: Replaces the entire list item identified by the merge key with the patch content.

. Save the schema file in the directory that contains the `kustomization.yaml` file.

. Reference the OpenAPI schema in the `kustomization.yaml` file:
+
[source,yaml]
----
openapi:
  path: schema.json
----

. Configure the OpenAPI schema path in the `PolicyGenerator` CR:
+
.Example `PolicyGenerator` CR for patching list fields by using an OpenAPI schema
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: PolicyGenerator
metadata:
  name: policy-generator-example
policies:
  - name: myapp
    manifests:
      - path: input-kustomize/
        patches: []
        openapi:
          path: schema.json
----

. Generate or apply the policies by using the policy generator.
+
The policy generator passes the OpenAPI schema to Kustomize to control how list fields are patched.
