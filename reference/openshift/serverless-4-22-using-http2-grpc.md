---
title: "Using HTTP2 and gRPC"
type: reference
domain: openshift
slug: serverless-4-22-using-http2-grpc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/using-http2-gRPC
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Using HTTP2 and gRPC

[id="using-http2-gRPC_{context}"]
= Using HTTP2 and gRPC

{ServerlessProductName} supports only insecure or edge-terminated routes. Insecure or edge-terminated routes do not support HTTP2 on OpenShift Container Platform. These routes also do not support gRPC because gRPC is transported by HTTP2. If you use these protocols in your application, you must call the application using the ingress gateway directly. To do this you must find the ingress gateway's public address and the application's specific host.

// Module included in the following assemblies:
//
// serverless/knative-serving/external-ingress-routing/using-http2-gRPC.adoc

[id="interacting-serverless-apps-http2-grpc_{context}"]
= Interacting with a serverless application using HTTP2 and gRPC

[IMPORTANT]
====
This method applies to OpenShift Container Platform 4.10 and later. For older versions, see the following section.
====

.Prerequisites

* Install {ServerlessOperatorName} and Knative Serving on your cluster.
* Install the OpenShift CLI (`oc`).
* Create a Knative service.
* Upgrade OpenShift Container Platform 4.10 or later.
* Enable HTTP/2 on OpenShift Ingress controller.

.Procedure

. Add the `serverless.openshift.io/default-enable-http2=true` annotation to the `KnativeServing` Custom Resource:
+
[source,terminal]
----
$ oc annotate knativeserving <your_knative_CR> -n knative-serving serverless.openshift.io/default-enable-http2=true
----

. After the annotation is added, you can verify that the `appProtocol` value of the Kourier service is `h2c`:
+
[source,terminal]
----
$ oc get svc -n knative-serving-ingress kourier -o jsonpath="{.spec.ports[0].appProtocol}"
----
+
.Example output
+
[source,terminal]
----
h2c
----

. Now you can use the gRPC framework over the HTTP/2 protocol for external traffic, for example:
+
[source,golang]
----
import "google.golang.org/grpc"

grpc.Dial(
   YOUR_URL, <1>
   grpc.WithTransportCredentials(insecure.NewCredentials())), <2>
)
----
<1> Your `ksvc` URL.
<2> Your certificate.

[role="_additional-resources"]
.Additional resources
Enabling HTTP/2 Ingress connectivity

// Module included in the following assemblies:
//
// serverless/knative-serving/external-ingress-routing/using-http2-gRPC.adoc

[id="interacting-serverless-apps-http2-grpc-up-to-4-9_{context}"]
= Interacting with a serverless application using HTTP2 and gRPC in OpenShift Container Platform 4.9 and older

[IMPORTANT]
====
This method needs to expose Kourier Gateway using the `LoadBalancer` service type. You can configure this by adding the following YAML to your `KnativeServing` custom resource definition (CRD):

[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: LoadBalancer
...
----
====

.Prerequisites

* Install {ServerlessOperatorName} and Knative Serving on your cluster.
* Install the OpenShift CLI (`oc`).
* Create a Knative service.

.Procedure

. Find the application host. See the instructions in _Verifying your serverless application deployment_.

. Find the ingress gateway's public address:
+
[source,terminal]
----
$ oc -n knative-serving-ingress get svc kourier
----
+
.Example output
+
[source,terminal]
----
NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP                                                             PORT(S)                                                                                                                                      AGE
kourier   LoadBalancer   172.30.51.103   a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com   80:31380/TCP,443:31390/TCP   67m
----
+
The public address is surfaced in the `EXTERNAL-IP` field, and in this case is `a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com`.

. Manually set the host header of your HTTP request to the application's host, but direct the request itself against the public address of the ingress gateway.
+
[source,terminal]
----
$ curl -H "Host: hello-default.example.com" a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com
----
+
.Example output
[source,terminal]
----
Hello Serverless!
----
+
You can also make a direct gRPC request against the ingress gateway:
+
[source,golang]
----
import "google.golang.org/grpc"

grpc.Dial(
    "a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com:80",
    grpc.WithAuthority("hello-default.example.com:80"),
    grpc.WithInsecure(),
)
----
+
[NOTE]
====
Ensure that you append the respective port, 80 by default, to both hosts as shown in the previous example.
====
