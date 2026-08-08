---
title: "Propagating custom metadata to ComplianceCheckResult objects"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-checkresult-custom-metadata
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-checkresult-custom-metadata
version: 4.22
family: security
documentKind: "Documentation"
---

# Propagating custom metadata to ComplianceCheckResult objects

[id="compliance-operator-checkresult-custom-metadata"]
= Propagating custom metadata to ComplianceCheckResult objects

[role="_abstract"]
Starting in Compliance Operator 1.9.0, add labels and annotations to `Rule` and `CustomRule` objects so matching metadata is displayed on `ComplianceCheckResult` objects after a scan. Downstream tools, dashboards, and ticketing workflows can use this metadata without maintaining a separate mapping.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-checkresult-custom-metadata.adoc

[id="compliance-operator-checkresult-custom-metadata-overview_{context}"]
= Understanding custom metadata on rules and check results

[role="_abstract"]
When the Compliance Operator creates or updates a `ComplianceCheckResult` object for a check that Open Security Content Automation Protocol (OpenSCAP) evaluates, it copies custom labels and annotations from the corresponding `Rule` object in the same namespace.

For checks that the Common Expression Language (CEL) scanner evaluates from a `CustomRule`, the Operator copies custom metadata from that `CustomRule` instead.

Custom metadata is any label or annotation whose name is not managed by the Compliance Operator or core Kubernetes namespaces. Some keys are reserved, so user-supplied values never replace the Operator values for those keys. Examples include the following:

* Keys starting with `compliance.openshift.io/`
* Keys starting with `complianceoperator.openshift.io/`
* Keys starting with `complianceascode.io/`
* Keys where the domain contains `kubernetes.io/` (such as `kubernetes.io/name` or `app.kubernetes.io/`)
* Keys where the domain contains `k8s.io/` (such as `k8s.io/component` or `node.k8s.io/instance-type`)

[NOTE]
====
Metadata that you set on `TailoredProfile`, `ScanSettingBinding`, or other orchestration resources is not propagated to individual `ComplianceCheckResult` objects. Attach metadata on the `Rule` or `CustomRule` that owns the check.
====

[NOTE]
====
Custom metadata on `ComplianceRemediation` objects is not covered by this feature.
====

Profile bundle updates:: When a `ProfileBundle` refreshes profile content, the Operator merges user-defined annotations on `Rule` objects with parser-managed annotations so your keys remain while Operator and content fields stay current.

Failure behavior:: If the Operator cannot build its in-memory index of `Rule` objects during aggregation, it logs a warning and still creates scan results without your custom metadata. If a label value violates Kubernetes length or syntax rules, the Operator can fail to create that specific `ComplianceCheckResult` while other results continue.

For more background on the enhancement, see Additional resources.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-checkresult-custom-metadata.adoc

[id="compliance-operator-checkresult-custom-metadata-configure-rules_{context}"]
= Adding custom labels and annotations to a Rule object

[role="_abstract"]
You can attach custom labels and annotations to a `Rule` that Open Security Content Automation Protocol (OpenSCAP) evaluates, and verify that they are displayed on the aggregated `ComplianceCheckResult` after the next scan.

.Prerequisites

* You have installed Compliance Operator 1.9.0 or later.
* You have access to the `openshift-compliance` namespace (or the namespace where your rules and scans run).
* You identified the `Rule` object name and the `ComplianceScan` that evaluates it.

.Procedure

. Add custom labels to the rule. Replace `<rule_name>` with your `Rule` object name, and adjust labels as needed with the following command:
+
[source,terminal]
----
$ oc label rule.compliance/<rule_name> \
  business-unit=payments \
  risk-tier=critical \
  -n openshift-compliance
----

. Add custom annotations with the following command:
+
[source,terminal]
----
$ oc annotate rule.compliance/<rule_name> \
  internal-id=SEC-4021 \
  exception-ticket=JIRA-123 \
  -n openshift-compliance
