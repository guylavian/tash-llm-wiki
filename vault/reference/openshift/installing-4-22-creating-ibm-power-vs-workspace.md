---
title: "Creating an {ibm-power-server-title} workspace"
type: reference
domain: openshift
slug: installing-4-22-creating-ibm-power-vs-workspace
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/creating-ibm-power-vs-workspace
version: 4.22
family: installing
documentKind: "Documentation"
---

# Creating an {ibm-power-server-title} workspace

[id="creating-ibm-power-vs-workspace"]
= Creating an {ibm-power-server-title} workspace

// * installing/installing_ibm_powervs/creating-ibm-power-vs-workspace.adoc

[id="creating-ibm-power-vs-workspace-procedure_{context}"]
= Creating an {ibm-power-server-title} workspace

Use the following procedure to create an {ibm-power-server-name} workspace.

.Procedure

. To create an {ibm-power-server-name} workspace, complete step 1 to step 5 from the {ibm-cloud-name} documentation for Creating an {ibm-power-server-name}.

. After it has finished provisioning, retrieve the 32-character alphanumeric Globally Unique Identifier (GUID) of your new workspace by entering the following command:
+
[source,terminal]
----
$ ibmcloud resource service-instance <workspace name>
----
+

[id="next-steps_creating-ibm-power-vs-workspace"]
== Next steps
* Installing a cluster on {ibm-power-server-name} with customizations
