---
title: "Using pods in a privileged security context"
type: reference
domain: openshift
slug: cicd-4-22-using-pods-in-a-privileged-security-context
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/using-pods-in-a-privileged-security-context
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Using pods in a privileged security context

[id="using-pods-in-a-privileged-security-context"]
= Using pods in a privileged security context

The default configuration of {pipelines-shortname} 1.3.x and later versions does not allow you to run pods with privileged security context, if the pods result from pipeline run or task run.
For such pods, the default service account is `pipeline`, and the security context constraint (SCC) associated with the `pipeline` service account is `pipelines-scc`. The `pipelines-scc` SCC is similar to the `anyuid` SCC, but with minor differences as defined in the YAML file for the SCC of pipelines:

.Example `pipelines-scc.yaml` snippet
[source,yaml,subs="attributes+"]
----
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
...
allowedCapabilities:
  - SETFCAP
...
fsGroup:
  type: MustRunAs
...
----

In addition, the `Buildah` cluster task, shipped as part of the {pipelines-shortname}, uses `vfs` as the default storage driver.

[id='op-running-pipeline-and-task-run-pods-with-privileged-security-context']
= Running pipeline run and task run pods with privileged security context

.Procedure

To run a pod (resulting from pipeline run or task run) with the `privileged` security context, do the following modifications:

* Configure the associated user account or service account to have an explicit SCC. You can perform the configuration using any of the following methods:
** Run the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user <scc-name> -z <service-account-name>
----
** Alternatively, modify the YAML files for `RoleBinding`, and `Role` or `ClusterRole`:

+
.Example `RoleBinding` object
[source,yaml,subs="attributes+"]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: service-account-name <1>
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: pipelines-scc-clusterrole <2>
subjects:
- kind: ServiceAccount
  name: pipeline
  namespace: default
----
<1> Substitute with an appropriate service account name.
<2> Substitute with an appropriate cluster role based on the role binding you use.

+
.Example `ClusterRole` object
[source,yaml,subs="attributes+"]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines-scc-clusterrole <1>
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - nonroot
  resources:
  - securitycontextconstraints
  verbs:
  - use
----
<1> Substitute with an appropriate cluster role based on the role binding you use.

+
[NOTE]
====
As a best practice, create a copy of the default YAML files and make changes in the duplicate file.
====
+

* If you do not use the `vfs` storage driver, configure the service account associated with the task run or the pipeline run to have a privileged SCC, and set the security context as `privileged: true`.

[id="op-running-pipeline-run-and-task-run-with-custom-scc-and-service-account_{context}"]
= Running pipeline run and task run by using a custom SCC and a custom service account

When using the `pipelines-scc` security context constraint (SCC) associated with the default `pipelines` service account, the pipeline run and task run pods may face timeouts. This happens because in the default `pipelines-scc` SCC, the `fsGroup.type` parameter is set to `MustRunAs`.

[NOTE]
====
For more information about pod timeouts, see BZ#1995779.
====

To avoid pod timeouts, you can create a custom SCC with the `fsGroup.type` parameter set to `RunAsAny`, and associate it with a custom service account.

[NOTE]
====
As a best practice, use a custom SCC and a custom service account for pipeline runs and task runs. This approach allows greater flexibility and does not break the runs when the defaults are modified during an upgrade.
====

.Procedure

. Define a custom SCC with the `fsGroup.type` parameter set to `RunAsAny`:
+
.Example: Custom SCC
[source,yaml]
----
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  annotations:
    kubernetes.io/description: my-scc is a close replica of anyuid scc. pipelines-scc has fsGroup - RunAsAny.
  name: my-scc
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: true
allowPrivilegedContainer: false
allowedCapabilities: null
defaultAddCapabilities: null
fsGroup:
  type: RunAsAny
groups:
- system:cluster-admins
priority: 10
readOnlyRootFilesystem: false
requiredDropCapabilities:
- MKNOD
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: MustRunAs
supplementalGroups:
  type: RunAsAny
volumes:
- configMap
- downwardAPI
- emptyDir
- persistentVolumeClaim
- projected
- secret
----

. Create the custom SCC:
+
.Example: Create the `my-scc` SCC
[source,terminal]
----
$ oc create -f my-scc.yaml
----

. Create a custom service account:
+
.Example: Create a `fsgroup-runasany` service account
[source,terminal]
----
$ oc create serviceaccount fsgroup-runasany
----

. Associate the custom SCC with the custom service account:
+
.Example: Associate the `my-scc` SCC with the `fsgroup-runasany` service account
[source,terminal]
----
$ oc adm policy add-scc-to-user my-scc -z fsgroup-runasany
----
+
If you want to use the custom service account for privileged tasks, you can associate the `privileged` SCC with the custom service account by running the following command:
+
.Example: Associate the `privileged` SCC with the `fsgroup-runasany` service account
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z fsgroup-runasany
----

. Use the custom service account in the pipeline run and task run:
+
.Example: Pipeline run YAML with `fsgroup-runasany` custom service account
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: <pipeline-run-name>
spec:
  pipelineRef:
    name: <pipeline-cluster-task-name>
  serviceAccountName: 'fsgroup-runasany'
----
+
.Example: Task run YAML with `fsgroup-runasany` custom service account
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: <task-run-name>
spec:
  taskRef:
    name: <cluster-task-name>
  serviceAccountName: 'fsgroup-runasany'
----

[role="_additional-resources"]
[id="additional-references_using-pods-in-a-privileged-security-context"]
== Additional resources

* For information on managing SCCs, refer to Managing security context constraints.
