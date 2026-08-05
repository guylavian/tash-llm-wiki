---
title: "Using configuration snippets"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-config-snippets
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-config-snippets
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Using configuration snippets

[id="microshift-config-snippets"]
= Using configuration snippets

[role="_abstract"]
To configure one or two settings in OpenShift Container Platform, use the `/etc/microshift/config.d/` configuration directory to drop in configuration snippet YAML files. Restart {microshift-short} for new or changed snippets to apply.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-config-snippets.adoc

[id="microshift-how-config-snippets-work_{context}"]
= How configuration snippets work

[role="_abstract"]
Configuration snippets in OpenShift Container Platform are YAML files in `/etc/microshift/config.d/` that merge with the existing configuration at runtime. You can use them to change one or two settings without editing the main config file.

You must restart {microshift-short} for new configurations to apply.

To return to previous values, you can delete a configuration snippet and restart {microshift-short}.

At runtime, the YAML files inside `/etc/microshift/config.d` are merged into the existing {microshift-short} configuration, whether that configuration is a result of default values or a user-created `config.yaml` file. You do not need to create a `config.yaml` file to use a configuration snippet.

Files in the snippet directory are sorted in lexicographical order and run sequentially. You can use numerical prefixes for snippets so that each is read in the order you want. The last-read file takes precedence when there is more than one YAML for the same parameter.

[IMPORTANT]
====
Configuration snippets take precedence over both default values and a customized `config.yaml` configuration file.
====

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-config-snippets.adoc

[id="microshift-ex-config-snippets-lists_{context}"]
= Examples of configuration snippet lists or arrays

[role="_abstract"]
Lists and arrays in OpenShift Container Platform configuration snippets are overwritten, not merged.

For example, you can replace a SAN or list of SANs by creating an additional snippet for the same field that is read after the first:

{microshift-short} configuration directory contents:: `/etc/microshift/config.yaml.default` or `/etc/microshift/config.yaml`

Example {microshift-short} configuration snippet directory contents:: `/etc/microshift/config.d/10-san.yaml` and `/etc/microshift/config.d/20-san.yaml`

.Example `10-san.yaml` snippet
[source,yaml]
----
apiServer:
  subjectAltNames:
    - host1
    - host2
----

.Example `20-san.yaml` snippet
[source,yaml]
----
apiServer:
  subjectAltNames:
    - hostZ
----

.Example configuration result
[source,yaml]
----
apiServer:
  subjectAltNames:
    - hostZ
----

If you want to add a value to an existing list, you can add it to an existing snippet. For example, to add `hostZ` to an existing list of SANs, edit the snippet you have instead of creating a new one:

.Example `10-san.yaml` snippet
[source,yaml]
----
apiServer:
  subjectAltNames:
    - host1
    - host2
    - hostZ
----

.Example configuration result
[source,yaml]
----
apiServer:
  subjectAltNames:
    - host1
    - host2
    - hostZ
----

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-config-snippets.adoc

[id="microshift-example-config-snippets-objects_{context}"]
= Example configuration snippets that are objects

[role="_abstract"]
Object fields in OpenShift Container Platform are merged together when you use a configuration snippet.

.Example `10-advertiseAddress.yaml` snippet
[source,yaml]
----
apiServer:
  advertiseAddress: "microshift-example"
----

.Example `20-audit-log.yaml` snippet
[source,yaml]
----
apiServer:
  auditLog:
    maxFileAge: 12
----

.Example configuration result
[source,yaml]
----
apiServer:
  advertiseAddress: "microshift-example"
  auditLog:
    maxFileAge: 12
----

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-config-snippets.adoc

[id="microshift-example-mixed-config-snippets_{context}"]
= Examples of mixed configuration snippets

[role="_abstract"]
When you use mixed configuration snippets in OpenShift Container Platform, object fields merge and the last-read snippet replaces list values. File order controls which list entries apply.

In the following example, the values of both `advertiseAddress` and `auditLog.maxFileAge` fields merge into the configuration, but only the `c.com` and `d.com` `subjectAltNames` values are retained. This happens because the numbering in the filename indicates that the `c.com` and `d.com` values are higher priority.

.Example `10-advertiseAddress.yaml` snippet
[source,yaml]
----
apiServer:
  advertiseAddress: "microshift-example"
----

.Example `20-audit-log.yaml` snippet
[source,yaml]
----
apiServer:
  auditLog:
    maxFileAge: 12
----

.Example `30-SAN.yaml` snippet
[source,yaml]
----
apiServer:
  subjectAltNames:
    - a.com
    - b.com
----

.Example `40-SAN.yaml` snippet
[source,yaml]
----
apiServer:
  subjectAltNames:
    - c.com
    - d.com
----

.Example configuration result
[source,yaml]
----
apiServer:
  advertiseAddress: "microshift-example"
  auditLog:
    maxFileAge: 12
  subjectAltNames:
    - c.com
    - d.com
----
