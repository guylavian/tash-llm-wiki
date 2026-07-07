---
title: "Networking for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-networking
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-networking
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Networking for {hcp}

[id="hcp-networking"]
= Networking for {hcp}

[role="_abstract"]
Ensure optimal performance with {hcp} by configuring network settings. Those settings include internal subnets and proxy support for control-plane workloads, compute nodes, management clusters, and hosted clusters.

//hcp isolation overview
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-isolation-overview_{context}"]
= Network isolation for hosted clusters

[role="_abstract"]
To provide distinct, secure environments for multiple hosted clusters that share the same management cluster, you can configure hosted clusters with specific network and virtual machine (VM) isolation levels.

For hosted clusters, network isolation levels include container-based isolation, VM-based isolation, and physical isolation:

Container-based isolation:: With container-based isolation, you use shared compute nodes, and isolation is enforced by policy, namespaces, and control group or SELinux boundaries. Control-plane components run as pods on the management cluster, isolated mainly by Kubernetes or Linux mechanisms, not by giving each hosted cluster its own VM or server. Each control plane runs in a dedicated namespace, with default-deny networking and a network policy that allows only defined traffic. Pods use the restricted security context constraint, with unique identifiers (UIDs) scoped for each namespace.

VM-based isolation:: With VM-based isolation, you run hosted control plane pods inside VMs; for example, on {VirtProductName}. This type of isolation is useful if you require VM-based isolation over container-based isolation for a multitenant management cluster. You add a hypervisor boundary between hosted clusters that share a management cluster. Control plane pods are pinned to dedicated VMs.
+
To achieve VM-based isolation, you follow a "shared-nothing" approach, where each control plane has its own dedicated node. The management cluster must be an OpenShift Container Platform cluster on a VM so that the VM compute nodes can be used with the "shared-nothing" annotations to dedicate them to specific hosted control planes. Those hosted control planes will not share kernel space with control planes from other hosted clusters that are on the same management cluster.

Physical isolation:: With physical isolation, you also follow a "shared-nothing" approach. Nodes for a specific hosted cluster are tainted and labeled with a specific `hypershift.openshift.io/hosted-cluster` value. Security involves the use of a network policy and physical network access control lists (ACLs) across hosted clusters.

For more information, see "Control plane isolation" and "Distributing hosted cluster workloads".

[role="_additional-resources"]
.Additional resources
 * Control plane isolation
 * Node labeling for {hcp}

//control plane isolation
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-prepare/hcp-distribute-workloads.adoc
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-isolation_{context}"]
= Control plane isolation

[role="_abstract"]
You can configure {hcp} to isolate network traffic or control plane pods.

Each hosted control plane is assigned to run in a dedicated Kubernetes namespace. By default, the Kubernetes namespace denies all network traffic.

The following network traffic is allowed through the network policy that is enforced by the Kubernetes Container Network Interface (CNI):

* Ingress pod-to-pod communication in the same namespace (intra-tenant)
* Ingress on port 6443 to the hosted `kube-apiserver` pod for the tenant
* Metric scraping from the management cluster Kubernetes namespace with the `network.openshift.io/policy-group: monitoring` label is allowed for monitoring

[id="hcp-cp-pod-isolation_{context}"]
== Control plane pod isolation

In addition to network policies, each hosted control plane pod is run with the `restricted` security context constraint. This policy denies access to all host features and requires pods to be run with a unique identifier (UID) and with SELinux context that is allocated uniquely to each namespace that hosts a customer control plane.

The policy ensures the following constraints:

* Pods cannot run as privileged.
* Pods cannot mount host directory volumes.
* Pods must run as a user in a pre-allocated range of UIDs.
* Pods must run with a pre-allocated Multi-Category Security (MCS) label.
* Pods cannot access the host network namespace.
* Pods cannot expose host network ports.
* Pods cannot access the host PID namespace.
* By default, pods drop the following Linux capabilities: `KILL`, `MKNOD`, `SETUID`, and `SETGID`.

The management components, such as `kubelet` and `crio`, on each management cluster worker node are protected by an SELinux label that is not accessible to the SELinux context for pods that support {hcp}.

The following SELinux labels are used for key processes and sockets:

