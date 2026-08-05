---
title: "Using {pac}"
type: reference
domain: openshift
slug: cicd-4-22-using-pipelines-as-code
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/using-pipelines-as-code
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Using {pac}

[id="using-pipelines-as-code"]
= Using {pac}

// :FeatureName: Pipelines as Code
[role="_abstract"]
With {pac}, cluster administrators and users with the required privileges can define pipeline templates as part of source code Git repositories. When triggered by a source code push or a pull request for the configured Git repository, {pac} runs the pipeline and reports the status.

[id="pac-key-features"]
== Key features
{pac} supports the following features:

* Pull request status and control on the platform hosting the Git repository.
* GitHub Checks API to set the status of a pipeline run, including rechecks.
* GitHub pull request and commit events.
* Pull request actions in comments, such as `/retest`.
* Git events filtering and a separate pipeline for each event.
* Automatic task resolution in {pipelines-shortname}, including local tasks, Tekton Hub, and remote URLs.
* Retrieval of configurations using GitHub blobs and objects API.
* Access Control List (ACL) over a GitHub organization, or using a Prow style `OWNER` file.
* The `tkn pac` CLI plugin for managing bootstrapping and {pac} repositories.
* Support for GitHub App, GitHub Webhook, Bitbucket Server, and Bitbucket Cloud.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="installing-pipelines-as-code-on-an-openshift-cluster_{context}"]
= Installing {pac} on an OpenShift Container Platform

[role="_abstract"]
{pac} is installed in the `openshift-pipelines` namespace when you install the {pipelines-title} Operator. For more details, see _Installing {pipelines-shortname}_ in the _Additional resources_ section.

To disable the default installation of {pac} with the Operator, set the value of the `enable` parameter to `false` in the `TektonConfig` custom resource.

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: false
        settings:
          application-name: Pipelines as Code CI
          auto-configure-new-github-repo: "false"
          bitbucket-cloud-check-source-ip: "true"
          hub-catalog-name: tekton
          hub-url: https://api.hub.tekton.dev/v1
          remote-tasks: "true"
          secret-auto-create: "true"
# ...
----

Optionally, you can run the following command:

[source,terminal]
----
$ oc patch tektonconfig config --type="merge" -p '{"spec": {"platforms": {"openshift":{"pipelinesAsCode": {"enable": false}}}}}'
----

To enable the default installation of {pac} with the {pipelines-title} Operator, set the value of the `enable` parameter to `true` in the `TektonConfig` custom resource:

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          application-name: Pipelines as Code CI
          auto-configure-new-github-repo: "false"
          bitbucket-cloud-check-source-ip: "true"
          hub-catalog-name: tekton
          hub-url: https://api.hub.tekton.dev/v1
          remote-tasks: "true"
          secret-auto-create: "true"
# ...
----

Optionally, you can run the following command:

[source,terminal]
----
$ oc patch tektonconfig config --type="merge" -p '{"spec": {"platforms": {"openshift":{"pipelinesAsCode": {"enable": true}}}}}'
----

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="installing-pipelines-as-code-cli_{context}"]
= Installing {pac} CLI

[role="_abstract"]
Cluster administrators can use the `tkn pac` and `opc` CLI tools on local machines or as containers for testing. The `tkn pac` and `opc` CLI tools are installed automatically when you install the `tkn` CLI for {pipelines-title}.

You can install the `tkn pac` and `opc` version `1.11.0` binaries for the supported platforms:

* Linux (x86_64, amd64)
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)
* Linux on {ibm-power-name} (ppc64le)
* macOS
* Windows

// In addition, you can install `tkn pac` using the following methods:

// [CAUTION]
// ====
// The `tkn pac` CLI tool available using these methods is _not updated regularly_.
// ====

// * Install on Linux or Mac OS using the `brew` package manager:
// +
// [source,terminal]
// ----
// $ brew install openshift-pipelines/pipelines-as-code/tektoncd-pac
// ----
// +
// You can upgrade the package by running the following command:
// +
// [source,terminal]
// ----
// $ brew upgrade openshift-pipelines/pipelines-as-code/tektoncd-pac
// ----

// * Install as a container using `podman`:
// +
// [source,terminal]
// ----
// $ podman run -e KUBECONFIG=/tmp/kube/config -v ${HOME}/.kube:/tmp/kube \
//      -it quay.io/openshift-pipeline/pipelines-as-code tkn pac help
// ----
// +
// You can also use `docker` as a substitute for `podman`.

// * Install from the GitHub repository using `go`:
// +
// [source,terminal]
// ----
// $ go install github.com/openshift-pipelines/pipelines-as-code/cmd/tkn-pac
// ----

[id="using-pipelines-as-code-with-a-git-repository-hosting-service-provider"]
== Using {pac} with a Git repository hosting service provider

[role="_abstract"]
After installing {pac}, cluster administrators can configure a Git repository hosting service provider. Currently, the following services are supported:

* GitHub App
* GitHub Webhook
* GitLab
* Bitbucket Server
* Bitbucket Cloud

[NOTE]
====
GitHub App is the recommended service for using with {pac}.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-with-a-github-app_{context}"]
= Using {pac} with a GitHub App

[role="_abstract"]
GitHub Apps act as a point of integration with {pipelines-title} and bring the advantage of Git-based workflows to {pipelines-shortname}. Cluster administrators can configure a single GitHub App for all cluster users. For GitHub Apps to work with {pac}, ensure that the webhook of the GitHub App points to the {pac} event listener route (or ingress endpoint) that listens for GitHub events.

[NOTE]
====
When importing an application using *Import from Git* and the Git repository has a `.tekton` directory, you can configure `pipelines-as-code` for your application.
====

[id="configuring-github-app-for-pac"]
== Configuring a GitHub App

Cluster administrators can create a GitHub App by running the following command:

[source,terminal]
----
$ tkn pac bootstrap github-app
----

If the `tkn pac` CLI plugin is not installed, you can create the GitHub App manually.

.Procedure

To create and configure a GitHub App manually for {pac}, perform the following steps:

. Sign in to your GitHub account.

. Go to **Settings** -> **Developer settings** -> **GitHub Apps**, and click **New GitHub App**.

. Provide the following information in the GitHub App form:

* **GitHub Application Name**: `{pipelines-shortname}`
* **Homepage URL**: OpenShift Console URL
* **Webhook URL**: The {pac} route or ingress URL. You can find it by running the following command:
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

* **Webhook secret**: An arbitrary secret. You can generate a secret by running the following command:
+
[source,terminal]
----
$ openssl rand -hex 20
----

. Select the following **Repository permissions**:

* **Checks**: `Read & Write`
* **Contents**: `Read & Write`
* **Issues**: `Read & Write`
* **Metadata**: `Read-only`
* **Pull request**: `Read & Write`

. Select the following **Organization permissions**:

* **Members**: `Readonly`
* **Plan**: `Readonly`

. Select the following **User permissions**:

* **Check run**
* **Issue comment**
* **Pull request**
* **Push**

. Click **Create GitHub App**.

. On the **Details** page of the newly created GitHub App, note the **App ID** displayed at the top.

. In the **Private keys** section, click **Generate Private key** to automatically generate and download a private key for the GitHub app. Securely store the private key for future reference and usage.

. Install the created App on a repository that you want to use with {pac}.

[id="configuring-pac-for-github-app"]
== Configuring {pac} to access a GitHub App

To configure {pac} to access the newly created GitHub App, execute the following command:

[source,terminal]
----
$ oc -n openshift-pipelines create secret generic pipelines-as-code-secret \
        --from-literal github-private-key="$(cat <PATH_PRIVATE_KEY>)" \ <1>
        --from-literal github-application-id="<APP_ID>" \ <2>
        --from-literal webhook.secret="<WEBHOOK_SECRET>" <3>
----
<1> The path to the private key you downloaded while configuring the GitHub App.
<2> The **App ID** of the GitHub App.
<3> The webhook secret provided when you created the GitHub App.

