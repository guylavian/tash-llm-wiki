---
title: "Configuring the Ingress Controller endpoint publishing strategy"
type: reference
domain: openshift
slug: networking-4-22-nw-configuring-ingress-controller-endpoint-publishing-strategy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/nw-configuring-ingress-controller-endpoint-publishing-strategy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the Ingress Controller endpoint publishing strategy

[id="nw-configuring-ingress-controller-endpoint-publishing-strategy"]
= Configuring the Ingress Controller endpoint publishing strategy

[role="_abstract"]
To expose Ingress Controller endpoints to external systems and enable load balancer integrations in OpenShift Container Platform, configure the `endpointPublishingStrategy` parameter.

[IMPORTANT]
====
On {rh-openstack-first}, the `LoadBalancerService` endpoint publishing strategy is supported only if a cloud provider is configured to create health monitors. For {rh-openstack} 16.2, this strategy is possible only if you use the Amphora Octavia provider.

For more information, see the "Setting {rh-openstack} Cloud Controller Manager options" section of the {rh-openstack} installation documentation.
====

// Ingress Controller endpoint publishing strategy
// Module included in the following assemblies:
//
// * networking/nw-configuring-ingress-controller-endpoint-publishing-strategy.adoc

[id="nw-ingress-controller-endpoint-publishing-strategies_{context}"]
= Ingress Controller endpoint publishing strategy

[role="_abstract"]
To expose Ingress Controller endpoints to external networks in OpenShift Container Platform, configure either the `NodePortService` endpoint publishing strategy or the `HostNetwork` endpoint publishing strategy.

`NodePortService` endpoint publishing strategy::

The `NodePortService` endpoint publishing strategy publishes the Ingress Controller using a Kubernetes NodePort service.

In this configuration, the Ingress Controller deployment uses container networking. A `NodePortService` is created to publish the deployment. The specific node ports are dynamically allocated by OpenShift Container Platform; however, to support static port allocations, your changes to the node port field of the managed `NodePortService` are preserved.

.Diagram of NodePortService
image::202_OpenShift_Ingress_0222_node_port.png[OpenShift Container Platform Ingress NodePort endpoint publishing strategy]

The preceding graphic shows the following concepts pertaining to OpenShift Container Platform Ingress NodePort endpoint publishing strategy:

* All the available nodes in the cluster have their own, externally accessible IP addresses. The service running in the cluster is bound to the unique NodePort for all the nodes.
* When the client connects to a node that is down, for example, by connecting the `10.0.128.4` IP address in the graphic, the node port directly connects the client to an available node that is running the service. In this scenario, no load balancing is required. As the image shows, the `10.0.128.4` address is down and another IP address must be used instead.

[NOTE]
====
The Ingress Operator ignores any updates to `.spec.ports[].nodePort` fields of the service.

By default, ports are allocated automatically and you can access the port allocations for integrations. However, sometimes static port allocations are necessary to integrate with existing infrastructure which may not be easily reconfigured in response to dynamic ports. To achieve integrations with static node ports, you can update the managed service resource directly.
====

For more information, see the Kubernetes Services documentation on `NodePort`.

`HostNetwork` endpoint publishing strategy*::

The `HostNetwork` endpoint publishing strategy publishes the Ingress Controller on node ports where the Ingress Controller is deployed.

An Ingress Controller with the `HostNetwork` endpoint publishing strategy can have only one pod replica per node. If you want _n_ replicas, you must use at least _n_ nodes where those replicas can be scheduled. Because each pod replica requests ports `80` and `443` on the node host where it is scheduled, a replica cannot be scheduled to a node if another pod on the same node is using those ports.

The `HostNetwork` object has a `hostNetwork` field with the following default values for the optional binding ports: `httpPort: 80`, `httpsPort: 443`, and `statsPort: 1936`. By specifying different binding ports for your network, you can deploy multiple Ingress Controllers on the same node for the `HostNetwork` strategy.

.Example
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: internal
  namespace: openshift-ingress-operator
spec:
  domain: example.com
  endpointPublishingStrategy:
    type: HostNetwork
    hostNetwork:
      httpPort: 80
      httpsPort: 443
      statsPort: 1936
----

// Configuring the Ingress Controller endpoint publishing scope to Internal
// Module included in the following assemblies:
//
// *networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="nw-ingresscontroller-change-internal_{context}"]
= Configuring the Ingress Controller endpoint publishing scope to Internal

[role="_abstract"]
As a cluster administrator, when you install a new cluster without specifying that the cluster is private, the default Ingress Controller is created with a `scope` set to `External`. You can change an `External` scoped Ingress Controller to `Internal`.

