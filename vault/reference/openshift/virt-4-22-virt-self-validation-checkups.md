---
title: "Self validation checkup"
type: reference
domain: openshift
slug: virt-4-22-virt-self-validation-checkups
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-self-validation-checkups
version: 4.22
family: virt
documentKind: "Documentation"
---

# Self validation checkup

[id="virt-self-validation-checkups"]
= Self validation checkup

[role="_abstract"]
As a cluster administrator, you can run a self validation checkup to validate the stability, health, and compliance of an {VirtProductName} installation. A self validation checkup enables you to run conformance tests on critical subsystems, such as networking and storage, to verify that the environment is fully functional and self-sustained before you deploy production workloads.

Running a self validation checkup streamlines the process of running functional tests, which are fully aligned with the exact build version of {VirtProductName} currently installed on the cluster.

You can view high-level summaries and detailed logs in a downloaded results file, or run tier 2 tests, enabling you to identify and resolve configuration issues without requiring external support immediately.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-self-validation-checkups.adoc

[id="virt-run-self-validation-checkup-web-console_{context}"]
= Run a self validation checkup in the web console

[role="_abstract"]
Running a self validation checkup streamlines the process of running functional tests, which enables you to validate the stability, health, and compliance of an {VirtProductName} installation before deploying workloads. You can run a self validation checkup as a cluster administrator in the OpenShift Container Platform web console.

.Prerequisites

* You have cluster administrator permissions.
* You have access to an OpenShift Container Platform cluster where {VirtProductName} is installed.
* You are logged in to the OpenShift Container Platform web console.

.Procedure

. In the OpenShift Container Platform web console, go to *Virtualization* -> *Checkups*.
. Go to the *Self validation* tab.
. Click *Run checkup*.
. Configure settings for the test that you want to run.
. Optional: You can enable a dry run test by clicking *Advanced settings* and then toggling the *Dry run* button.
. Click *Run*. The *Self validation checkup details* page is displayed.
+
You can observe the self validation checkup running in real time. The test can take several hours to complete.

. After the test is complete, you can view high-level results in the *Self validation checkup details* page, including the names of any failing tests.
. Optional: You can download detailed results as a ZIP file by clicking *Download results* in the *Self validation checkup details* page.
