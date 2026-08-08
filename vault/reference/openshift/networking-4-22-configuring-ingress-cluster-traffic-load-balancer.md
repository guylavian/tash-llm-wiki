---
title: "Configuring ingress cluster traffic using a load balancer"
type: reference
domain: openshift
slug: networking-4-22-configuring-ingress-cluster-traffic-load-balancer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ingress-cluster-traffic-load-balancer
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring ingress cluster traffic using a load balancer

[id="configuring-ingress-cluster-traffic-load-balancer"]
= Configuring ingress cluster traffic using a load balancer

[role="_abstract"]
OpenShift Container Platform provides methods for communicating from outside the cluster with services running in the cluster. This method uses a load balancer.

Before starting the following procedures, the administrator must complete the following prerequisite tasks:

* Set up the external port to the cluster networking environment so that requests can reach the cluster.

* Have an OpenShift Container Platform cluster with at least one control plane node, at least one compute node, and a system outside the cluster that has network access to the cluster. This procedure assumes that the external system is on the same subnet as the cluster. The additional networking required for external systems on a different subnet is out-of-scope for this topic.

* Make sure there is at least one user with cluster admin role. To add this role to a user, run the following command:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user cluster-admin username
----

// Module included in the following assemblies:
//
// * ingress/getting-traffic-cluster.adoc

[id="nw-using-load-balancer-getting-traffic_{context}"]
= Using a load balancer to get traffic into the cluster

[role="_abstract"]
If you do not need a specific external IP address, you can configure a load balancer service to allow external access to an OpenShift Container Platform cluster.

A load balancer service allocates a unique IP. The load balancer has a single edge router IP, which can be a virtual IP (VIP), but is still a single machine for initial load balancing.

[NOTE]
====
A pool gets configured at the infrastructure level and not the cluster administrator level.
====

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

// Module included in the following assemblies:
//
// * ingress/getting-traffic-cluster.adoc

[id="nw-create-load-balancer-service_{context}"]
= Creating a load balancer service

[role="_abstract"]
To distribute incoming traffic efficiently and ensure high availability for your applications in OpenShift Container Platform, create a load balancer service.

.Prerequisites

* Make sure that the project and service you want to expose exist.
* Your cloud provider supports load balancers.

.Procedure

. Log in to OpenShift Container Platform.

. Load the project where the service you want to expose is located.
+
.Example command
[source,terminal]
----
$ oc project project1
----

. Open a text file on the control plane node and paste the following text into the file. Edit the file as needed.
+
.Sample load balancer configuration file
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: egress-2
spec:
  ports:
  - name: db
    port: 3306
  loadBalancerIP:
  loadBalancerSourceRanges:
  - 10.0.0.0/8
  - 192.168.0.0/16
  type: LoadBalancer
  selector:
    name: mysql
----
+
where:
+
`metadata.name`:: Specifies a descriptive name for the load balancer service.
`ports.port`:: Specifies the same port that the service you want to expose is listening on.
`loadBalancerSourceRanges`:: Specifies a list of specific IP addresses to restrict traffic through the load balancer. The parameter is ignored if the cloud provider does not support the feature.
`type`:: Specifies `Loadbalancer` as the type.
`selector.name`:: Specifies the name of the service.
+
[NOTE]
====
To restrict the traffic through the load balancer to specific IP addresses, use the `spec.endpointPublishingStrategy.loadBalancer.allowedSourceRanges` Ingress Controller parameter. Do not set the `loadBalancerSourceRanges` parameter.
====

. Save and exit the file.

. Run the following command to create the service:
+
[source,terminal]
----
$ oc create -f <file_name>
----
+
For example:
+
[source,terminal]
----
$ oc create -f mysql-lb.yaml
----

. Execute the following command to view the new service:
+
[source,terminal]
----
$ oc get svc
----
+
.Example output
[source,terminal]
----
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP                             PORT(S)          AGE
egress-2   LoadBalancer   172.30.22.226   ad42f5d8b303045-487804948.example.com   3306:30357/TCP   15m
----
+
The service has an external IP address automatically assigned if there is a cloud provider enabled.

. On the master, use a tool, such as `curl`, to make sure you can reach the service by using the public IP address:
+
[source,terminal]
----
$ curl <public_ip>:<port>
----
+
For example:
+
[source,terminal]
----
$ curl 172.29.121.74:3306
----
+
The examples in this section use a MySQL service, which requires a client application. If you get a string of characters with the `Got packets out of order` message, you are connecting with the service:
+
If you have a MySQL client, log in with the standard CLI command:
+
[source,terminal]
----
$ mysql -h 172.30.131.89 -u admin -p
----
+
.Example output
[source,terminal]
----
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.

MySQL [(none)]>
----
