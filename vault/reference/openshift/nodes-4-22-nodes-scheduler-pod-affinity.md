---
title: "Placing pods relative to other pods using affinity and anti-affinity rules"
type: reference
domain: openshift
slug: nodes-4-22-nodes-scheduler-pod-affinity
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-scheduler-pod-affinity
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Placing pods relative to other pods using affinity and anti-affinity rules

[id="nodes-scheduler-pod-affinity"]
= Placing pods relative to other pods using affinity and anti-affinity rules

[role="_abstract"]
To control workload distribution, you can use pod affinity and anti-affinity rules to specify whether pods must be scheduled close to or separate from other pods.

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-pod-affinity.adoc

[id="nodes-scheduler-pod-affinity-about_{context}"]
= Understanding pod affinity

[role="_abstract"]
You can use _pod affinity_ and _pod anti-affinity_ to constrain which nodes your pod is eligible to be scheduled on based on the key/value labels on other pods.

* Pod affinity can tell the scheduler to locate a new pod on the same node as other pods if the label selector on the new pod matches the label on the current pod.
* Pod anti-affinity can prevent the scheduler from locating a new pod on the same node as pods with the same labels if the label selector on the new pod matches the label on the current pod.

For example, using affinity rules, you could spread or pack pods within a service or relative to pods in other services. Anti-affinity rules allow you to prevent pods of a particular service  from scheduling  on the same nodes as pods of another service that are known to interfere with the performance of the pods of the first service. Or, you could spread the pods of a service across nodes, availability zones, or availability sets to reduce correlated failures.

[NOTE]
====
A label selector might match pods with multiple pod deployments. Use unique combinations of labels when configuring anti-affinity rules to avoid matching pods.
====

There are two types of pod affinity rules: _required_ and _preferred_.

Required rules *must* be met before a pod can be scheduled on a node. Preferred rules specify that, if the rule is met, the scheduler tries to enforce the rules, but does not guarantee enforcement.

[NOTE]
====
Depending on your pod priority and preemption settings, the scheduler might not be able to find an appropriate node for a pod without violating affinity
requirements. If so, a pod might not be scheduled.

To prevent this situation, carefully configure pod affinity with equal-priority pods.
====

You configure pod affinity/anti-affinity through the `Pod` spec files. You can specify a required rule, a preferred rule, or both. If you specify both, the node must first meet the required rule, then attempts to meet the preferred rule.

The following example shows a `Pod` spec configured for pod affinity and anti-affinity.

In this example, the pod affinity rule indicates that the pod can schedule onto a node only if that node has at least one already-running pod with a label that has the key `security` and value `S1`. The pod anti-affinity rule says that the pod prefers to not schedule onto a node if that node is already running a pod with label having key `security` and value `S2`.

.Sample `Pod` config file with pod affinity
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: with-pod-affinity
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - S1
        topologyKey: topology.kubernetes.io/zone
  containers:
  - name: with-pod-affinity
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
----
where:

`spec.affinity.podAffinity`:: Specifies a stanza to configure pod affinity.
`spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution`:: Specifies the parameters for a _required_ rule. Configure the following `labelSelector.matchExpressions.key` parameters:
+
--
`key`:: Specifies the key of the key/value pair (label) that must be matched to apply the rule.
`values`:: Specifies the value of the key/value pair (label) that must be matched to apply the rule.
`operator`:: Specifies the relationship between the label on the existing pod and the set of values in the `matchExpression` parameters in the specification for the new pod. Can be `In`, `NotIn`, `Exists`, or `DoesNotExist`.
--

.Sample `Pod` config file with pod anti-affinity
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: with-pod-antiaffinity
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: security
              operator: In
              values:
              - S2
          topologyKey: kubernetes.io/hostname
  containers:
  - name: with-pod-affinity
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
----
where:

`spec.affinity.podAffinity`:: Specifies a stanza to configure pod affinity.
`spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution`:: Specifies the parameters for a _preferred_ rule. Configure a weight and the following `podAffinityTerm.labelSelector.matchExpressions` parameters:
+
--
`weight`:: Specifies the weight for a preferred rule. The node with the highest weight is preferred.
`key`:: Specifies the key of the key/value pair (label) that must be matched to apply the rule.
`values`:: Specifies the value of the key/value pair (label) that must be matched to apply the rule.
`operator`:: Specifies the relationship between the label on the existing pod and the set of values in the `matchExpression` parameters in the specification for the new pod. Can be `In`, `NotIn`, `Exists`, or `DoesNotExist`.
--

[NOTE]
====
If labels on a node change at runtime such that the affinity rules on a pod are no longer met, the pod continues to run on the node.
====

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-pod-affinity.adoc

[id="nodes-scheduler-pod-affinity-configuring_{context}"]
= Configuring a pod affinity rule

[role="_abstract"]
You can use the following example pod specifications to create a pod with a label and a pod that uses affinity to allow scheduling with that pod.

[NOTE]
====
You cannot add an affinity directly to a scheduled pod.
====

.Procedure

