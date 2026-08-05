---
title: "Configuring ingress cluster traffic for a service external IP"
type: reference
domain: openshift
slug: networking-4-22-configuring-ingress-cluster-traffic-service-external-ip
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ingress-cluster-traffic-service-external-ip
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring ingress cluster traffic for a service external IP

[id="configuring-ingress-cluster-traffic-service-external-ip"]
= Configuring ingress cluster traffic for a service external IP

[role="_abstract"]
You can use either a MetalLB implementation or an IP failover deployment to attach an ExternalIP resource to a service so that the service is available to traffic outside your OpenShift Container Platform cluster.

Hosting an external IP address in this way is only applicable for a cluster installed on bare-metal hardware.

You must ensure that you correctly configure the external network infrastructure to route traffic to the service.

Before you begin the procedure, ensure that you meet the following prerequisite:

* You configured your cluster with ExternalIPs enabled. For more information, see "Configuring ExternalIPs for services" in the _Additional resources_ section.

[NOTE]
====
Do not use the same ExternalIP for the egress IP.
====

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-service-external-ip.adoc

[id="nw-service-externalip-create_{context}"]
= Attaching an ExternalIP to a service

[role="_abstract"]
You can attach an ExternalIP resource to a service. If you configured your cluster to automatically attach the resource to a service, you might not need to manually attach an ExternalIP to the service.

The examples in the procedure use a scenario that manually attaches an ExternalIP resource to a service in a cluster with an IP failover configuration.

.Procedure

. Confirm compatible IP address ranges for the ExternalIP resource by entering the following command in your CLI:
+
[source,terminal]
----
$ oc get networks.config cluster -o jsonpath='{.spec.externalIP}{"\n"}'
----
+
[NOTE]
====
If `autoAssignCIDRs` is set and you did not specify a value for `spec.externalIPs` in the ExternalIP resource, OpenShift Container Platform automatically assigns ExternalIP to a new `Service` object.
====

. Choose one of the following options to attach an ExternalIP resource to the service:
+
.. If you are creating a new service, specify a value in the `spec.externalIPs` parameter and array of one or more valid IP addresses in the `allowedCIDRs` parameter.
+
.Example of service YAML configuration file that supports an ExternalIP resource
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: svc-with-externalip
spec:
  externalIPs:
    policy:
      allowedCIDRs:
      - 192.168.123.0/28
# ...
----
+
.. If you are attaching an ExternalIP to an existing service, enter the following command. Replace `<name>` with the service name. Replace `<ip_address>` with a valid ExternalIP address. You can provide multiple IP addresses separated by commas.
+
[source,terminal]
----
$ oc patch svc <name> -p \
  '{
    "spec": {
      "externalIPs": [ "<ip_address>" ]
    }
  }'
----
+
For example:
+
[source,terminal]
----
$ oc patch svc mysql-55-rhel7 -p '{"spec":{"externalIPs":["192.174.120.10"]}}'
----
+
.Example output
[source,terminal]
----
"mysql-55-rhel7" patched
----

. To confirm that an ExternalIP address is attached to the service, enter the following command. If you specified an ExternalIP for a new service, you must create the service first.
+
[source,terminal]
----
$ oc get svc
----
+
.Example output
[source,terminal]
----
NAME               CLUSTER-IP      EXTERNAL-IP     PORT(S)    AGE
mysql-55-rhel7     172.30.131.89   192.174.120.10  3306/TCP   13m
----

[role="_additional-resources"]
[id="configuring-ingress-cluster-traffic-service-external-ip-additional-resources"]
== Additional resources

Configuring ExternalIPs for services

* About MetalLB and the MetalLB Operator

* Configuring IP failover

* Configuring ExternalIPs for services
