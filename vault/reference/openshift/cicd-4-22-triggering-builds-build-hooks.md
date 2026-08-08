---
title: "Triggering and modifying builds"
type: reference
domain: openshift
slug: cicd-4-22-triggering-builds-build-hooks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/triggering-builds-build-hooks
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Triggering and modifying builds

[id="triggering-builds-build-hooks"]
= Triggering and modifying builds

The following sections outline how to trigger builds and modify builds using build hooks.

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-triggers_{context}"]
= Build triggers

When defining a `BuildConfig`, you can define triggers to control the circumstances in which the `BuildConfig` should be run. The following build triggers are available:

* Webhook
* Image change
* Configuration change

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-webhook-triggers_{context}"]
= Webhook triggers

Webhook triggers allow you to trigger a new build by sending a request to the OpenShift Container Platform API endpoint. You can define these triggers using GitHub, GitLab, Bitbucket, or Generic webhooks.

Currently, OpenShift Container Platform webhooks only support the analogous versions of the push event for each of the Git-based Source Code Management (SCM) systems. All other event types are ignored.

When the push events are processed, the OpenShift Container Platform control plane host confirms if the branch reference inside the event matches the branch reference in the corresponding `BuildConfig`. If so, it then checks out the exact commit reference noted in the webhook event on the OpenShift Container Platform build. If they do not match, no build is triggered.

[NOTE]
====
`oc new-app` and `oc new-build` create GitHub and Generic webhook triggers automatically, but any other needed webhook triggers must be added manually. You can manually add triggers by setting triggers.
====

For all webhooks, you must define a secret with a key named `WebHookSecretKey` and the value being the value to be supplied when invoking the webhook. The webhook definition must then reference the secret. The secret ensures the uniqueness of the URL, preventing others from triggering the build. The value of the key is compared to the secret provided during the webhook invocation.

For example here is a GitHub webhook with a reference to a secret named `mysecret`:

[source,yaml]
----
type: "GitHub"
github:
  secretReference:
    name: "mysecret"
----

The secret is then defined as follows. Note that the value of the secret is base64 encoded as is required for any `data` field of a `Secret` object.

[source,yaml]
----
- kind: Secret
  apiVersion: v1
  metadata:
    name: mysecret
    creationTimestamp:
  data:
    WebHookSecretKey: c2VjcmV0dmFsdWUx
----

// Module included in the following assemblies:
//
// * cicd/builds/triggering-builds-build-hooks.adoc

[id="unauthenticated-users-system-webhook_{context}"]
= Adding unauthenticated users to the system:webhook role binding

As a cluster administrator, you can add unauthenticated users to the `system:webhook` role binding in OpenShift Container Platform for specific namespaces. The `system:webhook` role binding allows users to trigger builds from external systems that do not use
an OpenShift Container Platform
a OpenShift Container Platform
authentication mechanism. Unauthenticated users do not have access to non-public role bindings by default. This is a change from OpenShift Container Platform versions before 4.16.

Adding unauthenticated users to the `system:webhook` role binding is required to successfully trigger builds from GitHub, GitLab, and Bitbucket.

If it is necessary to allow unauthenticated users access to a cluster, you can do so by adding unauthenticated users to the `system:webhook` role binding in each required namespace. This method is more secure than adding unauthenticated users to the `system:webhook` cluster role binding. However, if you have a large number of namespaces, it is possible to add unauthenticated users to the `system:webhook` cluster role binding which would apply the change to all namespaces.

[IMPORTANT]
====
Always verify compliance with your organization's security standards when modifying unauthenticated access.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file named `add-webhooks-unauth.yaml` and add the following content:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  name: webhook-access-unauthenticated
  namespace: <namespace> <1>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: "system:webhook"
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    name: "system:unauthenticated"
----
<1> The namespace of your `BuildConfig`.

. Apply the configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f add-webhooks-unauth.yaml
----

// Preventing cluster failure due to webhooks
// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="third-party-cluster-webhook-failure_{context}"]
= Prevent cluster failure due to webhooks

