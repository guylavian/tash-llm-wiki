---
title: "Traffic management"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-traffic-manage-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-traffic-manage
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Traffic management

[id="ossm-routing-traffic-v1x"]
= Traffic management

You can control the flow of traffic and API calls between services in {SMProductName}. For example, some services in your service mesh may need to communicate within the mesh and others may need to be hidden. Manage the traffic to hide specific backend services, expose services, create testing or versioning deployments, or add a security layer on a set of services.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-gateways_{context}"]
= Using gateways

You can use a gateway to manage inbound and outbound traffic for your mesh to specify which traffic you want to enter or leave the mesh. Gateway configurations are applied to standalone Envoy proxies that are running at the edge of the mesh, rather than sidecar Envoy proxies running alongside your service workloads.

Unlike other mechanisms for controlling traffic entering your systems, such as the Kubernetes Ingress APIs, {SMProductName} gateways use the full power and flexibility of traffic routing.

The {SMProductName} gateway resource can use layer 4-6 load balancing properties, such as ports, to expose and configure {SMProductName} TLS settings. Instead of adding application-layer traffic routing (L7) to the same API resource, you can bind a regular {SMProductName} virtual service to the gateway and manage gateway traffic like any other data plane traffic in a service mesh.

Gateways are primarily used to manage ingress traffic, but you can also configure egress gateways. An egress gateway lets you configure a dedicated exit node for the traffic leaving the mesh. This enables you to limit which services have access to external networks, which adds security control to your service mesh. You can also use a gateway to configure a purely internal proxy.

.Gateway example

A gateway resource describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. The specification describes a set of ports that should be exposed, the type of protocol to use, SNI configuration for the load balancer, and so on.

The following example shows a sample gateway configuration for external HTTPS ingress traffic:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: ext-host-gwy
spec:
  selector:
    istio: ingressgateway # use istio default controller
  servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
    - ext-host.example.com
    tls:
      mode: SIMPLE
      serverCertificate: /tmp/tls.crt
      privateKey: /tmp/tls.key
----

This gateway configuration lets HTTPS traffic from `ext-host.example.com` into the mesh on port 443, but doesn’t specify any routing for the traffic.

To specify routing and for the gateway to work as intended, you must also bind the gateway to a virtual service. You do this using the virtual service's gateways field, as shown in the following example:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: virtual-svc
spec:
  hosts:
  - ext-host.example.com
  gateways:
    - ext-host-gwy
----

You can then configure the virtual service with routing rules for the external traffic.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-ingress-gateway_{context}"]
= Configuring an ingress gateway

An ingress gateway is a load balancer operating at the edge of the mesh that receives incoming HTTP/TCP connections. It configures exposed ports and protocols but does not include any traffic routing configuration. Traffic routing for ingress traffic is instead configured with routing rules, the same way as for internal service requests.

The following steps show how to create a gateway and configure a `VirtualService` to expose a service in the Bookinfo sample application to outside traffic for paths `/productpage` and `/login`.

.Procedure

. Create a gateway to accept traffic.
+
.. Create a YAML file, and copy the following YAML into it.
+
.Gateway example gateway.yaml
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: bookinfo-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
----
+
.. Apply the YAML file.
+
[source,terminal]
----
$ oc apply -f gateway.yaml
----

. Create a `VirtualService` object to rewrite the host header.
+
.. Create a YAML file, and copy the following YAML into it.
+
.Virtual service example
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - "*"
  gateways:
  - bookinfo-gateway
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        prefix: /static
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /api/v1/products
    route:
    - destination:
        host: productpage
        port:
          number: 9080
----
+
.. Apply the YAML file.
+
[source,terminal]
----
$ oc apply -f vs.yaml
----

. Test that the gateway and VirtualService have been set correctly.
+
.. Set the Gateway URL.
+
[source,terminal]
----
export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
----
+
.. Set the port number. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
export TARGET_PORT=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.port.targetPort}')
----
+
.. Test a page that has been explicitly exposed.
+
[source,terminal]
----
curl -s -I "$GATEWAY_URL/productpage"
----
+
The expected result is `200`.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-ingress_{context}"]
= Managing ingress traffic

In {SMProductName}, the Ingress Gateway enables features such as monitoring, security, and route rules to apply to traffic that enters the cluster. Use a {SMProductShortName} gateway to expose a service outside of the service mesh.

[id="ossm-routing-determine-ingress_{context}"]
== Determining the ingress IP and ports

Ingress configuration differs depending on if your environment supports an external load balancer. An external load balancer is set in the ingress IP and ports for the cluster. To determine if your cluster's IP and ports are configured for external load balancers, run the following command. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.

