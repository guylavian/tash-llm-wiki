---
title: "Configuring ingress cluster traffic on AWS"
type: reference
domain: openshift
slug: networking-4-22-configuring-ingress-cluster-traffic-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ingress-cluster-traffic-aws
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring ingress cluster traffic on AWS

[id="configuring-ingress-cluster-traffic-aws"]
= Configuring ingress cluster traffic on AWS

[role="_abstract"]
OpenShift Container Platform provides methods for communicating from outside the cluster with services running in the cluster. This method uses load balancers on {aws-first}, specifically a Network Load Balancer (NLB) or a Classic Load Balancer (CLB). Both types of load balancers can forward the IP address of the client to the node, but a CLB requires proxy protocol support, which OpenShift Container Platform automatically enables.

There are two ways to switch an Ingress Controller from using a CLB to using an NLB. Use only one of these approaches for a given Ingress Controller; do not combine them.

. Force replace the Ingress Controller that is currently using a CLB. This deletes the `IngressController` object and an outage occurs while the new DNS records propagate and the NLB is being provisioned.
. Edit the existing `IngressController` to set `spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.type` to `NLB`. Starting in OpenShift Container Platform 4.22, the cloud controller does not reprovision the load balancer automatically. The `IngressController` displays a `Progressing` condition stating that you must delete the router `Service` in the `openshift-ingress` namespace so that a new load balancer can be created. That interruption can change the load balancer hostname and IP addresses. Complete the subnets update procedure to read the `Progressing` condition and delete the router `Service`.

You can configure these load balancers on a new or existing {aws-short} cluster.

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-configuring-elb-timeouts-aws-classic_{context}"]
= Configuring Classic Load Balancer timeouts on AWS

[role="_abstract"]
To prevent connection drops for long-running processes in OpenShift Container Platform, configure custom timeout periods for specific routes or Ingress Controllers.

Ensure these settings account for the {aws-full} Classic Load Balancer (CLB) default timeout of 60 seconds to maintain stable network traffic.

If the timeout period of the CLB is shorter than the route timeout or Ingress Controller timeout, the load balancer can prematurely terminate the connection. You can prevent this problem by increasing both the timeout period of the route and CLB.

// Module filename: nw-configuring-route-timeouts.adoc
// Module included in the following assemblies:
// * networking/configuring-routing.adoc
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-configuring-route-timeouts_{context}"]
= Configuring route timeouts

[role="_abstract"]
You can configure the default timeouts for an existing route when you have services in need of a low timeout, which is required for Service Level Availability (SLA) purposes, or a high timeout, for cases with a slow back end.

[IMPORTANT]
====
If you configured a user-managed external load balancer in front of your OpenShift Container Platform cluster, ensure that the timeout value for the user-managed external load balancer is higher than the timeout value for the route. This configuration prevents network congestion issues over the network that your cluster uses.
====

.Prerequisites

* You deployed an Ingress Controller on a running cluster.

.Procedure

* Using the `oc annotate` command, add the timeout to the route:
+
[source,terminal]
----
$ oc annotate route <route_name> \
    --overwrite haproxy.router.openshift.io/timeout=<timeout><time_unit>
----
* `<timeout>`: Supported time units are microseconds (us), milliseconds (ms), seconds (s), minutes (m), hours (h), or days (d).
+
The following example sets a timeout of two seconds on a route named `myroute`:
+
[source,terminal]
----
$ oc annotate route myroute --overwrite haproxy.router.openshift.io/timeout=2s
----

// Modules included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-configuring-clb-timeouts_{context}"]
= Configuring Classic Load Balancer timeouts

[role="_abstract"]
You can configure the default timeouts for a Classic Load Balancer (CLB) to extend idle connections.

.Prerequisites

* You must have a deployed Ingress Controller on a running cluster.

.Procedure

. Set an {aws-full} connection idle timeout of five minutes for the default `ingresscontroller` by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default \
    --type=merge --patch='{"spec":{"endpointPublishingStrategy": \
    {"type":"LoadBalancerService", "loadBalancer": \
    {"scope":"External", "providerParameters":{"type":"AWS", "aws": \
    {"type":"Classic", "classicLoadBalancer": \
    {"connectionIdleTimeout":"5m"}}}}}}}'
----

