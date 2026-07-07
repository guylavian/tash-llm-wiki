---
title: "Building of container images using Buildah as a non-root user"
type: reference
domain: openshift
slug: cicd-4-22-unprivileged-building-of-container-images-using-buildah
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/unprivileged-building-of-container-images-using-buildah
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Building of container images using Buildah as a non-root user

[id="unprivileged-building-of-container-images-using-buildah"]
= Building of container images using Buildah as a non-root user

Running {pipelines-shortname} as the root user on a container can expose the container processes and the host to other potentially malicious resources. You can reduce this type of exposure by running the workload as a specific non-root user in the container. To run builds of container images using Buildah as a non-root user, you can perform the following steps:

* Define custom service account (SA) and security context constraint (SCC).
* Configure Buildah to use the `build` user with id `1000`.
* Start a task run with a custom config map, or integrate it with a pipeline run.

// Module included in the following assemblies:
//
// * cicd/pipelines/unprivileged-building-of-container-images-using-buildah.adoc

[id="configuring-custom-sa-and-scc_{context}"]
= Configuring custom service account and security context constraint

The default `pipeline` SA allows using a user id outside of the namespace range. To reduce dependency on the default SA, you can define a custom SA and SCC with necessary cluster role and role bindings for the `build` user with user id `1000`.

[IMPORTANT]
====
At this time, enabling the `allowPrivilegeEscalation` setting is required for Buildah to run successfully in the container. With this setting, Buildah can leverage `SETUID` and `SETGID` capabilities when running as a non-root user.
====

.Procedure

* Create a custom SA and SCC with necessary cluster role and role bindings.
+
.Example: Custom SA and SCC for used id `1000`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: pipelines-sa-userid-1000 # <1>
---
kind: SecurityContextConstraints
metadata:
  annotations:
  name: pipelines-scc-userid-1000 # <2>
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: true # <3>
allowPrivilegedContainer: false
allowedCapabilities: null
apiVersion: security.openshift.io/v1
defaultAddCapabilities: null
fsGroup:
  type: MustRunAs
groups:
- system:cluster-admins
priority: 10
readOnlyRootFilesystem: false
requiredDropCapabilities:
- MKNOD
- KILL
runAsUser: # <4>
  type: MustRunAs
  uid: 1000
seLinuxContext:
  type: MustRunAs
supplementalGroups:
  type: RunAsAny
users: []
volumes:
- configMap
- downwardAPI
- emptyDir
- persistentVolumeClaim
- projected
- secret
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines-scc-userid-1000-clusterrole # <5>
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - pipelines-scc-userid-1000
  resources:
  - securitycontextconstraints
  verbs:
  - use
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pipelines-scc-userid-1000-rolebinding # <6>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: pipelines-scc-userid-1000-clusterrole
subjects:
- kind: ServiceAccount
  name: pipelines-sa-userid-1000
----

<1> Define a custom SA.

<2> Define a custom SCC created based on restricted privileges, with modified `runAsUser` field.

<3> At this time, enabling the `allowPrivilegeEscalation` setting is required for Buildah to run successfully in the container. With this setting, Buildah can leverage `SETUID` and `SETGID` capabilities when running as a non-root user.

<4> Restrict any pod that gets attached with the custom SCC through the custom SA to run as user id `1000`.

<5> Define a cluster role that uses the custom SCC.

<6> Bind the cluster role that uses the custom SCC to the custom SA.
// Module included in the following assemblies:
//
// * cicd/pipelines/unprivileged-building-of-container-images-using-buildah.adoc

[id="configuring-builah-to-use-build-user_{context}"]
= Configuring Buildah to use `build` user

You can define a Buildah task to use the `build` user with user id `1000`.

.Procedure

. Create a copy of the `buildah` cluster task as an ordinary task.
+
[source,terminal]
----
$ oc get clustertask buildah -o yaml | yq '. |= (del .metadata |= with_entries(select(.key == "name" )))' | yq '.kind="Task"' | yq '.metadata.name="buildah-as-user"' | oc create -f -
----

. Edit the copied `buildah` task.
+
[source,terminal]
----
$ oc edit task buildah-as-user
----
+
.Example: Modified Buildah task with `build` user
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: buildah-as-user
spec:
  description: >-
    Buildah task builds source into a container image and
    then pushes it to a container registry.
    Buildah Task builds source into a container image using Project Atomic's
    Buildah build tool.It uses Buildah's support for building from Dockerfiles,
    using its buildah bud command.This command executes the directives in the
    Dockerfile to assemble a container image, then pushes that image to a
    container registry.
  params:
  - name: IMAGE
    description: Reference of the image buildah will produce.
  - name: BUILDER_IMAGE
    description: The location of the buildah builder image.
    default: registry.redhat.io/rhel8/buildah@sha256:99cae35f40c7ec050fed3765b2b27e0b8bbea2aa2da7c16408e2ca13c60ff8ee
  - name: STORAGE_DRIVER
    description: Set buildah storage driver
    default: vfs
  - name: DOCKERFILE
    description: Path to the Dockerfile to build.
    default: ./Dockerfile
  - name: CONTEXT
    description: Path to the directory to use as context.
    default: .
  - name: TLSVERIFY
    description: Verify the TLS on the registry endpoint (for push/pull to a non-TLS registry)
    default: "true"
  - name: FORMAT
    description: The format of the built container, oci or docker
    default: "oci"
  - name: BUILD_EXTRA_ARGS
    description: Extra parameters passed for the build command when building images.
    default: ""
  - description: Extra parameters passed for the push command when pushing images.
    name: PUSH_EXTRA_ARGS
    type: string
    default: ""
  - description: Skip pushing the built image
    name: SKIP_PUSH
    type: string
    default: "false"
  results:
  - description: Digest of the image just built.
    name: IMAGE_DIGEST
    type: string
  workspaces:
  - name: source
  steps:
  - name: build
    securityContext:
      runAsUser: 1000 <1>
    image: $(params.BUILDER_IMAGE)
    workingDir: $(workspaces.source.path)
    script: |
      echo "Running as USER ID `id`" <2>
      buildah --storage-driver=$(params.STORAGE_DRIVER) bud \
        $(params.BUILD_EXTRA_ARGS) --format=$(params.FORMAT) \
        --tls-verify=$(params.TLSVERIFY) --no-cache \
        -f $(params.DOCKERFILE) -t $(params.IMAGE) $(params.CONTEXT)
      [[ "$(params.SKIP_PUSH)" == "true" ]] && echo "Push skipped" && exit 0
      buildah --storage-driver=$(params.STORAGE_DRIVER) push \
        $(params.PUSH_EXTRA_ARGS) --tls-verify=$(params.TLSVERIFY) \
        --digestfile $(workspaces.source.path)/image-digest $(params.IMAGE) \
        docker://$(params.IMAGE)
      cat $(workspaces.source.path)/image-digest | tee /tekton/results/IMAGE_DIGEST
    volumeMounts:
    - name: varlibcontainers
      mountPath: /home/build/.local/share/containers <3>
  volumes:
  - name: varlibcontainers
    emptyDir: {}
