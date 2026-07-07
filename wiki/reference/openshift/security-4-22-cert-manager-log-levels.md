---
title: "Configuring log levels for cert-manager and the {cert-manager-operator}"
type: reference
domain: openshift
slug: security-4-22-cert-manager-log-levels
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-log-levels
version: 4.22
family: security
documentKind: "Documentation"
---

# Configuring log levels for cert-manager and the {cert-manager-operator}

[id="cert-manager-log-levels"]
= Configuring log levels for cert-manager and the {cert-manager-operator}

[role="_abstract"]
To troubleshoot issues with the cert-manager components and the {cert-manager-operator}, you can configure the log level verbosity.

[NOTE]
====
To use different log levels for different cert-manager components, see _Customizing cert-manager Operator API fields_.
====

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-log-levels.adoc

[id="cert-manager-enable-operand-log-level_{context}"]
= Setting a log level for cert-manager

[role="_abstract"]
To troubleshoot issues and control log volume, configure the log level for the {cert-manager-operator}. You can set specific verbosity levels to capture the necessary details for debugging or to reduce noise in your cluster logs.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed version 1.11.1 or later of the {cert-manager-operator}.

.Procedure

. Edit the `CertManager` resource by running the following command:
+
[source,terminal]
----
$ oc edit certmanager.operator cluster
----

. Set the log level value by editing the `spec.logLevel` section:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
...
spec:
  logLevel: <log_level>
----
+
The valid log level values for the `CertManager` resource are `Normal`, `Debug`, `Trace`, and `TraceAll`. To audit logs and perform common operations when there are no issues, set `logLevel` to `Normal` . To troubleshoot a minor issue by viewing verbose logs, set `logLevel` to `Debug` . To troubleshoot a major issue by viewing more verbose logs, you can set `logLevel` to `Trace`. To troubleshoot serious issues, set `logLevel` to `TraceAll`. The default `logLevel` is `Normal`.
+
[NOTE]
====
`TraceAll` generates huge amount of logs. After setting `logLevel` to `TraceAll`, you might experience performance issues.
====

. Save your changes and quit the text editor to apply your changes.
+
After applying the changes, the verbosity level for the cert-manager components controller, CA injector, and webhook is updated.

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-log-levels.adoc

[id="cert-manager-enable-operator-log-level_{context}"]
= Setting a log level for the {cert-manager-operator}

[role="_abstract"]
To troubleshoot issues and control log volume, set the log level for the {cert-manager-operator}. You can configure the verbosity of the Operator log messages to capture the specific details required for your environment.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed version 1.11.1 or later of the {cert-manager-operator}.

.Procedure

* Update the subscription object for {cert-manager-operator} to provide the verbosity level for the operator logs by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"OPERATOR_LOG_LEVEL","value":"v"}]}}}'
----
+
Replace `v` with the desired log level number. The valid values for `v` can range from `1`to `10`. The default value is `2`.

.Verification

. The cert-manager Operator pod is redeployed. Verify that the log level of the {cert-manager-operator} is updated by running the following command:
+
[source,terminal]
----
$ oc set env deploy/cert-manager-operator-controller-manager -n cert-manager-operator --list | grep -e OPERATOR_LOG_LEVEL -e container
----
+
.Example output
[source,terminal]
----
# deployments/cert-manager-operator-controller-manager, container kube-rbac-proxy
OPERATOR_LOG_LEVEL=9
# deployments/cert-manager-operator-controller-manager, container cert-manager-operator
OPERATOR_LOG_LEVEL=9
----

. Verify that the log level of the {cert-manager-operator} is updated by running the `oc logs` command:
+
[source,terminal]
----
$ oc logs deploy/cert-manager-operator-controller-manager -n cert-manager-operator
----

[role="_additional-resources"]
[id="cert-manager-log-levels_additional-resources"]
== Additional resources

* Customizing cert-manager Operator API fields
