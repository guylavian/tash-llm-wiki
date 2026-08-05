---
title: "Build configuration resources"
type: reference
domain: openshift
slug: cicd-4-22-build-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/build-configuration
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Build configuration resources

[id="build-configuration"]
= Build configuration resources

Use the following procedure to configure build settings.

// Module included in the following assemblies:
//
// * builds/build-configuration.adoc

[id="builds-configuration-parameters_{context}"]
= Build controller configuration parameters

The `build.config.openshift.io/cluster` resource offers the following configuration parameters.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`Build`
|Holds cluster-wide information on how to handle builds. The canonical, and only valid name is `cluster`.

`spec`: Holds user-settable values for the build controller configuration.

|`buildDefaults`
|Controls the default information for builds.

`defaultProxy`: Contains the default proxy settings for all build operations, including image pull or push and source download.

You can override values by setting the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables in the `BuildConfig` strategy.

`gitProxy`: Contains the proxy settings for Git operations only. If set, this overrides any proxy settings for all Git commands, such as `git clone`.

Values that are not set here are inherited from DefaultProxy.

`env`: A set of default environment variables that are applied to the build if the specified variables do not exist on the build.

`imageLabels`: A list of labels that are applied to the resulting image. You can override a default label by providing a label with the same name in the `BuildConfig`.

`resources`: Defines resource requirements to execute the build.

|`ImageLabel`
|`name`: Defines the name of the label. It must have non-zero length.

|`buildOverrides`
|Controls override settings for builds.

`imageLabels`: A list of labels that are applied to the resulting image. If you provided a label in the `BuildConfig` with the same name as one in this table, your label will be overwritten.

`nodeSelector`: A selector which must be true for the build pod to fit on a node.

`tolerations`: A list of tolerations that overrides any existing tolerations set on a build pod.

|`BuildList`
|`items`: Standard object's metadata.

|===

// Module included in the following assemblies:
//
// * builds/build-configuration.adoc

[id="builds-configuration-file_{context}"]
= Configuring build settings

You can configure build settings by editing the `build.config.openshift.io/cluster` resource.

.Procedure

* Edit the `build.config.openshift.io/cluster` resource by entering the following command:
+
[source,terminal]
----
$ oc edit build.config.openshift.io/cluster
----
+
The following is an example `build.config.openshift.io/cluster` resource:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Build # <1>
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 2
  name: cluster
  resourceVersion: "107233"
  selfLink: /apis/config.openshift.io/v1/builds/cluster
  uid: e2e9cc14-78a9-11e9-b92b-06d6c7da38dc
spec:
  buildDefaults: # <2>
    defaultProxy: # <3>
      httpProxy: http://proxy.com
      httpsProxy: https://proxy.com
      noProxy: internal.com
    env: # <4>
    - name: envkey
      value: envvalue
    gitProxy: # <5>
      httpProxy: http://gitproxy.com
      httpsProxy: https://gitproxy.com
      noProxy: internalgit.com
    imageLabels: # <6>
    - name: labelkey
      value: labelvalue
    resources: # <7>
      limits:
        cpu: 100m
        memory: 50Mi
      requests:
        cpu: 10m
        memory: 10Mi
  buildOverrides: # <8>
    imageLabels: # <9>
    - name: labelkey
      value: labelvalue
    nodeSelector: # <10>
      selectorkey: selectorvalue
    tolerations: # <11>
    - effect: NoSchedule
      key: node-role.kubernetes.io/builds
operator: Exists
----
<1> `Build`: Holds cluster-wide information on how to handle builds. The canonical, and only valid name is `cluster`.
<2> `buildDefaults`: Controls the default information for builds.
<3> `defaultProxy`: Contains the default proxy settings for all build operations, including image pull or push and source download.
<4> `env`: A set of default environment variables that are applied to the build if the specified variables do not exist on the build.
<5> `gitProxy`: Contains the proxy settings for Git operations only. If set, this overrides any Proxy settings for all Git commands, such as `git clone`.
<6> `imageLabels`: A list of labels that are applied to the resulting image.
You can override a default label by providing a label with the same name in the `BuildConfig`.
<7> `resources`: Defines resource requirements to execute the build.
<8> `buildOverrides`: Controls override settings for builds.
<9> `imageLabels`: A list of labels that are applied to the resulting image.
If you provided a label in the `BuildConfig` with the same name as one in this table, your label will be overwritten.
<10> `nodeSelector`: A selector which must be true for the build pod to fit on a node.
<11> `tolerations`: A list of tolerations that overrides any existing tolerations set on a build pod.
