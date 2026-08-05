---
title: "ConfigMaps, secrets, and environment variables"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-configmaps-secrets-env-var
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-configmaps-secrets-env-var
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# ConfigMaps, secrets, and environment variables

[id="learning-deploying-configmaps-secrets-envvar"]
= ConfigMaps, secrets, and environment variables

[role="_abstract"]
To securely manage sensitive information and decouple configurations from your container image, configure your OSToy application by using config maps, secrets, and environment variables.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-configmaps-secrets-env-var.adoc
[id="learning-deploying-configmaps-secrets-envvar-configmaps_{context}"]
= Configuration using ConfigMaps

[role="_abstract"]
To keep your containerized applications portable, decouple your configuration artifacts from the container image content by using config maps. Managing these configurations separately ensures that your images remain completely environment-agnostic.

.Procedure
* In the OSToy application, in the left menu, click *Config Maps*, displaying the contents of the config map available to the OSToy application. The code snippet shows an example of a config map configuration:
+
*For example*:
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
// * rosa_learning/deploying_application_workshop/learning-deploying-configmaps-secrets-env-var.adoc
[id="learning-deploying-configmaps-secrets-envvar-secrets_{context}"]
= Configuration using secrets

[role="_abstract"]
To securely store and manage sensitive information like passwords and SSH keys, use Kubernetes `Secret` objects. Configuring a secret is safer and more flexible than embedding plain text directly into your pod definitions or container images.

.Procedure

* In the OSToy application, in the left menu, click *Secrets*, displaying the contents of the secrets available to the OSToy application. The code snippet shows an example of a secret configuration:
+
*For example*:
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
// * rosa_learning/deploying_application_workshop/learning-deploying-configmaps-secrets-env-var.adoc
[id="learning-deploying-configmaps-secrets-envvar-environment-variables_{context}"]
= Configuration using environment variables

[role="_abstract"]
You can change application behavior without requiring code changes by configuring environment variables. Setting, viewing, and updating these variables in OpenShift Container Platform allows you to easily customize how different deployments behave.

.Procedure

* In the OSToy application, in the left menu, click *ENV Variables*, displaying the environment variables available to the OSToy application. The code snippet shows an example of an environmental variable configuration:
+
*For example*:
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

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Understanding config maps
 * Secrets
