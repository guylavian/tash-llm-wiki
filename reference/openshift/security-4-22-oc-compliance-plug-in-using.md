---
title: "Using the oc-compliance plugin"
type: reference
domain: openshift
slug: security-4-22-oc-compliance-plug-in-using
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/oc-compliance-plug-in-using
version: 4.22
family: security
documentKind: "Documentation"
---

# Using the oc-compliance plugin

[id="using-oc-compliance-plug-in"]
= Using the oc-compliance plugin

Although the Compliance Operator automates many of the checks and remediations for the cluster, the full process of bringing a cluster into compliance often requires administrator interaction with the Compliance Operator API and other components. The `oc-compliance` plugin makes the process easier.

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="installing-oc-compliance_{context}"]
= Installing the oc-compliance plugin

.Procedure

. Extract the `oc-compliance` image to get the `oc-compliance` binary:
+
[source,terminal]
----
$ podman run --rm -v ~/.local/bin:/mnt/out:Z registry.redhat.io/compliance/oc-compliance-rhel8:stable /bin/cp /usr/bin/oc-compliance /mnt/out/
----
+
.Example output
+
[source,terminal]
----
W0611 20:35:46.486903   11354 manifest.go:440] Chose linux/amd64 manifest from the manifest list.
----
+
You can now run `oc-compliance`.

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="fetching-raw-results_{context}"]
= Fetching raw results

When a compliance scan finishes, the results of the individual checks are listed in the resulting `ComplianceCheckResult` custom resource (CR). However, an administrator or auditor might require the complete details of the scan. The OpenSCAP tool creates an Advanced Recording Format (ARF) formatted file with the detailed results. This ARF file is too large to store in a config map or other standard Kubernetes resource, so a persistent volume (PV) is created to contain it.

.Procedure

* Fetching the results from the PV with the Compliance Operator is a four-step process. However, with the `oc-compliance` plugin, you can use a single command:
+
[source,terminal]
----
$ oc compliance fetch-raw <object-type> <object-name> -o <output-path>
----
+
* `<object-type>` can be either `scansettingbinding`, `compliancescan` or `compliancesuite`, depending on which of these objects the scans were launched with.
* `<object-name>` is the name of the binding, suite, or scan object to gather the ARF file for, and `<output-path>` is the local directory to place the results.
+
For example:
+
[source,terminal]
----
$ oc compliance fetch-raw scansettingbindings my-binding -o /tmp/
----
+
.Example output
[source,terminal]
----
Fetching results for my-binding scans: ocp4-cis, ocp4-cis-node-worker, ocp4-cis-node-master
Fetching raw compliance results for scan 'ocp4-cis'.......
The raw compliance results are available in the following directory: /tmp/ocp4-cis
Fetching raw compliance results for scan 'ocp4-cis-node-worker'...........
The raw compliance results are available in the following directory: /tmp/ocp4-cis-node-worker
Fetching raw compliance results for scan 'ocp4-cis-node-master'......
The raw compliance results are available in the following directory: /tmp/ocp4-cis-node-master
----

View the list of files in the directory:

[source,terminal]
----
$ ls /tmp/ocp4-cis-node-master/
----

.Example output
[source,terminal]
----
ocp4-cis-node-master-ip-10-0-128-89.ec2.internal-pod.xml.bzip2  ocp4-cis-node-master-ip-10-0-150-5.ec2.internal-pod.xml.bzip2  ocp4-cis-node-master-ip-10-0-163-32.ec2.internal-pod.xml.bzip2
----

Extract the results:

[source,terminal]
----
$ bunzip2 -c resultsdir/worker-scan/worker-scan-stage-459-tqkg7-compute-0-pod.xml.bzip2 > resultsdir/worker-scan/worker-scan-ip-10-0-170-231.us-east-2.compute.internal-pod.xml
----

View the results:
[source,terminal]
----
$ ls resultsdir/worker-scan/
----

.Example output
[source,terminal]
----
worker-scan-ip-10-0-170-231.us-east-2.compute.internal-pod.xml
worker-scan-stage-459-tqkg7-compute-0-pod.xml.bzip2
worker-scan-stage-459-tqkg7-compute-1-pod.xml.bzip2
----

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="re-running-scans_{context}"]
= Re-running scans

Although it is possible to run scans as scheduled jobs, you must often re-run a scan on demand, particularly after remediations are applied or when other changes to the cluster are made.

.Procedure

