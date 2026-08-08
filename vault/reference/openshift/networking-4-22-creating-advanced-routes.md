---
title: "Securing routes through ingress objects"
type: reference
domain: openshift
slug: networking-4-22-creating-advanced-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/creating-advanced-routes
version: 4.22
family: networking
documentKind: "Documentation"
---

# Securing routes through ingress objects

[id="creating-advanced-routes"]
= Securing routes through ingress objects

[role="_abstract"]
You can secure your application traffic by managing certificates directly through ingress objects. This includes creating routes using the destination CA certificate in an ingress annotation or using the default certificate.

[WARNING]
====
The Ingress Controller maintains a one-way sync for certificates managed through ingress objects. Do not manually apply changes directly to the generated route's TLS configuration. Any manual modifications are silently overwritten the next time the parent ingress object is updated or reconciled. This is particularly important to note if you operate a GitOps-managed cluster.
====

//Creating a route using the destination CA certificate
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

//Creating an edge route with the default certificate
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
