---
title: "Migrating from Jenkins to OpenShift Pipelines or Tekton"
type: reference
domain: openshift
slug: cicd-4-22-migrating-from-jenkins-to-openshift-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/migrating-from-jenkins-to-openshift-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Migrating from Jenkins to OpenShift Pipelines or Tekton

//Jenkins-Tekton-Migration
[id="migrating-from-jenkins-to-openshift-pipelines_{context}"]
= Migrating from Jenkins to OpenShift Pipelines or Tekton

You can migrate your CI/CD workflows from Jenkins to {pipelines-title}, a cloud-native CI/CD experience based on the Tekton project.

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-comparison-of-jenkins-and-openshift-pipelines-concepts_{context}"]
= Comparison of Jenkins and {pipelines-shortname} concepts

You can review and compare the following equivalent terms used in Jenkins and {pipelines-shortname}.

== Jenkins terminology
Jenkins offers declarative and scripted pipelines that are extensible using shared libraries and plugins. Some basic terms in Jenkins are as follows:

* *Pipeline*: Automates the entire process of building, testing, and deploying applications by using Groovy syntax.
* *Node*: A machine capable of either orchestrating or executing a scripted pipeline.
* *Stage*: A conceptually distinct subset of tasks performed in a pipeline. Plugins or user interfaces often use this block to display the status or progress of tasks.
* **Step**: A single task that specifies the exact action to be taken, either by using a command or a script.

== {pipelines-shortname} terminology
{pipelines-shortname} uses YAML syntax for declarative pipelines and consists of tasks. Some basic terms in {pipelines-shortname} are as follows:

* **Pipeline**: A set of tasks in a series, in parallel, or both.
* **Task**: A sequence of steps as commands, binaries, or scripts.
* **PipelineRun**: Execution of a pipeline with one or more tasks.
* **TaskRun**: Execution of a task with one or more steps.
+
[NOTE]
====
You can initiate a PipelineRun or a TaskRun with a set of inputs such as parameters and workspaces, and the execution results in a set of outputs and artifacts.
====
* **Workspace**: In {pipelines-shortname}, workspaces are conceptual blocks that serve the following purposes:

** Storage of inputs, outputs, and build artifacts.

** Common space to share data among tasks.

** Mount points for credentials held in secrets, configurations held in config maps, and common tools shared by an organization.

+
[NOTE]
====
In Jenkins, there is no direct equivalent of {pipelines-shortname} workspaces. You can think of the control node as a workspace, as it stores the cloned code repository, build history, and artifacts. When a job is assigned to a different node, the cloned code and the generated artifacts are stored in that node, but the control node maintains the build history.
====

== Mapping of concepts
The building blocks of Jenkins and {pipelines-shortname} are not equivalent, and a specific comparison does not provide a technically accurate mapping. The following terms and concepts in Jenkins and {pipelines-shortname} correlate in general:

.Jenkins and {pipelines-shortname} - basic comparison
[cols="1,1",options="header"]
|===
|Jenkins|{pipelines-shortname}
|Pipeline|Pipeline and PipelineRun
|Stage|Task
|Step|A step in a task
|===

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-migrating-a-sample-pipeline-from-jenkins-to-openshift-pipelines_{context}"]
= Migrating a sample pipeline from Jenkins to {pipelines-shortname}

You can use the following equivalent examples to help migrate your build, test, and deploy pipelines from Jenkins to {pipelines-shortname}.

== Jenkins pipeline
Consider a Jenkins pipeline written in Groovy for building, testing, and deploying:
[source,groovy,subs="attributes+"]
----
pipeline {
   agent any
   stages {
       stage('Build') {
           steps {
               sh 'make'
           }
       }
       stage('Test'){
           steps {
               sh 'make check'
               junit 'reports/**/*.xml'
           }
       }
       stage('Deploy') {
           steps {
               sh 'make publish'
           }
       }
   }
}
----

== {pipelines-shortname} pipeline

To create a pipeline in {pipelines-shortname} that is equivalent to the preceding Jenkins pipeline, you create the following three tasks:

.Example `build` task YAML definition file
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: myproject-build
spec:
  workspaces:
  - name: source
  steps:
  - image: my-ci-image
    command: ["make"]
    workingDir: $(workspaces.source.path)
----

