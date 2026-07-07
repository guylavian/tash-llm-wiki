---
title: "Customizing the cert-manager Operator by using the CertManager custom resource"
type: reference
domain: openshift
slug: security-4-22-cert-manager-customizing-api-fields
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-customizing-api-fields
version: 4.22
family: security
documentKind: "Documentation"
---

# Customizing the cert-manager Operator by using the CertManager custom resource

[id="cert-manager-customizing-api-fields"]
= Customizing the cert-manager Operator by using the CertManager custom resource

[role="_abstract"]
After installing the {cert-manager-operator}, you can perform the following actions by configuring the `CertManager` custom resource (CR):

* Configure the arguments to modify the behavior of the cert-manager components, such as the cert-manager controller, CA injector, and Webhook.
* Set environment variables for the controller pod.
* Define resource requests and limits to manage CPU and memory usage.
* Configure scheduling rules to control where pods run in your cluster.

.Example CertManager CR YAML file
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
spec:
  controllerConfig:
    overrideArgs:
      - "--dns01-recursive-nameservers=8.8.8.8:53,1.1.1.1:53"
    overrideEnv:
      - name: HTTP_PROXY
        value: http://proxy.example.com:8080
    overrideResources:
      limits:
        cpu: "200m"
        memory: "512Mi"
      requests:
        cpu: "100m"
        memory: "256Mi"
    overrideScheduling:
      nodeSelector:
        custom: "label"
      tolerations:
        - key: "key1"
          operator: "Equal"
          value: "value1"
          effect: "NoSchedule"
    overrideReplicas: 2
#...

  webhookConfig:
    overrideArgs:
#...
    overrideResources:
#...
    overrideScheduling:
#...
    overrideReplicas:
#...

  cainjectorConfig:
    overrideArgs:
#...
    overrideResources:
#...
    overrideScheduling:
#...
    overrideReplicas:
#...
----

[WARNING]
====
To override unsupported arguments, you can add `spec.unsupportedConfigOverrides` section in the `CertManager` resource, but using `spec.unsupportedConfigOverrides` is unsupported.
====

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-explanation-of-certmanager-cr-fields_{context}"]
= Explanation of fields in the CertManager custom resource

[role="_abstract"]
To configure core components of the {cert-manager-operator}, use the CertManager custom resource (CR). You can define settings for the cert-manager controller, such as the spec.controllerConfig field, to customize your deployment.

The core components of the {cert-manager-operator} are as follows:

* Cert-manager controller: You can use the `spec.controllerConfig` field to configure the cert‑manager controller pod.
* Webhook: You can use the `spec.webhookConfig` field to configure the webhook pod, which handles validation and mutation requests.
* CA injector: You can use the `spec.cainjectorConfig` field to configure the CA injector pod.

[id="cert-manager-common-configuration-fields_{context}"]
== Common configurable fields in the CertManager CR for the cert-manager components

The following table lists the common fields that you can configure in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

.Common configurable fields in the CertManager CR for the cert-manager components
[cols=".^2,.^2,.^6a",options="header"]
|====

|Field|Type|Description

|`overrideArgs`
|`string`
|You can override the supported arguments for the cert-manager components.

|`overrideEnv`
|`dict`
|You can override the supported environment variables for the cert-manager controller. This field is only supported for the cert-manager controller component.

|`overrideReplicas`
|`int`
|You can configure the replicas for the cert-manager components. The default value is `1`. For production environments, the following replica counts are recommended:

* controller: 2

* cainjector: 2

* webhook: At least 3.

For more information, see High Availability.

|`overrideResources`
|`object`
|You can configure the CPU and memory limits for the cert-manager components.

|`overrideScheduling`
|`object`
|You can configure the pod scheduling constraints for the cert-manager components.

|====

[id="cert-manager-overridable-arguments_{context}"]
== Overridable arguments for the cert-manager components

You can configure the overridable arguments for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the overridable arguments for the cert-manager components:

.Overridable arguments the cert-manager components
[cols=".^5a,.^2,.^4a",options="header"]
|====

|Argument|Component|Description

|`--dns01-recursive-nameservers=<server_address>`
|Controller
|Provide a comma-separated list of nameservers to query for the DNS-01 self check. The nameservers can be specified either as `<host>:<port>`, for example, `1.1.1.1:53`, or use DNS over HTTPS (DoH), for example, `\https://1.1.1.1/dns-query`.