`kubelet`:: `system_u:system_r:unconfined_service_t:s0`
`crio`:: `system_u:system_r:container_runtime_t:s0`
`crio.sock`:: `system_u:object_r:container_var_run_t:s0`
`<example user container processes>`:: `system_u:system_r:container_t:s0:c14,c24`

To achieve physical or virtual machine (VM) isolation, you need to use a "shared-nothing" approach, where each control plane has its own dedicated node. Nodes for a specific hosted cluster are tainted and labeled with a specific `hypershift.openshift.io/hosted-cluster` value. Security involves the use of a network policy and physical network access control lists (ACLs) across hosted clusters.

//ingress and egress for hcp
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-ingress-egress-reqs_{context}"]
= Ingress and egress requirements for {hcp}

[role="_abstract"]
Specific network ports must be open for communication between the management cluster, the {hcp} components, and the compute nodes. The ports are categorized into ingress ports, which involve incoming traffic to {hcp} and egress ports, which involve outgoing traffic from {hcp}.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-ingress-reqs_{context}"]
= Ingress requirements for {hcp}

[role="_abstract"]
Ingress ports involve incoming traffic to {hcp}. Ensure the correct ports are open for communication between the management cluster, the {hcp} components, and the compute nodes.

The following table details the ports for incoming traffic to {hcp} across all platforms:

.Common ingress ports
[cols="5",options="header"]
|===

|Port |Protocol |Service |Description |Code reference

|`6443`
|TCP
|Kubernetes API server
|Primary API server port for `kubectl` and cluster communication
|`support/config/constants.go:35` - `KASSVCPort = 6443`

|`9090`
|TCP
|Ignition server
|Port from compute nodes during the bootstrap process, `NodePort` or `Route` service publishing strategy
|-

|===

The service publishing strategy determines additional ports. The `Ignition Proxy` and `Konnectivity` services are exposed through one of the following service publishing strategies:

`Route`:: This setting is the default on OpenShift Container Platform. Traffic flows through the OpenShift router on port 443. No additional firewall rules are needed beyond standard HTTPS.
`NodePort`:: Direct access is required to port 8091 (Konnectivity) and port 8443 (Ignition Proxy).
`LoadBalancer`:: Direct access is required to port 8091 (Konnectivity) through the cloud load balancer.

The following table details the ingress port configurations that are specific to each platform:

.Platform-specific ingress port configurations
[cols="5",options="header"]
|===

|Platform |Port |Service |Description |Code reference

|Agent
|`8443`
|Ignition Proxy
|HTTPS proxy for ignition content delivery (`NodePort` publishing)
|`hypershift-operator/controllers/hostedcluster/network_policies.go:390`

|Agent
|`8081`
|Agent CAPI health probe
|Health check endpoint for Agent platform CAPI provider
|`hypershift-operator/controllers/hostedcluster/internal/platform/agent.go:96,105,115`

|Agent
|`8080`
|Agent CAPI metrics
|Metrics endpoint for Agent platform CAPI provider (binds to localhost only)
|`hypershift-operator/controllers/hostedcluster/internal/platform/agent/agent.go:97`

|{aws-short}
|`9440`
|CAPI health check
|Health and readiness probe endpoint for {aws-short} CAPI provider
|`hypershift-operator/controllers/hostedcluster/internal/platform/aws/aws.go:222-223`

|Bare metal without the Agent platform
|`8443`
|Ignition Proxy
|HTTPS proxy for ignition content delivery (`NodePort` publishing)
|-

|KubeVirt
|`9440`
|CAPI health check
|Health and readiness probe endpoint
|`hypershift-operator/controllers/hostedcluster/internal/platform/kubevirt/kubevirt.go:140`

|{rh-openstack} (Technology Preview)
|`9440`
|CAPI health check
|Health and readiness probe endpoint
|`hypershift-operator/controllers/hostedcluster/internal/platform/openstack/openstack.go:238`

|{rh-openstack} (Technology Preview)
|`8081`
|ORC health check
|Health and readiness probe endpoint for OpenStack Resource Controller
|`hypershift-operator/controllers/hostedcluster/internal/platform/openstack/openstack.go:294,311`

|===

The following table details the ingress port configurations for private clusters, such as those on {aws-short}:

.Ingress port configurations for private clusters
[cols="4",options="header"]
|===

