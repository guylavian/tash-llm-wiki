---
title: "Configuring routes"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-configuring-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-configuring-routes
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Configuring routes

[id="microshift-configuring-routes"]
= Configuring routes

[role="_abstract"]
To enable {microshift-short} node access for services, configure the cluster routes. By using this configuration, you can expose specific applications directly through the network interface of the node.

Secure routes provide the ability to use several types of TLS termination to serve certificates to the client. See the _Additional resources_ section for links to the {OCP} documentation that describe how to create re-encrypt, edge, and passthrough routes with custom certificates.

//OCP module, edit with care; Creating an insecure/http route
// Module included in the following assemblies:
//
// * microshift_networking/microshift-configuring-routes.adoc

[id="microshift-nw-creating-a-route_{context}"]
= Creating an HTTP-based route

[role="_abstract"]
To host your application at a public URL by using the basic HTTP routing protocol, create an HTTP-based route. This configuration exposes a service on an unsecured application port, allowing external access without TLS encryption.

A route can either be secure or unsecured, depending on the network security configuration of your application.

The following procedure describes how to create a simple HTTP-based route to a web application, using the `hello-microshift` application as an example.

.Prerequisites

* You installed the {oc-first}.
* You have access to your {microshift-short} node.
* You have a web application that exposes a port and a TCP endpoint listening for traffic on the port.

.Procedure

. Create a service called `hello-microshift` by running the following command:
+
[source,terminal]
----
$ oc expose pod hello-microshift -n $namespace
----

. Create an unsecured route to the `hello-microshift` application by running the following command:
+
[source,terminal]
----
$ oc expose svc/hello-microshift --hostname=microshift.com $namespace
----

.Verification

* Verify that the `route` resource was created by running the following command:
+
[source,terminal]
----
$ oc get routes -o yaml <name of resource> -n $namespace
----
* `namespace`: Specifies the route that is named `hello-microshift` and the namespace is named `hello-microshift`.
+
.Sample YAML definition for the created unsecured route
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: hello-microshift
  namespace: hello-microshift
spec:
  host: microshift.com
  port:
    targetPort: 8080
  to:
    kind: Service
    name: hello-microshift
----
+
where:
+
`spec.host`:: Specifies the hostname.
`port.targetPort`:: Specifies the target port for the router to map the endpoint port in the service.
+
[NOTE]
====
{microshift-short} does not use an API that creates a default ingress domain, but instead provides a wildcard for automatically generated domains. Each route can also define a separate hostname.
====

//OCP module, edit with care; HTTP Strict Transport Security
// Module filename: nw-enabling-hsts.adoc
// Module included in the following assemblies:
// * networking/configuring-routing.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-enabling-hsts_{context}"]
= HTTP Strict Transport Security

[role="_abstract"]
To enhance security and optimize website performance, use the HTTP Strict Transport Security (HSTS) policy. This mechanism signals browsers to use only HTTPS traffic on the route host, eliminating the need for HTTP redirects and speeding up user interactions.

When HSTS policy is enforced, HSTS adds a Strict Transport Security header to HTTP and HTTPS responses from the site. You can use the `insecureEdgeTerminationPolicy` value in a route to redirect HTTP to HTTPS. When HSTS is enforced, the client changes all requests from the HTTP URL to HTTPS before the request is sent, eliminating the need for a redirect.

Cluster administrators can configure HSTS to do the following:

* Enable HSTS per-route
* Disable HSTS per-route
* Enforce HSTS per-domain, for a set of domains, or use namespace labels in combination with domains

[IMPORTANT]
====
HSTS works only with secure routes, either edge-terminated or re-encrypt. The configuration is ineffective on HTTP or passthrough routes.
====

//OCP module, edit with care; Enabling HTTP strict transport security per-route
// Module included in the following assemblies:
// * networking/configuring-routing.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-enabling-hsts-per-route_{context}"]
= Enabling HTTP Strict Transport Security per-route

[role="_abstract"]
To enforce secure HTTPS connections for specific applications, enable HTTP Strict Transport Security (HSTS) on a per-route basis. Applying the `haproxy.router.openshift.io/hsts_header` annotation to edge and re-encrypt routes ensures that browsers reject unencrypted traffic.

.Prerequisites
* You are logged in to the cluster with a user with administrator privileges for the project.
* You have root access to the cluster.
* You installed the {oc-first}.