.Prerequisites

* You installed the {oc-first}.

.Procedure

* To change an `External`-scoped Ingress Controller to `Internal`, enter the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch='{"spec":{"endpointPublishingStrategy":{"type":"LoadBalancerService","loadBalancer":{"scope":"Internal"}}}}'
----

.Verification

* To check the status of the Ingress Controller, enter the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator get ingresscontrollers/default -o yaml
----
+
** The `Progressing` status condition indicates whether you must take further action. For example, the status condition can indicate that you need to delete the service by entering the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress delete services/router-default
----
+
If you delete the service, the Ingress Operator recreates it as `Internal`.

// Configuring the Ingress Controller endpoint publishing scope to External
// Module included in the following assemblies:
//
// *networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="nw-ingresscontroller-change-external_{context}"]
= Configuring the Ingress Controller endpoint publishing scope to External

[role="_abstract"]
As an installation or post-installation task, a cluster administrator can configure the Ingress Controller to `Internal`. Additionally, a cluster administrator can change an `Internal` Ingress Controller to `External`.

When you install a new cluster without specifying that the cluster is private, the default Ingress Controller is created with a `scope` set to `External`.

[IMPORTANT]
====
On some platforms, it is necessary to delete and recreate the service.

Changing the scope can cause disruption to Ingress traffic, potentially for several minutes. This applies to platforms where it is necessary to delete and recreate the service, because the procedure can cause OpenShift Container Platform to deprovision the existing service load balancer, provision a new one, and update DNS.
====

.Prerequisites

* You installed the {oc-first}.

.Procedure

* To change an `Internal`-scoped Ingress Controller to `External`, enter the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontrollers/private --type=merge --patch='{"spec":{"endpointPublishingStrategy":{"type":"LoadBalancerService","loadBalancer":{"scope":"External"}}}}'
----

.Verification

* To check the status of the Ingress Controller, enter the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator get ingresscontrollers/default -o yaml
----
+
** The `Progressing` status condition indicates whether you must take further action. For example, the status condition can indicate that you need to delete the service by entering the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress delete services/router-default
----
+
If you delete the service, the Ingress Operator recreates it as `External`.

// Adding a single NodePort service to an Ingress Controller
// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/nw-configuring-ingress-controller-endpoint-publishing-strategy.adoc

[id="nw-ingress-controller-nodeportservice-projects_{context}"]
= Adding a single NodePort service to an Ingress Controller

[role="_abstract"]
To prevent port conflicts, instead of creating a `NodePort`-type `Service` for each project, create a custom Ingress Controller that can use the `NodePortService` endpoint publishing strategy.

Consider this configuration for your Ingress Controller when you want to apply a set of routes, through Ingress sharding, to nodes that might already have a `HostNetwork` Ingress Controller.

Before you set a `NodePort`-type `Service` for each project, read the following considerations:

* You must create a wildcard DNS record for the `Nodeport` Ingress Controller domain. A Nodeport Ingress Controller route can be reached from the address of a worker node. For more information about the required DNS records for routes, see "User-provisioned DNS requirements".
* You must expose a route for your service and specify the `--hostname` argument for your custom Ingress Controller domain.
* You must append the port that is assigned to the `NodePort`-type `Service` in the route so that you can access application pods.

.Prerequisites

* You installed the {oc-first}.
* Logged in as a user with `cluster-admin` privileges.
* You created a wildcard DNS record.
// https://docs.openshift.com/container-platform/4.17/networking/ingress-controller-dnsmgt.html (does not detail how to create the DNS)

.Procedure

. Create a custom resource (CR) file for the Ingress Controller:
+
.Example of a CR file that defines information for the `IngressController` object
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: <custom_ic_name>
  namespace: openshift-ingress-operator
spec:
  replicas: 1
  domain: <custom_ic_domain_name>
  nodePlacement:
    nodeSelector:
      matchLabels:
        <key>: <value>
  namespaceSelector:
    matchLabels:
      <key>: <value>
  endpointPublishingStrategy:
    type: NodePortService
# ...
----
+
where:
+
`metadata.name`:: Specifies a custom `name` for the `IngressController` CR.
`spec.domain`:: Specifies the DNS name that the Ingress Controller services. For example, the default ingresscontroller domain is `apps.ipi-cluster.example.com`, so you would specify the `<custom_ic_domain_name>` as `nodeportsvc.ipi-cluster.example.com`.
`nodeSelector.matchLabels.<key>`:: Specifies the label for the nodes that include the custom Ingress Controller.
`namespaceSelector.matchLabels.<key>`:: Specifies the label for a set of namespaces. Substitute `<key>:<value>` with a map of key-value pairs where `<key>` is a unique name for the new label and `<value>` is its value. For example: `ingresscontroller: custom-ic`.