. Create a pod with a specific label in the pod spec:
+
.. Create a YAML file with the following content:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: security-s1
  labels:
    security: S1
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: security-s1
    image: docker.io/ocpqe/hello-pod
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
----
+
.. Create the pod.
+
[source,terminal]
----
$ oc create -f <pod-spec>.yaml
----

. When creating other pods, configure the following parameters to add the affinity:
+
.. Create a YAML file with the following content:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: security-s1-east
# ...
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            values:
            - S1
            operator: In
        topologyKey: topology.kubernetes.io/zone
# ...
----
where:

`spec.affinity.podAffinity`:: Specifies a stanza to configure pod affinity.
`spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution`:: Specifies the parameters for a _required_ rule. Alternatively, you can configure a _preferred_ rule by using the `preferredDuringSchedulingIgnoredDuringExecution` paarmeter.
+
Configure the following `labelSelector.matchExpressions` parameters. If you want the new pod to be scheduled with the other pod, use the same `key` and `values` parameters as the label on the first pod.
+
--
`key`:: Specifies the key of the key/value pair (label) that must be matched to apply the rule.
`value`:: Specifies the value of the key/value pair (label) that must be matched to apply the rule.
`operator`:: Specifies the relationship between the label on the existing pod and the set of values in the `matchExpression` parameters in the specification for the new pod. Can be `In`, `NotIn`, `Exists`, or `DoesNotExist`.
`topologyKey`:: Specifies a prepopulated Kubernetes label that the system uses to denote such a topology domain.
--

.. Create the pod.
+
[source,terminal]
----
$ oc create -f <pod-spec>.yaml
----

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-pod-affinity.adoc

[id="nodes-scheduler-pod-anti-affinity-configuring_{context}"]
= Configuring a pod anti-affinity rule

[role="_abstract"]
To specify a preference to prevent a pod from being scheduling with another pod, you can create a pod with a label and a pod that uses an anti-affinity preferred rule.

The following steps demonstrate a simple two-pod configuration that creates pod with a label and a pod that uses an anti-affinity preferred rule to attempt to prevent scheduling with that pod.

[NOTE]
====
You cannot add an affinity directly to a scheduled pod.
====

.Procedure

. Create a pod with a specific label in the pod spec:
+
.. Create a YAML file with the following content:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: security-s1
  labels:
    security: S1
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: security-s1
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
----
+
.. Create the pod.
+
[source,terminal]
----
$ oc create -f <pod-spec>.yaml
----

. When creating other pods, configure the following parameters:
+
.. Create a YAML file with the following content:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: security-s2-east
# ...
spec:
# ...
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: security
              values:
              - S1
              operator: In
          topologyKey: kubernetes.io/hostname
# ...
----
where:

`spec.affinity.podAffinity`:: Specifies a stanza to configure pod affinity.
`spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution`:: Specifies the parameters for a _preferred_ rule. Alternatively, you can configure a _required_ rule by using the `requiredDuringSchedulingIgnoredDuringExecution` parameter.
+
Configure a weight and the following `podAffinityTerm.labelSelector.matchExpressions` parameters. If you want the new pod to be scheduled with the other pod, use the same `key` and `values` parameters as the label on the first pod.
+
--
`weight`:: For a preferred rule, specifies a weight for the node, as a number 1-100. The node with highest weight is preferred.
`key`:: Specifies the key of the key/value pair (label) that must be matched to apply the rule.
`value`:: Specifies the value of the key/value pair (label) that must be matched to apply the rule.
`operator`:: Specifies the relationship between the label on the existing pod and the set of values in the `matchExpression` parameters in the specification for the new pod. Can be `In`, `NotIn`, `Exists`, or `DoesNotExist`.
`topologyKey`:: Specifies a prepopulated Kubernetes label that the system uses to denote such a topology domain.
--

.. Create the pod.
+
[source,terminal]
----
$ oc create -f <pod-spec>.yaml
----

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-affinity.adoc

[id="nodes-scheduler-pod-affinity-example_{context}"]
= Sample pod affinity and anti-affinity rules

[role="_abstract"]
Use these configuration examples to understand how matching labels, non-matching labels, and specific label selectors affect how the cluster schedules pods onto nodes.

[id="nodes-scheduler-pod-affinity-example-affinity_{context}"]
== Pod Affinity

The following example demonstrates pod affinity for pods with matching labels and label selectors.

* The pod *team4* has the label `team:4`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: team4
  labels:
     team: "4"
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: ocp
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The pod *team4a* has the label selector `team:4` under `podAffinity`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: team4a
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: team
            operator: In
            values:
            - "4"
        topologyKey: kubernetes.io/hostname
  containers:
  - name: pod-affinity
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The *team4a* pod is scheduled on the same node as the *team4* pod.

[id="nodes-scheduler-pod-affinity-example-antiaffinity_{context}"]
== Pod Anti-affinity

The following example demonstrates pod anti-affinity for pods with matching labels and label selectors.

* The pod *pod-s1* has the label `security:s1`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-s1
  labels:
    security: s1
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: ocp
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The pod *pod-s2* has the label selector `security:s1` under `podAntiAffinity`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-s2
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - s1
        topologyKey: kubernetes.io/hostname
  containers:
  - name: pod-antiaffinity
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The pod *pod-s2* cannot be scheduled on the same node as `pod-s1`.

