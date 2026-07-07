---
title: "Deploying {hcp} on OpenStack"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-deploy-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-deploy-openstack
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Deploying {hcp} on OpenStack

[id="hcp-deploy-openstack"]
= Deploying {hcp} on OpenStack

[role="_abstract"]
You can deploy {hcp} with hosted clusters that run on {rh-openstack-first} 17.1.

A _hosted cluster_ is an OpenShift Container Platform cluster with its API endpoint and control plane that are hosted on a management cluster. With {hcp}, control planes exist as pods on a management cluster without the need for dedicated virtual or physical machines for each control plane.

// Module included in the following assemblies:
//
// * hosted_control_planes/hypershift-openstack.adoc

[id="hosted-clusters-openstack-prerequisites_{context}"]
= Prerequisites for OpenStack

[role="_abstract"]
Before you create a hosted cluster on {rh-openstack-first}, ensure that you meet the prerequisites.

* You have administrative access to a management OpenShift Container Platform cluster version 4.17 or greater. This cluster can run on bare metal, {rh-openstack}, or a supported public cloud.
* The HyperShift Operator is installed on the management cluster as specified in "Preparing to deploy hosted control planes".
* The management cluster is configured with OVN-Kubernetes as the default pod network CNI.
* The OpenShift CLI (`oc`) and hosted control planes CLI, `hcp` are installed.
* A load-balancer backend, for example, Octavia, is installed on the management OCP cluster. The load balancer is required for the `kube-api` service to be created for each hosted cluster.
** When ingress is configured with an Octavia load balance, the {rh-openstack} Octavia service is running in the cloud that hosts the guest cluster.
* A valid pull secret file is present for the `quay.io/openshift-release-dev` repository.
* The default external network for the management cluster is reachable from the guest cluster. The `kube-apiserver` load-balancer type service is created on this network.
* If you use a pre-defined floating IP address for ingress, you created a DNS record that points to it for the following wildcard domain: `*.apps.<cluster_name>.<base_domain>`, where:
** `<cluster_name>` is the name of the management cluster.
** `<base_domain>` is the parent DNS domain under which your cluster’s applications live.

[role="additional_resources"]
.Additional resources

* Pull secret

// Module included in the following assemblies:
//
// * hosted_control_planes/hypershift-openstack.adoc

[id="hosted-clusters-openstack-prepare-etcd_{context}"]
= Preparing the management cluster for etcd local storage

[role="_abstract"]
In a {hcp} deployment on {rh-openstack-first}, you can improve etcd performance by using local ephemeral storage that is provisioned with the TopoLVM CSI driver instead of relying on the default Cinder-based Persistent Volume Claims (PVCs).

.Prerequisites

* You have access to a management cluster with HyperShift installed.
* You can create and manage {rh-openstack} flavors and machine sets.
* You have the `oc` and `openstack` CLI tools installed and configured.
* You are familiar with TopoLVM and Logical Volume Manager (LVM) storage concepts.
* You installed the {lvms} Operator on the management cluster. For more information, see "Installing {lvms}
 by using the CLI" in the Storage section of the OpenShift Container Platform documentation.

.Procedure

. Create a Nova flavor with an additional ephemeral disk by using the `openstack` CLI. For example:
+
[source,terminal]
----
$ openstack flavor create \
  --id auto \
  --ram 8192 \
  --disk 0 \
  --ephemeral 100 \
  --vcpus 4 \
  --public \
  hcp-etcd-ephemeral
----
+
[NOTE]
====
Nova automatically attaches the ephemeral disk to the instance and formats it as `vfat` when a server is created with
 that flavor.
====
// Yes, that is the title.
. Create a compute machine set that uses the new flavor. For more information, see "Creating a compute machine set
on OpenStack" in the OpenShift Container Platform documentation.

. Scale the machine set to meet your requirements. If clusters are deployed for high availability, a minimum of 3 workers must be deployed so the pods can be distributed accordingly.

. Label the new worker nodes to identify them for etcd use. For example:
+
[source,terminal]
----
$ oc label node <node_name> hypershift-capable=true
----
+
This label is arbitrary; you can update it later.

