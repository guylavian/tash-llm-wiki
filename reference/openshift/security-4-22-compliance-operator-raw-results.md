---
title: "Retrieving Compliance Operator raw results"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-raw-results
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-raw-results
version: 4.22
family: security
documentKind: "Documentation"
---

# Retrieving Compliance Operator raw results

[id="compliance-operator-raw-results"]
= Retrieving Compliance Operator raw results

When proving compliance for your OpenShift Container Platform cluster, you might need to provide the scan results for auditing purposes.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-raw-results.adoc

[id="compliance-results_{context}"]
= Obtaining Compliance Operator raw results from a persistent volume

.Procedure

The Compliance Operator generates and stores the raw results in a persistent volume. These results are in Asset Reporting Format (ARF).

. Explore the `ComplianceSuite` object:
+
[source,terminal]
----
$ oc get compliancesuites nist-moderate-modified \
-o json -n openshift-compliance | jq '.status.scanStatuses[].resultsStorage'
----
+
.Example output
[source,json]
----
{
     "name": "ocp4-moderate",
     "namespace": "openshift-compliance"
}
{
     "name": "nist-moderate-modified-master",
     "namespace": "openshift-compliance"
}
{
     "name": "nist-moderate-modified-worker",
     "namespace": "openshift-compliance"
}
----
+
This shows the persistent volume claims where the raw results are accessible.

. Verify the raw data location by using the name and namespace of one of the results:
+
[source,terminal]
----
$ oc get pvc -n openshift-compliance rhcos4-moderate-worker
----
+
.Example output
[source,terminal]
----
NAME                 	STATUS   VOLUME                                 	CAPACITY   ACCESS MODES   STORAGECLASS   AGE
rhcos4-moderate-worker   Bound	pvc-548f6cfe-164b-42fe-ba13-a07cfbc77f3a   1Gi    	RWO        	gp2        	92m
----

. Fetch the raw results by spawning a pod that mounts the volume and copying the results:
+
[source,terminal]
----
$ oc create -n openshift-compliance -f pod.yaml
----
+
.Example pod.yaml
[source,yaml]
----
apiVersion: "v1"
kind: Pod
metadata:
  name: pv-extract
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: pv-extract-pod
      image: registry.access.redhat.com/ubi9/ubi
      command: ["sleep", "3000"]
      volumeMounts:
      - mountPath: "/workers-scan-results"
        name: workers-scan-vol
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  volumes:
    - name: workers-scan-vol
      persistentVolumeClaim:
        claimName: rhcos4-moderate-worker
----

. After the pod is running, download the results:
+
[source,terminal]
----
$ oc cp pv-extract:/workers-scan-results -n openshift-compliance .
----
+
[IMPORTANT]
====
Spawning a pod that mounts the persistent volume will keep the claim as `Bound`. If the volume's storage class in use has permissions set to `ReadWriteOnce`, the volume is only mountable by one pod at a time. You must delete the pod upon completion, or it will not be possible for the Operator to schedule a pod and continue storing results in this location.
====

. After the extraction is complete, the pod can be deleted:
+
[source,terminal]
----
$ oc delete pod pv-extract -n openshift-compliance
----
