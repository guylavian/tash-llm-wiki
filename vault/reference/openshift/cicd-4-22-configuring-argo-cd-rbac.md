---
title: "Configuring Argo CD RBAC"
type: reference
domain: openshift
slug: cicd-4-22-configuring-argo-cd-rbac
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-argo-cd-rbac
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring Argo CD RBAC

[id="configuring-argo-cd-rbac"]
= Configuring Argo CD RBAC

[role="_abstract"]
By default, if you are logged into Argo CD using RHSSO, you are a read-only user. You can change and manage the user level access.

// Module is included in the following assemblies:
//
// * installing-red-hat-openshift-gitops

[id="configuring-user-level-access_{context}"]
= Configuring user level access

[role="_abstract"]
To manage and modify the user level access, configure the RBAC section in Argo CD custom resource.

.Procedure

* Edit the `argocd` Custom Resource:
+
[source,terminal]
----
$ oc edit argocd [argocd-instance-name] -n [namespace]
----
.Output
+
[source,yaml]
----
metadata
...
...
  rbac:
    policy: 'g, rbacsystem:cluster-admins, role:admin'
    scopes: '[groups]'
----
+
* Add the `policy` configuration to the `rbac` section and add the `name`, `email` and the `role` of the user:
+
[source,yaml]
----
metadata
...
...
rbac:
    policy: <name>, <email>, role:<admin>
    scopes: '[groups]'
----

[NOTE]
====
Currently, RHSSO cannot read the group information of {gitops-title} users. Therefore, configure the RBAC at the user level.
====
// Module is included in the following assemblies:
//
// * installing-red-hat-openshift-gitops

[id="modifying-rhsso-resource-requests-limits_{context}"]
= Modifying RHSSO resource requests/limits

[role="_abstract"]
By default, the RHSSO container is created with resource requests and limitations. You can change and manage the resource requests.

|===
|*Resource* |*Requests* |*Limits*

|CPU|500|1000m
|Memory|512 Mi|1024 Mi

|===
.Procedure
Modify the default resource requirements patching the Argo CD CR:

[source,terminal]
----
$ oc -n openshift-gitops patch argocd openshift-gitops --type='json' -p='[{"op": "add", "path": "/spec/sso", "value": {"provider": "keycloak", "resources": {"requests": {"cpu": "512m", "memory": "512Mi"}, "limits": {"cpu": "1024m", "memory": "1024Mi"}} }}]'
----

[NOTE]
====
RHSSO created by the {gitops-title} only persists the changes that are made by the operator. If the RHSSO restarts, any additional configuration created by the Admin in RHSSO is deleted.
====
