---
title: "Pods crash or restart due to lack of memory or CPU"
type: reference
domain: openshift
slug: backup-and-restore-4-22-pods-crash-or-restart-due-to-lack-of-memory-or-cpu
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/pods-crash-or-restart-due-to-lack-of-memory-or-cpu
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Pods crash or restart due to lack of memory or CPU

[id="pods-crash-or-restart-due-to-lack-of-memory-or-cpu"]
= Pods crash or restart due to lack of memory or CPU

[role="_abstract"]
Resolve Velero or Restic pod crashes caused by insufficient memory or CPU by configuring resource requests in the `DataProtectionApplication` custom resource (CR). This helps you allocate adequate CPU and memory resources to prevent pod restarts and ensure stable backup and restore operations.

Ensure that the values for the resource request fields follow the same format as Kubernetes resource requirements.

If you do not specify `configuration.velero.podConfig.resourceAllocations` or `configuration.restic.podConfig.resourceAllocations`, see the following default `resources` specification configuration for a Velero or Restic pod:

[source,yaml]
----
requests:
  cpu: 500m
  memory: 128Mi
----

[role="_additional-resources"]
.Additional resources
* Velero CPU and memory requirements based on collected data

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/pods-crash-or-restart-due-to-lack-of-memory-or-cpu.adoc
//
[id="oadp-pod-crash-resource-request-velero_{context}"]
= Setting resource requests for a Velero pod

[role="_abstract"]
Use the `configuration.velero.podConfig.resourceAllocations` specification field in the `oadp_v1alpha1_dpa.yaml` file to set specific resource requests for a `Velero` pod.

.Procedure

* Set the `cpu` and `memory` resource requests as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
configuration:
  velero:
    podConfig:
      resourceAllocations:
        requests:
          cpu: 200m
          memory: 256Mi
----
+
The `resourceAllocations` listed are for average usage.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/pods-crash-or-restart-due-to-lack-of-memory-or-cpu.adoc
//
[id="oadp-pod-crash-resource-request-retics_{context}"]
= Setting resource requests for a Restic pod

[role="_abstract"]
Use the `configuration.restic.podConfig.resourceAllocations` specification field to set specific resource requests for a `Restic` pod.

.Procedure

* Set the `cpu` and `memory` resource requests as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
configuration:
  restic:
    podConfig:
      resourceAllocations:
        requests:
          cpu: 1000m
          memory: 16Gi
----
+
The `resourceAllocations` listed are for average usage.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/pods-crash-or-restart-due-to-lack-of-memory-or-cpu.adoc
//

[id="setting-resource-requests-for-a-nodeagent-pod_{context}"]
= Setting resource requests for a nodeAgent pod

[role="_abstract"]
Use the `configuration.nodeAgent.podConfig.resourceAllocations` specification field to set specific resource requests for a `nodeAgent` pod.

.Procedure

. Set the `cpu` and `memory` resource requests in the YAML file:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
spec:
  backupLocations:
  - velero:
      default: true
      objectStorage:
        bucket: oadp.....njph
        prefix: velero
      credential:
        key: cloud
        name: cloud-credentials-gcp
      provider: gcp
  configuration:
    velero:
      defaultPlugins:
      - gcp
      - openshift
      - csi
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        resourceAllocations:
          requests:
            cpu: 1000m
            memory: 16Gi
----
+
where:
+
`resourceAllocations`:: The resource allocation examples shown are for average usage.
`memory`:: You can modify this parameter depending on your infrastructure and usage.

. Create the DPA CR by running the following command:
+
[source,terminal]
----
$ oc create -f nodeAgent.yaml
----

.Verification

. Verify that the `nodeAgent` pods are running by using the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                                        READY   STATUS      RESTARTS   AGE
node-agent-hbj9l                                            1/1     Running     0          97s
node-agent-wmwgz                                            1/1     Running     0          95s
node-agent-zvc7k                                            1/1     Running     0          98s
openshift-adp-controller-manager-7f9db86d96-4lhgq           1/1     Running     0          137m
velero-7b6c7fb8d7-ppc8m                                     1/1     Running     0          4m2s
----

. Check the resource requests by describing one of the `nodeAgent` pod:
+
[source,terminal]
----
$ oc describe pod node-agent-hbj9l | grep -C 5 Requests
----
+
.Example output
[source,terminal]
----
      --log-format=text
    State:          Running
      Started:      Mon, 09 Jun 2025 16:22:15 +0530
    Ready:          True
    Restart Count:  0
    Requests:
      cpu:     1
      memory:  1Gi
    Environment:
      NODE_NAME:            (v1:spec.nodeName)
      VELERO_NAMESPACE:    openshift-adp (v1:metadata.namespace)
----
