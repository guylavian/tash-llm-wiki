---
title: "Configuring ingress cluster traffic by using a NodePort"
type: reference
domain: openshift
slug: networking-4-22-configuring-ingress-cluster-traffic-nodeport
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ingress-cluster-traffic-nodeport
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring ingress cluster traffic by using a NodePort

[id="configuring-ingress-cluster-traffic-nodeport"]
= Configuring ingress cluster traffic by using a NodePort

[role="_abstract"]
To enable external access to your application for specific networking requirements, expose a service by using a `NodePort`.

This configuration opens a specific port on every node in the cluster, allowing external traffic to reach your workloads by using an IP address of any node.

OpenShift Container Platform provides methods for communicating from outside the cluster with services running in the cluster. This method uses a `NodePort`.

Before starting the following procedures, the administrator must complete the following prerequisite tasks:

* Set up the external port to the cluster networking environment so that requests can reach the cluster.

* Have an OpenShift Container Platform cluster with at least one control plane node, at least one compute node, and a system outside the cluster that has network access to the cluster. This procedure assumes that the external system is on the same subnet as the cluster. The additional networking required for external systems on a different subnet is out-of-scope for this topic.

* Make sure there is at least one user with cluster admin role. To add this role to a user, run the following command:
+
----
$ oc adm policy add-cluster-role-to-user cluster-admin <user_name>
----

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="nw-using-nodeport_{context}"]
= Using a NodePort to get traffic into the cluster

[role="_abstract"]
Use a `NodePort`-type `Service` resource to expose a service on a specific port on all nodes in the cluster.

The port is specified in the `Service` resource's `.spec.ports[*].nodePort` parameter

[IMPORTANT]
====
Using a node port requires additional port resources.
====

A `NodePort` exposes the service on a static port on the IP address of a node. A `NodePort` spans the `30000` to `32767` IP address ranges by default, which means a `NodePort` is unlikely to match the intended port of a service. For example, port `8080` might be exposed as port `31020` on the node.

The administrator must ensure the external IP addresses are routed to the nodes.

A `NodePort` and external IPs are independent and both can be used concurrently.

// Creating a project and service
// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="nw-creating-project-and-service_{context}"]
= Creating a project and service

[role="_abstract"]
If the project and service that you want to expose does not exist, create the project and then create the service.

If the project and service already exists, skip to the procedure on exposing the service to create a route.

.Prerequisites

* Install the {oc-first} and log in as a cluster administrator.

.Procedure

. Create a new project for your service by running the `oc new-project` command:
+
[source,terminal]
----
$ oc new-project <project_name>
----

. Use the `oc new-app` command to create your service:
+
[source,terminal]
----
$ oc new-app nodejs:12~https://github.com/sclorg/nodejs-ex.git
----

. To verify that the service was created, run the following command:
+
[source,terminal]
----
$ oc get svc -n <project_name>
----
+
.Example output
[source,terminal]
----
NAME        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
nodejs-ex   ClusterIP   172.30.197.157   <none>        8080/TCP   70s
----
+
[NOTE]
====
By default, the new service does not have an external IP address.
====

// Exposing the service by creating a route
// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="nw-exposing-service_{context}"]
= Exposing the service by creating a route

[role="_abstract"]
To enable external access to your application that runs on OpenShift Container Platform, you can expose the service as a route by using the `oc expose` command.

.Prerequisites

* You logged into OpenShift Container Platform.

.Procedure

. Log in to the project where the service you want to expose is located:
+
[source,terminal]
----
$ oc project <project_name>
----

. Run the `oc expose service` command to expose the route:
+
[source,terminal]
----
$ oc expose service nodejs-ex
----
+
.Example output
[source,terminal]
----
route.route.openshift.io/nodejs-ex exposed
----

. To verify that the service is exposed, you can use a tool, such as `curl` to check that the service is accessible from outside the cluster.
+
.. To find the hostname of the route, enter the following command:
+
[source,terminal]
----
$ oc get route
----
+
.Example output
[source,terminal]
----
NAME        HOST/PORT                        PATH   SERVICES    PORT       TERMINATION   WILDCARD
nodejs-ex   nodejs-ex-myproject.example.com         nodejs-ex   8080-tcp                 None
----
+
.. To check that the host responds to a GET request, enter the following command:
+
.Example `curl` command
[source,terminal]
----
$ curl --head nodejs-ex-myproject.example.com
----
+
.Example output
[source,terminal]
----
HTTP/1.1 200 OK
...
----

. To expose a node port for the application, modify the custom resource definition (CRD) of a service by entering the following command:
+
[source,terminal]
----
$ oc edit svc <service_name>
----
+
.Example output
[source,yaml]
----
spec:
  ports:
  - name: 8443-tcp
    nodePort: 30327
    port: 8443
    protocol: TCP
    targetPort: 8443
  sessionAffinity: None
  type: NodePort
----
+
* `nodePort`: Optional parameter. Specifies the node port range for the application. By default, OpenShift Container Platform selects an available port in the `30000-32767` range.
* `type`: Specifies the service type.

. Optional: To confirm the service is available with a node port exposed, enter the following command:
+
[source,terminal]
----
$ oc get svc -n myproject
----
+
.Example output
[source,terminal]
----
NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
nodejs-ex           ClusterIP   172.30.217.127   <none>        3306/TCP         9m44s
nodejs-ex-ingress   NodePort    172.30.107.72    <none>        3306:31345/TCP   39s
----

. Optional: To remove the service created automatically by the `oc new-app` command, enter the following command:
+
[source,terminal]
----
$ oc delete svc nodejs-ex
----

.Verification

* To check that the service node port is updated with a port in the `30000-32767` range, enter the following command:
+
[source,terminal]
----
$ oc get svc
----
+
In the following example output, the updated port is `30327`:
+
.Example output
[source,terminal]
----
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
httpd   NodePort   172.xx.xx.xx    <none>        8443:30327/TCP   109s
----

[role="_additional-resources"]
[id="configuring-ingress-cluster-traffic-nodeport-additional-resources"]
== Additional resources

* Configuring the node port service range

* Adding a single NodePort service to an Ingress Controller
