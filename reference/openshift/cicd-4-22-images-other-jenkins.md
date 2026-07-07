---
title: "Configuring Jenkins images"
type: reference
domain: openshift
slug: cicd-4-22-images-other-jenkins
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/images-other-jenkins
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring Jenkins images

[id="images-other-jenkins"]
= Configuring Jenkins images

OpenShift Container Platform provides a container image for running Jenkins. This image provides a Jenkins server instance, which can be used to set up a basic flow for continuous testing, integration, and delivery.

The image is based on the Red Hat Universal Base Images (UBI).

OpenShift Container Platform follows the LTS release of Jenkins. OpenShift Container Platform provides an image that contains Jenkins 2.x.

The OpenShift Container Platform Jenkins images are available on Quay.io or registry.redhat.io.

For example:

[source,terminal]
----
$ podman pull registry.redhat.io/ocp-tools-4/jenkins-rhel8:<image_tag>
----

To use these images, you can either access them directly from these registries or push them into your OpenShift Container Platform container image registry. Additionally, you can create an image stream that points to the image, either in your container image registry or at the external location. Your OpenShift Container Platform resources can then reference the image stream.

But for convenience, OpenShift Container Platform provides image streams in the `openshift` namespace for the core Jenkins image as well as the example Agent images provided for OpenShift Container Platform integration with Jenkins.

[id="images-other-jenkins-config-customization_{context}"]
== Configuration and customization

You can manage Jenkins authentication in two ways:

* OpenShift Container Platform OAuth authentication provided by the OpenShift Container Platform Login plugin.
* Standard authentication provided by Jenkins.

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-oauth-auth_{context}"]
= OpenShift Container Platform OAuth authentication

OAuth authentication is activated by configuring options on the *Configure Global Security* panel in the Jenkins UI, or by setting the `OPENSHIFT_ENABLE_OAUTH` environment variable on the Jenkins *Deployment configuration* to anything other than `false`. This activates the OpenShift Container Platform Login plugin, which retrieves the configuration information from pod data or by interacting with the OpenShift Container Platform API server.

Valid credentials are controlled by the OpenShift Container Platform identity provider.

Jenkins supports both browser and non-browser access.

Valid users are automatically added to the Jenkins authorization matrix at log in, where OpenShift Container Platform roles dictate the specific Jenkins permissions that users have. The roles used by default are the predefined `admin`, `edit`, and `view`. The login plugin executes self-SAR requests against those roles in the project or namespace that Jenkins is running in.

Users with the `admin` role have the traditional Jenkins administrative user permissions. Users with the `edit` or `view` role have progressively fewer permissions.

The default OpenShift Container Platform `admin`, `edit`, and `view` roles and the Jenkins permissions those roles are assigned in the Jenkins instance are configurable.

When running Jenkins in
an OpenShift Container Platform
an OpenShift Container Platform
pod, the login plugin looks for a config map named `openshift-jenkins-login-plugin-config` in the namespace that Jenkins is running in.

If this plugin finds and can read in that config map, you can define the role to Jenkins Permission mappings. Specifically:

 * The login plugin treats the key and value pairs in the config map as Jenkins permission to OpenShift Container Platform role mappings.
 * The key is the Jenkins permission group short ID and the Jenkins permission short ID, with those two separated by a hyphen character.
 * If you want to add the `Overall Jenkins Administer` permission to
an OpenShift Container Platform
an OpenShift Container Platform
role, the key should be `Overall-Administer`.
 * To get a sense of which permission groups and permissions IDs are available, go to the matrix authorization page in the Jenkins console and IDs for the groups and individual permissions in the table they provide.
 * The value of the key and value pair is the list of OpenShift Container Platform roles the permission should apply to, with each role separated by a comma.
 * If you want to add the `Overall Jenkins Administer` permission to both the default `admin` and `edit` roles, as well as a new Jenkins role you have created, the value for the key `Overall-Administer` would be `admin,edit,jenkins`.

[NOTE]
====
The `admin` user that is pre-populated in the OpenShift Container Platform Jenkins image with administrative privileges is not given those privileges when OpenShift Container Platform OAuth is used. To grant these permissions the OpenShift Container Platform cluster administrator must explicitly define that user in the OpenShift Container Platform identity provider and assign the `admin` role to the user.
====

