---
title: "Using huge pages with virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-using-huge-pages-with-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-huge-pages-with-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using huge pages with virtual machines

[id="virt-using-huge-pages-with-vms"]
= Using huge pages with virtual machines

[role="_abstract"]
You can use huge pages as backing memory for virtual machines in your cluster.

// Module included in the following assemblies:
//
// * scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc
// * virt/virtual_machines/advanced_vm_management/virt-using-huge-pages-with-vms.adoc
// * post_installation_configuration/node-tasks.adoc

[id="what-huge-pages-do_{context}"]
= What huge pages do

[role="_abstract"]
To optimize memory mapping efficiency, understand the function of huge pages. Unlike standard 4Ki blocks, huge pages are larger memory segments that reduce the tracking load on the translation lookaside buffer (TLB) hardware cache.

Memory is managed in blocks known as pages. On most systems, a page is 4Ki; 1Mi of memory is equal to 256 pages; 1Gi of memory is 256,000 pages, and so on. CPUs have a built-in memory management unit that manages a list of these pages in hardware. The translation lookaside buffer (TLB) is a small hardware cache of virtual-to-physical page mappings. If the virtual address passed in a hardware instruction can be found in the TLB, the mapping can be determined quickly. If not, a TLB miss occurs, and the system falls back to slower, software-based address translation, resulting in performance issues. Since the size of the TLB is fixed, the only way to reduce the chance of a TLB miss is to increase the page size.

A huge page is a memory page that is larger than 4Ki. On x86_64 architectures, there are two common huge page sizes: 2Mi and 1Gi. Sizes vary on other architectures. To use huge pages, code must be written so that applications are aware of them. Transparent huge pages (THP) attempt to automate the management of huge pages without application knowledge, but they have limitations. In particular, they are limited to 2Mi page sizes. THP can lead to performance degradation on nodes with high memory utilization or fragmentation because of defragmenting efforts of THP, which can lock memory pages. For this reason, some applications might be designed to or recommend usage of pre-allocated huge pages instead of THP.

In OpenShift Container Platform, applications in a pod can allocate and consume pre-allocated huge pages.

In {VirtProductName}, virtual machines can be configured to consume pre-allocated huge pages.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-using-huge-pages-with-vms.adoc

[id="virt-configuring-huge-pages-for-vms_{context}"]
= Configuring huge pages for virtual machines

[role="_abstract"]
You can configure virtual machines to use pre-allocated huge pages by including the
`memory.hugepages.pageSize` and `resources.requests.memory` parameters in your virtual machine configuration.

The memory request must be divisible by the page size. For example, you cannot request `500Mi` memory with a page size of `1Gi`.

[NOTE]
====
The memory layouts of the host and the guest OS are unrelated.
Huge pages requested in the virtual machine manifest apply to QEMU.
Huge pages inside the guest can only be configured based on the amount of available memory of the virtual machine instance.
====

If you edit a running virtual machine, the virtual machine must be rebooted for the changes to take effect.

.Prerequisites

* Nodes must have pre-allocated huge pages configured.
* You have installed the {oc-first}.

.Procedure

. In your virtual machine configuration, add the `resources.requests.memory` and
`memory.hugepages.pageSize` parameters to the `spec.domain`. The following configuration snippet is
for a virtual machine that requests a total of `4Gi` memory with a page size of `1Gi`:
+

[source,yaml]
----
kind: VirtualMachine
# ...
spec:
  domain:
    resources:
      requests:
        memory: "4Gi"
    memory:
      hugepages:
        pageSize: "1Gi"
# ...
----
+
* `memory` defines the total amount of memory requested for the virtual machine. This value must be divisible by the page size.
* `pageSize` defines the size of each huge page. Valid values for x86_64 architecture are `1Gi` and `2Mi`. The page size must be smaller than the requested memory.

. Apply the virtual machine configuration:
+
[source,terminal]
----
$ oc apply -f <virtual_machine>.yaml
----
