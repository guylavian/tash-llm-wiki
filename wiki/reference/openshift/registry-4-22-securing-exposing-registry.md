---
title: "Exposing the registry"
type: reference
domain: openshift
slug: registry-4-22-securing-exposing-registry
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/securing-exposing-registry
version: 4.22
family: registry
documentKind: "Documentation"
---

# Exposing the registry

[id="securing-exposing-registry"]
= Exposing the registry

[role="_abstract"]
By default, the {product-registry} is secured during cluster installation so that it serves traffic through the Transport Layer Security (TLS) protocol. Unlike previous versions of OpenShift Container Platform, the registry is not exposed outside of the cluster at the time of installation.

[id="registry-exposing-default-registry-manually_{context}"]
= Exposing a default registry manually

[role="_abstract"]
Instead of logging in to the default {product-registry} from within the cluster, you can gain external access to the {product-registry} by exposing the registry with a route. With this external access, you can log in to the registry from outside the cluster by using the route address. You can then tag and push images to an existing project by using the route host.

.Prerequisites

* The following prerequisites are automatically performed:
** Deploy the Registry Operator.
** Deploy the Ingress Operator.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. To expose the registry by using the `defaultRoute` parameter that exists in the `configs.imageregistry.operator.openshift.io` resource, set `defaultRoute` to `true` by running the following command:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
----

. Get the default registry route by running the following command:
+
[source,terminal]
----
$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')
----

. Get the certificate of the Ingress Operator by running the following command:
+
[source,terminal]
----
$ oc extract secret/$(oc get ingresscontroller -n openshift-ingress-operator default -o json | jq '.spec.defaultCertificate.name // "router-certs-default"' -r) -n openshift-ingress --confirm
----

. Move the extracted certificate to the trusted CA directory of the system by running the following command:
+
[source,terminal]
----
$ sudo mv tls.crt /etc/pki/ca-trust/source/anchors/
----

. Enable the default certificate of the cluster to trust the route by running the following command:
+
[source,terminal]
----
$ sudo update-ca-trust enable
----

. Log in with podman with the default route by running the following command:
+
[source,terminal]
----
$ sudo podman login -u kubeadmin -p $(oc whoami -t) $HOST
----

// Module included in the following assemblies:
//
// * registry/securing-exposing-registry.adoc

[id="registry-exposing-secure-registry-manually_{context}"]
= Exposing a secure registry manually

[role="_abstract"]
Instead of logging in to the {product-registry} from within the cluster, you can gain external access to the {product-registry} by exposing the registry with a route. With this external access, you can log in to the registry from outside the cluster by using the route address. You can then tag and push images to an existing project by using the route host.

You can expose the route by using `DefaultRoute` parameter in the `configs.imageregistry.operator.openshift.io` resource or by using custom routes.

.Prerequisites

* The following prerequisites are automatically performed:
** Deploy the Registry Operator.
** Deploy the Ingress Operator.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. To expose the registry using `DefaultRoute` parameter, set `DefaultRoute` to `True`:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
----

. Log in with `podman` by entering the following command:
+
[source,terminal]
----
$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')
----
+
[source,terminal]
----
$ podman login -u kubeadmin -p $(oc whoami -t) --tls-verify=false $HOST
----
* `--tls-verify=false`: Set this parameter to `false` if the default certificate of the cluster for routes is untrusted. You can set a custom, trusted certificate as the default certificate with the Ingress Operator.

. To expose the registry using custom routes, create a secret with your route's TLS keys. This step is optional. If you do not create a secret, the route uses the default TLS configuration from the Ingress Operator.
+
[source,terminal]
----
$ oc create secret tls public-route-tls \
    -n openshift-image-registry \
    --cert=</path/to/tls.crt> \
    --key=</path/to/tls.key>
----

. On the Registry Operator, enter the following command:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----
+
[source,yaml]
----
spec:
  routes:
    - name: public-routes
      hostname: myregistry.mycorp.organization
      secretName: public-route-tls
...
----
+
[NOTE]
====
Only set `secretName` if you are providing a custom TLS configuration for the route of the registry.
====

.Troubleshooting

* Error creating TLS secret