[NOTE]
====
{pac} works automatically with GitHub Enterprise by detecting the header set from GitHub Enterprise and using it for the GitHub Enterprise API authorization URL.
====

// Module included in the following assemblies:
//
// * cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

[id="creating-a-github-application-in-administrator-perspective_{context}"]

= Creating a GitHub App in administrator perspective

As a cluster administrator, you can configure your GitHub App with the OpenShift Container Platform cluster to use {pac}. This configuration allows you to execute a set of tasks required for build deployment.

.Prerequisites
You have installed the {pipelines-title} `{pipelines-ver}` operator from the Operator Hub.

.Procedure
. In the administrator perspective, navigate to *Pipelines* using the navigation pane.
. Click *Setup GitHub App* on the *Pipelines* page.
. Enter your GitHub App name. For example, `pipelines-ci-clustername-testui`.
. Click *Setup*.
. Enter your Git password when prompted in the browser.
. Click *Create GitHub App for <username>*, where `<username>` is your GitHub user name.

.Verification
After successful creation of the GitHub App, the OpenShift Container Platform web console opens and displays the details about the application.

image::Github-app-details.png[]

The details of the GitHub App are saved as a secret in the `openShift-pipelines` namespace.

To view details such as name, link, and secret associated with the GitHub applications, navigate to *Pipelines* and click *View GitHub App*.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="scoping-github-token_{context}"]
= Scoping the GitHub token to additional repositories

{pac} uses the GitHub app to generate a GitHub access token. {pac} uses this token to retrieve the pipeline payload from the repository and to enable the CI/CD processes to interact with GitHub repositories.

By default, the access token is scoped only to the repository from which {pac} retrieves the pipeline definition. In some cases, you might want the token to have access to additional repositories. For example, there might be a CI repository where the `.tekton/pr.yaml` file and source payload are located, but the build process defined in `pr.yaml` fetches tasks from a separate private CD repository.

You can extend the scope of the GitHub token in two ways:

* _Global configuration_: You can extend the GitHub token to a list of repositories in different namespaces. You must have administrative permissions to set this configuration.
* _Repository level configuration_: You can extend the GitHub token to a list of repositories that exist in the same namespace as the original repository. You do not need administrative permissions to set this configuration.

.Procedure

. In the `TektonConfig` custom resource (CR), in the `pipelinesAsCode.settings` spec, set the `secret-github-app-token-scoped` parameter to `false`. This setting enables scoping the GitHub token to private and public repositories listed in the global and repository level configuration.

. To set global configuration for scoping the GitHub token, in the `TektonConfig` CR, in the `pipelinesAsCode.settings` spec, specify the additional repositories in the `secret-github-app-scope-extra-repos` parameter, as in the following example:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          secret-github-app-token-scoped: false
          secret-github-app-scope-extra-repos: "owner2/project2, owner3/project3"
----
+
. To set repository level configuration for scoping the GitHub token, specify the additional repositories in the `github_app_token_scope_repos` parameter of the `Repository` CR, as in the following example:
+
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: test
  namespace: test-repo
spec:
  url: "https://github.com/linda/project"
  settings:
    github_app_token_scope_repos:
    - "owner/project"
    - "owner1/project1"
----
+
In this example, the `Repository` custom resource is associated with the `linda/project` repository in the `test-repo` namespace. The scope of the generated GitHub token is extended to the `owner/project` and `owner1/project1` repositories, as well as the `linda/project` repository. These repositories must exist under the `test-repo` namespace.
+
[NOTE]
====
The additional repositories can be public or private, but must reside in the same namespace as the repository with which the `Repository` resource is associated.

If any of the repositories do not exist in the namespace, the scoping of the GitHub token fails with an error message:

[source,terminal]
----
failed to scope GitHub token as repo owner1/project1 does not exist in namespace test-repo
----
====

.Result

The generated GitHub token enables access to the additional repositories that you configured in the global and repository level configuration, as well as the original repository where the {pac} payload files are located.

If you provide both global configuration and repository level configuration, the token is scoped to all the repositories from both configurations, as in the following example.

.`TektonConfig` custom resource
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          secret-github-app-token-scoped: false
          secret-github-app-scope-extra-repos: "owner2/project2, owner3/project3"
----

.`Repository` custom resource
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
 name: test
 namespace: test-repo
spec:
 url: "https://github.com/linda/project"
 settings:
   github_app_token_scope_repos:
   - "owner/project"
   - "owner1/project1"
----

The GitHub token is scoped to the `owner/project`, `owner1/project1`, `owner2/project2`, `owner3/project3`, and `linda/project` respositories.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-with-github-webhook_{context}"]
= Using {pac} with GitHub Webhook

[role="_abstract"]
Use {pac} with GitHub Webhook on your repository if you cannot create a GitHub App. However, using {pac} with GitHub Webhook does not give you access to the GitHub Check Runs API. The status of the tasks is added as comments on the pull request and is unavailable under the *Checks* tab.

[NOTE]
====
{pac} with GitHub Webhook does not support GitOps comments such as `/retest` and `/ok-to-test`. To restart the continuous integration (CI), create a new commit to the repository. For example, to create a new commit without any changes, you can use the following command:

[source,terminal]
----
$ git --amend -a --no-edit && git push --force-with-lease <origin> <branchname>
----
====

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* For authorization, create a personal access token on GitHub.

** To generate a secure and fine-grained token, restrict its scope to a specific repository and grant the following permissions:
+
.Permissions for fine-grained tokens
[options="header"]
|===

| Name | Access

| Administration | Read-only

| Metadata | Read-only

| Content | Read-only

| Commit statuses | Read and Write

| Pull request | Read and Write

| Webhooks | Read and Write

|===

** To use classic tokens, set the scope as `public_repo` for public repositories and `repo` for private repositories. In addition, provide a short token expiration period and note the token in an alternate location.
+
[NOTE]
====
If you want to configure the webhook using the `tkn pac` CLI, add the `admin:repo_hook` scope.
====

[discrete]
.Procedure

. Configure the webhook and create a `Repository` custom resource (CR).

** To configure a webhook and create a `Repository` CR _automatically_ using the `tkn pac` CLI tool, use the following command:
+
[source,terminal]
----
$ tkn pac create repo
----
+
.Sample interactive output
[source,terminal]
----
? Enter the Git repository url (default: https://github.com/owner/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository owner-repo has been created in repo-pipelines namespace
✓ Setting up GitHub Webhook for Repository https://github.com/owner/repo
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: sJNwdmTifHTs):  sJNwdmTifHTs
ℹ ️You now need to create a GitHub personal access token, please checkout the docs at https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token for the required scopes
? Please enter the GitHub access token:  ****************************************
✓ Webhook has been created on repository owner/repo
🔑 Webhook Secret owner-repo has been created in the repo-pipelines namespace.
🔑 Repository CR owner-repo has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ We have detected your repository using the programming language Go.
✓ A basic template has been created in /home/Go/src/github.com/owner/repo/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On your GitHub repository or organization, perform the following steps:

.... Go to *Settings* –> *Webhooks* and click *Add webhook*.

.... Set the *Payload URL* to the {pac} controller public URL.

.... Select the content type as *application/json*.

.... Add a webhook secret and note it in an alternate location. With `openssl` installed on your local machine, generate a random secret.
+
[source,terminal]
----
$ openssl rand -hex 20
----

.... Click *Let me select individual events* and select these events: *Commit comments*, *Issue comments*, *Pull request*, and *Pushes*.

.... Click *Add webhook*.

... On your OpenShift cluster, create a `Secret` object with the personal access token and webhook secret.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic github-webhook-config \
  --from-literal provider.token="<GITHUB_PERSONAL_ACCESS_TOKEN>" \
  --from-literal webhook.secret="<WEBHOOK_SECRET>"
----

... Create a `Repository` CR.
+
.Example: `Repository` CR
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
  url: "https://github.com/owner/repo"
  git_provider:
    secret:
      name: "github-webhook-config"
      key: "provider.token" # Set this if you have a different key in your secret
    webhook_secret:
      name: "github-webhook-config"
      key: "webhook.secret" # Set this if you have a different key for your secret
----
+
[NOTE]
====
{pac} assumes that the OpenShift `Secret` object and the `Repository` CR are in the same namespace.
====

. Optional: For an existing `Repository` CR, add multiple GitHub Webhook secrets or provide a substitute for a deleted secret.

.. Add a webhook using the `tkn pac` CLI tool.
+
.Example: Additional webhook using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook add -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
✓ Setting up GitHub Webhook for Repository https://github.com/owner/repo
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: AeHdHTJVfAeH):  AeHdHTJVfAeH
✓ Webhook has been created on repository owner/repo
🔑 Secret owner-repo has been updated with webhook secert in the repo-pipelines namespace.
----

.. Update the `webhook.secret` key in the existing OpenShift `Secret` object.

. Optional: For an existing `Repository` CR, update the personal access token.

** Update the personal access token using the `tkn pac` CLI tool.
+
.Example: Updating personal access token using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook update-token -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
? Please enter your personal access token:  ****************************************
🔑 Secret owner-repo has been updated with new personal access token in the repo-pipelines namespace.
----

** Alternatively, update the personal access token by modifying the `Repository` CR.

... Find the name of the secret in the `Repository` CR.
+
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
# ...
  git_provider:
    secret:
      name: "github-webhook-config"
# ...
----

... Use the `oc patch` command to update the values of the `$NEW_TOKEN` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret github-webhook-config -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----

.Additional resources

* GitHub Webhook documentation on GitHub
* GitHub Check Runs documentation on GitHub
* Creating a personal access token on GitHub
* Classic tokens with pre-filled permissions

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-with-gitlab_{context}"]
= Using {pac} with GitLab

[role="_abstract"]
If your organization or project uses GitLab as the preferred platform, you can use {pac} for your repository with a webhook on GitLab.

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* For authorization, generate a personal access token as the manager of the project or organization on GitLab.
+
[NOTE]
====
* If you want to configure the webhook using the `tkn pac` CLI, add the `admin:repo_hook` scope to the token.

* Using a token scoped for a specific project cannot provide API access to a merge request (MR) sent from a forked repository. In such cases, {pac} displays the result of a pipeline as a comment on the MR.
====

[discrete]
.Procedure

. Configure the webhook and create a `Repository` custom resource (CR).

** To configure a webhook and create a `Repository` CR _automatically_ using the `tkn pac` CLI tool, use the following command:
+
[source,terminal]
----
$ tkn pac create repo
----
+
.Sample interactive output
[source,terminal]
----
? Enter the Git repository url (default: https://gitlab.com/owner/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository repositories-project has been created in repo-pipelines namespace
✓ Setting up GitLab Webhook for Repository https://gitlab.com/owner/repo
? Please enter the project ID for the repository you want to be configured,
  project ID refers to an unique ID (e.g. 34405323) shown at the top of your GitLab project : 17103
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: lFjHIEcaGFlF):  lFjHIEcaGFlF
ℹ ️You now need to create a GitLab personal access token with `api` scope
ℹ ️Go to this URL to generate one https://gitlab.com/-/profile/personal_access_tokens, see https://is.gd/rOEo9B for documentation
? Please enter the GitLab access token:  **************************
? Please enter your GitLab API URL::  https://gitlab.com
✓ Webhook has been created on your repository
🔑 Webhook Secret repositories-project has been created in the repo-pipelines namespace.
🔑 Repository CR repositories-project has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ A basic template has been created in /home/Go/src/gitlab.com/repositories/project/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On your GitLab project, perform the following steps:

.... Use the left sidebar to go to *Settings* –> *Webhooks*.

.... Set the *URL* to the {pac} controller public URL.

.... Add a webhook secret and note it in an alternate location. With `openssl` installed on your local machine, generate a random secret.
+
[source,terminal]
----
$ openssl rand -hex 20
----

.... Click *Let me select individual events* and select these events: *Commit comments*, *Issue comments*, *Pull request*, and *Pushes*.

.... Click *Save changes*.

... On your OpenShift cluster, create a `Secret` object with the personal access token and webhook secret.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic gitlab-webhook-config \
  --from-literal provider.token="<GITLAB_PERSONAL_ACCESS_TOKEN>" \
  --from-literal webhook.secret="<WEBHOOK_SECRET>"
----

... Create a `Repository` CR.
+
.Example: `Repository` CR
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
  url: "https://gitlab.com/owner/repo" <1>
  git_provider:
    secret:
      name: "gitlab-webhook-config"
      key: "provider.token" # Set this if you have a different key in your secret
    webhook_secret:
      name: "gitlab-webhook-config"
      key: "webhook.secret" # Set this if you have a different key for your secret
----
<1> Currently, {pac} does not automatically detects private instances for GitLab. In such cases, specify the API URL under the `git_provider.url` spec. In general, you can use the `git_provider.url` spec to manually override the API URL.

+
[NOTE]
====
* {pac} assumes that the OpenShift `Secret` object and the `Repository` CR are in the same namespace.
====

. Optional: For an existing `Repository` CR, add multiple GitLab Webhook secrets or provide a substitute for a deleted secret.

.. Add a webhook using the `tkn pac` CLI tool.
+
.Example: Adding additional webhook using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook add -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
✓ Setting up GitLab Webhook for Repository https://gitlab.com/owner/repo
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: AeHdHTJVfAeH):  AeHdHTJVfAeH
✓ Webhook has been created on repository owner/repo
🔑 Secret owner-repo has been updated with webhook secert in the repo-pipelines namespace.
----

.. Update the `webhook.secret` key in the existing OpenShift `Secret` object.

. Optional: For an existing `Repository` CR, update the personal access token.

** Update the personal access token using the `tkn pac` CLI tool.
+
.Example: Updating personal access token using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook update-token -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
? Please enter your personal access token:  ****************************************
🔑 Secret owner-repo has been updated with new personal access token in the repo-pipelines namespace.
----

** Alternatively, update the personal access token by modifying the `Repository` CR.

... Find the name of the secret in the `Repository` CR.
+
[source,yaml]
----
...
spec:
  git_provider:
    secret:
      name: "gitlab-webhook-config"
...
----

... Use the `oc patch` command to update the values of the `$NEW_TOKEN` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret gitlab-webhook-config -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----

.Additional resources

* GitLab Webhook documentation on GitLab

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-with-bitbucket-cloud_{context}"]
= Using {pac} with Bitbucket Cloud

[role="_abstract"]
If your organization or project uses Bitbucket Cloud as the preferred platform, you can use {pac} for your repository with a webhook on Bitbucket Cloud.

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* Create an app password on Bitbucket Cloud.

** Check the following boxes to add appropriate permissions to the token:
*** Account: `Email`, `Read`
*** Workspace membership: `Read`, `Write`
*** Projects: `Read`, `Write`
*** Issues: `Read`, `Write`
*** Pull requests: `Read`, `Write`
+
[NOTE]
====
* If you want to configure the webhook using the `tkn pac` CLI, add the `Webhooks`: `Read` and `Write` permission to the token.

* Once generated, save a copy of the password or token in an alternate location.
====

[discrete]
.Procedure

. Configure the webhook and create a `Repository` CR.

** To configure a webhook and create a `Repository` CR _automatically_ using the `tkn pac` CLI tool, use the following command:
+
[source,terminal]
----
$ tkn pac create repo
----
+
.Sample interactive output
[source,terminal]
----
? Enter the Git repository url (default: https://bitbucket.org/workspace/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository workspace-repo has been created in repo-pipelines namespace
✓ Setting up Bitbucket Webhook for Repository https://bitbucket.org/workspace/repo
? Please enter your bitbucket cloud username:  <username>
ℹ ️You now need to create a Bitbucket Cloud app password, please checkout the docs at https://is.gd/fqMHiJ for the required permissions
? Please enter the Bitbucket Cloud app password:  ************************************
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
✓ Webhook has been created on repository workspace/repo
🔑 Webhook Secret workspace-repo has been created in the repo-pipelines namespace.
🔑 Repository CR workspace-repo has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ A basic template has been created in /home/Go/src/bitbucket/repo/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On Bitbucket Cloud, perform the following steps:

.... Use the left navigation pane of your Bitbucket Cloud repository to go to *Repository settings* –> *Webhooks* and click *Add webhook*.

.... Set a *Title*. For example, "Pipelines as Code".

.... Set the *URL* to the {pac} controller public URL.

.... Select these events: *Repository: Push*, *Pull Request: Created*, *Pull Request: Updated*, and *Pull Request: Comment created*.

.... Click *Save*.

... On your OpenShift cluster, create a `Secret` object with the app password in the target namespace.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic bitbucket-cloud-token \
  --from-literal provider.token="<BITBUCKET_APP_PASSWORD>"
----

... Create a `Repository` CR.
+
.Example: `Repository` CR
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
  url: "https://bitbucket.com/workspace/repo"
  branch: "main"
  git_provider:
    user: "<BITBUCKET_USERNAME>" <1>
    secret:
      name: "bitbucket-cloud-token" <2>
      key: "provider.token" # Set this if you have a different key in your secret
----
<1> You can only reference a user by the `ACCOUNT_ID` in an owner file.
<2> {pac} assumes that the secret referred in the `git_provider.secret` spec and the `Repository` CR is in the same namespace.

+
[NOTE]
====
* The `tkn pac create` and `tkn pac bootstrap` commands are not supported on Bitbucket Cloud.

* Bitbucket Cloud does not support webhook secrets. To secure the payload and prevent hijacking of the CI, {pac} fetches the list of Bitbucket Cloud IP addresses and ensures that the webhook receptions come only from those IP addresses.
** To disable the default behavior, set the `bitbucket-cloud-check-source-ip` parameter to `false` in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.
** To allow additional safe IP addresses or networks, add them as comma separated values to the `bitbucket-cloud-additional-source-ip` parameter in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.
====

. Optional: For an existing `Repository` CR, add multiple Bitbucket Cloud Webhook secrets or provide a substitute for a deleted secret.

.. Add a webhook using the `tkn pac` CLI tool.
+
.Example: Adding additional webhook using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook add -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
✓ Setting up Bitbucket Webhook for Repository https://bitbucket.org/workspace/repo
? Please enter your bitbucket cloud username:  <username>
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
✓ Webhook has been created on repository workspace/repo
🔑 Secret workspace-repo has been updated with webhook secret in the repo-pipelines namespace.
----
+
[NOTE]
====
Use the `[-n <namespace>]` option with the `tkn pac webhook add` command only when the `Repository` CR exists in a namespace other than the default namespace.
====

.. Update the `webhook.secret` key in the existing OpenShift `Secret` object.

. Optional: For an existing `Repository` CR, update the personal access token.

** Update the personal access token using the `tkn pac` CLI tool.
+
.Example: Updating personal access token using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook update-token -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
? Please enter your personal access token:  ****************************************
🔑 Secret owner-repo has been updated with new personal access token in the repo-pipelines namespace.
----
+
[NOTE]
====
Use the `[-n <namespace>]` option with the `tkn pac webhook update-token` command only when the `Repository` CR exists in a namespace other than the default namespace.
====

** Alternatively, update the personal access token by modifying the `Repository` CR.

... Find the name of the secret in the `Repository` CR.
+
[source,yaml]
----
...
spec:
  git_provider:
    user: "<BITBUCKET_USERNAME>"
    secret:
      name: "bitbucket-cloud-token"
      key: "provider.token"
...
----

... Use the `oc patch` command to update the values of the `$password` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret bitbucket-cloud-token -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----

.Additional resources

* Creating app password on Bitbucket Cloud
* Introducing Altassian Account ID and Nicknames

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-with-bitbucket-server_{context}"]
= Using {pac} with Bitbucket Server

[role="_abstract"]
If your organization or project uses Bitbucket Server as the preferred platform, you can use {pac} for your repository with a webhook on Bitbucket Server.

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* Generate a personal access token as the manager of the project on Bitbucket Server, and save a copy of it in an alternate location.
+
[NOTE]
====
* The token must have the `PROJECT_ADMIN` and `REPOSITORY_ADMIN` permissions.
* The token must have access to forked repositories in pull requests.
====

[discrete]
.Procedure

. On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

. On Bitbucket Server, perform the following steps:

.. Use the left navigation pane of your Bitbucket Data Center repository to go to *Repository settings* –> *Webhooks* and click *Add webhook*.

.. Set a *Title*. For example, "Pipelines as Code".

.. Set the *URL* to the {pac} controller public URL.

.. Add a webhook secret and save a copy of it in an alternate location. If you have `openssl` installed on your local machine, generate a random secret using the following command:
+
[source,terminal]
----
$ openssl rand -hex 20
----

.. Select the following events:
*** *Repository: Push*
*** *Repository: Modified*
*** *Pull Request: Opened*
*** *Pull Request: Source branch updated*
*** *Pull Request: Comment added*

.. Click *Save*.

. On your OpenShift cluster, create a `Secret` object with the app password in the target namespace.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic bitbucket-server-webhook-config \
  --from-literal provider.token="<PERSONAL_TOKEN>" \
  --from-literal webhook.secret="<WEBHOOK_SECRET>"
----

. Create a `Repository` CR.
+
.Example: `Repository` CR
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
  url: "https://bitbucket.com/workspace/repo"
  git_provider:
    url: "https://bitbucket.server.api.url/rest" <1>
    user: "<BITBUCKET_USERNAME>" <2>
    secret: <3>
      name: "bitbucket-server-webhook-config"
      key: "provider.token" # Set this if you have a different key in your secret
    webhook_secret:
      name: "bitbucket-server-webhook-config"
      key: "webhook.secret" # Set this if you have a different key for your secret
----
<1> Ensure that you have the right Bitbucket Server API URL without the `/api/v1.0` suffix. Usually, the default install has a `/rest` suffix.
<2> You can only reference a user by the `ACCOUNT_ID` in an owner file.
<3> {pac} assumes that the secret referred in the `git_provider.secret` spec and the `Repository` CR is in the same namespace.
+
[NOTE]
====
The `tkn pac create` and `tkn pac bootstrap` commands are not supported on Bitbucket Server.
====

.Additional resources

* Creating personal tokens on Bitbucket Server
* Creating webhooks on Bitbucket server

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="interfacing-pipelines-as-code-with-custom-certificates_{context}"]
= Interfacing {pac} with custom certificates

[role="_abstract"]
To configure {pac} with a Git repository that is accessible with a privately signed or custom certificate, you can expose the certificate to {pac}.

.Procedure

* If you have installed {pac} using the {pipelines-title} Operator, you can add your custom certificate to the cluster using the `Proxy` object. The Operator exposes the certificate in all {pipelines-title} components and workloads, including {pac}.

.Additional resources

* Enabling the cluster-wide proxy

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-repository-crd-with-pipelines-as-code_{context}"]
= Using the Repository custom resource definition (CRD) with {pac}

[role="_abstract"]
The `Repository` custom resource (CR) has the following primary functions:

* Inform {pac} about processing an event from a URL.
* Inform {pac} about the namespace for the pipeline runs.
* Reference an API secret, username, or an API URL necessary for Git provider platforms when using webhook methods.
* Provide the last pipeline run status for a repository.

You can use the `tkn pac` CLI or other alternative methods to create a `Repository` CR inside the target namespace. For example:

[source,terminal]
----
cat <<EOF|kubectl create -n my-pipeline-ci -f- <1>

apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: project-repository
spec:
  url: "https://github.com/<repository>/<project>"
EOF
----
<1> `my-pipeline-ci` is the target namespace.

Whenever there is an event coming from the URL such as `https://github.com/<repository>/<project>`, {pac} matches it and starts checking out the content of the `<repository>/<project>` repository for pipeline run to match the content in the `.tekton/` directory.

[NOTE]
====
* You must create the `Repository` CRD in the same namespace where pipelines associated with the source code repository will be executed; it cannot target a different namespace.

* If multiple `Repository` CRDs match the same event, {pac} will process only the oldest one. If you need to match a specific namespace, add the `pipelinesascode.tekton.dev/target-namespace: "<mynamespace>"` annotation. Such explicit targeting prevents a malicious actor from executing a pipeline run in a namespace to which they do not have access.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="setting-concurrency-limits-in-repository-crd_{context}"]
= Setting concurrency limits

[role="_abstract"]
You can use the `concurrency_limit` spec in the `Repository` custom resource definition (CRD) to define the maximum number of pipeline runs running simultaneously for a repository.

[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
# ...
  concurrency_limit: <number>
# ...

----

If there are multiple pipeline runs matching an event, the pipeline runs that match the event start in an alphabetical order.

For example, if you have three pipeline runs in the `.tekton` directory and you create a pull request with a `concurrency_limit` of `1` in the repository configuration, then all the pipeline runs are executed in an alphabetical order. At any given time, only one pipeline run is in the running state while the rest are queued.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="changing-source-branch-in-repository-crd_{context}"]
= Changing the source branch for the pipeline definition

[role="_abstract"]
By default, when processing a push event or a pull request event, {pac} fetches the pipeline definition from the branch that triggered the event. You can use the `pipelinerun_provenance` setting in the `Repository` custom resource definition (CRD) to fetch the definition from the default branch configured on the Git repository provider, such as `main`, `master`, or `trunk`.

[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
# ...
  settings:
    pipelinerun_provenance: "default_branch"
# ...
----

[NOTE]
====
You can use this setting as a security precaution. With the default behaviour, {pac} uses the pipeline definition in the submitted pull request. With the `default-branch` setting, the pipeline definition must be merged into the default branch before it is run. This requirement ensures maximum possible verification of any changes during merge review.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="op-custom-parameter-expansion_{context}"]
= Custom parameter expansion

You can use {pac} to expand a custom parameter within your `PipelineRun` resource by using the `params` field. You can specify a value for the custom parameter inside the template of the `Repository` custom resource (CR). The specified value replaces the custom parameter in your pipeline run.

You can use custom parameters in the following scenarios:

* To define a URL parameter, such as a registry URL that varies based on a push or a pull request.
* To define a parameter, such as an account UUID that an administrator can manage without necessitating changes to the `PipelineRun` execution in the Git repository.

[NOTE]
====
Use the custom parameter expansion feature only when you cannot use the Tekton `PipelineRun` parameters because Tekton parameters are defined in a `Pipeline` resource and customized alongside it inside a Git repository. However, custom parameters are defined and customized where the `Repository` CR is located. So, you cannot manage your CI/CD pipeline from a single point.
====

The following example shows a custom parameter named `company` in the `Repository` CR:

[source,yaml]
----
...
spec:
  params:
    - name: company
      value: "ABC Company"
...
----

The value `ABC Company` replaces the parameter name `company` in your pipeline run and in the remotely fetched tasks.

You can also retrieve the value for a custom parameter from a Kubernetes secret, as shown in the following example:

[source,yaml]
----
...
spec:
  params:
    - name: company
      secretRef:
        name: my-secret
        key: companyname
...
----

{pac} parses and uses custom parameters in the following manner:

* If you have a `value` and a `secretRef` defined, {pac} uses the `value`.
* If you do not have a `name` in the `params` section, {pac} does not parse the parameter.
* If you have multiple `params` with the same `name`, {pac} uses the last parameter.

You can also define a custom parameter and use its expansion only when specified conditions were matched for a CEL filter. The following example shows a CEL filter applicable on a custom parameter named `company` when a pull request event is triggered:

[source,yaml]
----
...
spec:
  params:
    - name: company
      value: "ABC Company"
      filter:
        - name: event
          value: |
      pac.event_type == "pull_request"
...
----

[NOTE]
====
When you have multiple parameters with the same name and different filters, {pac} uses the first parameter that matches the filter. So, {pac} allows you to expand parameters according to different event types. For example, you can combine a push and a pull request event.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-pipelines-as-code-resolver_{context}"]
= Using the {pac} resolver

[role="_abstract"]
The {pac} resolver ensures that a running pipeline run does not conflict with others.

To split your pipeline and pipeline run, store the files in the `.tekton/` directory or its subdirectories.

If {pac} observes a pipeline run with a reference to a task or a pipeline in any YAML file located in the `.tekton/` directory, {pac} automatically resolves the referenced task to provide a single pipeline run with an embedded spec in a `PipelineRun` object.

If {pac} cannot resolve the referenced tasks in the `Pipeline` or `PipelineSpec` definition, the run fails before applying any changes to the cluster. You can see the issue on your Git provider platform and inside the events of the target namespace where the `Repository` CR is located.

The resolver skips resolving if it observes the following type of tasks:

* A reference to a cluster task.
* A task or pipeline bundle.
* A custom task with an API version that does not have a `tekton.dev/` prefix.

The resolver uses such tasks literally, without any transformation.

To test your pipeline run locally before sending it in a pull request, use the `tkn pac resolve` command.

You can also reference remote pipelines and tasks.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-remote-task-annotations-with-pipelines-as-code_{context}"]
= Using remote task annotations with {pac}

[role="_abstract"]
{pac} supports fetching remote tasks or pipelines by using annotations in a pipeline run. If you reference a remote task in a pipeline run, or a pipeline in a `PipelineRun` or a `PipelineSpec` object, the {pac} resolver automatically includes it. If there is any error while fetching the remote tasks or parsing them, {pac} stops processing the tasks.

To include remote tasks, refer to the following examples of annotation:

[discrete]
.Reference remote tasks in {tekton-hub}

* Reference a single remote task in {tekton-hub}.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "git-clone" <1>
...
----
<1> {pac} includes the latest version of the task from the {tekton-hub}.

* Reference multiple remote tasks from {tekton-hub}

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "[git-clone, golang-test, tkn]"
...
----

* Reference multiple remote tasks from {tekton-hub} using the `-<NUMBER>` suffix.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "git-clone"
  pipelinesascode.tekton.dev/task-1: "golang-test"
  pipelinesascode.tekton.dev/task-2: "tkn" <1>
...
----
<1> By default, {pac} interprets the string as the latest task to fetch from {tekton-hub}.

* Reference a specific version of a remote task from {tekton-hub}.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "[git-clone:0.1]" <1>
...
----
<1> Refers to the `0.1` version of the `git-clone` remote task from {tekton-hub}.

[discrete]
.Remote tasks using URLs

