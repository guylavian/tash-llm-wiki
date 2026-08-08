---
title: "Replacing a failed bare-metal control plane node without BMC credentials"
type: reference
domain: openshift
slug: nodes-4-22-nodes-nodes-replace-control-plane
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-nodes-replace-control-plane
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Replacing a failed bare-metal control plane node without BMC credentials

[id="replacing-control-plane-node"]
= Replacing a failed bare-metal control plane node without BMC credentials

If a control plane node on your bare-metal cluster has failed and cannot be recovered, but you installed your cluster without providing baseboard management controller (BMC) credentials, you must take extra steps in order to replace the failed node with a new one.

// Prerequisites
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="prerequisites_{context}"]
= Prerequisites

* You have identified the unhealthy bare metal etcd member.
* You have verified that either the machine is not running or the node is not ready.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup in case you encounter any issues.
* You have downloaded and installed the `coreos-installer` CLI.
* Your cluster does not have a control plane `machineset`. You can check for `machinesets` by running the following command:
+
[source,terminal]
----
$ oc get machinesets,controlplanemachinesets -n openshift-machine-api
----
+
[IMPORTANT]
====
There should be only one or more `machinesets` for the workers.
If `controlplanemachinesets` exists for the control plane, do not use this procedure.
====

// Removing the unhealthy etcd member
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="removing-etcd-member_{context}"]
= Removing the unhealthy etcd member

Begin removing the failed control plane node by first removing the unhealthy etcd member.

.Procedure

. List etcd pods by running the following command and make note of a pod that is not on the affected node:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
----
+
.Example output
[source,terminal]
----
etcd-openshift-control-plane-0   5/5   Running   11   3h56m   192.168.10.9    openshift-control-plane-0  <none>           <none>
etcd-openshift-control-plane-1   5/5   Running   0    3h54m   192.168.10.10   openshift-control-plane-1   <none>           <none>
etcd-openshift-control-plane-2   5/5   Running   0    3h58m   192.168.10.11   openshift-control-plane-2   <none>           <none>
----

. Connect to a running etcd container by running the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd <etcd_pod>
----
+
Replace `<etcd_pod>` with the name of an etcd pod associated with one of the healthy nodes.
+
.Example command
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
----

. View the etcd member list by running the following command. Make note of the ID and the name of the unhealthy etcd member because these values are required later.
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 6fc1e7c9db35841d | started | openshift-control-plane-2    | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
| 757b6793e2408b6c | started | openshift-control-plane-1    | https://10.0.164.97:2380  | https://10.0.164.97:2379  |
| ca8c2990a0aa29d1 | started | openshift-control-plane-0    | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
[IMPORTANT]
====
The `etcdctl endpoint health` command will list the removed member until the replacement is complete and the new member is added.
====

. Remove the unhealthy etcd member by running the following command:
+
[source,terminal]
----
sh-4.2# etcdctl member remove <unhealthy_member_id>
----
+
Replace `<unhealthy_member_id>` with the ID of the etcd member on the unhealthy node.
+
.Example command
[source,terminal]
----
sh-4.2# etcdctl member remove 6fc1e7c9db35841d
----
+
.Example output
[source,terminal]
----
Member 6fc1e7c9db35841d removed from cluster b23536c33f2cdd1b
----

. View the member list again by running the following command and verify that the member was removed:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 757b6793e2408b6c | started | openshift-control-plane-1    | https://10.0.164.97:2380  | https://10.0.164.97:2379  |
| ca8c2990a0aa29d1 | started | openshift-control-plane-0    | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
[IMPORTANT]
====
After you remove the member, the cluster might be unreachable for a short time while the remaining etcd instances reboot.
====

. Exit the rsh session into the etcd pod by running the following command:
+
[source,terminal]
----
sh-4.2# exit
----

. Turn off the etcd quorum guard by running the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----
+
This command ensures that you can successfully re-create secrets and roll out the static pods.