[source,terminal]
----
$ oc get svc istio-ingressgateway -n istio-system
----

That command returns the `NAME`, `TYPE`, `CLUSTER-IP`, `EXTERNAL-IP`, `PORT(S)`, and `AGE` of each item in your namespace.

If the `EXTERNAL-IP` value is set, your environment has an external load balancer that you can use for the ingress gateway.

If the `EXTERNAL-IP` value is `<none>`, or perpetually `<pending>`, your environment does not provide an external load balancer for the ingress gateway.

TO DO - remove XREF in this module.
Determine the ingress according to your environment. For an environment with load balancer support, Determining ingress ports with a load balancer. For an environment without load balancer support, Determining ingress ports without a load balancer. After you have determined the ingress ports, see Configuring ingress using a gateway to complete your configuration.

[id="ossm-routing-config-ig-lb_{context}"]
=== Determining ingress ports with a load balancer

Follow these instructions if your environment has an external load balancer.

.Procedure

. Run the following command to set the ingress IP and ports. This command sets a variable in your terminal.
+
[source,terminal]
----
$ export INGRESS_HOST=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
----

. Run the following command to set the ingress port.
+
[source,terminal]
----
$ export INGRESS_PORT=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
----

. Run the following command to set the secure ingress port.
+
[source,terminal]
----
$ export SECURE_INGRESS_PORT=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
----

. Run the following command to set the TCP ingress port.
+
[source,terminal]
----
$ export TCP_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="tcp")].port}')
----

[NOTE]
====
In some environments, the load balancer may be exposed using a hostname instead of an IP address. For that case, the ingress gateway's `EXTERNAL-IP` value is not an IP address. Instead, it is a hostname, and the previous command fails to set the `INGRESS_HOST` environment variable.

In that case, use the following command to correct the `INGRESS_HOST` value:
====

[source,terminal]
----
$ export INGRESS_HOST=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
----

[id="ossm-routing-config-ig-no-lb_{context}"]
=== Determining ingress ports without a load balancer

If your environment does not have an external load balancer, determine the ingress ports and use a node port instead.

.Procedure

. Set the ingress ports.
+
[source,terminal]
----
$ export INGRESS_PORT=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
----

. Run the following command to set the secure ingress port.
+
[source,terminal]
----
$ export SECURE_INGRESS_PORT=$(oc -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
----

. Run the following command to set the TCP ingress port.
+
[source,terminal]
----
$ export TCP_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="tcp")].nodePort}')
----

This TASK module included in the following assemblies:
// * service_mesh/v1x/ossm-traffic-manage.adoc

[id="ossm-auto-route-1x_{context}"]
= Automatic route creation

OpenShift routes for Istio Gateways are automatically managed in {SMProductName}. Every time an Istio Gateway is created, updated or deleted inside the service mesh, an OpenShift route is created, updated or deleted.

[id="ossm-auto-route-enable_{context}"]
== Enabling Automatic Route Creation
A {SMProductName} control plane component called Istio OpenShift Routing (IOR) synchronizes the gateway route. Enable IOR as part of the control plane deployment.

If the Gateway contains a TLS section, the OpenShift Route will be configured to support TLS.

. In the `ServiceMeshControlPlane` resource, add the `ior_enabled` parameter and set it to `true`. For example, see the following resource snippet:

[source,yaml]
----
spec:
  istio:
    gateways:
     istio-egressgateway:
       autoscaleEnabled: false
       autoscaleMin: 1
       autoscaleMax: 5
     istio-ingressgateway:
       autoscaleEnabled: false
       autoscaleMin: 1
       autoscaleMax: 5
       ior_enabled: true
----

[id="ossm-auto-route-subdomains_{context}"]
== Subdomains

{SMProductName} creates the route with the subdomain, but OpenShift Container Platform must be configured to enable it. Subdomains, for example `*.domain.com`, are supported but not by default. Configure an OpenShift Container Platform wildcard policy before configuring a wildcard host Gateway. For more information, see the "Links" section.

If the following gateway is created:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: gateway1
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - www.bookinfo.com
    - bookinfo.example.com
----

Then, the following OpenShift Routes are created automatically. You can check that the routes are created with the following command.

[source,terminal]
----
$ oc -n <control_plane_namespace> get routes
----

.Expected output
[source,terminal]
----
NAME           HOST/PORT             PATH  SERVICES               PORT  TERMINATION   WILDCARD
gateway1-lvlfn bookinfo.example.com        istio-ingressgateway   <all>               None
gateway1-scqhv www.bookinfo.com            istio-ingressgateway   <all>               None
----

