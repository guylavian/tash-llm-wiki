---
title: "Accessing secrets and config maps from functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-accessing-secrets-configmaps
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-accessing-secrets-configmaps
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Accessing secrets and config maps from functions

[id="serverless-functions-accessing-secrets-configmaps"]
= Accessing secrets and config maps from functions

After your functions have been deployed to the cluster, they can access data stored in secrets and config maps. This data can be mounted as volumes, or assigned to environment variables. You can configure this access interactively by using the Knative CLI, or by manually by editing the function configuration YAML file.

[IMPORTANT]
====
To access secrets and config maps, the function must be deployed on the cluster. This functionality is not available to a function running locally.

If a secret or config map value cannot be accessed, the deployment fails with an error message specifying the inaccessible values.
====

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-secrets-configmaps-interactively_{context}"]
= Modifying function access to secrets and config maps interactively

You can manage the secrets and config maps accessed by your function by using the `kn func config` interactive utility. The available operations include listing, adding, and removing values stored in config maps and secrets as environment variables, as well as listing, adding, and removing volumes. This functionality enables you to manage what data stored on the cluster is accessible by your function.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Run the following command in the function project directory:
+
[source,terminal]
----
$ kn func config
----
+
Alternatively, you can specify the function project directory using the `--path` or `-p` option.

. Use the interactive interface to perform the necessary operation. For example, using the utility to list configured volumes produces an output similar to this:
+
[source,terminal]
----
$ kn func config
? What do you want to configure? Volumes
? What operation do you want to perform? List
Configured Volumes mounts:
- Secret "mysecret" mounted at path: "/workspace/secret"
- Secret "mysecret2" mounted at path: "/workspace/secret2"
----
+
This scheme shows all operations available in the interactive utility and how to navigate to them:
+
[source]
----
kn func config
   ├─> Environment variables
   │               ├─> Add
   │               │    ├─> ConfigMap: Add all key-value pairs from a config map
   │               │    ├─> ConfigMap: Add value from a key in a config map
   │               │    ├─> Secret: Add all key-value pairs from a secret
   │               │    └─> Secret: Add value from a key in a secret
   │               ├─> List: List all configured environment variables
   │               └─> Remove: Remove a configured environment variable
   └─> Volumes
           ├─> Add
           │    ├─> ConfigMap: Mount a config map as a volume
           │    └─> Secret: Mount a secret as a volume
           ├─> List: List all configured volumes
           └─> Remove: Remove a configured volume
----

. Optional. Deploy the function to make the changes take effect:
+
[source,terminal]
----
$ kn func deploy -p test
----
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-secrets-configmaps-interactively-specialized_{context}"]
= Modifying function access to secrets and config maps interactively by using specialized commands

Every time you run the `kn func config` utility, you need to navigate the entire dialogue to select the operation you need, as shown in the previous section. To save steps, you can directly execute a specific operation by running a more specific form of the `kn func config` command:

* To list configured environment variables:
+
[source,terminal]
----
$ kn func config envs [-p <function-project-path>]
----

* To add environment variables to the function configuration:
+
[source,terminal]
----
$ kn func config envs add [-p <function-project-path>]
----

* To remove environment variables from the function configuration:
+
[source,terminal]
----
$ kn func config envs remove [-p <function-project-path>]
----

* To list configured volumes:
+
[source,terminal]
----
$ kn func config volumes [-p <function-project-path>]
----

* To add a volume to the function configuration:
+
[source,terminal]
----
$ kn func config volumes add [-p <function-project-path>]
----

* To remove a volume from the function configuration:
+
[source,terminal]
----
$ kn func config volumes remove [-p <function-project-path>]
----

[id="serverless-functions-secrets-configmaps-manually_{context}"]
== Adding function access to secrets and config maps manually

You can manually add configuration for accessing secrets and config maps to your function. This might be preferable to using the `kn func config` interactive utility and commands, for example when you have an existing configuration snippet.

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-mounting-secret-as-volume_{context}"]
= Mounting a secret as a volume

