---
title: "Integrating the {js-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-integrating-jobset
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/integrating-jobset
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Integrating the {js-operator}

[id="integrating-jobset"]
= Integrating the {js-operator}

[role="_abstract"]
You can integrate {js-operator} with {kueue-name} so you can leverage the scheduling and resource management functionality provided by {kueue-name} when running the {js-operator}.

You can use the {js-operator} to manage and run large-scale, coordinated workloads like high-performance computing (HPC) and AI training.

The {js-operator} models a distributed batch workload as a group of Kubernetes Jobs. This allows you to easily specify different pod templates for different distinct groups of pods, for example, a leader, workers, parameter servers, and so on.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/integrating-jobset.adoc

[id="kueue-installing-jobset_{context}"]
= Installing {js-operator} with {kueue-name}

[role="_abstract"]
You can configure {kueue-name} to work with the {js-operator}.

.Prerequisites

* You have installed {kueue-name} using the {kueue-op} in the software catalog.
* You have installed {js-operator} in the software catalog.
* You have cluster administrator permissions and the `kueue-batch-admin-role` role.
* You have access to the OpenShift Container Platform web console.
* You have installed the {cert-manager-operator} for your cluster.

.Procedure

* Add `JobSet` to the `config.integrations.frameworks` section of the {kueue-name}
cluster object, as shown in the following example:
+
[source,yaml]
----
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  name: cluster
  namespace: openshift-kueue-operator
spec:
  managementState: Managed
  config:
    integrations:
      frameworks:
      - JobSet
----
[role="_additional-resources"]
.Additional resources
* About the {js-operator}

* Run A JobSet (Kubernetes documentation)

* Installing the {cert-manager-operator} by using the web console

// Module included in the following assemblies:
//
// * ai_workloads/kueue/integrating-jobset.adoc

[id="kueue-running-jobset_{context}"]
= Running {js-operator} with {kueue-name}

[role="_abstract"]
You can add and run {js-operator} to your existing frameworks.

.Prerequisites

* {kueue-name} using the {kueue-op} is installed.
* {js-operator} is installed.
* The {cert-manager-operator} is installed.
* The `namespace` where `JobSet` will be created is labeled using `kueue.openshift.io/managed=true`.
* Ensure that the following objects have been configured:
** `ClusterQueue`
** `ResourceFlavor`
** `LocalQueue`
** `Namespace`

.Procedure

. Create a file named `jobset.yaml`.
+
.Example of a `JobSet`
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: jobset
  namespace: my-namespace
spec:
  replicatedJobs:
    - name: workers
      replicas: 1
      template:
        spec:
          parallelism: 3
          completions: 3
          backoffLimit: 1
          template:
            spec:
              containers:
                - name: sleep
                  image: busybox
                  resources:
                    requests:
                      cpu: 200m
                      memory: "200Mi"
                  command:
                    - sleep
                  args:
                    - 220s
    - name: driver
      template:
        spec:
          parallelism: 1
          completions: 1
          backoffLimit: 0
          template:
            spec:
              containers:
                - name: sleep
                  image: busybox
                  resources:
                    requests:
                      cpu: 200m
                      memory: "200Mi"
                  command:
                    - sleep
                  args:
                    - 220s
----

. Specify the target local queue in the `metadata.labels` section of the `JobSet` configuration.
+
[source,yaml]
----
metadata:
  labels:
    kueue.x-k8s.io/queue-name: <local-queue-name>
----

. Apply the JobSet configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f jobset.yaml
----

[role="_additional-resources"]
.Additional resources
* Configuring a cluster queue

* Configuring a resource flavor

* Configuring a local queue
