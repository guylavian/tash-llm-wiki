---
title: "Managing your {product-title} in AWS GovCloud account"
type: reference
domain: openshift
slug: rosa-govcloud-4-22-rosa-govcloud-account-management
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_govcloud/rosa-govcloud-account-management
version: 4.22
family: rosa_govcloud
documentKind: "Documentation"
---

# Managing your {product-title} in AWS GovCloud account

[id="rosa-govcloud-account-management"]
= Managing your OpenShift Container Platform in AWS GovCloud account

[role="_abstract"]
When you have access to the FedRAMP accounts, you can manage the credentials according to your needs.

// Module included in the following assemblies:
// * rosa_govcloud/rosa-govcloud-account-management.adoc

[id="rosa-govcloud-manage_{context}"]
= Changing your Red Hat FedRAMP account password

[role="_abstract"]
To change your FedRAMP account password, you must have access to your Red{nbsp}Hat FedRAMP account.

.Procedure

. Navigate to the Red Hat FedRAMP account management page.
. Sign in with your current username and password.
. Under the middle box called _Account Security_, click *Signing In*.
. Under _Basic authentication_, select *Password*.
. Click *Update* and choose a password that meets the following requirements:
+
* Minimum of fifteen (15) characters
* At least one (1) upper-case letter
* At least one (1) lower-case letter
* At least one (1) number
* At least one (1) special character (e.g. ~ ! @ # $ % ^ & * ( ) _ + = - ' [ ] / ? > <)
. Confirm your password.
. Click *Submit*.

// Module included in the following assemblies:
// * rosa_govcloud/rosa-govcloud-account-management.adoc

[id="rosa-govcloud-support-ticket_{context}"]
= Opening a support ticket

[role="_abstract"]
To get access to open a support ticket, complete the following steps.

.Procedure

. If you need to create an account, contact fedramp-css@openshiftusgov.com.
. After you receive access, navigate to the Red Hat GovCloud support portal.
. Click *Create Case* and complete the required information.
. Click *Submit*.

//following module not used anymore as no VPN required
//include::modules/rosa-govcloud-manage-vpn.adoc[leveloffset=+1]
