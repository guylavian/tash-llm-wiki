---
title: "Installing the MetalLB Operator"
type: reference
domain: openshift
slug: networking-4-22-metallb-operator-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/metallb-operator-install
version: 4.22
family: networking
documentKind: "Documentation"
---

# Installing the MetalLB Operator

[id="metallb-operator-install"]
= Installing the MetalLB Operator

[role="_abstract"]
As a cluster administrator, you can add the MetalLB Operator so that the Operator can manage the lifecycle for an instance of MetalLB on your cluster.

MetalLB and IP failover are incompatible. If you configured IP failover for your cluster, perform the steps to remove IP failover before you install the Operator.

// Install the Operator with console
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="metallb-installing-using-web-console_{context}"]
= Installing the MetalLB Operator from the software catalog by using the web console

[role="_abstract"]
As a cluster administrator, you can install the MetalLB Operator by using the OpenShift Container Platform web console.

.Prerequisites

* Log in as a user with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.

. Type `metallb` in the *Filter by keyword* box to find the MetalLB Operator.
+
You can also filter options by *Infrastructure Features*. For example, select *Disconnected* if you want to see Operators that work in disconnected environments, also known as restricted network environments.

. Click the *MetalLB Operator* tile and click *Install*.

. On the *Install Operator* page, accept the defaults and click *Install*.
+
The web console displays the *Installing Operator* page with a status update. Wait until the Operator installs before continuing.

. The web console displays the progress of the installation. When the installation is complete, click *View installed Operators*.

.Verification

. To confirm that the installation is successful:

.. Navigate to the *Ecosystem* -> *Installed Operators* page.

.. Check that the Operator is installed in the `metallb-system` namespace and that its status is `Succeeded`.

. If the Operator is not installed successfully, check the status of the Operator and review the logs:

.. Navigate to the *Ecosystem* -> *Installed Operators* page and inspect the `Status` column for any errors or failures.

.. Navigate to the *Workloads* -> *Pods* page and check the logs in any pods in the `metallb-system` project that are reporting issues.

// Install the Operator with CLI
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-installing-operator-cli_{context}"]
= Installing from the software catalog using the CLI

[role="_abstract"]
To install the MetalLB Operator from the software catalog in OpenShift Container Platform without using the web console, you can use the {oc-first}.

It is recommended that when using the CLI you install the Operator in the `metallb-system` namespace.

.Prerequisites

* A cluster installed on bare-metal hardware.
* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a namespace for the MetalLB Operator by entering the following command:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: metallb-system
EOF
----

. Create an Operator group custom resource (CR) in the namespace:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: metallb-operator
  namespace: metallb-system
EOF
----

. Confirm the Operator group is installed in the namespace:
+
[source,terminal]
----
$ oc get operatorgroup -n metallb-system
----
+
The following is example output:
+
[source,terminal]
----
NAME               AGE
metallb-operator   14m
----

