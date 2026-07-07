---
title: "Identifying URL of a Tang server deployed with the NBDE Tang Server Operator"
type: reference
domain: openshift
slug: security-4-22-nbde-tang-server-operator-identifying-url
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/nbde-tang-server-operator-identifying-url
version: 4.22
family: security
documentKind: "Documentation"
---

# Identifying URL of a Tang server deployed with the NBDE Tang Server Operator

[id="identifying-url-nbde-tang-server-operator"]
= Identifying URL of a Tang server deployed with the NBDE Tang Server Operator

Before you can configure your Clevis clients to use encryption keys advertised by your Tang servers, you must identify the URLs of the servers.

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-identifying-url.adoc

[id="identifying-url-nbde-tang-server-operator-using-web-console_{context}"]
= Identifying URL of the NBDE Tang Server Operator using the web console

You can identify the URLs of Tang servers deployed with the NBDE Tang Server Operator from the software catalog by using the OpenShift Container Platform web console. After you identify the URLs, you use the `clevis luks bind` command on your clients containing LUKS-encrypted volumes that you want to unlock automatically by using keys advertised by the Tang servers. See the Configuring manual enrollment of LUKS-encrypted volumes section in the RHEL 9 Security hardening document for detailed steps describing the configuration of clients with Clevis.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You deployed a Tang server by using the NBDE Tang Server Operator on your OpenShift cluster.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators* -> *Tang Server*.

. On the NBDE Tang Server Operator details page, select *Tang Server*.
+
image::nbde-tang-server-operator-19-tangserver-details.png[NBDE Tang Server Operator details]

. The list of Tang servers deployed and available for your cluster appears. Click the name of the Tang server you want to bind with a Clevis client.

. The web console displays an overview of the selected Tang server. You can find the URL of your Tang server in the `Tang Server External Url` section of the screen:
+
image::nbde-tang-server-operator-21-tangserver-overview.png[NBDE Tang Server Operator overview of a Tang server]
+
In this example, the URL of the Tang server is `\http://34.28.173.205:7500`.

.Verification

* You can check that the Tang server is advertising by using `curl`, `wget`, or similar tools, for example:
+
[source,terminal]
----
$ curl 2> /dev/null http://34.28.173.205:7500/adv  | jq
----
+
.Example output
[source,terminal]
----
{
  "payload": "eyJrZXlzIj…eSJdfV19",
  "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI6Imp3ay1zZXQranNvbiJ9",
  "signature": "AUB0qSFx0FJLeTU…aV_GYWlDx50vCXKNyMMCRx"
}
----

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-identifying-url.adoc

[id="identifying-url-nbde-tang-server-operator-using-cli_{context}"]
= Identifying URL of the NBDE Tang Server Operator using CLI

You can identify the URLs of Tang servers deployed with the NBDE Tang Server Operator from the software catalog by using the CLI. After you identify the URLs, you use the `clevis luks bind` command on your clients containing LUKS-encrypted volumes that you want to unlock automatically by using keys advertised by the Tang servers. See the Configuring manual enrollment of LUKS-encrypted volumes section in the RHEL 9 Security hardening document for detailed steps describing the configuration of clients with Clevis.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You have installed the OpenShift CLI (`oc`).
* You deployed a Tang server by using the NBDE Tang Server Operator on your OpenShift cluster.

.Procedure

. List details about your Tang server, for example:
+
[source,terminal]
----
$ oc -n nbde describe tangserver
----
+
.Example output
[source,terminal]
----
…
Spec:
…
Status:
  Ready:                 1
  Running:               1
  Service External URL:  http://34.28.173.205:7500/adv
  Tang Server Error:     No
Events:
…
----

. Use the value of the `Service External URL:` item without the `/adv` part. In this example, the URL of the Tang server is `\http://34.28.173.205:7500`.

.Verification

* You can check that the Tang server is advertising by using `curl`, `wget`, or similar tools, for example:
+
[source,terminal]
----
$ curl 2> /dev/null http://34.28.173.205:7500/adv  | jq
----
+
.Example output
[source,terminal]
----
{
  "payload": "eyJrZXlzIj…eSJdfV19",
  "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI6Imp3ay1zZXQranNvbiJ9",
  "signature": "AUB0qSFx0FJLeTU…aV_GYWlDx50vCXKNyMMCRx"
}
----

[id="additional-resources-identifying-url-nbde-tang-server-operator"]
[role="_additional-resources"]
== Additional resources

* Configuring manual enrollment of LUKS-encrypted volumes