|Port |Service |Description |Code reference

|`8080`
|Private router HTTP
|HTTP traffic through the private router
|`hypershift-operator/controllers/hostedcluster/network_policies.go:244`

|`8443`
|Private router HTTPS
|HTTPS traffic through the private router
|`hypershift-operator/controllers/hostedcluster/network_policies.go:245`

|===

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-egress-reqs_{context}"]
= Egress requirements for {hcp}

[role="_abstract"]
Egress ports involve outgoing traffic from {hcp}. Ensure the correct ports are open for communication between the management cluster, the {hcp} components, and the compute nodes.

The following table details the ports that must be accessible for outgoing traffic from {hcp}, across all platforms.

.Common egress ports
[cols="1,2,2,4",options="header"]
|===

|Port |Protocol |Service |Purpose

|`443`
|TCP
|HTTPS
|OLM images, `Ignition` content, external HTTPS services

|`6443`
|TCP
|Kubernetes API server
|Communication with management cluster API

|`53`
|TCP and UDP
|DNS
|Standard DNS queries

|===

Compute nodes require outbound network access to several {hcp} services. The following table details the egress requirements for compute nodes.

.Compute node egress requirements
[cols="1,1,1,4,4",options="header"]
|===

|Port |Protocol |Service |Purpose |When required

|`443`
|TCP
|HTTPS
|Container registries, `Ignition` or `Konnectivity` service via `Route` service publishing strategy, external HTTPS services
|Always

|`6443`
|TCP
|Kubernetes API server
|Cluster management and kubelet communication
|Always

|`8091`
|TCP
|Konnectivity server
|Establishes a reverse tunnel for control plane access
|`NodePort` or `LoadBalancer` publishing only

|`8443`
|TCP
|Ignition Proxy
|Retrieves bootstrap configuration
|`NodePort` publishing only for Agent platform or bare metal

|`53`
|TCP and UDP
|DNS
|Name resolution
|Always

|===

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-ingress-egress-example_{context}"]
= Example firewall configuration

[role="_abstract"]
Review an example of what the firewall configuration looks like for a typical {hcp} on {aws-short} deployment that uses `Route` service publishing.

Ingress rules::

* Port `6443`/TCP: Kubernetes API server, from compute nodes and external clients
* Port `443`/TCP: OpenShift Router for Ignition or Konnectivity routes, from compute nodes

Egress rules::

* Port `443`/TCP: HTTPS, to container registries, routes, and external services
* Port `6443`/TCP: Management cluster API, to management cluster
* Port `53`/TCP and UDP: DNS, to DNS servers

If you use `NodePort` or `LoadBalancer` service publishing instead of `Route` service publishing, the following rules apply:

* Port `8091`/TCP: Konnectivity server, from compute nodes
* Port `8443`/TCP: Ignition Proxy, from compute nodes during the bootstrap process, `NodePort` publishing strategy only
* Port `9090`/TCP: Ignition server, from compute nodes during the bootstrap process, `NodePort` publishing strategy only

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-bm.adoc
// * hosted_control_planes/hcp-manage/hcp-manage-non-bm.adoc
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-bm-ingress_{context}"]
= Handling ingress in a hosted cluster on bare metal

= Handling ingress in a hosted cluster on non-bare-metal agent machines

Every OpenShift Container Platform cluster has a default application Ingress Controller that typically has an external DNS record associated with it. For example, if you create a hosted cluster named `example` with the base domain `krnl.es`, you can expect the wildcard domain `*.apps.example.krnl.es` to be routable.

.Procedure

To set up a load balancer and wildcard DNS record for the `*.apps` domain, perform the following actions on your guest cluster:

. Deploy MetalLB by creating a YAML file that contains the configuration for the MetalLB Operator:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: metallb
  labels:
    openshift.io/cluster-monitoring: "true"
  annotations:
    workload.openshift.io/allowed: management
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: metallb-operator-operatorgroup
  namespace: metallb
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metallb-operator
  namespace: metallb
spec:
  channel: "stable"
  name: metallb-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

. Save the file as `metallb-operator-config.yaml`.

. Enter the following command to apply the configuration:
+
[source,terminal]
----
$ oc apply -f metallb-operator-config.yaml
----

. After the Operator is running, create the MetalLB instance:

