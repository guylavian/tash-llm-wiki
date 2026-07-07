---
title: "Using certificate manager on a {microshift-short} node"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-cert-manager
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-cert-manager
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using certificate manager on a {microshift-short} node

[id="microshift-cert-manager"]
= Using certificate manager on a {microshift-short} node

[role="_abstract"]
The {microshift-short} certificate manager supports managing TLS certificates. This integration results in the issue, renewal, and management of certificate from certificate authorities.

// Module included in the following assemblies:
//
// * microshift_running_apps/microshift-cert-manager.adoc

[id="microshift-cert-manager-tasks_{context}"]
= {microshift-short} certificate manager functions

[role="_abstract"]
With {microshift-short} certificate manager, you can complete the following tasks:

* Automates certificate management: cert-manager creates or updates certificates and detects Kubernetes resources that are annotated with `cert-manager.io/kind`.
* Supports multiple CAs: provides flexibility to select one that fits the security and operational needs.
* Simplifies ingress certificates: cert-manager handles certificates for an ingress controller, which simplifies the configuration and management of secure communication channels.
* Enhances security: certificate management is automated and the risk of error is reduced. Certificates are current and valid, which contribute to a secure environment.

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-cert-manager.adoc

[id="microshift-install-cert-manager_{context}"]
= Installing and enabling the cert-manager Operator using RPM

[role="_abstract"]
The microshift-cert-manager RPM is an optional component that can be installed at any time. Follow these steps to install and verify the certificate manager:

.Procedure

. Install the `cert-manager-operator` using the `microshift-cert-manager` RPM by running the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-cert-manager
----

. Verify the certificate manager versions that are used by running the following command:
+
[source,terminal]
----
$ rpm -qi microshift-cert-manager
----

. Restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ systemctl microshift restart
----

. Verify that the `microshift-cert-manager` RPM is installed by running the following command:
+
[source,terminal]
----
$ oc get deployment -n  cert-manager-operator
----
+
.Example output
[source,terminal]
----
NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
cert-manager-operator-controller-manager   1/1     1            1           2d22h
----

. Verify that the`cert-manager` deployments are in a ready state and are up-to-date in the cert-manager namespace by running the following command:
+
[source,terminal]
----
$ oc get deployment -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
cert-manager              1/1     1            1           2d22h
cert-manager-cainjector   1/1     1            1           2d22h
cert-manager-webhook      1/1     1            1           2d22h
----

. Verify that the pods are running in the `cert-manager` namespace by running the following command:
+
[source,terminal]
----
$ oc get pods -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-7cfb4fbb84-qdmk8              1/1     Running   2          2d22h
cert-manager-cainjector-854f669657-xzs8b   1/1     Running   2          2d22h
cert-manager-webhook-68fd6d5f5c-j942h      1/1     Running   2          2d22h
----

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-cert-manager.adoc

[id="microshift-install-cert-manager-olm_{context}"]
= Installing and enabling the cert-manager Operator using OLM

[role="_abstract"]
You can install the optional `microshift-cert-manager` by using OLM at any time. For more information, see Using Operator Lifecycle Manager with MicroShift and Installing the cert-manager Operator for Red Hat OpenShift.
