---
title: "On-cluster function building and deploying"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-on-cluster-builds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-on-cluster-builds
version: 4.22
family: serverless
documentKind: "Documentation"
---

# On-cluster function building and deploying

[id="serverless-functions-on-cluster-builds"]
= On-cluster function building and deploying

Instead of building a function locally, you can build a function directly on the cluster. When using this workflow on a local development machine, you only need to work with the function source code. This is useful, for example, when you cannot install on-cluster function building tools, such as docker or podman.

// Module included in the following assemblies:
//
// * /serverless/functions/serverless-functions-on-cluster-builds.adoc

[id="serverless-functions-creating-on-cluster-builds_{context}"]
= Building and deploying functions on the cluster

You can use the Knative (`kn`) CLI to initiate a function project build and then deploy the function directly on the cluster. To build a function project in this way, the source code for your function project must exist in a Git repository branch that is accessible to your cluster.

.Prerequisites

* {pipelines-title} must be installed on your cluster.

* You have installed the OpenShift CLI (`oc`).

* You have installed the Knative (`kn`) CLI.

.Procedure

. In each namespace where you want to run {pipelines-shortname} and deploy a function, you must create the following resources:

.. Create the `s2i` Tekton task to be able to use Source-to-Image in the pipeline:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-knative/kn-plugin-func/serverless-1.28.0/pipelines/resources/tekton/task/func-s2i/0.1/func-s2i.yaml
----

.. Create the `kn func` deploy Tekton task to be able to deploy the function in the pipeline:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/openshift-knative/kn-plugin-func/serverless-1.28.0/pipelines/resources/tekton/task/func-deploy/0.1/func-deploy.yaml
----

. Create a function:
+
[source,terminal]
----
$ kn func create <function_name> -l <runtime>
----

. After you have created a new function project, you must add the project to a Git repository and ensure that the repository is available to the cluster. Information about this Git repository is used to update the `func.yaml` file in the next step.

. Update the configuration in the `func.yaml` file for your function project to enable on-cluster builds for the Git repository:
+
[source,yaml]
----
...
git:
  url: <git_repository_url> <1>
  revision: main <2>
  contextDir: <directory_path> <3>
...
----
<1> Required. Specify the Git repository that contains your function's source code.
<2> Optional. Specify the Git repository revision to be used. This can be a branch, tag, or commit.
<3> Optional. Specify the function's directory path if the function is not located in the Git repository root folder.

. Implement the business logic of your function. Then, use Git to commit and push the changes.

. Deploy your function:
+
[source,terminal]
----
$ kn func deploy --remote
----
+
If you are not logged into the container registry referenced in your function configuration, you are prompted to provide credentials for the remote container registry that hosts the function image:
+
.Example output and prompts
[source,terminal]
----
🕕 Creating Pipeline resources
Please provide credentials for image registry used by Pipeline.
? Server: https://index.docker.io/v1/
? Username: my-repo
? Password: ********
   Function deployed at URL: http://test-function.default.svc.cluster.local
----

. To update your function, commit and push new changes by using Git, then run the `kn func deploy --remote` command again.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-on-cluster-builds.adoc

[id="serverless-functions-specifying-function-revision_{context}"]
= Specifying function revision

When building and deploying a function on the cluster, you must specify the location of the function code by specifying the Git repository, branch, and subdirectory within the repository. You do not need to specify the branch if you use the `main` branch. Similarly, you do not need to specify the subdirectory if your function is at the root of the repository. You can specify these parameters in the `func.yaml` configuration file, or by using flags with the `kn func deploy` command.

.Prerequisites

* {pipelines-title} must be installed on your cluster.

* You have installed the OpenShift (`oc`) CLI.

* You have installed the Knative (`kn`) CLI.

.Procedure

* Deploy your function:
+
[source,terminal]
----
$ kn func deploy --remote \ <1>
                 --git-url <repo-url> \ <2>
                 [--git-branch <branch>] \ <3>
                 [--git-dir <function-dir>] <4>
----
+
--
<1> With the `--remote` flag, the build runs remotely.
<2> Substitute `<repo-url>` with the URL of the Git repository.
<3> Substitute `<branch>` with the Git branch, tag, or commit. If using the latest commit on the `main` branch, you can skip this flag.
<4> Substitute `<function-dir>` with the directory containing the function if it is different than the repository root directory.
--
+
For example:
+
[source,terminal]
----
$ kn func deploy --remote \
                 --git-url https://example.com/alice/myfunc.git \
                 --git-branch my-feature \
                 --git-dir functions/example-func/
----
