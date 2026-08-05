---
title: "Deploying {hcp} on non-bare-metal agent machines"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-deploy-non-bm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-deploy-non-bm
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Deploying {hcp} on non-bare-metal agent machines

[id="hcp-deploy-non-bm"]
= Deploying {hcp} on non-bare-metal agent machines

[role="_abstract"]
To maintain infrastructure flexibility while using existing virtualization layers, you can deploy {hcp} on non-bare-metal Agent machines. You can use the management benefits of the Agent platform when running on virtualized environments or other cloud-based virtual machines.

You can deploy {hcp} by configuring a cluster to function as a hosting cluster. The hosting cluster is an OpenShift Container Platform cluster where the control planes are hosted. The hosting cluster is also known as the management cluster.

[NOTE]
====
The management cluster is not the same thing as the _managed_ cluster. A managed cluster is a cluster that the hub cluster manages.
====

The {hcp} feature is enabled by default.

The {mce-short} supports only the default `local-cluster` managed hub cluster. On {rh-rhacm-first} 2.10, you can use the `local-cluster` managed hub cluster as the hosting cluster.

A _hosted cluster_ is an OpenShift Container Platform cluster with its API endpoint and control plane that are hosted on the hosting cluster. The hosted cluster includes the control plane and its corresponding data plane. You can use the {mce-short} console or the `hcp` command-line interface (CLI) to create a hosted cluster.

The hosted cluster is automatically imported as a managed cluster. If you want to disable this automatic import feature, see "Disabling the automatic import of hosted clusters into {mce-short}".

[role="_additional-resources"]
.Additional resources

* Disabling the automatic import of hosted clusters into {mce-short}

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-prepare_{context}"]
= Preparing to deploy {hcp} on non-bare-metal agent machines

[role="_abstract"]
Before you deploy {hcp} on non-bare-metal agent machines, ensure that you understand requirements for the deployment.

* You can add agent machines as a worker node to a hosted cluster by using the Agent platform. Agent machine represents a host booted with a Discovery Image and ready to be provisioned as an OpenShift Container Platform node. The Agent platform is part of the central infrastructure management service. For more information, see "Enabling the central infrastructure management service".

* All hosts that are not bare metal require a manual boot with a Discovery Image ISO that the central infrastructure management provides.

* When you scale up the node pool, a machine is created for every replica. For every machine, the Cluster API provider finds and installs an Agent that is approved, is passing validations, is not currently in use, and meets the requirements that are specified in the node pool specification. You can monitor the installation of an Agent by checking its status and conditions.

* When you scale down a node pool, Agents are unbound from the corresponding cluster. Before you can reuse the Agents, you must restart them by using the Discovery image.

* When you configure storage for {hcp}, consider the recommended etcd practices. To ensure that you meet the latency requirements, dedicate a fast storage device to all {hcp} etcd instances that run on each control-plane node. You can use LVM storage to configure a local storage class for hosted etcd pods. For more information, see "Recommended etcd practices" and "Persistent storage using logical volume manager storage" in the OpenShift Container Platform documentation.

[role="_additional-resources"]
.Additional resources

* Enabling the central infrastructure management service ({rh-rhacm-title} documentation)
* Recommended etcd practices
* Persistent storage using logical volume manager storage

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-prereqs_{context}"]
= Prerequisites for deploying {hcp} on non-bare-metal agent machines

[role="_abstract"]
Before you deploy {hcp} on non-bare-metal agent machines, ensure you meet the prerequisites.

* You must have {mce} 2.5 or later installed on an OpenShift Container Platform cluster. You can install the {mce-short} as an Operator from the OpenShift Container Platform software catalog.

* You must have at least one managed OpenShift Container Platform cluster for the {mce-short}. The `local-cluster` management cluster is automatically imported. For more information about the `local-cluster`, see "Advanced configuration" in the {rh-rhacm-title} documentation. You can check the status of your management cluster by running the following command:
+
[source,terminal]
----
$ oc get managedclusters local-cluster
----