.Procedure

* To enable HSTS on a route, add the `haproxy.router.openshift.io/hsts_header` value to the edge-terminated or re-encrypt route. You can use the `oc annotate` tool to do this by running the following command. To properly run the command, ensure that the semicolon (`;`) in the `haproxy.router.openshift.io/hsts_header` route annotation is also surrounded by double quotation marks (`""`).
+
.Example `annotate` command that sets the maximum age to `31536000` ms (approximately 8.5 hours)
[source,terminal]
----
$ oc annotate route <route_name> -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header=max-age=31536000;\
includeSubDomains;preload"
----
+
.Example route configured with an annotation
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/hsts_header: max-age=31536000;includeSubDomains;preload
# ...
spec:
  host: def.abc.com
  tls:
    termination: "reencrypt"
    ...
  wildcardPolicy: "Subdomain"
# ...
----
+
where:
+
`max-age`:: Specifies the measurement of the length of time, in seconds, for the HSTS policy. If set to `0`, it negates the policy.
`includeSubDomains`:: Specifies that all subdomains of the host must have the same HSTS policy as the host. Optional parameter.
`preload`:: Specifies that the site is included in the HSTS preload list when `max-age` is greater than `0`. For example, sites such as Google can construct a list of sites that have `preload` set. Browsers can then use these lists to determine which sites they can communicate with over HTTPS, even before they have interacted with the site. Without `preload` set, browsers must have interacted with the site over HTTPS, at least once, to get the header. Optional parameter.

//OCP module, edit with care; Disabling HTTP strict transport security per-route
// Module included in the following assemblies:
// * networking/configuring-routing.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-disabling-hsts_{context}"]
= Disabling HTTP Strict Transport Security per-route

[role="_abstract"]
To allow unencrypted connections or troubleshoot access issues, disable HTTP Strict Transport Security (HSTS) for a specific route. Setting the `max-age` route annotation to `0` instructs browsers to stop enforcing HTTPS requirements on the route host.

.Prerequisites
* You are logged in to the cluster with a user with administrator privileges for the project.
* You have root access to the cluster.
* You installed the {oc-first}.

.Procedure

* To disable HSTS, enter the following to set the `max-age` value in the route annotation to `0`:
+
[source,terminal]
----
$ oc annotate route <route_name> -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=0"
----
+
[TIP]
====
You can alternatively apply the following YAML to create the config map for disabling HSTS per-route:

[source,yaml]
----
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  annotations:
    haproxy.router.openshift.io/hsts_header: max-age=0
----
====

* To disable HSTS for every route in a namespace, enter the following command:
+
[source,terminal]
----
$ oc annotate route --all -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=0"
----

.Verification

* To query the annotation for all routes, enter the following command:
+
[source,terminal]
----
$ oc get route  --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n := .metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}{{end}}'
----
+
.Example output
[source,terminal]
----
Name: routename HSTS: max-age=0
----

//Enforcing HTTP strict transport security per-domain
// Module included in the following assemblies:
//
// * microshift_networking/microshift-configuring-routes.adoc

[id="microshift-nw-enforcing-hsts-per-domain_{context}"]
= Enforcing HTTP Strict Transport Security per-domain

[role="_abstract"]
To enforce secure communication per-domain, configure routes with a compliant HSTS policy annotation. For upgraded nodes with non-compliant routes, ensure consistent enforcement by updating the source manifests to apply the new security policies.

You cannot use `oc expose route` or `oc create route` commands to add a route in a domain that enforces HSTS because the API for these commands does not accept annotations.

[IMPORTANT]
====
HSTS cannot be applied to insecure, or non-TLS, routes.
====

.Prerequisites

* You have root access to the node.
* You installed the {oc-first}.

.Procedure

* Apply HSTS to all routes in the node by running the following command:
+
[source,terminal]
----
$ oc annotate route --all --all-namespaces --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=31536000;preload;includeSubDomains"
----

* Apply HSTS to all routes in a particular namespace by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc annotate route --all -n __<my_namespace>__ --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=31536000;preload;includeSubDomains"
----
* `<my_namespace>`: Specify the namespace that you want to use.

.Verification

