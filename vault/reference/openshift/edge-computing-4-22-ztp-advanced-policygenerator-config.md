---
title: "Advanced managed cluster configuration with PolicyGenerator resources"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-advanced-policygenerator-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-advanced-policygenerator-config
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Advanced managed cluster configuration with PolicyGenerator resources

[id="ztp-advanced-policygenerator-config"]
= Advanced managed cluster configuration with PolicyGenerator resources

You can use `{policy-gen-cr}` CRs to deploy custom functionality in your managed clusters.
Using {rh-rhacm} and `{policy-gen-cr}` CRs is the recommended approach for managing policies and deploying them to managed clusters.
This replaces the use of `PolicyGenTemplate` CRs for this purpose.
For more information about `{policy-gen-cr}` resources, see the {rh-rhacm} Policy Generator documentation.

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-deploying-additional-changes-to-clusters_{context}"]
= Deploying additional changes to clusters

If you require cluster configuration changes outside of the base {ztp-first} pipeline configuration, there are three options:

Apply the additional configuration after the {ztp} pipeline is complete:: When the {ztp} pipeline deployment is complete, the deployed cluster is ready for application workloads. At this point, you can install additional Operators and apply configurations specific to your requirements. Ensure that additional configurations do not negatively affect the performance of the platform or allocated CPU budget.

Add content to the {ztp} library:: The base source custom resources (CRs) that you deploy with the {ztp} pipeline can be augmented with custom content as required.

Create extra manifests for the cluster installation:: Extra manifests are applied during installation and make the installation process more efficient.

[IMPORTANT]
====
Providing additional source CRs or modifying existing source CRs can significantly impact the performance or CPU profile of OpenShift Container Platform.
====

[role="_additional-resources"]
.Additional resources

* Customizing extra installation manifests in the {ztp} pipeline

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-update-source-crs_{context}"]
= Using {policy-gen-cr} CRs to override source CRs content

`{policy-gen-cr}` custom resources (CRs) allow you to overlay additional configuration details on top of the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container. You can think of `{policy-gen-cr}` CRs as a logical merge or patch to the base CR. Use `{policy-gen-cr}` CRs to update a single field of the base CR, or overlay the entire contents of the base CR. You can update values and insert fields that are not in the base CR.

The following example procedure describes how to update fields in the generated `PerformanceProfile` CR for the reference configuration based on the `{policy-gen-cr}` CR in the `{policy-prefix}group-du-sno-ranGen.yaml` file. Use the procedure as a basis for modifying other parts of the `{policy-gen-cr}` based on your requirements.

.Prerequisites

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.

.Procedure

. Review the baseline source CR for existing content. You can review the source CRs listed in the reference `{policy-gen-cr}` CRs by extracting them from the {ztp-first} container.

.. Create an `/out` folder:
+
[source,terminal]
----
$ mkdir -p ./out
----

.. Extract the source CRs:
+
[source,terminal,subs="attributes+"]
----
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v.1 extract /home/ztp --tar | tar x -C ./out
----

. Review the baseline `PerformanceProfile` CR in `./out/source-crs/PerformanceProfile.yaml`:
+
[source,yaml]
----
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: $name
  annotations:
    ran.openshift.io/ztp-deploy-wave: "10"
spec:
  additionalKernelArgs:
  - "idle=poll"
  - "rcupdate.rcu_normal_after_boot=0"
  cpu:
    isolated: $isolated
    reserved: $reserved
  hugepages:
    defaultHugepagesSize: $defaultHugepagesSize
    pages:
      - size: $size
        count: $count
        node: $node
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/$mcp: ""
  net:
    userLevelNetworking: true
  nodeSelector:
    node-role.kubernetes.io/$mcp: ''
  numa:
    topologyPolicy: "restricted"
  realTimeKernel:
    enabled: true
----
+
[NOTE]
====
Any fields in the source CR which contain `$...` are removed from the generated CR if they are not provided in the `{policy-gen-cr}` CR.
====