----
+
Long or free-form values are better suited to annotations than labels because of Kubernetes label length limits.

. Trigger a new scan or wait for the next scheduled run. For example, to request a rescan of an existing `ComplianceScan` named `ocp4-cis` use the following command:
+
[source,terminal]
----
$ oc annotate compliancescan ocp4-cis \
  compliance.openshift.io/rescan= \
  -n openshift-compliance
----

. After the scan finishes, list `ComplianceCheckResult` objects that carry your label using the following command:
+
[source,terminal]
----
$ oc get compliancecheckresults \
  -l business-unit=payments \
  -n openshift-compliance
----

. Confirm an annotation on a specific result with the following command:
+
[source,terminal]
----
$ oc get compliancecheckresult <result_name> \
  -o jsonpath='{.metadata.annotations.internal-id}' \
  -n openshift-compliance
----
+
Replace `<result_name>` with the `ComplianceCheckResult` name for your rule.

. Optional: Verify that a user annotation survives a `ProfileBundle` content image update using the following command.
+
[source,terminal]
----
$ oc get rule.compliance/<rule_name> \
  -o jsonpath='{.metadata.annotations.exception-ticket}' \
  -n openshift-compliance
----
+
After the profile parser reconciles the `Rule`, your key should still be present.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-checkresult-custom-metadata.adoc

[id="compliance-operator-checkresult-custom-metadata-configure-customrules_{context}"]
= Adding custom labels and annotations to a CustomRule object

[role="_abstract"]
For platform checks implemented as a `CustomRule` object and evaluated by the Common Expression Language (CEL) scanner, define labels and annotations on the `CustomRule` metadata. The Compliance Operator copies non-reserved entries onto each generated `ComplianceCheckResult`.

.Prerequisites

* You have installed Compliance Operator 1.9.0 or later.
* You use a `TailoredProfile` (or equivalent workflow) that enables your `CustomRule` for a CEL profile scan.

.Procedure

. Create a `CustomRule` object that includes your metadata in `metadata.labels` and `metadata.annotations`. The following example defines a platform CEL check; replace names, expressions, and metadata with values appropriate for your environment:
+
[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
kind: CustomRule
metadata:
  name: check-pod-security-standard
  namespace: openshift-compliance
  labels:
    break_severity: critical
    weakness_score: "9.5"
  annotations:
    internal-id: SEC-5500
    audit-contact: platform-security-team
spec:
  id: check-pod-security-standard
  title: "Ensure Pod Security Standards are enforced"
  severity: high
  checkType: Platform
  scannerType: CEL
  expression: |
    namespaces.items.all(ns,
      has(ns.metadata.labels) &&
      "pod-security.kubernetes.io/enforce" in ns.metadata.labels
    )
  failureReason: "One or more namespaces do not enforce Pod Security Standards"
  inputs:
    - name: namespaces
      kubernetesInputSpec:
        apiVersion: v1
        resource: namespaces
----

. Apply the manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f custom-rule.yaml
----

. Reference the `CustomRule` object from a `TailoredProfile`, for example:
+
[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: custom-cel-profile
  namespace: openshift-compliance
spec:
  title: "Custom CEL profile"
  description: "Profile with custom CEL rules"
  enableRules:
    - name: check-pod-security-standard
      rationale: "Enforce pod security standards"
      kind: CustomRule
----

. Bind the tailored profile with a `ScanSettingBinding` and run the scan using your normal workflow.

. After the scan completes, query results by a custom label by running the following command:
+
[source,terminal]
----
$ oc get compliancecheckresults \
  -l break_severity=critical \
  -n openshift-compliance
----

. Identify the `ComplianceCheckResult` name for your `CustomRule` object in the scan output, for example by listing results in the namespace and filtering by labels or name.

. Read a propagated annotation from that object by running the following command:
+
[source,terminal]
----
$ oc get compliancecheckresult <result_name> \
  -o jsonpath='{.metadata.annotations.internal-id}' \
  -n openshift-compliance
----