.. Create a YAML file that contains the configuration for the MetalLB instance:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb
----

.. Save the file as `metallb-instance-config.yaml`.

.. Create the MetalLB instance by entering this command:
+
[source,terminal]
----
$ oc apply -f metallb-instance-config.yaml
----

. Create an `IPAddressPool` resource with a single IP address. This IP address must be on the same subnet as the network that the cluster nodes use.

.. Create a file, such as `ipaddresspool.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb
  name: <ip_address_pool_name> <1>
spec:
  addresses:
    - <ingress_ip>-<ingress_ip> <2>
  autoAssign: false
----
<1> Specify the `IPAddressPool` resource name.
<2> Specify the IP address for your environment. For example, `192.168.122.23`.

.. Apply the configuration for the IP address pool by entering the following command:
+
[source,terminal]
----
$ oc apply -f ipaddresspool.yaml
----

. Create a L2 advertisement.

.. Create a file, such as `l2advertisement.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: <l2_advertisement_name> <1>
  namespace: metallb
spec:
  ipAddressPools:
   - <ip_address_pool_name> <2>
----
<1> Specify the `L2Advertisement` resource name.
<2> Specify the `IPAddressPool` resource name.

.. Apply the configuration by entering the following command:
+
[source,terminal]
----
$ oc apply -f l2advertisement.yaml
----

. After creating a service of the `LoadBalancer` type, MetalLB adds an external IP address for the service.

.. Configure a new load balancer service that routes ingress traffic to the ingress deployment by creating a YAML file named `metallb-loadbalancer-service.yaml`:
+
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  annotations:
   metallb.io/address-pool: ingress-public-ip
  name: metallb-ingress
  namespace: openshift-ingress
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 80
    - name: https
      protocol: TCP
      port: 443
      targetPort: 443
  selector:
    ingresscontroller.operator.openshift.io/deployment-ingresscontroller: default
  type: LoadBalancer
----

.. Save the `metallb-loadbalancer-service.yaml` file.

.. Enter the following command to apply the YAML configuration:
+
[source,terminal]
----
$ oc apply -f metallb-loadbalancer-service.yaml
----

.. Enter the following command to reach the OpenShift Container Platform console:
+
[source,bash]
----
$ curl -kI https://console-openshift-console.apps.example.krnl.es
----
+
.Example output
[source,terminal]
----
HTTP/1.1 200 OK
----

.. Check the `clusterversion` and `clusteroperator` values to verify that everything is running. Enter the following command:
+
[source,terminal]
----
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get clusterversion,co
----
+
.Example output
[source,terminal]
----
NAME                                         VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
clusterversion.config.openshift.io/version   4.x.y      True        False        3m32s   Cluster version is 4.x.y

NAME                                                                             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
clusteroperator.config.openshift.io/console                                      4.x.y     True        False         False      3m50s
clusteroperator.config.openshift.io/ingress                                      4.x.y     True        False         False      53m
----
+
Replace `<4.x.y>` with the supported OpenShift Container Platform version that you want to use, for example, `4.22.0-multi`.

//to add: konnectivity module

//to add: security considerations module

//to add: network policy considerations module

//cno and hcp
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-custom-ovn-subnets_{context}"]
= Configuring internal OVN IPv4 subnets for hosted clusters

[role="_abstract"]
In hosted clusters, you can configure internal OVN subnets to avoid routing conflicts, customize network architecture, or enable virtual private cloud (VPC) peering.

Avoid CIDR conflicts:: Connect VPCs that host {product-rosa} clusters with other VPCs that use the default OVN internal subnets of 100.88.0.0/16 and 100.64.0.0/16. To avoid a conflict on a `kubevirt` hosted cluster, the HyperShift Operator sets the OVN join subnet to `100.66.0.0/16` instead of `100.64.0.0/16` or `100.65.0.0/16`. The default CIDR for the OVN gateway router is `100.64.0.0/16`. The default CIDR for the user-defined network (UDN) join subnet is `100.65.0.0/16`.
Customize network architecture:: Configure internal OVN subnets to align with your corporate network policies.
Enable VPC peering:: Deploy hosted clusters in environments where default subnets conflict with peered networks.

To configure OVN-internal subnets, you expose two OVN-Kubernetes internal subnet configuration options:

