---
title: "CLI flags for traffic splitting"
type: reference
domain: openshift
slug: serverless-4-22-traffic-splitting-flags
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/traffic-splitting-flags
version: 4.22
family: serverless
documentKind: "Documentation"
---

# CLI flags for traffic splitting

[id="traffic-splitting-flags"]
= CLI flags for traffic splitting

The Knative (`kn`) CLI supports traffic operations on the traffic block of a service as part of the `kn service update` command.

// kn flags
// Module included in the following assemblies:
//
// * serverless/develop/serverless-traffic-management.adoc

[id="serverless-traffic-splitting-flags-kn_{context}"]
= Knative CLI traffic splitting flags

The following table displays a summary of traffic splitting flags, value formats, and the operation the flag performs. The *Repetition* column denotes whether repeating the particular value of flag is allowed in a `kn service update` command.

[cols=4*,options="header"]
|===
|Flag
|Value(s)
|Operation
|Repetition

|`--traffic`
|`RevisionName=Percent`
|Gives `Percent` traffic to `RevisionName`
|Yes

|`--traffic`
|`Tag=Percent`
|Gives `Percent` traffic to the revision having `Tag`
|Yes

|`--traffic`
|`@latest=Percent`
|Gives `Percent` traffic to the latest ready revision
|No

|`--tag`
|`RevisionName=Tag`
|Gives `Tag` to `RevisionName`
|Yes

|`--tag`
|`@latest=Tag`
|Gives `Tag` to the latest ready revision
|No

|`--untag`
|`Tag`
|Removes `Tag` from revision
|Yes
|===

[id="serverless-traffic-splitting-flags-kn-precedence_{context}"]
== Multiple flags and order precedence

All traffic-related flags can be specified using a single `kn service update` command. `kn` defines the precedence of these flags. The order of the flags specified when using the command is not taken into account.

The precedence of the flags as they are evaluated by `kn` are:

. `--untag`: All the referenced revisions with this flag are removed from the traffic block.
. `--tag`: Revisions are tagged as specified in the traffic block.
. `--traffic`: The referenced revisions are assigned a portion of the traffic split.

You can add tags to revisions and then split traffic according to the tags you have set.

// creating custom URLs by using tags
// Module included in the following assemblies:
//
// * serverless/develop/serverless-traffic-management.adoc

[id="serverless-custom-revision-urls_{context}"]
= Custom URLs for revisions

Assigning a `--tag` flag to a service by using the `kn service update` command creates a custom URL for the revision that is created when you update the service. The custom URL follows the pattern `https://<tag>-<service_name>-<namespace>.<domain>` or `http://<tag>-<service_name>-<namespace>.<domain>`.

The `--tag` and `--untag` flags use the following syntax:

* Require one value.
* Denote a unique tag in the traffic block of the service.
* Can be specified multiple times in one command.

[id="serverless-custom-revision-urls-assign_{context}"]
== Example: Assign a tag to a revision

The following example assigns the tag `latest` to a revision named `example-revision`:

[source,terminal]
----
$ kn service update <service_name> --tag @latest=example-tag
----

[id="serverless-custom-revision-urls-remove_{context}"]
== Example: Remove a tag from a revision

You can remove a tag to remove the custom URL, by using the `--untag` flag.

[NOTE]
====
If a revision has its tags removed, and it is assigned 0% of the traffic, the revision is removed from the traffic block entirely.
====

The following command removes all tags from the revision named `example-revision`:

[source,terminal]
----
$ kn service update <service_name> --untag example-tag
----
