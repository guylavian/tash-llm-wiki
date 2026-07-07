---
title: "Pruning objects to reclaim resources"
type: reference
domain: openshift
slug: applications-4-22-pruning-objects
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/pruning-objects
version: 4.22
family: applications
documentKind: "Documentation"
---

# Pruning objects to reclaim resources

[id="pruning-objects"]
= Pruning objects to reclaim resources

Over time, API objects created in OpenShift Container Platform can accumulate in the
cluster's etcd data store through normal user operations, such as when building
and deploying applications.

Cluster administrators can periodically prune older versions of objects from the
cluster that are no longer required. For example, by pruning images you can delete
older images and layers that are no longer in use, but are still taking up disk
space.
A user with the `dedicated-admin` role can periodically prune older versions of objects from the
cluster that are no longer required. For example, by pruning images you can delete
older images and layers that are no longer in use, but are still taking up disk
space.

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-basic-operations_{context}"]
= Basic pruning operations

The CLI groups prune operations under a common parent command:

[source,terminal]
----
$ oc adm prune <object_type> <options>
----

This specifies:

- The `<object_type>` to perform the action on, such as `groups`, `builds`,
`deployments`, or `images`.
- The `<options>` supported to prune that object type.

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-groups_{context}"]
= Pruning groups

To prune groups records from an external provider, administrators can run the
following command:

[source,terminal]
----
$ oc adm prune groups \
    --sync-config=path/to/sync/config [<options>]
----

.`oc adm prune groups` flags
[cols="4,8",options="header"]
|===

|Options |Description

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a dry-run.

.^|`--blacklist`
|Path to the group blacklist file.

.^|`--whitelist`
|Path to the group whitelist file.

.^|`--sync-config`
|Path to the synchronization configuration file.
|===

.Procedure

. To see the groups that the prune command deletes, run the following command:
+
[source,terminal]
----
$ oc adm prune groups --sync-config=ldap-sync-config.yaml
----

. To perform the prune operation, add the `--confirm` flag:
+
[source,terminal]
----
$ oc adm prune groups --sync-config=ldap-sync-config.yaml --confirm
----

Needs "Additional resources" links when converted:

//Future Configuring LDAP Sync
//Future Syncing Groups With LDAP

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-deployments_{context}"]
= Pruning deployment resources

You can prune resources associated with deployments that are no longer required by the system, due to age and status.

The following command prunes replication controllers associated with `DeploymentConfig` objects:

[source,terminal]
----
$ oc adm prune deployments [<options>]
----

[NOTE]
====
To also prune replica sets associated with `Deployment` objects, use the `--replica-sets` flag. This flag is currently a Technology Preview feature.
====

.`oc adm prune deployments` flags
[cols="4,8a",options="header"]
|===

|Option |Description

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a dry-run.

.^|`--keep-complete=<N>`
|Per the `DeploymentConfig` object, keep the last `N` replication controllers that have a status of `Complete` and replica count of zero. The default is `5`.

.^|`--keep-failed=<N>`
|Per the `DeploymentConfig` object, keep the last `N` replication controllers that have a status of `Failed` and replica count of zero. The default is `1`.

.^|`--keep-younger-than=<duration>`
|Do not prune any replication controller that is younger than `<duration>` relative to the current time. Valid units of measurement include nanoseconds (`ns`), microseconds (`us`), milliseconds (`ms`), seconds (`s`), minutes (`m`), and hours (`h`). The default is `60m`.

.^|`--orphans`
|Prune all replication controllers that no longer have a `DeploymentConfig` object, has status of `Complete` or `Failed`, and has a replica count of zero.

.^|`--replica-sets=true\|false`
|If `true`, replica sets are included in the pruning process. The default is `false`.

[IMPORTANT]
====
This flag is a Technology Preview feature.
====
|===

.Procedure

. To see what a pruning operation would delete, run the following command:
+
[source,terminal]
----
$ oc adm prune deployments --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m
----

. To actually perform the prune operation, add the `--confirm` flag:
+
[source,terminal]
----
$ oc adm prune deployments --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m --confirm
----

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-builds_{context}"]
= Pruning builds

To prune builds that are no longer required by the system due to age and status, administrators can run the following command:

[source,terminal]
----
$ oc adm prune builds [<options>]
----

.`oc adm prune builds` flags
[cols="4,8",options="header"]
|===

|Option |Description

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a dry-run.

.^|`--orphans`
|Prune all builds whose build configuration no longer exists, status is complete, failed, error, or canceled.

.^|`--keep-complete=<N>`
|Per build configuration, keep the last `N` builds whose status is complete. The default is `5`.

.^|`--keep-failed=<N>`
|Per build configuration, keep the last `N` builds whose status is failed, error, or canceled. The default is `1`.

.^|`--keep-younger-than=<duration>`
|Do not prune any object that is younger than `<duration>` relative to the current time. The default is `60m`.
|===

.Procedure

. To see what a pruning operation would delete, run the following command:
+
[source,terminal]
----
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m
----

. To actually perform the prune operation, add the `--confirm` flag:
+
[source,terminal]
----
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m --confirm
----

[NOTE]
====
Developers can enable automatic build pruning by modifying their build configuration.
====

[role="_additional-resources"]
.Additional resources
* Performing advanced builds -> Pruning builds

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images_{context}"]
= Automatically pruning images

[role="_abstract"]
To reclaim storage in the {product-registry} in OpenShift Container Platform and set how long the cluster keeps images, you can configure the automatic image pruner. You set the schedule, suspension, and retention options on the pruning custom resource (CR).

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with cluster administrator permissions.
* You have access to an OpenShift Container Platform cluster using an account with `dedicated-admin` permissions.
* Install the `oc` CLI.

[IMPORTANT]
====
The behavior of the Image Registry Operator for managing the pruner is independent to the `managementState` specified on the `ClusterOperator` object of the Image Registry Operator. If the Image Registry Operator is not in the `Managed` state, the image pruner can still be configured and managed by the Pruning Custom Resource.

However, the `managementState` of the Image Registry Operator alters the behavior of the deployed image pruner job:

* `Managed`: the `--prune-registry` flag for the image pruner is set to `true`.
* `Removed`: the `--prune-registry` flag for the image pruner is set to `false`, meaning it only prunes image metadata in etcd.
====

.Procedure

* Verify that the object named `imagepruners.imageregistry.operator.openshift.io/cluster` contains the following `spec` and `status` fields:
+
[source,yaml]
----
spec:
  schedule: 0 0 * * *
  suspend: false
  keepTagRevisions: 3
  keepYoungerThanDuration: 60m
  keepYoungerThan: 3600000000000
  resources: {}
  affinity: {}
  nodeSelector: {}
  tolerations: []
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 3
status:
  observedGeneration: 2
  conditions:
  - type: Available
    status: "True"
    lastTransitionTime: 2019-10-09T03:13:45
    reason: Ready
    message: "Periodic image pruner has been created."
  - type: Scheduled
    status: "True"
    lastTransitionTime: 2019-10-09T03:13:45
    reason: Scheduled
    message: "Image pruner job has been scheduled."
  - type: Failed
    staus: "False"
    lastTransitionTime: 2019-10-09T03:13:45
    reason: Succeeded
    message: "Most recent image pruning job succeeded."
----
* `schedule`: `CronJob` formatted schedule. This is an optional field, default is daily at midnight.
* `suspend`: If set to `true`, the `CronJob` running pruning is suspended. This is an optional field, default is `false`. The initial value on new clusters is `false`.
* `keepTagRevisions`: The number of revisions per tag to keep. This is an optional field, default is `3`. The initial value is `3`.
* `keepYoungerThanDuration`: Retain images younger than this duration. This is an optional field. If a value is not specified, either `keepYoungerThan` or the default value `60m` (60 minutes) is used.
* `keepYoungerThan`: Deprecated. The same as `keepYoungerThanDuration`, but the duration is specified as an integer in nanoseconds. This is an optional field. When `keepYoungerThanDuration` is set, this field is ignored.
* `resources`: Standard pod resource requests and limits. This is an optional field.
* `affinity`: Standard pod affinity. This is an optional field.
* `nodeSelector`: Standard pod node selector. This is an optional field.
* `tolerations`: Standard pod tolerations. This is an optional field.
* `successfulJobsHistoryLimit`: The maximum number of successful jobs to retain. Must be greater than or equal to `1` to ensure metrics are reported. This is an optional field, default is `3`. The initial value is `3`.
* `failedJobsHistoryLimit`: The maximum number of failed jobs to retain. Must be greater than or equal `1` to ensure metrics are reported. This is an optional field, default is `3`. The initial value is `3`.
* `observedGeneration`: The generation observed by the Operator.
* `conditions`: The standard condition objects with the following types:
** `Available`: Indicates if the pruning job has been created. Reasons can be `Ready` or `Error`.
** `Scheduled`: Indicates if the next pruning job has been scheduled. Reasons can be `Scheduled`, `Suspended`, or `Error`.
** `Failed`: Indicates if the most recent pruning job failed.