. Optional: Restore the default value of the timeout by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default \
    --type=merge --patch='{"spec":{"endpointPublishingStrategy": \
    {"loadBalancer":{"providerParameters":{"aws":{"classicLoadBalancer": \
    {"connectionIdleTimeout":null}}}}}}}'
----
+
[NOTE]
====
You must specify the `scope` field when you change the connection timeout value unless the current scope is already set. When you set the `scope` field, you do not need to do so again if you restore the default timeout value.
====

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-configuring-ingress-cluster-traffic-aws-network-load-balancer_{context}"]
= Configuring ingress cluster traffic on AWS using a Network Load Balancer

[role="_abstract"]
To enable high-performance communication between external services and your OpenShift Container Platform cluster, configure an {aws-full} Network Load Balancer (NLB). You can set up an NLB on a new or existing {aws-short} cluster to manage ingress traffic with low latency.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-ingress-nlb-dual-stack_{context}"]
= Dual-stack networking for the Ingress Controller load balancer on AWS

[role="_abstract"]
On {aws-full}, an Ingress Controller must use a publishing `Service` type Network Load Balancer (NLB) to enable publishing over IPv4 and IPv6 when the cluster runs {aws-short} dual-stack networking. A Classic Load Balancer (CLB) does not support the dual-stack publishing path.

If your Ingress Controller uses an NLB and the cluster-scoped `Infrastructure` resource named `cluster` contains `DualStackIPv4Primary` or `DualStackIPv6Primary` in the `status.platformStatus.aws.ipFamily` field, the Ingress Operator sets the Ingress Controller load balancer `Service` to dual-stack IP families.

The `Service` lists IPv4 first for `DualStackIPv4Primary` and IPv6 first for `DualStackIPv6Primary`.

If the Ingress Controller uses a CLB and the cluster runs {aws-short} dual-stack networking, the publishing load balancer stays IPv4-only. To expose the Ingress Controller over IPv4 and IPv6, you must configure the Ingress Controller to use an NLB.

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-switching-clb-with-nlb_{context}"]
= Switching the Ingress Controller from using a Classic Load Balancer to a Network Load Balancer

[role="_abstract"]
To improve performance and reduce latency for cluster traffic in OpenShift Container Platform on {aws-full}, switch an Ingress Controller using a Classic Load Balancer (CLB) to one that uses a Network Load Balancer (NLB).

Switching between these load balancers does not delete the `IngressController` object.

[WARNING]
====
This procedure might cause an outage that can last several minutes due to new DNS records propagation, new load balancers provisioning, and other factors. IP addresses and canonical names of the Ingress Controller load balancer might change after applying this procedure.
====

.Procedure

. Modify the existing Ingress Controller that you want to switch to by using an NLB. This example assumes that your default Ingress Controller has an `External` scope and no other customizations:
+
.Example `ingresscontroller.yaml` file
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: NLB
    type: LoadBalancerService
----
+
[NOTE]
====
If you do not specify a value for the `spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.type` field, the Ingress Controller uses the `spec.loadBalancer.platform.aws.type` value from the cluster `Ingress` configuration that was set during installation.
====
+
[TIP]
====
If your Ingress Controller has other customizations that you want to update, such as changing the domain, consider force replacing the Ingress Controller definition file instead.
====

. Apply the changes to the Ingress Controller YAML file by running the command:
+
[source,terminal]
----
$ oc apply -f ingresscontroller.yaml
----

. Check that the `Progressing` condition of the Ingress Controller is set to `True` by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller default -n openshift-ingress-operator -o jsonpath='{.status.conditions[?(@.type=="Progressing")]}'
----

. Delete the service associated with the Ingress Controller by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress delete svc/router-<name>
----
* Replace `<name>` with the specific instance name of your Ingress Controller.
+
Expect several minutes of outages while the Ingress Controller updates.

.Verification

* Confirm that the Ingress Controller updated successfully by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator default -o jsonpath="{.status.conditions}" | yq -PC
----

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-switching-nlb-with-clb_{context}"]
= Switching the Ingress Controller from using a Network Load Balancer to a Classic Load Balancer

[role="_abstract"]
To support specific networking configurations in OpenShift Container Platform on {aws-full}, switch an Ingress Controller using a Network Load Balancer (NLB) to one that uses a Classic Load Balancer (CLB).

Switching between these load balancers does not delete the `IngressController` object.

[WARNING]
====
This procedure might cause an outage that can last several minutes due to new DNS records propagation, new load balancers provisioning, and other factors. IP addresses and canonical names of the Ingress Controller load balancer might change after applying this procedure.
====

