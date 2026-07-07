---
title: "Integrating {SMProductShortName} with {ServerlessProductName}"
type: reference
domain: openshift
slug: serverless-4-22-serverless-ossm-setup
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-ossm-setup
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Integrating {SMProductShortName} with {ServerlessProductName}

[id="serverless-ossm-setup"]
= Integrating {SMProductShortName} with {ServerlessProductName}

The {ServerlessOperatorName} provides Kourier as the default ingress for Knative. However, you can use {SMProductShortName} with {ServerlessProductName} whether Kourier is enabled or not. Integrating with Kourier disabled allows you to configure additional networking and routing options that the Kourier ingress does not support, such as mTLS functionality.

[IMPORTANT]
====
{ServerlessProductName} only supports the use of {SMProductName} functionality that is explicitly documented in this guide, and does not support other undocumented features.
====

[id="prerequsites_serverless-ossm-setup"]
== Prerequisites

* The examples in the following procedures use the domain `example.com`. The example certificate for this domain is used as a certificate authority (CA) that signs the subdomain certificate.
+
To complete and verify these procedures in your deployment, you need either a certificate signed by a widely trusted public CA or a CA provided by your organization. Example commands must be adjusted according to your domain, subdomain, and CA.

* You must configure the wildcard certificate to match the domain of your OpenShift Container Platform cluster. For example, if your OpenShift Container Platform console address is `https://console-openshift-console.apps.openshift.example.com`, you must configure the wildcard certificate so that the domain is `*.apps.openshift.example.com`. For more information about configuring wildcard certificates, see the following topic about _Creating a certificate to encrypt incoming external traffic_.

* If you want to use any domain name, including those which are not subdomains of the default OpenShift Container Platform cluster domain, you must set up domain mapping for those domains. For more information, see the {ServerlessProductName} documentation about Creating a custom domain mapping.

// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-ossm-setup.adoc

[id="serverlesss-ossm-external-certs_{context}"]
= Creating a certificate to encrypt incoming external traffic

By default, the {SMProductShortName} mTLS feature only secures traffic inside of the {SMProductShortName} itself, between the ingress gateway and individual pods that have sidecars. To encrypt traffic as it flows into the OpenShift Container Platform cluster, you must generate a certificate before you enable the {ServerlessProductName} and {SMProductShortName} integration.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have installed the {ServerlessOperatorName} and Knative Serving.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Create a root certificate and private key that signs the certificates for your Knative services:
+
[source,terminal]
----
$ openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 \
    -subj '/O=Example Inc./CN=example.com' \
    -keyout root.key \
    -out root.crt
----
. Create a wildcard certificate:
+
[source,terminal]
----
$ openssl req -nodes -newkey rsa:2048 \
    -subj "/CN=*.apps.openshift.example.com/O=Example Inc." \
    -keyout wildcard.key \
    -out wildcard.csr
----
. Sign the wildcard certificate:
+
[source,terminal]
----
$ openssl x509 -req -days 365 -set_serial 0 \
    -CA root.crt \
    -CAkey root.key \
    -in wildcard.csr \
    -out wildcard.crt
----
. Create a secret by using the wildcard certificate:
+
[source,terminal]
----
$ oc create -n istio-system secret tls wildcard-certs \
    --key=wildcard.key \
    --cert=wildcard.crt
----
+
This certificate is picked up by the gateways created when you integrate {ServerlessProductName} with {SMProductShortName}, so that the ingress gateway serves traffic with this certificate.
// without kourier
// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-ossm-setup.adoc

[id="serverless-ossm-setup_{context}"]
= Integrating {SMProductShortName} with {ServerlessProductName}

You can integrate {SMProductShortName} with {ServerlessProductName} without using Kourier as the default ingress. To do this, do not install the Knative Serving component before completing the following procedure. There are additional steps required when creating the `KnativeServing` custom resource definition (CRD) to integrate Knative Serving with {SMProductShortName}, which are not covered in the general Knative Serving installation procedure. This procedure might be useful if you want to integrate {SMProductShortName} as the default and only ingress for your {ServerlessProductName} installation.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

* Install the {SMProductName} Operator and create a `ServiceMeshControlPlane` resource in the `istio-system` namespace. If you want to use mTLS functionality, you must also set the `spec.security.dataPlane.mtls` field for the `ServiceMeshControlPlane` resource to `true`.
+
[IMPORTANT]
====
Using {ServerlessProductName} with {SMProductShortName} is only supported with {SMProductName} version 2.0.5 or later.
====

* Install the {ServerlessOperatorName}.