. List the secrets for the removed, unhealthy etcd member by running the following command:
+
[source,terminal]
----
$ oc get secrets -n openshift-etcd | grep <node_name>
----
+
Replace `<node_name>` with the name of the failed node whose etcd member you removed.
+
.Example command
[source,terminal]
----
$ oc get secrets -n openshift-etcd | grep openshift-control-plane-2
----
+
.Example output
[source,terminal]
----
etcd-peer-openshift-control-plane-2             kubernetes.io/tls   2   134m
etcd-serving-metrics-openshift-control-plane-2  kubernetes.io/tls   2   134m
etcd-serving-openshift-control-plane-2          kubernetes.io/tls   2   134m
----

. Delete the secrets associated with the affected node that was removed:

.. Delete the peer secret by running the following command:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-peer-<node_name>
----
+
Replace `<node_name>` with the name of the affected node.

.. Delete the serving secret by running the following command:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-<node_name>
----
+
Replace `<node_name>` with the name of the affected node.

.. Delete the metrics secret by running the following command:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-metrics-<node_name> <1>
----
+
Replace `<node_name>` with the name of the affected node.

// Deleting the machine of the unhealthy etcd member
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="deleting-machine_{context}"]
= Deleting the machine of the unhealthy etcd member

Finish removing the failed control plane node by deleting the machine of the unhealthy etcd member.

.Procedure

. Ensure that the Bare Metal Operator is available by running the following command:
+
[source,terminal]
----
$ oc get clusteroperator baremetal
----
+
.Example output
[source,terminal]
----
NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
baremetal   4.22.0    True        False         False      3d15h
----

. Save the `BareMetalHost` object of the affected node to a file for later use by running the following command:
+
[source,terminal]
----
$ oc get -n openshift-machine-api bmh <node_name> -o yaml > bmh_affected.yaml
----
+
Replace `<node_name>` with the name of the affected node, which usually matches the associated `BareMetalHost` name.

. View the YAML file of the saved `BareMetalHost` object by running the following command, and ensure the content is correct:
+
[source,terminal]
----
$ cat bmh_affected.yaml
----

. Remove the affected `BareMetalHost` object by running the following command:
+
[source,terminal]
----
$ oc delete -n openshift-machine-api bmh <node_name>
----
+
Replace `<node_name>` with the name of the affected node.

. List all machines by running the following command and identify the machine associated with the affected node:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                            PHASE    TYPE  REGION  ZONE  AGE    NODE                       PROVIDERID                                                                                             STATE
examplecluster-control-plane-0  Running                      3h11m  openshift-control-plane-0  baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e  externally provisioned
examplecluster-control-plane-1  Running                      3h11m  openshift-control-plane-1  baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1  externally provisioned
examplecluster-control-plane-2  Running                      3h11m  openshift-control-plane-2  baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135  externally provisioned
examplecluster-compute-0        Running                      165m   openshift-compute-0        baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f        provisioned
examplecluster-compute-1        Running                      165m   openshift-compute-1        baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9        provisioned
----

. Delete the machine of the unhealthy member by running the following command:
+
[source,terminal]
----
$ oc delete machine -n openshift-machine-api <machine_name>
----
+
Replace `<machine_name>` with the machine name associated with the affected node.
+
.Example command
[source,terminal]
----
$ oc delete machine -n openshift-machine-api examplecluster-control-plane-2
----
+
[NOTE]
====
After you remove the `BareMetalHost` and `Machine` objects, the machine controller automatically deletes the `Node` object.
====

. If deletion of the machine is delayed for any reason or the command is obstructed and delayed, force deletion by removing the machine object finalizer field.
+
[WARNING]
====
Do not interrupt machine deletion by pressing `Ctrl+c`. You must allow the command to proceed to completion. Open a new terminal window to edit and delete the finalizer fields.
====

.. On a new terminal window, edit the machine configuration by running the following command:
+
[source,terminal]
----
$ oc edit machine -n openshift-machine-api examplecluster-control-plane-2
----

.. Delete the following fields in the `Machine` custom resource, and then save the updated file:
+
[source,yaml]
----
finalizers:
- machine.machine.openshift.io
----
+
.Example output
[source,terminal]
----
machine.machine.openshift.io/examplecluster-control-plane-2 edited
----

// Verifying that the failed node was deleted
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="verify-machine-deleted_{context}"]
= Verifying that the failed node was deleted

Before proceeding to create a replacement control plane node, verify that the failed node was successfully deleted.

.Procedure