. Add a label to a node by using the `oc label node` command:
+
[source,terminal]
----
$ oc label node <node_name> <key>=<value>
----
+
* `<key>=<value>`: Where `<value>` must match the key-value pair specified in the `nodePlacement` section of your `IngressController` CR.

. Create the `IngressController` object:
+
[source,terminal]
----
$ oc create -f <ingress_controller_cr>.yaml
----

. Find the port for the service created for the `IngressController` CR:
+
[source,terminal]
----
$ oc get svc -n openshift-ingress
----
+
.Example output that shows port `80:32432/TCP` for the `router-nodeport-custom-ic3` service
[source,terminal]
----
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                     AGE
router-internal-default      ClusterIP   172.30.195.74    <none>        80/TCP,443/TCP,1936/TCP                     223d
router-nodeport-custom-ic3   NodePort    172.30.109.219   <none>        80:32432/TCP,443:31366/TCP,1936:30499/TCP   155m
----

. To create a new project, enter the following command:
+
[source,terminal]
----
$ oc new-project <project_name>
----

. To label the new namespace, enter the following command:
+
[source,terminal]
----
$ oc label namespace <project_name> <key>=<value>
----
+
* `<key>=<value>`:: Where `<key>=<value>` must match the value in the `namespaceSelector` section of your Ingress Controller CR.

. Create a new application in your cluster:
+
[source,terminal]
----
$ oc new-app --image=<image_name>
----
+
* `<image_name>`: An example of `<image_name>` is `quay.io/openshifttest/hello-openshift:multiarch`.

. Create a `Route` object for a service, so that the pod can use the service to expose the application external to the cluster.
+
[source,terminal]
----
$ oc expose svc/<service_name> --hostname=<svc_name>-<project_name>.<custom_ic_domain_name>
----
+
[NOTE]
====
You must specify the domain name of your custom Ingress Controller in the `--hostname` argument. If you do not do this, the Ingress Operator uses the default Ingress Controller to serve all the routes for your cluster.
====

. Check that the route has the `Admitted` status and that it includes metadata for the custom Ingress Controller:
+
[source,terminal,subs="quotes,attributes"]
----
$ oc get route/hello-openshift -o json | jq '.status.ingress'
----
+
.Example output
[source,terminal]
----
# ...
{
  "conditions": [
    {
      "lastTransitionTime": "2024-05-17T18:25:41Z",
      "status": "True",
      "type": "Admitted"
    }
  ],
  [
    {
      "host": "hello-openshift.nodeportsvc.ipi-cluster.example.com",
      "routerCanonicalHostname": "router-nodeportsvc.nodeportsvc.ipi-cluster.example.com",
      "routerName": "nodeportsvc", "wildcardPolicy": "None"
    }
  ],
}
----

. Update the default `IngressController` CR to prevent the default Ingress Controller from managing the `NodePort`-type `Service`. The default Ingress Controller will continue to monitor all other cluster traffic.
+
[source,terminal]
----
$ oc patch --type=merge -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"namespaceSelector":{"matchExpressions":[{"key":"<key>","operator":"NotIn","values":["<value>]}]}}}'
----

.Verification

. Verify that the DNS entry can route inside and outside of your cluster by entering the following command. The command outputs the IP address of the node that received the label from running the `oc label node` command earlier in the procedure.
+
[source,terminal]
----
$ dig +short <svc_name>-<project_name>.<custom_ic_domain_name>
----

. To verify that your cluster uses the IP addresses from external DNS servers for DNS resolution, check the connection of your cluster by entering the following command:
+
[source,terminal]
----
$ curl <svc_name>-<project_name>.<custom_ic_domain_name>:<port> <1>
----
+
* `<custom_ic_domain_name>:<port>`: Where `<port>` is the node port from the `NodePort`-type `Service`. Based on example output from the `oc get svc -n openshift-ingress` command, the `80:32432/TCP` HTTP route means that `32432` is the node port.
+
.Output example
[source,terminal]
----
Hello OpenShift!
----

[role="_additional-resources"]
== Additional resources

* Ingress Controller configuration parameters

* Setting {rh-openstack} Cloud Controller Manager options

* User-provisioned DNS requirements
