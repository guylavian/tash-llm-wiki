---
title: "Integrating the {lws-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-integrating-lws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/integrating-lws
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Integrating the {lws-operator}

[id="integrating-lws"]
= Integrating the {lws-operator}

[role="_abstract"]
You can integrate the {lws-operator} with {kueue-name} so you can leverage the scheduling and resource management functionality when running LeaderWorkerSets.

The {lws-operator} allows you to manage multi-node AI/ML inference deployments efficiently. {kueue-name} provides scheduling and resource management capabilities for these deployments. You can configure {lws-operator} to leverage these capabilities when running the `LeaderWorkerSet` API for deploying a group of pods as a unit of replication.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/integrating-leader-worker-set.adoc

[id="kueue-installing-lws_{context}"]
= Installing {lws-operator} with {kueue-name}

[role="_abstract"]
You can configure {kueue-name} to work with the {lws-operator}.

.Prerequisites

* You have installed {kueue-name} using the {kueue-op} in the software catalog.
* You have installed {lws-operator} and Operand in the software catalog.
* You have cluster administrator permissions and the `kueue-batch-admin-role` role.
* You have access to the OpenShift Container Platform web console.
* You have installed the {cert-manager-operator} for your cluster.

.Procedure

* Add `LeaderWorkerSet` to the `config.integrations.framework` section of the {kueue-name} cluster object, as shown in the following example:
+
[source,yaml]
----
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  labels:
    app.kubernetes.io/name: kueue-operator
    app.kubernetes.io/managed-by: kustomize
  name: cluster
  namespace: openshift-kueue-operator
spec:
  managementState: Managed
  config:
    integrations:
      frameworks:
      - BatchJob
      - LeaderWorkerSet
----

[role="_additional-resources"]
.Additional resources
* About the {lws-operator}

* LeaderWorkerSet API (Kubernetes documentation)

* Installing the {cert-manager-operator} by using the web console

// Module included in the following assemblies:
//
// * ai_workloads/kueue/integrating-leader-worker-set.adoc

[id="kueue-running-lws_{context}"]
= Running {lws-operator} with {kueue-name}

[role="_abstract"]
You can add and run the {lws-operator} to your existing frameworks.

.Prerequisites

* {kueue-name} using the {kueue-op} is installed.
* {lws-operator} and Operand are installed.
* The {cert-manager-operator} is installed.
* The `namespace` where `LeaderWorkerSet` will be created is labeled using `kueue.openshift.io/managed=true`.
* Ensure that the following objects have been configured:
** `ClusterQueue`
** `ResourceFlavor`
** `LocalQueue`
** `Namespace`

.Procedure

. Create a file named `leaderworkerset.yaml`.
+
.Example of a `LeaderWorkerSet`
[source,yaml]
----
apiVersion: leaderworkerset.x-k8s.io/v1
kind: LeaderWorkerSet
metadata:
  generation: 1
  name: my-lws
  namespace: my-namespace
spec:
  leaderWorkerTemplate:
    leaderTemplate:
      metadata: {}
      spec:
        containers:
        - image: nginxinc/nginx-unprivileged:1.27
          name: leader
          resources: {}
    restartPolicy: RecreateGroupOnPodRestart
    size: 3
    workerTemplate:
      metadata: {}
      spec:
        containers:
        - image: nginxinc/nginx-unprivileged:1.27
          name: worker
          ports:
          - containerPort: 8080
            protocol: TCP
          resources: {}
  networkConfig:
    subdomainPolicy: Shared
  replicas: 2
  rolloutStrategy:
    rollingUpdateConfiguration:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  startupPolicy: LeaderCreated
----

. Specify the target local queue in the `metadata.labels` section of the `LeaderWorkerSet` configuration.
+
[source,yaml]
----
metadata:
  labels:
    kueue.x-k8s.io/queue-name: user-queue
----

. Apply the leader worker set configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f leaderworkerset.yaml
----

[role="_additional-resources"]
.Additional resources
* Configuring a cluster queue

* Configuring a resource flavor

* Configuring a local queue