* You have enabled central infrastructure management. For more information, see "Enabling the central infrastructure management service" in the {rh-rhacm-title} documentation.

* You have installed the `hcp` command-line interface.

* Your hosted cluster has a cluster-wide unique name.

* You are running the management cluster and workers on the same infrastructure.

[role="_additional-resources"]
.Additional resources

* Advanced configuration ({rh-rhacm-title} documentation)

* Enabling the central infrastructure management service ({rh-rhacm-title} documentation)

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-firewall-port-svc-reqs_{context}"]
= Firewall, port, and service requirements for non-bare-metal agent machines

[role="_abstract"]
You must meet the firewall and port requirements so that ports can communicate between the management cluster, the control plane, and hosted clusters.

[NOTE]
====
Services run on their default ports. However, if you use the `NodePort` publishing strategy, services run on the port that is assigned by the `NodePort` service.
====

Use firewall rules, security groups, or other access controls to restrict access to only required sources. Avoid exposing ports publicly unless necessary. For production deployments, use a load balancer to simplify access through a single IP address.

A hosted control plane exposes the following services on non-bare-metal agent machines:

* `APIServer`

** The `APIServer` service runs on port 6443 by default and requires ingress access for communication between the control plane components.
** If you use MetalLB load balancing, allow ingress access to the IP range that is used for load balancer IP addresses.

* `OAuthServer`

** The `OAuthServer` service runs on port 443 by default when you use the route and ingress to expose the service.
** If you use the `NodePort` publishing strategy, use a firewall rule for the `OAuthServer` service.

* `Konnectivity`

** The `Konnectivity` service runs on port 443 by default when you use the route and ingress to expose the service.
** The `Konnectivity` agent establishes a reverse tunnel to allow the control plane to access the network for the hosted cluster. The agent uses egress to connect to the `Konnectivity` server. The server is exposed by using either a route on port 443 or a manually assigned `NodePort`.
** If the cluster API server address is an internal IP address, allow access from the workload subnets to the IP address on port 6443.
** If the address is an external IP address, allow egress on port 6443 to that external IP address from the nodes.

* `Ignition`

** The `Ignition` service runs on port 443 by default when you use the route and ingress to expose the service.
** If you use the `NodePort` publishing strategy, use a firewall rule for the `Ignition` service.

You do not need the following services on non-bare-metal agent machines:

* `OVNSbDb`
* `OIDC`

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-infra-reqs_{context}"]
= Infrastructure requirements for non-bare-metal agent machines

[role="_abstract"]
The Agent platform does not create any infrastructure, but it has several requirements.

* Agents: An _Agent_ represents a host that is booted with a discovery image and is ready to be provisioned as an OpenShift Container Platform node.

* DNS: The API and ingress endpoints must be routable.

[role="_additional-resources"]
.Additional resources

* Recommended etcd practices

* Persistent storage using logical volume manager storage

* Disabling the automatic import of hosted clusters into {mce-short}

* Manually enabling the {hcp} feature

* Disabling the {hcp} feature

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-dns_{context}"]
= DNS configuration on non-bare-metal agent machines

[role="_abstract"]
The API Server for the hosted cluster is exposed as a `NodePort` service. A DNS entry must exist for `api.<hosted_cluster_name>.<basedomain>` that points to destination where the API Server can be reached.

The DNS entry can be as simple as a record that points to one of the nodes in the managed cluster that is running the hosted control plane. The entry can also point to a load balancer that is deployed to redirect incoming traffic to the ingress pods.

The following examples show how to configure DNS for specific environments.

.Example DNS configuration for a connected environment on an IPv4 network
[source,text]
----
api.example.krnl.es.        IN A 192.168.122.20
api.example.krnl.es.        IN A 192.168.122.21
api.example.krnl.es.        IN A 192.168.122.22
api-int.example.krnl.es.    IN A 192.168.122.20
api-int.example.krnl.es.    IN A 192.168.122.21
api-int.example.krnl.es.    IN A 192.168.122.22
`*`.apps.example.krnl.es.   IN A 192.168.122.23
----

