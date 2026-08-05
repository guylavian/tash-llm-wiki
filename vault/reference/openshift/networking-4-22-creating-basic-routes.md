---
title: "Creating basic routes"
type: reference
domain: openshift
slug: networking-4-22-creating-basic-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/creating-basic-routes
version: 4.22
family: networking
documentKind: "Documentation"
---

# Creating basic routes

[id="creating-basic-routes"]
= Creating basic routes

[role="_abstract"]
If you have unencrypted HTTP, you can create a basic route with a route object.

// Module included in the following assemblies:
//
// * networking/routes/route-configuration.adoc

[id="nw-creating-a-route_{context}"]
= Creating an HTTP-based route

[role="_abstract"]
You can use the following procedure to create a simple HTTP-based route to a web application, using the `hello-openshift` application as an example.

You can create a route to host your application at a public URL. The route can either be secure or unsecured, depending on the network security configuration of your application. An HTTP-based route is an unsecured route that uses the basic HTTP routing protocol and exposes a service on an unsecured application port.

//hello-openshift

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You are logged in as an administrator.
* You have a web application that exposes a port and a TCP endpoint listening for traffic on the port.

.Procedure

. Create a project called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc new-project hello-openshift
----

. Create a pod in the project by running the following command:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/openshift/origin/master/examples/hello-openshift/hello-pod.json
----

. Create a service called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc expose pod/hello-openshift
----

. Create an unsecured route to the `hello-openshift` application by running the following command:
+
[source,terminal]
----
$ oc expose svc hello-openshift
----

.Verification

* To verify that the `route` resource that you created, run the following command:
+
[source,terminal]
----
$ oc get routes -o yaml hello-openshift
----
+
.Example YAML definition of the created unsecured route
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: hello-openshift
spec:
  host: www.example.com
  port:
    targetPort: 8080
  to:
    kind: Service
    name: hello-openshift
----
+
where:

`host`:: Specifies an alias DNS record that points to the service. This field can be any valid DNS name, such as `www.example.com`. The DNS name must follow DNS952 subdomain conventions. If not specified, a route name is automatically generated.
`targetPort`:: Specifies the target port on pods that is selected by the service that this route points to.
+
[NOTE]
====
To display your default ingress domain, run the following command:
[source,terminal]
----
$ oc get ingresses.config/cluster -o jsonpath={.spec.domain}
----
====

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

// Creating a route for router sharding
// Module included in the following assemblies:
//
// * configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-ingress-controller.adoc
// * networking/routes/route-configuration.adoc

[id="nw-ingress-sharding-route-configuration_{context}"]
= Creating a route for Ingress Controller sharding

[role="_abstract"]
You can use a route to host your application at a URL. Ingress Controller sharding helps balance incoming traffic load among a set of Ingress Controllers. Ingress Controller sharding can also isolate traffic to a specific Ingress Controller. For example, company A goes to one Ingress Controller and company B to another.

The following procedure describes how to create a route for Ingress Controller sharding, using the `hello-openshift` application as an example.

.Prerequisites

* You installed the {oc-first}.
* You are logged in as a project administrator.
* You have a web application that exposes a port and an HTTP or TLS endpoint listening for traffic on the port.
* You have configured the Ingress Controller for sharding.

.Procedure

. Create a project called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc new-project hello-openshift
----

. Create a pod in the project by running the following command:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/openshift/origin/master/examples/hello-openshift/hello-pod.json
----

. Create a service called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc expose pod/hello-openshift
----

. Create a route definition called `hello-openshift-route.yaml`:
+
.YAML definition of the created route for sharding
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  labels:
    type: sharded
  name: hello-openshift-edge
  namespace: hello-openshift
spec:
  subdomain: hello-openshift
  tls:
    termination: edge
  to:
    kind: Service
    name: hello-openshift
----
+
where:
+
`type`:: Specifies both the label key and its corresponding label value must match the ones specified in the Ingress Controller. In this example, the Ingress Controller has the label key and value `type: sharded`.
`subdomain`:: Specifies the route gets exposed by using the value of the `subdomain` field. When you specify the `subdomain` field, you must leave the hostname unset. If you specify both the `host` and `subdomain` fields, then the route uses the value of the `host` field, and ignore the `subdomain` field.

. Use `hello-openshift-route.yaml` to create a route to the `hello-openshift` application by running the following command:
+
[source,terminal]
----
$ oc -n hello-openshift create -f hello-openshift-route.yaml
----

.Verification

* Get the status of the route with the following command:
+
[source,terminal]
----
$ oc -n hello-openshift get routes/hello-openshift-edge -o yaml
----
+
The resulting `Route` resource should look similar to the following:
+
.Example output
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  labels:
    type: sharded
  name: hello-openshift-edge
  namespace: hello-openshift