Jenkins users' permissions that are stored can be changed after the users are initially established. The OpenShift Container Platform Login plugin polls the OpenShift Container Platform API server for permissions and updates the permissions stored in Jenkins for each user with the permissions retrieved from OpenShift Container Platform. If the Jenkins UI is used to update permissions for a Jenkins user, the permission changes are overwritten the next time the plugin polls OpenShift Container Platform.

You can control how often the polling occurs with the `OPENSHIFT_PERMISSIONS_POLL_INTERVAL` environment variable. The default polling interval is five minutes.

The easiest way to create a new Jenkins service using OAuth authentication is to use a template.

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-auth_{context}"]
= Jenkins authentication

Jenkins authentication is used by default if the image is run directly, without using a template.

The first time Jenkins starts, the configuration is created along with the administrator user and password. The default user credentials are `admin` and `password`. Configure the default password by setting the `JENKINS_PASSWORD` environment variable when using, and only when using, standard Jenkins authentication.

.Procedure

* Create a Jenkins application that uses standard Jenkins authentication by entering the following command:
+
[source,terminal]
----
$ oc new-app -e \
    JENKINS_PASSWORD=<password> \
    ocp-tools-4/jenkins-rhel8
----

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-env-var_{context}"]
= Jenkins environment variables

The Jenkins server can be configured with the following environment variables:

[options="header"]
|===
| Variable | Definition | Example values and settings

|`OPENSHIFT_ENABLE_OAUTH`
|Determines whether the OpenShift Container Platform Login plugin manages authentication when logging in to Jenkins. To enable, set to `true`.
|Default: `false`

|`JENKINS_PASSWORD`
|The password for the `admin` user when using standard Jenkins authentication. Not applicable when `OPENSHIFT_ENABLE_OAUTH` is set to `true`.
|Default: `password`

|`JAVA_MAX_HEAP_PARAM`,
`CONTAINER_HEAP_PERCENT`,
`JENKINS_MAX_HEAP_UPPER_BOUND_MB`
|These values control the maximum heap size of the Jenkins JVM. If
`JAVA_MAX_HEAP_PARAM` is set, its value takes precedence. Otherwise, the maximum heap size is dynamically calculated as `CONTAINER_HEAP_PERCENT` of the container memory limit, optionally capped at `JENKINS_MAX_HEAP_UPPER_BOUND_MB` MiB.

By default, the maximum heap size of the Jenkins JVM is set to 50% of the container memory limit with no cap.
|`JAVA_MAX_HEAP_PARAM` example setting: `-Xmx512m`

`CONTAINER_HEAP_PERCENT` default: `0.5`, or 50%

`JENKINS_MAX_HEAP_UPPER_BOUND_MB` example setting: `512 MiB`

|`JAVA_INITIAL_HEAP_PARAM`,
`CONTAINER_INITIAL_PERCENT`
|These values control the initial heap size of the Jenkins JVM. If `JAVA_INITIAL_HEAP_PARAM` is set, its value takes precedence. Otherwise, the initial heap size is dynamically calculated as `CONTAINER_INITIAL_PERCENT` of the dynamically calculated maximum heap size.

By default, the JVM sets the initial heap size.
|`JAVA_INITIAL_HEAP_PARAM` example setting: `-Xms32m`

`CONTAINER_INITIAL_PERCENT` example setting: `0.1`, or 10%

|`CONTAINER_CORE_LIMIT`
|If set, specifies an integer number of cores used for sizing numbers of internal JVM threads.
|Example setting: `2`

|`JAVA_TOOL_OPTIONS`
|Specifies options to apply to all JVMs running in this container. It is not recommended to override this value.
|Default: `-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -Dsun.zip.disableMemoryMapping=true`

|`JAVA_GC_OPTS`
|Specifies Jenkins JVM garbage collection parameters. It is not recommended to override this value.
|Default: `-XX:+UseParallelGC -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=10 -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90`