.Example DNS configuration for a disconnected environment on an IPv6 network
[source,text]
----
api.example.krnl.es.        IN A 2620:52:0:1306::5
api.example.krnl.es.        IN A 2620:52:0:1306::6
api.example.krnl.es.        IN A 2620:52:0:1306::7
api-int.example.krnl.es.    IN A 2620:52:0:1306::5
api-int.example.krnl.es.    IN A 2620:52:0:1306::6
api-int.example.krnl.es.    IN A 2620:52:0:1306::7
`*`.apps.example.krnl.es.   IN A 2620:52:0:1306::10
----

.Example DNS configuration for a disconnected environment on a dual stack network
[source,text]
----
host-record=api-int.hub-dual.dns.base.domain.name,192.168.126.10
host-record=api.hub-dual.dns.base.domain.name,192.168.126.10
address=/apps.hub-dual.dns.base.domain.name/192.168.126.11
dhcp-host=aa:aa:aa:aa:10:01,ocp-master-0,192.168.126.20
dhcp-host=aa:aa:aa:aa:10:02,ocp-master-1,192.168.126.21
dhcp-host=aa:aa:aa:aa:10:03,ocp-master-2,192.168.126.22
dhcp-host=aa:aa:aa:aa:10:06,ocp-installer,192.168.126.25
dhcp-host=aa:aa:aa:aa:10:07,ocp-bootstrap,192.168.126.26

host-record=api-int.hub-dual.dns.base.domain.name,2620:52:0:1306::2
host-record=api.hub-dual.dns.base.domain.name,2620:52:0:1306::2
address=/apps.hub-dual.dns.base.domain.name/2620:52:0:1306::3
dhcp-host=aa:aa:aa:aa:10:01,ocp-master-0,[2620:52:0:1306::5]
dhcp-host=aa:aa:aa:aa:10:02,ocp-master-1,[2620:52:0:1306::6]
dhcp-host=aa:aa:aa:aa:10:03,ocp-master-2,[2620:52:0:1306::7]
dhcp-host=aa:aa:aa:aa:10:06,ocp-installer,[2620:52:0:1306::8]
dhcp-host=aa:aa:aa:aa:10:07,ocp-bootstrap,[2620:52:0:1306::9]
----

For this configuration, be sure to include DNS entries for both IPv4 and IPv6.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.adoc

[id="hcp-custom-dns_{context}"]
= Defining a custom DNS name

[role="_abstract"]
As a cluster administrator, you can create a hosted cluster with an external API DNS name that differs from the internal endpoint that gets used for node bootstraps and control plane communication.

You might want to define a different DNS name for the following reasons:

* To replace the user-facing TLS certificate with one from a public CA without breaking the control plane functions that bind to the internal root CA
* To support split-horizon DNS and NAT scenarios
* To ensure a similar experience to standalone control planes, where you can use functions, such as the `Show Login Command` function, with the correct `kubeconfig` and DNS configuration

You can define a DNS name either during your initial setup or during postinstallation operations, by entering a domain name in the `kubeAPIServerDNSName` parameter of a `HostedCluster` object.

.Prerequisites

* You have a valid TLS certificate that covers the DNS name that you set in the `kubeAPIServerDNSName` parameter.
* You have a resolvable DNS name URI that can reach and point to the correct address.

.Procedure

* In the specification for the `HostedCluster` object, add the `kubeAPIServerDNSName` parameter and the address for the domain and specify which certificate to use, as shown in the following example:
+
[source,yaml]
----
#...
spec:
  configuration:
    apiServer:
      servingCerts:
        namedCertificates:
        - names:
          - xxx.example.com
          - yyy.example.com
          servingCertificate:
            name: <my_serving_certificate>
  kubeAPIServerDNSName: <custom_address>
