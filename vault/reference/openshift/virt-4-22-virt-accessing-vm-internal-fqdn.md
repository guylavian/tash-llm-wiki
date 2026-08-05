---
title: "Accessing a virtual machine  by using its internal FQDN"
type: reference
domain: openshift
slug: virt-4-22-virt-accessing-vm-internal-fqdn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-accessing-vm-internal-fqdn
version: 4.22
family: virt
documentKind: "Documentation"
---

# Accessing a virtual machine  by using its internal FQDN

[id="virt-accessing-vm-internal-fqdn"]
= Accessing a virtual machine  by using its internal FQDN

[role="_abstract"]
You can access a virtual machine (VM) that is connected to the default internal pod network on a stable fully qualified domain name (FQDN) by using headless services. A Kubernetes _headless service_ creates a DNS record for each pod associated with the service instead of providing a single virtual IP address for the service. You can expose a VM through its FQDN without having to expose a specific TCP or UDP port.

[IMPORTANT]
====
If you created a VM by using the OpenShift Container Platform web console, you can find its internal FQDN listed in the *Network* tile on the *Overview* tab of the *VirtualMachine details* page.
====

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-accessing-vm-internal-fqdn.adoc

[id="virt-creating-headless-services_{context}"]
= Creating a headless service in a project by using the CLI

[role="_abstract"]
To create a headless service in a namespace, add the `clusterIP: None` parameter to the service YAML definition.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a `Service` manifest to expose the VM, such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: mysubdomain
spec:
  selector:
    expose: me
  clusterIP: None
  ports:
  - protocol: TCP
    port: 1234
    targetPort: 1234
----
+
* `metadata.name` defines the name of the service. This must match the `spec.subdomain` attribute in the `VirtualMachine` manifest file.
* `spec.selector` defines the service selector that must match the `expose:me` label in the `VirtualMachine` manifest file.
* `spec.clusterIP` defines a headless service.
* `spec.ports` defines the list of ports that are exposed by the service. You must define at least one port. This can be any arbitrary value as it does not affect the headless service.

. Save the `Service` manifest file.

. Create the service by running the following command:
+
[source,terminal]
----
$ oc create -f headless_service.yaml
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-accessing-vm-internal-fqdn.adoc

[id="virt-discovering-vm-internal-fqdn_{context}"]
= Mapping a virtual machine to a headless service by using the CLI

[role="_abstract"]
To connect to a virtual machine (VM) from within the cluster by using its internal fully qualified domain name (FQDN), you must first map the VM to a headless service. Set the `spec.hostname` and `spec.subdomain` parameters in the VM configuration file.

If a headless service exists with a name that matches the subdomain, a unique DNS A record is created for the VM in the form of `<vm.spec.hostname>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the `VirtualMachine` manifest to add the service selector label and subdomain by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name>
----
+
Example `VirtualMachine` manifest file:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-fedora
spec:
  template:
    metadata:
      labels:
        expose: me
    spec:
      hostname: "myvm"
      subdomain: "mysubdomain"
# ...
----
+
* `spec.template.metadata.labels.expose` defines a label that must match the `spec.selector` attribute of the `Service` manifest that you previously created.
* `spec.template.spec.hostname` defines the hostname. If this attribute is not specified, the resulting DNS A record takes the form of `<vm.metadata.name>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.
* `spec.template.spec.subdomain` defines the subdomain. The `spec.subdomain` attribute must match the `metadata.name` value of the `Service` object.

. Save your changes and exit the editor.

. Restart the VM to apply the changes.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-accessing-vm-internal-fqdn.adoc

[id="virt-connecting-vm-internal-fqdn_{context}"]
= Connecting to a virtual machine by using its internal FQDN

[role="_abstract"]
You can connect to a virtual machine (VM) by using its internal fully qualified domain name (FQDN).

.Prerequisites
* You have installed the `virtctl` tool.
* You have identified the internal FQDN of the VM from the web console or by mapping the VM to a headless service. The internal FQDN has the format `<vm.spec.hostname>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.

.Procedure

. Connect to the VM console by entering the following command:
+
[source,terminal]
----
$ virtctl console vm-fedora
----

. To connect to the VM by using the requested FQDN, run the following command:
+
[source,terminal]
----
$ ping myvm.mysubdomain.<namespace>.svc.cluster.local
----
+
Example output:
+
[source,terminal]
----
PING myvm.mysubdomain.default.svc.cluster.local (10.244.0.57) 56(84) bytes of data.
64 bytes from myvm.mysubdomain.default.svc.cluster.local (10.244.0.57): icmp_seq=1 ttl=64 time=0.029 ms
----
+
In the preceding example, the DNS entry for `myvm.mysubdomain.default.svc.cluster.local` points to `10.244.0.57`, which is the cluster IP address that is currently assigned to the VM.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Exposing a VM by using a service