* Review the HSTS annotations on all routes by running the following command:
+
[source,terminal]
----
$ oc get route  --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n := .metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}{{end}}'
----
+
.Example output
[source,terminal]
----
Name: <_routename_> HSTS: max-age=31536000;preload;includeSubDomains
----

//OCP module, edit with care; Troubleshooting Throughput Issues
// Module filename: nw-throughput-troubleshoot.adoc
// Module included in the following assemblies:
// * networking/routes/route-configuration.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-throughput-troubleshoot_{context}"]
= Throughput issue troubleshooting methods

[role="_abstract"]
To diagnose and resolve network throughput issues, such as unusually high latency between specific services, apply troubleshooting methods. Identifying connectivity bottlenecks helps ensure stable application performance within OpenShift Container Platform.

If pod logs do not reveal any cause of the problem, use the following methods to analyze performance issues:

* Use a packet analyzer, such as `ping` or `tcpdump` to analyze traffic between a pod and its node.
+
For example, run the `tcpdump` tool on each pod while reproducing the behavior that led to the issue. Review the captures on both sides to compare send and receive timestamps to analyze the latency of traffic to and from a pod. Latency can occur in OpenShift Container Platform if a node interface is overloaded with traffic from other pods, storage devices, or the data plane.
+
[source,terminal]
----
$ tcpdump -s 0 -i any -w /tmp/dump.pcap host <podip 1> && host <podip 2> <1>
----
+
where:
+
`podip`:: Specifies the IP address for the pod. Run the `oc get pod <pod_name> -o wide` command to get the IP address of a pod.
+
The `tcpdump` command generates a file at `/tmp/dump.pcap` containing all traffic between these two pods. You can run the analyzer shortly before the issue is reproduced and stop the analyzer shortly after the issue is finished reproducing to minimize the size of the file. You can also run a packet analyzer between the nodes with:
+
[source,terminal]
----
$ tcpdump -s 0 -i any -w /tmp/dump.pcap port 4789
----

* Use a bandwidth measuring tool, such as `iperf`, to measure streaming throughput and UDP throughput. Locate any bottlenecks by running the tool from the pods first, and then running it from the nodes.

** For information on installing and using `iperf`, see this Red Hat Solution.
* In some cases, the cluster might mark the node with the router pod as unhealthy due to latency issues. Use worker latency profiles to adjust the frequency that the cluster waits for a status update from the node before taking action.

* If your cluster has designated lower-latency and higher-latency nodes, configure the `spec.nodePlacement` field in the Ingress Controller to control the placement of the router pod.

//OCP module, edit with care; Using cookies to keep route statefulness
// Module filename: nw-using-cookies-keep-route-statefulness.adoc
// Use module with the following module:
// nw-annotating-a-route-with-a-cookie-name.adoc
//
// Module included in the following assemblies:
//
// * networking/configuring-routing.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-using-cookies-keep-route-statefulness_{context}"]
= Using cookies to keep route statefulness

[role="_abstract"]
To maintain stateful application traffic during pod restarts or scaling events, configure sticky sessions by using cookies. By using this method, you ensure that all incoming traffic reaches the same endpoint, preventing state loss even if the specific endpoint pod changes.

OpenShift Container Platform can use cookies to configure session persistence. The Ingress Controller selects an endpoint to handle any user requests, and creates a cookie for the session. The cookie is passed back in the response to the request and the user sends the cookie back with the next request in the session. The cookie tells the Ingress Controller which endpoint is handling the session, ensuring that client requests use the cookie so that they are routed to the same pod.

[NOTE]
====
Cookies cannot be set on passthrough routes, because the HTTP traffic cannot be seen. Instead, a number is calculated based on the source IP address, which determines the backend.

If backends change, the traffic can be directed to the wrong server, making it less sticky. If you are using a load balancer, which hides source IP, the same number is set for all connections and traffic is sent to the same pod.
====

//OCP module, edit with care; Using cookies to keep route statefulness
// Module filename: nw-annotating-a-route-with-a-cookie-name.adoc
// Use module with the following module:
// nw-using-cookies-keep-route-statefulness.adoc
//
// Module included in the following assemblies:
//
// * networking/configuring-routing.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-annotating-a-route-with-a-cookie-name_{context}"]
= Annotating a route with a cookie

[role="_abstract"]
To enable applications to manage session persistence and load distribution, annotate the route with a custom cookie name. Overwriting the default cookie allows the backend application to identify and delete the specific cookie, forcing endpoint re-selection when necessary.

