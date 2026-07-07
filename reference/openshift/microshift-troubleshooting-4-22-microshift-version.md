---
title: "Checking which version you have installed"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-version
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-version
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Checking which version you have installed

[id="microshift-version"]
= Checking which version you have installed

[role="_abstract"]
To begin troubleshooting, you must know which version of OpenShift Container Platform you have installed.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-version.adoc

[id="microshift-version-cli_{context}"]
= Checking the version using the command-line interface

[role="_abstract"]
To begin troubleshooting, you must know your {microshift-short} version. One way to get this information is by using the command-line interface (CLI).

.Procedure

* Check the version information by running the following command:
+
[source,terminal]
----
$ microshift version
----
+
.Example output
[source,terminal,subs="attributes+"]
----
{microshift-short} Version: -0.microshift-e6980e25
Base OCP Version: 
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-version.adoc

[id="microshift-version-api_{context}"]
= Checking the {microshift-short} version using the API

[role="_abstract"]
To begin troubleshooting, you must know your {microshift-short} version. One way to get this information is by using the API.

.Procedure

* To get the version number using the {oc-first}, view the `kube-public/microshift-version` config map by running the following command:
+
[source,terminal]
----
$ oc get configmap -n kube-public microshift-version -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
data:
  major: "4"
  minor: "20"
  version: 4.20.0-0.microshift-fa441af87431
kind: ConfigMap
metadata:
  creationTimestamp: "2025-11-03T21:06:11Z"
  name: microshift-version
  namespace: kube-public
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-version.adoc
// * microshift_support/microshift-etcd.adoc

[id="microshift-version-etcd_{context}"]
= Checking the etcd version

[role="_abstract"]
You can get the version information for the etcd database included with your {microshift-short} by using one or both of the following methods, depending on the level of information that you need.

.Procedure

* To display the base database version information, run the following command:
+
[source,terminal]
----
$ microshift-etcd version
----
+
.Example output
[source,terminal,subs="attributes+"]
----
microshift-etcd Version: 4.20.0
Base etcd Version: 3.5.13
----

* To display the full database version information, run the following command:
+
[source,terminal]
----
$ microshift-etcd version -o json
----
+
.Example output
[source,terminal]
----
{
  "major": "4",
  "minor": "20",
  "gitVersion": "4.20.0",
  "gitCommit": "140777711962eb4e0b765c39dfd325fb0abb3622",
  "gitTreeState": "clean",
  "buildDate": "2025-11-03T16:37:53Z",
  "goVersion": "go1.21.9"
  "compiler": "gc",
  "platform": "linux/amd64",
  "patch": "",
  "etcdVersion": "3.5.13"
}
----
