---
title: "Configuring certificate rotation"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-certificate-rotation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-certificate-rotation
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring certificate rotation

[id="virt-configuring-certificate-rotation"]
= Configuring certificate rotation

[role="_abstract"]
Configure certificate rotation parameters to replace existing certificates.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-configuring-certificate-rotation.adoc

[id="virt-configuring-certificate-rotation_{context}"]
= Configuring certificate rotation

[role="_abstract"]
You can do this during {VirtProductName} installation in the web console or after installation in the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `spec.certConfig` fields as shown in the following example. To avoid overloading the system, ensure that all values are greater than or equal to 10 minutes. Express all values as strings that comply with the golang `ParseDuration` format.
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  certConfig:
    ca:
      duration: 48h0m0s
      renewBefore: 24h0m0s
    server:
      duration: 24h0m0s
      renewBefore: 12h0m0s
----
+
** The value of `ca.renewBefore` must be less than or equal to the value of `ca.duration`.
** The value of `server.duration` must be less than or equal to the value of `ca.duration`.
** The value of `server.renewBefore` must be less than or equal to the value of `server.duration`.

. Apply updates to the `HyperConverged` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc apply -f kubevirt-hyperconverged.yaml
----
// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-certificate-rotation.adoc

[id="virt-troubleshooting-cert-rotation-parameters_{context}"]
= Troubleshooting certificate rotation parameters

[role="_abstract"]
Deleting one or more `certConfig` values in the `HyperConverged` custom resource (CR) causes the `certConfig` values to revert to the default values.

If the default values conflict with one of the following conditions, you receive an error message instead:

* The value of `ca.renewBefore` must be less than or equal to the value of `ca.duration`.
* The value of `server.duration` must be less than or equal to the value of `ca.duration`.
* The value of `server.renewBefore` must be less than or equal to the value of `server.duration`.

For example, if you remove the `server.duration` value, the default value of `24h0m0s` is greater than the value of `ca.duration`, which conflicts with the specified conditions:

[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  # ...
  certConfig:
    ca:
      duration: 4h0m0s
      renewBefore: 1h0m0s
    server:
      duration: 4h0m0s
      renewBefore: 4h0m0s
# ...
----

This results in the following error message:

[source,terminal]
----
error: hyperconvergeds.hco.kubevirt.io "kubevirt-hyperconverged" could not be patched: admission webhook "validate-hco.kubevirt.io" denied the request: spec.certConfig: ca.duration is smaller than server.duration
----

The error message only mentions the first conflict. Review all `certConfig` values before you proceed.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* golang `ParseDuration` format