When a server is overloaded, the server tries to remove the requests from the client and redistribute the requests to other endpoints.

.Procedure

. Annotate the route with the specified cookie name:
+
[source,terminal]
----
$ oc annotate route <route_name> router.openshift.io/cookie_name="<cookie_name>"
----
+
where:
+
`<route_name>`:: Specifies the name of the route.
`<cookie_name>`:: Specifies the name for the cookie.
+
For example, to annotate the route `my_route` with the cookie name `my_cookie`:
+
[source,terminal]
----
$ oc annotate route my_route router.openshift.io/cookie_name="my_cookie"
----

. Capture the route hostname in a variable:
+
[source,terminal]
----
$ ROUTE_NAME=$(oc get route <route_name> -o jsonpath='{.spec.host}')
----
+
where:
+
`<route_name>`:: Specifies the name of the route.

. Save the cookie, and then access the route:
+
[source,terminal]
----
$ curl $ROUTE_NAME -k -c /tmp/cookie_jar
----
+
Use the cookie saved by the previous command when connecting to the route:
+
[source,terminal]
----
$ curl $ROUTE_NAME -k -b /tmp/cookie_jar
----

//OCP module, edit with care
// Module filename: nw-path-based-routes.adoc
// Module included in the following assemblies:
// * networking/routes/route-configuration.adoc

[id="nw-path-based-routes_{context}"]
= Path-based routes

[role="_abstract"]
To serve multiple applications by using a single hostname, configure path-based routes. This HTTP-based configuration directs traffic to specific services by comparing the URL path component, ensuring requests match the most specific route defined.

The following table shows example routes and their accessibility:

.Route availability
[cols="3*", options="header"]
|===
|Route | When compared to | Accessible
.2+|_www.example.com/test_ |_www.example.com/test_|Yes
|_www.example.com_|No
.2+|_www.example.com/test_ and _www.example.com_ | _www.example.com/test_|Yes
|_www.example.com_|Yes
.2+|_www.example.com_|_www.example.com/text_|Yes (Matched by the host, not the route)
|_www.example.com_|Yes
|===

.Example of an unsecured route with a path
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: route-unsecured
spec:
  host: www.example.com
  path: "/test"
  to:
    kind: Service
    name: service-name
----
* `spec.host`: Specifies the path attribute for a path-based route.

[NOTE]
====
Path-based routing is not available when using passthrough TLS, as the router does not terminate TLS in that case and cannot read the contents of the request.
====

//OCP module, edit with care; just use the `Route` CR
// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc
// * networking/route-configuration.adoc

[id="nw-http-header-configuration_{context}"]
= HTTP header configuration

[role="_abstract"]
To customize request and response headers for your applications, configure the Ingress Controller or apply specific route annotations. Understanding the interaction between these configuration methods ensures you effectively manage global and route-specific header policies.

You can also set certain headers by using route annotations. The various ways of configuring headers can present challenges when working together.
To customize request and response headers, modify individual route configurations or apply route annotations. Understanding the interaction between these methods ensures you effectively manage header policies and resolve potential configuration conflicts.

The various ways of configuring headers can present challenges when working together.

[NOTE]
====
You can only set or delete headers within an `IngressController` or `Route` CR, you cannot append them. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.
====

[NOTE]
====
You can only set or delete headers within a `Route` CR. You cannot append headers. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.
====

Order of precedence::

When the same HTTP header is modified both in the Ingress Controller and in a route, HAProxy prioritizes the actions in certain ways depending on whether it is a request or response header.

* For HTTP response headers, actions specified in the Ingress Controller are executed after the actions specified in a route. This means that the actions specified in the Ingress Controller take precedence.

* For HTTP request headers, actions specified in a route are executed after the actions specified in the Ingress Controller. This means that the actions specified in the route take precedence.

For example, a cluster administrator sets the X-Frame-Options response header with the value `DENY` in the Ingress Controller using the following configuration:

.Example `IngressController` spec
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: DENY
----

A route owner sets the same response header that the cluster administrator set in the Ingress Controller, but with the value `SAMEORIGIN` using the following configuration:

.Example `Route` spec
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: SAMEORIGIN
----
When both the `IngressController` spec and `Route` spec are configuring the X-Frame-Options response header, then the value set for this header at the global level in the Ingress Controller takes precedence, even if a specific route allows frames. For a request header, the `Route` spec value overrides the `IngressController` spec value.