.Procedure

. Modify the existing Ingress Controller that you want to switch to using a CLB. This example assumes that your default Ingress Controller has an `External` scope and no other customizations:
+
.Example `ingresscontroller.yaml` file
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: Classic
    type: LoadBalancerService
----
+
[NOTE]
====
If you do not specify a value for the `spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.type` field, the Ingress Controller uses the `spec.loadBalancer.platform.aws.type` value from the cluster `Ingress` configuration that was set during installation.
====
+
[TIP]
====
If your Ingress Controller has other customizations that you want to update, such as changing the domain, consider force replacing the Ingress Controller definition file instead.
====

. Apply the changes to the Ingress Controller YAML file by running the command:
+
[source,terminal]
----
$ oc apply -f ingresscontroller.yaml
----

. Check that the `Progressing` condition of the Ingress Controller is set to `True` by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller default -n openshift-ingress-operator -o jsonpath='{.status.conditions[?(@.type=="Progressing")]}'
----

. Delete the service associated with the Ingress Controller by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress delete svc/router-<name>
----
* Replace `<name>` with the specific instance name of your Ingress Controller.
+
Expect several minutes of outages while the Ingress Controller updates.

.Verification

* Confirm that the Ingress Controller updated successfully by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator default -o jsonpath="{.status.conditions}" | yq -PC
----

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-replacing-clb-with-nlb_{context}"]
= Replacing Ingress Controller Classic Load Balancer with Network Load Balancer

[role="_abstract"]
To improve performance and reduce latency for traffic in OpenShift Container Platform on {aws-full}, replace an Ingress Controller using a Classic Load Balancer (CLB) with one that uses a Network Load Balancer (NLB).

[WARNING]
====
This procedure might cause an outage that can last several minutes due to new DNS records propagation, new load balancers provisioning, and other factors. IP addresses and canonical names of the Ingress Controller load balancer might change after applying this procedure.
====

.Procedure

. Create a file with a new default Ingress Controller. The following example assumes that your default Ingress Controller has an `External` scope and no other customizations:
+
.Example `ingresscontroller.yml` file
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: NLB
    type: LoadBalancerService
----
+
If your default Ingress Controller has other customizations, ensure that you modify the file accordingly.
+
[TIP]
====
If your Ingress Controller has no other customizations and you are only updating the load balancer type, consider following the procedure detailed in "Switching the Ingress Controller from using a Classic Load Balancer to a Network Load Balancer".
====

. Force replace the Ingress Controller YAML file:
+
[source,terminal]
----
$ oc replace --force --wait -f ingresscontroller.yml
----
+
Wait until the Ingress Controller is replaced. Expect several of minutes of outages.

// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-nlb-existing-cluster_{context}"]
= Configuring an Ingress Controller Network Load Balancer on an existing AWS cluster

[role="_abstract"]
To improve performance for high-traffic workloads in OpenShift Container Platform, configure an Ingress Controller backed by an {aws-full} Network Load Balancer (NLB) on an existing cluster.

You can create an Ingress Controller backed by an {aws-full} Network Load Balancer (NLB) on an existing cluster.

.Prerequisites

* You installed an {aws-short} cluster.
* `PlatformStatus` of the infrastructure resource must be {aws-short}.
** To verify that the `PlatformStatus` is {aws-short}, run the following command:
+
[source,terminal]
----
$ oc get infrastructure/cluster -o jsonpath='{.status.platformStatus.type}'
AWS
----

.Procedure

. Create the Ingress Controller manifest:
+
[source,terminal]
----
 $ cat ingresscontroller-aws-nlb.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: <ingress_controller_name>
  namespace: openshift-ingress-operator
spec:
  domain: <unique_ingress_domain
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: NLB
----
+
where:
+
`<ingress_controller_name>`:: Specifies a unique name for the Ingress Controller.
`<unique_ingress_domain>`:: Specifies a domain name that is unique among all Ingress Controllers in the cluster. This variable must be a subdomain of the DNS name `<clustername>.<domain>`.
`scope`:: Specifies the type of NLB, either `External` to use an external NLB or `Internal` to use an internal NLB.