[NOTE]
====
DNS over HTTPS (DoH) is supported starting only from {cert-manager-operator} version 1.13.0 and later.
====

|`--dns01-recursive-nameservers-only`
|Controller
|Specify to only use recursive nameservers instead of checking the authoritative nameservers associated with that domain.

|`--acme-http01-solver-nameservers=<host>:<port>`
|Controller
|Provide a comma-separated list of `<host>:<port>` nameservers to query for the Automated Certificate Management Environment (ACME) HTTP01 self check. For example, `--acme-http01-solver-nameservers=1.1.1.1:53`.

|`--metrics-listen-address=<host>:<port>`
|Controller
|Specify the host and port for the metrics endpoint. The default value is `--metrics-listen-address=0.0.0.0:9402`.

|`--issuer-ambient-credentials`
|Controller
|You can use this argument to configure an ACME Issuer to solve DNS-01 challenges by using ambient credentials.

|`--enable-certificate-owner-ref`
|Controller
|This argument sets the certificate resource as an owner of the secret where the TLS certificate is stored. For more information, see "Deleting a TLS secret automatically upon Certificate removal".

|`--acme-http01-solver-resource-limits-cpu`
|Controller
|Defines the maximum CPU limit for ACME HTTP‑01 solver pods. The default value is `100m`.

|`--acme-http01-solver-resource-limits-memory`
|Controller
|Defines the maximum memory limit for ACME HTTP‑01 solver pods. The default value is `64Mi`.

|`--acme-http01-solver-resource-request-cpu`
|Controller
|Defines the minimum CPU request for ACME HTTP‑01 solver pods. The default value is `10m`.

|`--acme-http01-solver-resource-request-memory`
|Controller
|Defines the minimum memory request for ACME HTTP‑01 solver pods. The default value is `64Mi`.

|`--certificate-request-minimum-backoff-duration`
|Controller
|Specify the minimum backoff duration for certificate requests. The default value is `1h0m0s`.

|`--v=<verbosity_level>`
|Controller, Webhook, CA injector
|Specify the log level verbosity to determine the verbosity of log messages.

|====

[id="cert-manager-overridable-env-variables_{context}"]
== Overridable environment variables for the cert-manager controller

You can configure the overridable environment variables for the cert-manager controller in the `spec.controllerConfig.overrideEnv` field in the `CertManager` CR.

The following table describes the overridable environment variables for the cert-manager controller:

.Overridable environment variables for the cert-manager controller
[cols=".^2,.^2",options="header"]
|====

|Environment variable|Description

|`HTTP_PROXY`
|Proxy server for outgoing HTTP requests.

|`HTTPS_PROXY`
|Proxy server for outgoing HTTPS requests.

|`NO_PROXY`
|Comma‑separated list of hosts that bypass the proxy.

|====

[id="cert-manager-overridable-resource-parameters_{context}"]
== Overridable resource parameters for the cert-manager components

You can configure the CPU and memory limits for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the overridable resource parameters for the cert-manager components:

.Overridable resource parameters for the cert-manager components
[cols=".^2,.^2",options="header"]
|====

|Field|Description

|`overrideResources.limits.cpu`
|Defines the maximum amount of CPU that a component pod can use.

|`overrideResources.limits.memory`
|Defines the maximum amount of memory that a component pod can use.

|`overrideResources.requests.cpu`
|Defines the minimum amount of CPU requested by the scheduler for a component pod.

|`overrideResources.requests.memory`
|Defines the minimum amount of memory requested by the scheduler for a component pod.

|====

[id="cert-manager-overridable-scheduling-parameters_{context}"]
== Overridable scheduling parameters for the cert-manager components

