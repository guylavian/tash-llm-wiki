---
title: "Authenticating pipelines using git secret"
type: reference
domain: openshift
slug: cicd-4-22-authenticating-pipelines-using-git-secret
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/authenticating-pipelines-using-git-secret
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Authenticating pipelines using git secret

[id="authenticating-pipelines-using-git-secret"]
= Authenticating pipelines using git secret

A Git secret consists of credentials to securely interact with a Git repository, and is often used to automate authentication. In {pipelines-title}, you can use Git secrets to authenticate pipeline runs and task runs that interact with a Git repository during execution.

A pipeline run or a task run gains access to the secrets through the associated service account. {pipelines-shortname} support the use of Git secrets as annotations (key-value pairs) for basic authentication and SSH-based authentication.

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-understanding-credential-selection_{context}"]
= Credential selection

A pipeline run or task run might require multiple authentications to access different Git repositories. Annotate each secret with the domains where {pipelines-shortname} can use its credentials.

A credential annotation key for Git secrets must begin with `tekton.dev/git-`, and its value is the URL of the host for which you want {pipelines-shortname} to use that credential.

In the following example, {pipelines-shortname} uses a `basic-auth` secret, which relies on a username and password, to access repositories at `github.com` and `gitlab.com`.

.Example: Multiple credentials for basic authentication
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  annotations:
    tekton.dev/git-0: github.com
    tekton.dev/git-1: gitlab.com
type: kubernetes.io/basic-auth
stringData:
  username: <username> <1>
  password: <password> <2>
----
<1> Username for the repository
<2> Password or personal access token for the repository

You can also use an `ssh-auth` secret (private key) to access a Git repository.

.Example: Private key for SSH based authentication
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  annotations:
    tekton.dev/git-0: https://github.com
type: kubernetes.io/ssh-auth
stringData:
  ssh-privatekey: <1>
----
<1> The content of the SSH private key file.

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-configuring-basic-authentication-for-git_{context}"]
= Configuring basic authentication for Git

[role="_abstract"]
For a pipeline to retrieve resources from password-protected repositories, you must configure the basic authentication for that pipeline.

To configure basic authentication for a pipeline, update the `secret.yaml`, `serviceaccount.yaml`, and `run.yaml` files with the credentials from the Git secret for the specified repository. When you complete this process, {pipelines-shortname} can use that information to retrieve the specified pipeline resources.

[NOTE]
====
For GitHub, authentication using plain password is deprecated. Instead, use a personal access token.
====

.Procedure

. In the `secret.yaml` file, specify the username and password or GitHub personal access token to access the target Git repository.
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: basic-user-pass <1>
  annotations:
    tekton.dev/git-0: https://github.com
type: kubernetes.io/basic-auth
stringData:
  username: <username> <2>
  password: <password> <3>
----
<1> Name of the secret. In this example, `basic-user-pass`.
<2> Username for the Git repository.
<3> Password for the Git repository.

+
. In the `serviceaccount.yaml` file, associate the secret with the appropriate service account.
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-bot <1>
secrets:
  - name: basic-user-pass <2>
----
<1> Name of the service account. In this example, `build-bot`.
<2> Name of the secret. In this example, `basic-user-pass`.
+
. In the `run.yaml` file, associate the service account with a task run or a pipeline run.
+
* Associate the service account with a task run:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: build-push-task-run-2 <1>
spec:
  serviceAccountName: build-bot <2>
  taskRef:
    name: build-push <3>
----
<1> Name of the task run. In this example, `build-push-task-run-2`.
<2> Name of the service account. In this example, `build-bot`.
<3> Name of the task. In this example, `build-push`.
+
* Associate the service account with a `PipelineRun` resource:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: demo-pipeline <1>
  namespace: default
spec:
  serviceAccountName: build-bot <2>
  pipelineRef:
    name: demo-pipeline <3>
----
<1> Name of the pipeline run. In this example, `demo-pipeline`.
<2> Name of the service account. In this example, `build-bot`.
<3> Name of the pipeline. In this example, `demo-pipeline`.
+
. Apply the changes.
+
[source,terminal]
----
$ oc apply --filename secret.yaml,serviceaccount.yaml,run.yaml
----

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-configuring-ssh-authentication-for-git_{context}"]
= Configuring SSH authentication for Git

[role="_abstract"]
For a pipeline to retrieve resources from repositories configured with SSH keys, you must configure the SSH-based authentication for that pipeline.