.Example `test` task YAML definition file
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: myproject-test
spec:
  workspaces:
  - name: source
  steps:
  - image: my-ci-image
    command: ["make check"]
    workingDir: $(workspaces.source.path)
  - image: junit-report-image
    script: |
      #!/usr/bin/env bash
      junit-report reports/**/*.xml
    workingDir: $(workspaces.source.path)
----

.Example `deploy` task YAML definition file
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: myprojectd-deploy
spec:
  workspaces:
  - name: source
  steps:
  - image: my-deploy-image
    command: ["make deploy"]
    workingDir: $(workspaces.source.path)
----

You can combine the three tasks sequentially to form a pipeline in {pipelines-shortname}:

.Example: {pipelines-shortname} pipeline for building, testing, and deployment
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: myproject-pipeline
spec:
  workspaces:
  - name: shared-dir
  tasks:
  - name: build
    taskRef:
      name: myproject-build
    workspaces:
    - name: source
      workspace: shared-dir
  - name: test
    taskRef:
      name: myproject-test
    workspaces:
    - name: source
      workspace: shared-dir
  - name: deploy
    taskRef:
      name: myproject-deploy
    workspaces:
    - name: source
      workspace: shared-dir
----

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-migrating-from-jenkins-plugins-to-openshift-pipelines-hub-tasks_{context}"]
= Migrating from Jenkins plugins to Tekton Hub tasks

You can extend the capability of Jenkins by using plugins. To achieve similar extensibility in {pipelines-shortname}, use any of the tasks available from Tekton Hub.

For example, consider the git-clone task in Tekton Hub, which corresponds to the git plugin for Jenkins.

.Example: `git-clone` task from Tekton Hub
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
 name: demo-pipeline
spec:
 params:
   - name: repo_url
   - name: revision
 workspaces:
   - name: source
 tasks:
   - name: fetch-from-git
     taskRef:
       name: git-clone
     params:
       - name: url
         value: $(params.repo_url)
       - name: revision
         value: $(params.revision)
     workspaces:
     - name: output
       workspace: source
----

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-extending-openshift-pipelines-capabilities-using-custom-tasks-and-scripts_{context}"]
= Extending {pipelines-shortname} capabilities using custom tasks and scripts

In {pipelines-shortname}, if you do not find the right task in Tekton Hub, or need greater control over tasks, you can create custom tasks and scripts to extend the capabilities of {pipelines-shortname}.

.Example: A custom task for running the `maven test` command
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: maven-test
spec:
  workspaces:
  - name: source
  steps:
  - image: my-maven-image
    command: ["mvn test"]
    workingDir: $(workspaces.source.path)
----

.Example: Run a custom shell script by providing its path
[source,yaml,subs="attributes+"]
----
...
steps:
  image: ubuntu
  script: |
      #!/usr/bin/env bash
      /workspace/my-script.sh
...
----

.Example: Run a custom Python script by writing it in the YAML file
[source,yaml,subs="attributes+"]
----
...
steps:
  image: python
  script: |
      #!/usr/bin/env python3
      print(“hello from python!”)
...
----

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-comparison-of-jenkins-openshift-pipelines-execution-models_{context}"]
= Comparison of Jenkins and {pipelines-shortname} execution models

Jenkins and {pipelines-shortname} offer similar functions but are different in architecture and execution.

.Comparison of execution models in Jenkins and {pipelines-shortname}
[cols="1,1",options="header"]
|===
|Jenkins|{pipelines-shortname}
|Jenkins has a controller node. Jenkins runs pipelines and steps centrally, or orchestrates jobs running in other nodes.|{pipelines-shortname} is serverless and distributed, and there is no central dependency for execution.
|Containers are launched by the Jenkins controller node through the pipeline.|{pipelines-shortname} adopts a 'container-first' approach, where every step runs as a container in a pod (equivalent to nodes in Jenkins).
|Extensibility is achieved by using plugins.|Extensibility is achieved by using tasks in Tekton Hub or by creating custom tasks and scripts.
|===

// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

[id="jt-examples-of-common-use-cases_{context}"]
= Examples of common use cases

Both Jenkins and {pipelines-shortname} offer capabilities for common CI/CD use cases, such as:

* Compiling, building, and deploying images using Apache Maven
* Extending the core capabilities by using plugins
* Reusing shareable libraries and custom scripts

== Running a Maven pipeline in Jenkins and {pipelines-shortname}