[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "<https://remote.url/task.yaml>" <1>
...
----
<1> The public URL to the remote task.
+
[NOTE]
====
* If you use GitHub and the remote task URL uses the same host as the `Repository` custom resource definition (CRD), {pac} uses the GitHub token and fetches the URL using the GitHub API.
+
For example, if you have a repository URL similar to `https://github.com/<organization>/<repository>` and the remote HTTP URL references a GitHub blob similar to `https://github.com/<organization>/<repository>/blob/<mainbranch>/<path>/<file>`, {pac} fetches the task definition files from that private repository with the GitHub App token.
+
When you work on a public GitHub repository, {pac} acts similarly for a GitHub raw URL such as `https://raw.githubusercontent.com/<organization>/<repository>/<mainbranch>/<path>/<file>`.

* GitHub App tokens are scoped to the owner or organization where the repository is located. When you use the GitHub webhook method, you can fetch any private or public repository on any organization where the personal token is allowed.
====

[discrete]
.Reference a task from a YAML file inside your repository

[source,yaml]
----
...
pipelinesascode.tekton.dev/task: "<share/tasks/git-clone.yaml>" <1>
...
----
<1> Relative path to the local file containing the task definition.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-remote-pipeline-annotations-with-pipelines-as-code_{context}"]
= Using remote pipeline annotations with {pac}

[role="_abstract"]
You can share a pipeline definition across multiple repositories by using the remote pipeline annotation.

[source,yaml]
----
...
    pipelinesascode.tekton.dev/pipeline: "<https://git.provider/raw/pipeline.yaml>" <1>
...
----
<1> URL to the remote pipeline definition. You can also provide locations for files inside the same repository.

[NOTE]
====
You can reference only one pipeline definition using the annotation.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="creating-pipeline-run-using-pipelines-as-code_{context}"]
= Creating a pipeline run using {pac}

[role="_abstract"]
To run pipelines using {pac}, you can create pipelines definitions or templates as YAML files in the `.tekton/` directory of the repository. You can reference YAML files in other repositories using remote URLs, but pipeline runs are only triggered by events in the repository containing the `.tekton/` directory.

The {pac} resolver bundles the pipeline runs with all tasks as a single pipeline run without external dependencies.

[NOTE]
====
* For pipelines, use at least one pipeline run with a spec, or a separated `Pipeline` object.
* For tasks, embed task spec inside a pipeline, or define it separately as a Task object.
====

[discrete]
.Parameterizing commits and URLs

You can specify the parameters of your commit and URL by using dynamic, expandable variables with the {{<var>}} format. Currently, you can use the following variables:

* `{{repo_owner}}`: The repository owner.
* `{{repo_name}}`: The repository name.
* `{{repo_url}}`: The repository full URL.
* `{{revision}}`: Full SHA revision of a commit.
* `{{sender}}`: The username or account id of the sender of the commit.
* `{{source_branch}}`: The branch name where the event originated.
* `{{target_branch}}`: The branch name that the event targets. For push events, it's the same as the `source_branch`.
* `{{pull_request_number}}`: The pull or merge request number, defined only for a `pull_request` event type.
* `{{git_auth_secret}}`: The secret name that is generated automatically with Git provider's token for checking out private repos.

[discrete]
.Matching an event to a pipeline run

You can match different Git provider events with each pipeline by using special annotations on the pipeline run. If there are multiple pipeline runs matching an event, {pac} runs them in parallel and posts the results to the Git provider as soon a pipeline run finishes.

[discrete]
.Matching a pull event to a pipeline run

You can use the following example to match the `pipeline-pr-main` pipeline with a `pull_request` event that targets the `main` branch:

[source,yaml]
----
...
  metadata:
    name: pipeline-pr-main
  annotations:
    pipelinesascode.tekton.dev/on-target-branch: "[main]" <1>
    pipelinesascode.tekton.dev/on-event: "[pull_request]"
...
----
<1> You can specify multiple branches by adding comma-separated entries. For example, `"[main, release-nightly]"`. In addition, you can specify the following:
* Full references to branches such as `"refs/heads/main"`
* Globs with pattern matching such as `"refs/heads/\*"`
* Tags such as `"refs/tags/1.\*"`

[discrete]
.Matching a push event to a pipeline run

You can use the following example to match the `pipeline-push-on-main` pipeline with a `push` event targeting the `refs/heads/main` branch:

[source,yaml]
----
...
  metadata:
    name: pipeline-push-on-main
  annotations:
    pipelinesascode.tekton.dev/on-target-branch: "[refs/heads/main]" <1>
    pipelinesascode.tekton.dev/on-event: "[push]"
...
----
<1> You can specifiy multiple branches by adding comma-separated entries. For example, `"[main, release-nightly]"`. In addition, you can specify the following:
* Full references to branches such as `"refs/heads/main"`
* Globs with pattern matching such as `"refs/heads/\*"`
* Tags such as `"refs/tags/1.\*"`

[discrete]
.Advanced event matching

{pac} supports using Common Expression Language (CEL) based filtering for advanced event matching. If you have the `pipelinesascode.tekton.dev/on-cel-expression` annotation in your pipeline run, {pac} uses the CEL expression and skips the `on-target-branch` annotation. Compared to the simple `on-target-branch` annotation matching, the CEL expressions allow complex filtering and negation.

To use CEL-based filtering with {pac}, consider the following examples of annotations:

* To match a `pull_request` event targeting the `main` branch and coming from the `wip` branch:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && target_branch == "main" && source_branch == "wip"
...
----

* To run a pipeline only if a path has changed, you can use the `.pathChanged` suffix function with a glob pattern:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && "docs/\*.md".pathChanged() <1>
...
----
<1> Matches all markdown files in the `docs` directory.

* To match all pull requests starting with the title `[DOWNSTREAM]`:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request && event_title.startsWith("[DOWNSTREAM]")
...
----

* To run a pipeline on a `pull_request` event, but skip the `experimental` branch:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && target_branch != experimental"
...
----

For advanced CEL-based filtering while using {pac}, you can use the following fields and suffix functions:

* `event`: A `push` or `pull_request` event.
* `target_branch`: The target branch.
* `source_branch`: The branch of origin of a `pull_request` event. For `push` events, it is same as the `target_branch`.
* `event_title`: Matches the title of the event, such as the commit title for a `push` event, and the title of a pull or merge request for a `pull_request` event. Currently, only GitHub, Gitlab, and Bitbucket Cloud are the supported providers.
* `.pathChanged`: A suffix function to a string. The string can be a glob of a path to check if the path has changed. Currently, only GitHub and Gitlab are supported as providers.

[discrete]
.Using the temporary GitHub App token for Github API operations

You can use the temporary installation token generated by {pac} from GitHub App to access the GitHub API. The token value is stored in the temporary `{{git_auth_secret}}` dynamic variable generated for private repositories in the `git-provider-token` key.

For example, to add a comment to a pull request, you can use the `github-add-comment` task from {tekton-hub} using a {pac} annotation:

[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "github-add-comment"
...
----

You can then add a task to the `tasks` section or `finally` tasks in the pipeline run definition:

[source,yaml]
----
[...]
tasks:
  - name:
      taskRef:
        name: github-add-comment
      params:
        - name: REQUEST_URL
          value: "{{ repo_url }}/pull/{{ pull_request_number }}" <1>
        - name: COMMENT_OR_FILE
          value: "Pipelines as Code IS GREAT!"
        - name: GITHUB_TOKEN_SECRET_NAME
          value: "{{ git_auth_secret }}"
        - name: GITHUB_TOKEN_SECRET_KEY
          value: "git-provider-token"
...
----
<1> By using the dynamic variables, you can reuse this snippet template for any pull request from any repository.

[NOTE]
====
On GitHub Apps, the generated installation token is available for 8 hours and scoped to the repository from where the events originate unless configured differently on the cluster.
====

.Additional resources

* CEL language specification

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="running-pipeline-run-using-pipelines-as-code_{context}"]
= Running a pipeline run using {pac}

[role="_abstract"]
With default configuration, {pac} runs any pipeline run in the `.tekton/` directory of the default branch of repository, when specified events such as pull request or push occurs on the repository. For example, if a pipeline run on the default branch has the annotation `pipelinesascode.tekton.dev/on-event: "[pull_request]"`, it will run whenever a pull request event occurs.

In the event of a pull request or a merge request, {pac} also runs pipelines from branches other than the default branch, if the following conditions are met by the author of the pull request:

* The author is the owner of the repository.
* The author is a collaborator on the repository.
* The author is a public member on the organization of the repository.
* The pull request author is listed in an `OWNER` file located in the repository root of the `main` branch as defined in the GitHub configuration for the repository. Also, the  pull request author is added to either `approvers` or `reviewers` section. For example, if an author is listed in the `approvers` section, then a pull request raised by that author starts the pipeline run.

[source,yaml]
----
...
  approvers:
    - approved
...
----

If the pull request author does not meet the requirements, another user who meets the requirements can comment `/ok-to-test` on the pull request, and start the pipeline run.

[discrete]
.Pipeline run execution
A pipeline run always runs in the namespace of the `Repository` custom resource definition (CRD) associated with the repository that generated the event.

You can observe the execution of your pipeline runs using the `tkn pac` CLI tool.

* To follow the execution of the last pipeline run, use the following example:
+
[source,terminal]
----
$ tkn pac logs -n <my-pipeline-ci> -L <1>
----
<1> `my-pipeline-ci` is the namespace for the `Repository` CRD.

* To follow the execution of any pipeline run interactively, use the following example:
+
[source,terminal]
----
$ tkn pac logs -n <my-pipeline-ci> <1>
----
<1> `my-pipeline-ci` is the namespace for the `Repository` CRD.
If you need to view a pipeline run other than the last one, you can use the `tkn pac logs` command to select a `PipelineRun` attached to the repository:

If you have configured {pac} with a GitHub App, {pac} posts a URL in the *Checks* tab of the GitHub App. You can click the URL and follow the pipeline execution.

[discrete]
.Restarting a pipeline run

You can restart a pipeline run with no events, such as sending a new commit to your branch or raising a pull request. On a GitHub App, go to the *Checks* tab and click *Re-run*.

If you target a pull or merge request, use the following comments inside your pull request to restart all or specific pipeline runs:

* The `/retest` comment restarts all pipeline runs.

* The `/retest <pipelinerun-name>` comment restarts a specific pipeline run.

* The `/cancel` comment cancels all pipeline runs.

* The `/cancel <pipelinerun-name>` comment cancels a specific pipeline run.

The results of the comments are visible under the *Checks* tab of a GitHub App.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="monitoring-pipeline-run-status-using-pipelines-as-code_{context}"]
= Monitoring pipeline run status using {pac}

[role="_abstract"]
Depending on the context and supported tools, you can monitor the status of a pipeline run in different ways.

[discrete]
.Status on GitHub Apps
When a pipeline run finishes, the status is added in the *Check* tabs with limited information on how long each task of your pipeline took, and the output of the `tkn pipelinerun describe` command.

[discrete]
.Log error snippet
When {pac} detects an error in one of the tasks of a pipeline, a small snippet consisting of the last 3 lines in the task breakdown of the first failed task is displayed.

[NOTE]
====
{pac} avoids leaking secrets by looking into the pipeline run and replacing secret values with hidden characters. However, {pac} cannot hide secrets coming from workspaces and envFrom source.
====

[discrete]
.Annotations for log error snippets

In the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec, you can set the `error-detection-from-container-logs` parameter to `true`. In this case, {pac} detects the errors from the container logs and adds them as annotations on the pull request where the error occurred.

Currently, {pac} supports only the simple cases where the error looks like `makefile` or `grep` output of the following format:
[source,yaml]
----
<filename>:<line>:<column>: <error message>
----

You can customize the regular expression used to detect the errors with the `error-detection-simple-regexp` parameter. The regular expression uses named groups to give flexibility on how to specify the matching. The groups needed to match are `filename`, `line`, and `error`. You can view the {pac} config map for the default regular expression.

[NOTE]
====
By default, {pac} scans only the last 50 lines of the container logs. You can increase this value in the `error-detection-max-number-of-lines` field or set `-1` for an unlimited number of lines. However, such configurations may increase the memory usage of the watcher.
====

[discrete]
.Status for webhook
For webhook, when the event is a pull request, the status is added as a comment on the pull or merge request.

[discrete]
.Failures
If a namespace is matched to a `Repository` custom resource definition (CRD), {pac} emits its failure log messages in the Kubernetes events inside the namespace.

[discrete]
.Status associated with Repository CRD
The last 5 status messages for a pipeline run is stored inside the `Repository` custom resource.

[source,terminal]
----
$ oc get repo -n <pipelines-as-code-ci>
----

[source,terminal]
----
NAME                  URL                                                        NAMESPACE             SUCCEEDED   REASON      STARTTIME   COMPLETIONTIME
pipelines-as-code-ci   https://github.com/openshift-pipelines/pipelines-as-code   pipelines-as-code-ci   True        Succeeded   59m         56m
----

Using the `tkn pac describe` command, you can extract the status of the runs associated with your repository and its metadata.

[discrete]
.Notifications
{pac} does not manage notifications. If you need to have notifications, use the `finally` feature of pipelines.

.Additional resources

* An example task to send Slack messages on success or failure
* An example of a pipeline run with `finally` tasks triggered on push events

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-private-repositories-with-pipelines-as-code_{context}"]
= Using private repositories with {pac}

[role="_abstract"]
{pac} supports private repositories by creating or updating a secret in the target namespace with the user token. The `git-clone` task from {tekton-hub} uses the user token to clone private repositories.

Whenever {pac} creates a new pipeline run in the target namespace, it creates or updates a secret with the  `pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>` format.

You must reference the secret with the `basic-auth` workspace in your pipeline run and pipeline definitions, which is then passed on to the `git-clone` task.

[source,yaml]
----
...
  workspace:
  - name: basic-auth
    secret:
      secretName: "{{ git_auth_secret }}"
...
----

In the pipeline, you can reference the `basic-auth` workspace for the `git-clone` task to reuse:

[source,yaml]
----
...
workspaces:
  - name basic-auth
params:
    - name: repo_url
    - name: revision
...
tasks:
  workspaces:
    - name: basic-auth
      workspace: basic-auth
  ...
  tasks:
  - name: git-clone-from-catalog
      taskRef:
        name: git-clone <1>
      params:
        - name: url
          value: $(params.repo_url)
        - name: revision
          value: $(params.revision)
...
----
<1> The `git-clone` task picks up the `basic-auth` workspace and uses it to clone the private repository.

You can modify this configuration by setting the `secret-auto-create` parameter to either a `false` or `true` value, as required, in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.

.Additional resources

* An example of the `git-clone` task used for cloning private repositories

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="cleaning-up-pipeline-run-using-pipelines-as-code_{context}"]
= Cleaning up pipeline run using {pac}

[role="_abstract"]

There can be many pipeline runs in a user namespace. By setting the `max-keep-runs` annotation, you can configure {pac} to retain a limited number of pipeline runs that matches an event. For example:

[source,yaml]
----
...
  pipelinesascode.tekton.dev/max-keep-runs: "<max_number>" <1>
...
----
<1> {pac} starts cleaning up right after it finishes a successful execution, retaining only the maximum number of pipeline runs configured using the annotation.
+
[NOTE]
====
* {pac} skips cleaning the running pipelines but cleans up the pipeline runs with an unknown status.
* {pac} skips cleaning a failed pull request.
====

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="using-incoming-webhook-with-pipelines-as-code_{context}"]
= Using incoming webhook with {pac}

[role="_abstract"]
Using an incoming webhook URL and a shared secret, you can start a pipeline run in a repository.

To use incoming webhooks, specify the following within the `spec` section of the `Repository` custom resource definition (CRD):

* The incoming webhook URL that {pac} matches.
* The Git provider and the user token. Currently, {pac} supports `github`, `gitlab`, and `bitbucket-cloud`.
+
[NOTE]
====
When using incoming webhook URLs in the context of GitHub app, you must specify the token.
====
* The target branches and a secret for the incoming webhook URL.

.Example: `Repository` CRD with incoming webhook
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: repo
  namespace: ns
spec:
  url: "https://github.com/owner/repo"
  git_provider:
    type: github
    secret:
      name: "owner-token"
  incoming:
    - targets:
      - main
      secret:
        name: repo-incoming-secret
      type: webhook-url