. Update the `{policy-gen-cr}` entry for `PerformanceProfile` in the `{policy-prefix}group-du-sno-ranGen.yaml` reference file. The following example `{policy-gen-cr}` CR stanza supplies appropriate CPU specifications, sets the `hugepages` configuration, and adds a new field that sets `globallyDisableIrqLoadBalancing` to false.
+
[source,yaml]
----
----

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} argo CD application.
+
.Example output
The {ztp} application generates an {rh-rhacm} policy that contains the generated `PerformanceProfile` CR. The contents of that CR are derived by merging the `metadata` and `spec` contents from the `PerformanceProfile` entry in the `{policy-gen-cr}` onto the source CR. The resulting CR has the following content:
+
[source,yaml]
----
---
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
    name: openshift-node-performance-profile
spec:
    additionalKernelArgs:
        - idle=poll
        - rcupdate.rcu_normal_after_boot=0
    cpu:
        isolated: 2-19,22-39
        reserved: 0-1,20-21
    globallyDisableIrqLoadBalancing: false
    hugepages:
        defaultHugepagesSize: 1G
        pages:
            - count: 10
              size: 1G
    machineConfigPoolSelector:
        pools.operator.machineconfiguration.openshift.io/master: ""
    net:
        userLevelNetworking: true
    nodeSelector:
        node-role.kubernetes.io/master: ""
    numa:
        topologyPolicy: restricted
    realTimeKernel:
        enabled: true
----

[NOTE]
====
In the `/source-crs` folder that you extract from the `ztp-site-generate` container,  the `$` syntax is not used for template substitution as implied by the syntax. Rather, if the `policyGen` tool sees the `$` prefix for a string and you do not specify a value for that field in the related `{policy-gen-cr}` CR, the field is omitted from the output CR entirely.

An exception to this is the `$mcp` variable in `/source-crs` YAML files that is substituted with the specified value for `mcp` from the `{policy-gen-cr}` CR. For example, in `example/{path-prefix}/{policy-prefix}group-du-standard-ranGen.yaml`, the value for `mcp` is `worker`:

[source,yaml]
----
spec:
  bindingRules:
    group-du-standard: ""
  mcp: "worker"
----

The `policyGen` tool replace instances of `$mcp` with `worker` in the output CRs.
====

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-adding-new-content-to-gitops-ztp_{context}"]
= Adding custom content to the {ztp} pipeline

Perform the following procedure to add new content to the {ztp} pipeline.

.Procedure

. Create a subdirectory named `source-crs` in the directory that contains the `kustomization.yaml` file for the `{policy-gen-cr}` custom resource (CR).

. Add your user-provided CRs to the `source-crs` subdirectory, as shown in the following example:
+

. Update the required `{policy-gen-cr}` CRs to include references to the content you added in the `source-crs/custom-crs` and `source-crs/elasticsearch` directories. For example:
+

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository that is monitored by the GitOps ZTP Argo CD policies application.

. Update the `ClusterGroupUpgrade` CR to include the changed `{policy-gen-cr}` and save it as `cgu-test.yaml`. The following example shows a generated `cgu-test.yaml` file.
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: custom-source-cr
  namespace: ztp-clusters
spec:
  managedPolicies:
    - group-dev-config-policy
  enable: true
  clusters:
  - cluster1
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
----

