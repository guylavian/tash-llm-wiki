---
title: "Using remote health reporting in a restricted network"
type: reference
domain: openshift
slug: support-4-22-remote-health-reporting-from-restricted-network
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/remote-health-reporting-from-restricted-network
version: 4.22
family: support
documentKind: "Documentation"
---

# Using remote health reporting in a restricted network

[id="remote-health-reporting-from-restricted-network"]
= Using remote health reporting in a restricted network

[role="_abstract"]
You can manually gather and upload {insights-operator} archives to diagnose issues from a restricted network.

To use the {insights-operator} in a restricted network, you must:

* Create a copy of your {insights-operator} archive.
* Upload the {insights-operator} archive to console.redhat.com.

Additionally, you can select to obfuscate the {insights-operator} data before upload.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting-from-restricted-network.adoc

[id="insights-operator-one-time-gather_{context}"]
= Running an {insights-operator} gather operation

[role="_abstract"]
You must run a gather operation to create an {insights-operator} archive.

.Prerequisites

* You are logged in to OpenShift Container Platform as `cluster-admin`.

.Procedure

. Create a file named `gather-job.yaml` using this template:
+
[source,yaml]
----

----
. Copy your `insights-operator` image version:
+
[source,terminal]
----
$ oc get -n openshift-insights deployment insights-operator -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: insights-operator
  namespace: openshift-insights
# ...
spec:
  template:
# ...
    spec:
      containers:
      - args:
# ...
        image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
# ...
----
+
The `spec.template.spec.containers.image` field specifies your `insights-operator` image version.

. Paste your image version in `gather-job.yaml`:
+
[source,yaml,subs="+quotes"]
----
apiVersion: batch/v1
kind: Job
metadata:
  name: insights-operator-job
# ...
spec:
# ...
  template:
    spec:
    initContainers:
    - name: insights-operator
      image: image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
      terminationMessagePolicy: FallbackToLogsOnError
      volumeMounts:
----
+
where::
`spec.template.initContainers.image`:: Replace any existing value with your `insights-operator` image version.

. Create the gather job:
+
[source,terminal]
----
$ oc apply -n openshift-insights -f gather-job.yaml
----
. Find the name of the job pod:
+
[source,terminal]
----
$ oc describe -n openshift-insights job/insights-operator-job
----
+
.Example output
[source,terminal,subs="+quotes"]
----
Name:             insights-operator-job
Namespace:        openshift-insights
# ...
Events:
  Type    Reason            Age    From            Message
  ----    ------            ----   ----            -------
  Normal  SuccessfulCreate  7m18s  job-controller  Created pod: insights-operator-job-<your_job>
----
+
where:: `insights-operator-job-<your_job>` is the name of the pod.

. Verify that the operation has finished:
+
[source,terminal,subs="+quotes"]
----
$ oc logs -n openshift-insights insights-operator-job-<your_job> insights-operator
----
+
.Example output
[source,terminal]
----
I0407 11:55:38.192084       1 diskrecorder.go:34] Wrote 108 records to disk in 33ms
----
. Save the created archive:
+
[source,terminal,subs="+quotes"]
----
$ oc cp openshift-insights/insights-operator-job-_<your_job>_:/var/lib/insights-operator ./insights-data
----
. Clean up the job:
+
[source,terminal]
----
$ oc delete -n openshift-insights job insights-operator-job
----

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting-from-restricted-network.adoc

[id="insights-operator-manual-upload_{context}"]
= Uploading an {insights-operator} archive

[role="_abstract"]
You can manually upload an {insights-operator} archive to console.redhat.com to diagnose potential issues.

.Prerequisites

* You are logged in to OpenShift Container Platform as `cluster-admin`.
* You have a workstation with unrestricted internet access.
* You have created a copy of the {insights-operator} archive.

.Procedure

. Download the `dockerconfig.json` file:
+
[source,terminal]
----
$ oc extract secret/pull-secret -n openshift-config --to=.
----
. Copy your `"cloud.openshift.com"` `"auth"` token from the `dockerconfig.json` file:
+
[source,json,subs="+quotes"]
----
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "_<your_token>_",
      "email": "asd@redhat.com"
    }
}
----

. Upload the archive to console.redhat.com:
+
[source,terminal,subs="+quotes"]
----
$ curl -v -H "User-Agent: insights-operator/one10time200gather184a34f6a168926d93c330 cluster/_<cluster_id>_" -H "Authorization: Bearer _<your_token>_" -F "upload=@_<path_to_archive>_; type=application/vnd.redhat.openshift.periodic+tar" https://console.redhat.com/api/ingress/v1/upload
----
where `_<cluster_id>_` is your cluster ID, `_<your_token>_` is the token from your pull secret, and `_<path_to_archive>_` is the path to the {insights-operator} archive.
+
If the operation is successful, the command returns a `"request_id"` and `"account_number"`:
+
.Example output
[source,terminal]
----
* Connection #0 to host console.redhat.com left intact
{"request_id":"393a7cf1093e434ea8dd4ab3eb28884c","upload":{"account_number":"6274079"}}%
----

.Verification
. Log in to .

. Click the *Cluster List* menu in the left pane.

. To display the details of the cluster, click the cluster name.

. Open the *{red-hat-lightspeed} Advisor* tab of the cluster.
+
If the upload was successful, the tab displays one of the following:
+
* *Your cluster passed all recommendations*, if the {red-hat-lightspeed} advisor service did not identify any issues.

* A list of issues that the {red-hat-lightspeed} advisor service has detected, prioritized by risk (low, moderate, important, and critical).

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting-from-restricted-network.adoc

[id="insights-operator-enable-obfuscation_{context}"]
= Enabling {insights-operator} data obfuscation

[role="_abstract"]
You can enable obfuscation to mask sensitive and identifiable IPv4 addresses and cluster base domains that the {insights-operator} sends to console.redhat.com.

[WARNING]
====
Although this feature is available, Red Hat recommends keeping obfuscation disabled for a more effective support experience.
====

Obfuscation assigns non-identifying values to cluster IPv4 addresses, and uses a translation table that is retained in memory to change IP addresses to their obfuscated versions throughout the {insights-operator} archive before uploading the data to console.redhat.com.

For cluster base domains, obfuscation changes the base domain to a hardcoded substring. For example, `cluster-api.openshift.example.com` becomes `cluster-api.<CLUSTER_BASE_DOMAIN>`.

The following procedure enables obfuscation using the `support` secret in the `openshift-config` namespace.

.Prerequisites

* You are logged in to the OpenShift Container Platform web console as `cluster-admin`.

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. Select the *openshift-config* project.
. Search for the *support* secret using the *Search by name* field. If it does not exist, click *Create* -> *Key/value secret* to create it.
. Click the Options menu {kebab}, and then click *Edit Secret*.
. Click *Add Key/Value*.
. Create a key named `enableGlobalObfuscation` with a value of `true`, and click *Save*.
. Navigate to *Workloads* -> *Pods*
. Select the `openshift-insights` project.
. Find the `insights-operator` pod.
. To restart the `insights-operator` pod, click the Options menu {kebab}, and then click *Delete Pod*.

.Verification

. Navigate to *Workloads* -> *Secrets*.
. Select the *openshift-insights* project.
. Search for the *obfuscation-translation-table* secret using the *Search by name* field.

If the `obfuscation-translation-table` secret exists, then obfuscation is enabled and working.

Alternatively, you can inspect `/insights-operator/gathers.json` in your {insights-operator} archive for the value `"is_global_obfuscation_enabled": true`.

[role="_additional-resources"]
.Additional resources

* Showing data collected by the {insights-operator}