. In a file called `lvmcluster.yaml`, create the following `LVMCluster` custom resource to the local storage
configuration for etcd:
+
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: etcd-hcp
  namespace: openshift-storage
spec:
  storage:
    deviceClasses:
    - name: etcd-class
      default: true
      nodeSelector:
         nodeSelectorTerms:
         - matchExpressions:
           - key: hypershift-capable
            operator: In
            values:
            - "true"
      deviceSelector:
        forceWipeDevicesAndDestroyAllData: true
        paths:
        - /dev/vdb
----
+
In this example resource:
+
* The ephemeral disk location is `/dev/vdb`, which is the case in most situations. Verify that this location is true in your case, and note that symlinks are not supported.
* The parameter `forceWipeDevicesAndDestroyAllData` is set to a `True` value because the default Nova ephemeral disk
comes formatted in VFAT.

. Apply the `LVMCluster` resource by running the following command:
+
[source,terminal]
----
oc apply -f lvmcluster.yaml
----

. Verify the `LVMCluster` resource by running the following command:
+
[source,terminal]
----
$ oc get lvmcluster -A
----
+
.Example output
[source,terminal]
----
NAMESPACE           NAME    STATUS
openshift-storage   etcd-hcp   Ready
----

. Verify the `StorageClass` resource by running the following command:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source,terminal]
----
NAME                    PROVISIONER               RECLAIMPOLICY   VOLUMEBINDINGMODE     ALLOWVOLUMEEXPANSION   AGE
lvms-etcd-class         topolvm.io                Delete          WaitForFirstConsumer  true                   23m
standard-csi (default)  cinder.csi.openstack.org  Delete          WaitForFirstConsumer  true                   56m
----
+
You can now deploy a hosted cluster with a performant etcd configuration. The deployment process is described in "Creating a hosted cluster on OpenStack".

// Module included in the following assemblies:
//
// * hosted_control_planes/hypershift-openstack.adoc

[id="hosted-clusters-openstack-create-floating-ip_{context}"]
= Creating a floating IP for ingress

[role="_abstract"]
If you want to make ingress available in a hosted cluster without manual intervention, you can create a floating IP address for it in advance.

.Prerequisites

* You have access to the {rh-openstack-first} cloud.
* If you use a pre-defined floating IP address for ingress, you created a DNS record that points to it for the following wildcard domain: `*.apps.<cluster_name>.<base_domain>`, where:
** `<cluster_name>` is the name of the management cluster.
** `<base_domain>` is the parent DNS domain under which your cluster’s applications live.

.Procedure

* Create a floating IP address by running the following command:
+
[source,terminal]
----
$ openstack floating ip create <external_network_id>
----
+
--
where:

`<external_network_id>`:: Specifies the ID of the external network.
--
+
[NOTE]
====
If you specify a floating IP address by using the `--openstack-ingress-floating-ip` flag without creating it in advance, the `cloud-provider-openstack` component attempts to create it automatically. This process only succeeds if the
 Neutron API policy permits creating a floating IP address with a specific IP address.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy-hcp-deploy-openstack

[id="hosted-clusters-openstack-upload-rhcos_{context}"]
= Uploading the RHCOS image to OpenStack

[role="_abstract"]
If you want to specify the {op-system} image to use when deploying node pools on {hcp} and {rh-openstack-first} deployment, upload the image to the {rh-openstack} cloud.

If you do not upload the image, the OpenStack Resource Controller (ORC) downloads an image from the OpenShift Container Platform mirror and deletes the image after deletion of the hosted cluster.

.Prerequisites

* You downloaded the {op-system} image from the OpenShift Container Platform mirror.
* You have access to your {rh-openstack} cloud.

.Procedure

* Upload an {op-system} image to {rh-openstack} by running the following command:
+
[source,terminal]
----
$ openstack image create --disk-format qcow2 --file <image_file_name> rhcos
----
+
--
where:

`<image_file_name>`:: Specifies the file name of the {op-system} image.
--

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy-hcp-deploy-openstack

[id="hcp-deploy-openstack-create_{context}"]
= Creating a hosted cluster on OpenStack

[role="_abstract"]
You can create a hosted cluster on {rh-openstack-first} by using the `hcp` CLI.