----
+
The value for the `kubeAPIServerDNSName` parameter must be a valid and addressable domain.
+
After you define the `kubeAPIServerDNSName` parameter and specify the certificate, the Control Plane Operator controllers create a `kubeconfig` file named `custom-admin-kubeconfig`, where the file gets stored in the `HostedControlPlane` namespace. The generation of certificates happen from the root CA, and the `HostedControlPlane` namespace manages their expiration and renewal.
+
The Control Plane Operator reports a new `kubeconfig` file named `CustomKubeconfig` in the `HostedControlPlane` namespace. That file uses the defined new server in the `kubeAPIServerDNSName` parameter.
+
A reference for the custom `kubeconfig` file exists in the `status` parameter as `CustomKubeconfig` of the `HostedCluster` object. The `CustomKubeConfig` parameter is optional, and you can add the parameter only if the `kubeAPIServerDNSName` parameter is not empty. After you set the `CustomKubeConfig` parameter, the parameter triggers the generation of a secret named `<hosted_cluster_name>-custom-admin-kubeconfig` in the `HostedCluster` namespace. You can use the secret to access the `HostedCluster` API server. If you remove the `CustomKubeConfig` parameter during postinstallation operations, deletion of all related secrets and status references occur.
+
[NOTE]
====
Defining a custom DNS name does not directly impact the data plane, so no expected rollouts occur. The `HostedControlPlane` namespace receives the changes from the HyperShift Operator and deletes the corresponding parameters.
====
+
If you remove the `kubeAPIServerDNSName` parameter from the specification for the `HostedCluster` object, all newly generated secrets and the `CustomKubeconfig` reference are removed from the cluster and from the `status` parameter.

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-hc_{context}"]
= Creating a hosted cluster on non-bare-metal agent machines by using the CLI

[role="_abstract"]
When you create a hosted cluster with the Agent platform, the HyperShift Operator installs the Agent Cluster API provider in the hosted control plane namespace. You can create a hosted cluster on bare metal or import one.

[NOTE]
====
* Each hosted cluster must have a cluster-wide unique name. A hosted cluster name cannot be the same as any existing managed cluster in order for {mce-short} to manage it.

* Do not use `clusters` as a hosted cluster name.

* A hosted cluster cannot be created in the namespace of a {mce-short} managed cluster.
====

.Procedure

. Create the hosted control plane namespace by entering the following command:
+
[source,terminal]
----
$ oc create ns <hosted_cluster_namespace>-<hosted_cluster_name>
----
+
Replace `<hosted_cluster_namespace>` with your hosted cluster namespace name, for example, `my-hosted-cluster-namespace`. Replace `<hosted_cluster_name>` with your hosted cluster name.

. Create a hosted cluster by entering the following command:
+
[source,terminal]
----
$ hcp create cluster agent \
  --name=my-hosted-cluster \
  --pull-secret=/user/name/pullsecret \
  --agent-namespace=clusters-example \
  --base-domain=krnl.es \
  --api-server-address=api.my-hosted-cluster.krnl.es \
  --etcd-storage-class=lvm-storageclass \
  --ssh-key ~/.ssh/id_rsa.pub \
  --namespace my-hosted-cluster-namespace \
  --control-plane-availability-policy HighlyAvailable \
  --release-image=quay.io/openshift-release-dev/ocp-release:4.22.0-multi \
  --node-pool-replicas 3
----
+
* `--name` specifies the name of your hosted cluster.
* `--pull-secret` specifies the path to your pull secret.
* `--agent-namespace` specifies your hosted control plane namespace. Ensure that agents are available in this namespace by using the `oc get agent -n <hosted-control-plane-namespace>` command.
* `--base-domain` specifies your base domain.
* `--api-server-address` The `--api-server-address` flag defines the IP address that is used for the Kubernetes API communication in the hosted cluster. If you do not set the `--api-server-address` flag, you must log in to connect to the management cluster.
* `--etcd-storage-class` specifies the etcd storage class name. Verify that you have a default storage class configured for your cluster. Otherwise, you might end up with pending PVCs.
* `--ssh_key` specifies the path to your SSH public key. The default file path is `~/.ssh/id_rsa.pub`.
* `--namespace` specifies your hosted cluster namespace.
* `--control-plane-availability-policy` specifies the availability policy for the hosted control plane components. Supported options are `SingleReplica` and `HighlyAvailable`. The default value is `HighlyAvailable`.
* `--release-image` specifies the supported OpenShift Container Platform version that you want to use.
* `--node-pool-replicas` specifies the node pool replica count. You must specify the replica count as `0` or greater to create the same number of replicas. Otherwise, no node pools are created.

