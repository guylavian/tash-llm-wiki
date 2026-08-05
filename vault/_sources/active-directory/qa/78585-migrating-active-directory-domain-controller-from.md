---
title: "Migrating Active Directory Domain Controller from Windows 2016 to Windows 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/78585/migrating-active-directory-domain-controller-from
question_id: 78585
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrating Active Directory Domain Controller from Windows 2016 to Windows 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/78585/migrating-active-directory-domain-controller-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there,  

We had Windows Server 2012 R2 domain controller with DNS and Active Directory Certificate Services in the past, and we migrated to Windows Server 2016. And, now we have planned to migrate the Windows Server 2016 domain controller to Windows Server 2019.  

I would like to know whether it is the same process to 1) Setup a new Windows Server 2019 server as additional domain controller, and 2) transfer the FSMO roles, 3) demote the Windows Server 2016 and 4) replace the IP address on the Windows Server 2019 from the demoted server?  

Please advise.  

Thank you, Anand

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-27*

Basically yes but check the prerequisites have been met.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

and before any changes are made; use dcdiag / repadmin tools to verify health correcting all errors found before starting any operations  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-27*

Hello @Anand Franklin  ,    

Thank you for posting here.    

According to the description above, we have only one DC (PDC) and we installed the AD CS role on this PDC, if I misunstood you, please correct me.    

I would like to know whether it is the same process, I think the main process is OK.    

1)Setup a new Windows Server 2019 server as additional domain controller (add AD DS and DNS role, also make this DC as GC);    

2)Check new DC is working fine and AD replication is complete. Transfer the FSMO roles    

3)Migrate AD CS from 2016 to 2019 DC;    

4)Demote the Windows Server 2016;    

5)Replace the IP address on the Windows Server 2016 using a idle IP address;    

6)Replace the IP address on the Windows Server 2019 from the demoted server;    

Before migrating AD domain controller, we had better check:    

-  Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on each DC.    

-  Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on each DC.    

-  Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.    

-  Check we can update gpupdate /force on each DC successfully.    

-  Check CA health by opening PKIview.msc to ensure all Status is OK.    

Meanwhile, we recommend the following points:    

-  We had better have at least two DCs in one domain.    

-  We suggest we install /migrate AD CS on one member server.    

-  If we have other roles on the old domain controllers, we should also migrate these roles as needed.    

-  Make the changes during downtime.    

-  Usually, we want a DC to be just a DC, there is nothing else, because this reduces possible resource conflicts and exploit vulnerabilities and minimizes patching of other applications that might cause downtime.    

Ideally, a DC should be easy to replace, just by standing up another DC.    

When we put other software and roles on one DC, maybe the DC is harder to replace it.    

For example,    

If we have a DC with AD CS(it is also a CA server), if there is some issues with this DC and we want to demote this DC, we need to remove/migrate AD CS first and then demote this DC.    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou
