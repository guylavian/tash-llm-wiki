---
title: "Using feature gates to develop solutions for your applications"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-feature-gates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-feature-gates
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Using feature gates to develop solutions for your applications

[id="microshift-feature-gates"]
= Using feature gates to develop solutions for your applications

[role="_abstract"]
Use feature gates to test new Kubernetes features for potential use in your {microshift-short} deployments.

// Module included in the following assemblies:
//
// microshift_configuring/microshift-feature-gates.adoc

[id="microshift-feature-gates-con_{context}"]
= Understanding feature gates for {microshift-short}

[role="_abstract"]
As an application developer for edge computing environments, you can now experiment with upcoming Kubernetes features to evaluate their potential benefits for specific use cases.

By using feature gates, you can test various enhancements that might improve performance in your resource-constrained edge environments. For example, you can try advanced CPU management, enhanced scheduling features, or experimental storage options.

[WARNING]
====
When you trial new features using feature gates, your {microshift-short} can become unstable or lose data. Enable feature gates only in non-production environments.
====

When planning to use feature gates for development, consider the following details:

* After you specify feature gates, you cannot update {microshift-short}.
* If your configuration is not valid, {microshift-short} can fail to start.
* The Kubernetes components you enable handle feature gate validation.
* Feature gates are disabled by default in {microshift-short}. After you enable feature gates, you cannot disable them.

// Module included in the following assemblies:
//
// microshift_configuring/microshift-feature-gates.adoc

[id="microshift-feature-gates-using_{context}"]
= Using feature gates for {microshift-short}

[role="_abstract"]
To use feature gates in your development environment, you must specify them in the `config.yaml` file or create a configuration snippet file. You must also configure the feature set you want to work with.

[IMPORTANT]
====
* A `config.yaml` configuration file takes precedence over built-in settings. The `config.yaml` file is read every time the {microshift-short} service starts.
* Configuration snippet YAMLs take precedence over both built-in settings and the `config.yaml` configuration file.
* After you enable feature gates, you cannot disable them.
====

.Prerequisites

* You installed {microshift-short}.
* You installed the {oc-first}.
* You have `sudo` privileges on the {microshift-short} host.

.Procedure

. Apply features gates in one of the two following ways:

.. Update the {microshift-short} `config.yaml` configuration file by making a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory. Name it `config.yaml` and keep it in the source directory.

.. Use a configuration snippet to apply the ingress control settings you want. To do this, create a configuration snippet YAML file and put it in the `/etc/microshift/config.d/` configuration directory. For example, `/etc/microshift/config.d/10-feature-gate.yaml`.

. Replace the default values in the `xyz` section of the {microshift-short} YAML with your valid values, or create a configuration snippet file with the sections you need.
+
.Feature gates configuration with example values
[source,yaml]
----
# ...
apiServer:
  featureGates:
    featureSet: TechPreviewNoUpgrade
# ...
apiServer:
  featureGates:
    featureSet: CustomNoUpgrade
    customNoUpgrade:
      enabled:
      - "CPUManagerPolicyAlphaOptions"
      - "MemoryQoS"
      disabled:
      - "SomeDefaultEnabledFeature"
# ...
----

. Use the following configuration rules:
.. You must set the `featureSet` field when configuring feature gates.
.. When you use `customNoUpgrade` feature, you must set the `featureSet` to `CustomNoUpgrade`. The `customNoUpgrade` field is only valid when `featureSet: CustomNoUpgrade`.
.. If you have a support exception for a customized node, make sure that the custom feature you want to use appears in the `specialHandlingSupportExceptionRequired` field and is enabled. The custom feature must also be enabled in the `customNoUpgrade` field.
+
[NOTE]
====
If a feature is enabled in the `specialHandlingSupportExceptionRequired` field, your customized node can upgrade in the same manner as a supported node.
====
+
.Custom feature example configuration
[source,yaml]
----
# ...
apiServer:
   featureGates:
     featureSet: customNoUpgrade
     customNoUpgrade:
       enabled:
       - "SomeFeature"
     specialHandlingSupportExceptionRequired:
       enabled:
       - "SomeFeature"
# ...
----

. Configure any settings required for the feature set you want to work with.

. Restart {microshift-short} to apply the configuration changes by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