.Verification

* After a few moments, verify that your hosted control plane pods are up and running by entering the following command:
+
[source,terminal]
----
$ oc -n <hosted_cluster_namespace>-<hosted_cluster_name> get pods
----
+
.Example output
[source,terminal]
----
NAME                                             READY   STATUS    RESTARTS   AGE
catalog-operator-6cd867cc7-phb2q                 2/2     Running   0          2m50s
control-plane-operator-f6b4c8465-4k5dh           1/1     Running   0          4m32s
----

[role="_additional-resources"]
.Additional resources

* Manually importing a hosted cluster

* Configuring a custom API server certificate in a hosted cluster

* Adding hosts to the host inventory by using the Discovery Image ({rh-rhacm-title} documentation)

* Extracting the release image digest

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-hc-console_{context}"]
= Creating a hosted cluster on non-bare-metal agent machines by using the web console

[role="_abstract"]
You can create a hosted cluster on non-bare-metal agent machines by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Open the OpenShift Container Platform web console and log in by entering your administrator credentials.

. In the console header, select **All Clusters**.

. Click **Infrastructure -> Clusters**.

. Click **Create cluster  Host inventory -> Hosted control plane**.
+
The **Create cluster** page is displayed.

. On the **Create cluster** page, follow the prompts to enter details about the cluster, node pools, networking, and automation.
+
As you enter details about the cluster, you might find the following tips useful:

* If you want to use predefined values to automatically populate fields in the console, you can create a host inventory credential. For more information, see _Creating a credential for an on-premises environment_.

* On the *Cluster details* page, the pull secret is your OpenShift Container Platform pull secret that you use to access OpenShift Container Platform resources. If you selected a host inventory credential, the pull secret is automatically populated.

* On the *Node pools* page, the namespace contains the hosts for the node pool. If you created a host inventory by using the console, the console creates a dedicated namespace.

* On the *Networking* page, you select an API server publishing strategy. The API server for the hosted cluster can be exposed either by using an existing load balancer or as a service of the `NodePort` type. A DNS entry must exist for the `api.<hosted_cluster_name>.<basedomain>` setting that points to the destination where the API server can be reached. This entry can be a record that points to one of the nodes in the management cluster or a record that points to a load balancer that redirects incoming traffic to the Ingress pods.

. Review your entries and click **Create**.
+
The **Hosted cluster** view is displayed.

. Monitor the deployment of the hosted cluster in the **Hosted cluster** view. If you do not see information about the hosted cluster, ensure that **All Clusters** is selected, and click the cluster name. Wait until the control plane components are ready. This process can take a few minutes.

. To view the node pool status, scroll to the **NodePool** section. The process to install the nodes takes about 10 minutes. You can also click **Nodes** to confirm whether the nodes joined the hosted cluster.

[role="_additional-resources"]
.Additional resources

* Creating a credential for an on-premises environment ({rh-rhacm-title} documentation)

* Accessing the web console

* Configuring a custom API server certificate in a hosted cluster

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-hc-mirror_{context}"]
= Creating a hosted cluster on non-bare-metal agent machines by using a mirror registry

[role="_abstract"]
You can use a mirror registry to create a hosted cluster on non-bare-metal agent machines by specifying the `--image-content-sources` flag in the `hcp create cluster` command.

.Procedure

