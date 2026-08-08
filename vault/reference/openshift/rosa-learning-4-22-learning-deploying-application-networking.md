---
title: "Networking"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-application-networking
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-application-networking
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Networking

[id="learning-deploying-application-networking"]
= Networking

[role="_abstract"]
To explore how applications use microservices, set up intra-cluster networking in OSToy. Separating these application functions provides a practical demonstration of how a microservices architecture operates.

image::deploying-networking-arch.png[OSToy Diagram]

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-networking.adoc
[id="learning-deploying-application-networking-multiple-pods_{context}"]
= Communication across pods

[role="_abstract"]
Pods are the smallest execution units in OpenShift Container Platform. Using pods abstracts the underlying infrastructure and helps you efficiently manage your containerized environments.

In this workshop, there are at least two separate pods, each with its own service. One pod functions as the front end web application with a service and a publicly accessible route. The other pod functions as the backend microservice with a service object so that the front end pod can communicate with the microservice.

Communication occurs across the pods if there is more than one pod. The microservice is not accessible from outside the cluster and other namespaces or projects. The purpose of the microservice is to serve internal web requests and return a JSON object containing the current hostname (the pod's name) and a randomly generated color string. This color string displays a box with that color on the OSToy application web console.
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-networking.adoc
[id="learning-deploying-application-networking-intraculter-networking_{context}"]
= Configuring intra-cluster networking

[role="_abstract"]
You can view your networking configurations such as internal ClusterIP addresses and microservices in your OSToy application. These isolated processes help improve application stability and demonstrate how internal web requests are handled.

.Procedure
. In the OSToy application web console, click *Networking* in the left menu.
. Review the networking configuration. The tile "Hostname Lookup" illustrates how the service name created for a pod translates into an internal ClusterIP address.
+
image::deploying-networking-example.png[OSToy Networking page]

. Enter the name of the microservice created in the "Hostname Lookup" tile following the format: `<service_name>.<namespace>.svc.cluster.local`. You can find the microservice name in the service definition of `ostoy-microservice.yaml` by running the following command:
+
[source,terminal]
----
$ oc get service <name_of_service> -o yaml
----
+
*For example*:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: ostoy-microservice-svc
  labels:
    app: ostoy-microservice
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  selector:
    app: ostoy-microservice
----
+
In this example, the full hostname is `ostoy-microservice-svc.ostoy.svc.cluster.local`.

. An IP address is returned. In this example it is `172.30.165.246`. This is the intra-cluster IP address, which is only accessible from within the cluster.
+
image::deploying-networking-dns.png[OSToy DNS]

[role="_additional-resources"]
== Additional resources

* About network policy
