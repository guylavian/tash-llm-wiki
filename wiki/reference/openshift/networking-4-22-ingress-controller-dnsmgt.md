---
title: "Understanding DNS management policies"
type: reference
domain: openshift
slug: networking-4-22-ingress-controller-dnsmgt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ingress-controller-dnsmgt
version: 4.22
family: networking
documentKind: "Documentation"
---

# Understanding DNS management policies

[id="ingress-controller-dnsmgt"]
= Understanding DNS management policies

[role="_abstract"]
As a cluster administrator, when you create an Ingress Controller, the Operator manages the DNS records automatically. This approach has some limitations when the required DNS zone is different from the cluster DNS zone or when the DNS zone is hosted outside the cloud provider.

The following list details key aspects for a managed DNS management policy:

* The Managed DNS management policy for Ingress Controllers ensures that the lifecycle of the wildcard DNS record on the cloud provider is automatically managed by the Operator. This is the default behavior.

* When you change an Ingress Controller from `Managed` to `Unmanaged` DNS management policy, the Operator does not clean up the previous wildcard DNS record provisioned on the cloud.

* When you change an Ingress Controller from `Unmanaged` to `Managed` DNS management policy, the Operator attempts to create the DNS record on the cloud provider if it does not exist or updates the DNS record if it already exists.

The following list details key aspects for a unmanaged DNS management policy:

* The Unmanaged DNS management policy for Ingress Controllers ensures that the lifecycle of the wildcard DNS record on the cloud provider is not automatically managed; instead, it becomes the responsibility of the cluster administrator.
+
[NOTE]
====
For {gcp-first} installations, you can use a custom DNS solution. Refer to the `DNSRecord` CR for information on what you need to include in the DNS record. For more information, see Enabling a user-managed DNS and Provisioning your own DNS records.
====

// Module included in the following assemblies:
//
// *ingress-controller-dnsmgt.adoc

[id="creating-a-custom-ingress-controller_{context}"]
= Creating an Ingress Controller for manual DNS management

[role="_abstract"]
As a cluster administrator, you can create a new custom Ingress Controller with the Unmanaged DNS management policy.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in as a user with `cluster-admin` privileges.

.Procedure

. Create an `IngressController` custom resource (CR) file named `sample-ingress.yaml` with the following content:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: <name>
spec:
  domain: <domain>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: External
      dnsManagementPolicy: Unmanaged
----
+
where:
+
`metadata.name`:: Specify the `<name>` with a name for the `IngressController` object.
`spec.domain`:: Specify the `domain` based on the DNS record that was created as a prerequisite.
`loadBalancer.scope`:: Specify the `scope` as `External` to expose the load balancer externally.
`loadBalancer.dnsManagementPolicy`: Specifies if the Ingress Controller is managing the lifecycle of the wildcard DNS record associated with the load balancer. The valid values are `Managed` and `Unmanaged`. The default value is `Managed`.

. Apply the manifest to create the `IngressController` object:
+
[source,terminal]
----
$ oc apply -f sample-ingress.yaml
----

. Verify that the Ingress Controller was created with the correct policy by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller <name> -n openshift-ingress-operator -o=jsonpath={.spec.endpointPublishingStrategy.loadBalancer}
----
+
Inspect the output and confirm that `dnsManagementPolicy` is set to `Unmanaged`.

// Module included in the following assemblies:
//
// *ingress-controller-dnsmgt.adoc

[id="modifying-an-existing-ingress-controller_{context}"]
= Modifying an existing Ingress Controller for manual DNS management

[role="_abstract"]
As a cluster administrator, you can modify an existing Ingress Controller to manually manage the DNS record lifecycle.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in as a user with `cluster-admin` privileges.

.Procedure

. Modify the chosen Ingress Controller to set the `dnsManagementPolicy` parameter:
+
[source,terminal]
----
$ SCOPE=$(oc -n openshift-ingress-operator get ingresscontroller <name> -o=jsonpath="{.status.endpointPublishingStrategy.loadBalancer.scope}")
----
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch="{\"spec\":{\"endpointPublishingStrategy\":{\"type\":\"LoadBalancerService\",\"loadBalancer\":{\"dnsManagementPolicy\":\"Unmanaged\", \"scope\":\"${SCOPE}\"}}}}"
ingresscontroller.operator.openshift.io/default patched
----

. Verify that the Ingress Controller was modified correctly by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller <name> -n openshift-ingress-operator -o=jsonpath={.spec.endpointPublishingStrategy.loadBalancer}
----
+
Inspect the output and confirm that `dnsManagementPolicy` is set to `Unmanaged`.

[role="_additional-resources"]
[id="configuring-ingress-controller-dns-management-additional-resources"]
== Additional resources
* Ingress Controller configuration parameters