This prioritization occurs because the `haproxy.config` file uses the following logic, where the Ingress Controller is considered the front end and individual routes are considered the back end. The header value `DENY` applied to the front end configurations overrides the same header with the value `SAMEORIGIN` that is set in the back end:

[source,text]
----
frontend public
  http-response set-header X-Frame-Options 'DENY'

frontend fe_sni
  http-response set-header X-Frame-Options 'DENY'

frontend fe_no_sni
  http-response set-header X-Frame-Options 'DENY'

backend be_secure:openshift-monitoring:alertmanager-main
  http-response set-header X-Frame-Options 'SAMEORIGIN'
----

Additionally, any actions defined in either the Ingress Controller or a route override values set using route annotations.

Any actions defined in a route override values set using route annotations.

Special case headers::

The following headers are either prevented entirely from being set or deleted, or allowed under specific circumstances:

.Special case header configuration options
[cols="5*a",options="header"]
|===
|Header name |Configurable using `IngressController` spec |Configurable using `Route` spec |Reason for disallowment |Configurable using another method

|`proxy`
|No
|No
|The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.
|No

|`host`
|No
|Yes
|When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.
|No

|`strict-transport-security`
|No
|No
|The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.
|Yes: the `haproxy.router.openshift.io/hsts_header` route annotation

|`cookie` and `set-cookie`
|No
|No
|The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy's session affinity and restrict HAProxy's ownership of a cookie.
|Yes:

* the `haproxy.router.openshift.io/disable_cookie` route annotation
* the `haproxy.router.openshift.io/cookie_name` route annotation

|===

|===
|Header name |Configurable using `Route` spec |Reason for disallowment |Configurable using another method

|`proxy`
|No
|The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.
|No

|`host`
|Yes
|When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.
|No

|`strict-transport-security`
|No
|The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.
|Yes: the `haproxy.router.openshift.io/hsts_header` route annotation

|`cookie` and `set-cookie`
|No
|The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy's session affinity and restrict HAProxy's ownership of a cookie.
|Yes:

* the `haproxy.router.openshift.io/disable_cookie` route annotation
* the `haproxy.router.openshift.io/cookie_name` route annotation

|===

//OCP module, edit with care
// Module included in the following assemblies:
//
// * networking/route-configuration.adoc

[id="nw-route-set-or-delete-http-headers_{context}"]
= Setting or deleting HTTP request and response headers in a route

[role="_abstract"]
You can set or delete certain HTTP request and response headers for compliance purposes or other reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for specific routes.

For example, you might want to enable a web application to serve content in alternate locations for specific routes if that content is written in multiple languages, even if there is a default global location specified by the Ingress Controller serving the routes.

The following procedure creates a route that sets the Content-Location HTTP request header so that the URL associated with the application, `\https://app.example.com`, directs to the location `\https://app.example.com/lang/en-us`. Directing application traffic to this location means that anyone using that specific route is accessing web content written in American English.

.Prerequisites
* You have installed the {oc-first}.
* You are logged into an OpenShift Container Platform cluster as a project administrator.
* You have a web application that exposes a port and an HTTP or TLS endpoint listening for traffic on the port.

.Procedure

. Create a route definition and save it in a file called `app-example-route.yaml`:
+
.YAML definition of the created route with HTTP header directives
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  host: app.example.com
  tls:
    termination: edge
  to:
    kind: Service
    name: app-example
  httpHeaders:
    actions:
      response:
      - name: Content-Location
        action:
          type: Set
          set:
            value: /lang/en-us
# ...
----
+
where:
+
`actions`:: Specifies the list of actions you want to perform on the HTTP headers.
`response`:: Specifies the type of header you want to change. In this case, a response header.
`response.name`:: Specifies the name of the header you want to change. For a list of available headers you can set or delete, see _HTTP header configuration_.
`action.type`:: Specifies the type of action being taken on the header. This field can have the value `Set` or `Delete`.
`set.value`:: When setting HTTP headers, you must provide a `value`. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy's dynamic value syntax. In this case, the value is set to the relative location of the content.

