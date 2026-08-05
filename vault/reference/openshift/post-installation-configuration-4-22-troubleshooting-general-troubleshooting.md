---
title: "General troubleshooting"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-general-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-general-troubleshooting
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# General troubleshooting

[id="troubleshooting-general-troubleshooting"]
= General troubleshooting

When you encounter a problem, the first step is to find the specific area where the issue is happening.
To narrow down the potential problematic areas, complete one or more of the following tasks:

* Query your cluster
* Check your pod logs
* Debug a pod
* Review events

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-query-cluster_{context}"]
= Querying your cluster

[role="_abstract"]
Get information about your cluster so that you can more accurately find potential problems.

.Procedure

. Switch into a project by running the following command:
+
[source,terminal]
----
$ oc project <project_name>
----

. Query your cluster version, cluster Operator, and node within that namespace by running the following command:
+
--
[source,terminal]
----
$ oc get clusterversion,clusteroperator,node
----

[source,terminal]
----
NAME                                         VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
clusterversion.config.openshift.io/version   4.16.11   True        False         62d     Cluster version is 4.16.11

NAME                                                                           VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
clusteroperator.config.openshift.io/authentication                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/baremetal                                  4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cloud-controller-manager                   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cloud-credential                           4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cluster-autoscaler                         4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/config-operator                            4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/console                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/control-plane-machine-set                  4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/csi-snapshot-controller                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/dns                                        4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/etcd                                       4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/image-registry                             4.16.11   True        False         False      55d
clusteroperator.config.openshift.io/ingress                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/insights                                   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-apiserver                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-controller-manager                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-scheduler                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-storage-version-migrator              4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-api                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-approver                           4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-config                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/marketplace                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/monitoring                                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/network                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/node-tuning                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-apiserver                        4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-controller-manager               4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-samples                          4.16.11   True        False         False      35d
clusteroperator.config.openshift.io/operator-lifecycle-manager                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/operator-lifecycle-manager-catalog         4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/operator-lifecycle-manager-packageserver   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/service-ca                                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/storage                                    4.16.11   True        False         False      62d

NAME                STATUS   ROLES                         AGE   VERSION
node/ctrl-plane-0   Ready    control-plane,master,worker   62d   v1.29.7
node/ctrl-plane-1   Ready    control-plane,master,worker   62d   v1.29.7
node/ctrl-plane-2   Ready    control-plane,master,worker   62d   v1.29.7
----
--
+
For more information, see "oc get" and "Reviewing pod status".

[role="_additional-resources"]
.Additional resources

* oc get
* Reviewing pod status

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-check-logs_{context}"]
= Checking pod logs

[role="_abstract"]
Get logs from the pod so that you can review the logs for issues.

.Procedure

. List the pods by running the following command:
+
--
[source,terminal]
----
$ oc get pod
----

[source,terminal]
----
NAME        READY   STATUS    RESTARTS          AGE
busybox-1   1/1     Running   168 (34m ago)     7d
busybox-2   1/1     Running   119 (9m20s ago)   4d23h
busybox-3   1/1     Running   168 (43m ago)     7d
busybox-4   1/1     Running   168 (43m ago)     7d
----
--

. Check pod log files by running the following command:
+
[source,terminal]
----
$ oc logs -n <namespace> busybox-1
----
+
For more information, see "oc logs", "Logging", and "Inspecting pod and container logs".

[role="_additional-resources"]
.Additional resources

* oc logs
* Logging
* Inspecting pod and container logs

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

[role="_additional-resources"]
.Additional resources

* oc describe

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-review-events_{context}"]
= Reviewing events

[role="_abstract"]
You can review the events in a given namespace to find potential issues.

.Procedure

. Check for events in your namespace by running the following command:
+
[source,terminal]
----
$ oc get events -n <namespace> --sort-by=".metadata.creationTimestamp"
----
+
The `--sort-by=".metadata.creationTimestamp"` flag places the most recent events at the end of the output.

