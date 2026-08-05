---
title: "Persistent volumes for cluster storage"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-application-storage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-application-storage
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Persistent volumes for cluster storage

[id="learning-deploying-application-storage"]
= Persistent volumes for cluster storage

[role="_abstract"]
Configure persistent volumes for your OpenShift Container Platform clusters by using Amazon Web Services (AWS) Elastic Block Store (EBS) or AWS Elastic File System (EFS). Utilizing these storage options allows you to safely retain and manage your containerized application data.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-using-persistent-volumes_{context}"]
= Using persistent volumes

[role="_abstract"]
Test your cluster's persistent volume by creating a file, storing it, then purposefully causing a pod failure. Confirming that the file still exists after the pod is re-created demonstrates how your data is protected during unexpected outages.
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-viewing_{context}"]
= Viewing a persistent volume claim

[role="_abstract"]
To verify your storage configuration, view your application's persistent volume claim from {cluster-manager-first}.

.Procedure
. Navigate to the cluster's {ocp-short} web console.
. Click *Storage* in the left menu, then click *PersistentVolumeClaims* to see a list of all the persistent volume claims.
. Click a persistent volume claim to see the size, access mode, storage class, and other additional claim details.
+
[NOTE]
====
The access mode is `ReadWriteOnce` (RWO). This means that the volume can only be mounted to one node and the pod or pods can read and write to the volume.
====
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-storing_{context}"]
= Storing your file

[role="_abstract"]
To demonstrate the persistent storage capabilities of the cluster, store files within your application by using the OSToy console.

.Procedure
. In the OSToy app console, click *Persistent Storage* in the left menu.
. In the *Filename* box, enter a file name with a `.txt` extension, for example `test-pv.txt`.
. In the *File contents* box, enter a sentence of text, for example `OpenShift is the greatest thing since sliced bread!`.
. Click *Create file*.
+
image::cloud-experts-storage-ostoy-createfile.png[]
+
.Verification
. Scroll to *Existing files* on the OSToy app console.
. Click the file you created to see the file name and contents.
+
image::cloud-experts-storage-ostoy-viewfile.png[]
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-crash-pod_{context}"]
= Crashing the pod

[role="_abstract"]
To demonstrate the persistent storage of your cluster, cause the pod of your application to crash from the OSToy application console.

.Procedure
. On the OSToy application console, click *Home* in the left menu.
. Click *Crash pod*.
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-confirm_{context}"]
= Confirming persistent storage

[role="_abstract"]
To ensure your data is retained after a pod shuts down, you can verify the persistent storage configuration for your OSToy application.

.Procedure
. Wait for the pod to re-create.
. On the OSToy application console, click *Persistent Storage* in the left menu.
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
. Verify that the output is the text you entered in the OSToy application console.
+
*For example*:
+
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
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-storage.adoc
[id="learning-deploying-application-storage-end-session_{context}"]
= Ending the session

[role="_abstract"]
To securely close your workspace and free up system resources, end your session from the terminal.

.Procedure
* Type `exit` in your terminal to quit the session and return to the command line interface (CLI).

[role="_additional-resources"]
== Additional resources
* Understanding persistent storage
* Storage overview
* Amazon Web Services (AWS) Elastic Block Store (EBS)
* AWS Elastic File System (EFS)