To configure SSH-based authentication for a pipeline, update the `secret.yaml`, `serviceaccount.yaml`, and `run.yaml` files with the credentials from the SSH private key for the specified repository. When you complete this process, {pipelines-shortname} can use that information to retrieve the specified pipeline resources.

[NOTE]
====
Consider using SSH-based authentication rather than basic authentication.
====

.Procedure

. Generate an SSH private key, or copy an existing private key, which is usually available in the `~/.ssh/id_rsa` file.
. In the `secret.yaml` file, set the value of `ssh-privatekey` to the content of the SSH private key file, and set the value of `known_hosts` to the content of the known hosts file.

+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: ssh-key <1>
  annotations:
    tekton.dev/git-0: github.com
type: kubernetes.io/ssh-auth
stringData:
  ssh-privatekey: <2>
  known_hosts: <3>
----
<1> Name of the secret containing the SSH private key. In this example, `ssh-key`.
<2> The content of the SSH private key file.
<3> The content of the known hosts file.
+
[CAUTION]
====
If you omit the private key, {pipelines-shortname} accepts the public key of any server.
====
+
. Optional: To specify a custom SSH port, add `:<port number>` to the end of the `annotation` value. For example, `tekton.dev/git-0: github.com:2222`.
. In the `serviceaccount.yaml` file, associate the `ssh-key` secret with the `build-bot` service account.
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-bot <1>
secrets:
  - name: ssh-key <2>
----
<1> Name of the service account. In this example, `build-bot`.
<2> Name of the secret containing the SSH private key. In this example, `ssh-key`.
+
. In the `run.yaml` file, associate the service account with a task run or a pipeline run.
+
* Associate the service account with a task run:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: build-push-task-run-2 <1>
spec:
  serviceAccountName: build-bot <2>
  taskRef:
    name: build-push <3>
----
<1> Name of the task run. In this example, `build-push-task-run-2`.
<2> Name of the service account. In this example, `build-bot`.
<3> Name of the task. In this example, `build-push`.
+
* Associate the service account with a pipeline run:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: demo-pipeline <1>
  namespace: default
spec:
  serviceAccountName: build-bot <2>
  pipelineRef:
    name: demo-pipeline <3>
----
<1> Name of the pipeline run. In this example, `demo-pipeline`.
<2> Name of the service account. In this example, `build-bot`.
<3> Name of the pipeline. In this example, `demo-pipeline`.
+
. Apply the changes.
+
[source,terminal]
----
$ oc apply --filename secret.yaml,serviceaccount.yaml,run.yaml
----

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-using-ssh-authentication-in-git-type-tasks_{context}"]
= Using SSH authentication in git type tasks

When invoking Git commands, you can use SSH authentication directly in the steps of a task. SSH authentication ignores the `$HOME` variable and only uses the user's home directory specified in the `/etc/passwd` file. So each step in a task must symlink the `/tekton/home/.ssh` directory to the home directory of the associated user.

However, explicit symlinks are not necessary when you use a pipeline resource of the `git` type, or the `git-clone` task available in the Tekton catalog.

As an example of using SSH authentication in `git` type tasks, refer to authenticating-git-commands.yaml.

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-using-secrets-as-a-nonroot-user_{context}"]
= Using secrets as a non-root user

You might need to use secrets as a non-root user in certain scenarios, such as:

* The users and groups that the containers use to execute runs are randomized by the platform.
* The steps in a task define a non-root security context.
* A task specifies a global non-root security context, which applies to all steps in a task.

In such scenarios, consider the following aspects of executing task runs and pipeline runs as a non-root user:

* SSH authentication for Git requires the user to have a valid home directory configured in the `/etc/passwd` directory. Specifying a UID that has no valid home directory results in authentication failure.
* SSH authentication ignores the `$HOME` environment variable. So you must or symlink the appropriate secret files from the `$HOME` directory defined by {pipelines-shortname} (`/tekton/home`), to the non-root user's valid home directory.

In addition, to configure SSH authentication in a non-root security context, refer to the example for authenticating git commands.

// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-limiting-secret-access-to-specific-steps_{context}"]
= Limiting secret access to specific steps

By default, the secrets for {pipelines-shortname} are stored in the `$HOME/tekton/home` directory, and are available for all the steps in a task.

To limit a secret to specific steps, use the secret definition to specify a volume, and mount the volume in specific steps.