. Verify that the machine was deleted by running the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                                 PROVIDERID                                                                                       STATE
examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
----

. Verify that the node has been deleted by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                     STATUS ROLES   AGE   VERSION
openshift-control-plane-0 Ready master 3h24m v1.35.4
openshift-control-plane-1 Ready master 3h24m v1.35.4
openshift-compute-0       Ready worker 176m v1.35.4
openshift-compute-1       Ready worker 176m v1.35.4
----

. Wait for all of the cluster Operators to complete rolling out changes.
Run the following command to monitor the progress:
+
[source,terminal]
----
$ watch oc get co
----

// Creating the new control plane node
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="create-new-machine_{context}"]
= Creating the new control plane node

Begin creating the new control plane node by creating a `BareMetalHost` object and node.

.Procedure

. Edit the `bmh_affected.yaml` file that you previously saved:
+
--
.. Remove the following metadata items from the file:
+
* `creationTimestamp`
* `generation`
* `resourceVersion`
* `uid`

.. Remove the `status` section of the file.
--
+
The resulting file should resemble the following example:
+
.Example `bmh_affected.yaml` file
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  labels:
    installer.openshift.io/role: control-plane
  name: openshift-control-plane-2
  namespace: openshift-machine-api
spec:
  automatedCleaningMode: disabled
  bmc:
    address:
    credentialsName:
    disableCertificateVerification: true
  bootMACAddress: ab:cd:ef:ab:cd:ef
  bootMode: UEFI
  externallyProvisioned: true
  online: true
  rootDeviceHints:
    deviceName: /dev/disk/by-path/pci-0000:04:00.0-nvme-1
  userData:
    name: master-user-data-managed
    namespace: openshift-machine-api
----

. Create the `BareMetalHost` object using the `bmh_affected.yaml` file by running the following command:
+
[source,terminal]
----
$ oc create -f bmh_affected.yaml
----
+
The following warning is expected upon creation of the `BareMetalHost` object:
+
[source,terminal]
----
Warning: metadata.finalizers: "baremetalhost.metal3.io": prefer a domain-qualified finalizer name to avoid accidental conflicts with other finalizer writers
----

. Extract the control plane ignition secret by running the following command:
+
[source,terminal]
----
$ oc extract secret/master-user-data-managed \
    -n openshift-machine-api \
    --keys=userData \
    --to=- \
    | sed '/^userData/d' > new_controlplane.ign
----
+
This command also removes the starting `userData` line of the ignition secret.

. Create an Nmstate YAML file titled `new_controlplane_nmstate.yaml` for the new node's network configuration, using the following example for reference:
+
.Example Nmstate YAML file
[source,yaml]
----
interfaces:
  - name: eno1
    type: ethernet
    state: up
    mac-address: "ab:cd:ef:01:02:03"
    ipv4:
      enabled: true
      address:
        - ip: 192.168.20.11
          prefix-length: 24
      dhcp: false
    ipv6:
      enabled: false
dns-resolver:
  config:
    search:
      - iso.sterling.home
    server:
      - 192.168.20.8
routes:
  config:
  - destination: 0.0.0.0/0
    metric: 100
    next-hop-address: 192.168.20.1
    next-hop-interface: eno1
    table-id: 254
----
+
[NOTE]
====
If you installed your cluster using the Agent-based Installer, you can use the failed node's `networkConfig` section in the `agent-config.yaml` file from the original cluster deployment as a starting point for the new control plane node's Nmstate file. For example, the following command extracts the `networkConfig` section for the first control plane node:

[source,terminal]
----
$ cat agent-config-iso.yaml | yq .hosts[0].networkConfig > new_controlplane_nmstate.yaml
----
====

. Create the customized {op-system-first} live ISO by running the following command:
+
[source,terminal]
----
$ coreos-installer iso customize rhcos-live.86_64.iso \
    --dest-ignition new_controlplane.ign \
    --network-nmstate new_controlplane_nmstate.yaml \
    --dest-device /dev/disk/by-path/<device_path> \
    -f
----
+
Replace `<device_path>` with the path to the target device on which the ISO will be generated.

. Boot the new control plane node with the customized {op-system} live ISO.

. Approve the Certificate Signing Requests (CSR) to join the new node to the cluster.