[role="_abstract"]
To prevent potential cluster failure and ensure pods can always start, you must configure third-party admission webhooks to exclude infrastructure namespaces. Implementing specific selectors and adopting a `ValidatingAdmissionPolicy` resource provides a more stable environment for cluster recovery and management.

When possible, use a `ValidatingAdmissionPolicy` resource instead of an admission webhook. It does not require an external service, has no timeout limitations, and cannot cause cluster-wide failures.

If you use admission webhooks take the following precautions:

* Configure the webhook to exclude OpenShift Container Platform and Kubernetes infrastructure namespaces.

* Configure webhook timeouts to 10 seconds or less to provide a safety buffer for the system-enforced 13-second limit.

* Set the `failurePolicy` value to `Ignore` for non-critical webhooks so that requests can proceed if the webhook is unavailable.

// Recovering an unstable cluster due to admission webhooks
// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="third-party-cluster-webhook-failures_{context}"]
= Recovering an unstable cluster due to admission webhooks

[role="_abstract"]
If a misconfigured admission webhook causes your cluster to fail, you must delete the webhook configuration to restore functionality.

.Procedure

. Back up the webhook configuration. Choose either `ValidatingWebhookConfiguration` or `MutatingWebhookConfiguration` for the `<webhook_configuration>` value.
+
[source,terminal]
----
oc get <webhook_configuration> <webhook_name> -o yaml > webhook-backup.yaml
----

. Delete the webhook.
+
[source,terminal]
----
oc delete <webhook_configuration> <webhook_name>
----

. Fix the webhook configuration to exclude infrastructure namespaces when you reapply it.
+
.Example
[source,yaml]
----
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: machine-api
webhooks:
  - name: default.machine.machine.openshift.io
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE", "UPDATE"]
        resources: ["pods"]
        scope: "*"
    clientConfig:
      service:
        namespace: machine-api-operator-webhook
        name: openshift-machine-api
        path: "/validate"
    admissionReviewVersions: ["v1"]
    sideEffects: None
    timeoutSeconds: 5
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values:
            - openshift
            - openshift-apiserver
            - openshift-authentication
            - openshift-monitoring
            - kube-system
            - kube-public
            - kube-node-lease
            - default
----
+
Where `kind` is the type of webhook configuration you are using. Valid values are `ValidatingWebhookConfiguration` or `MutatingWebhookConfiguration`.

[role="_additional-resources"]
.Additional resources

* Cluster role bindings for unauthenticated groups

* Webhook admission plugins

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-github-webhooks_{context}"]
= Using GitHub webhooks

GitHub webhooks handle the call made by GitHub when a repository is updated. When defining the trigger, you must specify a secret, which is part of the URL you supply to GitHub when configuring the webhook.

Example GitHub webhook definition:

[source,yaml]
----
type: "GitHub"
github:
  secretReference:
    name: "mysecret"
----

[NOTE]
====
The secret used in the webhook trigger configuration is not the same as the `secret` field you encounter when configuring webhook in GitHub UI. The secret in the webhook trigger configuration makes the webhook URL unique and hard to predict. The secret configured in the GitHub UI is an optional string field that is used to create an HMAC hex digest of the body, which is sent as an `X-Hub-Signature` header.
====

The payload URL is returned as the GitHub Webhook URL by the `oc describe`
command (see Displaying Webhook URLs), and is structured as follows:

.Example output
[source,terminal]
----
https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/github
----

.Prerequisites

* Create a `BuildConfig` from a GitHub repository.
* `system:unauthenticated` has access to the `system:webhook` role in the required namespaces. Or, `system:unauthenticated` has access to the `system:webhook` cluster role.

.Procedure

. Configure a GitHub Webhook.

.. After creating a `BuildConfig` object from a GitHub repository, run the following command:
+
[source,terminal]
----
$ oc describe bc/<name_of_your_BuildConfig>
----
+
This command generates a webhook GitHub URL.
+
.Example output
[source,terminal]
----
https://api.starter-us-east-1.openshift.com:443/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/github
----

