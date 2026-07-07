---
title: "Expanding single-node OpenShift clusters with GitOps ZTP"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-sno-additional-worker-node
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-sno-additional-worker-node
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Expanding single-node OpenShift clusters with GitOps ZTP

[id="ztp-sno-additional-worker-node"]
= Expanding single-node OpenShift clusters with GitOps ZTP

You can expand {sno} clusters with {ztp-first}. When you add a worker node to {sno} clusters, the original {sno} cluster retains the control plane node role. Adding a worker node does not require any downtime for the existing {sno} cluster.

[NOTE]
====
You can only expand a {sno} cluster with one additional worker node. It is not recommended to expand a {sno} cluster with more than one worker node.
====

If you require workload partitioning on the worker node, you must deploy and remediate the managed cluster policies on the hub cluster before installing the node. This way, the workload partitioning `MachineConfig` objects are rendered and associated with the `worker` machine config pool before the {ztp} workflow applies the `MachineConfig` ignition file to the worker node.

It is recommended that you first remediate the policies, and then install the worker node.
If you create the workload partitioning manifests after installing the worker node, you must drain the node manually and delete all the pods managed by daemon sets. When the managing daemon sets create the new pods, the new pods undergo the workload partitioning process.

[role="_additional-resources"]
.Additional resources

* For more information about {sno} clusters tuned for vDU application deployments, see Reference configuration for deploying vDUs on {sno}.

* For more information about worker nodes, see Adding worker nodes to {sno} clusters.

* For information about removing a worker node from an expanded {sno} cluster, see Removing managed cluster nodes by using the command line interface.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

[id="ztp-additional-worker-apply-du-profile_{context}"]
= Applying profiles to the worker node with PolicyGenerator or PolicyGenTemplate resources

You can configure the additional worker node with a DU profile.

You can apply a RAN distributed unit (DU) profile to the worker node cluster using the {ztp-first} common, group, and site-specific `PolicyGenerator` or  `PolicyGenTemplate` resources. The {ztp} pipeline that is linked to the ArgoCD `policies` application includes the following CRs that you can find in the relevant `out/argocd/example` folder when you extract the `ztp-site-generate` container:

/acmpolicygenerator resources::
* `acm-common-ranGen.yaml`
* `acm-group-du-sno-ranGen.yaml`
* `acm-example-sno-site.yaml`
* `ns.yaml`
* `kustomization.yaml`

/policygentemplates resources::
* `common-ranGen.yaml`
* `group-du-sno-ranGen.yaml`
* `example-sno-site.yaml`
* `ns.yaml`
* `kustomization.yaml`

Configuring the DU profile on the worker node is considered an upgrade. To initiate the upgrade flow, you must update the existing policies or create additional ones. Then, you must create a `ClusterGroupUpgrade` CR to reconcile the policies in the group of clusters.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

[id="ztp-additional-worker-daemon-selector-comp_{context}"]
= Ensuring PTP and SR-IOV daemon selector compatibility

If the DU profile was deployed using the {ztp-first} plugin version 4.11 or earlier, the PTP and SR-IOV Operators might be configured to place the daemons only on nodes labeled as `master`. This configuration prevents the PTP and SR-IOV daemons from operating on the worker node. If the PTP and SR-IOV daemon node selectors are incorrectly configured on your system, you must change the daemons before proceeding with the worker DU profile configuration.

.Procedure

. Check the daemon node selector settings of the PTP Operator on one of the spoke clusters:
+
[source,terminal]
----
$ oc get ptpoperatorconfig/default -n openshift-ptp -ojsonpath='{.spec}' | jq
----
+
.Example output for PTP Operator
+
[source,json]
----
{"daemonNodeSelector":{"node-role.kubernetes.io/master":""}} <1>
----
<1> If the node selector is set to `master`, the spoke was deployed with the version of the {ztp} plugin that requires changes.

