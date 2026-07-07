---
title: "Using hub templates in PolicyGenerator or PolicyGenTemplate CRs"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-using-hub-cluster-templates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-using-hub-cluster-templates
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Using hub templates in PolicyGenerator or PolicyGenTemplate CRs

[id="ztp-using-hub-cluster-templates-pgt"]
= Using hub templates in PolicyGenerator or PolicyGenTemplate CRs

{cgu-operator-full} supports {rh-rhacm-first} hub cluster template functions in configuration policies used with {ztp-first}.

Hub-side cluster templates allow you to define configuration policies that can be dynamically customized to the target clusters.
This reduces the need to create separate policies for many clusters with similar configurations but with different values.

[IMPORTANT]
====
Policy templates are restricted to the same namespace as the namespace where the policy is defined.
This means you must create the objects referenced in the hub template in the same namespace where the policy is created.
====

[role="_additional-resources"]
.Additional resources

* Configuring managed cluster policies by using PolicyGenerator resources

* Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

* {rh-rhacm} support for template processing in configuration policies

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.adoc

[id="ztp-specifying-nics-in-pgt-crs-with-hub-cluster-templates_{context}"]
= Specifying group and site configurations in group PolicyGenerator or PolicyGentemplate CRs

You can manage the configuration of fleets of clusters with `ConfigMap` CRs by using hub templates to populate the group and site values in the generated policies that get applied to the managed clusters.
Using hub templates in site `PolicyGenerator` or `PolicyGentemplate` CRs means that you do not need to create a policy CR for each site.

You can group the clusters in a fleet in various categories, depending on the use case, for example hardware type or region.
Each cluster should have a label corresponding to the group or groups that the cluster is in.
If you manage the configuration values for each group in different `ConfigMap` CRs, then you require only one group policy CR to apply the changes to all the clusters in the group by using hub templates.

The following example shows you how to use three `ConfigMap` CRs and one `PolicyGenerator` CR to apply both site and group configuration to clusters grouped by hardware type and region.

[NOTE]
====
There is a 1 MiB size limit (Kubernetes documentation) for `ConfigMap` CRs.
The effective size for the `ConfigMap` CRs is further limited by the `last-applied-configuration` annotation.
To avoid the `last-applied-configuration` limitation, add the following annotation to the template `ConfigMap`:

[source,yaml]
----
argocd.argoproj.io/sync-options: Replace=true
----
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have created a Git repository where you manage your custom site configuration data.
The repository must be accessible from the hub cluster and be defined as a source repository for the {ztp} ArgoCD application.

.Procedure

. Create three `ConfigMap` CRs that contain the group and site configuration:
+
--
.. Create  a `ConfigMap` CR named `group-hardware-types-configmap` to hold the hardware-specific configuration. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: group-hardware-types-configmap
  namespace: ztp-group
  annotations:
    argocd.argoproj.io/sync-options: Replace=true <1>
data:
  # SriovNetworkNodePolicy.yaml
  hardware-type-1-sriov-node-policy-pfNames-1: "[\"ens5f0\"]"
  hardware-type-1-sriov-node-policy-pfNames-2: "[\"ens7f0\"]"
  # PerformanceProfile.yaml
  hardware-type-1-cpu-isolated: "2-31,34-63"
  hardware-type-1-cpu-reserved: "0-1,32-33"
  hardware-type-1-hugepages-default: "1G"
  hardware-type-1-hugepages-size: "1G"
  hardware-type-1-hugepages-count: "32"
----
<1> The `argocd.argoproj.io/sync-options` annotation is required only if the `ConfigMap` is larger than 1 MiB in size.

.. Create  a `ConfigMap` CR named `group-zones-configmap` to hold the regional configuration. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: group-zones-configmap
  namespace: ztp-group
data:
  # ClusterLogForwarder.yaml
  zone-1-cluster-log-fwd-outputs: "[{\"type\":\"kafka\", \"name\":\"kafka-open\", \"url\":\"tcp://10.46.55.190:9092/test\"}]"
  zone-1-cluster-log-fwd-pipelines: "[{\"inputRefs\":[\"audit\", \"infrastructure\"], \"labels\": {\"label1\": \"test1\", \"label2\": \"test2\", \"label3\": \"test3\", \"label4\": \"test4\"}, \"name\": \"all-to-default\", \"outputRefs\": [\"kafka-open\"]}]"
----

.. Create a `ConfigMap` CR named `site-data-configmap` to hold the site-specific configuration. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: site-data-configmap
  namespace: ztp-group