`internalJoinSubnet`:: Internal subnet used by OVN-Kubernetes for the join network (default: `100.64.0.0/16`)
`internalTransitSwitchSubnet`:: Internal subnet used for the distributed transit switch in OVN Interconnect architecture (default: `100.88.0.0/16`)

You can configure internal OVN subnets in an existing hosted cluster or configure the subnets while you create a hosted cluster.

.Prerequisites

* Your hosted cluster version must be OpenShift Container Platform 4.20 or later.
* For the network type, your hosted cluster must use `networkType: OVNKubernetes`.
* Custom subnets must not overlap with the following subnets:

** Machine CIDRs
** Service CIDRs
** Cluster network CIDRs
** Any other networks in your infrastructure

.Procedure

* To configure internal OVN subnets while you create a hosted cluster, in the configuration file for the hosted cluster, include the following section:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_control_plane_namespace>
spec:
  networking:
    networkType: OVNKubernetes
    machineCIDR: 10.0.0.0/16
    serviceCIDR: 172.30.0.0/16
    clusterNetwork:
    - cidr: 10.128.0.0/14
  operatorConfiguration:
    clusterNetworkOperator:
      ovnKubernetesConfig:
        ipv4:
          internalJoinSubnet: "100.99.0.0/16"
          internalTransitSwitchSubnet: "100.69.0.0/16"
----
+
where:
+
--
`metadata`:: Specifies the name of the hosted cluster and the name of the hosted control plane namespace.
`spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig.ipv4`:: Specifies the subnets to use. Both subnet fields in this section must be in a valid IPv4 CIDR notation, such as `192.168.1.0/24`. The prefix range is `/0` to `/30`, inclusive. The first octet cannot be 0, and the string length must be 9-18 characters. The subnet fields cannot use the same value. The subnet must be large enough to accommodate one IP address per node in the cluster. When you plan subnet size, consider future cluster growth. If you omit these fields, the default value for the `internalJoinSubnet` field is `100.64.0.0/16`, and the default value for the `internalTransitSwitchSubnet` field is `100.88.0.0/16`.
--
+
For full details about creating a hosted cluster, see "Creating a hosted cluster by using the CLI".

* To configure internal OVN subnets in an existing hosted cluster, enter the following command:
+
[IMPORTANT]
====
When you make this change to an existing hosted cluster, the `ovnkube-node` DaemonSet is rolled out and the OVN components on compute nodes are restarted. During this process, you might experience brief network disruptions.
====
+
[source,terminal]
----
$ oc patch hostedcluster <hosted_cluster_name> \
  -n <hosted_control_plane_namespace> \
  --type=merge \
  -p '{
    "spec": {
      "operatorConfiguration": {
        "clusterNetworkOperator": {
          "ovnKubernetesConfig": {
            "ipv4": {
              "internalJoinSubnet": "100.99.0.0/16",
              "internalTransitSwitchSubnet": "100.69.0.0/16"
            }
          }
        }
      }
    }
  }'
----
+
where:
+
--
`metadata`:: Specifies the name of the hosted cluster and the name of the hosted control plane namespace.
`spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig.ipv4`:: Specifies the subnets to use. Both subnet fields in this section must be in a valid IPv4 CIDR notation, such as `192.168.1.0/24`. The prefix range is `/0` to `/30`, inclusive. The first octet cannot be 0, and the string length must be 9-18 characters. The subnet fields cannot use the same value. The subnet must be large enough to accommodate one IP address per node in the cluster. When you plan subnet size, consider future cluster growth. If you omit these fields, the default value for the `internalJoinSubnet` field is `100.64.0.0/16`, and the default value for the `internalTransitSwitchSubnet` field is `100.88.0.0/16`.
--

.Verification

. Verify that the hosted configuration is correct by entering the following command:
+
[source,terminal]
----
$ oc get hostedcluster <hosted_cluster_name> -n <hosted_control_plane_namespace> \
  -o jsonpath='{.spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig}' | jq .
----
+
.Example output
[source,terminal]
----
{
  "ipv4": {
    "internalJoinSubnet": "100.99.0.0/16",
    "internalTransitSwitchSubnet": "100.69.0.0/16"
  }
}
----