* Install the OpenShift CLI (`oc`).

.Procedure

. Add the namespaces that you would like to integrate with {SMProductShortName} to the `ServiceMeshMemberRoll` object as members:
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  members: <1>
    - knative-serving
    - <namespace>
----
<1> A list of namespaces to be integrated with {SMProductShortName}.
+
[IMPORTANT]
====
This list of namespaces must include the `knative-serving` namespace.
====

. Apply the `ServiceMeshMemberRoll` resource:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create the necessary gateways so that {SMProductShortName} can accept traffic:
+
.Example `knative-local-gateway` object using HTTP
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: knative-ingress-gateway
  namespace: knative-serving
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      hosts:
        - "*"
      tls:
        mode: SIMPLE
        credentialName: <wildcard_certs> <1>
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
 name: knative-local-gateway
 namespace: knative-serving
spec:
 selector:
   istio: ingressgateway
 servers:
   - port:
       number: 8081
       name: http
       protocol: HTTP <2>
     hosts:
       - "*"
---
apiVersion: v1
kind: Service
metadata:
 name: knative-local-gateway
 namespace: istio-system
 labels:
   experimental.istio.io/disable-gateway-port-translation: "true"
spec:
 type: ClusterIP
 selector:
   istio: ingressgateway
 ports:
   - name: http2
     port: 80
     targetPort: 8081
----
<1> Add the name of the secret that contains the wildcard certificate.
<2> The `knative-local-gateway` serves HTTP traffic. Using HTTP means that traffic coming from outside of {SMProductShortName}, but using an internal hostname, such as `example.default.svc.cluster.local`, is not encrypted. You can set up encryption for this path by creating another wildcard certificate and an additional gateway that uses a different `protocol` spec.
+
.Example `knative-local-gateway` object using HTTPS
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: knative-local-gateway
  namespace: knative-serving
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      hosts:
        - "*"
      tls:
        mode: SIMPLE
        credentialName: <wildcard_certs>
----

. Apply the `Gateway` resources:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Install Knative Serving by creating the following `KnativeServing` custom resource definition (CRD), which also enables the Istio integration:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  ingress:
    istio:
      enabled: true <1>
  deployments: <2>
  - name: activator
    annotations:
      "sidecar.istio.io/inject": "true"
      "sidecar.istio.io/rewriteAppHTTPProbers": "true"
  - name: autoscaler
    annotations:
      "sidecar.istio.io/inject": "true"
      "sidecar.istio.io/rewriteAppHTTPProbers": "true"
----
<1> Enables Istio integration.
<2> Enables sidecar injection for Knative Serving data plane pods.

. Apply the `KnativeServing` resource:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create a Knative Service that has sidecar injection enabled and uses a pass-through route:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: <service_name>
  namespace: <namespace> <1>
  annotations:
    serving.knative.openshift.io/enablePassthrough: "true" <2>
spec:
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: "true" <3>
        sidecar.istio.io/rewriteAppHTTPProbers: "true"
    spec:
      containers:
      - image: <image_url>
----
<1> A namespace that is part of the Service Mesh member roll.
<2> Instructs Knative Serving to generate an OpenShift Container Platform pass-through enabled route, so that the certificates you have generated are served through the ingress gateway directly.
<3> Injects {SMProductShortName} sidecars into the Knative service pods.

. Apply the `Service` resource:
+
[source,terminal]
----
$ oc apply -f <filename>
----

.Verification

* Access your serverless application by using a secure connection that is now trusted by the CA:
+
[source,terminal]
----
$ curl --cacert root.crt <service_url>
----
+
.Example command
[source,terminal]
----
$ curl --cacert root.crt https://hello-default.apps.openshift.example.com
----
+
.Example output
[source,terminal]
----
Hello Openshift!
----
// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-ossm-setup.adoc

[id="serverless-ossm-enabling-serving-metrics_{context}"]
= Enabling Knative Serving metrics when using Service Mesh with mTLS

If Service Mesh is enabled with mTLS, metrics for Knative Serving are disabled by default, because Service Mesh prevents Prometheus from scraping metrics. This section shows how to enable Knative Serving metrics when using Service Mesh and mTLS.

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Serving on your cluster.
* You have installed {SMProductName} with the mTLS functionality enabled.

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Specify `prometheus` as the `metrics.backend-destination` in the `observability` spec of the Knative Serving custom resource (CR):
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    observability:
      metrics.backend-destination: "prometheus"
...
----
+
This step prevents metrics from being disabled by default.

. Apply the following network policy to allow traffic from the Prometheus namespace:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-monitoring-ns
  namespace: knative-serving
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: "openshift-monitoring"
  podSelector: {}