|`JENKINS_JAVA_OVERRIDES`
|Specifies additional options for the Jenkins JVM. These options are appended to all other options, including the Java options above, and may be used to override any of them if necessary. Separate each additional option with a space; if any option contains space characters, escape them with a backslash.
|Example settings: `-Dfoo -Dbar`; `-Dfoo=first\ value -Dbar=second\ value`.

|`JENKINS_OPTS`
|Specifies arguments to Jenkins.
|

|`INSTALL_PLUGINS`
|Specifies additional Jenkins plugins to install when the container is first run or when `OVERRIDE_PV_PLUGINS_WITH_IMAGE_PLUGINS` is set to `true`. Plugins are specified as a comma-delimited list of name:version pairs.
|Example setting: `git:3.7.0,subversion:2.10.2`.

|`OPENSHIFT_PERMISSIONS_POLL_INTERVAL`
|Specifies the interval in milliseconds that the OpenShift Container Platform Login plugin polls OpenShift Container Platform for the permissions that are associated with each user that is defined in Jenkins.
|Default: `300000` - 5 minutes

|`OVERRIDE_PV_CONFIG_WITH_IMAGE_CONFIG`
|When running this image with
an OpenShift Container Platform
an OpenShift Container Platform
persistent volume (PV) for the Jenkins configuration directory, the transfer of configuration from the image to the PV is performed only the first time the image starts because the PV is assigned when the persistent volume claim (PVC) is created. If you create a custom image that extends this image and updates the configuration in the custom image after the initial startup, the configuration is not copied over unless you set this environment variable to `true`.
|Default: `false`

|`OVERRIDE_PV_PLUGINS_WITH_IMAGE_PLUGINS`
|When running this image with
an OpenShift Container Platform
an OpenShift Container Platform
PV for the Jenkins configuration directory, the transfer of plugins from the image to the PV is performed only the first time the image starts because the PV is assigned when the PVC is created. If you create a custom image that extends this image and updates plugins in the custom image after the initial startup, the plugins are not copied over unless you set this environment variable to `true`.
|Default: `false`

|`ENABLE_FATAL_ERROR_LOG_FILE`
|When running this image with
an OpenShift Container Platform
an OpenShift Container Platform
PVC for the Jenkins configuration directory, this environment variable allows the fatal error log file to persist when a fatal error occurs. The fatal error file is saved at `/var/lib/jenkins/logs`.
|Default: `false`

|`AGENT_BASE_IMAGE`
|Setting this value overrides the image used for the `jnlp` container in the sample Kubernetes plugin pod templates provided with this image. Otherwise, the image from the `jenkins-agent-base-rhel8:latest` image stream tag in the `openshift` namespace is used.
|Default:
`image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest`

|`JAVA_BUILDER_IMAGE`
|Setting this value overrides the image used for the `java-builder` container in the `java-builder` sample Kubernetes plugin pod templates provided with this image. Otherwise, the image from the `java:latest` image stream tag in the `openshift` namespace is used.
|Default:
`image-registry.openshift-image-registry.svc:5000/openshift/java:latest`

|`JAVA_FIPS_OPTIONS`
|Setting this value controls how the JVM operates when running on a FIPS node. For more information, see Configure Red Hat build of OpenJDK 11 in FIPS mode.
|Default: `-Dcom.redhat.fips=false`

|===

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-cross-project_{context}"]
= Providing Jenkins cross project access

If you are going to run Jenkins somewhere other than your same project, you must provide an access token to Jenkins to access your project.

.Procedure

. Identify the secret for the service account that has appropriate permissions to access the project that Jenkins must access by entering the following command:
+
[source,terminal]
----
$ oc describe serviceaccount jenkins
----
+
.Example output
[source,terminal]
----
Name:       default
Labels:     <none>
Secrets:    {  jenkins-token-uyswp    }
            {  jenkins-dockercfg-xcr3d    }
Tokens:     jenkins-token-izv1u
            jenkins-token-uyswp
----
+
In this case the secret is named `jenkins-token-uyswp`.

. Retrieve the token from the secret by entering the following command:
+
[source,terminal]
----
$ oc describe secret <secret name from above>
----
+
.Example output
[source,terminal]
----
Name:       jenkins-token-uyswp
Labels:     <none>
Annotations:    kubernetes.io/service-account.name=jenkins,kubernetes.io/service-account.uid=32f5b661-2a8f-11e5-9528-3c970e3bf0b7
Type:   kubernetes.io/service-account-token
Data
====
ca.crt: 1066 bytes
token:  eyJhbGc..<content cut>....wRA
----
+
The token parameter contains the token value Jenkins requires to access the project.