. Check the Network Operator configuration in the hosted cluster:
+
.. Extract the hosted cluster kubeconfig file by entering the following command:
+
[source,terminal]
----
$ oc extract secret/<hosted_cluster_name>-admin-kubeconfig \
  -n <hosted_control_plane_namespace> --to=- > <hosted_cluster_kubeconfig_file>
----
+
.. Verify the Network Operator configuration by entering the following command:
+
[source,terminal]
----
$ oc get network.operator.openshift.io cluster \
  --kubeconfig=<hosted_cluster_kubeconfig_file> \
  -o jsonpath='{.spec.defaultNetwork.ovnKubernetesConfig.ipv4}' | jq .
----
+
.Example output
[source,terminal]
----
{
  "internalJoinSubnet": "100.99.0.0/16",
  "internalTransitSwitchSubnet": "100.69.0.0/16"
}
----

. Create 2 test pods by completing the following steps:
+
.. In node 1, create pod 1, as shown in the following example:
+
[source,yaml]
----
kind: Pod
apiVersion: v1
  metadata:
    name: "<pod_1>"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: <pod_name>
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
    - image: "<image_url>"
      name: <pod_name>
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
    nodeName: "${NODE1}"
----
+
.. In node 2, create pod 2, as shown in the following example:
+
[source,yaml]
----
kind: Pod
apiVersion: v1
  metadata:
    name: "<pod_2>"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: <pod_name>
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
    - image: "<image_url>"
      name: <pod_name>
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
    nodeName: "${NODE2}"
----

. Create a test service that backs up both pods, as shown in the following example:
+
[source,yaml]
----
kind: Service
apiVersion: v1
  metadata:
    name: "<test_service_name"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: test-service
  spec:
    internalTrafficPolicy: "Cluster"
    externalTrafficPolicy: ""
    ipFamilyPolicy: "SingleStack"
    ports:
    - name: http
      port: <service_test_port_number>
      protocol: "TCP"
      targetPort: 8080
    selector:
      name: "<pod_name>"
    type: "ClusterIP"
----

. Verify that the OVN pods are running:

.. Enter the following command:
+
[source,terminal]
----
$ oc rollout status daemonset/ovnkube-node \
  -n openshift-ovn-kubernetes \
  --kubeconfig=<hosted_cluster_kubeconfig_file> \
  --timeout=5m
----

.. Enter the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes --kubeconfig=<hosted_cluster_kubeconfig_file>
----
+
All `ovnkube-node` pods should be in `Running` state with all containers ready.

. Make sure that the changes synchronized to the Network Operator by entering the following command:
+
[source,terminal]
----
$ oc get network.operator.openshift.io/cluster \
  -ojsonpath='{.spec.defaultNetwork.ovnKubernetesConfig.ipv4}' \
  --kubeconfig=<clusters-hostedclustername> | jq .
----

. Get the IP address of pod 2 and transfer it from pod 1:

.. Enter the following command:
+
[source,terminal]
----
$ pod2_ip=oc get pod -n e2e-test-networking-ovnkubernetes-xxt8s <pod_2> -o=jsonpath={.status.podIPs[0].ip}
----

.. Enter the following command:
+
[source,terminal]
----
$ oc exec <pod_1> -- /bin/sh -x -c curl --connect-timeout 5 -s <pod2_ip>:8080
----

. Get the service IP address and verify that the pod can be visited externally from a service:

.. Enter the following command:
+
[source,terminal]
----
$ SERVICE_IP=oc get service test-service-o=jsonpath={.spec.clusterIPs[0]}
----

.. Enter the following command:
+
[source,terminal]
----
$ oc exec <pod_1> -- /bin/sh -x -c curl --connect-timeout 5 -s $SERVICE_IP:<service_test_port_number>
----

[role="_additional-resources"]
.Additional resources
* Troubleshooting internal subnets for hosted clusters
* Creating a hosted cluster by using the CLI

//hcp proxy overview
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-overview_{context}"]
= Proxy support for {hcp}

[role="_abstract"]
To ensure that control-plane workloads, compute nodes, management clusters, and hosted clusters have the access they need for optimal performance, you can configure proxy support.

In standalone OpenShift Container Platform, the primary purposes of proxy support are ensuring that workloads in the cluster are configured to use the HTTP or HTTPS proxy to access external services, honoring the `NO_PROXY` setting if one is configured, and accepting any trust bundle that is configured for the proxy.

