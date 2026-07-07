---
title: "`{odo-title}` release notes"
type: reference
domain: openshift
slug: cli-reference-4-22-odo-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/odo-release-notes
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# `{odo-title}` release notes

[id='odo-release-notes']
= `{odo-title}` release notes

[id="odo-notable-improvements_{context}"]
== Notable changes and improvements in `{odo-title}` version 2.5.0

// #5238
* Creates unique routes for each component, using `adler32` hashing
// #5252
* Supports additional fields in the devfile for assigning resources:
** cpuRequest
** cpuLimit
** memoryRequest
** memoryLimit
// #5276
* Adds the `--deploy` flag to the `odo delete` command, to remove components deployed using the `odo deploy` command:
+
[source,terminal]
----
$ odo delete --deploy
----
// #5237
* Adds mapping support to the `odo link` command
// #5279
* Supports ephemeral volumes using the `ephemeral` field in `volume` components
// #5270
* Sets the default answer to `yes` when asking for telemetry opt-in
// #5260
* Improves metrics by sending additional telemetry data to the devfile registry
// #5287
* Updates the bootstrap image to `registry.access.redhat.com/ocp-tools-4/odo-init-container-rhel8:1.1.11`
// #5308
* The upstream repository is available at 

[id="odo-fixed-issues_{context}"]
== Bug fixes
// #5294
* Previously, `odo deploy` would fail if the `.odo/env` file did not exist. The command now creates the `.odo/env` file if required.
// #5286
* Previously, interactive component creation using the `odo create` command would fail if disconnect from the cluster. This issue is fixed in the latest release.

[id="odo-getting-support_{context}"]
== Getting support

.For Product

If you find an error, encounter a bug, or have suggestions for improving the functionality of `{odo-title}`, file an issue in Bugzilla. Choose *OpenShift Developer Tools and Services* as a product type and *odo* as a component.

Provide as many details in the issue description as possible.

.For Documentation

If you find an error or have suggestions for improving the documentation, file an issue in Bugzilla. Choose the *OpenShift Container Platform* product type and the *Documentation* component type.

== Known issues

//[id="odo-technology-preview_{context}"]
//== Technology Preview features `{odo-title}`