// Linking the node, bare metal host, and machine together
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="linking-node-machine-bmh_{context}"]
= Linking the node, bare metal host, and machine together

Continue creating the new control plane node by creating a machine and then linking it with the new `BareMetalHost` object and node.

.Procedure

. Get the `providerID` for control plane nodes by running the following command:
+
[source,terminal]
----
$ oc get -n openshift-machine-api baremetalhost -l installer.openshift.io/role=control-plane -ojson | jq -r '.items[] | "baremetalhost:///openshift-machine-api/" + .metadata.name + "/" + .metadata.uid'
----
+
.Example output
[source,terminal]
----
baremetalhost:///openshift-machine-api/master-00/6214c5cf-c798-4168-8c78-1ff1a3cd2cb4
baremetalhost:///openshift-machine-api/master-01/58fb60bd-b2a6-4ff3-a88d-208c33abf954
baremetalhost:///openshift-machine-api/master-02/dc5a94f3-625b-43f6-ab5a-7cc4fc79f105
----

. Get cluster information for labels by running the following command:
+
[source,terminal]
----
$ oc get machine -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machine-role=master \
    -L machine.openshift.io/cluster-api-cluster
----
+
.Example output
[source,terminal]
----
NAME                           PHASE   TYPE  REGION  ZONE  AGE  CLUSTER-API-CLUSTER
ci-op-jcp3s7wx-ng5sd-master-0  Running                     10h  ci-op-jcp3s7wx-ng5sd
ci-op-jcp3s7wx-ng5sd-master-1  Running                     10h  ci-op-jcp3s7wx-ng5sd
ci-op-jcp3s7wx-ng5sd-master-2  Running                     10h  ci-op-jcp3s7wx-ng5sd
----

. Create a `Machine` object for the new control plane node by creating a yaml file similar to the following:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  annotations:
    metal3.io/BareMetalHost: openshift-machine-api/<new_control_plane_machine> <1>
  finalizers:
    - machine.machine.openshift.io
  labels:
    machine.openshift.io/cluster-api-cluster: <cluster_api_cluster> <2>
    machine.openshift.io/cluster-api-machine-role: master
    machine.openshift.io/cluster-api-machine-type: master
  name: <new_control_plane_machine> <1>
  namespace: openshift-machine-api
spec:
  metadata: {}
  providerID: <provider_id> <3>
  providerSpec:
    value:
      apiVersion: baremetal.cluster.k8s.io/v1alpha1
      hostSelector: {}
      image:
        checksum: ""
        url: ""
      kind: BareMetalMachineProviderSpec
      userData:
        name: master-user-data-managed
----
+
--
where:

`<new_control_plane_machine>`:: Specifies the name of the new machine, which can be the same as the previously deleted machine name.
`<cluster_api_cluster>`:: Specifies the `CLUSTER-API-CLUSTER` value  for the other control plane machines, shown in the output of the previous step.
`<provider_id>`:: Specifies the `providerID` value of the new bare metal host, shown in the output of an earlier step.
--
+
The following warning is expected:
+
[source,terminal]
----
Warning: metadata.finalizers: "machine.machine.openshift.io": prefer a domain-qualified finalizer name to avoid accidental conflicts with other finalizer writers
----

. Link the new control plane node and `Machine` object to the `BareMetalHost` object by performing the following steps in a single bash shell session:

.. Define the `NEW_NODE_NAME` variable by running the following command:
+
[source,terminal]
----
$ NEW_NODE_NAME=<new_node_name>
----
+
Replace `<new_node_name>` with the name of the new control plane node.

.. Define the `NEW_MACHINE_NAME` variable by running the following command:
+
[source,terminal]
----
$ NEW_MACHINE_NAME=<new_machine_name>
----
+
Replace `<new_machine_name>` with the name of the new machine.

.. Define the `BMH_UID` by running the following commands to extract it from the new node's `BareMetalHost` object:
+
[source,terminal]
----
$ BMH_UID=$(oc get -n openshift-machine-api bmh $NEW_NODE_NAME -ojson | jq -r .metadata.uid)
----
+
[source,terminal]
----
$ echo $BMH_UID
----

