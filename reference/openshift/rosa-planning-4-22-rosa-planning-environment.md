---
title: "Planning resource usage in your cluster"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-planning-environment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-planning-environment
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Planning resource usage in your cluster

[id="rosa-planning-environment"]
= Planning resource usage in your cluster

[role="_abstract"]
Plan your OpenShift Container Platform environment by reviewing the tested cluster maximums. Adhering to these supported limits ensures that your deployment is reliable and optimized for scale.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-planning-environment.adoc

[id="planning-environment-cluster-maximums_{context}"]
= Planning your environment based on tested cluster maximums

[role="_abstract"]
You can use tested cluster maximums when you size OpenShift Container Platform clusters and namespaces. These values are not hard limits or Red{nbsp}Hat supported ceilings for production.

The following tables summarize the latest published tested maximums for your architecture.

[NOTE]
====
These numbers come from internal Red{nbsp}Hat tests on the latest OpenShift Container Platform clusters using default cluster tunings. Reaching or exceeding a number does not mean the cluster fails or degrade immediately.

Each value reflects limits for individual OpenShift resources measured with separate workloads that target a few resource types at a time. The workloads do not reproduce every production load, but they target patterns that stay close to common customer use cases. Tests used the Cloud Native Computing Foundation (CNCF) workload orchestrator. For more information, see the project page for this orchestrator.
====
// Module included in the following assemblies:
//
// * rosa_planning/rosa-planning-environment.adoc

[id="planning-environment-tested-maximums-classic_{context}"]
= Tested cluster maximums for OpenShift Container Platform

[role="_abstract"]
These tested maximums apply to OpenShift Container Platform clusters. Use the table to plan worker nodes, namespaces, pods, and related objects within validated scale ranges.

[options="header",cols="2,1"]
|===
|Maximum type |OpenShift Container Platform tested maximum

|Number of compute (worker) nodes
|249

|Number of pods
|60,000

|Number of pods per node
|250

|Number of deployments
|11,200

|Number of namespaces
|2,250

|Number of routes
|4,500

|Number of secrets
|29,000

|Number of config maps
|34,000

|Number of services
|22,000

|Number of pods per namespace
|2,000

|Number of services per namespace
|1,000

|Number of deployments per namespace
|2,000
|===
// Module included in the following assemblies:
//
// * rosa_planning/rosa-planning-environment.adoc

[id="planning-environment-cluster-maximums-considerations_{context}"]
= Considerations for cluster maximum tests

[role="_abstract"]
These tests measure individual OpenShift resource limits with dedicated workloads. The following considerations describe factors that can change the limits you observe in production compared with the published tested maximums.

* *Idle pod baselines:* Metrics include `pause` pods and default cluster control plane pods on control plane nodes. Results use the `node-density` workload and change with active application load.
* *Resource and I/O limitations:* Observed limits depend on workload intensity. For example, high-density I/O workloads or hitting the PVC-per-node ceiling can reduce the maximum stable pod count.
* *Namespace composition:* Tests include default cluster Operator namespaces. Each test namespace has idle pods, config maps, and secrets to model routine operational load.
* *Service scalability:* Data reflects tested `ClusterIP` services with a single endpoint using the `cni-density` workload. Other service types can scale differently.
* *Infrastructure and routing:* The test environment used two routers with default settings on dedicated OpenShift Container Platform infrastructure nodes. Limits used the `cluster-density` workload.
// Module included in the following assemblies:
//
// * rosa_planning/rosa-planning-environment.adoc

[id="planning-environment-tested-maximums-hcp_{context}"]
= Tested cluster maximums for OpenShift Container Platform

[role="_abstract"]
These tested maximums apply to OpenShift Container Platform clusters. Use the table to plan worker nodes, namespaces, pods, and related objects within validated scale ranges.

[options="header",cols="2,1"]
|===
|Maximum type |OpenShift Container Platform tested maximum

|Number of compute (worker) nodes
|501

|Number of pods
|105,205

|Number of pods per node
|250

|Number of deployments
|22,600

|Number of namespaces
|4,500

|Number of routes
|9,000

|Number of secrets
|59,000

|Number of config maps
|68,000

|Number of services
|38,000

|Number of pods per namespace
|2,000

|Number of services per namespace
|1,000

|Number of deployments per namespace
|2,000
|===

// Module included in the following assemblies:
//
// * rosa_planning/rosa-planning-environment.adoc

[id="planning-environment-application-requirements_{context}"]
= Planning your environment based on application requirements

[role="_abstract"]
This document describes how to plan your OpenShift Container Platform environment based on your application requirements.

Consider an example application environment:

[options="header",cols="5"]
|===
|Pod type |Pod quantity |Max memory |CPU cores |Persistent storage

|apache
|100
|500 MB
|0.5
|1 GB

|node.js
|200
|1 GB
|1
|1 GB