----

.Example: The `repo-incoming-secret` secret for incoming webhook
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: repo-incoming-secret
  namespace: ns
type: Opaque
stringData:
  secret: <very-secure-shared-secret>
----

To trigger a pipeline run located in the `.tekton` directory of a Git repository, use the following command:

[source,terminal]
----
$ curl -X POST 'https://control.pac.url/incoming?secret=very-secure-shared-secret&repository=repo&branch=main&pipelinerun=target_pipelinerun'
----

{pac} matches the incoming URL and treats it as a `push` event. However, {pac} does not report status of the pipeline runs triggered by this command.

To get a report or a notification, add it directly with a `finally` task to your pipeline. Alternatively, you can inspect the `Repository` CRD with the `tkn pac` CLI tool.

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="customizing-pipelines-as-code-configuration_{context}"]
= Customizing {pac} configuration

[role="_abstract"]
To customize {pac}, cluster administrators can configure the following parameters in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec:

.Customizing {pac} configuration
[options="header"]
|===

| Parameter | Description | Default

| `application-name` | The name of the application. For example, the name displayed in the GitHub Checks labels. | `"Pipelines as Code CI"`

| `secret-auto-create` | Indicates whether or not a secret should be automatically created using the token generated in the GitHub application. This secret can then be used with private repositories. | `enabled`

| `remote-tasks` | When enabled, allows remote tasks from pipeline run annotations. | `enabled`

| `hub-url` | The base URL for the Tekton Hub API. | `https://hub.tekton.dev/`

| `hub-catalog-name` | The Tekton Hub catalog name. | `tekton`

| `tekton-dashboard-url` | The URL of the Tekton Hub dashboard. {pac} uses this URL to generate a `PipelineRun` URL on the Tekton Hub dashboard.  | NA

| `bitbucket-cloud-check-source-ip` | Indicates whether to secure the service requests by querying IP ranges for a public Bitbucket. Changing the parameter's default value might result into a security issue. | `enabled`

| `bitbucket-cloud-additional-source-ip` | Indicates whether to provide an additional set of IP ranges or networks, which are separated by commas. | NA

| `max-keep-run-upper-limit` | A maximum limit for the `max-keep-run` value for a pipeline run. | NA

| `default-max-keep-runs` | A default limit for the `max-keep-run` value for a pipeline run. If defined, the value is applied to all pipeline runs that do not have a `max-keep-run` annotation. | NA

| `auto-configure-new-github-repo` | Configures new GitHub repositories automatically. {pac} sets up a namespace and creates a custom resource for your repository. This parameter is only supported with GitHub applications. | `disabled`

| `auto-configure-repo-namespace-template` | Configures a template to automatically generate the namespace for your new repository, if `auto-configure-new-github-repo` is enabled. | `{repo_name}-pipelines`

| `error-log-snippet` | Enables or disables the view of a log snippet for the failed tasks, with an error in a pipeline. You can disable this parameter in the case of data leakage from your pipeline. | `true`

| `error-detection-from-container-logs` | Enables or disables the inspection of container logs to detect error message and expose them as annotations on the pull request. This setting applies only if you are using the GitHub app. | `true`

| `error-detection-max-number-of-lines` | The maximum number of lines inspected in the container logs to search for error messages. Set to `-1` to inspect an unlimited number of lines. | 50

| `secret-github-app-token-scoped` | If set to `true`, the GitHub access token that {pac} generates using the GitHub app is scoped only to the repository from which {pac} fetches the pipeline definition. If set to `false`, you can use both the `TektonConfig` custom resource and the `Repository` custom resource to scope the token to additional repositories. | `true`

| `secret-github-app-scope-extra-repos` | Additional repositories for scoping the generated GitHub access token. |

|===

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="pipelines-as-code-command-reference_{context}"]
= {pac} command reference

[role="_abstract"]
The `tkn pac` CLI tool offers the following capabilities:

* Bootstrap {pac} installation and configuration.
* Create a new {pac} repository.
* List all {pac} repositories.
* Describe a {pac} repository and the associated runs.
* Generate a simple pipeline run to get started.
* Resolve a pipeline run as if it was executed by {pac}.

[TIP]
====
You can use the commands corresponding to the capabilities for testing and experimentation, so that you do not have to make changes to the Git repository containing the application source code.
====

== Basic syntax

[source,terminal]
----
$ tkn pac [command or options] [arguments]
----

== Global options

[source,terminal]
----
$ tkn pac --help
----

== Utility commands

=== bootstrap

.Bootstrapping {pac} installation and configuration
[options="header"]
|===

| Command | Description

| `tkn pac bootstrap` | Installs and configures {pac} for Git repository hosting service providers, such as GitHub and GitHub Enterprise.

| `tkn pac bootstrap --nightly` | Installs the nightly build of {pac}.

| `tkn pac bootstrap --route-url <public_url_to_ingress_spec>` | Overrides the OpenShift route URL.

By default, `tkn pac bootstrap` detects the OpenShift route, which is automatically associated with the {pac} controller service.

If you do not have an OpenShift Container Platform cluster, it asks you for the public URL that points to the ingress endpoint.

| `tkn pac bootstrap github-app` | Create a GitHub application and secrets in the `openshift-pipelines` namespace.

|===

=== repository

.Managing {pac} repositories
[options="header"]
|===

| Command | Description

| `tkn pac create repository` | Creates a new {pac} repository and a namespace based on the pipeline run template.

| `tkn pac list` | Lists all the {pac} repositories and displays the last status of the associated runs.

| `tkn pac repo describe` | Describes a {pac} repository and the associated runs.

|===

=== generate

.Generating pipeline runs using {pac}
[options="header"]
|===

| Command | Description

| `tkn pac generate` | Generates a simple pipeline run.

When executed from the directory containing the source code, it automatically detects current Git information.

In addition, it uses basic language detection capability and adds extra tasks depending on the language.

For example, if it detects a `setup.py` file at the repository root, the pylint task is automatically added to the generated pipeline run.

|===

=== resolve

.Resolving and executing pipeline runs using {pac}
[options="header"]
|===

| Command | Description

| `tkn pac resolve` | Executes a pipeline run as if it is owned by the {pac} on service.

| `tkn pac resolve -f .tekton/pull-request.yaml \| oc apply -f -` | Displays the status of a live pipeline run that uses the template in `.tekton/pull-request.yaml`.

Combined with a Kubernetes installation running on your local machine, you can observe the pipeline run without generating a new commit.

If you run the command from a source code repository, it attempts to detect the current Git information and automatically resolve parameters such as current revision or branch.

| `tkn pac resolve -f .tekton/pr.yaml -p revision=main -p repo_name=<repository_name>` | Executes a pipeline run by overriding default parameter values derived from the Git repository.

The `-f` option can also accept a directory path and apply the `tkn pac resolve` command on all `.yaml` or `.yml` files in that directory. You can also use the `-f` flag multiple times in the same command.

You can override the default information gathered from the Git repository by specifying parameter values using the `-p` option. For example, you can use a Git branch as a revision and a different repository name.

|===

// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

[id="splitting-pipelines-as-code-logs-by-namespace_{context}"]
= Splitting {pac} logs by namespace

The logs contain the namespace information to make it possible to filter logs or split the logs by a particular namespace. For example, to view the logs related to the `mynamespace` namespace, enter the following command:

[source,terminal]
----
$ oc logs pipelines-as-code-controller-<unique-id> -n openshift-pipelines | grep mynamespace <1>
----
<1> Replace `pipelines-as-code-controller-<unique-id>` with the {pac} controller name.

[role="_additional-resources"]
[id="additional-resources-pac"]
== Additional resources

* An example of the `.tekton/` directory in the Pipelines as Code repository

* Installing {pipelines-shortname}

* Installing tkn

* {pipelines-title} release notes

* Creating applications using the Developer perspective
