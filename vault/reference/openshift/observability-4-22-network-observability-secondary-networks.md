---
title: "Secondary networks"
type: reference
domain: openshift
slug: observability-4-22-network-observability-secondary-networks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-secondary-networks
version: 4.22
family: observability
documentKind: "Documentation"
---

# Secondary networks

[id="network-observability-secondary-networks"]
= Secondary networks

[role="_abstract"]
You can configure the Network Observability Operator to collect and enrich network flow data from secondary networks, such as `SR-IOV` and `OVN-Kubernetes`.

// Note to tech review:
// Is the existing SR-IOV example we have, "Configuring monitoring for SR-IOV interface traffic", an example of secondary network? If so, it is not through a VM, right?

[id="network-observability-secondary-network-prerequisites_{context}"]
== Prerequisites
* Access to an OpenShift Container Platform cluster with an additional network interface, such as a secondary interface or an L2 network.

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-secondary-networks.adoc

[id="network-observability-SR-IOV-config_{context}"]
= Configuring monitoring for SR-IOV interface traffic

[role="_abstract"]
Configure the `FlowCollector` resource to monitor traffic on Single Root I/O Virtualization (SR-IOV) device by setting the `spec.agent.ebpf.privileged` field to `true`, which enables the eBPF agent to monitor other network namespaces.

The eBPF agent monitors other network namespaces in addition to the host network namespaces, which are monitored by default. When a pod with a virtual functions (VF) interface is created, a new network namespace is created. With `SRIOVNetwork` policy `IPAM` configurations specified, the VF interface is migrated from the host network namespace to the pod network namespace.

.Prerequisites
* Access to an OpenShift Container Platform cluster with a SR-IOV device.
* The `SRIOVNetwork` custom resource (CR) `spec.ipam` configuration must be set with an IP address from the range that the interface lists or from other plugins.

.Procedure
. In the web console, navigate to *Ecosystem* -> *Installed Operators*.
. Under the *Provided APIs* heading for the *NetObserv Operator*, select *Flow Collector*.
. Select *cluster* and then select the *YAML* tab.
. Configure the `FlowCollector` custom resource. A sample configuration is as follows:
+
.Configure `FlowCollector` for SR-IOV monitoring
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      privileged: true
----
+
** The `spec.agent.ebpf.privileged` field value must be set to `true` to enable SR-IOV monitoring.

[role="_additional-resources"]
.Additional resources
* Configuring an SR-IOV network device

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-secondary-networks.adoc

[id="network-observability-virtualization-config_{context}"]
= Configuring virtual machine (VM) secondary network interfaces for Network Observability

[role="_abstract"]
Configure the `FlowCollector` to monitor VM secondary network traffic by setting the eBPF agent to `privileged` mode and defining the indexing for secondary networks, enabling the capture and enrichment of flows from {VirtProductName}.

Network flows coming from VMs that are connected to the default internal pod network are automatically captured by network observability.

.Procedure
. Get information about the virtual machine launcher pod by running the following command. This information is used in Step 5:
+
[source,terminal]
----
$ oc get pod virt-launcher-<vm_name>-<suffix> -n <namespace> -o yaml
----
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
        "name": "ovn-kubernetes",
        "interface": "eth0",
        "ips": [
          "10.129.2.39"
        ],
        "mac": "0a:58:0a:81:02:27",
        "default": true,
        "dns": {}
      },
      {
        "name": "my-vms/l2-network",
        "interface": "podc0f69e19ba2",
        "ips": [
          "10.10.10.15"
        ],
        "mac": "02:fb:f8:00:00:12",
        "dns": {}
      }]
  name: virt-launcher-fedora-aqua-fowl-13-zr2x9
  namespace: my-vms
spec:
#  ...
status:
#  ...
----
+
where:

`name`:: Specifies the name of the secondary network.
`interface`:: Specifies the network interface of the secondary network.
`ips`:: Specifies the list of IP addresses used by the secondary network.
`mac`:: Specifies the MAC address used for the secondary network.

. In the web console, navigate to *Ecosystem* -> *Installed Operators*.
. Under the *Provided APIs* heading for the *NetObserv Operator*, select *Flow Collector*.
. Select *cluster* and then select the *YAML* tab.
. Configure `FlowCollector` based on the information you found from the additional network investigation:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    ebpf:
      privileged: true
  processor:
    advanced:
      secondaryNetworks:
      - index:
        - MAC
        name: my-vms/l2-network
# ...
----
+
where:

`spec.agent.ebpf.privileged`:: Specifies that the eBPF agent runs in `privileged` mode, which is required to collect flows from secondary network interfaces on virtual machine launcher pods.
`spec.processor.advanced.secondaryNetworks.index`:: Specifies the fields to use for indexing the virtual machine launcher pods. It is recommended to use the `MAC` address as the indexing field to get network flows enrichment for secondary interfaces. If you have overlapping MAC addresses between pods, then additional indexing fields, such as `IP` and `Interface`, can be added to ensure accurate enrichment.
`MAC`:: Specifies the MAC address as an indexing field value. Add `MAC` to the `index` field list if your additional network information includes a MAC address.
`spec.processor.advanced.secondaryNetworks.name`:: Specifies the name of the secondary network as found in the `k8s.v1.cni.cncf.io/network-status` annotation of the virtual machine launcher pod. The format is typically `<namespace>/<network_attachment_definition_name>`.

.Verification
. Observe VM traffic:
.. Navigate to the *Network Traffic* page.
.. Filter by *Source* IP using your virtual machine IP found in `k8s.v1.cni.cncf.io/network-status` annotation.
.. View both *Source* and *Destination* fields, which should be enriched, and identify the VM launcher pods and the VM instance as owners.
