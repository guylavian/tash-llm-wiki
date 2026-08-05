---
title: "Active directory 2019 - ADC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/89165/active-directory-2019-adc
question_id: 89165
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Active directory 2019 - ADC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/89165/active-directory-2019-adc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

currently i'm having windows 2012 domain controller and when promoting the additional domain controller in windows 2019.  

In the DCPROMO logs i'm getting error message   

 Error - Active Directory Domain Services could not replicate the directory partition CN=Schema,CN=Configuration,DC= ??,DC=com from the remote Active Directory Domain Controller . (123)  

EVENTLOG (Error): NTDS General / Internal Processing : 1168  

Internal error: An Active Directory Domain Services error has occurred.  

DCdiag Error:  

Active Directory LDAP Services Check  

         The host b47fe834-4a2e-4464-a79e-042359eb3e79._msdcs.???.com

```
could not be resolved to an IP address. Check the DNS server, DHCP,

     server name, etc.

     Got error while checking LDAP and RPC connectivity. Please check your

     firewall settings.

     ......................... ?? failed test Connectivity
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-09*

Hello @bala198222  ,

Thank you for posting here.

Here are the answers for our questions:

-   Before we add 2019 DC into existing domain, we should ensure: The minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.

-   Before we do any change in existing AD domain environment, we had better do:  

-  Check if AD environment is healthy. Check all DCs in this domain is working fine by running Dcdiag /v. Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.  

-  back up all domain controllers.

-   Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.

-   Check we can update gpupdate /force on each DC successfully.

After we ensure forest function level is 2008 and SYSVOL replication is DFSR replication type, we can add one Windows server 2019 to the existing domain and promote is as a domain controller.

-   Join a new Windows server 2019 to existing domain  

    

-   Install AD DS role and DNS role on this Windows server 2019 and promote this server as a DC (as a GC).

-   Check if AD environment is healthy again. Check all DCs in this domain is working fine by running Dcdiag /v. Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.

References:  

Forest and Domain Functional Levels  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels

Migrating FRS to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405

Hope the information above is helpful. And look forward to your update of this issue. If anything is unclear, please feel free to let us know.

Best Regards,  

Stephanie Yu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-08*

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`(etc. as other DC's exist)`  

then put unzipped text files up on OneDrive and share a link.  

Dcdiag /skip:systemlog /v /c /d /e /s:%computername% >c:\dcdiag.log
