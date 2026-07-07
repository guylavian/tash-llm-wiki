---
title: "Managing SELinux profiles"
type: reference
domain: openshift
slug: security-4-22-spo-selinux
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-selinux
version: 4.22
family: security
documentKind: "Documentation"
---

# Managing SELinux profiles

[id="spo-selinux"]
= Managing SELinux profiles

[role="_abstract"]
Create and manage SELinux profiles and bind them to workloads.

[IMPORTANT]
====
The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.
====

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-create-selinux-profile_{context}"]
= Creating SELinux profiles

[role="_abstract"]
Use the `SelinuxProfile` object to create SELinux profiles.

The `SelinuxProfile` object has several features that allow for better security hardening and readability:

* Restricts the profiles to inherit from to the current namespace or a system-wide profile. Because there are typically many profiles installed on the system, but only a subset should be used by cluster workloads, the inheritable system profiles are listed in the `spod` instance in `spec.selinuxOptions.allowedSystemProfiles`.
* Performs basic validation of the permissions, classes and labels.
* Adds a new keyword `@self` that describes the process using the policy. This allows reusing a policy between workloads and namespaces easily, as the usage of the policy is based on the name and namespace.
* Adds features for better security hardening and readability compared to writing a profile directly in the SELinux CIL language.

.Procedure

. Create a project by running the following command:
+
[source,terminal]
----
$ oc new-project nginx-deploy
----

. Create a policy that can be used with a non-privileged workload by creating the following `SelinuxProfile` object:
+
[source,yaml]
----
apiVersion: security-profiles-operator.x-k8s.io/v1alpha2
kind: SelinuxProfile
metadata:
  name: nginx-secure
spec:
  allow:
    '@self':
      tcp_socket:
      - listen
    http_cache_port_t:
      tcp_socket:
      - name_bind
    node_t:
      tcp_socket:
      - node_bind
  inherit:
  - kind: System
    name: container
----

. Wait for `selinuxd` to install the policy by running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=ready selinuxprofile nginx-secure
----
+
.Example output
[source,terminal]
----
selinuxprofile.security-profiles-operator.x-k8s.io/nginx-secure condition met
----
+
The policies are placed into an `emptyDir` in the container owned by the Security Profiles Operator. The policies are saved in Common Intermediate Language (CIL) format in `/etc/selinux.d/<name>_<namespace>.cil`.

. Access the pod by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles rsh -c selinuxd ds/spod
----

.Verification

. View the file contents with `cat` by running the following command:
+
[source,terminal]
----
$ cat /etc/selinux.d/nginx-secure.cil
----
+
.Example output
[source,terminal]
----
(block nginx-secure
(blockinherit container)
(allow process nginx-secure.process ( tcp_socket ( listen )))
(allow process http_cache_port_t ( tcp_socket ( name_bind )))
(allow process node_t ( tcp_socket ( node_bind )))
)
----

. Verify that a policy has been installed by running the following command:
+
[source,terminal]
----
$ semodule -l | grep nginx-secure
----
+
.Example output
[source,terminal]
----
nginx-secure
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-applying-profiles_{context}"]
= Applying {type} profiles to a pod

Create a pod to apply one of the created profiles.

For {type} profiles, the namespace must be labelled to allow privileged workloads.

.Procedure

. Create a pod object that defines a `securityContext`:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: Localhost
      localhostProfile: operator/profile1.json
  containers:
    - name: test-container
      image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
----

. View the profile path of the `seccompProfile.localhostProfile` attribute by running the following command:
+
[source,terminal]
----
$ oc get seccompprofile profile1 --output wide
----
+
.Example output
[source,terminal]
----
NAME       STATUS     AGE   SECCOMPPROFILE.LOCALHOSTPROFILE
profile1   Installed  14s   operator/profile1.json
----

. View the path to the localhost profile by running the following command:
+
[source,terminal]
----
$ oc get sp profile1 --output=jsonpath='{.status.localhostProfile}'
----
+
.Example output
[source,terminal]
----
operator/profile1.json
----

. Apply the `localhostProfile` output to the patch file:
+
[source,yaml]
----
spec:
  template:
    spec:
      securityContext:
        seccompProfile:
          type: Localhost
          localhostProfile: operator/profile1.json
----

. Apply the profile to any other workload, such as a `Deployment` object, by running the following command:
+
[source,terminal]
----
$ oc -n my-namespace patch deployment myapp --patch-file patch.yaml --type=merge
----
+
.Example output
[source,terminal]
----
deployment.apps/myapp patched
----