[id="images-other-jenkins-cross-volume-mount_{context}"]
== Jenkins cross volume mount points

The Jenkins image can be run with mounted volumes to enable persistent storage for the configuration:

* `/var/lib/jenkins` is the data directory where Jenkins stores configuration files, including job definitions.

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-customize-s2i_{context}"]
= Customizing the Jenkins image through source-to-image

To customize the official OpenShift Container Platform Jenkins image, you can use the image as a source-to-image (S2I) builder.

You can use S2I to copy your custom Jenkins jobs definitions, add additional plugins, or replace the provided `config.xml` file with your own, custom, configuration.

To include your modifications in the Jenkins image, you must have a Git repository with the following directory structure:

`plugins`::
This directory contains those binary Jenkins plugins you want to copy into Jenkins.

`plugins.txt`::
This file lists the plugins you want to install using the following syntax:

----
pluginId:pluginVersion
----

`configuration/jobs`::
This directory contains the Jenkins job definitions.

`configuration/config.xml`::
This file contains your custom Jenkins configuration.

The contents of the `configuration/` directory is copied to the `/var/lib/jenkins/` directory, so you can also include additional files, such as `credentials.xml`, there.

.Sample build configuration to customize the Jenkins image in OpenShift Container Platform
[source,yaml]
----
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: custom-jenkins-build
spec:
  source:                       <1>
    git:
      uri: https://github.com/custom/repository
    type: Git
  strategy:                     <2>
    sourceStrategy:
      from:
        kind: ImageStreamTag
        name: jenkins:2
        namespace: openshift
    type: Source
  output:                       <3>
    to:
      kind: ImageStreamTag
      name: custom-jenkins:latest
----

<1> The `source` parameter defines the source Git repository with the layout described above.
<2> The `strategy` parameter defines the original Jenkins image to use as a source image for the build.
<3> The `output` parameter defines the resulting, customized Jenkins image that you can use in deployment configurations instead of the official Jenkins image.

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-config-kubernetes_{context}"]
= Configuring the Jenkins Kubernetes plugin

The OpenShift Jenkins image includes the preinstalled Kubernetes plugin for Jenkins so that Jenkins agents can be dynamically provisioned on multiple container hosts using Kubernetes and OpenShift Container Platform.

To use the Kubernetes plugin, OpenShift Container Platform provides an OpenShift Agent Base image that is suitable for use as a Jenkins agent.

[IMPORTANT]
====
OpenShift Container Platform 4.11 moves the OpenShift Jenkins and OpenShift Agent Base images to the `ocp-tools-4` repository at `registry.redhat.io` so that Red Hat can produce and update the images outside the OpenShift Container Platform lifecycle. Previously, these images were in the OpenShift Container Platform install payload and the `openshift4` repository at `registry.redhat.io`.

The OpenShift Jenkins Maven and NodeJS Agent images were removed from the OpenShift Container Platform 4.11 payload. Red Hat no longer produces these images, and they are not available from the `ocp-tools-4` repository at `registry.redhat.io`. Red Hat maintains the 4.10 and earlier versions of these images for any significant bug fixes or security CVEs, following the OpenShift Container Platform lifecycle policy.

For more information, see the "Important changes to OpenShift Jenkins images" link in the following "Additional resources" section.
====

The Maven and Node.js agent images are automatically configured as Kubernetes pod template images within the OpenShift Container Platform Jenkins image configuration for the Kubernetes plugin. That configuration includes labels for each image that you can apply to any of your Jenkins jobs under their `Restrict where this project can be run` setting. If the label is applied, jobs run under
an OpenShift Container Platform
an OpenShift Container Platform
pod running the respective agent image.

