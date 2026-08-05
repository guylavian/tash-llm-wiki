---
title: "Using the Stream Control Transmission Protocol (SCTP)"
type: reference
domain: openshift
slug: networking-4-22-using-sctp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/using-sctp
version: 4.22
family: networking
documentKind: "Documentation"
---

# Using the Stream Control Transmission Protocol (SCTP)

[id="using-sctp"]
= Using the Stream Control Transmission Protocol (SCTP)

As a cluster administrator, you can use the Stream Control Transmission Protocol (SCTP) on a bare-metal cluster.

// Module included in the following assemblies:
//
// * networking/using-sctp.adoc

[id="nw-sctp-about_{context}"]
= Support for SCTP on OpenShift Container Platform

As a cluster administrator, you can enable SCTP on the hosts in the cluster. On {op-system-first}, the SCTP module is disabled by default.

SCTP is a reliable message based protocol that runs on top of an IP network.

When enabled, you can use SCTP as a protocol with pods, services, and network policy.
A `Service` object must be defined with the `type` parameter set to either the `ClusterIP` or `NodePort` value.

[id="example_configurations_{context}"]
== Example configurations using SCTP protocol

You can configure a pod or service to use SCTP by setting the `protocol` parameter to the `SCTP` value in the pod or service object.

In the following example, a pod is configured to use SCTP:

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  namespace: project1
  name: example-pod
spec:
  containers:
    - name: example-pod
...
      ports:
        - containerPort: 30100
          name: sctpserver
          protocol: SCTP
----

In the following example, a service is configured to use SCTP:

[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  namespace: project1
  name: sctpserver
spec:
...
  ports:
    - name: sctpserver
      protocol: SCTP
      port: 30100
      targetPort: 30100
  type: ClusterIP
----

In the following example, a `NetworkPolicy` object is configured to apply to SCTP network traffic on port `80` from any pods with a specific label:

[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-sctp-on-http
spec:
  podSelector:
    matchLabels:
      role: web
  ingress:
  - ports:
    - protocol: SCTP
      port: 80
----

// Module included in the following assemblies:
//
// * networking/using-sctp.adoc

[id="nw-sctp-enabling_{context}"]
= Enabling Stream Control Transmission Protocol (SCTP)

As a cluster administrator, you can load and enable the blacklisted SCTP kernel module on worker nodes in your cluster.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Create a file named `load-sctp-module.yaml` that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: load-sctp-module
  labels:
    machineconfiguration.openshift.io/role: worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - path: /etc/modprobe.d/sctp-blacklist.conf
          mode: 0644
          overwrite: true
          contents:
            source: data:,
        - path: /etc/modules-load.d/sctp-load.conf
          mode: 0644
          overwrite: true
          contents:
            source: data:,sctp
----

. To create the `MachineConfig` object, enter the following command:
+
[source,terminal]
----
$ oc create -f load-sctp-module.yaml
----

. Optional: To watch the status of the nodes while the MachineConfig Operator applies the configuration change, enter the following command. When the status of a node transitions to `Ready`, the configuration update is applied.
+
[source,terminal]
----
$ oc get nodes
----

// Module included in the following assemblies:
//
// * networking/using-sctp.adoc

[id="nw-sctp-verifying_{context}"]
= Verifying Stream Control Transmission Protocol (SCTP) is enabled

You can verify that SCTP is working on a cluster by creating a pod with an application that listens for SCTP traffic, associating it with a service, and then connecting to the exposed service.

.Prerequisites

* Access to the internet from the cluster to install the `nc` package.
* Install the OpenShift CLI (`oc`).
* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Create a pod starts an SCTP listener:

.. Create a file named `sctp-server.yaml` that defines a pod with the following YAML:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: sctpserver
  labels:
    app: sctpserver
spec:
  containers:
    - name: sctpserver
      image: {image}
      command: ["/bin/sh", "-c"]
      args:
        ["dnf install -y nc && sleep inf"]
      ports:
        - containerPort: 30102
          name: sctpserver
          protocol: SCTP
----

.. Create the pod by entering the following command:
+
[source,terminal]
----
$ oc create -f sctp-server.yaml
----

. Create a service for the SCTP listener pod.

.. Create a file named `sctp-service.yaml` that defines a service with the following YAML:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: sctpservice
  labels:
    app: sctpserver
spec:
  type: NodePort
  selector:
    app: sctpserver
  ports:
    - name: sctpserver
      protocol: SCTP
      port: 30102
      targetPort: 30102
----

.. To create the service, enter the following command:
+
[source,terminal]
----
$ oc create -f sctp-service.yaml
----

. Create a pod for the SCTP client.

.. Create a file named `sctp-client.yaml` with the following YAML:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: sctpclient
  labels:
    app: sctpclient
spec:
  containers:
    - name: sctpclient
      image: {image}
      command: ["/bin/sh", "-c"]
      args:
        ["dnf install -y nc && sleep inf"]
----

.. To create the `Pod` object, enter the following command:
+
[source,terminal]
----
$ oc apply -f sctp-client.yaml
----

. Run an SCTP listener on the server.

.. To connect to the server pod, enter the following command:
+
[source,terminal]
----
$ oc rsh sctpserver
----

.. To start the SCTP listener, enter the following command:
+
[source,terminal]
----
$ nc -l 30102 --sctp
----

. Connect to the SCTP listener on the server.

.. Open a new terminal window or tab in your terminal program.

.. Obtain the IP address of the `sctpservice` service. Enter the following command:
+
[source,terminal]
----
$ oc get services sctpservice -o go-template='{{.spec.clusterIP}}{{"\n"}}'
----

.. To connect to the client pod, enter the following command:
+
[source,terminal]
----
$ oc rsh sctpclient
----

.. To start the SCTP client, enter the following command. Replace `<cluster_IP>` with the cluster IP address of the `sctpservice` service.
+
[source,terminal]
----
# nc <cluster_IP> 30102 --sctp
----