----
<1> Run the container explicitly as the user id `1000`, which corresponds to the `build` user in the Buildah image.
<2> Display the user id to confirm that the process is running as user id `1000`.
<3> You can change the path for the volume mount as necessary.
// Module included in the following assemblies:
//
// * cicd/pipelines/unprivileged-building-of-container-images-using-buildah.adoc

[id="starting-a-task-run-with-custom-config-map-or-a-pipeline-run_{context}"]
= Starting a task run with custom config map, or a pipeline run

After defining the custom Buildah cluster task, you can create a `TaskRun` object that builds an image as a `build` user with user id `1000`. In addition, you can integrate the `TaskRun` object as part of a `PipelineRun` object.

.Procedure

. Create a `TaskRun` object with a custom `ConfigMap` and `Dockerfile` objects.
+
.Example: A task run that runs Buildah as user id `1000`
[source,yaml]
----
apiVersion: v1
data:
  Dockerfile: |
    ARG BASE_IMG=registry.access.redhat.com/ubi9/ubi
    FROM $BASE_IMG AS buildah-runner
    RUN dnf -y update && \
        dnf -y install git && \
        dnf clean all
    CMD git
kind: ConfigMap
metadata:
  name: dockerfile # <1>
---
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: buildah-as-user-1000
spec:
  serviceAccountName: pipelines-sa-userid-1000 # <2>
  params:
  - name: IMAGE
    value: image-registry.openshift-image-registry.svc:5000/test/buildahuser
  taskRef:
    kind: Task
    name: buildah-as-user
  workspaces:
  - configMap:
      name: dockerfile # <3>
    name: source
----
<1> Use a config map because the focus is on the task run, without any prior task that fetches some sources with a Dockerfile.
<2> The name of the service account that you created.
<3> Mount a config map as the source workspace for the `buildah-as-user` task.

. (Optional) Create a pipeline and a corresponding pipeline run.
+
.Example: A pipeline and corresponding pipeline run
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: pipeline-buildah-as-user-1000
spec:
  params:
  - name: IMAGE
  - name: URL
  workspaces:
  - name: shared-workspace
  - name: sslcertdir
    optional: true
  tasks:
  - name: fetch-repository # <1>
    taskRef:
      name: git-clone
      kind: ClusterTask
    workspaces:
    - name: output
      workspace: shared-workspace
    params:
    - name: url
      value: $(params.URL)
    - name: subdirectory
      value: ""
    - name: deleteExisting
      value: "true"
  - name: buildah
    taskRef:
      name: buildah-as-user # <2>
    runAfter:
    - fetch-repository
    workspaces:
    - name: source
      workspace: shared-workspace
    - name: sslcertdir
      workspace: sslcertdir
    params:
    - name: IMAGE
      value: $(params.IMAGE)
---
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: pipelinerun-buildah-as-user-1000
spec:
  taskRunSpecs:
    - pipelineTaskName: buildah
      taskServiceAccountName: pipelines-sa-userid-1000 # <3>
  params:
  - name: URL
    value: https://github.com/openshift/pipelines-vote-api
  - name: IMAGE
    value: image-registry.openshift-image-registry.svc:5000/test/buildahuser
  pipelineRef:
    name: pipeline-buildah-as-user-1000
  workspaces:
  - name: shared-workspace # <4>
    volumeClaimTemplate:
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 100Mi
----
<1> Use the `git-clone` cluster task to fetch the source containing a Dockerfile and build it using the modified Buildah task.
<2> Refer to the modified Buildah task.
<3> Use the service account that you created for the Buildah task.
<4> Share data between the `git-clone` task and the modified Buildah task using a persistent volume claim (PVC) created automatically by the controller.

. Start the task run or the pipeline run.
// Module included in the following assemblies:
//
// * cicd/pipelines/unprivileged-building-of-container-images-using-buildah.adoc

[id="limitations-of-unprivileged-builds_{context}"]
= Limitations of unprivileged builds

The process for unprivileged builds works with most `Dockerfile` objects. However, there are some known limitations might cause a build to fail:

* Using the `--mount=type=cache` option might fail due to lack of necessay permissions issues. For more information, see this article.
* Using the `--mount=type=secret` option fails because mounting resources requires additionnal capabilities that are not provided by the custom SCC.

.Additional resources

* Managing security context constraints (SCCs)