spec:
  subdomain: hello-openshift
  tls:
    termination: edge
  to:
    kind: Service
    name: hello-openshift
status:
  ingress:
  - host: hello-openshift.<apps-sharded.basedomain.example.net>
    routerCanonicalHostname: router-sharded.<apps-sharded.basedomain.example.net>
    routerName: sharded
----
+
where:
+
`host`:: Specifies the hostname the Ingress Controller, or router, uses to expose the route. The value of the `host` field is automatically determined by the Ingress Controller, and uses its domain. In this example, the domain of the Ingress Controller is `<apps-sharded.basedomain.example.net>`.
`<apps-sharded.basedomain.example.net>`:: Specifies the hostname of the Ingress Controller. If the hostname is not set, the route can use a subdomain instead. When you specify a subdomain, you automatically use the domain of the Ingress Controller that exposes the route. When a route is exposed by multiple Ingress Controllers, the route is hosted at multiple URLs.
`routerName`:: Specifies the name of the Ingress Controller. In this example, the Ingress Controller has the name `sharded`.

// Creating a route via an Ingress
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

//About label propogation
// Module included in the following assemblies:
//
// * networking/routes/creating-basic-routes.adoc

[id="networking-ingress-label-propagation-about_{context}"]
= About label propagation from Ingress to Route resources

[role="_abstract"]
You can opt-in to a feature that enables the Ingress Operator to automatically propagate labels. This allows you to add metadata that helps track or manage resources, or to control specific behaviors that depend on labels.

By default, the managed `Route` object does not inherit labels from the `Ingress` resource. When you enable the propagation feature, the Operator actively reconciles the labels on the generated `Route` resource to match the labels on the parent `Ingress` resource.

[NOTE]
====
When label propagation is enabled, the Ingress Operator replaces all labels on the managed `Route` resource with the exact set of labels from the parent `Ingress` resource. Any labels that were manually added to the `Route` resource are removed.
====

The propagation behavior is controlled by the `route.openshift.io/reconcile-labels` annotation on the `Ingress` resource. The Operator's behavior changes depending on the state of this annotation:

* Annotation not present (default): The Operator does not sync labels from the `Ingress` resource to the `Route` resource. Any existing labels on the `Route` are preserved.

* Annotation enabled (`route.openshift.io/reconcile-labels: "true"`): The Operator enables label propagation. On the next reconciliation (triggered by the `Ingress` create or update event), the Operator replaces all labels on the generated `Route` resource with the labels from the `Ingress` resource.

* Annotation disabled (removed or value set to non-"true"): The Operator disables label propagation. The labels that currently exist on the `Route` resource are kept as-is, but the Operator no longer syncs them with the `Ingress` resource.

* Annotation re-enabled: The Operator resumes propagation. It will again replace all labels on the `Route` resource with the current labels from the `Ingress` resource.

//Enabling label propogation
// Module included in the following assemblies:
//
// * networking/routes/creating-basic-routes.adoc

[id="networking-ingress-label-propagation-enabling_{context}"]
= Enabling label propagation from Ingress to Route resources

[role="_abstract"]
You can enable the Ingress Operator to automatically propagate labels from an `Ingress` resource to the `Route` resource it manages. To enable this, you must add the `reconcile-labels` annotation to an `Ingress` resource.

.Prerequisites

* You have access to an OpenShift Container Platform cluster.
* You have the `cluster-admin` role or permissions to create and edit `Ingress` resources in a project.

.Procedure

. Create or edit an `Ingress` resource manifest.

. In the `metadata.annotations` section, add `route.openshift.io/reconcile-labels: "true"`.

. In the `metadata.labels` section, add the labels you want to propagate.
+
Example `Ingress` resource with label propagation enabled:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    route.openshift.io/reconcile-labels: "true"
  labels:
    app: my-app
    owner: dev-team
spec:
  ingressClassName: openshift-default
  rules:
  - host: example.com
    http:
      paths:
      - backend:
          service:
            name: example-service
            port:
              number: 27017
        path: "/"
        pathType: "Prefix"
----

. Apply the manifest to your cluster:
+
[source,terminal]
----
$ oc apply -f <example-ingress-manifest.yaml>
----
+
Replace `<example-ingress-manifest.yaml>` with the name of your specific manifest file.

. Verify that the labels from the `Ingress` resource have propagated to the generated `Route` resource:
+
[source,terminal]
----
$ oc get route -l app=my-app --show-labels
----
+
Example output:
+
[source,terminal]
----
NAME          HOST/PORT     PATH   SERVICES          PORT    TERMINATION   WILDCARD   LABELS
example-rt    example.com   /      example-service   8080                  None       app=my-app,owner=dev-team
----