. Optional: If the events within your specified namespace do not provide enough information, expand your query to all namespaces by running the following command:
+
[source,terminal]
----
$ oc get events -A --sort-by=".metadata.creationTimestamp"
----
+
The `--sort-by=".metadata.creationTimestamp"` flag places the most recent events at the end of the output.
+
To filter the results of all events from a cluster, you can use the `grep` command.
For example, if you are looking for errors, the errors can appear in two different sections of the output: the `TYPE` or `MESSAGE` sections.
With the `grep` command, you can search for keywords, such as `error` or `failed`.

. For example, search for a message that contains `warning` or `error` by running the following command:
+
--
[source,terminal]
----
$ oc get events -A | grep -Ei "warning|error"
----

[source,terminal]
----
NAMESPACE    LAST SEEN   TYPE      REASON          OBJECT              MESSAGE
openshift    59s         Warning   FailedMount     pod/openshift-1     MountVolume.SetUp failed for volume "v4-0-config-user-idp-0-file-data" : references non-existent secret key: test
----
--

. Optional: To clean up the events and see only recurring events, you can delete the events in the relevant namespace by running the following command:
+
[source,terminal]
----
$ oc delete events -n <namespace> --all
----
+
For more information, see "Watching cluster events".

[role="_additional-resources"]
.Additional resources

* Watching cluster events

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-connect-to-pod_{context}"]
= Connecting to a pod

[role="_abstract"]
You can directly connect to a currently running pod with the `oc rsh` command, which provides you with a shell on that pod.

[WARNING]
====
In pods that run a low-latency application, latency issues can occur when you run the `oc rsh` command.
Use the `oc rsh` command only if you cannot connect to the node by using the `oc debug` command.
====

.Procedure

* Connect to your pod by running the following command:
+
[source,terminal]
----
$ oc rsh -n <namespace> busybox-1
----
+
For more information, see "oc rsh" and "Accessing running pods".

[role="_additional-resources"]
.Additional resources

* oc rsh
* Accessing running pods

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-general-debug-pod_{context}"]
= Debugging a pod

[role="_abstract"]
In certain cases, you do not want to directly interact with your pod that is in production.

To avoid interfering with running traffic, you can use a secondary pod that is a copy of your original pod.
The secondary pod uses the same components as that of the original pod but does not have running traffic.

.Procedure

. List the pods by running the following command:
+
--
[source,terminal]
----
$ oc get pod
----

[source,terminal]
----
NAME        READY   STATUS    RESTARTS          AGE
busybox-1   1/1     Running   168 (34m ago)     7d
busybox-2   1/1     Running   119 (9m20s ago)   4d23h
busybox-3   1/1     Running   168 (43m ago)     7d
busybox-4   1/1     Running   168 (43m ago)     7d
----
--

. Debug a pod by running the following command:
+
--
[source,terminal]
----
$ oc debug -n <namespace> busybox-1
----

[source,terminal]
----
Starting pod/busybox-1-debug, command was: sleep 3600
Pod IP: 10.133.2.11
----

If you do not see a shell prompt, press Enter.
--
+
For more information, see "oc debug" and "Starting debug pods with root access".

[role="_additional-resources"]
.Additional resources

* oc debug
* Starting debug pods with root access

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-general-troubleshooting.adoc

[id="troubleshooting-run-command-on-pod_{context}"]
= Running a command on a pod

[role="_abstract"]
If you want to run a command or set of commands on a pod without directly logging into it, you can use the `oc exec -it` command.
You can interact with the pod quickly to get process or output information from the pod.
A common use case is to run the `oc exec -it` command inside a script to run the same command on multiple pods in a replica set or deployment.

[WARNING]
====
In pods that run a low-latency application, the `oc exec` command can cause latency issues.
====

.Procedure

* To run a command on a pod without logging into it, run the following command:
+
[source,terminal]
----
$ oc exec -it <pod> -- <command>
----
+
For more information, see "oc exec" and "Executing remote commands in containers".

[role="_additional-resources"]
.Additional resources

* oc exec
* Executing remote commands in containers
