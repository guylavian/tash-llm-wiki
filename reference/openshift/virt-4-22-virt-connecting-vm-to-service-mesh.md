---
title: "Connecting a virtual machine to a service mesh"
type: reference
domain: openshift
slug: virt-4-22-virt-connecting-vm-to-service-mesh
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-connecting-vm-to-service-mesh
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connecting a virtual machine to a service mesh

[id="virt-connecting-vm-to-service-mesh"]
= Connecting a virtual machine to a service mesh

[role="_abstract"]
{VirtProductName} is now integrated with {SMProductName}. You can monitor, visualize, and control traffic between pods that run virtual machine (VM) workloads on the default pod network with IPv4.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-service-mesh.adoc

[id="virt-adding-vm-to-service-mesh_{context}"]
= Adding a virtual machine to a service mesh

[role="_abstract"]
To add a virtual machine (VM) workload to a service mesh, enable automatic sidecar injection in the VM configuration file by setting the `sidecar.istio.io/inject` annotation to `true`. Then expose your VM as a service to view your application in the mesh.

[IMPORTANT]
====
To avoid port conflicts, do not use ports used by the Istio sidecar proxy. These include ports 15000, 15001, 15006, 15008, 15020, 15021, and 15090.
====

.Prerequisites

* You have installed the {oc-first}.
* You have installed the {SMProductShortName} Operator.

.Procedure

. Edit the VM configuration file to add the `sidecar.istio.io/inject: "true"` annotation.
+
Example configuration file:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    kubevirt.io/vm: vm-istio
  name: vm-istio
spec:
  runStrategy: Always
  template:
    metadata:
      labels:
        kubevirt.io/vm: vm-istio
        app: vm-istio
      annotations:
        sidecar.istio.io/inject: "true"
    spec:
      domain:
        devices:
          interfaces:
          - name: default
            masquerade: {}
          disks:
          - disk:
              bus: virtio
            name: containerdisk
          - disk:
              bus: virtio
            name: cloudinitdisk
        resources:
          requests:
            memory: 1024M
      networks:
      - name: default
        pod: {}
      terminationGracePeriodSeconds: 180
      volumes:
      - containerDisk:
          image: registry:5000/kubevirt/fedora-cloud-container-disk-demo:devel
        name: containerdisk
----
** `spec.template.metadata.labels.app` specifies the key/value pair (label) that must be matched to the service selector attribute.
** `spec.template.metadata.annotations.sidecar.istio.io/inject` is the annotation to enable automatic sidecar injection.
** `spec.template.spec.domain.devices.interfaces.masquerade` is the binding method (masquerade mode) for use with the default pod network.

. Run the following command to apply the VM configuration:
+
[source,terminal]
----
$ oc apply -f <vm_name>.yaml
----
+
where:
+
`<vm_name>`:: Specifies the name of the virtual machine YAML file.

. Create a `Service` object to expose your VM to the service mesh:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: vm-istio
spec:
  selector:
    app: vm-istio
  ports:
    - port: 8080
      name: http
      protocol: TCP
----
** `spec.selector.app` specifies the service selector that determines the set of pods targeted by a service. This attribute corresponds to the `spec.metadata.labels` field in the VM configuration file. In the above example, the `Service` object named `vm-istio` targets TCP port 8080 on any pod with the label `app=vm-istio`.

. Run the following command to create the service:
+
[source,terminal]
----
$ oc create -f <service_name>.yaml
----
+
where:
+
`<service_name>`:: Specifies the name of the service YAML file.

// Hiding in OSD until PR 67901 merges - HCP hidden as well
[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Installing the Service Mesh Operator
