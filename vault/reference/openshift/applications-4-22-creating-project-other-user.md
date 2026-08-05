---
title: "Creating a project as another user"
type: reference
domain: openshift
slug: applications-4-22-creating-project-other-user
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/creating-project-other-user
version: 4.22
family: applications
documentKind: "Documentation"
---

# Creating a project as another user

[id="creating-project-other-user"]
= Creating a project as another user

Impersonation allows you to create a project as a different user.

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
// * applications/projects/creating-project-other-user.adoc

[id="impersonation-project-creation_{context}"]
= Impersonating a user when you create a project

You can impersonate a different user when you create a project request. Because
`system:authenticated:oauth` is the only bootstrap group that can
create project requests, you must impersonate that group.

.Procedure

* To create a project request on behalf of a different user:
+
[source,terminal]
----
$ oc new-project <project> --as=<user> \
    --as-group=system:authenticated --as-group=system:authenticated:oauth
----