You can use Maven in both Jenkins and {pipelines-shortname} workflows for compiling, building, and deploying images. To map your existing Jenkins workflow to {pipelines-shortname}, consider the following examples:

.Example: Compile and build an image and deploy it to OpenShift using Maven in Jenkins
[source,groovy]
----
#!/usr/bin/groovy
node('maven') {
    stage 'Checkout'
    checkout scm

    stage 'Build'
    sh 'cd helloworld && mvn clean'
    sh 'cd helloworld && mvn compile'

    stage 'Run Unit Tests'
    sh 'cd helloworld && mvn test'

    stage 'Package'
    sh 'cd helloworld && mvn package'

    stage 'Archive artifact'
    sh 'mkdir -p artifacts/deployments && cp helloworld/target/*.war artifacts/deployments'
    archive 'helloworld/target/*.war'

    stage 'Create Image'
    sh 'oc login https://kubernetes.default -u admin -p admin --insecure-skip-tls-verify=true'
    sh 'oc new-project helloworldproject'
    sh 'oc project helloworldproject'
    sh 'oc process -f helloworld/jboss-eap70-binary-build.json | oc create -f -'
    sh 'oc start-build eap-helloworld-app --from-dir=artifacts/'

    stage 'Deploy'
    sh 'oc new-app helloworld/jboss-eap70-deploy.json' }

----

.Example: Compile and build an image and deploy it to OpenShift using Maven in {pipelines-shortname}.
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: maven-pipeline
spec:
  workspaces:
    - name: shared-workspace
    - name: maven-settings
    - name: kubeconfig-dir
      optional: true
  params:
    - name: repo-url
    - name: revision
    - name: context-path
  tasks:
    - name: fetch-repo
      taskRef:
        name: git-clone
      workspaces:
        - name: output
          workspace: shared-workspace
      params:
        - name: url
          value: "$(params.repo-url)"
        - name: subdirectory
          value: ""
        - name: deleteExisting
          value: "true"
        - name: revision
          value: $(params.revision)
    - name: mvn-build
      taskRef:
        name: maven
      runAfter:
        - fetch-repo
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["-DskipTests", "clean", "compile"]
    - name: mvn-tests
      taskRef:
        name: maven
      runAfter:
        - mvn-build
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["test"]
    - name: mvn-package
      taskRef:
        name: maven
      runAfter:
        - mvn-tests
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["package"]
    - name: create-image-and-deploy
      taskRef:
        name: openshift-client
      runAfter:
        - mvn-package
      workspaces:
        - name: manifest-dir
          workspace: shared-workspace
        - name: kubeconfig-dir
          workspace: kubeconfig-dir
      params:
        - name: SCRIPT
          value: |
            cd "$(params.context-path)"
            mkdir -p ./artifacts/deployments && cp ./target/*.war ./artifacts/deployments
            oc new-project helloworldproject
            oc project helloworldproject
            oc process -f jboss-eap70-binary-build.json | oc create -f -
            oc start-build eap-helloworld-app --from-dir=artifacts/
            oc new-app jboss-eap70-deploy.json

----

== Extending the core capabilities of Jenkins and {pipelines-shortname} by using plugins
Jenkins has the advantage of a large ecosystem of numerous plugins developed over the years by its extensive user base. You can search and browse the plugins in the Jenkins Plugin Index.

{pipelines-shortname} also has many tasks developed and contributed by the community and enterprise users. A publicly available catalog of reusable {pipelines-shortname} tasks are available in the Tekton Hub.

In addition, {pipelines-shortname} incorporates many of the plugins of the Jenkins ecosystem within its core capabilities. For example, authorization is a critical function in both Jenkins and {pipelines-shortname}. While Jenkins ensures authorization using the Role-based Authorization Strategy plugin, {pipelines-shortname} uses OpenShift's built-in Role-based Access Control system.

== Sharing reusable code in Jenkins and {pipelines-shortname}
Jenkins shared libraries provide reusable code for parts of Jenkins pipelines. The libraries are shared between Jenkinsfiles to create highly modular pipelines without code repetition.

Although there is no direct equivalent of Jenkins shared libraries in {pipelines-shortname}, you can achieve similar workflows by using tasks from the Tekton Hub in combination with custom tasks and scripts.

[role="_additional-resources"]
== Additional resources
* Understanding {pipelines-shortname}
* Role-based Access Control