. Create the resource in the cluster:
+
[source,terminal]
----
$ oc create -f ingresscontroller-aws-nlb.yaml
----
+
[IMPORTANT]
====
Before you can configure an Ingress Controller NLB on a new AWS cluster, you must complete the creating the installation configuration file procedure. For more information, see "Creating the installation configuration file".
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-nlb-new-cluster_{context}"]
= Configuring an Ingress Controller Network Load Balancer on a new AWS cluster

[role="_abstract"]
You can create an Ingress Controller backed by an {aws-full} Network Load Balancer (NLB) on a new cluster in situations where you need more transparent networking capabilities.

.Prerequisites

* Create and edit the `install-config.yaml` file. For instructions, see "Creating the installation configuration file" in the _Additonal resources_ section.

.Procedure

. Change to the directory that contains the installation program and create the manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
* For `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.

. Create a file that is named `cluster-ingress-default-ingresscontroller.yaml` in the `<installation_directory>/manifests/` directory:
+
[source,terminal]
----
$ touch <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
----
`<installation_directory>`:: Specifies the directory name that contains the `manifests/` directory for your cluster.

. Check the several network configuration files that exist in the `manifests/` directory by entering the following command:
+
[source,terminal]
----
$ ls <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
----
+
.Example output
[source,terminal]
----
cluster-ingress-default-ingresscontroller.yaml
----

. Open the `cluster-ingress-default-ingresscontroller.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration you want:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: NLB
    type: LoadBalancerService
----

. Save the `cluster-ingress-default-ingresscontroller.yaml` file and quit the text editor.

. Optional: Back up the `manifests/cluster-ingress-default-ingresscontroller.yaml` file because the installation program deletes the `manifests/` directory during cluster creation.

// Modules included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-setting-select-subnet-Loadbalancerservice_{context}"]
= Choosing subnets while creating a LoadBalancerService Ingress Controller

[role="_abstract"]
To manually control network placement for Ingress Controllers in an existing cluster, specify the load balancer subnets in your configuration. This method provides precise control over your infrastructure by overriding the default automatic subnet discovery method used by {aws-full}.

.Prerequisites
* You must have an installed {aws-short} cluster.
* You must know the names or IDs of the subnets to which you intend to map your `IngressController`.

.Procedure

. Create a custom resource (CR) YAML file, such as `sample-ingress.yaml`, and specifying the following content for the file:
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
  dnsManagementPolicy: Managed
# ...
----

. Add subnets to the CR file:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name:  <name>
  namespace: openshift-ingress-operator
spec:
  domain: <domain>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: Classic
          classicLoadBalancer:
            subnets:
              ids:
              - <subnet>
              - <subnet>
              - <subnet>
dnsManagementPolicy: Managed
----
+
where:
+
`name`:: Specifies a name for the `IngressController`.
`domain`:: Specifies the DNS name serviced by the `IngressController`.
`classicLoadBalancer`:: Specifies the type of load balancer, either `classicLoadBalancer` if using a CLB or `networkLoadBalancer` field if using an NLB.
`ids`:: Specifies a subnet by name using the `names` field instead of specifying the subnet by ID. This field is optional.
`<subnet>`:: Specifies the subnet IDs (or names if you using `names`).
+
[IMPORTANT]
====
You can specify a maximum of one subnet per availability zone. Only provide public subnets for external Ingress Controllers and private subnets for internal Ingress Controllers.
====

. Save and apply the CR file by using the {oc-first}:
+
[source,terminal]
----
$  oc apply -f sample-ingress.yaml
----

. Confirm the load balancer was provisioned successfully by checking the `IngressController` conditions.
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator <name> -o jsonpath="{.status.conditions}" | yq -PC
----

// Modules included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-setting-update-subnet-Loadbalancerservice_{context}"]
= Updating the subnets on an existing Ingress Controller

[role="_abstract"]
You can update an `IngressController` with manually specified load balancer subnets in OpenShift Container Platform to avoid any disruptions, to maintain the stability of your services, and to ensure that your network configuration aligns with your specific requirements.

The example in the procedure shows you how to select and apply new subnets, verify the configuration changes, and confirm successful load balancer provisioning.

[WARNING]
====
This procedure may cause an outage that can last several minutes due to new DNS records propagation, new load balancers provisioning, and other factors. IP addresses and canonical names of the Ingress Controller load balancer might change after applying this procedure.
====

.Procedure

. Modify the existing IngressController by specifying the new subnets:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name:  <name>
  namespace: openshift-ingress-operator
