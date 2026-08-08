---
title: "Serverless upgrades"
type: reference
domain: openshift
slug: serverless-4-22-serverless-upgrades
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-upgrades
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Serverless upgrades

[id="serverless-upgrades"]
= Serverless upgrades

{ServerlessProductName} should be upgraded without skipping release versions. This section shows how to resolve problems with upgrading.

// Module included in the following assemblies:
//
// * /serverless/install/serverless-upgrades.adoc

[id="serverless-resolving-operator-upgrade-failure_{context}"]
= Resolving an {ServerlessOperatorName} upgrade failure

You might encounter an error when upgrading {ServerlessOperatorName}, for example, when performing manual uninstalls and reinstalls. If you encounter an error, you must manually reinstall {ServerlessOperatorName}.

.Procedure

. Identify the version of {ServerlessOperatorName} that was installed originally by searching in the {ServerlessProductName} Release Notes.
+
For example, the error message during attempted upgrade might contain the following string:
+
[source]
----
The installed KnativeServing version is v1.5.0.
----
+
In this example, the KnativeServing `MAJOR.MINOR` version is `1.5`, which is covered in the release notes for {ServerlessProductName} 1.26: _OpenShift Serverless now uses Knative Serving 1.5_.

. Uninstall {ServerlessOperatorName} and all of its install plans.

. Manually install the version of {ServerlessOperatorName} that you discovered in the first step. To install, first create a `serverless-subscription.yaml` file as shown in the following example:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: serverless-operator
  namespace: openshift-serverless
spec:
  channel: stable
  name: serverless-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
  startingCSV: serverless-operator.v1.26.0
----

. Then, install the subscription by running the following command:
+
[source,terminal]
----
$ oc apply -f serverless-subscription.yaml
----

. Upgrade by manually approving the upgrade install plans as they appear.

[role="_additional-resources"]
.Additional resources

* {ServerlessProductName} Release Notes
* Deleting Operators from a cluster using the web console
* Installing the OpenShift Serverless Operator from the web console