You can mount a secret as a volume. Once a secret is mounted, you can access it from the function as a regular file. This enables you to store on the cluster data needed by the function, for example, a list of URIs that need to be accessed by the function.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For each secret you want to mount as a volume, add the following YAML to the `volumes` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
volumes:
- secret: mysecret
  path: /workspace/secret
----
+
* Substitute `mysecret` with the name of the target secret.
* Substitute `/workspace/secret` with the path where you want to mount the secret.
+
For example, to mount the `addresses` secret, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
volumes:
- configMap: addresses
  path: /workspace/secret-addresses
----

. Save the configuration.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-mounting-configmap-as-volume_{context}"]
= Mounting a config map as a volume

You can mount a config map as a volume. Once a config map is mounted, you can access it from the function as a regular file. This enables you to store on the cluster data needed by the function, for example, a list of URIs that need to be accessed by the function.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For each config map you want to mount as a volume, add the following YAML to the `volumes` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
volumes:
- configMap: myconfigmap
  path: /workspace/configmap
----
+
* Substitute `myconfigmap` with the name of the target config map.
* Substitute `/workspace/configmap` with the path where you want to mount the config map.
+
For example, to mount the `addresses` config map, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
volumes:
- configMap: addresses
  path: /workspace/configmap-addresses
----

. Save the configuration.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-key-value-in-secret-to-env-variable_{context}"]
= Setting environment variable from a key value defined in a secret

You can set an environment variable from a key value defined as a secret. A value previously stored in a secret can then be accessed as an environment variable by the function at runtime. This can be useful for getting access to a value stored in a secret, such as the ID of a user.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For each value from a secret key-value pair that you want to assign to an environment variable, add the following YAML to the `envs` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- name: EXAMPLE
  value: '{{ secret:mysecret:key }}'
----
+
* Substitute `EXAMPLE` with the name of the environment variable.
* Substitute `mysecret` with the name of the target secret.
* Substitute `key` with the key mapped to the target value.
+
For example, to access the user ID that is stored in `userdetailssecret`, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:userdetailssecret:userid }}'
----

. Save the configuration.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-key-value-in-configmap-to-env-variable_{context}"]
= Setting environment variable from a key value defined in a config map

You can set an environment variable from a key value defined as a config map. A value previously stored in a config map can then be accessed as an environment variable by the function at runtime. This can be useful for getting access to a value stored in a config map, such as the ID of a user.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For each value from a config map key-value pair that you want to assign to an environment variable, add the following YAML to the `envs` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- name: EXAMPLE
  value: '{{ configMap:myconfigmap:key }}'
----
+
* Substitute `EXAMPLE` with the name of the environment variable.
* Substitute `myconfigmap` with the name of the target config map.
* Substitute `key` with the key mapped to the target value.
+
For example, to access the user ID that is stored in `userdetailsmap`, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:userdetailsmap:userid }}'
----

. Save the configuration.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-all-values-in-secret-to-env-variables_{context}"]
= Setting environment variables from all values defined in a secret

You can set an environment variable from all values defined in a secret. Values previously stored in a secret can then be accessed as environment variables by the function at runtime. This can be useful for simultaneously getting access to a collection of values stored in a secret, for example, a set of data pertaining to a user.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For every secret for which you want to import all key-value pairs as environment variables, add the following YAML to the `envs` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ secret:mysecret }}' <1>
----
<1> Substitute `mysecret` with the name of the target secret.
+
For example, to access all user data that is stored in `userdetailssecret`, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:userdetailssecret }}'
----

. Save the configuration.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-all-values-in-configmap-to-env-variables_{context}"]
= Setting environment variables from all values defined in a config map

You can set an environment variable from all values defined in a config map. Values previously stored in a config map can then be accessed as environment variables by the function at runtime. This can be useful for simultaneously getting access to a collection of values stored in a config map, for example, a set of data pertaining to a user.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For every config map for which you want to import all key-value pairs as environment variables, add the following YAML to the `envs` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:myconfigmap }}' <1>
----
<1> Substitute `myconfigmap` with the name of the target config map.
+
For example, to access all user data that is stored in `userdetailsmap`, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:userdetailsmap }}'
----

. Save the file.