. Create a `Subscription` CR:
.. Define the `Subscription` CR and save the YAML file, for example, `metallb-sub.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metallb-operator-sub
  namespace: metallb-system
spec:
  channel: stable
  name: metallb-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----
+
** For the `spec.source` parameter, must specify the `redhat-operators` value.

.. To create the `Subscription` CR, run the following command:
+
[source,terminal]
----
$ oc apply -f metallb-sub.yaml
----

. Optional: To ensure BGP and BFD metrics appear in Prometheus, you can label the namespace as in the following command:
+
[source,terminal]
----
$ oc label ns metallb-system "openshift.io/cluster-monitoring=true"
----

.Verification

The verification steps assume the MetalLB Operator is installed in the `metallb-system` namespace.

. Verify that the Operator installed successfully by running the following command. Wait until the `PHASE` displays `Succeeded`:
+
[source,terminal]
----
$ oc get clusterserviceversion -n metallb-system \
  -o custom-columns=Name:.metadata.name,Phase:.status.phase
----
+
The following is example output:
+
[source,terminal]
----
Name                                                Phase
metallb-operator..0-nnnnnnnnnnnn   Succeeded
----
+
[NOTE]
====
Installation of the Operator might take a few seconds.
====

. Confirm that the install plan is in the namespace:
+
[source,terminal]
----
$ oc get installplan -n metallb-system
----
+
The following is example output:
+
[source,terminal,subs="attributes+"]
----
NAME            CSV                                                 APPROVAL    APPROVED
install-wzg94   metallb-operator..0-nnnnnnnnnnnn   Automatic   true
----

// Starting MetalLB on your cluster
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-operator-initial-config_{context}"]
= Starting MetalLB on your cluster

[role="_abstract"]
To start MetalLB on your cluster after installing the MetalLB Operator in OpenShift Container Platform, you create a single MetalLB custom resource.

.Prerequisites

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

* Install the MetalLB Operator.

.Procedure

. Create a single instance of a MetalLB custom resource:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
EOF
----
+
** For the `metadata.namespace` parameter, substitute `metallb-system` with `openshift-operators` if you installed the MetalLB Operator using the web console.

.Verification

Confirm that the deployment for the MetalLB controller and the daemon set for the MetalLB speaker are running.

[NOTE]
====
It might take a few seconds for the controller deployment and speaker daemon set to become available after you create the `MetalLB` custom resource.
====

. Verify that the deployment for the controller is running:
+
[source,terminal]
----
$ oc get deployment -n metallb-system controller
----
+
The following is example output:
+
[source,terminal]
----
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
controller   1/1     1            1           11m
----

. Verify that the daemon set for the speaker is running:
+
[source,terminal]
----
$ oc get daemonset -n metallb-system speaker
----
+
The following is example output:
+
[source,terminal]
----
NAME      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
speaker   6         6         6       6            6           kubernetes.io/os=linux   18m
----
+
The example output indicates six speaker pods. The number of speaker pods in your cluster might differ from the example output. Verify that the number of speaker pods equals the number of nodes in your cluster. For example, a single-node cluster has one speaker pod.

// Deployment specifications for metallb CR
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-operator-deployment-specifications-for-metallb_{context}"]
= Deployment specifications for MetalLB

[role="_abstract"]
Deployment specifications in the `MetalLB` custom resource control how the MetalLB `controller` and `speaker` pods deploy and run in OpenShift Container Platform.

Use deployment specifications to manage the following tasks:

* Select nodes for MetalLB pod deployment.
* Manage scheduling by using pod priority and pod affinity.
* Assign CPU limits for MetalLB pods.
* Assign a container RuntimeClass for MetalLB pods.
* Assign metadata for MetalLB pods.

// Deployment specs to limit speaker pods to specific nodes
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-operator-limit-speaker-to-nodes_{context}"]
= Limit speaker pods to specific nodes

[role="_abstract"]
You can limit MetalLB `speaker` pods to specific nodes in OpenShift Container Platform by configuring a node selector in the `MetalLB` custom resource. Only nodes that run a `speaker` pod advertise load balancer IP addresses, so you control which nodes serve MetalLB traffic.

The most common reason to limit the `speaker` pods to specific nodes is to ensure that only nodes with network interfaces on specific networks advertise load balancer IP addresses.

If you limit the `speaker` pods to specific nodes and specify `local` for the external traffic policy of a service, then you must ensure that the application pods for the service are deployed to the same nodes.

.Example configuration to limit `speaker` pods to worker nodes
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  speakerTolerations:
  - key: "Example"
    operator: "Exists"
    effect: "NoExecute"
----

** In this example configuration, the `spec.nodeSelector` field assigns the `speaker` pods to worker nodes. You can specify labels that you assigned to nodes or any valid node selector.
** In this example configuration, `spec.speakerToTolerations` pod that this toleration is attached to tolerates any taint that matches the `key` and `effect` values by using the `operator` value.

After you apply a manifest with the `spec.nodeSelector` field, you can check the number of pods that the Operator deployed with the `oc get daemonset -n metallb-system speaker` command.
Similarly, you can display the nodes that match your labels with a command like `oc get nodes -l node-role.kubernetes.io/worker=`.

You can optionally allow the node to control which speaker pods should, or should not, be scheduled on them by using affinity rules. You can also limit these pods by applying a list of tolerations. For more information about affinity rules, taints, and tolerations, see the additional resources.

// Deployment specs to set pod priority and pod affinity
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-operator-setting-pod-priority-affinity_{context}"]
= Configuring pod priority and pod affinity in a MetalLB deployment

[role="_abstract"]
To control scheduling of MetalLB controller and `speaker` pods in OpenShift Container Platform, you can assign pod priority and pod affinity in the `MetalLB` custom resource. You create a `PriorityClass` and set `priorityClassName` and affinity in the `MetalLB` spec, then apply the configuration.

The pod priority indicates the relative importance of a pod on a node and schedules the pod based on this priority. Set a high priority on your `controller` or `speaker` pod to ensure scheduling priority over other pods on the node.

Pod affinity manages relationships among pods. Assign pod affinity to the `controller` or `speaker` pods to control on what node the scheduler places the pod in the context of pod relationships. For example, you can use pod affinity rules to ensure that certain pods are located on the same node or nodes, which can help improve network communication and reduce latency between those components.

.Prerequisites

* You are logged in as a user with `cluster-admin` privileges.

* You have installed the MetalLB Operator.

* You have started the MetalLB Operator on your cluster.

.Procedure

. Create a `PriorityClass` custom resource, such as `myPriorityClass.yaml`, to configure the priority level. This example defines a `PriorityClass` named `high-priority` with a value of `1000000`. Pods that are assigned this priority class are considered higher priority during scheduling compared to pods with lower priority classes:
+
[source,yaml]
----
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
----

. Apply the `PriorityClass` custom resource configuration:
+
[source,bash]
----
$ oc apply -f myPriorityClass.yaml
----

. Create a `MetalLB` custom resource, such as `MetalLBPodConfig.yaml`, to specify the `priorityClassName` and `podAffinity` values:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  logLevel: debug
  controllerConfig:
    priorityClassName: high-priority
    affinity:
      podAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
             app: metallb
          topologyKey: kubernetes.io/hostname
  speakerConfig:
    priorityClassName: high-priority
    affinity:
      podAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
             app: metallb
          topologyKey: kubernetes.io/hostname
----
+
where:
+
--
`spec.controllerConfig.priorityClassName`:: Specifies the priority class for the MetalLB controller pods. In this case, it is set to `high-priority`.

`spec.controllerConfig.affinity.podAffinity`:: Specifies that you are configuring pod affinity rules. These rules dictate how pods are scheduled in relation to other pods or nodes. This configuration instructs the scheduler to schedule pods that have the label `app: metallb` onto nodes that share the same hostname. This helps to co-locate MetalLB-related pods on the same nodes, potentially optimizing network communication, latency, and resource usage between these pods.
--

. Apply the `MetalLB` custom resource configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f MetalLBPodConfig.yaml
----

.Verification

* To view the priority class that you assigned to pods in the `metallb-system` namespace, run the following command:
+
[source,terminal]
----
$ oc get pods -n metallb-system -o custom-columns=NAME:.metadata.name,PRIORITY:.spec.priorityClassName
----
+
.Example output
[source,terminal]
----
NAME                                                 PRIORITY
controller-584f5c8cd8-5zbvg                          high-priority
metallb-operator-controller-manager-9c8d9985-szkqg   <none>
metallb-operator-webhook-server-c895594d4-shjgx      <none>
speaker-dddf7                                        high-priority
----

* Verify that the scheduler placed pods according to pod affinity rules by viewing the metadata for the node of the pod. For example:
+
[source,terminal]
----
$ oc get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name -n metallb-system
----

// Deployment specs to set pod CPU limits
// Module included in the following assemblies:
//
// * networking/metallb/metallb-operator-install.adoc

[id="nw-metallb-operator-setting-pod-CPU-limits_{context}"]
= Configuring pod CPU limits in a MetalLB deployment

[role="_abstract"]
To manage compute resources on nodes running MetalLB in OpenShift Container Platform, you can assign CPU limits to the `controller` and `speaker` pods in the `MetalLB` custom resource. This ensures that all pods on the node have the necessary compute resources to manage workloads and cluster housekeeping.

.Prerequisites

* You are logged in as a user with `cluster-admin` privileges.

* You have installed the MetalLB Operator.

.Procedure

. Create a `MetalLB` custom resource file, such as `CPULimits.yaml`, to specify the `cpu` value for the `controller` and `speaker` pods:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  logLevel: debug
  controllerConfig:
    resources:
      limits:
        cpu: "200m"
  speakerConfig:
    resources:
      limits:
        cpu: "300m"
----

. Apply the `MetalLB` custom resource configuration:
+
[source,bash]
----
$ oc apply -f CPULimits.yaml
----

.Verification

* To view compute resources for a pod, run the following command, replacing `<pod_name>` with your target pod:
+
[source,bash]
----
$ oc describe pod <pod_name>
----

[role="_additional-resources"]
[id="additional-resources_metallb-operator-install"]
== Additional resources

* Placing pods on specific nodes using node selectors
* Controlling pod placement using node taints
* Understanding pod priority
* Understanding pod affinity