.Verification

* Confirm the profile was applied correctly by running the following command:
+
[source,terminal]
----
$ oc -n my-namespace get deployment myapp --output=jsonpath='{.spec.template.spec.securityContext}' | jq .
----
+
.Example output
[source,json]
----
{
  "seccompProfile": {
    "localhostProfile": "operator/profile1.json",
    "type": "localhost"
  }
}
----

. Apply the `scc.podSecurityLabelSync=false` label to the `nginx-deploy` namespace by running the following command:
+
[source,terminal]
----
$ oc label ns nginx-deploy security.openshift.io/scc.podSecurityLabelSync=false
----

. Apply the `privileged` label to the `nginx-deploy` namespace by running the following command:
+
[source,terminal]
----
$ oc label ns nginx-deploy --overwrite=true pod-security.kubernetes.io/enforce=privileged
----

. Obtain the SELinux profile usage string by running the following command:
+
[source,terminal]
----
$ oc get selinuxprofile.security-profiles-operator.x-k8s.io/nginx-secure -ojsonpath='{.status.usage}'
----
+
.Example output
[source,terminal]
----
nginx-secure.process
----

. Apply the output string in the workload manifest in the `.spec.containers[].securityContext.seLinuxOptions` attribute:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: nginx-secure
  namespace: nginx-deploy
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - image: nginxinc/nginx-unprivileged:1.21
      name: nginx
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
        seLinuxOptions:
          # NOTE: This uses an appropriate SELinux type
          type: nginx-secure.process
----
+
[IMPORTANT]
====
The SELinux `type` must exist before creating the workload.
====

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-selinux-permissive_{context}"]
= Applying SELinux log policies

To log policy violations or AVC denials, set the `SElinuxProfile` profile to `permissive`.

[IMPORTANT]
====
This procedure defines logging policies. It does not set enforcement policies.
====

.Procedure

* Add `permissive: true` to an `SElinuxProfile`:
+
[source,yaml]
----
apiVersion: security-profiles-operator.x-k8s.io/v1alpha2
kind: SelinuxProfile
metadata:
  name: nginx-secure
spec:
  permissive: true
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-binding-workloads_{context}"]
= Binding workloads to profiles with ProfileBindings

[role="_abstract"]
You can use the `ProfileBinding` resource to bind a security profile to the `SecurityContext` of a container.

.Procedure

. To bind a pod that uses a `quay.io/security-profiles-operator/test-nginx-unprivileged:1.21` image to the example `{kind}` profile, create a `ProfileBinding` object in the same namespace with the pod and the `{kind}` objects:
+
[source,yaml,subs="attributes+"]
----
apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
kind: ProfileBinding
metadata:
  namespace: my-namespace
  name: nginx-binding
spec:
  profileRef:
    kind: {kind}
    name: profile
  image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
----
+
where:

`spec.profileRef.kind`:: Specifies the kind of the profile.
`spec.profileRef.name`:: Specifies the name of the profile.
`spec.image`:: Allows you to enable a default security profile by using a wildcard in the image attribute: `image: "*"`

+
[IMPORTANT]
====
Using the `image: "*"` wildcard attribute binds all new pods with a default security profile in a given namespace.
====

. Label the namespace with `enable-binding=true` by running the following command:
+
[source,terminal]
----
$ oc label ns my-namespace spo.x-k8s.io/enable-binding=true
----

