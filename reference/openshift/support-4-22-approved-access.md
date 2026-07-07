---
title: "Approved access"
type: reference
domain: openshift
slug: support-4-22-approved-access
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/approved-access
version: 4.22
family: support
documentKind: "Documentation"
---

# Approved access

[id="approved-access"]
= Approved access

[role="_abstract"]
With Red{nbsp}Hat Site Reliability Engineering (SRE), you typically do not need elevated access to systems to do normal operations to manage and support your OpenShift Container Platform clusters. If you have elevated access, you can give SRE the access levels of a cluster-admin role.

In the unlikely event that SRE needs elevated access to systems, use the _Approved Access_ interface to review and _approve_ or _deny_ access to these systems. SRE can create elevated access requests to {product-rosa} clusters and the corresponding cloud accounts in response to a customer-initiated support ticket or to alerts as part of the standard incident response process.

When you enable _Approved Access_ and an SRE creates an access request, _cluster owners_ receive an email notification informing them of a new access request. The email notification has a link allowing the cluster owner to approve or deny the access request. If you do not respond to this request, there is a risk to your service-level agreement (SLA) for {product-rosa}.

[NOTE]
====
Denying an access request requires you to complete the *Justification* field. In this case, SRE cannot directly act on the resources related to the incident. Customers can still use the *Red Hat Customer Support* resource to help investigate and resolve any issues.
====

// Module included in the following assemblies:
//
// * support/getting-support.adoc
// * osd_architecture/osd-support.adoc

[id="support-submitting-a-case-enable-approved-access_{context}"]
= Enabling approved access for ROSA clusters by submitting a support case

[role="_abstract"]
{product-rosa} _Approved Access_ is not enabled by default. To enable _Approved Access_ for your {product-rosa} clusters, you should create a support ticket.

.Procedure

. Log in to the *Customer Support* page of the Red{nbsp}Hat Customer Portal.

. Click *Get support*.

. On the *Cases* tab of the *Customer support* page:

.. Optional: Change the pre-filled account and owner details if needed.

.. Select the *Configuration* category and click *Continue*.

. Enter the following information:

.. In the *Product* field, select *OpenShift Container Platform*.
.. In the *Product* field, select *OpenShift Container Platform {hcp-capital}*.
.. In the *Problem statement* field, enter *Enable ROSA Access Protection*.
.. Click *See more options*.

. Select *OpenShift Cluster ID* from the drop-down list.

. Fill the remaining mandatory fields in the form:

.. What are you experiencing? What are you expecting to happen?
... Fill with *Approved Access*.

.. Define the value or impact to you or the business.
... Fill with *Approved Access*.
.. Click *Continue*.

. Select *Severity* as *4(Low)* and click *Continue*.

. Preview the case details and click *Submit*.

// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc

[id="support-reviewing-an-access-request-from-an-email-notification_{context}"]
= Reviewing an access request from an email notification

[role="_abstract"]
Cluster owners receive an email notification when Red{nbsp}Hat Site Reliability Engineering (SRE) request access to their cluster with a link to review the request in the {hybrid-console-second}.

.Prerequisites
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Click the link within the email to bring you to the {hybrid-console-second}.

. In the *Access Request Details* dialog, click *Approve* or *Deny* under *Decision*.
+
[NOTE]
====
Denying an access request requires you to complete the *Justification* field. In this case, SRE cannot directly act on the resources related to the incident. Customers can still use the *Customer Support* to help investigate and resolve any issues.
====

. Click *Save*.

// Module included in the following assemblies:
//
// * support/getting-support.adoc
// * osd_architecture/osd-support.adoc

[id="support-reviewing-an-access-request-from-the-hybrid-cloud-console_{context}"]
= Reviewing an access request from the {hybrid-console-second}

[role="_abstract"]
Review access requests for your {product-rosa} clusters from the {hybrid-console-second}.

.Prerequisites
* You have access to the cluster as a user with the `Cluster Owner` role.

.Procedure

. Navigate to {cluster-manager-url} and select *Cluster List*.

. Click the cluster name to review the *Access Request*.

. Select the *Access Requests* tab to list all *states*.

. Select *Open* under *Actions* for the *Pending* state.

. In the *Access Request Details* dialog, click *Approve* or *Deny* under *Decision*.
+
[NOTE]
====
Denying an access request requires you to complete the *Justification* field. In this case, Site Reliability Engineering (SRE) cannot directly act on the resources related to the incident. Customers can still use the *Customer Support* to help investigate and resolve any issues.
====

. Click *Save*.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Cluster roles
* Adding notification cluster contacts
* Red Hat Customer Support