. Create a route to your existing web application using the newly created route definition:
+
[source,terminal]
----
$ oc -n app-example create -f app-example-route.yaml
----
+
For HTTP request headers, the actions specified in the route definitions are executed after any actions performed on HTTP request headers in the Ingress Controller. This means that any values set for those request headers in a route will take precedence over the ones set in the Ingress Controller. For more information on the processing order of HTTP headers, see _HTTP header configuration_.

//OCP module, edit with care
// Module included in the following assemblies:
//
// * networking/routes/route-configuration.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-ingress-creating-a-route-via-an-ingress_{context}"]
= Creating a route through an Ingress object

[role="_abstract"]
To integrate ecosystem components that require Ingress resources, configure an Ingress object. OpenShift Container Platform automatically manages the lifecycle of the corresponding route objects, creating and deleting them to ensure seamless connectivity.

.Prerequisites

* If clients must receive a full certificate chain, you must combine the PEM-encoded leaf certificate and intermediates into a single file. Place the leaf certificate first, followed by each issuer in chain order.
* You confirmed the private key matches the leaf certificate in the `tls.crt` key.
* You confirmed the `tls.key` key has only the private key for the leaf certificate.
* The certificate Subject Alternative Name (SAN), or the subject CN if no SAN is present, covers every hostname set in `spec.rules[].host` and `spec.tls[].hosts`. These values must match for the same host.
* The private key is not password-encrypted. You must decrypt the key before you create the TLS secret so that OpenShift Container Platform can read the key material.
* You created a `Secret` of type `kubernetes.io/tls` in the same namespace as the `Ingress`. The `secretName` must match the `spec.tls[].secretName` field. If you have not created the secret, you must do so before you apply the `Ingress` object.

.Procedure

. Define an Ingress object in the OpenShift Container Platform console or by entering the `oc create` command:
+
.YAML Definition of an Ingress
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend
  annotations:
    route.openshift.io/termination: "reencrypt"
    route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
spec:
  rules:
  - host: www.example.com
    http:
      paths:
      - backend:
          service:
            name: frontend
            port:
              number: 443
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - www.example.com
    secretName: example-com-tls-certificate
# ...
----
+
where:
+
`route.openshift.io/termination`:: Specifies the `route.openshift.io/termination` annotation. You can configure the `spec.tls.termination` parameter of the `Route` because `Ingress` does not have this parameter. The accepted values are `edge`, `passthrough`, and `reencrypt`. All other values are silently ignored. When  the annotation value is unset, `edge` is the default route. The TLS certificate details must be defined in the template file to implement the default edge route.
`rules.host`:: Specifies an explicit hostname for the `Ingress` object. Mandatory parameter. You can use the `<host_name>.<cluster_ingress_domain>` syntax, for example `apps.openshiftdemos.com`, to take advantage of the `*.<cluster_ingress_domain>` wildcard DNS record and serving certificate for the cluster. Otherwise, you must ensure that there is a DNS record for the chosen hostname.
`destination-ca-certificate-secret`:: Specifies the `route.openshift.io/destination-ca-certificate-secret` annotation. The annotation can be used on an Ingress object to define a route with a custom destination certificate (CA). The annotation references a kubernetes secret, `secret-ca-cert` that will be inserted into the generated route.

+
.. If you specify the `passthrough` value in the `route.openshift.io/termination` annotation, set `path` to `''` and `pathType` to `ImplementationSpecific` in the spec:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
# ...
  spec:
    rules:
    - host: www.example.com
      http:
        paths:
        - path: ''
          pathType: ImplementationSpecific
          backend:
            service:
              name: frontend
              port:
                number: 443
# ...
----
+
[source,terminal]
----
$ oc apply -f ingress.yaml
----
+
.. To specify a route object with a destination CA from an ingress object, you must create a `kubernetes.io/tls` or `Opaque` type secret with a certificate in PEM-encoded format in the `data.tls.crt` specifier of the secret.

. List your routes:
+
[source,terminal]
----
$ oc get routes
----
+
The result includes an autogenerated route whose name starts with `frontend-`:
+
[source,terminal]
----
NAME             HOST/PORT         PATH    SERVICES    PORT    TERMINATION          WILDCARD
frontend-gnztq   www.example.com           frontend    443     reencrypt/Redirect   None
----
+
.YAML definition example of an autogenerated route
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: frontend-gnztq
  ownerReferences:
  - apiVersion: networking.k8s.io/v1
    controller: true
    kind: Ingress
    name: frontend
    uid: 4e6c59cc-704d-4f44-b390-617d879033b6