//cannot create resource "serviceaccounts". cannot create resource "cronjobs"

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-manual_{context}"]
= Manually pruning images

// out of scope for this PR - needs to be split into multiple modules, there shouldn't be multiple procedures in one module

The pruning custom resource enables automatic image pruning for the images from the {product-registry}. Administrators can manually prune images with the `oc adm prune images <image_prune_option>` command. For example:

[source,terminal]
----
$ oc adm prune images <image_prune_option> <1>
----
<1> For more information about available pruning options, see "Manual image pruning command options".

This command removes images that are no longer required by the system.

Depending on your needs, you can prune images based on their age and tag history, or prune images that cause a project to exceed its defined storage limits.

[id="considerations-pruning-images_{context}"]
== Considerations when pruning images

Consider the following information before manually pruning images:

* Pruning with the `--namespace` flag does not remove images. It only removes image streams, because images are cluster-scoped resources. Limiting pruning to a particular namespace makes it impossible to calculate current usage.

* By default, the integrated registry caches metadata of blobs to reduce the number of requests to storage, and to increase request-processing speed. Pruning does not update the integrated registry cache. Images that still contain pruned layers after pruning will be broken because the pruned layers that have metadata in the cache will not be pushed. Therefore, you must redeploy the registry to clear the cache after pruning:
+
[source,terminal]
----
$ oc rollout restart deployment/image-registry -n openshift-image-registry
----

* If the integrated registry uses a Redis cache, you must clean the database manually.

* If redeploying the registry after pruning is not an option, then you must permanently disable the cache.

* `oc adm prune images` operations require a route for your registry. Registry routes are not created by default.

[id="additional-pruning-limitations_{context}"]
== Limitations when pruning images

The following limitations apply when pruning an image:

* Pruning images from external registries is unsupported.

* When an image is pruned, all references to the image are removed from all image streams that contain the image in `status.tags`.

* Image layers that are no longer referenced by any images are removed.

//include::modules/pruning-images-job-cronjob.adoc[leveloffset=+2]
// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-conditions_{context}"]
= Image prune conditions

OpenShift Container Platform supports two methodologies for pruning images:

. Pruning by age and tag

. Pruning by size limit

These methodologies are mutually exclusive. You must choose whether to prune by age and tag, or by size limit. Regardless of the method that you choose, the image pruner checks to ensure that images in use are not removed.

An image is only pruned if it meets the primary condition *and* is not actively referenced by a system component.

[id="pruning-images-age-tag_{context}"]
== Pruning an image by age and tag

Pruning an image by age and tag is the default pruning strategy. It identifies images for removal by using the `--keep-younger-than` and `--keep-tag-revisions` flags. To prune an image by age and tag, the image must be older than the `--keep-younger-than` threshold, not one of the most recent tag revisions, and cannot be in use by an active workload.

For an image to be pruned by age and tag, *all* of the following conditions must be met:

. The image is managed by OpenShift Container Platform or has the `openshift.io/image.managed` annotation.

. The image is older than the time specified by the `--keep-younger-than` flag.

. The image is not one of the most recent images for its tag, as specified by the `--keep-tag-revisions` flag.

. The image is *not* currently referenced by any of the following active or recent API objects:
+
* Pods or image streams created more recently than the `--keep-younger-than` duration.
* Running or pending pods
* Deployments, replication controllers, replica sets, or stateful sets.
* Builds, build configurations, jobs, or cronjobs.

