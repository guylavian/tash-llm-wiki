---
title: "Virtual machine control plane tuning"
type: reference
domain: openshift
slug: virt-4-22-virt-vm-control-plane-tuning
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-vm-control-plane-tuning
version: 4.22
family: virt
documentKind: "Documentation"
---

# Virtual machine control plane tuning

[id="virt-vm-control-plane-tuning"]
= Virtual machine control plane tuning

[role="_abstract"]
In {VirtProductName}, you can control how the control plane handles concurrency when you create or migrate virtual machines (VMs). For example, you can use the `highBurst` profile with either the fixed `QPS` or `burst` rates to batch create virtual machines (VMs) in a batch, or tune migration settings in the `HyperConverged` custom resource (CR).

// Module included in the following assemblies:
//
// * virt/advanced_vm_management/virt-vm-control-plane-tuning.adoc

[id="virt-configuring-highburst-profile_{context}"]
= Configuring a highBurst profile

[role="_abstract"]
You can use the `highBurst` profile to create and maintain a large number of virtual machines (VMs) in one cluster.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Apply the following patch to enable the `highBurst` tuning policy profile:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type=json -p='[{"op": "add", "path": "/spec/tuningPolicy", \
  "value": "highBurst"}]'
----

.Verification

* Run the following command to verify the `highBurst` tuning policy profile is enabled:
+
[source,terminal,subs="attributes+"]
----
$ oc get kubevirt.kubevirt.io/kubevirt-kubevirt-hyperconverged \
  -n {CNVNamespace} -o go-template --template='{{range $config, \
  $value := .spec.configuration}} {{if eq $config "apiConfiguration" \
  "webhookConfiguration" "controllerConfiguration" "handlerConfiguration"}} \
  {{"\n"}} {{$config}} = {{$value}} {{end}} {{end}} {{"\n"}}
----