. Apply the updated `ClusterGroupUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f cgu-test.yaml
----

.Verification

* Check that the updates have succeeded by running the following command:
+
[source, terminal]
----
$ oc get cgu -A
----
+
.Example output
+
[source, terminal]
----
NAMESPACE     NAME               AGE   STATE        DETAILS
ztp-clusters  custom-source-cr   6s    InProgress   Remediating non-compliant policies
ztp-install   cluster1           19h   Completed    All clusters are compliant with all the managed policies
----

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-configuring-pgt-compliance-eval-timeouts_{context}"]
= Configuring policy compliance evaluation timeouts for {policy-gen-cr} CRs

Use {rh-rhacm-first} installed on a hub cluster to monitor and report on whether your managed clusters are compliant with applied policies. {rh-rhacm} uses policy templates to apply predefined policy controllers and policies. Policy controllers are Kubernetes custom resource definition (CRD) instances.

You can override the default policy evaluation intervals with `{policy-gen-cr}` custom resources (CRs). You configure duration settings that define how long a `ConfigurationPolicy` CR can be in a state of policy compliance or non-compliance before {rh-rhacm} re-evaluates the applied cluster policies.

The {ztp-first} policy generator generates `ConfigurationPolicy` CR policies with pre-defined policy evaluation intervals. The default value for the `noncompliant` state is 10 seconds. The default value for the `compliant` state is 10 minutes. To disable the evaluation interval, set the value to `never`.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have created a Git repository where you manage your custom site configuration data.

.Procedure

. To configure the evaluation interval for all policies in a `{policy-gen-cr}` CR, set appropriate `compliant` and `noncompliant` values for the `evaluationInterval` field.
For example:
+
[source,yaml]
----
spec:
  evaluationInterval:
    compliant: 30m
    noncompliant: 20s
policyDefaults:
  evaluationInterval:
    compliant: 30m
    noncompliant: 45s
----
+
[NOTE]
====
You can also set `compliant` and `noncompliant` fields to `never` to stop evaluating the policy after it reaches particular compliance state.
====

. To configure the evaluation interval for an individual policy object in a `{policy-gen-cr}` CR, add the `evaluationInterval` field and set appropriate values.
For example:
+
[source,yaml]
----
spec:
  sourceFiles:
    - fileName: SriovSubscription.yaml
      policyName: "sriov-sub-policy"
      evaluationInterval:
        compliant: never
        noncompliant: 10s
policies:
  - name: "sriov-sub-policy"
    manifests:
      - path: "SriovSubscription.yaml"
        evaluationInterval:
          compliant: never
          noncompliant: 10s
----

. Commit the `{policy-gen-cr}` CRs files in the Git repository and push your changes.

.Verification

Check that the managed spoke cluster policies are monitored at the expected intervals.

. Log in as a user with `cluster-admin` privileges on the managed cluster.

. Get the pods that are running in the `open-cluster-management-agent-addon` namespace. Run the following command:
+
[source,terminal]
----
$ oc get pods -n open-cluster-management-agent-addon
----
+
.Example output
[source,terminal]
----
NAME                                         READY   STATUS    RESTARTS        AGE
config-policy-controller-858b894c68-v4xdb    1/1     Running   22 (5d8h ago)   10d
----

. Check the applied policies are being evaluated at the expected interval in the logs for the `config-policy-controller` pod:
+
[source,terminal]
----
$ oc logs -n open-cluster-management-agent-addon config-policy-controller-858b894c68-v4xdb
----
+
.Example output
[source,terminal]
----
2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-config-policy-config"}
2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-common-compute-1-catalog-policy-config"}
----

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-creating-a-validator-inform-policy_{context}"]
= Signalling {ztp} cluster deployment completion with validator inform policies

Create a validator inform policy that signals when the {ztp-first} installation and configuration of the deployed cluster is complete. This policy can be used for deployments of {sno} clusters, three-node clusters, and standard clusters.

.Procedure

. Create a standalone `{policy-gen-cr}` custom resource (CR) that contains the source file
`validatorCRs/informDuValidator.yaml`. You only need one standalone `{policy-gen-cr}` CR for each cluster type. For example, this CR applies a validator inform policy for {sno} clusters:
+

. Commit the `{policy-gen-cr}` CR file in your Git repository and push the changes.

[role="_additional-resources"]
.Additional resources

* Upgrading {ztp}

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-configure-power-saving-states_{context}"]
= Configuring power states using {policy-gen-cr} CRs

For low latency and high-performance edge deployments, it is necessary to disable or limit C-states and P-states.
With this configuration, the CPU runs at a constant frequency, which is typically the maximum turbo frequency. This ensures that the CPU is always running at its maximum speed, which results in high performance and low latency.
This leads to the best latency for workloads.
However, this also leads to the highest power consumption, which might not be necessary for all workloads.

Workloads can be classified as critical or non-critical, with critical workloads requiring disabled C-state and P-state settings for high performance and low latency, while non-critical workloads use C-state and P-state settings for power savings at the expense of some latency and performance. You can configure the following three power states using {ztp-first}:

* High-performance mode provides ultra low latency at the highest power consumption.
* Performance mode provides low latency at a relatively high power consumption.
* Power saving balances reduced power consumption with increased latency.

The default configuration is for a low latency, performance mode.

`{policy-gen-cr}` custom resources (CRs) allow you to overlay additional configuration details onto the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container.

Configure the power states by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `{policy-gen-cr}` CR in the `{policy-prefix}group-du-sno-ranGen.yaml`.

The following common prerequisites apply to configuring all three power states.

.Prerequisites

* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.

* You have followed the procedure described in "Preparing the {ztp} site configuration repository".

[role="_additional-resources"]
.Additional resources

* Configuring node power consumption and realtime processing with workload hints

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-configure-performance-mode_{context}"]
= Configuring performance mode using {policy-gen-cr} CRs

Follow this example to set performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `{policy-gen-cr}` CR in the `{policy-prefix}group-du-sno-ranGen.yaml`.

Performance mode provides low latency at a relatively high power consumption.

.Prerequisites

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

.Procedure

. Update the `{policy-gen-cr}` entry for `PerformanceProfile` in the `{policy-prefix}group-du-sno-ranGen.yaml` reference file in `{argocd-folder}/` as follows to set performance mode.
+
[source,yaml]
----
----

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-configure-high-performance-mode_{context}"]
= Configuring high-performance mode using {policy-gen-cr} CRs

Follow this example to set high performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `{policy-gen-cr}` CR in the `{policy-prefix}group-du-sno-ranGen.yaml`.

High performance mode provides ultra low latency at the highest power consumption.

.Prerequisites

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

.Procedure

. Update the `{policy-gen-cr}` entry for `PerformanceProfile` in the `{policy-prefix}group-du-sno-ranGen.yaml` reference file in `{argocd-folder}` as follows to set high-performance mode.
+
[source,yaml]
----
----

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-configure-power-saving-mode_{context}"]
= Configuring power saving mode using {policy-gen-cr} CRs

Follow this example to set power saving mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `{policy-gen-cr}` CR in the `{policy-prefix}group-du-sno-ranGen.yaml`.

The power saving mode balances reduced power consumption with increased latency.

.Prerequisites

* You enabled C-states and OS-controlled P-states in the BIOS.

.Procedure

. Update the `{policy-gen-cr}` entry for `PerformanceProfile` in the `{policy-prefix}group-du-sno-ranGen.yaml` reference file in `{argocd-folder}` as follows to configure power saving mode. It is recommended to configure the CPU governor for the power saving mode through the additional kernel arguments object.
+

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.

.Verification

.  Select a worker node in your deployed cluster from the list of nodes identified by using the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Log in to the node by using the following command:
+
[source,terminal]
----
$ oc debug node/<node-name>
----
+
Replace `<node-name>` with the name of the node you want to verify the power state on.

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths as shown in the following example:
+
[source,terminal]
----
# chroot /host
----

. Run the following command to verify the applied power state:
+
[source,terminal]
----
# cat /proc/cmdline
----

.Expected output

* For power saving mode the `intel_pstate=passive`.

[role="_additional-resources"]
.Additional resources

* Configuring power saving for nodes that run colocated high and low priority workloads

* Configuring host firmware for low latency and high performance

* Preparing the {ztp} site configuration repository

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-using-pgt-to-maximize-power-savings-mode_{context}"]
= Maximizing power savings

Limiting the maximum CPU frequency is recommended to achieve maximum power savings.
Enabling C-states on the non-critical workload CPUs without restricting the maximum CPU frequency negates much of the power savings by boosting the frequency of the critical CPUs.

Maximize power savings by updating the `sysfs` plugin fields, setting an appropriate value for `max_perf_pct` in the `TunedPerformancePatch` CR for the reference configuration. This example based on the `{policy-prefix}group-du-sno-ranGen.yaml` describes the procedure to follow to restrict the maximum CPU frequency.

.Prerequisites

* You have configured power savings mode as described in "Using {policy-gen-cr} CRs to configure power savings mode".

.Procedure

. Update the `{policy-gen-cr}` entry for `TunedPerformancePatch` in the `{policy-prefix}group-du-sno-ranGen.yaml` reference file in `{argocd-folder}`. To maximize power savings, add `max_perf_pct` as shown in the following example:
+
+
[NOTE]
====
To maximize power savings, set a lower value. Setting a lower value for `max_perf_pct` limits the maximum CPU frequency, thereby reducing power consumption, but also potentially impacting performance. Experiment with different values and monitor the system's performance and power consumption to find the optimal setting for your use-case.
====

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-provisioning-lvm-storage_{context}"]
= Configuring {lvms} using {policy-gen-cr} CRs

You can configure {lvms-first} for managed clusters that you deploy with {ztp-first}.

[NOTE]
====
You use {lvms} to persist event subscriptions when you use PTP events or bare-metal hardware events with HTTP transport.

Use the Local Storage Operator for persistent storage that uses local volumes in distributed units.
====

.Prerequisites

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

* Create a Git repository where you manage your custom site configuration data.

.Procedure

. To configure {lvms} for new managed clusters, add the following YAML to `{rangen-yaml-path}` in the `{policy-prefix}common-ranGen.yaml` file:
+
+
[NOTE]
====
The Storage LVMO subscription is deprecated. In future releases of OpenShift Container Platform, the storage LVMO subscription will not be available. Instead, you must use the Storage LVMS subscription.

In OpenShift Container Platform , you can use the Storage LVMS subscription instead of the LVMO subscription. The LVMS subscription does not require manual overrides in the `{policy-prefix}common-ranGen.yaml` file. Add the following YAML to `{rangen-yaml-path}` in the `{policy-prefix}common-ranGen.yaml` file to use the Storage LVMS subscription:

[source,yaml]
----
----
====

. Add the `LVMCluster` CR to `{rangen-yaml-path}` in your specific group or individual site configuration file. For example, in the `{policy-prefix}group-du-sno-ranGen.yaml` file, add the following:
+
--

This example configuration creates a volume group (`vg1`) with all the available devices, except the disk where OpenShift Container Platform is installed.
A thin-pool logical volume is also created.
--

. Merge any other required changes and files with your custom site repository.

. Commit the `{policy-gen-cr}` changes in Git, and then push the changes to your site configuration repository to deploy {lvms} to new sites using {ztp}.

[id="ztp-advanced-policy-config-ptp_{context}"]
== Configuring PTP events with {policy-gen-cr} CRs

You can use the {ztp} pipeline to configure PTP events that use HTTP transport.

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-configuring-ptp-fast-events_{context}"]
= Configuring PTP events that use HTTP transport

You can configure PTP events that use HTTP transport on managed clusters that you deploy with the {ztp-first} pipeline.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

* You have created a Git repository where you manage your custom site configuration data.

.Procedure

. Apply the following `{policy-gen-cr}` changes to `{policy-prefix}group-du-3node-ranGen.yaml`, `{policy-prefix}group-du-sno-ranGen.yaml`, or `{policy-prefix}group-du-standard-ranGen.yaml` files according to your requirements:

.. In `{rangen-yaml-path}`, add the `PtpOperatorConfig` CR file that configures the transport host:
+
[source,yaml]
----
----
+
[NOTE]
====
In OpenShift Container Platform 4.13 or later, you do not need to set the `transportHost` field in the `PtpOperatorConfig` resource when you use HTTP transport with PTP events.
====

.. Configure the `linuxptp` and `phc2sys` for the PTP clock type and interface. For example, add the following YAML into `{rangen-yaml-path}`:
+

. Merge any other required changes and files with your custom site repository.

. Push the changes to your site configuration repository to deploy PTP fast events to new sites using {ztp}.

[role="_additional-resources"]
.Additional resources

* Using {policy-gen-cr} CRs to override source CRs content

[role="_additional-resources"]
.Additional resources

* {product-registry} overview

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-add-local-reg-for-sno-duprofile_{context}"]
= Configuring the Image Registry Operator for local caching of images

OpenShift Container Platform manages image caching using a local registry. In edge computing use cases, clusters are often subject to bandwidth restrictions when communicating with centralized image registries, which might result in long image download times.

Long download times are unavoidable during initial deployment. Over time, there is a risk that CRI-O will erase the `/var/lib/containers/storage` directory in the case of an unexpected shutdown.
To address long image download times, you can create a local image registry on remote managed clusters using {ztp-first}. This is useful in Edge computing scenarios where clusters are deployed at the far edge of the network.

Before you can set up the local image registry with {ztp}, you need to configure disk partitioning in the `ClusterInstance` CR that you use to install the remote managed cluster. After installation, you configure the local image registry using a `{policy-gen-cr}` CR. Then, the {ztp} pipeline creates Persistent Volume (PV) and Persistent Volume Claim (PVC) CRs and patches the `imageregistry` configuration.

[NOTE]
====
The local image registry can only be used for user application images and cannot be used for the OpenShift Container Platform or Operator Lifecycle Manager operator images.
====

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform registry overview

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-configuring-disk-partitioning_{context}"]
= Configuring disk partitioning with ClusterInstance

Configure disk partitioning for a managed cluster using a `ClusterInstance` CR and {ztp-first}. The  disk partition details in the `ClusterInstance` CR must match the underlying disk.

[IMPORTANT]
====
You must complete this procedure at installation time.
====

.Prerequisites

* Install Butane.

.Procedure

. Create the `storage.bu` file.
+
[source,yaml]
----
variant: fcos
version: 1.3.0
storage:
  disks:
  - device: /dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0 <1>
    wipe_table: false
    partitions:
    - label: var-lib-containers
      start_mib: <start_of_partition> <2>
      size_mib: <partition_size> <3>
  filesystems:
    - path: /var/lib/containers
      device: /dev/disk/by-partlabel/var-lib-containers
      format: xfs
      wipe_filesystem: true
      with_mount_unit: true
      mount_options:
        - defaults
        - prjquota
----
<1> Specify the root disk.
<2> Specify the start of the partition in MiB. If the value is too small, the installation fails.
<3> Specify the size of the partition. If the value is too small, the deployments fails.

. Convert the `storage.bu` to an Ignition file by running the following command:
+
--
[source,terminal]
----
$ butane storage.bu
----

.Example output
[source,terminal]
----
{"ignition":{"version":"3.2.0"},"storage":{"disks":[{"device":"/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0","partitions":[{"label":"var-lib-containers","sizeMiB":0,"startMiB":250000}],"wipeTable":false}],"filesystems":[{"device":"/dev/disk/by-partlabel/var-lib-containers","format":"xfs","mountOptions":["defaults","prjquota"],"path":"/var/lib/containers","wipeFilesystem":true}]},"systemd":{"units":[{"contents":"# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target","enabled":true,"name":"var-lib-containers.mount"}]}}
----
--

. Use a tool such as JSON Pretty Print to convert the output into JSON format.

. Copy the output into the `spec.nodes[].ignitionConfigOverride` field in the `ClusterInstance` CR.
+
.Example
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-sno"
  namespace: "example-sno"
spec:
  # ...
  nodes:
    - hostName: "node1.example.com"
      role: "master"
      ignitionConfigOverride: |
          {
            "ignition": {
              "version": "3.2.0"
            },
            "storage": {
              "disks": [
                {
                  "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                  "partitions": [
                    {
                      "label": "var-lib-containers",
                      "sizeMiB": 0,
                      "startMiB": 250000
                    }
                  ],
                  "wipeTable": false
                }
              ],
              "filesystems": [
                {
                  "device": "/dev/disk/by-partlabel/var-lib-containers",
                  "format": "xfs",
                  "mountOptions": [
                    "defaults",
                    "prjquota"
                  ],
                  "path": "/var/lib/containers",
                  "wipeFilesystem": true
                }
              ]
            },
            "systemd": {
              "units": [
                {
                  "contents": "# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                  "enabled": true,
                  "name": "var-lib-containers.mount"
                }
              ]
            }
          }
----
+
[NOTE]
====
If the `spec.nodes[].ignitionConfigOverride` field does not exist, create it.
====

.Verification

.  During or after installation, verify on the hub cluster that the `BareMetalHost` object shows the annotation by running the following command:
+
--
[source,terminal]
----
$ oc get bmh -n my-sno-ns my-sno -ojson | jq '.metadata.annotations["bmac.agent-install.openshift.io/ignition-config-overrides"]
----

.Example output
[source,terminal]
----
"{\"ignition\":{\"version\":\"3.2.0\"},\"storage\":{\"disks\":[{\"device\":\"/dev/disk/by-id/wwn-0x6b07b250ebb9d0002a33509f24af1f62\",\"partitions\":[{\"label\":\"var-lib-containers\",\"sizeMiB\":0,\"startMiB\":250000}],\"wipeTable\":false}],\"filesystems\":[{\"device\":\"/dev/disk/by-partlabel/var-lib-containers\",\"format\":\"xfs\",\"mountOptions\":[\"defaults\",\"prjquota\"],\"path\":\"/var/lib/containers\",\"wipeFilesystem\":true}]},\"systemd\":{\"units\":[{\"contents\":\"# Generated by Butane\\n[Unit]\\nRequires=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\nAfter=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\n\\n[Mount]\\nWhere=/var/lib/containers\\nWhat=/dev/disk/by-partlabel/var-lib-containers\\nType=xfs\\nOptions=defaults,prjquota\\n\\n[Install]\\nRequiredBy=local-fs.target\",\"enabled\":true,\"name\":\"var-lib-containers.mount\"}]}}"
----
--

. After installation, check the {sno} disk status.

.. Enter into a debug session on the {sno} node by running the following command. This step instantiates a debug pod called `<node_name>-debug`:
+
[source,terminal]
----
$ oc debug node/my-sno-node
----

.. Set `/host` as the root directory within the debug shell by running the following command. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----

.. List information about all available block devices by running the following command:
+
[source,terminal]
----
# lsblk
----
+
.Example output
[source,terminal]
----
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 446.6G  0 disk
├─sda1   8:1    0     1M  0 part
├─sda2   8:2    0   127M  0 part
├─sda3   8:3    0   384M  0 part /boot
├─sda4   8:4    0 243.6G  0 part /var
│                                /sysroot/ostree/deploy/rhcos/var
│                                /usr
│                                /etc
│                                /
│                                /sysroot
└─sda5   8:5    0 202.5G  0 part /var/lib/containers
----

.. Display information about the file system disk space usage by running the following command:
+
[source,terminal]
----
# df -h
----
+
.Example output
[source,terminal]
----
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        4.0M     0  4.0M   0% /dev
tmpfs           126G   84K  126G   1% /dev/shm
tmpfs            51G   93M   51G   1% /run
/dev/sda4       244G  5.2G  239G   3% /sysroot
tmpfs           126G  4.0K  126G   1% /tmp
/dev/sda5       203G  119G   85G  59% /var/lib/containers
/dev/sda3       350M  110M  218M  34% /boot
tmpfs            26G     0   26G   0% /run/user/1000
----

// Module included in the following assemblies:
//
// * edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.adoc
// * edge_computing/policygentemplate_for_ztp/ztp-advanced-policy-config.adoc

[id="ztp-configuring-pgt-image-registry_{context}"]
= Configuring the image registry using {policy-gen-cr} CRs

Use `{policy-gen-cr}` (PGT) CRs to apply the CRs required to configure the image registry and patch the `imageregistry` configuration.

.Prerequisites

* You have configured a disk partition in the managed cluster.

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have created a Git repository where you manage your custom site configuration data for use with {ztp-first}.

.Procedure

. Configure the storage class, persistent volume claim, persistent volume, and image registry configuration in the appropriate `{policy-gen-cr}` CR. For example, to configure an individual site, add the following YAML to the file `{policy-prefix}example-sno-site.yaml`:
+
[source,yaml]
----
sourceFiles:
  # storage class
  - fileName: StorageClass.yaml
    policyName: "sc-for-image-registry"
    metadata:
      name: image-registry-sc
      annotations:
        ran.openshift.io/ztp-deploy-wave: "100" <1>
  # persistent volume claim
  - fileName: StoragePVC.yaml
    policyName: "pvc-for-image-registry"
    metadata:
      name: image-registry-pvc
      namespace: openshift-image-registry
      annotations:
        ran.openshift.io/ztp-deploy-wave: "100"
    spec:
      accessModes:
        - ReadWriteMany
      resources:
        requests:
          storage: 100Gi
      storageClassName: image-registry-sc
      volumeMode: Filesystem
  # persistent volume
  - fileName: ImageRegistryPV.yaml <2>
    policyName: "pv-for-image-registry"
    metadata:
      annotations:
        ran.openshift.io/ztp-deploy-wave: "100"
  - fileName: ImageRegistryConfig.yaml
    policyName: "config-for-image-registry"
    complianceType: musthave
    metadata:
      annotations:
        ran.openshift.io/ztp-deploy-wave: "100"
    spec:
      storage:
        pvc:
          claim: "image-registry-pvc"
----
<1> Set the appropriate value for `ztp-deploy-wave` depending on whether you are configuring image registries at the site, common, or group level. `ztp-deploy-wave: "100"` is suitable for development or testing because it allows you to group the referenced source files together.
<2> In `ImageRegistryPV.yaml`, ensure that the `spec.local.path` field is set to `/var/imageregistry` to match the value set for the `mount_point` field in the `ClusterInstance` CR.

+
[IMPORTANT]
====
Do not set `complianceType: mustonlyhave` for the `- fileName: ImageRegistryConfig.yaml` configuration. This can cause the registry pod deployment to fail.
====

. Commit the `{policy-gen-cr}` change in Git, and then push to the Git repository being monitored by the {ztp} ArgoCD application.

.Verification

Use the following steps to troubleshoot errors with the local image registry on the managed clusters:

* Verify successful login to the registry while logged in to the managed cluster. Run the following commands:

.. Export the managed cluster name:
+
[source,terminal]
----
$ cluster=<managed_cluster_name>
----

.. Get the managed cluster `kubeconfig` details:
+
[source,terminal]
----
$ oc get secret -n $cluster $cluster-admin-password -o jsonpath='{.data.password}' | base64 -d > kubeadmin-password-$cluster
----

.. Download and export the cluster `kubeconfig`:
+
[source,terminal]
----
$ oc get secret -n $cluster $cluster-admin-kubeconfig -o jsonpath='{.data.kubeconfig}' | base64 -d > kubeconfig-$cluster && export KUBECONFIG=./kubeconfig-$cluster
----

.. Verify access to the image registry from the managed cluster. See "Accessing the registry".

* Check that the `Config` CRD in the `imageregistry.operator.openshift.io` group instance is not reporting errors. Run the following command while logged in to the managed cluster:
+
[source,terminal]
----
$ oc get image.config.openshift.io cluster -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: "true"
    include.release.openshift.io/self-managed-high-availability: "true"
    include.release.openshift.io/single-node-developer: "true"
    release.openshift.io/create-only: "true"
  creationTimestamp: "2021-10-08T19:02:39Z"
  generation: 5
  name: cluster
  resourceVersion: "688678648"
  uid: 0406521b-39c0-4cda-ba75-873697da75a4
spec:
  additionalTrustedCA:
    name: acm-ice
----

* Check that the `PersistentVolumeClaim` on the managed cluster is populated with data. Run the following command while logged in to the managed cluster:
+
[source,terminal]
----
$ oc get pv image-registry-sc
----

* Check that the `registry*` pod is running and is located under the `openshift-image-registry` namespace.
+
[source,terminal]
----
$ oc get pods -n openshift-image-registry | grep registry*
----
+
.Example output
[source,terminal]
----
cluster-image-registry-operator-68f5c9c589-42cfg   1/1     Running     0          8d
image-registry-5f8987879-6nx6h                     1/1     Running     0          8d
----

* Check that the disk partition on the managed cluster is correct:

.. Open a debug shell to the managed cluster:
+
[source,terminal]
----
$ oc debug node/sno-1.example.com
----

.. Run `lsblk` to check the host disk partitions:
+
[source,terminal]
----
sh-4.4# lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 446.6G  0 disk
  |-sda1   8:1    0     1M  0 part
  |-sda2   8:2    0   127M  0 part
  |-sda3   8:3    0   384M  0 part /boot
  |-sda4   8:4    0 336.3G  0 part /sysroot
  `-sda5   8:5    0 100.1G  0 part /var/imageregistry <1>
sdb      8:16   0 446.6G  0 disk
sr0     11:0    1   104M  0 rom
----
<1> `/var/imageregistry` indicates that the disk is correctly partitioned.

[role="_additional-resources"]
.Additional resources

* Accessing the registry