. Check the daemon node selector settings of the SR-IOV Operator on one of the spoke clusters:
+
[source,terminal]
----
$  oc get sriovoperatorconfig/default -n \
openshift-sriov-network-operator -ojsonpath='{.spec}' | jq
----
+
.Example output for SR-IOV Operator
+
[source,json]
----
{"configDaemonNodeSelector":{"node-role.kubernetes.io/worker":""},"disableDrain":false,"enableInjector":true,"enableOperatorWebhook":true} <1>
----
<1> If the node selector is set to `master`, the spoke was deployed with the version of the {ztp} plugin that requires changes.

. In the group policy, add the following `complianceType` and `spec` entries:
+
[source,yaml]
----
spec:
    - fileName: PtpOperatorConfig.yaml
      policyName: "config-policy"
      complianceType: mustonlyhave
      spec:
        daemonNodeSelector:
          node-role.kubernetes.io/worker: ""
    - fileName: SriovOperatorConfig.yaml
      policyName: "config-policy"
      complianceType: mustonlyhave
      spec:
        configDaemonNodeSelector:
          node-role.kubernetes.io/worker: ""
----
+
[IMPORTANT]
====
Changing the `daemonNodeSelector` field causes temporary PTP synchronization loss and SR-IOV connectivity loss.
====

. Commit the changes in Git, and then push to the Git repository being monitored by the {ztp} ArgoCD application.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

[id="ztp-additional-worker-node-selector-comp_{context}"]
= PTP and SR-IOV node selector compatibility

The PTP configuration resources and SR-IOV network node policies use `node-role.kubernetes.io/master: ""` as the node selector. If the additional worker node has the same NIC configuration as the control plane node, the policies used to configure the control plane node can be reused for the worker node. However, the node selector must be changed to select both node types, for example with the `"node-role.kubernetes.io/worker"` label.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

[id="ztp-additional-worker-policies-{policy-gen-cr}_{context}"]
= Using {policy-gen-cr} CRs to apply worker node policies to the worker node

You can create policies for the additional worker node by using `{policy-gen-cr}` CRs.

.Procedure

. Create the following `{policy-gen-cr}` CR:
+
--

You can generate the content of `crio` and `kubelet` configuration files.
--

. Add the created policy template to the Git repository monitored by the ArgoCD `policies` application.

. Add the policy in the `kustomization.yaml` file.

. Commit the changes in Git, and then push to the Git repository being monitored by the {ztp} ArgoCD application.

. To remediate the new policies to your spoke cluster, create a TALM custom resource:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: example-sno-worker-policies
  namespace: default
spec:
  backup: false
  clusters:
  - example-sno
  enable: true
  managedPolicies:
  - group-du-sno-config-policy
  - example-sno-workers-config-policy
  - example-sno-config-policy
  preCaching: false
  remediationStrategy:
    maxConcurrency: 1
EOF
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

[id="ztp-additional-worker-sno-proc_{context}"]
= Adding an additional worker node {sno} clusters with {ztp}

You can add an additional worker node to existing {sno} clusters to increase available CPU resources in the cluster.

.Prerequisites

* Install and configure {rh-rhacm} 2.12 or later in an OpenShift Container Platform 4.11 or later bare-metal hub cluster
* Install {cgu-operator-full} in the hub cluster
* Install {gitops-title} in the hub cluster
* Use the {ztp} `ztp-site-generate` container image version 4.12 or later
* Deploy a managed {sno} cluster with {ztp}
* Configure the Central Infrastructure Management as described in the {rh-rhacm} documentation
* Configure the DNS serving the cluster to resolve the internal API endpoint `api-int.<cluster_name>.<base_domain>`

.Procedure

. If you deployed your cluster by using the `example-sno.yaml` `ClusterInstance` CR, add your new worker node to the `spec.nodes` list:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-sno"
  namespace: "example-sno"