.. Cut and paste this URL into GitHub, from the GitHub web console.

.. In your GitHub repository, select *Add Webhook* from *Settings -> Webhooks*.

.. Paste the URL output into the *Payload URL* field.

.. Change the *Content Type* from GitHub's default `application/x-www-form-urlencoded` to `application/json`.

.. Click *Add webhook*.
+
You should see a message from GitHub stating that your webhook was successfully configured.
+
Now, when you push a change to your GitHub repository, a new build automatically starts, and upon a successful build a new deployment starts.
+
[NOTE]
====
Gogs supports the same webhook payload format as GitHub. Therefore, if you are using a Gogs server, you can define a GitHub webhook trigger on your `BuildConfig` and trigger it by your Gogs server as well.
====

. Given a file containing a valid JSON payload, such as `payload.json`, you can manually trigger the webhook with the following `curl` command:
+
[source,terminal]
----
$ curl -H "X-GitHub-Event: push" -H "Content-Type: application/json" -k -X POST --data-binary @payload.json https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/github
----
+
The `-k` argument is only necessary if your API server does not have a properly
signed certificate.

[NOTE]
====
The build will only be triggered if the `ref` value from GitHub webhook event matches the `ref` value specified in the `source.git` field of the `BuildConfig` resource.
====

[role="_additional-resources"]
.Additional resources

//* GitHub
* Gogs

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-gitlab-webhooks_{context}"]
= Using GitLab webhooks

GitLab webhooks handle the call made by GitLab when a repository is updated. As with the GitHub triggers, you must specify a secret. The following example is a trigger definition YAML within the `BuildConfig`:

[source,yaml]
----
type: "GitLab"
gitlab:
  secretReference:
    name: "mysecret"
----

The payload URL is returned as the GitLab Webhook URL by the `oc describe` command, and is structured as follows:

.Example output
[source,terminal]
----
https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/gitlab
----

.Prerequisites

* `system:unauthenticated` has access to the `system:webhook` role in the required namespaces. Or, `system:unauthenticated` has access to the `system:webhook` cluster role.

.Procedure

. Configure a GitLab Webhook.

.. Get the webhook URL by entering the following command:
+
[source,terminal]
----
$ oc describe bc <name>
----

.. Copy the webhook URL, replacing `<secret>` with your secret value.

.. Follow the GitLab setup instructions
to paste the webhook URL into your GitLab repository settings.

. Given a file containing a valid JSON payload, such as `payload.json`, you can
manually trigger the webhook with the following `curl` command:
+
[source,terminal]
----
$ curl -H "X-GitLab-Event: Push Hook" -H "Content-Type: application/json" -k -X POST --data-binary @payload.json https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/gitlab
----
+
The `-k` argument is only necessary if your API server does not have a properly
signed certificate.

[role="_additional-resources"]
.Additional resources
//* GitLab

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-bitbucket-webhooks_{context}"]
= Using Bitbucket webhooks

Bitbucket webhooks handle the call made by Bitbucket when a repository is updated. Similar to GitHub and GitLab triggers, you must specify a secret. The following example is a trigger definition YAML within the `BuildConfig`:

[source,yaml]
----
type: "Bitbucket"
bitbucket:
  secretReference:
    name: "mysecret"
----

The payload URL is returned as the Bitbucket Webhook URL by the `oc describe` command, and is structured as follows:

.Example output
[source,terminal]
----
https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/bitbucket
----

.Prerequisites

* `system:unauthenticated` has access to the `system:webhook` role in the required namespaces. Or, `system:unauthenticated` has access to the `system:webhook` cluster role.

.Procedure

. Configure a Bitbucket Webhook.

.. Get the webhook URL by entering the following command:
+
[source,terminal]
----
$ oc describe bc <name>
----

.. Copy the webhook URL, replacing `<secret>` with your secret value.