spec:
  domain: <domain>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: External
      providerParameters:
        type: AWS
        aws:
          type: Classic
          classicLoadBalancer:
            subnets:
              ids:
              - <updated_subnet>
              - <updated_subnet>
              - <updated_subnet>
# ...
----
+
where:
+
`<name>`:: Specifies a name for the `IngressController`.
`<domain>`:: Specifies the DNS name serviced by the `IngressController`.
`type`:: Specifies the updated subnet IDs (or names if you using `names`).
`classicLoadBalancer`:: You can also use the `networkLoadBalancer` field if using an NLB.
`ids`:: Specifies the subnet by name using the `names` field instead of specifying the subnet by ID. This parameter is optional.
`<updated_subnet>`:: Specifies the updated subnet IDs (or names if you are using `names`).
+
[IMPORTANT]
====
You can specify a maximum of one subnet per availability zone. Only provide public subnets for external Ingress Controllers and private subnets for internal Ingress Controllers.
====

. Examine the `Progressing` condition on the `IngressController` for instructions on how to apply the subnet updates by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator subnets -o jsonpath="{.status.conditions[?(@.type==\"Progressing\")]}" | yq -PC
----
+
.Example output
[source,terminal]
----
lastTransitionTime: "2024-11-25T20:19:31Z"
message: 'One or more status conditions indicate progressing: LoadBalancerProgressing=True (OperandsProgressing: One or more managed resources are progressing: The IngressController subnets were changed from [...] to [...].  To effectuate this change, you must delete the service: `oc -n openshift-ingress delete svc/router-<name>`; the service load-balancer will then be deprovisioned and a new one created. This will most likely cause the new load-balancer to have a different host name and IP address and cause disruption. To return to the previous state, you can revert the change to the IngressController: [...]'
reason: IngressControllerProgressing
status: "True"
type: Progressing
----

. To apply the update, delete the service associated with the Ingress controller by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress delete svc/router-<name>
----

.Verification

* To confirm that the load balancer was provisioned successfully, check the `IngressController` conditions by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator <name> -o jsonpath="{.status.conditions}" | yq -PC
----

// Modules included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-ingress-aws-static-eip-nlb-configuration_{context}"]
= Configuring AWS Elastic IP (EIP) addresses for a Network Load Balancer (NLB)

[role="_abstract"]
You can specify static IPs, otherwise known as elastic IPs, for your network load balancer (NLB) in the Ingress Controller. This is useful in situations where you want to configure appropriate firewall rules for your cluster network.

.Prerequisites
* You must have an installed {aws-full} cluster.
* You must know the names or IDs of the subnets to which you intend to map your `IngressController`.

.Procedure

. Create a YAML file that contains the following example content:
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
    loadBalancer:
      scope: External
      type: LoadBalancerService
      providerParameters:
        type: AWS
        aws:
          type: NLB
          networkLoadBalancer:
            subnets:
              ids:
              - <subnet_ID>
              names:
              - <subnet_A>
              - <subnet_B>
            eipAllocations:
            - <eipalloc_A>
            - <eipalloc_B>
            - <eipalloc_C>
----
+
where:
+
`<name>`:: Specifies a name for the Ingress Controller.
`<domain>`:: Specifies the DNS name serviced by the Ingress Controller.
`scope`:: Specifies a scope for the EIPs. The scope must be set to the value `External` and be Internet-facing in order to allocate EIPs.
`subnets:: Specifies the IDs and names for your subnets. The total number of IDs and names must be equal to your allocated EIPs.
`eipAllocations`:: Specifies the EIP addresses.
+
[IMPORTANT]
====
You can specify a maximum of one subnet per availability zone. Only provide public subnets for external Ingress Controllers. You can associate one EIP address per subnet.
====

. Save and apply the CR file by entering the following command:
+
[source,terminal]
----
$  oc apply -f sample-ingress.yaml
----

.Verification

. Confirm the load balancer was provisioned successfully by checking the `IngressController` conditions by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller -n openshift-ingress-operator <name> -o jsonpath="{.status.conditions}" | yq -PC
----

[id="additional-resources_configuring-ingress-cluster-traffic-aws"]
[role="_additional-resources"]
== Additional resources

* Converting to a dual-stack cluster network
* Enabling features using feature gates
* Creating the installation configuration file
* Infrastructure cluster configuration API
* Installing a cluster on AWS with network customizations
* Network Load Balancer support on AWS
* Configure proxy protocol support for your Classic Load Balancer