.Prerequisites

* You completed all prerequisite steps in "Preparing to deploy hosted control planes".
* You reviewed "Prerequisites for OpenStack".
* You completed all steps in "Preparing the management cluster for etcd local storage".
* You have access to the management cluster.
* You have access to the {rh-openstack} cloud.

.Procedure

* Create a hosted cluster by running the `hcp create` command. For example, for a cluster that takes advantage of the performant etcd configuration detailed in "Preparing the management cluster for etcd local storage", enter:
+
[source,terminal]
----
$ hcp create cluster openstack \
  --name my-hcp-cluster \
  --openstack-node-flavor m1.xlarge \
  --base-domain example.com \
  --pull-secret /path/to/pull-secret.json \
  --release-image quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64 \
  --node-pool-replicas 3 \
  --etcd-storage-class lvms-etcd-class
----
+
[NOTE]
====
Many options are available at cluster creation. For {rh-openstack}-specific options, see "Options for creating a Hosted Control Planes cluster on OpenStack". For general options, see the `hcp` documentation.
====

.Verification
. Verify that the hosted cluster is ready by running the following command on it:
+
[source,terminal]
----
$ oc -n clusters-<cluster_name> get pods
----
+
--
where:

`<cluster_name>`:: Specifies the name of the cluster.
--
+
After several minutes, the output should show that the hosted control plane pods are running.
+
.Example output
[source,terminal]
----
NAME                                                  READY   STATUS    RESTARTS   AGE
capi-provider-5cc7b74f47-n5gkr                        1/1     Running   0          3m
catalog-operator-5f799567b7-fd6jw                     2/2     Running   0          69s
certified-operators-catalog-784b9899f9-mrp6p          1/1     Running   0          66s
cluster-api-6bbc867966-l4dwl                          1/1     Running   0          66s
...
...
...
redhat-operators-catalog-9d5fd4d44-z8qqk              1/1     Running   0
----

. To validate the etcd configuration of the cluster:

.. Validate the etcd persistent volume claim (PVC) by running the following command:
+
[source,terminal]
----
$ oc get pvc -A
----

.. Inside the {hcp} etcd pod, confirm the mount path and device by running the following command:
+
[source,terminal]
----
$ df -h /var/lib
----
+
[NOTE]
====
The {rh-openstack} resources that the cluster API provider creates are tagged with the label `openshiftClusterID=<infraID>`.

You can define additional tags for the resources as values in the `HostedCluster.Spec.Platform.OpenStack.Tags` field of a YAML manifest that you use to create the hosted cluster. After you scale up the node pool, the tags apply to resources.
====

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-openstack.adoc

[id="hcp-deploy-openstack-parameters_{context}"]
= Options for creating a Hosted Control Planes cluster on OpenStack

[role="_abstract"]
You can supply several options to the `hcp` CLI while deploying a Hosted Control Planes Cluster on {rh-openstack-first}.

|===
|Option|Description|Required

|`--openstack-ca-cert-file`
|Path to the OpenStack CA certificate file. If not provided, this will be automatically extracted from the cloud entry in `clouds.yaml`.
|No

|`--openstack-cloud`
|Name of the cloud entry in `clouds.yaml`. The default value is `openstack`.
|No

|`--openstack-credentials-file`
a|Path to the OpenStack credentials file. If not provided, `hcp` will search the following directories:

* The current working directory
* `$HOME/.config/openstack`
* `/etc/openstack`

|No

|`--openstack-dns-nameservers`
|List of DNS server addresses that are provided when creating the subnet.
|No

|`--openstack-external-network-id`
|ID of the OpenStack external network.
|No

|`--openstack-ingress-floating-ip`
|A floating IP for OpenShift ingress.
|No

|`--openstack-node-additional-port`
|Additional ports to attach to nodes. Valid values are: `network-id`, `vnic-type`, `disable-port-security`, and `address-pairs`.
|No

|`--openstack-node-availability-zone`
|Availability zone for the node pool.
|No

|`--openstack-node-flavor`
|Flavor for the node pool.
|Yes

|`--openstack-node-image-name`
|Image name for the node pool.
|No
|===