spec:
  host: www.example.com
  path: /
  port:
    targetPort: https
  tls:
    certificate: |
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
    insecureEdgeTerminationPolicy: Redirect
    key: |
      -----BEGIN RSA PRIVATE KEY-----
      [...]
      -----END RSA PRIVATE KEY-----
    termination: reencrypt
    destinationCACertificate: |
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
  to:
    kind: Service
    name: frontend
----

//OCP module, edit with care
// This is included in the following assemblies:
//
// * networking/ingress_load_balancing/routes/securing-routes-via-ingress-objects.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-ingress-edge-route-default-certificate_{context}"]
= Creating a route using the default certificate through an Ingress object

[role="_abstract"]
To generate a secure, edge-terminated route that uses the default ingress certificate, specify an empty TLS configuration in the Ingress object. This configuration overrides the default behavior, preventing the creation of an insecure route.

.Prerequisites

* You have a service that you want to expose.
* You have access to the {oc-first}.

.Procedure

. Create a YAML file for the Ingress object. In the following example, the file is called `example-ingress.yaml`:
+
.YAML definition of an Ingress object
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend
  ...
spec:
  rules:
    ...
  tls:
  - {}
----
+
where:
+
`spec.tls`:: Specifies the TLS configuration. Use the exact syntax shown to specify TLS without specifying a custom certificate.

. Create the Ingress object by running the following command:
+
[source,terminal]
----
$ oc create -f example-ingress.yaml
----

.Verification

* Verify that OpenShift Container Platform has created the expected route for the Ingress object by running the following command:
+
[source,terminal]
----
$ oc get routes -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: frontend-j9sdd
# ...
  spec:
  ...
    tls:
      insecureEdgeTerminationPolicy: Redirect
      termination: edge
# ...
----
+
where:
+
`metadata.name`:: Specifies the name of the route, which includes the name of the Ingress object followed by a random suffix.
`spec.tls`:: To use the default certificate, the route should not specify `spec.certificate`.
`tls.termination`:: Specifies the termination policy for the route. The route should specify the `edge` termination policy.

//OCP module, edit with care
// This is included in the following assemblies:
//
// * networking/ingress_load_balancing/routes/securing-routes-via-ingress-objects.adoc
// * microshift_networking/microshift-configuring-routes.adoc

[id="nw-ingress-re-encrypt-route-custom-cert_{context}"]
= Creating a route using the destination CA certificate in the Ingress annotation

[role="_abstract"]
To define a route with a custom destination CA certificate, apply the `route.openshift.io/destination-ca-certificate-secret` annotation to an Ingress object. This configuration ensures the Ingress Controller uses the specified secret to verify the identity of the destination service.

.Prerequisites

* You have a certificate/key pair in PEM-encoded files, where the certificate is valid for the route host.
* You have a separate CA certificate in a PEM-encoded file that completes the certificate chain.
* You have a separate destination CA certificate in a PEM-encoded file.
* You have a service that you want to expose.

.Procedure

. Create a secret for the destination CA certificate by entering the following command:
+
[source,terminal]
----
$ oc create secret generic dest-ca-cert --from-file=tls.crt=<file_path>
----
+
For example:
+
[source,terminal]
----
$ oc -n test-ns create secret generic dest-ca-cert --from-file=tls.crt=tls.crt
----
+
.Example output
[source,terminal]
----
secret/dest-ca-cert created
----

. Add the `route.openshift.io/destination-ca-certificate-secret` to the Ingress annotations:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend
  annotations:
    route.openshift.io/termination: "reencrypt"
    route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
...
----
+
where:
+
`destination-ca-certificate-secret`:: Specifies the `route.openshift.io/destination-ca-certificate-secret` annotation. The annotation references a Kubernetes secret.
+
The Ingress Controller inserts a secret that is referenced in the annotation into the generated route.
+
.Example output
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: frontend
  annotations:
    route.openshift.io/termination: reencrypt
    route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
spec:
...
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: reencrypt
    destinationCACertificate: |
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
...
----

[role="_additional-resources"]
.Additional resources

* Creating a re-encrypt route with a custom certificate

* Creating an edge route with a custom certificate

* Creating a passthrough route