An image is only removed if it is old, not a recent tag revision, and is confirmed to have no active references by system components.

[id="pruning-images-size-limit_{context}"]
== Pruning an image by size limit

Pruning an image by size limit uses the `--prune-over-size-limit` flag. This method is used to bring a project back under its defined image storage limit.

[NOTE]
====
The `--prune-over-size-limit` flag cannot be combined with the `--keep-tag-revisions` flag nor the `--keep-younger-than` flags. Doing so returns information that this operation is not allowed.
====

For an image to be pruned using this method, all of the following conditions must be true:

. The image is part of a project that is currently exceeding its smallest defined size limit.

. The image is selected by the pruner as a candidate for deletion to reduce the total size.

. The image is not currently referenced by any of the following active API objects:
+
* Pods that are in a `running` or `pending` state.
* Deployments, replication controllers, replica sets, or stateful sets.
* Builds, build configurations, jobs, or cronjobs.

With this method, the primary trigger is the project's size, but the safety check to ensure that the image is not actively in use is still performed.

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-running-operation_{context}"]
= Running image prune operations

Use the following procedure to run an image prune operation

.Prerequisites

* You must be logged into the CLI with an access token.
* You must have the `system:image-pruner` cluster role or greater (for example, `cluster-admin`).
* The image registry must be exposed.
* You have reviewed the "Considerations when manually pruning images" section of this document.

.Procedure

. Optional: To preview which images would be pruned, enter the following command. This command prints a list of the images, image streams, and pods that would be removed. Note that nothing is deleted until you add the `--confirm` flag.
+
[source,terminal]
----
$ oc adm prune images <image_prune_option_one> <image_prune_option_two> <1>
----
<1> For more information about available pruning options, see "Manual image pruning command options".

. Review the output to confirm the list of images, image streams, and pods to be removed.

. Run the `oc adm prune images` command with the appropriate options for your cluster. Add the `--confirm` flag to confirm deletion. For example:
+
[source,terminal]
----
$ oc adm prune images <image_prune_option_one> <image_prune_option_two> --confirm
----

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-secure-insecure_{context}"]
= Using secure or insecure connections

The secure connection is the preferred and recommended approach. It is done over
HTTPS protocol with a mandatory certificate verification. The `prune` command
always attempts to use it if possible. If it is not possible, in some cases it
can fall-back to insecure connection, which is dangerous. In this case, either
certificate verification is skipped or plain HTTP protocol is used.

The fall-back to insecure connection is allowed in the following cases unless
`--certificate-authority` is specified:

. The `prune` command is run with the `--force-insecure` option.
. The provided `registry-url` is prefixed with the `http://` scheme.
. The provided `registry-url` is a local-link address or `localhost`.
. The configuration of the current user allows for an insecure connection. This
can be caused by the user either logging in using `--insecure-skip-tls-verify`
or choosing the insecure connection when prompted.

[IMPORTANT]
====
If the registry is secured by a certificate authority different from the one used by OpenShift Container Platform, it must be specified using the
`--certificate-authority` flag. Otherwise, the `prune` command fails with an error.
====

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-options_{context}"]
= Image pruning CLI options

The following table describes the options you can use with the `oc adm prune images <image_prune_option>` command.

.Manual image pruning command options
[cols="4,8",options="header"]
|===

|Option |Description

.^|`--all`
|Include images that were not pushed to the registry, but have been mirrored by
pullthrough. This is on by default. To limit the pruning to images that were
pushed to the integrated registry, pass `--all=false`.

.^|`--certificate-authority`
|The path to a certificate authority file to use when communicating with the
OpenShift Container Platform-managed registries. Defaults to the certificate authority data
from the current user's configuration file. If provided, a secure connection is
initiated.

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a test-run. This
requires a valid route to the integrated container image registry. If this
command is run outside of the cluster network, the route must be provided
using `--registry-url`.

.^|`--force-insecure`
|Use caution with this option. Allow an insecure connection to the container
registry that is hosted via HTTP or has an invalid HTTPS certificate.

.^|`--keep-tag-revisions=<N>`
|For each imagestream, keep up to at most `N` image revisions per tag (default
`3`).