spec:
  # ... existing cluster configuration ...
  nodes:
      - hostName: "example-sno.example.com"
        role: "master"
        # ... existing master node configuration ...
      - hostName: "example-node2.example.com"
        role: "worker"
        bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
        bmcCredentialsName:
          name: "example-node2-bmh-secret"
        bootMACAddress: "AA:BB:CC:DD:EE:11"
        bootMode: "UEFI"
        nodeNetwork:
          interfaces:
            - name: eno1
              macAddress: "AA:BB:CC:DD:EE:11"
          config:
            interfaces:
              - name: eno1
                type: ethernet
                state: up
                macAddress: "AA:BB:CC:DD:EE:11"
                ipv4:
                  enabled: false
                ipv6:
                  enabled: true
                  address:
                  - ip: 1111:2222:3333:4444::1
                    prefix-length: 64
            dns-resolver:
              config:
                search:
                - example.com
                server:
                - 1111:2222:3333:4444::2
            routes:
              config:
              - destination: ::/0
                next-hop-interface: eno1
                next-hop-address: 1111:2222:3333:4444::1
                table-id: 254
----

. Create a BMC authentication secret for the new host, as referenced by the `bmcCredentialsName` field in the `spec.nodes` section of your `ClusterInstance` CR:
+
[source,yaml]
----
apiVersion: v1
data:
  password: "password"
  username: "username"
kind: Secret
metadata:
  name: "example-node2-bmh-secret"
  namespace: example-sno
type: Opaque
----

. Commit the changes in Git, and then push to the Git repository that is being monitored by the {ztp} ArgoCD application.
+
When the ArgoCD `cluster` application synchronizes, two new manifests appear on the hub cluster generated by the SiteConfig Operator:
+
* `BareMetalHost`
* `NMStateConfig`
+
[IMPORTANT]
====
The `cpuset` field should not be configured for the worker node. Workload partitioning for the worker node is added through management policies after the node installation is complete.
====

.Verification

You can monitor the installation process in several ways.

* Check if the preprovisioning images are created by running the following command:
+
[source,terminal]
----
$ oc get ppimg -n example-sno
----
+
.Example output
[source,terminal]
----
NAMESPACE       NAME            READY   REASON
example-sno     example-sno     True    ImageCreated
example-sno     example-node2   True    ImageCreated
----

* Check the state of the bare-metal hosts:
+
[source,terminal]
----
$ oc get bmh -n example-sno
----
+
.Example output
[source,terminal]
----
NAME            STATE          CONSUMER   ONLINE   ERROR   AGE
example-sno     provisioned               true             69m
example-node2   provisioning              true             4m50s <1>
----
<1> The `provisioning` state indicates that node booting from the installation media is in progress.

* Continuously monitor the installation process:

.. Watch the agent install process by running the following command:
+
[source,terminal]
----
$ oc get agent -n example-sno --watch
----
+
.Example output
[source,terminal]
----
NAME                                   CLUSTER   APPROVED   ROLE     STAGE
671bc05d-5358-8940-ec12-d9ad22804faa   example-sno   true       master   Done
[...]
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Starting installation
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Installing
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Writing image to disk
[...]
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Waiting for control plane
[...]
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Rebooting
14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Done
----

.. When the worker node installation is finished, the worker node certificates are approved automatically. At this point, the worker appears in the `ManagedClusterInfo` status. Run the following command to see the status:
+
[source,terminal]
----
$ oc get managedclusterinfo/example-sno -n example-sno -o \
jsonpath='{range .status.nodeList[*]}{.name}{"\t"}{.conditions}{"\t"}{.labels}{"\n"}{end}'
----
+
.Example output
[source,terminal]
----
example-sno	[{"status":"True","type":"Ready"}]	{"node-role.kubernetes.io/master":"","node-role.kubernetes.io/worker":""}
example-node2	[{"status":"True","type":"Ready"}]	{"node-role.kubernetes.io/worker":""}
----
