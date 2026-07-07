---
title: "Accessing a virtual machine by using its external FQDN"
type: reference
domain: openshift
slug: virt-4-22-virt-accessing-vm-secondary-network-fqdn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-accessing-vm-secondary-network-fqdn
version: 4.22
family: virt
documentKind: "Documentation"
---

# Accessing a virtual machine by using its external FQDN

[id="virt-accessing-vm-secondary-network-fqdn"]
= Accessing a virtual machine by using its external FQDN

[role="_abstract"]
You can access a virtual machine (VM) that is attached to a secondary network interface from outside the cluster by using its fully qualified domain name (FQDN). To connect to a VM by using its external FQDN, you must configure the DNS server, retrieve the cluster FQDN, then connect to the VM by using the `ssh` command.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-accessing-vm-secondary-network-fqdn.adoc

[id="virt-configuring-secondary-dns-server_{context}"]
= Configuring a DNS server for secondary networks

[role="_abstract"]
The Cluster Network Addons Operator (CNAO) deploys a Domain Name Server (DNS) server and monitoring components when you enable the `deployKubeSecondaryDNS` feature gate in the `HyperConverged` custom resource (CR).

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You configured a load balancer for the cluster.
* You logged in to the cluster with `cluster-admin` permissions.

.Procedure

. Edit the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Enable the DNS server and monitoring components according to the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
    featureGates:
      deployKubeSecondaryDNS: true
# ...
----
+
Setting `deployKubeSecondaryDNS` to `true` enables the DNS server.

. Save the file and exit the editor.

. Create a load balancer service to expose the DNS server outside the cluster by running the `oc expose` command according to the following example:
+
[source,terminal,subs="attributes+"]
----
$ oc expose -n {CNVNamespace} deployment/secondary-dns --name=dns-lb \
  --type=LoadBalancer --port=53 --target-port=5353 --protocol='UDP'
----

. Retrieve the external IP address by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get service -n {CNVNamespace}
----
+
Example output:
+
[source,text]
----
NAME       TYPE             CLUSTER-IP     EXTERNAL-IP      PORT(S)          AGE
dns-lb     LoadBalancer     172.30.27.5    10.46.41.94      53:31829/TCP     5s
----

. Edit the `HyperConverged` CR again:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the external IP address that you previously retrieved to the `kubeSecondaryDNSNameServerIP` field in the enterprise DNS server records. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  featureGates:
    deployKubeSecondaryDNS: true
  kubeSecondaryDNSNameServerIP: "10.46.41.94"
# ...
----
+
Specify the external IP address exposed by the load balancer service in the `kubeSecondaryDNSNameServerIP` field.

. Save the file and exit the editor.

. Retrieve the cluster FQDN by running the following command:
+
[source,terminal]
----
 $ oc get dnses.config.openshift.io cluster -o jsonpath='{.spec.baseDomain}'
----
+
Example output:
+
[source,text]
----
openshift.example.com
----

. Point to the DNS server. To do so, add the `kubeSecondaryDNSNameServerIP` value and the cluster FQDN to the enterprise DNS server records. For example:
+
[source,terminal]
----
vm.<FQDN>. IN NS ns.vm.<FQDN>.
----
+
[source,terminal]
----
ns.vm.<FQDN>. IN A <kubeSecondaryDNSNameServerIP>
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-accessing-vm-secondary-network-fqdn.adoc

[id="virt-connecting-vm-secondarynw-fqdn_{context}"]
= Connecting to a VM on a secondary network by using the cluster FQDN

[role="_abstract"]
You can access a running virtual machine (VM) attached to a secondary network interface by using the fully qualified domain name (FQDN) of the cluster.

.Prerequisites

* You installed the {oc-first}.
* You installed the QEMU guest agent on the VM.
* The IP address of the VM is public.
* You configured the DNS server for secondary networks.
* You retrieved the fully qualified domain name (FQDN) of the cluster.
+
To obtain the FQDN, use the `oc get` command as follows:
+
[source,terminal]
----
$ oc get dnses.config.openshift.io cluster -o json | jq .spec.baseDomain
----

.Procedure

. Retrieve the network interface name from the VM configuration by running the following command:
+
[source,terminal]
----
$ oc get vm -n <namespace> <vm_name> -o yaml
----
+
Example output:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  runStrategy: Always
  template:
    spec:
      domain:
        devices:
          interfaces:
            - bridge: {}
              name: example-nic
# ...
      networks:
      - multus:
          networkName: bridge-conf
        name: example-nic
----
+
Note the `name` of the network interface.

. Connect to the VM by using the `ssh` command:
+
[source,terminal]
----
$ ssh <user_name>@<interface_name>.<vm_name>.<namespace>.vm.<cluster_fqdn>
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
// Hiding until OSDOCS-3691 is merged
* Configuring ingress cluster traffic by using a load balancer
* About MetalLB and the MetalLB Operator
* Configuring IP addresses for virtual machines