.. Follow the Bitbucket setup instructions to paste the webhook URL into your Bitbucket repository settings.

. Given a file containing a valid JSON payload, such as `payload.json`, you can
manually trigger the webhook by entering the following `curl` command:
+
[source,terminal]
----
$ curl -H "X-Event-Key: repo:push" -H "Content-Type: application/json" -k -X POST --data-binary @payload.json https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/bitbucket
----
+
The `-k` argument is only necessary if your API server does not have a properly signed certificate.

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-generic-webhooks_{context}"]
= Using generic webhooks

Generic webhooks are called from any system capable of making a web request. As with the other webhooks, you must specify a secret, which is part of the URL that the caller must use to trigger the build. The secret ensures the uniqueness of the URL, preventing others from triggering the build. The following is an example trigger definition YAML within the `BuildConfig`:

[source,yaml]
----
type: "Generic"
generic:
  secretReference:
    name: "mysecret"
  allowEnv: true # <1>
----
<1> Set to `true` to allow a generic webhook to pass in environment variables.

.Procedure

. To set up the caller, supply the calling system with the URL of the generic
webhook endpoint for your build.
+
.Example generic webhook endpoint URL
[source]
----
https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/generic
----
+
The caller must call the webhook as a `POST` operation.

. To call the webhook manually, enter the following `curl` command:
+
[source,terminal]
----
$ curl -X POST -k https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/generic
----
+
The HTTP verb must be set to `POST`. The insecure `-k` flag is specified to ignore certificate validation. This second flag is not necessary if your cluster has properly signed certificates.
+
The endpoint can accept an optional payload with the following format:
+
[source,yaml]
----
git:
  uri: "<url to git repository>"
  ref: "<optional git reference>"
  commit: "<commit hash identifying a specific git commit>"
  author:
    name: "<author name>"
    email: "<author e-mail>"
  committer:
    name: "<committer name>"
    email: "<committer e-mail>"
  message: "<commit message>"
env: <1>
   - name: "<variable name>"
     value: "<variable value>"
----
<1> Similar to the `BuildConfig` environment variables, the environment variables defined here are made available to your build. If these variables collide with the `BuildConfig` environment variables, these variables take precedence. By default, environment variables passed by webhook are ignored. Set the `allowEnv` field to `true` on the webhook definition to enable this behavior.

. To pass this payload using `curl`, define it in a file named `payload_file.yaml` and run the following command:
+
[source,terminal]
----
$ curl -H "Content-Type: application/yaml" --data-binary @payload_file.yaml -X POST -k https://<openshift_api_host:port>/apis/build.openshift.io/v1/namespaces/<namespace>/buildconfigs/<name>/webhooks/<secret>/generic
----
+
The arguments are the same as the previous example with the addition of a header and a payload. The `-H` argument sets the `Content-Type` header to `application/yaml` or `application/json` depending on your payload format. The `--data-binary` argument is used to send a binary payload with newlines intact with the `POST` request.

[NOTE]
====
OpenShift Container Platform permits builds to be triggered by the generic webhook even if an invalid request payload is presented, for example, invalid content type, unparsable or invalid content, and so on. This behavior is maintained for backwards compatibility. If an invalid request payload is presented, OpenShift Container Platform returns a warning in JSON format as part of its `HTTP 200 OK` response.
====

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-displaying-webhook-urls_{context}"]
= Displaying webhook URLs

You can use the `oc describe` command to display webhook URLs associated with a build configuration. If the command does not display any webhook URLs, then no webhook trigger is currently defined for that build configuration.

.Procedure

* To display any webhook URLs associated with a `BuildConfig`, run the following command:

[source,terminal]
----
$ oc describe bc <name>
----

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-image-change-triggers_{context}"]
= Using image change triggers

As a developer, you can configure your build to run automatically every time a base image changes.

You can use image change triggers to automatically invoke your build when a new version of an upstream image is available. For example, if a build is based on a RHEL image, you can trigger that build to run any time the RHEL image changes. As a result, the application image is always running on the latest RHEL base image.

