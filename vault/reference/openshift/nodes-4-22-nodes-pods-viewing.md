---
title: "Viewing pods"
type: reference
domain: openshift
slug: nodes-4-22-nodes-pods-viewing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-pods-viewing
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Viewing pods

[id="nodes-pods-viewing"]
= Viewing pods

[role="_abstract"]
As an administrator, you can view cluster pods, check their health, and evaluate the overall health of the cluster. You can also view a list of pods associated with a specific project or view usage statistics about pods. Regularly viewing pods can help you detect problems early, track resource usage, and ensure cluster stability.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-viewing.adoc

[id="nodes-pods-viewing-project_{context}"]
= Viewing pods in a project

[role="_abstract"]
You can display pod usage statistics, such as CPU, memory, and storage consumption, to monitor container runtime environments and ensure efficient resource use.

.Procedure

. Change to the project by entering the following command:
+
[source,terminal]
----
$ oc project <project_name>
----

. Obtain a list of pods by entering the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE
console-698d866b78-bnshf   1/1     Running   2          165m
console-698d866b78-m87pm   1/1     Running   2          165m
----

. Optional: Add the `-o wide` flags to view the pod IP address and the node where the pod is located. For example:
+
[source,terminal]
----
$ oc get pods -o wide
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE    IP            NODE                           NOMINATED NODE
console-698d866b78-bnshf   1/1     Running   2          166m   10.128.0.24   ip-10-0-152-71.ec2.internal    <none>
console-698d866b78-m87pm   1/1     Running   2          166m   10.129.0.23   ip-10-0-173-237.ec2.internal   <none>
----

// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-viewing.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-describe-pod_{context}"]
= Describing a pod

[role="_abstract"]
To troubleshoot pod issues and view detailed information about a pod in OpenShift Container Platform, you can describe a pod using the `oc describe pod` command. The *Events* section in the output provides detailed information about the pod and the containers inside of it.

.Procedure

* Describe a pod by running the following command:
+
[source,terminal]
----
$ oc describe pod -n <namespace> busybox-1
----
+
.Example output
[source,terminal]
----
Name:             busybox-1
Namespace:        busy
Priority:         0
Service Account:  default
Node:             worker-3/192.168.0.0
Start Time:       Mon, 27 Nov 2023 14:41:25 -0500
Labels:           app=busybox
                  pod-template-hash=<hash>
Annotations:      k8s.ovn.org/pod-networks:
…
Events:
  Type    Reason   Age                   From     Message
  ----    ------   ----                  ----     -------
  Normal  Pulled   41m (x170 over 7d1h)  kubelet  Container image "quay.io/quay/busybox:latest" already present on machine
  Normal  Created  41m (x170 over 7d1h)  kubelet  Created container busybox
  Normal  Started  41m (x170 over 7d1h)  kubelet  Started container busybox
----

// Module included in the following assemblies:
//
// * nodes/nodes-pods-viewing.adoc

[id="nodes-pods-viewing-usage_{context}"]
= Viewing pod usage statistics

[role="_abstract"]
You can display usage statistics about pods, including CPU, memory, and storage consumption. By monitoring pod usage levels you can help ensure efficient resource use.

.Prerequisites

* You must have `cluster-reader` permission to view the usage statistics.
* Metrics must be installed to view the usage statistics.

.Procedure

. View the usage statistics by entering the following command:
+
[source,terminal]
----
$ oc adm top pods -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                         CPU(cores)   MEMORY(bytes)
console-7f58c69899-q8c8k     0m           22Mi
console-7f58c69899-xhbgg     0m           25Mi
downloads-594fcccf94-bcxk8   3m           18Mi
downloads-594fcccf94-kv4p6   2m           15Mi
----

. Optional: Add the `--selector=''` label to view usage statistics for pods with labels. Note that you must choose the label query to filter on, such as `=`, `==`, or `!=`. For example:
+
[source,terminal]
----
$ oc adm top pod --selector='<pod_name>'
----

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization.adoc
// * nodes/pods/nodes-pods-viewing.adoc

[id="viewing-resource-logs-cli-console_{context}"]
= Viewing resource logs

[role="_abstract"]
You can view logs for resources in the {oc-first} or web console. By viewing logs for resources, you can troubleshoot issues and monitor resource behavior.

Logs display from the end (or tail) by default.

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization.adoc
// * nodes/pods/nodes-pods-viewing.adoc

[id="viewing-resource-logs-console_{context}"]
= Viewing resource logs by using the web console

[role="_abstract"]
You can view resource logs by using the OpenShift Container Platform web console. By viewing logs for resources, you can troubleshoot issues and monitor resource behavior.

.Procedure

. In the OpenShift Container Platform console, navigate to *Workloads* -> *Pods* or navigate to the pod through the resource you want to investigate.
+
[NOTE]
====
Some resources, such as builds, do not have pods to query directly. In such instances, you can locate the *Logs* link on the *Details* page for the resource.
====

. Select a project from the drop-down menu.

. Click the name of the pod you want to investigate.

. Click *Logs*.

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization.adoc
// * nodes/pods/nodes-pods-viewing.adoc

[id="viewing-resource-logs-cli_{context}"]
= Viewing resource logs by using the CLI

[role="_abstract"]
You can view resource logs by using the command-line interface (CLI). By viewing logs for resources, you can troubleshoot issues and monitor resource behavior.

.Prerequisites

* Access to the {oc-first}.

.Procedure

* View the log for a specific pod by entering the following command:
+
[source,terminal]
----
$ oc logs -f <pod_name> -c <container_name>
----
+
--
where:

`-f`:: Optional: Specifies that the output follows what is being written into the logs.
`<pod_name>`:: Specifies the name of the pod.
`<container_name>`:: Optional: Specifies the name of a container. When a pod has more than one container, you must specify the container name.
--
+
For example:
+
[source,terminal]
----
$ oc logs -f ruby-57f7f4855b-znl92 -c ruby
----

* View the log for a specific resource by entering the following command:
+
[source,terminal]
----
$ oc logs <object_type>/<resource_name>
----
+
For example:
+
[source,terminal]
----
$ oc logs deployment/ruby
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* oc describe