* Rerunning a scan with the Compliance Operator requires use of an annotation on the scan object. However, with the `oc-compliance` plugin you can rerun a scan with a single command. Enter the following command to rerun the scans for the `ScanSettingBinding` object named `my-binding`:
+
[source,terminal]
----
$ oc compliance rerun-now scansettingbindings my-binding
----
+
.Example output
[source,terminal]
----
Rerunning scans from 'my-binding': ocp4-cis
Re-running scan 'openshift-compliance/ocp4-cis'
----

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/oc-compliance-plug-in-using.adoc

[id="using-scan-setting-bindings_{context}"]
= Using ScanSettingBinding custom resources

When using the `ScanSetting` and `ScanSettingBinding` custom resources (CRs) that the Compliance Operator provides, it is possible to run scans for multiple profiles while using a common set of scan options, such as `schedule`, `machine roles`, `tolerations`, and so on. While that is easier than working with multiple `ComplianceSuite` or `ComplianceScan` objects, it can confuse new users.

The `oc compliance bind` subcommand helps you create a `ScanSettingBinding` CR.

.Procedure

. Run:
+
[source,terminal]
----
$ oc compliance bind [--dry-run] -N <binding name> [-S <scansetting name>] <objtype/objname> [..<objtype/objname>]
----
+
* If you omit the `-S` flag, the `default` scan setting provided by the Compliance Operator is used.
* The object type is the Kubernetes object type, which  can be `profile` or `tailoredprofile`. More than one object can be provided.
* The object name is the name of the Kubernetes resource, such as `.metadata.name`.
* Add the `--dry-run` option to display the YAML file of the objects that are created.
+
For example, given the following profiles and scan settings:
+
[source,terminal]
----
$ oc get profile.compliance -n openshift-compliance
----
+
.Example output
[source,terminal]
----
NAME                       AGE     VERSION
ocp4-cis                   3h49m   1.5.0
ocp4-cis-1-4               3h49m   1.4.0
ocp4-cis-1-5               3h49m   1.5.0
ocp4-cis-node              3h49m   1.5.0
ocp4-cis-node-1-4          3h49m   1.4.0
ocp4-cis-node-1-5          3h49m   1.5.0
ocp4-e8                    3h49m
ocp4-high                  3h49m   Revision 4
ocp4-high-node             3h49m   Revision 4
ocp4-high-node-rev-4       3h49m   Revision 4
ocp4-high-rev-4            3h49m   Revision 4
ocp4-moderate              3h49m   Revision 4
ocp4-moderate-node         3h49m   Revision 4
ocp4-moderate-node-rev-4   3h49m   Revision 4
ocp4-moderate-rev-4        3h49m   Revision 4
ocp4-nerc-cip              3h49m
ocp4-nerc-cip-node         3h49m
ocp4-pci-dss               3h49m   3.2.1
ocp4-pci-dss-3-2           3h49m   3.2.1
ocp4-pci-dss-4-0           3h49m   4.0.0
ocp4-pci-dss-node          3h49m   3.2.1
ocp4-pci-dss-node-3-2      3h49m   3.2.1
ocp4-pci-dss-node-4-0      3h49m   4.0.0
ocp4-stig                  3h49m   V2R1
ocp4-stig-node             3h49m   V2R1
ocp4-stig-node-v1r1        3h49m   V1R1
ocp4-stig-node-v2r1        3h49m   V2R1
ocp4-stig-v1r1             3h49m   V1R1
ocp4-stig-v2r1             3h49m   V2R1
rhcos4-e8                  3h49m
rhcos4-high                3h49m   Revision 4
rhcos4-high-rev-4          3h49m   Revision 4
rhcos4-moderate            3h49m   Revision 4
rhcos4-moderate-rev-4      3h49m   Revision 4
rhcos4-nerc-cip            3h49m
rhcos4-stig                3h49m   V2R1
rhcos4-stig-v1r1           3h49m   V1R1
rhcos4-stig-v2r1           3h49m   V2R1

----
+
[source,terminal]
----
$ oc get scansettings -n openshift-compliance
----
+
.Example output
[source,terminal]
----
NAME                 AGE
default              10m
default-auto-apply   10m
----

. To apply the `default` settings to the `ocp4-cis` and `ocp4-cis-node` profiles, run:
+
[source,terminal]
----
$ oc compliance bind -N my-binding profile/ocp4-cis profile/ocp4-cis-node
----
+
.Example output
[source,terminal]
----
Creating ScanSettingBinding my-binding
----
+
After the `ScanSettingBinding` CR is created, the bound profile begins scanning for both profiles with the related settings. Overall, this is the fastest way to begin scanning with the Compliance Operator.

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="printing-controls_{context}"]
= Printing controls

Compliance standards are generally organized into a hierarchy as follows:

* A benchmark is the top-level definition of a set of controls for a particular standard. For example, FedRAMP Moderate or Center for Internet Security (CIS) v.1.6.0.
* A control describes a family of requirements that must be met in order to be in compliance with the benchmark. For example, FedRAMP AC-01 (access control policy and procedures).
* A rule is a single check that is specific for the system being brought into compliance, and one or more of these rules map to a control.
* The Compliance Operator handles the grouping of rules into a profile for a single benchmark. It can be difficult to determine which controls that the set of rules in a profile satisfy.

.Procedure

* The `oc compliance` `controls` subcommand provides a report of the standards and controls that a given profile satisfies:
+
[source,terminal]
----
$ oc compliance controls profile ocp4-cis-node
----
+
.Example output
[source,terminal]
----
+-----------+----------+
| FRAMEWORK | CONTROLS |
+-----------+----------+
| CIS-OCP   | 1.1.1    |
+           +----------+
|           | 1.1.10   |
+           +----------+
|           | 1.1.11   |
+           +----------+
...
----

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="fetching-compliance-remediation-details_{context}"]
= Fetching compliance remediation details

The Compliance Operator provides remediation objects that are used to automate the changes required to make the cluster compliant. The `fetch-fixes` subcommand can help you understand exactly which configuration remediations are used. Use the `fetch-fixes` subcommand to extract the remediation objects from a profile, rule, or `ComplianceRemediation` object into a directory to inspect.

.Procedure

. View the remediations for a profile:
+
[source,terminal]
----
$ oc compliance fetch-fixes profile ocp4-cis -o /tmp
----
+
.Example output
[source,terminal]
----
No fixes to persist for rule 'ocp4-api-server-api-priority-flowschema-catch-all' <1>
No fixes to persist for rule 'ocp4-api-server-api-priority-gate-enabled'
No fixes to persist for rule 'ocp4-api-server-audit-log-maxbackup'
Persisted rule fix to /tmp/ocp4-api-server-audit-log-maxsize.yaml
No fixes to persist for rule 'ocp4-api-server-audit-log-path'
No fixes to persist for rule 'ocp4-api-server-auth-mode-no-aa'
No fixes to persist for rule 'ocp4-api-server-auth-mode-node'
No fixes to persist for rule 'ocp4-api-server-auth-mode-rbac'
No fixes to persist for rule 'ocp4-api-server-basic-auth'
No fixes to persist for rule 'ocp4-api-server-bind-address'
No fixes to persist for rule 'ocp4-api-server-client-ca'
Persisted rule fix to /tmp/ocp4-api-server-encryption-provider-cipher.yaml
Persisted rule fix to /tmp/ocp4-api-server-encryption-provider-config.yaml
----
<1> The `No fixes to persist` warning is expected whenever there are rules in a profile that do not have a corresponding remediation, because either the rule cannot be remediated automatically or a remediation was not provided.

. You can view a sample of the YAML file. The `head` command will show you the first 10 lines:
+
[source,terminal]
----
$ head /tmp/ocp4-api-server-audit-log-maxsize.yaml
----
+
.Example output
[source,terminal]
----
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  maximumFileSizeMegabytes: 100
----

. View the remediation from a `ComplianceRemediation` object created after a scan:
+
[source,terminal]
----
$ oc get complianceremediations -n openshift-compliance
----
+
.Example output
[source,terminal]
----
NAME                                             STATE
ocp4-cis-api-server-encryption-provider-cipher   NotApplied
ocp4-cis-api-server-encryption-provider-config   NotApplied
----
+
[source,terminal]
----
$ oc compliance fetch-fixes complianceremediations ocp4-cis-api-server-encryption-provider-cipher -o /tmp
----
+
.Example output
[source,terminal]
----
Persisted compliance remediation fix to /tmp/ocp4-cis-api-server-encryption-provider-cipher.yaml
----

. You can view a sample of the YAML file. The `head` command will show you the first 10 lines:
+
[source,terminal]
----
$ head /tmp/ocp4-cis-api-server-encryption-provider-cipher.yaml
----
+
.Example output
[source,terminal]
----
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  encryption:
    type: aescbc
----

[WARNING]
====
Use caution before applying remediations directly. Some remediations might not be applicable in bulk, such as the usbguard rules in the moderate profile. In these cases, allow the Compliance Operator to apply the rules because it addresses the dependencies and ensures that the cluster remains in a good state.
====

// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

[id="viewing-compliance-remediation-details_{context}"]
= Viewing ComplianceCheckResult object details

When scans are finished running, `ComplianceCheckResult` objects are created for the individual scan rules. The `view-result` subcommand provides a human-readable output of the `ComplianceCheckResult` object details.

.Procedure

* Run:
+
[source,terminal]
----
$ oc compliance view-result ocp4-cis-scheduler-no-bind-address
----
