---
title: "Tutorial: Networking"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-networking
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-networking
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Networking

[id="cloud-experts-deploying-application-networking"]
= Tutorial: Networking

[role="_abstract"]
This tutorial shows how the OSToy app uses intra-cluster networking to separate functions by using microservices and visualize the scaling of pods.

image::deploying-networking-arch.png[OSToy Diagram]

The diagram shows there are at least two separate pods, each with its own service.

One pod functions as the front end web application with a service and a publicly accessible route. The other pod functions as the backend microservice with a service object so that the front end pod can communicate with the microservice. This communication occurs across the pods if more than one. Because of these communication limits, this microservice is not accessible from outside this cluster or from other namespaces or projects if these are configured. The sole purpose of this microservice is to serve internal web requests and return a JSON object containing the current hostname, which is the pod's name, and a randomly generated color string. This color string is used to display a box with that color displayed in the tile titled "Intra-cluster Communication".

For more information about the networking limitations, see About network policy.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-networking.adoc

[id="cloud-experts-deploying-application-networking-intra-cluster_{context}"]
= Intra-cluster networking

[role="_abstract"]
You can view your networking configurations in your OSToy application.

.Procedure
. In the OSToy application, click *Networking* in the left menu.
. Review the networking configuration. The right tile titled "Hostname Lookup" illustrates how the service name created for a pod can be used to translate into an internal ClusterIP address.
+
image::deploying-networking-example.png[OSToy Networking page]

. Enter the name of the microservice created in the right tile ("Hostname Lookup") following the format of `<service_name>.<namespace>.svc.cluster.local`. You can find this service name in the service definition of `ostoy-microservice.yaml` by running the following command:
+
[source,terminal]
----
$ oc get service <name_of_service> -o yaml
----
+
**Example output**
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

. You see an IP address returned. In this example it is `172.30.165.246`. This is the intra-cluster IP address, which is only accessible from within the cluster.
+
image::deploying-networking-dns.png[OSToy DNS]