If the gateway is deleted, {SMProductName} deletes the routes. However, routes created manually are never modified by {SMProductName}.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-service-entries_{context}"]
= Understanding service entries

A service entry adds an entry to the service registry that {SMProductName} maintains internally. After you add the service entry, the Envoy proxies send traffic to the service as if it is a service in your mesh. Service entries allow you to do the following:

* Manage traffic for services that run outside of the service mesh.
* Redirect and forward traffic for external destinations (such as, APIs consumed from the web) or traffic to services in legacy infrastructure.
* Define retry, timeout, and fault injection policies for external destinations.
* Run a mesh service in a Virtual Machine (VM) by adding VMs to your mesh.

[NOTE]
====
Add services from a different cluster to the mesh to configure a multicluster {SMProductName} mesh on Kubernetes.
====

.Service entry examples
The following example is a mesh-external service entry that adds the `ext-resource` external dependency to the {SMProductName} service registry:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: svc-entry
spec:
  hosts:
  - ext-svc.example.com
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  location: MESH_EXTERNAL
  resolution: DNS
----

Specify the external resource using the `hosts` field. You can qualify it fully or use a wildcard prefixed domain name.

You can configure virtual services and destination rules to control traffic to a service entry in the same way you configure traffic for any other service in the mesh. For example, the following destination rule configures the traffic route to use mutual TLS to secure the connection to the `ext-svc.example.com` external service that is configured using the service entry:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: ext-res-dr
spec:
  host: ext-svc.example.com
  trafficPolicy:
    tls:
      mode: MUTUAL
      clientCertificate: /etc/certs/myclientcert.pem
      privateKey: /etc/certs/client_private_key.pem
      caCertificates: /etc/certs/rootcacerts.pem
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-virtual-services_{context}"]
= Using VirtualServices

You can route requests dynamically to multiple versions of a microservice through {SMProductName} with a virtual service. With virtual services, you can:

* Address multiple application services through a single virtual service. If your mesh uses Kubernetes, for example, you can configure a virtual service to handle all services in a specific namespace. A virtual service enables you to turn a monolithic application into a service consisting of distinct microservices with a seamless consumer experience.
* Configure traffic rules in combination with gateways to control ingress and egress traffic.

[id="ossm-routing-vs_{context}"]
== Configuring VirtualServices

Requests are routed to services within a service mesh with virtual services. Each virtual service consists of a set of routing rules that are evaluated in order. {SMProductName} matches each given request to the virtual service to a specific real destination within the mesh.

Without virtual services, {SMProductName} distributes traffic using least requests load balancing between all service instances. With a virtual service, you can specify traffic behavior for one or more hostnames. Routing rules in the virtual service tell {SMProductName} how to send the traffic for the virtual service to appropriate destinations. Route destinations can be versions of the same service or entirely different services.

.Procedure

. Create a YAML file using the following example to route requests to different versions of the Bookinfo sample application service depending on which user connects to the application.
+
.Example VirtualService.yaml
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v3
----

. Run the following command to apply `VirtualService.yaml`, where `VirtualService.yaml` is the path to the file.
+
[source,terminal]
----
$ oc apply -f <VirtualService.yaml>
----

== VirtualService configuration reference

//Need a sentence or two here

[options="header"]
[cols="l, a"]
|===
|Parameter |Description
|spec:
  hosts:
|The `hosts` field lists the virtual service's destination address to which the routing rules apply. This is the address(es) that are used to send requests to the service. The virtual service hostname can be an IP address, a DNS name, or a short name that resolves to a fully qualified domain name.

|spec:
  http:
  - match:
|The `http` section contains the virtual service's routing rules which describe match conditions and actions for routing HTTP/1.1, HTTP2, and gRPC traffic sent to the destination as specified in the hosts field. A routing rule consists of the destination where you want the traffic to go and any specified match conditions.
The first routing rule in the example has a condition that begins with the match field. In this example, this routing applies to all requests from the user `jason`. Add the `headers`, `end-user`, and `exact` fields to select the appropriate requests.

|spec:
  http:
  - match:
    - destination:
|The `destination` field in the route section specifies the actual destination for traffic that matches this condition. Unlike the virtual service's host, the destination's host must be a real destination that exists in the {SMProductName} service registry. This can be a mesh service with proxies or a non-mesh service added using a service entry. In this example, the hostname is a Kubernetes service name:
|===

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-destination-rules_{context}"]
= Understanding destination rules

Destination rules are applied after virtual service routing rules are evaluated, so they apply to the traffic's real destination. Virtual services route traffic to a destination. Destination rules configure what happens to traffic at that destination.

