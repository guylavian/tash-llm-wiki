---
title: "Managing seccomp profiles"
type: reference
domain: openshift
slug: security-4-22-spo-seccomp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-seccomp
version: 4.22
family: security
documentKind: "Documentation"
---

# Managing seccomp profiles

[id="spo-seccomp"]
= Managing seccomp profiles

[role="_abstract"]
Create and manage seccomp profiles and bind them to workloads.

[IMPORTANT]
====
The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.
====

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc

[id="spo-create-seccomp-profile_{context}"]
= Creating seccomp profiles

[role="_abstract"]
Use the `SeccompProfile` object to create seccomp profiles.

`SeccompProfile` objects can restrict syscalls within a container, limiting the access of your application.

.Procedure

. Create a project by running the following command:
+
[source,terminal]
----
$ oc new-project my-namespace
----

. Create the `SeccompProfile` object:
+
[source,yaml]
----
apiVersion: security-profiles-operator.x-k8s.io/v1beta1
kind: SeccompProfile
metadata:
  name: profile1
spec:
  defaultAction: SCMP_ACT_LOG
----
+
The seccomp profile will be saved in `/var/lib/kubelet/seccomp/operator/<namespace>/<name>.json`.
+
An `init` container creates the root directory of the Security Profiles Operator to run the Operator without `root` group or user ID privileges. A symbolic link is created from the rootless profile storage `/var/lib/openshift-security-profiles` to the default `seccomp` root path inside of the kubelet root `/var/lib/kubelet/seccomp/operator`.

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

[role="_additional-resources"]
[id="additional-resources_spo-seccomp"]
== Additional resources

* Managing security context constraints
* Managing SCCs in OpenShift
* Using the log enricher
* About security profiles