.^|`--keep-younger-than=<duration>`
|Do not prune any image that is younger than `<duration>` relative to the
current time. Alternately, do not prune any image that is referenced by any other object that
is younger than `<duration>` relative to the current time (default `60m`).

.^|`--prune-over-size-limit`
|Prune each image that exceeds the smallest limit defined in the same project.
This flag cannot be combined with `--keep-tag-revisions` nor
`--keep-younger-than`.

.^|`--registry-url`
|The address to use when contacting the registry. The command attempts to use a
cluster-internal URL determined from managed images and image streams. In case
it fails (the registry cannot be resolved or reached), an alternative route that
works needs to be provided using this flag. The registry hostname can be
prefixed by `https://` or `http://`, which enforces particular connection
protocol.

.^|`--prune-registry`
|In conjunction with the conditions stipulated by the other options, this option
controls whether the data in the registry corresponding to the OpenShift Container Platform
image API object is pruned. By default, image pruning processes both the image
API objects and corresponding data in the registry.

This option is useful when you are only concerned with removing etcd content, to reduce the number of image objects but are not concerned with cleaning up registry storage, or if you intend to do that separately by hard pruning the registry during an appropriate maintenance window for the registry.
|===

[id="information-about-prune-registry-flag_{context}"]
== Additional information about the --prune-registry flag

You can separate the removal of OpenShift Container Platform image API objects from the removal of image data in the registry by passing in the `--prune-registry=false` flag. For example, the following command prunes only the API objects, leaving the registry storage untouched:

[source,terminal]
----
$ oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m --confirm --prune-registry=false
----

Then, you can perform a hard prune of the registry to remove the associated image data. This approach can narrow the timing window for race conditions compared to pruning both in a single command.

However, timing windows are not completely eliminated. For example, a pod might still be created that references an image while that image is being identified for pruning. You should track any API objects created during pruning to ensure that they do not reference deleted content.

Re-running the pruning without the `--prune-registry` option, or with `--prune-registry=true`, does not remove the associated registry storage for images previously pruned with `--prune-registry=false`. Those images can only be removed from registry storage by performing a hard prune of the registry. For more information, see "Hard pruning the registry".

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-images-troubleshooting_{context}"]
= Image pruning problems

[id="pruning-images-not-being-pruned_{context}"]
== Images not being pruned

If your images keep accumulating and the `prune` command removes just a small
portion of what you expect, ensure that you understand the image prune
conditions that must apply for an image to be considered a candidate for
pruning.

Ensure that images you want removed occur at higher positions in each tag
history than your chosen tag revisions threshold. For example, consider an old
and obsolete image named `sha256:abz`. By running the following command in your
namespace, where the image is tagged, the image is tagged three times in a
single image stream named `myapp`:

[source,terminal]
----
$ oc get is -n <namespace> -o go-template='{{range $isi, $is := .items}}{{range $ti, $tag := $is.status.tags}}'\
'{{range $ii, $item := $tag.items}}{{if eq $item.image "sha256:<hash>"}}{{$is.metadata.name}}:{{$tag.tag}} at position {{$ii}} out of {{len $tag.items}}\n'\
'{{end}}{{end}}{{end}}{{end}}'
----

.Example output
[source,terminal]
----
myapp:v2 at position 4 out of 5
myapp:v2.1 at position 2 out of 2
myapp:v2.1-may-2016 at position 0 out of 1
----

When default options are used, the image is never pruned because it occurs at
position `0` in a history of `myapp:v2.1-may-2016` tag. For an image to be
considered for pruning, the administrator must either:

* Specify `--keep-tag-revisions=0` with the `oc adm prune images` command.
+
[WARNING]
====
This action removes all the tags from all the namespaces with underlying images, unless they are younger or they are referenced by objects younger than the specified threshold.
====

* Delete all the `istags` where the position is below the revision threshold,
which means `myapp:v2.1` and `myapp:v2.1-may-2016`.

* Move the image further in the history, either by running new builds pushing to
the same `istag`, or by tagging other image. This is not always
desirable for old release tags.

Tags having a date or time of a particular image's build in their names should
be avoided, unless the image must be preserved for an undefined amount of time.
Such tags tend to have just one image in their history, which prevents
them from ever being pruned.