data:
  # SriovNetwork.yaml
  du-sno-1-zone-1-sriov-network-vlan-1: "140"
  du-sno-1-zone-1-sriov-network-vlan-2: "150"
----
--
+
[NOTE]
====
Each `ConfigMap` CR must be in the same namespace as the policy to be generated from the group `PolicyGenerator` CR.
====

. Commit the `ConfigMap` CRs in Git, and then push to the Git repository being monitored by the Argo CD application.

. Apply the hardware type and region labels to the clusters.
The following command applies to a single cluster named `du-sno-1-zone-1` and the labels chosen are `"hardware-type": "hardware-type-1"` and `"group-du-sno-zone": "zone-1"`:
+
[source,terminal]
----
$ oc patch managedclusters.cluster.open-cluster-management.io/du-sno-1-zone-1 --type merge -p '{"metadata":{"labels":{"hardware-type": "hardware-type-1", "group-du-sno-zone": "zone-1"}}}'
----

. Depending on your requirements, Create a group `PolicyGenerator` or `PolicyGentemplate` CR that uses hub templates to obtain the required data from the `ConfigMap` objects:
+
--
.. Create a group `PolicyGenerator` CR.
This example `PolicyGenerator` CR configures logging, VLAN IDs, NICs and Performance Profile for the clusters that match the labels listed the under `policyDefaults.placement` field:
+
[source,yaml]
----
----

.. Create a group `PolicyGenTemplate` CR.
This example `PolicyGenTemplate` CR configures logging, VLAN IDs, NICs and Performance Profile for the clusters that match the labels listed under `spec.bindingRules`:
+
[source,yaml]
----
----
--

+
[NOTE]
====
To retrieve site-specific configuration values, use the `.ManagedClusterName` field.
This is a template context value set to the name of the target managed cluster.

To retrieve group-specific configuration, use the `.ManagedClusterLabels` field.
This is a template context value set to the value of the managed cluster's labels.
====

. Commit the site `PolicyGenerator` or `PolicyGentemplate` CR in Git and push to the Git repository that is monitored by the ArgoCD application.
+
[NOTE]
====
Subsequent changes to the referenced `ConfigMap` CR are not automatically synced to the applied policies.
You need to manually sync the new `ConfigMap` changes to update existing `PolicyGenerator` CRs. See "Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGenTemplate CRs".

You can use the same `PolicyGenerator` or `PolicyGentemplate` CR for multiple clusters.
If there is a configuration change, then the only modifications you need to make are to the `ConfigMap` objects that hold the configuration for each cluster and the labels of the managed clusters.
====

// Module included in the following assemblies:
//
// * edge_computing/ztp-using-hub-cluster-templates.adoc

[id="ztp-syncing-new-configmap-changes-to-existing-pgt-crs_{context}"]
= Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGentemplate CRs

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have created a `PolicyGenerator` or `PolicyGentemplate` CR that pulls information from a `ConfigMap` CR using hub cluster templates.

.Procedure

. Update the contents of your `ConfigMap` CR, and apply the changes in the hub cluster.

. To sync the contents of the updated `ConfigMap` CR to the deployed policy, do either of the following:

.. Option 1: Delete the existing policy. ArgoCD uses the `PolicyGenerator` or `PolicyGentemplate` CR to immediately recreate the deleted policy. For example, run the following command:
+
[source,terminal]
----
$ oc delete policy <policy_name> -n <policy_namespace>
----

.. Option 2: Apply a special annotation `policy.open-cluster-management.io/trigger-update` to the policy with a different value every time when you update the `ConfigMap`. For example:
+
[source,terminal]
----
$ oc annotate policy <policy_name> -n <policy_namespace> policy.open-cluster-management.io/trigger-update="1"
----
+
[NOTE]
====
You must apply the updated policy for the changes to take effect. For more information, see Special annotation for reprocessing.
====

. Optional: If it exists, delete the `ClusterGroupUpdate` CR that contains the policy. For example:
+
[source,terminal]
----
$ oc delete clustergroupupgrade <cgu_name> -n <cgu_namespace>
----

.. Create a new `ClusterGroupUpdate` CR that includes the policy to apply with the updated `ConfigMap` changes. For example, add the following YAML to the file `cgr-example.yaml`:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgr_name>
  namespace: <policy_namespace>
spec:
  managedPolicies:
    - <managed_policy>
  enable: true
  clusters:
  - <managed_cluster_1>
  - <managed_cluster_2>
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
----

.. Apply the updated policy:
+
[source,terminal]
----
$ oc apply -f cgr-example.yaml
----