.. Patch the `consumerRef` object into the bare metal host by running the following command:
+
[source,terminal]
----
$ oc patch -n openshift-machine-api bmh $NEW_NODE_NAME --type merge --patch '{"spec":{"consumerRef":{"apiVersion":"machine.openshift.io/v1beta1","kind":"Machine","name":"'$NEW_MACHINE_NAME'","namespace":"openshift-machine-api"}}}'
----

.. Patch the `providerID` value into the new node by running the following command:
+
[source,terminal]
----
$ oc patch node $NEW_NODE_NAME --type merge --patch '{"spec":{"providerID":"baremetalhost:///openshift-machine-api/'$NEW_NODE_NAME'/'$BMH_UID'"}}'
----

.. Review the `providerID` values by running the following command:
+
[source,terminal]
----
$ oc get node -l node-role.kubernetes.io/control-plane -ojson | jq -r '.items[] | .metadata.name + "  " + .spec.providerID'
----

. Set the `BareMetalHost` object's `poweredOn` status to `true` by running the following command:
+
[source,terminal]
----
$ oc patch -n openshift-machine-api bmh $NEW_NODE_NAME --subresource status --type json -p '[{"op":"replace","path":"/status/poweredOn","value":true}]'
----

. Review the `BareMetalHost` object's `poweredOn` status by running the following command:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api -ojson | jq -r '.items[] | .metadata.name + "   PoweredOn:" +  (.status.poweredOn | tostring)'
----

. Review the `BareMetalHost` object's provisioning state by running the following command:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api -ojson | jq -r '.items[] | .metadata.name + "   ProvisioningState:" +  .status.provisioning.state'
----
+
[IMPORTANT]
====
If the provisioning state is not `unmanaged`, change the provisioning state by running the following command:

[source,terminal]
----
$ oc patch -n openshift-machine-api bmh $NEW_NODE_NAME --subresource status --type json -p '[{"op":"replace","path":"/status/provisioning/state","value":"unmanaged"}]'
----
====

. Set the machine's state to `Provisioned` by running the following command:
+
[source,terminal]
----
$ oc patch -n openshift-machine-api machines $NEW_MACHINE_NAME -n openshift-machine-api --subresource status --type json -p '[{"op":"replace","path":"/status/phase","value":"Provisioned"}]'
----

// Adding the new etcd member
// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-replace-control-plane.adoc

[id="add-new-etcd-member_{context}"]
= Adding the new etcd member

Finish adding the new control plane node by adding the new etcd member to the cluster.

.Procedure

. Add the new etcd member to the cluster by performing the following steps in a single bash shell session:

.. Find the IP of the new control plane node by running the following command:
+
[source,terminal]
----
$ oc get nodes -owide -l node-role.kubernetes.io/control-plane
----
+
Make note of the node's IP address for later use.

.. List the etcd pods by running the following command:
+
[source,terminal]
----
$ oc get -n openshift-etcd pods -l k8s-app=etcd -o wide
----

.. Connect to one of the running etcd pods by running the following command. The etcd pod on the new node should be in a `CrashLoopBackOff` state.
+
[source,terminal]
----
$ oc rsh -n openshift-etcd <running_pod>
----
+
Replace `<running_pod>` with the name of a running pod shown in the previous step.

.. View the etcd member list by running the following command:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----

.. Add the new control plane etcd member by running the following command:
+
[source,terminal]
----
sh-4.2# etcdctl member add <new_node> --peer-urls="https://<ip_address>:2380"
----
+
where:

`<new_node>`:: Specifies the name of the new control plane node
`<ip_address>`:: Specifies the IP address of the new node.

.. Exit the rsh shell by running the following command:
+
[source,terminal]
----
sh-4.2# exit
----

. Force an etcd redeployment by running the following command:
+
[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "single-master-recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
----

. Turn the etcd quorum guard back on by running the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

. Monitor the cluster Operator rollout by running the following command:
+
[source,terminal]
----
$ watch oc get co
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready
* Replacing an unhealthy etcd member whose etcd pod is crashlooping
* BareMetalHost reference is missing after adding a host to OpenShift Assisted Installer cluster (Red{nbsp}Hat KCS article)
* How to retrieve Master or Worker Ignition Configuration from OpenShift Container Platform 4? (Red{nbsp}Hat KCS article)
