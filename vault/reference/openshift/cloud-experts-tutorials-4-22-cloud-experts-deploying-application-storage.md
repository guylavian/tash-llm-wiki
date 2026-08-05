---
title: "Tutorial: Persistent volumes for cluster storage"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-storage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-storage
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Persistent volumes for cluster storage

[id="cloud-experts-deploying-application-storage"]
= Tutorial: Persistent volumes for cluster storage

[role="_abstract"]
OpenShift Container Platform supports storing persistent volumes with either Amazon Web Services (AWS) Elastic Block Store (EBS) or AWS Elastic File System (EFS).

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-storage.adoc

[id="cloud-experts-deploying-application-storage-persistent-volumes_{context}"]
= Using persistent volumes

[role="_abstract"]
Use the following procedures to create a file, store it on a persistent volume in your cluster, and confirm that it still exists after pod failure and re-creation.

.Procedure
. View your persistent volume claim by navigating to the cluster's OpenShift web console.
. Click *Storage* in the left menu, then click *PersistentVolumeClaims* to see a list of all the persistent volume claims.
. Click a persistence volume claim to see the size, access mode, storage class, and other additional claim details.
+
[NOTE]
====
The access mode is `ReadWriteOnce` (RWO). This means that the volume can only be mounted to one node and the pod or pods can read and write to the volume.
====
. In the OSToy app console, click *Persistent Storage* in the left menu.
. In the *Filename* box, enter a file name with a `.txt` extension, for example `test-pv.txt`.
. In the *File contents* box, enter a sentence of text, for example `OpenShift is the greatest thing since sliced bread!`.
. Click *Create file*.
+
image::cloud-experts-storage-ostoy-createfile.png[]

.Verification
. Scroll to *Existing files* on the OSToy app console.
. Click the file you created to see the file name and contents.
+
image::cloud-experts-storage-ostoy-viewfile.png[]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-storage.adoc

[id="cloud-experts-deploying-application-storage-crashing-pod_{context}"]
= Crashing the pod

[role="_abstract"]
Crash the pod to test that persistent storage persists across pod restarts.

.Procedure
. On the OSToy app console, click *Home* in the left menu.
. Click *Crash pod*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-storage.adoc

[id="cloud-experts-deploying-application-storage-verification_{context}"]
= Verifying persistent storage

[role="_abstract"]
Verify that the file you created persists after the pod is recreated and confirm the contents are intact.

.Procedure
. Wait for the pod to re-create.
. On the OSToy app console, click *Persistent Storage* in the left menu.
. Find the file you created, and open it to view and confirm the contents.
+
image::cloud-experts-storage-ostoy-existingfile.png[]

.Verification
The deployment YAML file shows that we mounted the directory `/var/demo_files` to our persistent volume claim.

. Retrieve the name of your front-end pod by running the following command:
+
[source,terminal]
----
$ oc get pods
----
+
. Start a secure shell (SSH) session in your container by running the following command:
+
[source,terminal]
----
$ oc rsh <pod_name>
----
+
. Go to the directory by running the following command:
+
[source,terminal]
----
$ cd /var/demo_files
----
+
. *Optional:* See all the files you created by running the following command:
+
[source,terminal]
----
$ ls
----
+
. Open the file to view the contents by running the following command:
+
[source,terminal]
----
$ cat test-pv.txt
----
+
. Verify that the output is the text you entered in the OSToy app console.
+
.Example terminal
[source,terminal]
----
$ oc get pods
NAME                                  READY     STATUS    RESTARTS   AGE
ostoy-frontend-5fc8d486dc-wsw24       1/1       Running   0          18m
ostoy-microservice-6cf764974f-hx4qm   1/1       Running   0          18m

$ oc rsh ostoy-frontend-5fc8d486dc-wsw24

$ cd /var/demo_files/

$ ls
lost+found   test-pv.txt

$ cat test-pv.txt
OpenShift is the greatest thing since sliced bread!
----
. Type `exit` in your terminal to quit the session and return to the CLI.

[role="_additional-resources"]
.Additional resources
* Understanding persistent storage
* Storage overview