[IMPORTANT]
====
In OpenShift Container Platform 4.10 and later, the recommended pattern for running Jenkins agents using the Kubernetes plugin is to use pod templates with both `jnlp` and `sidecar` containers. The `jnlp` container uses the OpenShift Container Platform Jenkins Base agent image to facilitate launching a separate pod for your build. The `sidecar` container image has the tools needed to build in a particular language within the separate pod that was launched. Many container images from the Red Hat Container Catalog are referenced in the sample image streams in the `openshift` namespace. The OpenShift Container Platform Jenkins image has a pod template named `java-build` with sidecar containers that demonstrate this approach. This pod template uses the latest Java version provided by the `java` image stream in the `openshift` namespace.
====

The Jenkins image also provides auto-discovery and auto-configuration of additional agent images for the Kubernetes plugin.

With the OpenShift Container Platform sync plugin, on Jenkins startup, the Jenkins image searches within the project it is running, or the projects listed in the plugin's configuration, for the following items:

* Image streams with the `role`  label set to `jenkins-agent`.
* Image stream tags with the `role` annotation set to `jenkins-agent`.
* Config maps with the `role` label set to `jenkins-agent`.

When the Jenkins image finds an image stream with the appropriate label, or an image stream tag with the appropriate annotation, it generates the corresponding Kubernetes plugin configuration. This way, you can assign your Jenkins jobs to run in a pod running the container image provided by the image stream.

The name and image references of the image stream, or image stream tag, are mapped to the name and image fields in the Kubernetes plugin pod template. You can control the label field of the Kubernetes plugin pod template by setting an annotation on the image stream, or image stream tag object, with the key `agent-label`. Otherwise, the name is used as the label.

[NOTE]
====
Do not log in to the Jenkins console and change the pod template configuration. If you do so after the pod template is created, and the OpenShift Container Platform Sync plugin detects that the image associated with the image stream or image stream tag has changed, it replaces the pod template and overwrites those configuration changes. You cannot merge a new configuration with the existing configuration.

Consider the config map approach if you have more complex configuration needs.
====

When it finds a config map with the appropriate label, the Jenkins image assumes that any values in the key-value data payload of the config map contain Extensible Markup Language (XML) consistent with the configuration format for Jenkins and the Kubernetes plugin pod templates. One key advantage of config maps over image streams and image stream tags is that you can control all the Kubernetes plugin pod template parameters.

