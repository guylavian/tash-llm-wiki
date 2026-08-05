---
title: "Overriding the active deadline for run-once pods"
type: reference
domain: openshift
slug: nodes-4-22-run-once-duration-override-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/run-once-duration-override-install
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Overriding the active deadline for run-once pods

[id="run-once-duration-override-install"]
= Overriding the active deadline for run-once pods

[role="_abstract"]
You can use the {run-once-operator} to specify a maximum time limit that run-once pods can be active for. By enabling the run-once duration override on a namespace, all future run-once pods created or updated in that namespace have their `activeDeadlineSeconds` field set to the value specified by the {run-once-operator}.

[NOTE]
====
If both the run-once pod and the {run-once-operator} have their `activeDeadlineSeconds` value set, the lower of the two values is used.
====

// Installing the {run-once-operator}
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-install.adoc

[id="rodoo-install-operator_{context}"]
= Installing the {run-once-operator}

You can use the web console to install the {run-once-operator}.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Create the required namespace for the {run-once-operator}.
.. Navigate to *Administration* -> *Namespaces* and click *Create Namespace*.
.. Enter `openshift-run-once-duration-override-operator` in the *Name* field and click *Create*.

. Install the {run-once-operator}.
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. Enter *{run-once-operator}* into the filter box.
.. Select the *{run-once-operator}* and click *Install*.
.. On the *Install Operator* page:
... The *Update channel* is set to *stable*, which installs the latest stable release of the {run-once-operator}.
... Select *A specific namespace on the cluster*.
... Choose *openshift-run-once-duration-override-operator* from the dropdown menu under *Installed namespace*.
... Select an *Update approval* strategy.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.
... Click *Install*.

. Create a `RunOnceDurationOverride` instance.
.. From the *Ecosystem* -> *Installed Operators* page, click *{run-once-operator}*.
.. Select the *Run Once Duration Override* tab and click *Create RunOnceDurationOverride*.
.. Edit the settings as necessary.
+
Under the `runOnceDurationOverride` section, you can update the `spec.activeDeadlineSeconds` value, if required. The predefined value is `3600` seconds, or 1 hour.

.. Click *Create*.

.Verification

. Log in to the OpenShift CLI.

. Verify all pods are created and running properly.
+
[source,terminal]
----
$ oc get pods -n openshift-run-once-duration-override-operator
----
+
.Example output
[source,terminal]
----
NAME                                                   READY   STATUS    RESTARTS   AGE
run-once-duration-override-operator-7b88c676f6-lcxgc   1/1     Running   0          7m46s
runoncedurationoverride-62blp                          1/1     Running   0          41s
runoncedurationoverride-h8h8b                          1/1     Running   0          41s
runoncedurationoverride-tdsqk                          1/1     Running   0          41s
----

// Enabling the run-once duration override on a namespace
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-install.adoc

[id="rodoo-enable-override_{context}"]
= Enabling the run-once duration override on a namespace

To apply the run-once duration override from the {run-once-operator} to run-once pods, you must enable it on each applicable namespace.

.Prerequisites

* The {run-once-operator} is installed.

.Procedure

. Log in to the OpenShift CLI.

. Add the label to enable the run-once duration override to your namespace:
+
[source,terminal]
----
$ oc label namespace <namespace> \ <1>
    runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true
----
<1> Specify the namespace to enable the run-once duration override on.

After you enable the run-once duration override on this namespace, future run-once pods that are created in this namespace will have their `activeDeadlineSeconds` field set to the override value from the {run-once-operator}. Existing pods in this namespace will also have their `activeDeadlineSeconds` value set when they are updated next.

.Verification

. Create a test run-once pod in the namespace that you enabled the run-once duration override on:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: example
  namespace: <namespace>                 <1>
spec:
  restartPolicy: Never                   <2>
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: busybox
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
      image: busybox:1.25
      command:
        - /bin/sh
        - -ec
        - |
          while sleep 5; do date; done
----
<1> Replace `<namespace>` with the name of your namespace.
<2> The `restartPolicy` must be `Never` or `OnFailure` to be a run-once pod.

. Verify that the pod has its `activeDeadlineSeconds` field set:
+
[source,terminal]
----
$ oc get pods -n <namespace> -o yaml | grep activeDeadlineSeconds
----
+
.Example output
[source,terminal]
----
    activeDeadlineSeconds: 3600
----

// Updating the run-once active deadline override value
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-install.adoc

[id="rodoo-update-active-deadline-seconds_{context}"]
= Updating the run-once active deadline override value

You can customize the override value that the {run-once-operator} applies to run-once pods. The predefined value is `3600` seconds, or 1 hour.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed the {run-once-operator}.

.Procedure

. Log in to the OpenShift CLI.

. Edit the `RunOnceDurationOverride` resource:
+
[source,terminal]
----
$ oc edit runoncedurationoverride cluster
----

. Update the `activeDeadlineSeconds` field:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: RunOnceDurationOverride
metadata:
# ...
spec:
  runOnceDurationOverride:
    spec:
      activeDeadlineSeconds: 1800 <1>
# ...
----
<1> Set the `activeDeadlineSeconds` field to the desired value, in seconds.

. Save the file to apply the changes.

Any future run-once pods created in namespaces where the run-once duration override is enabled will have their `activeDeadlineSeconds` field set to this new value. Existing run-once pods in these namespaces will receive this new value when they are updated.
