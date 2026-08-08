---
title: "Triggering updates on image stream changes"
type: reference
domain: openshift
slug: openshift-images-4-22-triggering-updates-on-imagestream-changes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/triggering-updates-on-imagestream-changes
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Triggering updates on image stream changes

[id="triggering-updates-on-imagestream-changes"]
= Triggering updates on image stream changes

[role="_abstract"]
When image stream tags update in OpenShift Container Platform, the platform automatically rolls out new images to deployments and builds that reference those tags. You configure this automatic triggering behavior differently depending on the type of resource that uses the image stream.

[id="openshift-resources"]
== Resources

OpenShift Container Platform `DeploymentConfig` and `BuildConfig` resources can be automatically triggered by changes to image stream tags. When triggered, these resources use the new image value referenced by the updated image stream tag.

// Module included in the following assemblies:
//
// * openshift_images/triggering-updates-on-imagestream-changes.adoc

[id="images-triggering-updates-imagestream-changes-kubernetes-about_{context}"]
= Triggering Kubernetes resources

[role="_abstract"]
To enable Kubernetes resources, such as `Deployments` and `StatefulSets`, to seamlessly consume new image versions, configure image stream change triggers in OpenShift Container Platform. This ensures your application deployments are automatically updated when the associated image stream detects a change.

Kubernetes resources do not have fields for triggering, unlike deployment and build configurations, which include as part of their API definition a set of fields for controlling triggers. Instead, you can use annotations in OpenShift Container Platform to request triggering.

The annotation is defined as follows:

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    image.openshift.io/triggers:
      [
       {
         "from": {
           "kind": "ImageStreamTag",
           "name": "example:latest",
           "namespace": "myapp"
         },
         "fieldPath": "spec.template.spec.containers[?(@.name==\"web\")].image",
         "paused": false
       },
      # ...
      ]
# ...
----
where:

`kind`:: Specifies the resource to trigger from, and must have the value `ImageStreamTag`.
`name`:: Specifies the name of an image stream tag.
`namespace`:: Specifies the namespace of the object. This field is optional.
`fieldPath`:: Specifies the JSON path to change. This field is limited and accepts only a JSON path expression that precisely matches a container by ID or index. For pods, the JSON path is `spec.containers[?(@.name='web')].image`.
`paused`:: Specifies whether or not the trigger is paused. This field is optional, and defaults to the value `false`. Set the value to `true` to temporarily disable this trigger.

When one of the core Kubernetes resources contains both a pod template and this annotation, OpenShift Container Platform attempts to update the object by using the image currently associated with the image stream tag that is referenced by trigger. The update is performed against the `fieldPath` specified.

Examples of core Kubernetes resources that can contain both a pod template and annotation include:

* `CronJobs`
* `Deployments`
* `StatefulSets`
* `DaemonSets`
* `Jobs`
* `ReplicationControllers`
* `Pods`

// Module included in the following assemblies:
//
// * openshift_images/triggering-updates-on-imagestream-changes.adoc

[id="images-triggering-updates-imagestream-changes-kubernetes-cli_{context}"]
= Setting the image trigger on Kubernetes resources

[role="_abstract"]
To enable automatic updates for your deployed applications managed by Kubernetes, use the command-line interface (CLI) to set an image stream change trigger on Kubernetes resources. This ensures that resources, like `Deployments` and `StatefulSets`, are automatically invoked when a new version of an upstream image is available.

When adding an image trigger to deployments, you can use the `oc set triggers` command. For example, the sample command in this procedure adds an image change trigger to the deployment named `example` so that when the `example:latest` image stream tag is updated, the `web` container inside the deployment updates with the new image value. This command sets the correct `image.openshift.io/triggers` annotation on the deployment resource.

.Procedure

* Trigger Kubernetes resources by entering the `oc set triggers` command:
+
[source,terminal]
----
$ oc set triggers deploy/example --from-image=example:latest -c web
----
+
.Example deployment with trigger annotation
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    image.openshift.io/triggers: '[{"from":{"kind":"ImageStreamTag","name":"example:latest"},"fieldPath":"spec.template.spec.containers[?(@.name==\"container\")].image"}]'
# ...
----
+
Unless the deployment is paused, this pod template update automatically causes a deployment to occur with the new image value.
