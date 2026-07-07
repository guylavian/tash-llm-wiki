---
title: "Command quick reference for creating clusters and users"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-quickstart
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-quickstart
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Command quick reference for creating clusters and users

[id="rosa-command-reference"]
= Command quick reference for creating clusters and users

[role="_abstract"]
If you have already created your first cluster and users, this list can serve as a command quick reference list when creating additional clusters and users.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-quickstart.adoc

[id="rosa-quickstart-instructions"]
= Command quick reference list

If you have already created your first cluster and users, this list can serve as a command quick reference list when creating additional clusters and users.

[source,terminal]
----
## Configures your AWS account and ensures everything is setup correctly
$ rosa init
----

[source,terminal]
----
## Starts the cluster creation process (~30-40minutes)
$ rosa create cluster --cluster-name=<cluster_name>
----

[source,terminal]
----
## Connect your IDP to your cluster
$ rosa create idp --cluster=<cluster_name> --interactive
----

[source,terminal]
----
## Promotes a user from your IDP to dedicated-admin level
$ rosa grant user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----

[source,terminal]
----
## Checks if your install is ready (look for State: Ready),
## and provides your Console URL to login to the web console.
$ rosa describe cluster --cluster=<cluster_name>
----

[role="_additional-resources"]
== Additional resources
* Understanding the ROSA deployment workflow