[id="pruning-images-secure-against-insecure_{context}"]
== Using a secure connection against insecure registry

If you see a message similar to the following in the output of the `oc adm prune images`
command, then your registry is not secured and the `oc adm prune images`
client attempts to use a secure connection:

[source,terminal]
----
error: error communicating with registry: Get https://172.30.30.30:5000/healthz: http: server gave HTTP response to HTTPS client
----

* The recommended solution is to secure the registry. Otherwise, you can force the
client to use an insecure connection by appending `--force-insecure`  to the
command; however, this is not recommended.

[id="pruning-images-insecure-against-secure_{context}"]
== Using an insecure connection against a secured registry

If you see one of the following errors in the output of the `oc adm prune images`
command, it means that your registry is secured using a certificate signed by a
certificate authority other than the one used by `oc adm prune images` client for
connection verification:

[source,terminal]
----
error: error communicating with registry: Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"
error: error communicating with registry: [Get https://172.30.30.30:5000/healthz: x509: certificate signed by unknown authority, Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"]
----

By default, the certificate authority data stored in the user's configuration files is used; the same is true for communication with the master API.

Use the `--certificate-authority` option to provide the right certificate authority for the container image registry server.

[id="pruning-images-wrong-ca_{context}"]
== Using the wrong certificate authority

The following error means that the certificate authority used to sign the certificate of the secured container image registry is different from the authority used by the client:

[source,terminal]
----
error: error communicating with registry: Get https://172.30.30.30:5000/: x509: certificate signed by unknown authority
----

Make sure to provide the right one with the flag `--certificate-authority`.

As a workaround, the `--force-insecure` flag can be added instead. However, this is not recommended.

[role="_additional-resources"]
.Additional resources
* Accessing the registry
* Exposing the registry
* See
Image
Registry Operator in OpenShift Container Platform for information on how to create a
registry route.

// cannot patch resource "configs"

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-hard-pruning-registry_{context}"]
= Hard pruning the registry

The OpenShift Container Registry can accumulate blobs that are not referenced by
the OpenShift Container Platform cluster's etcd. The basic pruning images procedure,
therefore, is unable to operate on them. These are called _orphaned blobs_.

Orphaned blobs can occur from the following scenarios:

- Manually deleting an image with `oc delete image <sha256:image-id>` command,
which only removes the image from etcd, but not from the registry's storage.

- Pushing to the registry initiated by daemon failures, which causes some blobs to
get uploaded, but the image manifest (which is uploaded as the very last
component) does not. All unique image blobs become orphans.

- OpenShift Container Platform refusing an image because of quota restrictions.

- The standard image pruner deleting an image manifest, but is interrupted before
it deletes the related blobs.

- A bug in the registry pruner, which fails to remove the intended blobs, causing
the image objects referencing them to be removed and the blobs becoming orphans.
// Find this BZ

_Hard pruning_ the registry, a separate procedure from basic image pruning,
allows cluster administrators to remove orphaned blobs. You should hard prune if
you are running out of storage space in your OpenShift Container Registry and
believe you have orphaned blobs.

This should be an infrequent operation and is necessary only when you have
evidence that significant numbers of new orphans have been created. Otherwise,
you can perform standard image pruning at regular intervals, for example, once a
day (depending on the number of images being created).

.Procedure

To hard prune orphaned blobs from the registry:

. *Log in.*
+
Log in to the cluster with the CLI as `kubeadmin` or another privileged user that
has access to the `openshift-image-registry` namespace.

. *Run a basic image prune*.
+
Basic image pruning removes additional images that are no longer needed. The
hard prune does not remove images on its own. It only removes blobs stored in
the registry storage. Therefore, you should run this just before the hard prune.

. *Switch the registry to read-only mode.*
+
If the registry is not running in read-only mode, any pushes happening at the
same time as the prune will either:
+
--
- fail and cause new orphans, or
- succeed although the images cannot be pulled (because some of the
referenced blobs were deleted).
--
+
Pushes will not succeed until the registry is switched back to read-write mode.
Therefore, the hard prune must be carefully scheduled.
+
To switch the registry to read-only mode:

.. In `configs.imageregistry.operator.openshift.io/cluster`, set `spec.readOnly` to `true`:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io/cluster -p '{"spec":{"readOnly":true}}' --type=merge
----

. *Add the `system:image-pruner` role.*
+
The service account used to run the registry instances requires additional
permissions to list some resources.

.. Get the service account name:
+
[source,terminal]
----
$ service_account=$(oc get -n openshift-image-registry \
    -o jsonpath='{.spec.template.spec.serviceAccountName}' deploy/image-registry)
----

.. Add the `system:image-pruner` cluster role to the service account:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user \
    system:image-pruner -z \
    ${service_account} -n openshift-image-registry
----

. *Optional: Run the pruner in dry-run mode.*
+
To see how many blobs would be removed, run the hard pruner in dry-run mode. No changes are actually made. The following example references an image registry pod called `image-registry-3-vhndw`:
+
[source,terminal]
----
$ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c '/usr/bin/dockerregistry -prune=check'
----
+
Alternatively, to get the exact paths for the prune candidates, increase the
logging level:
+
[source,terminal]
----
$ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c 'REGISTRY_LOG_LEVEL=info /usr/bin/dockerregistry -prune=check'
----
+
.Example output
[source,terminal]
----
time="2017-06-22T11:50:25.066156047Z" level=info msg="start prune (dry-run mode)" distribution_version="v2.4.1+unknown" kubernetes_version=v1.6.1+$Format:%h$ openshift_version=unknown
time="2017-06-22T11:50:25.092257421Z" level=info msg="Would delete blob: sha256:00043a2a5e384f6b59ab17e2c3d3a3d0a7de01b2cabeb606243e468acc663fa5" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
time="2017-06-22T11:50:25.092395621Z" level=info msg="Would delete blob: sha256:0022d49612807cb348cabc562c072ef34d756adfe0100a61952cbcb87ee6578a" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
time="2017-06-22T11:50:25.092492183Z" level=info msg="Would delete blob: sha256:0029dd4228961086707e53b881e25eba0564fa80033fbbb2e27847a28d16a37c" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
time="2017-06-22T11:50:26.673946639Z" level=info msg="Would delete blob: sha256:ff7664dfc213d6cc60fd5c5f5bb00a7bf4a687e18e1df12d349a1d07b2cf7663" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
time="2017-06-22T11:50:26.674024531Z" level=info msg="Would delete blob: sha256:ff7a933178ccd931f4b5f40f9f19a65be5eeeec207e4fad2a5bafd28afbef57e" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
time="2017-06-22T11:50:26.674675469Z" level=info msg="Would delete blob: sha256:ff9b8956794b426cc80bb49a604a0b24a1553aae96b930c6919a6675db3d5e06" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
...
Would delete 13374 blobs
Would free up 2.835 GiB of disk space
Use -prune=delete to actually delete the data
----

. *Run the hard prune.*
+
Execute the following command inside one running instance of a `image-registry` pod to run the hard prune. The following example references an image registry pod called `image-registry-3-vhndw`:
+
[source,terminal]
----
$ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c '/usr/bin/dockerregistry -prune=delete'
----
+
.Example output
[source,terminal]
----
Deleted 13374 blobs
Freed up 2.835 GiB of disk space
----

. *Switch the registry back to read-write mode.*
+
After the prune is finished, the registry can be switched back to read-write
mode. In `configs.imageregistry.operator.openshift.io/cluster`, set
`spec.readOnly` to `false`:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io/cluster -p '{"spec":{"readOnly":false}}' --type=merge
----

// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-cronjobs_{context}"]
= Pruning cron jobs

Cron jobs can perform pruning of successful jobs, but might not properly handle
failed jobs. Therefore, the cluster administrator should perform regular cleanup of
jobs manually. They should also restrict the access to cron jobs to a small
group of trusted users and set appropriate quota to prevent the cron job from
creating too many jobs and pods.

[role="_additional-resources"]
.Additional resources
// When the Operators book is added to ROSA/OSD, check if this link is valid.
* Running tasks in pods using jobs
* Resource quotas across multiple projects
// When the Operators book is added to ROSA/OSD, check if this link is valid.
* Using RBAC to define and apply permissions
