---
title: "Configuring and managing Tang servers using the NBDE Tang Server Operator"
type: reference
domain: openshift
slug: security-4-22-nbde-tang-server-operator-configuring-managing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/nbde-tang-server-operator-configuring-managing
version: 4.22
family: security
documentKind: "Documentation"
---

# Configuring and managing Tang servers using the NBDE Tang Server Operator

[id="configuring-and-managing-nbde-tang-server-operator"]
= Configuring and managing Tang servers using the NBDE Tang Server Operator

With the NBDE Tang Server Operator, you can deploy and quickly configure Tang servers. On the deployed Tang servers, you can list existing keys and rotate them.

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc

[id="deploying-nbde-tang-server_{context}"]
= Deploying a Tang server using the NBDE Tang Server Operator

You can deploy and quickly configure one or more Tang servers using the NBDE Tang Server Operator in the web console.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You have installed the NBDE Tang Server Operator on your OCP cluster.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Select *Project*, and click *Create Project*:
+
image::nbde-tang-server-operator-07-create-project.png[Create Project in the web console]
. On the `Create Project` page, fill in the required information, for example:
+
image::nbde-tang-server-operator-09-project-values.png[Example values on the Create Project page]
. Click *Create*.
. NBDE Tang Server replicas require a Persistent Volume Claim (PVC) for storing encryption keys. In the web console, navigate to *Storage* -> *PersistentVolumeClaims*:
+
image::nbde-tang-server-operator-11-pvc.png[PersistentVolumeClaims in the Storage menu]
. On the following `PersistentVolumeClaims` screen, click *Create PersistentVolumeClaim*.
. On the `Create PersistentVolumeClaim` page, select a storage that fits your deployment scenario. Consider how often you want to rotate the encryption keys. Name your PVC and choose the claimed storage capacity, for example:
+
image::nbde-tang-server-operator-13-create-pvc.png[Create PersistentVolumeClaims page]
. Navigate to *Ecosystem* -> *Installed Operators*, and click *NBDE Tang Server*.
. Click *Create instance*.
+
image::nbde-tang-server-operator-15-create-instance.png[Create NBDE Tang Server instance]
. On the `Create TangServer` page, choose the name of the Tang Server instance, amount of replicas, and specify the name of the previously created Persistent Volume Claim, for example:
+
image::nbde-tang-server-operator-17-create-tangserver.png[Create TangServer page]
. After you enter the required values a change settings that differ from the default values in your scenario, click *Create*.

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc

[id="rotating-keys-using-nbde-tang-server-operator_{context}"]
= Rotating keys using the NBDE Tang Server Operator

With the NBDE Tang Server Operator, you also can rotate your Tang server keys. The precise interval at which you should rotate them depends on your application, key sizes, and institutional policy.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You deployed a Tang server using the NBDE Tang Server Operator on your OpenShift cluster.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List the existing keys on your Tang server, for example:
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
Status:
  Active Keys:
	File Name:  	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
	Generated:  	2022-02-08 15:44:17.030090484 +0000
	sha1:       	PvYQKtrTuYsMV2AomUeHrUWkCGg
	sha256:     	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
----
. Create a YAML file for moving your active keys to hidden keys, for example, `minimal-keyretrieve-rotate-tangserver.yaml`:
+
.Example key-rotation YAML for tang-operator
[source,yaml]
----
apiVersion: daemons.redhat.com/v1alpha1
kind: TangServer
metadata:
  name: tangserver
  namespace: nbde
  finalizers:
    - finalizer.daemons.tangserver.redhat.com
spec:
  replicas: 1
  hiddenKeys:
    - sha1: "PvYQKtrTuYsMV2AomUeHrUWkCGg" <1>
----
<1> Specify the SHA-1 thumbprint of your active key to rotate it.

. Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f minimal-keyretrieve-rotate-tangserver.yaml
----

.Verification

. After a certain amount of time depending on your configuration, check that the previous `activeKey` value is the new `hiddenKey` value and the `activeKey` key file is newly generated, for example:
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
  Hidden Keys:
    sha1:    PvYQKtrTuYsMV2AomUeHrUWkCGg
  Replicas:  1
Status:
  Active Keys:
    File Name:  T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY.jwk
    Generated:  2023-10-25 15:38:18.134939752 +0000
    sha1:       vVxkNCNq7gygeeA9zrHrbc3_NZ4
    sha256:     T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY
  Hidden Keys:
    File Name:           .QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg.jwk
    Generated:           2023-10-25 15:37:29.126928965 +0000
    Hidden:              2023-10-25 15:38:13.515467436 +0000
    sha1:                PvYQKtrTuYsMV2AomUeHrUWkCGg
    sha256:              QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
----

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc

[id="deleting-hidden-keys-with-nbde-tang-server-operator_{context}"]
= Deleting hidden keys with the NBDE Tang Server Operator

After you rotate your Tang server keys, the previously active keys become hidden and are no longer advertised by the Tang instance. You can use the NBDE Tang Server Operator to remove encryption keys no longer used.

WARNING:: Do not remove any hidden keys unless you are sure that all bound Clevis clients already use new keys.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You deployed a Tang server using the NBDE Tang Server Operator on your OpenShift cluster.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List the existing keys on your Tang server, for example:
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
Status:
  Active Keys:
	File Name:  	PvYQKtrTuYsMV2AomUeHrUWkCGg.jwk
	Generated:  	2022-02-08 15:44:17.030090484 +0000
	sha1:	    	PvYQKtrTuYsMV2AomUeHrUWkCGg
	sha256:	    	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
----
. Create a YAML file for removing all hidden keys, for example, `hidden-keys-deletion-tangserver.yaml`:
+
.Example hidden-keys-deletion YAML for tang-operator
[source,yaml]
----
apiVersion: daemons.redhat.com/v1alpha1
kind: TangServer
metadata:
  name: tangserver
  namespace: nbde
  finalizers:
    - finalizer.daemons.tangserver.redhat.com
spec:
  replicas: 1
  hiddenKeys: [] <1>
----
<1> The empty array as the value of the `hiddenKeys` entry indicates you want to preserve no hidden keys on your Tang server.

. Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f hidden-keys-deletion-tangserver.yaml
----

.Verification

. After a certain amount of time depending on your configuration, check that the previous active key still exists, but no hidden key is available, for example:
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
  Hidden Keys:
    sha1:    PvYQKtrTuYsMV2AomUeHrUWkCGg
  Replicas:  1
Status:
  Active Keys:
    File Name:  T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY.jwk
    Generated:  2023-10-25 15:38:18.134939752 +0000
    sha1:       vVxkNCNq7gygeeA9zrHrbc3_NZ4
    sha256:     T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY
Status:
  Ready:                 1
  Running:               1
  Service External URL:  http://35.222.247.84:7500/adv
  Tang Server Error:     No
Events:
…
----