In {hcp}, proxy support includes use cases beyond those in standalone OpenShift Container Platform.

//cp workloads that need to use a proxy to access external services
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-cp-workloads_{context}"]
= Control plane workloads that need to access external services

Operators that run in the control plane need to access external services through the proxy that is configured for the hosted cluster. The proxy is usually accessible only through the data plane. The control plane workloads are as follows:

* The Control Plane Operator needs to validate and obtain endpoints from certain identity providers when it creates the OAuth server configuration.

* The OAuth server needs non-LDAP identity provider access.

* The OpenShift API server handles image registry metadata import.

* The Ingress Operator needs access to validate external canary routes.

* You must open the firewall port `53` on Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to allow the Domain Name Service (DNS) protocol to work as expected.

In a hosted cluster, you must send traffic that originates from the Control Plane Operator, Ingress Operator, OAuth server, and OpenShift API server pods through the data plane to the configured proxy and then to its final destination.

[NOTE]
====
Some operations are not possible when a hosted cluster is reduced to zero compute nodes; for example, when you import OpenShift image streams from a registry that requires proxy access.
====

//workers need a proxy to communicate with ignition endpoint
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-ignition_{context}"]
= Compute nodes that need to access an ignition endpoint

When compute nodes need a proxy to access the ignition endpoint, you must configure the proxy in the user-data stub that is configured on the compute node when it is created. For cases where machines need a proxy to access the ignition URL, the proxy configuration is included in the stub.

The stub resembles the following example:

[source,terminal]
---
{"ignition":{"config":{"merge":[{"httpHeaders":[{"name":"Authorization","value":"Bearer ..."},{"name":"TargetConfigVersionHash","value":"a4c1b0dd"}],"source":"https://ignition.controlplanehost.example.com/ignition","verification":{}}],"replace":{"verification":{}}},"proxy":{"httpProxy":"http://proxy.example.org:3128", "httpsProxy":"https://proxy.example.org:3129", "noProxy":"host.example.org"},"security":{"tls":{"certificateAuthorities":[{"source":"...","verification":{}}]}},"timeouts":{},"version":"3.2.0"},"passwd":{},"storage":{},"systemd":{}}
---

//workers need proxy to communicate with cp
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-api_{context}"]
= Compute nodes that need to access the API server

This use case is relevant to self-managed {hcp}, not to {product-rosa} with {hcp}.

For communication with the control plane, {hcp} uses a local proxy in every compute node that listens on IP address 172.20.0.1 and forwards traffic to the API server. If an external proxy is required to access the API server, that local proxy needs to use the external proxy to send traffic out. When a proxy is not needed, {hcp} uses `haproxy` for the local proxy, which only forwards packets via TCP. When a proxy is needed, {hcp} uses a custom proxy, `control-plane-operator-kubernetes-default-proxy`, to send traffic through the external proxy.

//cp workloads that need access to external services and must use the proxy for the management cluster
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-mgmt-cluster_{context}"]
= Management clusters that need external access

The HyperShift Operator has a controller that monitors the OpenShift global proxy configuration of the management cluster and sets the proxy environment variables on its own deployment. Control plane deployments that need external access are configured with the proxy environment variables of the management cluster.

//proxy configuration on the mgmt cluster when the hosted cluster has a secondary network and no default pod network
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-networking.adoc

[id="hcp-proxy-addl-network_{context}"]
= Management cluster that uses a proxy and a hosted cluster with a secondary network and no default pod network

If a management cluster uses a proxy configuration and you are configuring a hosted cluster with a secondary network but are not attaching the default pod network, add the CIDR of the secondary network to the proxy configuration. Specifically, you need to add the CIDR of the secondary network to the `noProxy` section of the proxy configuration for the management cluster. Otherwise, the Kubernetes API server will route some API requests through the proxy. In the hosted cluster configuration, the CIDR of the secondary network is automatically added to the `noProxy` section.

[role="_additional-resources"]
.Additional resources

* Troubleshooting internal subnets for hosted clusters
* Creating a hosted cluster by using the CLI
* About the OVN-Kubernetes network plugin
* Configuring the cluster-wide proxy