. Create a YAML file to define Image Content Source Policies (ICSP). See the following example:
+
[source,yaml]
----
- mirrors:
  - brew.registry.redhat.io
  source: registry.redhat.io
- mirrors:
  - brew.registry.redhat.io
  source: registry.stage.redhat.io
- mirrors:
  - brew.registry.redhat.io
  source: registry-proxy.engineering.redhat.com
----

. Save the file as `icsp.yaml`. This file contains your mirror registries.

. To create a hosted cluster by using your mirror registries, run the following command:
+
[source,terminal]
----
$ hcp create cluster agent \
    --name=my-hosted-cluster \
    --pull-secret=/user/name/pullsecret\
    --agent-namespace=clusters-example \
    --base-domain=krnl.es \
    --api-server-address=api.my-hosted-cluster.krnl.es \
    --image-content-sources icsp.yaml  \
    --ssh-key  ~/.ssh/id_rsa.pub \
    --namespace my-hosted-cluster-namespace \
    --release-image=quay.io/openshift-release-dev/ocp-release:4.22.0-multi
----
+
* `--name` specifies the name of your hosted cluster.
* `--pull-secret` specifies the path to your pull secret.
* `--agent-namespace` specifies your hosted control plane namespace. Ensure that agents are available in this namespace by using the `oc get agent -n <hosted-control-plane-namespace>` command.
* `--base-domain` specifies your base domain.
* `--api-server-address` defines the IP address that is used for the Kubernetes API communication in the hosted cluster. If you do not set the `--api-server-address` flag, you must log in to connect to the management cluster.
* `--image-content-sources` specifies the `icsp.yaml` file that defines ICSP and your mirror registries.
* `--ssh-key` specifies the path to your SSH public key. The default file path is `~/.ssh/id_rsa.pub`.
* `--namespace` specifies your hosted cluster namespace.
* `--release-image` specifies the supported OpenShift Container Platform version that you want to use. If you are using a disconnected environment, replace the version with the digest image. To extract the OpenShift Container Platform release image digest, see "Extracting the OpenShift Container Platform release image digest".

[role="_additional-resources"]
.Additional resources

* Accessing the hosted cluster

* Configuring a custom API server certificate in a hosted cluster

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-non-bm.adoc

[id="hcp-non-bm-verify_{context}"]
= Verifying hosted cluster creation on non-bare-metal agent machines

[role="_abstract"]
After the deployment process is complete, you can verify that the hosted cluster was created successfully.

Follow these steps a few minutes after you create the hosted cluster.

.Procedure

. Obtain the `kubeconfig` file for your new hosted cluster by entering the following command:
+
[source,terminal]
----
$ oc extract -n <hosted_cluster_namespace> \
  secret/<hosted_cluster_name>-admin-kubeconfig --to=- \
  > kubeconfig-<hosted_cluster_name>
----

. Use the `kubeconfig` file to view the cluster Operators of the hosted cluster. Enter the following command:
+
[source,terminal]
----
$ oc get co --kubeconfig=kubeconfig-<hosted_cluster_name>
----
+
.Example output
[source,terminal]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
console                                    4.10.26   True        False         False      2m38s
csi-snapshot-controller                    4.10.26   True        False         False      4m3s
dns                                        4.10.26   True        False         False      2m52s
----

. View the running pods on your hosted cluster by entering the following command:
+
[source,terminal]
----
$ oc get pods -A --kubeconfig=kubeconfig-<hosted_cluster_name>
----
+
.Example output
[source,terminal]
----
NAMESPACE                                          NAME                                                      READY   STATUS             RESTARTS        AGE
kube-system                                        konnectivity-agent-khlqv                                  0/1     Running            0               3m52s
openshift-cluster-samples-operator                 cluster-samples-operator-6b5bcb9dff-kpnbc                 2/2     Running            0               20m
openshift-monitoring                               alertmanager-main-0                                       6/6     Running            0               100s
openshift-monitoring                               openshift-state-metrics-677b9fb74f-qqp6g                  3/3     Running            0               104s
----