...
----

. Modify and reapply the default Service Mesh control plane in the `istio-system` namespace, so that it includes the following spec:
+
[source,yaml]
----
...
spec:
  proxy:
    networking:
      trafficControl:
        inbound:
          excludedPorts:
          - 8444
...
----
// With kourier
// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-ossm-setup.adoc

[id="serverless-ossm-setup-with-kourier_{context}"]
= Integrating {SMProductShortName} with {ServerlessProductName} when Kourier is enabled

You can use {SMProductShortName} with {ServerlessProductName} even if Kourier is already enabled. This procedure might be useful if you have already installed Knative Serving with Kourier enabled, but decide to add a {SMProductShortName} integration later.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* Install the OpenShift CLI (`oc`).
* Install the {ServerlessOperatorName} and Knative Serving on your cluster.
* Install {SMProductName}. {ServerlessProductName} with {SMProductShortName} and Kourier is supported for use with both {SMProductName} versions 1.x and 2.x.

.Procedure

. Add the namespaces that you would like to integrate with {SMProductShortName} to the `ServiceMeshMemberRoll` object as members:
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  members:
    - <namespace> <1>
...
----
<1> A list of namespaces to be integrated with {SMProductShortName}.
. Apply the `ServiceMeshMemberRoll` resource:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Create a network policy that permits traffic flow from Knative system pods to Knative services:
.. For each namespace that you want to integrate with {SMProductShortName}, create a `NetworkPolicy` resource:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-serving-system-namespace
  namespace: <namespace> <1>
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          knative.openshift.io/part-of: "openshift-serverless"
  podSelector: {}
  policyTypes:
  - Ingress
...
----
<1> Add the namespace that you want to integrate with {SMProductShortName}.
+
[NOTE]
====
The `knative.openshift.io/part-of: "openshift-serverless"` label was added in {ServerlessProductName} 1.22.0. If you are using {ServerlessProductName} 1.21.1 or earlier, add the `knative.openshift.io/part-of` label to the `knative-serving` and `knative-serving-ingress` namespaces.

Add the label to the `knative-serving` namespace:

[source,terminal]
----
$ oc label namespace knative-serving knative.openshift.io/part-of=openshift-serverless
----

Add the label to the `knative-serving-ingress` namespace:

[source,terminal]
----
$ oc label namespace knative-serving-ingress knative.openshift.io/part-of=openshift-serverless
----
====
.. Apply the `NetworkPolicy` resource:
+
[source,terminal]
----
$ oc apply -f <filename>
----
// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-ossm-setup.adoc

[id="serverless-ossm-secret-filtering-net-istio_{context}"]
= Improving net-istio memory usage by using secret filtering for {SMProductShortName}

By default, the informers implementation for the Kubernetes `client-go` library fetches all resources of a particular type. This can lead to a substantial overhead when many resources are available, which can cause the Knative `net-istio` ingress controller to fail on large clusters due to memory leaking. However, a filtering mechanism is available for the Knative `net-istio` ingress controller, which enables the controller to only fetch Knative related secrets. You can enable this mechanism by adding an annotation to the `KnativeServing` custom resource (CR).

[IMPORTANT]
====
If you enable secret filtering, all of your secrets need to be labeled with  `networking.internal.knative.dev/certificate-uid: "<id>"`. Otherwise, Knative Serving does not detect them, which leads to failures. You must label both new and existing secrets.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* Install {SMProductName}. {ServerlessProductName} with {SMProductShortName} only is supported for use with {SMProductName} version 2.0.5 or later.
* Install the {ServerlessOperatorName} and Knative Serving.
* Install the OpenShift CLI (`oc`).

.Procedure

* Add the `serverless.openshift.io/enable-secret-informer-filtering` annotation to the `KnativeServing` CR:
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
  annotations:
    serverless.openshift.io/enable-secret-informer-filtering: "true" <1>
spec:
  ingress:
    istio:
      enabled: true
  deployments:
    - annotations:
        sidecar.istio.io/inject: "true"
        sidecar.istio.io/rewriteAppHTTPProbers: "true"
      name: activator
    - annotations:
        sidecar.istio.io/inject: "true"
        sidecar.istio.io/rewriteAppHTTPProbers: "true"
      name: autoscaler
----
<1> Adding this annotation injects an environment variable, `ENABLE_SECRET_INFORMER_FILTERING_BY_CERT_UID=true`, to the `net-istio` controller pod.
+
[NOTE]
====
This annotation is ignored if you set a different value by overriding deployments.
====