. Define a pod named `test-pod.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  containers:
  - name: test-container
    image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
----

. Create the pod:
+
[source,terminal]
----
$ oc create -f test-pod.yaml
----
+
[NOTE]
====
If the pod already exists, you must re-create the pod for the binding to work properly.
====

.Verification

* Confirm the pod inherits the `ProfileBinding` by running the following command:
+
[source,terminal]
----
$ oc get pod test-pod -o jsonpath='{.spec.containers[*].securityContext.seccompProfile}'
----
+
.Example output
[source,terminal]
----
{"localhostProfile":"operator/profile.json","type":"Localhost"}
----
* Confirm the pod inherits the `ProfileBinding` by running the following command:
+
[source,terminal]
----
$ oc get pod test-pod -o jsonpath='{.spec.containers[*].securityContext.seLinuxOptions.type}'
----
+
.Example output
[source,terminal]
----
profile.process
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-replicating-controllers_{context}"]
= Replicating controllers and SecurityContextConstraints

[role="_abstract"]
You can deploy SELinux policies for replicating controllers, such as deployments or daemon sets.

Note that the `Pod` objects spawned by the controllers are not running with the identity of the user who creates the workload. Unless a `ServiceAccount` is selected, the pods might revert to using a restricted `SecurityContextConstraints` (SCC) which does not allow use of custom security policies.

.Procedure

. Create a project by running the following command:
+
[source,terminal]
----
$ oc new-project nginx-secure
----

. Create the following `RoleBinding` object to allow SELinux policies to be used in the `nginx-secure` namespace:
+
[source,yaml]
----
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: spo-nginx
  namespace: nginx-secure
subjects:
- kind: ServiceAccount
  name: spo-deploy-test
roleRef:
  kind: Role
  name: spo-nginx
  apiGroup: rbac.authorization.k8s.io
----

. Create the `Role` object:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: spo-nginx
  namespace: nginx-secure
rules:
- apiGroups:
  - security.openshift.io
  resources:
  - securitycontextconstraints
  resourceNames:
  - privileged
  verbs:
  - use
----

. Create the `ServiceAccount` object:
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: spo-deploy-test
  namespace: nginx-secure
----

. Create the `Deployment` object:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: selinux-test
  namespace: nginx-secure
  metadata:
    labels:
      app: selinux-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: selinux-test
  template:
    metadata:
      labels:
        app: selinux-test
    spec:
      serviceAccountName: spo-deploy-test
      securityContext:
        seLinuxOptions:
          type: nginx-secure.process
      containers:
      - name: nginx-unpriv
        image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
        ports:
        - containerPort: 8080
----
+
The `spec.template.spec.securityContext.seLinuxOptions.type` must exist before the Deployment is created.
+
[NOTE]
====
The SELinux type is not specified in the workload and is handled by the SCC. When the pods are created by the deployment and the `ReplicaSet`, the pods will run with the appropriate profile.
====
+
Ensure that your SCC is usable by only the correct service account. Refer to _Additional resources_ for more information.

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-recording-profiles_{context}"]
= Recording profiles from workloads

The Security Profiles Operator can record system calls with `ProfileRecording` objects, making it easier to create baseline profiles for applications.

When using the log enricher for recording {type} profiles, verify the log enricher feature is enabled. See _Additional resources_ for more information.

[NOTE]
====
A container with `privileged: true` security context restraints prevents log-based recording. Privileged containers are not subject to {type} policies, and log-based recording makes use of a special {type} profile to record events.
====

.Procedure

. Create a project by running the following command:
+
[source,terminal]
----
$ oc new-project my-namespace
----

. Label the namespace with `enable-recording=true` by running the following command:
+
[source,terminal]
----
$ oc label ns my-namespace spo.x-k8s.io/enable-recording=true
----

. Create a `ProfileRecording` object containing a `recorder: logs` variable:
+
[source,yaml,subs="attributes+"]
----
apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
kind: ProfileRecording
metadata:
  namespace: my-namespace
  name: test-recording
spec:
  kind: {kind}
  recorder: logs
  podSelector:
    matchLabels:
      app: my-app
----

. Create a workload to record:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  namespace: my-namespace
  name: my-pod
  labels:
    app: my-app
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: nginx
      image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
      ports:
        - containerPort: 8080
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
    - name: redis
      image: quay.io/security-profiles-operator/redis:6.2.1
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
----

. Confirm the pod is in a `Running` state by entering the following command:
+
[source,terminal]
----
$ oc -n my-namespace get pods
----
+
.Example output
[source,terminal]
----
NAME     READY   STATUS    RESTARTS   AGE
my-pod   2/2     Running   0          18s
----

. Confirm the enricher indicates that it receives audit logs for those containers:
+
[source,terminal]
----
$ oc -n openshift-security-profiles logs --since=1m --selector name=spod -c log-enricher
----

+
.Example output
[source,terminal]
----
I0523 14:19:08.747313  430694 enricher.go:445] log-enricher "msg"="audit" "container"="redis" "executable"="/usr/local/bin/redis-server" "namespace"="my-namespace" "node"="xiyuan-23-5g2q9-worker-eastus2-6rpgf" "pid"=656802 "pod"="my-pod" "syscallID"=0 "syscallName"="read" "timestamp"="1684851548.745:207179" "type"="seccomp"
----

+
.Example output
[source,terminal,subs="attributes+"]
----
I0517 13:55:36.383187  348295 enricher.go:376] log-enricher "msg"="audit" "container"="redis" "namespace"="my-namespace" "node"="ip-10-0-189-53.us-east-2.compute.internal" "perm"="name_bind" "pod"="my-pod" "profile"="test-recording_redis_6kmrb_1684331729" "scontext"="system_u:system_r:selinuxrecording.process:s0:c4,c27" "tclass"="tcp_socket" "tcontext"="system_u:object_r:redis_port_t:s0" "timestamp"="1684331735.105:273965" "type"="selinux"
----

.Verification

. Remove the pod:
+
[source,terminal]
----
$ oc -n my-namespace delete pod my-pod
----

. Confirm the Security Profiles Operator reconciles the two {type} profiles:

+
[source,terminal]
----
$ oc get seccompprofiles -lspo.x-k8s.io/recording-id=test-recording
----
+
.Example output for seccompprofile
[source,terminal]
----
NAME                   STATUS      AGE
test-recording-nginx   Installed   2m48s
test-recording-redis   Installed   2m48s
----

+
[source,terminal]
----
$ oc get selinuxprofiles -lspo.x-k8s.io/recording-id=test-recording
----
+
.Example output for selinuxprofile
[source,terminal]
----
NAME                   USAGE                                 STATE
test-recording-nginx   test-recording-nginx.process   Installed
test-recording-redis   test-recording-redis.process   Installed
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc
// JKB added conditionalization requested by QE

[id="spo-container-profile-instances_{context}"]
= Merging per-container profile instances

By default, each container instance records into a separate profile. The Security Profiles Operator can merge the per-container profiles into a single profile. Merging profiles is useful when deploying applications using `ReplicaSet` or `Deployment` objects.

.Procedure

. Edit a `ProfileRecording` object to include a `mergeStrategy: containers` variable:
+
[source,yaml,subs="attributes+"]
----
apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
kind: ProfileRecording
metadata:
  # The name of the Recording is the same as the resulting {kind} CRD
  # after reconciliation.
  name: test-recording
  namespace: my-namespace
spec:
  kind: {kind}
  recorder: logs
  mergeStrategy: containers
  podSelector:
    matchLabels:
      app: sp-record
----

. Label the namespace by running the following command:
+
[source,terminal]
----
$ oc label ns my-namespace security.openshift.io/scc.podSecurityLabelSync=false pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged --overwrite=true
----
. Create the workload with the following YAML:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  namespace: my-namespace
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sp-record
  template:
    metadata:
      labels:
        app: sp-record
    spec:
      serviceAccountName: spo-record-sa
      containers:
      - name: nginx-record
        image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
        ports:
        - containerPort: 8080
----

. To record the individual profiles, delete the deployment by running the following command:
+
[source,terminal]
----
$ oc delete deployment nginx-deploy -n my-namespace
----

. To merge the profiles, delete the profile recording by running the following command:
+
[source,terminal]
----
$ oc delete profilerecording test-recording -n my-namespace
----

. To start the merge operation and generate the results profile, run the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {object} -lspo.x-k8s.io/recording-id=test-recording -n my-namespace
----
+
.Example output for {object}
[source,terminal]
----
NAME                          USAGE                            STATE
test-recording-nginx-record   test-recording-nginx-record.process   Installed
----
+
.Example output for {object}
[source,terminal]
----
NAME                          STATUS       AGE
test-recording-nginx-record   Installed    55s
----
. To view the permissions used by any of the containers, run the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {object} test-recording-nginx-record -o yaml
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc

[id="spo-selinux-runasany_{context}"]

= About seLinuxContext: RunAsAny

Recording of SELinux policies is implemented with a webhook that injects a special SELinux type to the pods being recorded. The SELinux type makes the pod run in `permissive` mode, logging all the AVC denials into `audit.log`. By default, a workload is not allowed to run with a custom SELinux policy, but uses an auto-generated type.

To record a workload, the workload must use a service account that has permissions to use an SCC that allows the webhook to inject the permissive SELinux type. The `privileged` SCC contains `seLinuxContext: RunAsAny`.

In addition, the namespace must be labeled with `pod-security.kubernetes.io/enforce: privileged` if your cluster enables the Pod Security Admission because only the `privileged` Pod Security Standard allows using a custom SELinux policy.

[role="_additional-resources"]
[id="additional-resources_spo-selinux"]
== Additional resources

* Managing security context constraints
* Managing SCCs in OpenShift
* Using the log enricher
* About security profiles
