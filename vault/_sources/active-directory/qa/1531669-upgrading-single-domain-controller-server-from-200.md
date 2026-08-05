---
title: "Upgrading single Domain Controller server from 2008R2 to server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1531669/upgrading-single-domain-controller-server-from-200
question_id: 1531669
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Upgrading single Domain Controller server from 2008R2 to server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1531669/upgrading-single-domain-controller-server-from-200 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a client with a very old active directory environment on Windows Server 2008 R2. We are going to replace it with a new server and would like to upgrade the existing server to keep all of the permissions and profiles in place. We realize we will need to do it in a couple steps. We created a Hyper-V server to test the upgrade. During the initial attempt to upgrade to 2012 R2 we received an error indicating Forestprep and Domainprep need to be run. The Forestprep completed successfully but Domainprep had issues with replication. Long ago there was another server but it was decommissioned before we got the client so we don't have access to it. I was able to manually remove the old server in sites and services to effectively disable replication. Now I am getting a permissions error creating CN=TPM Devices,DC=CVV,DC=local in Active Directory Domain Services. See log excerpt below:
We have a client with a very old active directory environment on Windows Server 2008 R2. We are going to replace it with a new server and would like to upgrade the existing server to keep all of the permissions and profiles in place. We realize we will need to do it in a couple steps. We created a Hyper-V server to test the upgrade. During the initial attempt to upgrade to 2012 R2 we received an error indicating Forestprep and Domainprep need to be run. The Forestprep completed successfully but Domainprep had issues with replication. Long ago there was another server but it was decommissioned before we got the client so we don't have access to it. I was able to manually remove the old server in sites and services to effectively disable replication. Now I am getting a permissions error creating CN=TPM Devices,DC=CVV,DC=local in Active Directory Domain Services. See log excerpt below:

```
[Status/Consequence]  The operation has not run or is not currently running. It will be run next. [2024/02/13:16:51:53.609] Adprep was about to call the following LDAP API. ldap_add_s(). The entry to add is CN=TPM Devices,DC=CVV,DC=local. [2024/02/13:16:51:53.610] LDAP API ldap_add_s() finished, return code is 0x10  [2024/02/13:16:51:53.617] Adprep was unable to create the object CN=TPM Devices,DC=CVV,DC=local in Active Directory Domain Services.  [Status/Consequence]  This Adprep operation failed.  [User Action]  Check the log file ADPrep.log in the C:\Windows\debug\adprep\logs\20240213165153 directory for more information. Restart Adprep. [2024/02/13:16:51:53.621] Adprep encountered an LDAP error.   Error code: 0x10. Server extended error code: 0x57, Server error message: 00000057: LdapErr: DSID-0C090CB7, comment: Error in attribute conversion operation, data 0, v1db1   DSID Info: DSID: 0x1811100d ldap error = 0x10 NT BUILD: 9600 NT BUILD: 16384  [2024/02/13:16:51:53.628] Adprep was unable to update domain information.   [Status/Consequence]  Adprep requires access to existing domain-wide information from the infrastructure master in order to complete this operation.  [User Action]  Check the log file, ADPrep.log, in the C:\Windows\debug\adprep\logs\20240213165153 directory for more information.   D:\support\adprep>netdom query fsmo Schema master               Culinary01.CVV.local Domain naming master        Culinary01.CVV.local PDC                         Culinary01.CVV.local RID pool manager            Culinary01.CVV.local Infrastructure master       Culinary01.CVV.local The command completed successfully.
```

I ran adprep /domainprep using an elevated command prompt logged in with an admin account belonging to Domain Admins and Enterprise Admins. Anyone have an idea how to fix this error?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-14*

Hi @Scomage Support  

Before launch the promotion of the first domain controller under Windows 2019 you should check:

-  Replication health :   

repadmin /showrepl   

repadmin /replsummary

-  Domain controller health by checkin event viewer and dcdiag command

-  The domain and forest functional level must be Windows 2008 R2

-  The system replication for sysvol folder must be DFSR

Try to launch the domain adprep /domainprep on the domain controller with all FSMO roles.

Please don't forget to accept helpful answer