.Sample config map for `jenkins-agent`
[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: jenkins-agent
  labels:
    role: jenkins-agent
data:
  template1: |-
    <org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
      <inheritFrom></inheritFrom>
      <name>template1</name>
      <instanceCap>2147483647</instanceCap>
      <idleMinutes>0</idleMinutes>
      <label>template1</label>
      <serviceAccount>jenkins</serviceAccount>
      <nodeSelector></nodeSelector>
      <volumes/>
      <containers>
        <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
          <name>jnlp</name>
          <image>openshift/jenkins-agent-maven-35-centos7:v3.10</image>
          <privileged>false</privileged>
          <alwaysPullImage>true</alwaysPullImage>
          <workingDir>/tmp</workingDir>
          <command></command>
          <args>${computer.jnlpmac} ${computer.name}</args>
          <ttyEnabled>false</ttyEnabled>
          <resourceRequestCpu></resourceRequestCpu>
          <resourceRequestMemory></resourceRequestMemory>
          <resourceLimitCpu></resourceLimitCpu>
          <resourceLimitMemory></resourceLimitMemory>
          <envVars/>
        </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
      </containers>
      <envVars/>
      <annotations/>
      <imagePullSecrets/>
      <nodeProperties/>
    </org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
----

The following example shows two containers that reference image streams in the `openshift` namespace. One container handles the JNLP contract for launching Pods as Jenkins Agents. The other container uses an image with tools for building code in a particular coding language:

[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: jenkins-agent
  labels:
    role: jenkins-agent
data:
  template2: |-
        <org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
          <inheritFrom></inheritFrom>
          <name>template2</name>
          <instanceCap>2147483647</instanceCap>
          <idleMinutes>0</idleMinutes>
          <label>template2</label>
          <serviceAccount>jenkins</serviceAccount>
          <nodeSelector></nodeSelector>
          <volumes/>
          <containers>
            <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
              <name>jnlp</name>
              <image>image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest</image>
              <privileged>false</privileged>
              <alwaysPullImage>true</alwaysPullImage>
              <workingDir>/home/jenkins/agent</workingDir>
              <command></command>
              <args>\$(JENKINS_SECRET) \$(JENKINS_NAME)</args>
              <ttyEnabled>false</ttyEnabled>
              <resourceRequestCpu></resourceRequestCpu>
              <resourceRequestMemory></resourceRequestMemory>
              <resourceLimitCpu></resourceLimitCpu>
              <resourceLimitMemory></resourceLimitMemory>
              <envVars/>
            </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
            <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
              <name>java</name>
              <image>image-registry.openshift-image-registry.svc:5000/openshift/java:latest</image>
              <privileged>false</privileged>
              <alwaysPullImage>true</alwaysPullImage>
              <workingDir>/home/jenkins/agent</workingDir>
              <command>cat</command>
              <args></args>
              <ttyEnabled>true</ttyEnabled>
              <resourceRequestCpu></resourceRequestCpu>
              <resourceRequestMemory></resourceRequestMemory>
              <resourceLimitCpu></resourceLimitCpu>
              <resourceLimitMemory></resourceLimitMemory>
              <envVars/>
            </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
          </containers>
          <envVars/>
          <annotations/>
          <imagePullSecrets/>
          <nodeProperties/>
        </org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
----

[NOTE]
====
Do not log in to the Jenkins console and change the pod template configuration. If you do so after the pod template is created, and the OpenShift Container Platform Sync plugin detects that the image associated with the image stream or image stream tag has changed, it replaces the pod template and overwrites those configuration changes. You cannot merge a new configuration with the existing configuration.

Consider the config map approach if you have more complex configuration needs.
====

After it is installed, the OpenShift Container Platform Sync plugin monitors the API server of OpenShift Container Platform for updates to image streams, image stream tags, and config maps and adjusts the configuration of the Kubernetes plugin.

The following rules apply:

* Removing the label or annotation from the config map, image stream, or image stream tag deletes any existing `PodTemplate` from the configuration of the Kubernetes plugin.
* If those objects are removed, the corresponding configuration is removed from the Kubernetes plugin.
* If you create appropriately labeled or annotated `ConfigMap`, `ImageStream`, or `ImageStreamTag` objects, or add labels after their initial creation, this results in the creation of a `PodTemplate` in the Kubernetes-plugin configuration.
* In the case of the `PodTemplate` by config map form, changes to the config map data for the `PodTemplate` are applied to the `PodTemplate` settings in the Kubernetes plugin configuration. The changes also override any changes that were made to the `PodTemplate` through the Jenkins UI between changes to the config map.

To use a container image as a Jenkins agent, the image must run the agent as an entry point. For more details, see the official https://wiki.jenkins-ci.org/display/JENKINS/Distributed+builds#Distributedbuilds-Launchslaveagentheadlessly[Jenkins documentation].

.Additional resources

* Important changes to OpenShift Jenkins images

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-permissions_{context}"]
= Jenkins permissions

If in the config map the `<serviceAccount>` element of the pod template XML is the OpenShift Container Platform service account used for the resulting pod, the service account credentials are mounted into the pod. The permissions are associated with the service account and control which operations against the OpenShift Container Platform master are allowed from the pod.

Consider the following scenario with service accounts used for the pod, which is launched by the Kubernetes Plugin that runs in the OpenShift Container Platform Jenkins image.

If you use the example template for Jenkins that is provided by OpenShift Container Platform, the `jenkins` service account is defined with the `edit` role for the project Jenkins runs in, and the master Jenkins pod has that service account mounted.

The two default Maven and NodeJS pod templates that are injected into the Jenkins configuration are also set to use the same service account as the Jenkins master.

* Any pod templates that are automatically discovered by the OpenShift Container Platform sync plugin because their image streams or image stream tags have the required label or annotations are configured to use the Jenkins master service account as their service account.
* For the other ways you can provide a pod template definition into Jenkins and the Kubernetes plugin, you have to explicitly specify the service account to use. Those other ways include the Jenkins console, the `podTemplate` pipeline DSL that is provided by the Kubernetes plugin, or labeling a config map whose data is the XML configuration for a pod template.
* If you do not specify a value for the service account, the `default` service account is used.
* Ensure that whatever service account is used has the necessary permissions, roles, and so on defined within OpenShift Container Platform to manipulate whatever projects you choose to manipulate from the within the pod.

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-create-service_{context}"]
= Creating a Jenkins service from a template

Templates provide parameter fields to define all the environment variables with predefined default values. OpenShift Container Platform provides templates to make creating a new Jenkins service easy. The Jenkins templates should be registered in the default `openshift` project by your cluster administrator during the initial cluster setup.

The two available templates both define deployment configuration and a service. The templates differ in their storage strategy, which affects whether the Jenkins content persists across a pod restart.

[NOTE]
====
A pod might be restarted when it is moved to another node or when an update of the deployment configuration triggers a redeployment.
====

* `jenkins-ephemeral` uses ephemeral storage. On pod restart, all data is lost. This template is only useful for development or testing.

* `jenkins-persistent` uses a Persistent Volume (PV) store. Data survives a pod restart.

To use a PV store, the cluster administrator must define a PV pool in the OpenShift Container Platform deployment.

After you select which template you want, you must instantiate the template to be able to use Jenkins.

.Procedure

* Create a new Jenkins application using one of the following methods:
** A PV:
+
[source,terminal]
----
$ oc new-app jenkins-persistent
----

** Or an `emptyDir` type volume where configuration does not persist across pod restarts:
+
[source,terminal]
----
$ oc new-app jenkins-ephemeral
----

With both templates, you can run `oc describe` on them to see all the parameters available for overriding.

For example:

[source,terminal]
----
$ oc describe jenkins-ephemeral
----

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-kubernetes-plugin_{context}"]
= Using the Jenkins Kubernetes plugin

In the following example, the `openshift-jee-sample` `BuildConfig` object causes a Jenkins Maven agent pod to be dynamically provisioned. The pod clones some Java source code, builds a WAR file, and causes a second `BuildConfig`, `openshift-jee-sample-docker` to run. The second `BuildConfig` layers the new WAR file into a container image.

[IMPORTANT]
====
OpenShift Container Platform 4.11 removed the OpenShift Jenkins Maven and NodeJS Agent images from its payload. Red Hat no longer produces these images, and they are not available from the `ocp-tools-4` repository at `registry.redhat.io`. Red Hat maintains the 4.10 and earlier versions of these images for any significant bug fixes or security CVEs, following the OpenShift Container Platform lifecycle policy.

For more information, see the "Important changes to OpenShift Jenkins images" link in the following "Additional resources" section.
====

.Sample `BuildConfig` that uses the Jenkins Kubernetes plugin
[source,yaml]
----
kind: List
apiVersion: v1
items:
- kind: ImageStream
  apiVersion: image.openshift.io/v1
  metadata:
    name: openshift-jee-sample
- kind: BuildConfig
  apiVersion: build.openshift.io/v1
  metadata:
    name: openshift-jee-sample-docker
  spec:
    strategy:
      type: Docker
    source:
      type: Docker
      dockerfile: |-
        FROM openshift/wildfly-101-centos7:latest
        COPY ROOT.war /wildfly/standalone/deployments/ROOT.war
        CMD $STI_SCRIPTS_PATH/run
      binary:
        asFile: ROOT.war
    output:
      to:
        kind: ImageStreamTag
        name: openshift-jee-sample:latest
- kind: BuildConfig
  apiVersion: build.openshift.io/v1
  metadata:
    name: openshift-jee-sample
  spec:
    strategy:
      type: JenkinsPipeline
      jenkinsPipelineStrategy:
        jenkinsfile: |-
          node("maven") {
            sh "git clone https://github.com/openshift/openshift-jee-sample.git ."
            sh "mvn -B -Popenshift package"
            sh "oc start-build -F openshift-jee-sample-docker --from-file=target/ROOT.war"
          }
    triggers:
    - type: ConfigChange
----

It is also possible to override the specification of the dynamically created Jenkins agent pod. The following is a modification to the preceding example, which overrides the container memory and specifies an environment variable.

.Sample `BuildConfig` that uses the Jenkins Kubernetes plugin, specifying memory limit and environment variable
[source,yaml]
----
kind: BuildConfig
apiVersion: build.openshift.io/v1
metadata:
  name: openshift-jee-sample
spec:
  strategy:
    type: JenkinsPipeline
    jenkinsPipelineStrategy:
      jenkinsfile: |-
        podTemplate(label: "mypod", <1>
                    cloud: "openshift", <2>
                    inheritFrom: "maven", <3>
                    containers: [
            containerTemplate(name: "jnlp", <4>
                              image: "openshift/jenkins-agent-maven-35-centos7:v3.10", <5>
                              resourceRequestMemory: "512Mi", <6>
                              resourceLimitMemory: "512Mi", <7>
                              envVars: [
              envVar(key: "CONTAINER_HEAP_PERCENT", value: "0.25") <8>
            ])
          ]) {
          node("mypod") { <9>
            sh "git clone https://github.com/openshift/openshift-jee-sample.git ."
            sh "mvn -B -Popenshift package"
            sh "oc start-build -F openshift-jee-sample-docker --from-file=target/ROOT.war"
          }
        }
  triggers:
  - type: ConfigChange
----
<1> A new pod template called `mypod` is defined dynamically. The new pod template name is referenced in the node stanza.
<2> The `cloud` value must be set to `openshift`.
<3> The new pod template can inherit its configuration from an existing pod template. In this case, inherited from the Maven pod template that is pre-defined by OpenShift Container Platform.
<4> This example overrides values in the pre-existing container, and must be specified by name. All Jenkins agent images shipped with OpenShift Container Platform use the Container name `jnlp`.
<5> Specify the container image name again. This is a known issue.
<6> A memory request of `512 Mi` is specified.
<7> A memory limit of `512 Mi` is specified.
<8> An environment variable `CONTAINER_HEAP_PERCENT`, with value `0.25`, is specified.
<9> The node stanza references the name of the defined pod template.

// Writer, remove or update jenkins-agent-maven reference in 4.12

By default, the pod is deleted when the build completes. This behavior can be modified with the plugin or within a pipeline Jenkinsfile.

Upstream Jenkins has more recently introduced a YAML declarative format for defining a `podTemplate` pipeline DSL in-line with your pipelines. An example of this format, using the sample `java-builder` pod template that is defined in the OpenShift Container Platform Jenkins image:

[source,yaml]
----
def nodeLabel = 'java-buidler'

pipeline {
  agent {
    kubernetes {
      cloud 'openshift'
      label nodeLabel
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    worker: ${nodeLabel}
spec:
  containers:
  - name: jnlp
    image: image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: java
    image: image-registry.openshift-image-registry.svc:5000/openshift/java:latest
    command:
    - cat
    tty: true
"""
    }
  }

  options {
    timeout(time: 20, unit: 'MINUTES')
  }

  stages {
    stage('Build App') {
      steps {
        container("java") {
          sh "mvn --version"
        }
     }
    }
  }
}
----

.Additional resources

* Important changes to OpenShift Jenkins images

// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

[id="images-other-jenkins-memory_{context}"]
= Jenkins memory requirements

When deployed by the provided Jenkins Ephemeral or Jenkins Persistent templates, the default memory limit is `1 Gi`.

By default, all other process that run in the Jenkins container cannot use more than a total of `512 MiB` of memory. If they require more memory, the container halts. It is therefore highly recommended that pipelines run external commands in an agent container wherever possible.

And if `Project` quotas allow for it, see recommendations from the Jenkins documentation on what a Jenkins master should have from a memory perspective. Those recommendations proscribe to allocate even more memory for the Jenkins master.

It is recommended to specify memory request and limit values on agent containers created by the Jenkins Kubernetes plugin. Admin users can set default values on a per-agent image basis through the Jenkins configuration. The memory request and limit parameters can also be overridden on a per-container basis.

You can increase the amount of memory available to Jenkins by overriding the `MEMORY_LIMIT` parameter when instantiating the Jenkins Ephemeral or Jenkins Persistent template.

[role="_additional-resources"]
== Additional resources

// This xref points to a topic that is not currently included in the OSD and ROSA docs.
* See Base image options for more information about the Red Hat Universal Base Images (UBI).
* Important changes to OpenShift Jenkins images