[id="nodes-scheduler-pod-affinity-example-no-labels_{context}"]
== Pod Affinity with no Matching Labels

The following example demonstrates pod affinity for pods without matching labels and label selectors.

* The pod *pod-s1* has the label `security:s1`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-s1
  labels:
    security: s1
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: ocp
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The pod *pod-s2* has the label selector `security:s2`.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-s2
# ...
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - s2
        topologyKey: kubernetes.io/hostname
  containers:
  - name: pod-affinity
    image: docker.io/ocpqe/hello-pod
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
# ...
----

* The pod *pod-s2* is not scheduled unless there is a node with a pod that has the `security:s2` label. If there is no other pod with that label, the new pod remains in a pending state:
+
.Example output
[source,terminal]
----
NAME      READY     STATUS    RESTARTS   AGE       IP        NODE
pod-s2    0/1       Pending   0          32s       <none>
----

// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-node-affinity.adoc
// * nodes/scheduling/nodes-scheduler-pod-affinity.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-overriding-operator-pod-affinity_{context}"]

= Controlling where an Operator is installed

= Using pod affinity and anti-affinity to control where an Operator is installed

= Using node affinity to control where an Operator is installed

[role="_abstract"]
You can use affinities to schedule an Operator pod on a specific node or set of nodes.

By default, when you install an Operator, OpenShift Container Platform installs the Operator pod on one of your compute nodes randomly. However, the following examples describe situations where you might want to schedule an Operator pod to a specific node or set of nodes:

* If an Operator requires a particular platform, such as `amd64` or `arm64`
* If an Operator requires a particular operating system, such as Linux or Windows
* If you want Operators that work together scheduled on the same host or on hosts located on the same rack
* If you want Operators dispersed throughout the infrastructure to avoid downtime due to network or hardware issues

You can control where an Operator pod is installed by adding node affinity, pod affinity, or pod anti-affinity constraints to the Operator's `Subscription` object. Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. Pod affinity enables you to ensure that related pods are scheduled to the same node. Pod anti-affinity allows you to prevent a pod from being scheduled on a node.

You can control where an Operator pod is installed by adding a pod affinity or anti-affinity to the Operator's `Subscription` object.

You can control where an Operator pod is installed by adding a node affinity constraints to the Operator's `Subscription` object.

The following examples show how to use node affinity or pod anti-affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:
The following examples show how to use node affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:

The following node affinity example places the Operator pod on a specific node:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-163-94.us-west-2.compute.internal
#...
----

This node affinity requires the Operator's pod be scheduled on a node named `ip-10-0-163-94.us-west-2.compute.internal`.

The following node affinity example places the Operator pod on a node with a specific platform:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/arch
              operator: In
              values:
              - arm64
            - key: kubernetes.io/os
              operator: In
              values:
              - linux
#...
----

This node affinity requires the Operator's pod be scheduled on a node with the `kubernetes.io/arch=arm64` and `kubernetes.io/os=linux` labels.

The following example shows how to use pod anti-affinity to prevent the installation the Custom Metrics Autoscaler Operator from any node that has pods with a specific label:

The following pod affinity example places the Operator pod on one or more specific nodes:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - test
          topologyKey: kubernetes.io/hostname
#...
----

This pod affinity places the Operator's pod on a node that has pods with the `app=test` label.

The following pod anti-affinity example prevents the Operator pod from one or more specific nodes:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: cpu
              operator: In
              values:
              - high
          topologyKey: kubernetes.io/hostname
#...
----

This pod anti-affinity prevents the Operator's pod from being scheduled on a node that has pods with the `cpu=high` label.

To control the placement of an Operator pod, complete the following steps.

.Procedure

. Install the Operator as usual.

. If needed, ensure that your nodes are labeled to properly respond to the affinity.

. Edit the Operator `Subscription` object to add an affinity:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-185-229.ec2.internal
#...
----
where:

`spec.config.affinity`:: Specifies a `nodeAffinity`, `podAffinity`, or `podAntiAffinity`. See the Additional resources section that follows for information about creating the affinity.
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-185-229.ec2.internal
#...
----
where:

`spec.config.affinity`:: Specifies a `nodeAffinity`.
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - ip-10-0-185-229.ec2.internal
            topologyKey: topology.kubernetes.io/zone
#...
----
where:

`spec.config.affinity`:: Specifies a `podAffinity` or `podAntiAffinity`.

.Verification

* To ensure that the pod is deployed on the specific node, run the following command:
+
[source,yaml]
----
$ oc get pods -o wide
----
+
.Example output
[source,terminal]
----
NAME                                                  READY   STATUS    RESTARTS   AGE   IP            NODE                           NOMINATED NODE   READINESS GATES
custom-metrics-autoscaler-operator-5dcc45d656-bhshg   1/1     Running   0          50s   10.131.0.20   ip-10-0-185-229.ec2.internal   <none>           <none>
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Node label (Kubernetes documentation)
