---
title: "Enabling multicast for a project"
type: reference
domain: openshift
slug: networking-4-22-enabling-multicast
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/enabling-multicast
version: 4.22
family: networking
documentKind: "Documentation"
---

# Enabling multicast for a project

[id="nw-ovn-kubernetes-enabling-multicast"]
= Enabling multicast for a project

[role="_abstract"]
In OpenShift Container Platform with OVN-Kubernetes, you can enable IP multicast on a per-project basis so pods can send and receive multicast traffic.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/enabling-multicast.adoc

[id="nw-about-multicast_{context}"]
= About multicast

[role="_abstract"]
With IP multicast in OpenShift Container Platform, data is broadcast to many IP addresses simultaneously. With OVN-Kubernetes, multicast is off by default and is not affected by network policies when you enable it in a project.

[IMPORTANT]
====
* At this time, multicast is best used for low-bandwidth coordination or service discovery and not a high-bandwidth solution.
* By default, network policies affect all connections in a namespace. However, multicast is unaffected by network policies. If multicast is enabled in the same namespace as your network policies, it is always allowed, even if there is a `deny-all` network policy.
* Cluster administrators must consider the implications of the exemption of multicast from network policies before enabling it.
====

Multicast traffic between OpenShift Container Platform pods is disabled by default. If you are using the OVN-Kubernetes network plugin, you can enable multicast on a per-project basis.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/enabling-multicast.adoc

[id="nw-enabling-multicast_{context}"]
= Enabling multicast between pods

[role="_abstract"]
To enable multicast between pods in a project, you can add the `k8s.ovn.org/multicast-enabled` annotation to the namespace by using the `oc annotate` command or a namespace manifest.

.Prerequisites

* Install the {oc-first}.
* You must log in to the cluster with a user that has the `cluster-admin`
or the `dedicated-admin`
role.

.Procedure

* Run the following command to enable multicast for a project. Replace `<namespace>` with the namespace for the project you want to enable multicast for.
+
[source,terminal,subs="attributes+"]
----
$ oc annotate {namespace} <namespace> \
    {annotation}
----
+
[TIP]
====
You can alternatively apply the following YAML to add the annotation:

[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/multicast-enabled: "true"
----
====

.Verification

To verify that multicast is enabled for a project, complete the following procedure:

. Change your current project to the project that you enabled multicast for. Replace `<project>` with the project name.
+
[source,terminal]
----
$ oc project <project>
----

. Create a pod to act as a multicast receiver:
+
[source,terminal]
----
$ cat <<EOF| oc create -f -
apiVersion: v1
kind: Pod
metadata:
  name: mlistener
  labels:
    app: multicast-verify
spec:
  containers:
    - name: mlistener
      image: registry.access.redhat.com/ubi9
      command: ["/bin/sh", "-c"]
      args:
        ["dnf -y install socat hostname && sleep inf"]
      ports:
        - containerPort: 30102
          name: mlistener
          protocol: UDP
EOF
----

. Create a pod to act as a multicast sender:
+
[source,terminal]
----
$ cat <<EOF| oc create -f -
apiVersion: v1
kind: Pod
metadata:
  name: msender
  labels:
    app: multicast-verify
spec:
  containers:
    - name: msender
      image: registry.access.redhat.com/ubi9
      command: ["/bin/sh", "-c"]
      args:
        ["dnf -y install socat && sleep inf"]
EOF
----

. In a new terminal window or tab, start the multicast listener.

.. Get the IP address for the Pod:
+
[source,terminal]
----
$ POD_IP=$(oc get pods mlistener -o jsonpath='{.status.podIP}')
----

.. Start the multicast listener by entering the following command:
+
[source,terminal]
----
$ oc exec mlistener -i -t -- \
    socat UDP4-RECVFROM:30102,ip-add-membership=224.1.0.1:$POD_IP,fork EXEC:hostname
----

. Start the multicast transmitter.

.. Get the pod network IP address range:
+
[source,terminal]
----
$ CIDR=$(oc get Network.config.openshift.io cluster \
    -o jsonpath='{.status.clusterNetwork[0].cidr}')
----

.. To send a multicast message, enter the following command:
+
[source,terminal]
----
$ oc exec msender -i -t -- \
    /bin/bash -c "echo | socat STDIO UDP4-DATAGRAM:224.1.0.1:30102,range=$CIDR,ip-multicast-ttl=64"
----
+
If multicast is working, the previous command returns the following output:
+
[source,text]
----
mlistener
----
