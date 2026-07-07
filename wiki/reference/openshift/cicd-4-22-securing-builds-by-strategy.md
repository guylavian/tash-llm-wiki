---
title: "Securing builds by strategy"
type: reference
domain: openshift
slug: cicd-4-22-securing-builds-by-strategy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/securing-builds-by-strategy
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Securing builds by strategy

[id="securing-builds-by-strategy"]
= Securing builds by strategy

Builds in OpenShift Container Platform are run in privileged containers. Depending on the build strategy used, if you have privileges, you can run builds to escalate their permissions on the cluster and host nodes. And as a security measure, it limits who can run builds and the strategy that is used for those builds. Custom builds are inherently less safe than source builds, because they can execute any code within a privileged container, and are disabled by default. Grant docker build permissions with caution, because a vulnerability in the Dockerfile processing logic could result in a privileges being granted on the host node.

By default, all users that can create builds are granted permission to use the docker and Source-to-image (S2I) build strategies. Users with cluster administrator privileges can enable the custom build strategy, as referenced in the restricting build strategies to a user globally section.

You can control who can build and which build strategies they can use by using an authorization policy. Each build strategy has a corresponding build subresource. A user must have permission to create a build and permission to create on the build strategy subresource to create builds using that strategy. Default roles are provided that grant the create permission on the build strategy subresource.

.Build Strategy Subresources and Roles
[options="header"]
|===

|Strategy |Subresource |Role

|Docker
|builds/docker
|system:build-strategy-docker

|Source-to-Image
|builds/source
|system:build-strategy-source

|Custom
|builds/custom
|system:build-strategy-custom

|JenkinsPipeline
|builds/jenkinspipeline
|system:build-strategy-jenkinspipeline

|===

// Module included in the following assemblies:
//
// * builds/securing-builds-by-strategy.adoc

[id="builds-disabling-build-strategy-globally_{context}"]
= Disabling access to a build strategy globally

To prevent access to a particular build strategy globally, log in as a user with cluster administrator privileges, remove the corresponding role from the `system:authenticated` group, and apply the annotation `rbac.authorization.kubernetes.io/autoupdate: "false"` to protect them from changes between the API restarts. The following example shows disabling the docker build strategy.

.Procedure

. Apply the `rbac.authorization.kubernetes.io/autoupdate` annotation by entering the following command:
+
[source,terminal]
----
$ oc annotate clusterrolebinding.rbac system:build-strategy-docker-binding 'rbac.authorization.kubernetes.io/autoupdate=false' --overwrite
----

. Remove the role by entering the following command:
+
[source,terminal]
----
$ oc adm policy remove-cluster-role-from-group system:build-strategy-docker system:authenticated
----

. Ensure the build strategy subresources are also removed from the `admin` and `edit` user roles:
+
[source,terminal]
----
$ oc get clusterrole admin -o yaml | grep "builds/docker"
----
+
[source,terminal]
----
$ oc get clusterrole edit -o yaml | grep "builds/docker"
----
// Module included in the following assemblies:
//
// * builds/securing-builds-by-strategy.adoc

[id="builds-restricting-build-strategy-globally_{context}"]
= Restricting build strategies to users globally

You can allow a set of specific users to create builds with a particular strategy.

.Procedure

* Assign the role that corresponds to the build strategy to a specific user. For
example, to add the `system:build-strategy-docker` cluster role to the user
`devuser`:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user system:build-strategy-docker devuser
----
+
[WARNING]
====
Granting a user access at the cluster level to the `builds/docker` subresource means that the user can create builds with the docker strategy in any project in which they can create builds.
====
// Module included in the following assemblies:
//
// * builds/securing-builds-by-strategy.adoc

[id="builds-restricting-build-strategy-to-user_{context}"]
= Restricting build strategies to a user within a project

Similar to granting the build strategy role to a user globally, you can allow a set of specific users within a project to create builds with a particular strategy.

.Procedure

* Assign the role that corresponds to the build strategy to a specific user within a project. For example, to add the `system:build-strategy-docker` role within the project `devproject` to the user `devuser`:
+
[source,terminal]
----
$ oc adm policy add-role-to-user system:build-strategy-docker devuser -n devproject
----
