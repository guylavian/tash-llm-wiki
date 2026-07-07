---
title: "Using service accounts in applications"
type: reference
domain: openshift
slug: authentication-4-22-using-service-accounts-in-applications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/using-service-accounts-in-applications
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Using service accounts in applications

[id="using-service-accounts"]
= Using service accounts in applications

// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-overview_{context}"]
= Service accounts overview

A service account is an OpenShift Container Platform account that allows a component to
directly access the API. Service accounts are API objects that exist within each project.
Service accounts provide a flexible way to control API
access without sharing a regular user's credentials.

When you use the OpenShift Container Platform CLI or web console, your API token
authenticates you to the API. You can associate a component with a service account
so that they can access the API without using a regular user's credentials.

For example, service accounts can allow:

* Replication controllers to make API calls to create or delete pods
* Applications inside containers to make API calls for discovery purposes
* External applications to make API calls for monitoring or integration purposes

Each service account's user name is derived from its project and name:

[source,text]
----
system:serviceaccount:<project>:<name>
----

Every service account is also a member of two groups:

[cols="1,2",options="header"]
|===

|Group
|Description

|system:serviceaccounts
|Includes all service accounts in the system.

|system:serviceaccounts:<project>
|Includes all service accounts in the
specified project.

|===

// Module included in the following assemblies:
//
// * authentication/using-service-accounts-in-applications.adoc

[id="service-accounts-default_{context}"]
= Default service accounts

Your OpenShift Container Platform cluster contains default service accounts for
cluster management and generates more service accounts for each project.

[id="default-cluster-service-accounts_{context}"]
== Default cluster service accounts

Several infrastructure controllers run using service account credentials. The
following service accounts are created in the OpenShift Container Platform infrastructure
project (`openshift-infra`) at server start, and given the following roles
cluster-wide:

[cols="1,3",options="header"]
|====
|Service account |Description

|`replication-controller`
|Assigned the `system:replication-controller` role

|`deployment-controller`
|Assigned the `system:deployment-controller` role

|`build-controller`
|Assigned the `system:build-controller` role. Additionally, the
`build-controller` service account is included in the privileged
security context constraint to create privileged
build pods.
|====

To configure the project where those service accounts are created, set the
`openshiftInfrastructureNamespace` field in the
*_/etc/origin/master/master-config.yml_* file on the master:

----
policyConfig:
  ...
  openshiftInfrastructureNamespace: openshift-infra
----

[id="default-service-accounts-and-roles_{context}"]
== Default project service accounts and roles

Three service accounts are automatically created in each project:

[options="header",cols="1,3a"]
|===
|Service account |Usage

|`builder`
|Used by build pods. It is given the `system:image-builder` role, which allows
pushing images to any imagestream in the project using the internal Docker
registry.

[NOTE]
====
The `builder` service account is not created if the `Build` cluster capability is not enabled.
====

|`deployer`
|Used by deployment pods and given the `system:deployer` role, which allows
viewing and modifying replication controllers and pods in the project.

[NOTE]
====
The `deployer` service account is not created if the `DeploymentConfig` cluster capability is not enabled.
====

|`default`
|Used to run all other pods unless they specify a different service account.

[IMPORTANT]
====
Access rights and security privileges tied to the `default` service account apply to every pod in the project that does not specify a different service account. To implement the principle of least privilege and improve auditability, create dedicated service accounts for your workloads instead of using the `default` service account.

While most OpenShift Container Platform platform components and Operators use dedicated service accounts, the following dynamic tools continue to use the `default` service account to ensure operational efficiency:

* `oc debug`: Uses the `default` service account to avoid the performance overhead of creating and removing unique service accounts for short-lived troubleshooting sessions.
* `oc adm must-gather`: Uses the `default` service account to collect diagnostic data across the cluster without requiring extensive manual RBAC modifications.
====
|===

All service accounts in a project are given the `system:image-puller` role,
which allows pulling images from any image stream in the project using the
internal container image registry.

// Module included in the following assemblies:
//
// * authentication/using-service-accounts-in-applications.adoc
// * pods/nodes-pods-secrets.adoc

[id="auto-generated-sa-token-secrets_{context}"]
= Automatically generated image pull secrets

[role="_abstract"]
OpenShift Container Platform automatically creates image pull secrets for each service account to integrate the internal image registry with user authentication.

[NOTE]
====
Prior to OpenShift Container Platform 4.16, a long-lived service account API token secret was also generated for each service account that was created. Starting with OpenShift Container Platform 4.16, this service account API token secret is no longer created.

After upgrading to , any existing long-lived service account API token secrets are not deleted and will continue to function. For information about detecting long-lived API tokens that are in use in your cluster or deleting them if they are not needed, see "Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase)".
====

This image pull secret is necessary to integrate the {product-registry} into the cluster's user authentication and authorization system.

However, if you do not enable the `ImageRegistry` capability or if you disable the integrated {product-registry} in the Cluster Image Registry Operator's configuration, an image pull secret is not generated for each service account.

When the integrated {product-registry} is disabled on a cluster that previously had it enabled, the previously generated image pull secrets are deleted automatically.

// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-managing_{context}"]
= Creating service accounts

You can create a service account in a project and grant it permissions by
binding it to a role.

.Procedure

. Optional: To view the service accounts in the current project:
+
[source,terminal]
----
$ oc get sa
----
+
.Example output
[source,terminal]
----
NAME       SECRETS   AGE
builder    1         2d
default    1         2d
deployer   1         2d
----

. To create a new service account in the current project:
+
[source,terminal]
----
$ oc create sa <service_account_name> <1>
----
<1> To create a service account in a different project, specify `-n <project_name>`.
+
.Example output
[source,terminal]
----
serviceaccount "robot" created
----
+
[TIP]
====
You can alternatively apply the following YAML to create the service account:

[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name>
  namespace: <current_project>
----
====

. Optional: View the secrets for the service account:
+
[source,terminal]
----
$ oc describe sa robot
----
+
.Example output
[source,terminal]
----
Name:                robot
Namespace:           project1
Labels:              <none>
Annotations:         openshift.io/internal-registry-pull-secret-ref: robot-dockercfg-qzbhb
Image pull secrets:  robot-dockercfg-qzbhb
Mountable secrets:   robot-dockercfg-qzbhb
Tokens:              <none>
Events:              <none>
----

// include::modules/service-accounts-using-credentials-inside-a-container.adoc[leveloffset=+1]