[NOTE]
====
Image streams that point to container images in v1 container registries only trigger a build once when the image stream tag becomes available and not on subsequent image updates. This is due to the lack of uniquely identifiable images in v1 container registries.
====

.Procedure

. Define an `ImageStream` that points to the upstream image you want to use as a trigger:
+
[source,yaml]
----
kind: "ImageStream"
apiVersion: "v1"
metadata:
  name: "ruby-20-centos7"
----
+
This defines the image stream that is tied to a container image repository located at `_<system-registry>_/_<namespace>_/ruby-20-centos7`. The `<system-registry>` is defined as a service with the name `docker-registry` running in OpenShift Container Platform.

. If an image stream is the base image for the build, set the `from` field in the build strategy to point to the `ImageStream`:
+
[source,yaml]
----
strategy:
  sourceStrategy:
    from:
      kind: "ImageStreamTag"
      name: "ruby-20-centos7:latest"
----
+
In this case, the `sourceStrategy` definition is consuming the `latest` tag of the image stream named `ruby-20-centos7` located within this namespace.

. Define a build with one or more triggers that point to `ImageStreams`:
+
[source,yaml]
----
type: "ImageChange" <1>
imageChange: {}
type: "ImageChange" <2>
imageChange:
  from:
    kind: "ImageStreamTag"
    name: "custom-image:latest"
----
<1> An image change trigger that monitors the `ImageStream` and `Tag` as defined by the build strategy's `from` field. The `imageChange` object here must be empty.
<2> An image change trigger that monitors an arbitrary image stream. The `imageChange` part, in this case, must include a `from` field that references the `ImageStreamTag` to monitor.

When using an image change trigger for the strategy image stream, the generated build is supplied with an immutable docker tag that points to the latest image corresponding to that tag. This new image reference is used by the strategy when it executes for the build.

For other image change triggers that do not reference the strategy image stream, a new build is started, but the build strategy is not updated with a unique image reference.

Since this example has an image change trigger for the strategy, the resulting build is:

[source,yaml]
----
strategy:
  sourceStrategy:
    from:
      kind: "DockerImage"
      name: "172.30.17.3:5001/mynamespace/ruby-20-centos7:<immutableid>"
----

This ensures that the triggered build uses the new image that was just pushed to the repository, and the build can be re-run any time with the same inputs.

You can pause an image change trigger to allow multiple changes on the referenced image stream before a build is started. You can also set the `paused` attribute to true when initially adding an `ImageChangeTrigger` to a `BuildConfig` to prevent a build from being immediately triggered.

[source,yaml]
----
type: "ImageChange"
imageChange:
  from:
    kind: "ImageStreamTag"
    name: "custom-image:latest"
  paused: true
----

In addition to setting the image field for all `Strategy` types, for custom builds, the `OPENSHIFT_CUSTOM_BUILD_BASE_IMAGE` environment variable is checked.
If it does not exist, then it is created with the immutable image reference. If it does exist, then it is updated with the immutable image reference.

If a build is triggered due to a webhook trigger or manual request, the build that is created uses the `<immutableid>` resolved from the `ImageStream` referenced by the `Strategy`. This ensures that builds are performed using consistent image tags for ease of reproduction.

[role="_additional-resources"]
.Additional resources

* v1 container registries

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-image-change-trigger-identification_{context}"]
= Identifying the image change trigger of a build

As a developer, if you have image change triggers, you can identify which image change initiated the last build. This can be useful for debugging or troubleshooting builds.

.Example `BuildConfig`
[source,yaml]
----
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: bc-ict-example
  namespace: bc-ict-example-namespace
spec:

# ...

  triggers:
  - imageChange:
      from:
        kind: ImageStreamTag
        name: input:latest
        namespace: bc-ict-example-namespace
  - imageChange:
      from:
        kind: ImageStreamTag
        name: input2:latest
        namespace: bc-ict-example-namespace
    type: ImageChange