By default, {SMProductName} uses a least requests load balancing policy, where the service instance in the pool with the least number of active connections receives the request. {SMProductName} also supports the following models, which you can specify in destination rules for requests to a particular service or service subset.

* Random: Requests are forwarded at random to instances in the pool.
* Weighted: Requests are forwarded to instances in the pool according to a specific percentage.
* Least requests: Requests are forwarded to instances with the least number of requests.

.Destination rule example

The following example destination rule configures three different subsets for the `my-svc` destination service, with different load balancing policies:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-destination-rule
spec:
  host: my-svc
  trafficPolicy:
    loadBalancer:
      simple: RANDOM
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
    trafficPolicy:
      loadBalancer:
        simple: ROUND_ROBIN
  - name: v3
    labels:
      version: v3
----

This guide references the Bookinfo sample application to provide examples of routing in an example application. Install the Bookinfo application to learn how these routing examples work.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-bookinfo_{context}"]
= Bookinfo routing tutorial

The {SMProductShortName} Bookinfo sample application consists of four separate microservices, each with multiple versions. After installing the Bookinfo sample application, three different versions of the `reviews` microservice run concurrently.

When you access the Bookinfo app `/product` page in a browser and refresh several times, sometimes the book review output contains star ratings and other times it does not. Without an explicit default service version to route to, {SMProductShortName} routes requests to all available versions one after the other.

This tutorial helps you apply rules that route all traffic to `v1` (version 1) of the microservices. Later, you can apply a rule to route traffic based on the value of an HTTP request header.

.Prerequisites

* Deploy the Bookinfo sample application to work with the following examples.

[id="ossm-routing-bookinfo-applying_{context}"]
= Applying a virtual service

In the following procedure, the virtual service routes all traffic to `v1` of each micro-service by applying virtual services that set the default version for the micro-services.

.Procedure

. Apply the virtual services.
+
[source,bash,subs="attributes"]
----
$ oc apply -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/virtual-service-all-v1.yaml
----

. To verify that you applied the virtual services, display the defined routes with the following command:
+
[source,terminal]
----
$ oc get virtualservices -o yaml
----
+
That command returns a resource of `kind: VirtualService` in YAML format.

You have configured {SMProductShortName} to route to the `v1` version of the Bookinfo microservices including the `reviews` service version 1.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc
[id="ossm-routing-bookinfo-test_{context}"]
= Testing the new route configuration

Test the new configuration by refreshing the `/productpage` of the Bookinfo application.

.Procedure

. Set the value for the `GATEWAY_URL` parameter. You can use this variable to find the URL for your Bookinfo product page later. In this example, istio-system is the name of the control plane project.
+
[source,terminal]
----
export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
----

. Run the following command to retrieve the URL for the product page.
+
[source,terminal]
----
echo "http://$GATEWAY_URL/productpage"
----

. Open the Bookinfo site in your browser.

The reviews part of the page displays with no rating stars, no matter how many times you refresh. This is because you configured {SMProductShortName} to route all traffic for the reviews service to the version `reviews:v1` and this version of the service does not access the star ratings service.

Your service mesh now routes traffic to one version of a service.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc
[id="ossm-routing-bookinfo-route_{context}"]
= Route based on user identity

Change the route configuration so that all traffic from a specific user is routed to a specific service version. In this case, all traffic from a user named `jason` will be routed to the service `reviews:v2`.

{SMProductShortName} does not have any special, built-in understanding of user identity. This example is enabled by the fact that the `productpage` service adds a custom `end-user` header to all outbound HTTP requests to the reviews service.

.Procedure

. Run the following command to enable user-based routing in the Bookinfo sample application.
+
[source,bash,subs="attributes"]
----
$ oc apply -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/virtual-service-reviews-test-v2.yaml
----

. Run the following command to confirm the rule is created. This command returns all resources of `kind: VirtualService` in YAML format.
+
[source,terminal]
----
$ oc get virtualservice reviews -o yaml
----

. On the `/productpage` of the Bookinfo app, log in as user `jason` with no password.
+
. Refresh the browser. The star ratings appear next to each review.

. Log in as another user (pick any name you want). Refresh the browser. Now the stars are gone. Traffic is now routed to `reviews:v1` for all users except Jason.

You have successfully configured the Bookinfo sample application to route traffic based on user identity.

[role="_additional-resources-traffic-management"]
== Additional resources
For more information about configuring an OpenShift Container Platform wildcard policy, see "Using wildcard routes" in Ingress Operator in OpenShift Container Platform.
