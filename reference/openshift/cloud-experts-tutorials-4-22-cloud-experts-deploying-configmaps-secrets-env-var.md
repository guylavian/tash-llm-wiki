---
title: "Tutorial: ConfigMaps, secrets, and environment variables"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-configmaps-secrets-env-var
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-configmaps-secrets-env-var
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: ConfigMaps, secrets, and environment variables

[id="cloud-experts-deploying-configmaps-secrets-envvar"]
= Tutorial: ConfigMaps, secrets, and environment variables

//rosaworkshop.io content metadata
//Brought into ROSA product docs 05-07-2024

[role="_abstract"]
This tutorial shows how to configure the OSToy application by using config maps, secrets, and environment variables. For more information, see these linked topics.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-configmaps-secrets-env-var.adoc

[id="cloud-experts-deploying-configmaps-secrets-env-var-configmaps_{context}"]
= Configuration using ConfigMaps

[role="_abstract"]
Config maps allow you to decouple configuration artifacts from container image content to keep containerized applications portable.

.Procedure
* In the OSToy app, in the left menu, click *Config Maps*, displaying the contents of the config map available to the OSToy application. The code snippet shows an example of a config map configuration:
+
**Example output:**
+
[source,text]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: ostoy-configmap-files
data:
  config.json:  '{ "default": "123" }'
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-configmaps-secrets-env-var.adoc

[id="cloud-experts-deploying-configmaps-secrets-env-var-secrets_{context}"]
= Configuration using secrets

[role="_abstract"]
Kubernetes `Secret` objects allow you to store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. Putting this information in a secret is safer and more flexible than putting it in plain text into a pod definition or a container image.

.Procedure

* In the OSToy app, in the left menu, click *Secrets*, displaying the contents of the secrets available to the OSToy application. The code snippet shows an example of a secret configuration:
+
**Example output:**
+
[source,text]
----
USERNAME=my_user
PASSWORD=VVNFUk5BTUU9bXlfdXNlcgpQQVNTV09SRD1AT3RCbCVYQXAhIzYzMlk1RndDQE1UUWsKU01UUD1sb2NhbGhvc3QKU01UUF9QT1JUPTI1
SMTP=localhost
SMTP_PORT=25
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-configmaps-secrets-env-var.adoc

[id="cloud-experts-deploying-configmaps-secrets-env-var-env-variables_{context}"]
= Configuration using environment variables

[role="_abstract"]
Using environment variables is an easy way to change application behavior without requiring code changes. It allows different deployments of the same application to potentially behave differently based on the environment variables. OpenShift Container Platform makes it simple to set, view, and update environment variables for pods or deployments.

.Procedure

* In the OSToy app, in the left menu, click *ENV Variables*, displaying the environment variables available to the OSToy application. The code snippet shows an example of an environmental variable configuration:
+
**Example output:**
+
[source,text]
----
{
  "npm_config_local_prefix": "/opt/app-root/src",
  "STI_SCRIPTS_PATH": "/usr/libexec/s2i",
  "npm_package_version": "1.7.0",
  "APP_ROOT": "/opt/app-root",
  "NPM_CONFIG_PREFIX": "/opt/app-root/src/.npm-global",
  "OSTOY_MICROSERVICE_PORT_8080_TCP_PORT": "8080",
  "NODE": "/usr/bin/node",
  "LD_PRELOAD": "libnss_wrapper.so",
  "KUBERNETES_SERVICE_HOST": "172.30.0.1",
  "OSTOY_MICROSERVICE_PORT": "tcp://172.30.60.255:8080",
  "OSTOY_PORT": "tcp://172.30.152.25:8080",
  "npm_package_name": "ostoy",
  "OSTOY_SERVICE_PORT_8080_TCP": "8080",
  "_": "/usr/bin/node"
  "ENV_TOY_CONFIGMAP": "ostoy-configmap -env"
}
----