|postgresql
|100
|1 GB
|2
|10 GB

|JBoss EAP
|100
|1 GB
|1
|1 GB
|===

Extrapolated requirements: 550 CPU cores, 450 GB RAM, and 1.4 TB storage.

Instance size for nodes can be modulated up or down, depending on your preference. Nodes are often resource overcommitted. In this deployment scenario, you can choose to run additional smaller nodes or fewer larger nodes to provide the same amount of resources. Factors such as operational agility and cost-per-instance should be considered.

[options="header",cols="4"]
|===
|Node type |Quantity |CPUs |RAM (GB)

|Nodes (option 1)
|100
|4
|16

|Nodes (option 2)
|50
|8
|32

|Nodes (option 3)
|25
|16
|64
|===

Some applications lend themselves well to overcommitted environments, and some do not. Most Java applications and applications that use huge pages are examples of applications that would not allow for overcommitment. That memory cannot be used for other applications. In the example above, the environment would be roughly 30 percent overcommitted, a common ratio.

The application pods can access a service either by using environment variables or DNS. If using environment variables, for each active service the variables are injected by the kubelet when a pod is run on a node. A cluster-aware DNS server watches the Kubernetes API for new services and creates a set of DNS records for each one. If DNS is enabled throughout your cluster, then all pods should automatically be able to resolve services by their DNS name. Service discovery using DNS can be used in case you must go beyond 5000 services. When using environment variables for service discovery, if the argument list exceeds the allowed length after 5000 services in a namespace, then the pods and deployments will start failing.

Disable the service links in the deployment's service specification file to overcome this. Consider the following example:

[source,yaml]
----
Kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: deploymentConfigTemplate
  creationTimestamp:
  annotations:
    description: This template will create a deploymentConfig with 1 replica, 4 env vars and a service.
    tags: ''
objects:
  - kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: deploymentconfig${IDENTIFIER}
    spec:
      template:
        metadata:
          labels:
            name: replicationcontroller${IDENTIFIER}
        spec:
          enableServiceLinks: false
          containers:
          - name: pause${IDENTIFIER}
            image: "${IMAGE}"
            ports:
            - containerPort: 8080
              protocol: TCP
            env:
            - name: ENVVAR1_${IDENTIFIER}
              value: "${ENV_VALUE}"
            - name: ENVVAR2_${IDENTIFIER}
              value: "${ENV_VALUE}"
            - name: ENVVAR3_${IDENTIFIER}
              value: "${ENV_VALUE}"
            - name: ENVVAR4_${IDENTIFIER}
              value: "${ENV_VALUE}"
            resources: {}
            imagePullPolicy: IfNotPresent
            capabilities: {}
            securityContext:
              capabilities: {}
              privileged: false
          restartPolicy: Always
          serviceAccount: ''
      replicas: 1
      selector:
        name: replicationcontroller${IDENTIFIER}
      triggers:
      - type: ConfigChange
      strategy:
        type: Rolling
  - kind: Service
    apiVersion: v1
    metadata:
      name: service${IDENTIFIER}
    spec:
      selector:
        name: replicationcontroller${IDENTIFIER}
      ports:
      - name: serviceport${IDENTIFIER}
        protocol: TCP
        port: 80
        targetPort: 8080
      portalIP: ''
      type: ClusterIP
      sessionAffinity: None
    status:
      loadBalancer: {}
  parameters:
  - name: IDENTIFIER
    description: Number to append to the name of resources
    value: '1'
    required: true
  - name: IMAGE
    description: Image to use for deploymentConfig
    value: gcr.io/google-containers/pause-amd64:3.0
    required: false
  - name: ENV_VALUE
    description: Value to use for environment variables
    generate: expression
    from: "[A-Za-z0-9]{255}"
    required: false
  labels:
template: deploymentConfigTemplate
----

The number of application pods that can run in a namespace is dependent on the number of services and the length of the service name when the environment variables are used for service discovery. `ARG_MAX` on the system defines the maximum argument length for a new process and it is set to 2097152 bytes (2 MiB) by default. The kubelet injects environment variables in to each pod scheduled to run in the namespace including:

* `<SERVICE_NAME>_SERVICE_HOST=<IP>`
* `<SERVICE_NAME>_SERVICE_PORT=<PORT>`
* `<SERVICE_NAME>_PORT=tcp://<IP>:<PORT>`
* `<SERVICE_NAME>_PORT_<PORT>_TCP=tcp://<IP>:<PORT>`
* `<SERVICE_NAME>_PORT_<PORT>_TCP_PROTO=tcp`
* `<SERVICE_NAME>_PORT_<PORT>_TCP_PORT=<PORT>`
* `<SERVICE_NAME>_PORT_<PORT>_TCP_ADDR=<ADDR>`

The pods in the namespace start to fail if the argument length exceeds the allowed value and if the number of characters in a service name impacts it.