status:
  imageChangeTriggers:
  - from:
      name: input:latest
      namespace: bc-ict-example-namespace
    lastTriggerTime: "2021-06-30T13:47:53Z"
    lastTriggeredImageID: image-registry.openshift-image-registry.svc:5000/bc-ict-example-namespace/input@sha256:0f88ffbeb9d25525720bfa3524cb1bf0908b7f791057cf1acfae917b11266a69
  - from:
      name: input2:latest
      namespace: bc-ict-example-namespace
    lastTriggeredImageID:  image-registry.openshift-image-registry.svc:5000/bc-ict-example-namespace/input2@sha256:0f88ffbeb9d25525720bfa3524cb2ce0908b7f791057cf1acfae917b11266a69

  lastVersion: 1
----

[NOTE]
====
This example omits elements that are not related to image change triggers.
====

.Prerequisites

* You have configured multiple image change triggers. These triggers have triggered one or more builds.

.Procedure

. In the `BuildConfig` CR, in `status.imageChangeTriggers`, identify the `lastTriggerTime` that has the latest timestamp.
+
This `ImageChangeTriggerStatus`

 Then you use the `name` and `namespace` from that build to find the corresponding image change trigger in `buildConfig.spec.triggers`.

. Under `imageChangeTriggers`, compare  timestamps to identify the latest

.Image change triggers

In your build configuration, `buildConfig.spec.triggers` is an array of build trigger policies, `BuildTriggerPolicy`.

Each `BuildTriggerPolicy` has a `type` field and set of pointers fields. Each pointer field corresponds to one of the allowed values for the `type` field. As such, you can only set `BuildTriggerPolicy` to only one pointer field.

For image change triggers, the value of `type` is `ImageChange`. Then, the `imageChange` field is the pointer to an `ImageChangeTrigger` object, which has the following fields:

* `lastTriggeredImageID`: This field, which is not shown in the example, is deprecated in OpenShift Container Platform 4.8 and will be ignored in a future release. It contains the resolved image reference for the `ImageStreamTag` when the last build was triggered from this `BuildConfig`.
* `paused`: You can use this field, which is not shown in the example, to temporarily disable this particular image change trigger.
* `from`: Use this field to reference the `ImageStreamTag` that drives this image change trigger. Its type is the core Kubernetes type, `OwnerReference`.

The `from` field has the following fields of note:

* `kind`: For image change triggers, the only supported value is `ImageStreamTag`.
* `namespace`: Use this field to specify the namespace of the `ImageStreamTag`.
* `name`: Use this field to specify the `ImageStreamTag`.

.Image change trigger status

In your build configuration, `buildConfig.status.imageChangeTriggers` is an array of `ImageChangeTriggerStatus` elements. Each `ImageChangeTriggerStatus` element includes the `from`, `lastTriggeredImageID`, and `lastTriggerTime` elements shown in the preceding example.

The `ImageChangeTriggerStatus` that has the most recent `lastTriggerTime` triggered the most recent build. You use its `name` and `namespace` to identify the image change trigger in `buildConfig.spec.triggers` that triggered the build.

The `lastTriggerTime` with the most recent timestamp signifies the `ImageChangeTriggerStatus` of the last build. This `ImageChangeTriggerStatus` has the same `name` and `namespace` as the image change trigger in `buildConfig.spec.triggers` that triggered the build.

[role="_additional-resources"]
.Additional resources

* v1 container registries

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-configuration-change-triggers_{context}"]
= Configuration change triggers

A configuration change trigger allows a build to be automatically invoked as soon as a new `BuildConfig` is created.

The following is an example trigger definition YAML within the `BuildConfig`:

[source,yaml]
----
  type: "ConfigChange"
----

[NOTE]
====
Configuration change triggers currently only work when creating a new `BuildConfig`. In a future release, configuration change triggers will also be able to launch a build whenever a `BuildConfig` is updated.
====

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-setting-triggers-manually_{context}"]
= Setting triggers manually

Triggers can be added to and removed from build configurations with `oc set triggers`.

