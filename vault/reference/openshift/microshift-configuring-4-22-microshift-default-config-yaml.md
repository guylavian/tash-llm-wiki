---
title: "About the default {microshift-short} configuration file"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-default-config-yaml
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-default-config-yaml
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# About the default {microshift-short} configuration file

[id="microshift-default-config-yaml"]
= About the default {microshift-short} configuration file

[role="_abstract"]
To view or customize the built-in settings for {microshift-short}, you can reference the default configuration YAML file or run `microshift show-config`. The file lists the settings that apply when no `config.yaml` file is present.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-default-config-yaml.adoc

[id="microshift-config-rhde-con_{context}"]
= Configuring {op-system-bundle}

[role="_abstract"]
The {microshift-short} configuration file, `config.yaml`, centralizes {op-system-bundle} and service settings for your single-node edge platform. To create a custom configuration, you can copy the installed `config.yaml.default` file and rename it to `config.yaml`.

{microshift-short} and {op-system-base-full} work together to bring a lighter-weight, single-node Kubernetes to the edge. This combination means that there is a single node that is both control-plane and worker. It also means that the operating system handles many functions. You add features by installing optional RPMs or Operators. In many cases, you must configure the operating system or other resources in addition to the {microshift-short} service.

Bringing these components together is the {microshift-short} configuration file, `config.yaml`. The configuration file customizes your application platform and enables advanced functionality.

[id="using-the-default-configuration-file_{context}"]
== Using the default configuration file

A `config.yaml.default` file is installed automatically. You can copy this file, rename it config.yaml, and use it as the starting point for your custom configuration.

[id="configuring-platform-features_{context}"]
== Configuring platform features

You can use the {microshift-short} configuration file to control and customize platform features. For example:

Ingress:: Ingress is available by default, but you can add advanced functions such as TLS and route admission specifications by using parameters in the {microshift-short} configuration file.
Storage:: If you do not need storage, you can disable the built-in storage provider by using the {microshift-short} configuration file. If you do want to use the built-in storage provider, you must make your adjustments in the `lvmd.config` file. The role of the {microshift-short} configuration file in this case is to set whether you use the default storage provider.
Advanced networking functions:: Advanced networking functions, such as using multiple networks. The Multus package is an installable RPM, but you set up access by using the {microshift-short} configuration file to set parameters. In addition, you must configure network settings on your networks through the host.

[NOTE]
====
You can also add features that operate without configurations to the {microshift-short} `config.yaml` file. For example, you can install and configure GitOps for application management without configuring {microshift-short}.
====

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-default-config-yaml.adoc

[id="microshift-config-yaml_{context}"]
= The {microshift-short} configuration file

[role="_abstract"]
At startup, {microshift-short} checks the system-wide `/etc/microshift/` directory for a configuration file named `config.yaml`. If the configuration file does not exist in the directory, built-in default values are used to start the service.

You must use the {microshift-short} configuration file in combination with host and, sometimes, application and service settings. Ensure that you configure each function in tandem when you adjust settings for your {microshift-short} node.

For your convenience, a `config.yaml.default` file ready for your inputs is automatically installed.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-default-config-yaml.adoc
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-yaml-default_{context}"]
= Default settings

[role="_abstract"]
When no `config.yaml` or configuration snippet exists, {microshift-short} uses built-in default values. To view these defaults, run `microshift show-config`.

The following example shows the default configuration settings.

.Procedure

*  To see the default values, run the following command:
+
[source,terminal]
----
$ microshift show-config
----
+
.Default values example output in YAML form
[source,yaml]
----
apiServer:
  advertiseAddress: 10.44.0.0/32
  auditLog:
    maxFileAge: 0
    maxFileSize: 200
    maxFiles: 10
    profile: Default
  namedCertificates:
    - certPath: ""
      keyPath: ""
      names:
        - ""
  subjectAltNames: []
  tls:
    cipherSuites:
    minVersion: VersionTLS12
debugging:
  logLevel: "Normal"
dns:
  baseDomain: microshift.example.com
etcd:
  memoryLimitMB: 0
genericDevicePlugin:
    devices:
        - groups:
            - count: 1
              paths:
                - limit: 1
                  mountPath: /dev/ttyACM0
                  path: /dev/ttyACM0
                  permissions: mrw
                  readOnly: false
                  type: Device
              usbs:
                - product: ""
                  serial: ""
                  vendor: ""
          name: serial
    domain: device.microshift.io
    status: Disabled
ingress:
  accessLogging:
    destination:
      type:
      container:
        maxLength: 1024
      syslog:
        address: ""
        facility: ""
        maxLength: 1024
        port: 0
        type: ""
    httpCaptureCookies:
      - matchType: ""
        maxLength: 0
        name: ""
        namePrefix: ""
    httpCaptureHeaders:
      request:
        - maxLength: 0
          name: ""
      response:
        - maxLength: 0
          name: ""
    httpLogFormat: ""
    status: Disabled
  certificateSecret: router-certs-default
  clientTLS:
    allowedSubjectPatterns:
    clientCA:
      name: ""
    clientCertificatePolicy: ""
  defaultHTTPVersion: 1
  forwardedHeaderPolicy: ""
  httpCompression:
    mimeTypes:
      - ""
  httpEmptyRequestsPolicy: Respond
  httpErrorCodePages:
      name: ""
  listenAddress: []
  logEmptyRequests: Log
  ports:
    http: 80
    https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
    wildcardPolicy: WildcardPolicyAllowed
  status: Managed
  tlsSecurityProfile:
    type: Intermediate
  tuningOptions:
      clientFinTimeout: "1s"
      clientTimeout: "30s"
      headerBufferBytes: 0
      headerBufferMaxRewriteBytes: 0
      healthCheckInterval: "5s"
      maxConnections: 0
      serverFinTimeout: "1s"
      serverTimeout: "30s"
      threadCount: 0
      tlsInspectDelay: "5s"
      tunnelTimeout: "1h"
kubelet:
manifests:
  kustomizePaths:
    - /usr/lib/microshift/manifests
    - /usr/lib/microshift/manifests.d/*
    - /etc/microshift/manifests
    - /etc/microshift/manifests.d/*
network:
  clusterNetwork:
    - 10.42.0.0/16
  cniPlugin: ""
  multus:
    status: Disabled
  serviceNetwork:
    - 10.43.0.0/16
  serviceNodePortRange: 30000-32767
node:
  hostnameOverride: ""
  nodeIP: ""
  nodeIPv6: ""
storage:
  driver: ""
  optionalCsiComponents:
    - ""
telemetry:
  endpoint: https://infogw.api.openshift.com
  proxy: ""
  status: Enabled
----
+
where:
+
--
`apiserver.advertiseAddress`:: Specifies the address of the service network.
`network.multus.status`:: Specifies the status of the Multus Container Network Interface (CNI).
`node.nodeIP`:: Specifies the IP address of the default route.
`storage.driver`:: Specifies the storage driver to use. Default null value deploys Logical Volume Managed Storage (LVMS).
`storage.optionalCsiComponents`:: Specifies the CSI components to deploy. Default null value deploys `snapshot-controller`.
--