You can configure the pod scheduling constrainsts for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig` field, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the pod scheduling parameters for the cert-manager components:

.Overridable scheduling parameters for the cert-manager components
[cols=".^2,.^2",options="header"]
|====

|Field|Description

|`overrideScheduling.nodeSelector`
|Key‑value pairs to constrain pods to specific nodes.

|`overrideScheduling.tolerations`
|List of tolerations to schedule pods on tainted nodes.

|====

[role="_additional-resources"]
.Additional resources

* Deleting a TLS secret automatically upon Certificate removal

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-override-environment-variables_{context}"]
= Customizing cert-manager by overriding environment variables from the cert-manager Operator API

[role="_abstract"]
To refine your deployment for specific operational requirements, override supported environment variables for the {cert-manager-operator}. You can customize these variables through the Operator API to apply configurations, such as proxy settings or system-level adjustments, that differ from the default values.

You can override the supported environment variables for the {cert-manager-operator} by adding a `spec.controllerConfig` section in the `CertManager` resource.

.Prerequisites

* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `CertManager` resource by running the following command:
+
[source,terminal]
----
$ oc edit certmanager cluster
----

. Add a `spec.controllerConfig` section with the following override arguments:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
  ...
spec:
  ...
  controllerConfig:
    overrideEnv:
      - name: HTTP_PROXY
        value: http://<proxy_url>
      - name: HTTPS_PROXY
        value: https://<proxy_url>
      - name: NO_PROXY
        value: <ignore_proxy_domains>
----
+
where:
+
`HTTP_PROXY`:: Specifies the proxy server URL.
`NO_PROXY`:: Specifies a comma separated list of domains. These domains are ignored by the proxy server.
+
[NOTE]
====
For more information about the overridable environment variables, see "Overridable environment variables for the cert-manager components" in "Explanation of fields in the CertManager custom resource".
====

. Save your changes and quit the text editor to apply your changes.

.Verification

. Verify that the cert-manager controller pod is redeployed by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt  1/1     Running   0          39s
----

. Verify that environment variables are updated for the cert-manager pod by running the following command:
+
[source,terminal]
----
$ oc get pod <redeployed_cert-manager_controller_pod> -n cert-manager -o yaml
----
+
.Example output
[source,yaml]
----
    env:
    ...
    - name: HTTP_PROXY
      value: http://<PROXY_URL>
    - name: HTTPS_PROXY
      value: https://<PROXY_URL>
    - name: NO_PROXY
      value: <IGNORE_PROXY_DOMAINS>
----

[role="_additional-resources"]
.Additional resources

* Explanation of fields in the CertManager custom resource

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-override-arguments_{context}"]
= Customizing cert-manager by overriding arguments from the cert-manager Operator API

[role="_abstract"]
You can override the supported arguments for the {cert-manager-operator} by adding a `spec.controllerConfig` section in the `CertManager` resource.

.Prerequisites

* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `CertManager` resource by running the following command:
+
[source,terminal]
----
$ oc edit certmanager cluster
----

. Add a `spec.controllerConfig` section with the following override arguments:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
  ...
spec:
  ...
  controllerConfig:
    overrideArgs:
      - '--dns01-recursive-nameservers=<server_address>'
      - '--dns01-recursive-nameservers-only'
      - '--acme-http01-solver-nameservers=<host>:<port>'
      - '--v=<verbosity_level>'
      - '--metrics-listen-address=<host>:<port>'
      - '--issuer-ambient-credentials'
      - '--acme-http01-solver-resource-limits-cpu=<quantity>'
      - '--acme-http01-solver-resource-limits-memory=<quantity>'
      - '--acme-http01-solver-resource-request-cpu=<quantity>'
      - '--acme-http01-solver-resource-request-memory=<quantity>'
      - '--certificate-request-minimum-backoff-duration=<duration>'
  webhookConfig:
    overrideArgs:
      - '--v=<verbosity_level>'
  cainjectorConfig:
    overrideArgs:
      - '--v=<verbosity_level>'
----
+
For information about the overridable aruguments, see "Overridable arguments for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

. Save your changes and quit the text editor to apply your changes.

.Verification

* Verify that arguments are updated for cert-manager pods by running the following command:
+
[source,terminal]
----
$ oc get pods -n cert-manager -o yaml
----
+
.Example output
[source,yaml]
----
...
  metadata:
    name: cert-manager-6d4b5d4c97-kldwl
    namespace: cert-manager
...
  spec:
    containers:
    - args:
      - --acme-http01-solver-nameservers=1.1.1.1:53
      - --cluster-resource-namespace=$(POD_NAMESPACE)
      - --dns01-recursive-nameservers=1.1.1.1:53
      - --dns01-recursive-nameservers-only
      - --leader-election-namespace=kube-system
      - --max-concurrent-challenges=60
      - --metrics-listen-address=0.0.0.0:9042
      - --v=6
...
  metadata:
    name: cert-manager-cainjector-866c4fd758-ltxxj
    namespace: cert-manager
...
  spec:
    containers:
    - args:
      - --leader-election-namespace=kube-system
      - --v=2
...
  metadata:
    name: cert-manager-webhook-6d48f88495-c88gd
    namespace: cert-manager
...
  spec:
    containers:
    - args:
      ...
      - --v=4
----

[role="_additional-resources"]
.Additional resources

* Explanation of fields in the CertManager custom resource

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-override-flag-controller_{context}"]
= Deleting a TLS secret automatically upon Certificate removal

[role="_abstract"]
You can enable the `--enable-certificate-owner-ref` flag for the {cert-manager-operator} by adding a `spec.controllerConfig` section in the `CertManager` resource. The `--enable-certificate-owner-ref` flag sets the certificate resource as an owner of the secret where the TLS certificate is stored.

[WARNING]
====
If you uninstall the {cert-manager-operator} or delete certificate resources from the cluster, the secret is deleted automatically. This might cause network connectivity issues depending upon where the certificate TLS secret is being used.
====

.Prerequisites

* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You have installed version 1.12.0 or later of the {cert-manager-operator}.

.Procedure

. Check that the `Certificate` object and its secret are available by running the following command:
+
[source,terminal]
----
$ oc get certificate
----
+
.Example output
[source,terminal]
----
NAME                                             READY   SECRET                                           AGE
certificate-from-clusterissuer-route53-ambient   True    certificate-from-clusterissuer-route53-ambient   8h
----

. Edit the `CertManager` resource by running the following command:
+
[source,terminal]
----
$ oc edit certmanager cluster
----

. Add a `spec.controllerConfig` section with the following override arguments:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
# ...
spec:
# ...
  controllerConfig:
    overrideArgs:
      - '--enable-certificate-owner-ref'
----

. Save your changes and quit the text editor to apply your changes.

.Verification

* Verify that the `--enable-certificate-owner-ref` flag is updated for cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager -o yaml
----
+
.Example output
[source,yaml]
----
# ...
  metadata:
    name: cert-manager-6e4b4d7d97-zmdnb
    namespace: cert-manager
# ...
  spec:
    containers:
    - args:
      - --enable-certificate-owner-ref
----

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-configure-cpu-memory_{context}"]
= Overriding CPU and memory limits for the cert-manager components

[role="_abstract"]
To ensure stable resource allocation and operation, configure CPU and memory limits for {cert-manager-operator} components. You can set specific constraints for the cert-manager controller, CA injector, and Webhook to align with your specific cluster requirements.

.Prerequisites

* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You have installed version 1.12.0 or later of the {cert-manager-operator}.

.Procedure

. Check that the deployments of the cert-manager controller, CA injector, and Webhook are available by entering the following command:
+
[source,terminal]
----
$ oc get deployment -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
cert-manager              1/1     1            1           53m
cert-manager-cainjector   1/1     1            1           53m
cert-manager-webhook      1/1     1            1           53m
----

. Before setting the CPU and memory limit, check the existing configuration for the cert-manager controller, CA injector, and Webhook by entering the following command:
+
[source,terminal]
----
$ oc get deployment -n cert-manager -o yaml
----
+
.Example output
[source,yaml]
----
# ...
  metadata:
    name: cert-manager
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-controller
          resources: {}
# ...
  metadata:
    name: cert-manager-cainjector
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-cainjector
          resources: {}
# ...
  metadata:
    name: cert-manager-webhook
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-webhook
          resources: {}
# ...
----
+
The `spec.resources` field is empty by default. The cert-manager components do not have CPU and memory limits.

. To configure the CPU and memory limits for the cert-manager controller, CA injector, and Webhook, enter the following command:
+
[source,terminal]
----
$ oc patch certmanager.operator cluster --type=merge -p="
spec:
  controllerConfig:
    overrideResources:
      limits:
        cpu: 200m
        memory: 64Mi
      requests:
        cpu: 10m
        memory: 16Mi
  webhookConfig:
    overrideResources:
      limits:
        cpu: 200m
        memory: 64Mi
      requests:
        cpu: 10m
        memory: 16Mi
  cainjectorConfig:
    overrideResources:
      limits:
        cpu: 200m
        memory: 64Mi
      requests:
        cpu: 10m
        memory: 16Mi
"
----
+
For information about the overridable resource parameters, see "Overridable resource parameters for the cert-manager components" in "Explanation of fields in the CertManager custom resource".
+
.Example output
[source,terminal]
----
certmanager.operator.openshift.io/cluster patched
----

.Verification

. Verify that the CPU and memory limits are updated for the cert-manager components:
+
[source,terminal]
----
$ oc get deployment -n cert-manager -o yaml
----
+
.Example output
[source,yaml]
----
# ...
  metadata:
    name: cert-manager
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-controller
          resources:
            limits:
              cpu: 200m
              memory: 64Mi
            requests:
              cpu: 10m
              memory: 16Mi
# ...
  metadata:
    name: cert-manager-cainjector
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-cainjector
          resources:
            limits:
              cpu: 200m
              memory: 64Mi
            requests:
              cpu: 10m
              memory: 16Mi
# ...
  metadata:
    name: cert-manager-webhook
    namespace: cert-manager
# ...
  spec:
    template:
      spec:
        containers:
        - name: cert-manager-webhook
          resources:
            limits:
              cpu: 200m
              memory: 64Mi
            requests:
              cpu: 10m
              memory: 16Mi
# ...
----

[role="_additional-resources"]
.Additional resources

* Explanation of fields in the CertManager custom resource

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-customizing-api-fields.adoc

[id="cert-manager-override-scheduling_{context}"]
= Configuring scheduling overrides for cert-manager components

[role="_abstract"]
You can configure the pod scheduling from the {cert-manager-operator} API for the {cert-manager-operator} components, such as the cert-manager controller, CA injector, and Webhook.

.Prerequisites

* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You have installed version 1.15.0 or later of the {cert-manager-operator}.

.Procedure

* Update the `certmanager.operator` custom resource to configure pod scheduling overrides for the desired components by running the following command. Use the `overrideScheduling` field under the `controllerConfig`, `webhookConfig`, or `cainjectorConfig` sections to define `nodeSelector` and `tolerations` settings.
+
[source,terminal]
----
$ oc patch certmanager.operator cluster --type=merge -p="
spec:
  controllerConfig:
    overrideScheduling:
      nodeSelector:
        node-role.kubernetes.io/control-plane: ''
      tolerations:
        - key: node-role.kubernetes.io/master
          operator: Exists
          effect: NoSchedule
  webhookConfig:
    overrideScheduling:
      nodeSelector:
        node-role.kubernetes.io/control-plane: ''
      tolerations:
        - key: node-role.kubernetes.io/master
          operator: Exists
          effect: NoSchedule
  cainjectorConfig:
    overrideScheduling:
      nodeSelector:
        node-role.kubernetes.io/control-plane: ''
      tolerations:
        - key: node-role.kubernetes.io/master
          operator: Exists
          effect: NoSchedule"
"
----
+
For information about the overridable scheduling parameters, see "Overridable scheduling parameters for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

.Verification

. Verify pod scheduling settings for `cert-manager` pods:

.. Check the deployments in the `cert-manager` namespace to confirm they have the correct `nodeSelector` and `tolerations` by running the following command:
+
[source,terminal]
----
$ oc get pods -n cert-manager -o wide
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE   IP            NODE                         NOMINATED NODE   READINESS GATES
cert-manager-58d9c69db4-78mzp              1/1     Running   0          10m   10.129.0.36   ip-10-0-1-106.ec2.internal   <none>           <none>
cert-manager-cainjector-85b6987c66-rhzf7   1/1     Running   0          11m   10.128.0.39   ip-10-0-1-136.ec2.internal   <none>           <none>
cert-manager-webhook-7f54b4b858-29bsp      1/1     Running   0          11m   10.129.0.35   ip-10-0-1-106.ec2.internal   <none>           <none>
----

.. Check the `nodeSelector` and `tolerations` settings applied to deployments by running the following command:
+
[source,terminal]
----
$ oc get deployments -n cert-manager -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{.spec.template.spec.nodeSelector}{"\n"}{.spec.template.spec.tolerations}{"\n\n"}{end}'
----
+
.Example output
[source,terminal]
----
cert-manager
{"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]

cert-manager-cainjector
{"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]

cert-manager-webhook
{"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]
----

. Verify pod scheduling events in the `cert-manager` namespace by running the following command:
+
[source,terminal]
----
$ oc get events -n cert-manager --field-selector reason=Scheduled
----

[role="_additional-resources"]
.Additional resources

* Explanation of fields in the CertManager custom resource