.Procedure

* To set a GitHub webhook trigger on a build configuration, enter the following command:
+
[source,terminal]
----
$ oc set triggers bc <name> --from-github
----

* To set an image change trigger, enter the following command:
+
[source,terminal]
----
$ oc set triggers bc <name> --from-image='<image>'
----

* To remove a trigger, enter the following command:
+
[source,terminal]
----
$ oc set triggers bc <name> --from-bitbucket --remove
----

[NOTE]
====
When a webhook trigger already exists, adding it again regenerates the webhook secret.
====

For more information, consult the help documentation by entering the following command:

[source,terminal]
----
$ oc set triggers --help
----

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-build-hooks_{context}"]
= Build hooks

Build hooks allow behavior to be injected into the build process.

The `postCommit` field of a `BuildConfig` object runs commands inside a temporary container that is running the build output image. The hook is run immediately after the last layer of the image has been committed and before the image is pushed to a registry.

The current working directory is set to the image's `WORKDIR`, which is the default working directory of the container image. For most images, this is where the source code is located.

The hook fails if the script or command returns a non-zero exit code or if starting the temporary container fails. When the hook fails it marks the build as failed and the image is not pushed to a registry. The reason for failing can be inspected by looking at the build logs.

Build hooks can be used to run unit tests to verify the image before the build is marked complete and the image is made available in a registry. If all tests pass and the test runner returns with exit code `0`, the build is marked successful. In case of any test failure, the build is marked as failed. In all cases, the build log contains the output of the test runner, which can be used to identify failed tests.

The `postCommit` hook is not only limited to running tests, but can be used for other commands as well. Since it runs in a temporary container, changes made by the hook do not persist, meaning that running the hook cannot affect the final image. This behavior allows for, among other uses, the installation and usage of test dependencies that are automatically discarded and are not present in the final image.

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-configuring-post-commit-build-hooks_{context}"]
= Configuring post commit build hooks

There are different ways to configure the post-build hook. All forms in the following examples are equivalent and run `bundle exec rake test --verbose`.

.Procedure

* Use one of the following options to configure post-build hooks:
+
|===
|Option |Description

|Shell script
a|
[source,yaml]
----
postCommit:
  script: "bundle exec rake test --verbose"
----

The `script` value is a shell script to be run with `/bin/sh -ic`. Use this option when a shell script is appropriate to execute the build hook. For example, for running unit tests as above. To control the image entry point or if the image does not have `/bin/sh`, use `command`, or `args`, or both.

[NOTE]
====
The additional `-i` flag was introduced to improve the experience working with CentOS and RHEL images, and may be removed in a future release.
====

|Command as the image entry point
a|
[source,yaml]
----
postCommit:
  command: ["/bin/bash", "-c", "bundle exec rake test --verbose"]
----

In this form, `command` is the command to run, which overrides the image
entry point in the exec form, as documented in the Dockerfile reference. This is needed if the image does not have `/bin/sh`, or if you do not want to use a shell. In all other cases, using `script` might be more convenient.

|Command with arguments
a|
[source,yaml]
----
postCommit:
  command: ["bundle", "exec", "rake", "test"]
  args: ["--verbose"]
----

This form is equivalent to appending the arguments to `command`.
|===

[NOTE]
====
Providing both `script` and `command` simultaneously creates an invalid build hook.
====

// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-using-cli-post-commit-build-hooks_{context}"]
= Using the CLI to set post commit build hooks

The `oc set build-hook` command can be used to set the build hook for a build configuration.

.Procedure

. Complete one of the following actions:

** To set a command as the post-commit build hook, enter the following command:
+
[source,terminal]
----
$ oc set build-hook bc/mybc \
    --post-commit \
    --command \
    -- bundle exec rake test --verbose
----
+
** To set a script as the post-commit build hook, enter the following command:
+
[source,terminal]
----
$ oc set build-hook bc/mybc --post-commit --script="bundle exec rake test --verbose"
----
