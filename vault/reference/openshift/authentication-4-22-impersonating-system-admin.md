---
title: "Impersonating the system:admin user"
type: reference
domain: openshift
slug: authentication-4-22-impersonating-system-admin
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/impersonating-system-admin
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Impersonating the system:admin user

[id="impersonating-system-admin"]
= Impersonating the system:admin user

// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc
// * applications/projects/creating-project-other-user.adoc
// * users_and_roles/impersonating-system-admin.adoc

[id="authentication-api-impersonation_{context}"]
= API impersonation

You can configure a request to the OpenShift Container Platform API to act as though it originated from another user. For more information, see User impersonation in the Kubernetes documentation.

// Module included in the following assemblies:
//
// * users_and_roles/impersonating-system-admin.adoc

[id="impersonation-system-admin-user_{context}"]
= Impersonating the system:admin user

You can use the OpenShift web console to impersonate a user and select multiple group memberships at the same time to reproduce that user’s effective permissions.

.Procedure

* To grant a user permission to impersonate `system:admin`, run the following command:
+
[source,terminal]
----
$ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --user=<username>
----
+
[TIP]
====
You can alternatively apply the following YAML to grant permission to impersonate `system:admin`:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: <any_valid_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: sudoer
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: <username>
----
====

// Module included in the following assemblies:
//
// * users_and_roles/impersonating-system-admin.adoc

[id="impersonation-system-admin-group_{context}"]
= Impersonating the system:admin group

When a `system:admin` user is granted cluster administration permissions through a group, you must include the
`--as=<user> --as-group=<group1> --as-group=<group2>` parameters in the command to impersonate the associated groups.

.Procedure

* To grant a user permission to impersonate a `system:admin` by impersonating the associated cluster administration groups,
run the following command:
+
[source,terminal]
----
$ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --as=<user> \
--as-group=<group1> --as-group=<group2>
----

[id="impersonating-user-multiple-group-memberships-web-console"]
= Impersonating a user with multiple group memberships in the web console

[role="_abstract"]
You can start user impersonation from multiple locations in the OpenShift Container Platform Console. Depending on where you start, you can impersonate a single user, a single group, or a user with one or more group memberships.

.Prerequisites
* You must be logged in to the OpenShift Container Platform web console as a user with permission to impersonate other users.
* The user or group that you want to impersonate must already exist.

[NOTE]
====
The impersonated user can belong to zero or more groups.
====

.Procedure
. From the **Overview** page in the OpenShift Container Platform console, click your user name and select **Impersonate User**.
. In the **Username** field in the **Impersonate** dialog, enter the name of the user you want to impersonate.
. Optional: In the **Groups** field, choose one or more groups that are associated with the user.
+
The dialog displays a warning message explaining that impersonation applies the effective permissions of the specified user and any selected groups.

. Click **Impersonate** to impersonate your selected user, groups, or both.

[NOTE]
====
Selecting one group uses the existing single-group impersonation behavior. Selecting no groups uses regular single-user impersonation.
====

[id="starting-impersonation-users-groups-pages"]
= Starting impersonation from the Users or Groups pages

[role="_abstract"]
You can start impersonation for users or groups from the **Users** or **Groups** pages in the OpenShift Container Platform Console.

.Procedure
. From the **Overview** page in the OpenShift Container Platform console, click **User Management** → **Users**.
. Open the menu for the user you want to impersonate and select **Impersonate User**.
. Optional: To impersonate a group, click **User Management** → **Groups**, click the menu for that group, and select **Impersonate Group**.

[id="stopping-impersonation"]
= Stopping impersonation

[role="_abstract"]
You can stop impersonating a user or group at any time from the OpenShift Container Platform Console.

.Procedure
. On any page in the OpenShift Container Platform console, click **Stop impersonating** at the top of the page.
. Alternatively, click your user name and select **Stop impersonating**.

// Module included in the following assemblies:
//
// * authentication/impersonating-system-admin.adoc
// * authentication/tokens-scoping.adoc
// * authentication/managing-oauth-access-tokens.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="unauthenticated-users-cluster-role-bindings_{context}"]
= Adding unauthenticated groups to cluster roles

[role="_abstract"]
As a cluster administrator, you can add unauthenticated users to the following cluster roles in OpenShift Container Platform by creating a cluster role binding. Unauthenticated users do not have access to non-public cluster roles. This should only be done in specific use cases when necessary.

You can add unauthenticated users to the following cluster roles:

* `system:scope-impersonation`
* `system:webhook`
* `system:oauth-token-deleter`
* `self-access-reviewer`

[IMPORTANT]
====
Always verify compliance with your organization's security standards when modifying unauthenticated access.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file named `add-<cluster_role>-unauth.yaml` and add the following content:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 annotations:
   rbac.authorization.kubernetes.io/autoupdate: "true"
 name: <cluster_role>access-unauthenticated
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: <cluster_role>
subjects:
 - apiGroup: rbac.authorization.k8s.io
   kind: Group
   name: system:unauthenticated
----
. Apply the configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f add-<cluster_role>.yaml
----
