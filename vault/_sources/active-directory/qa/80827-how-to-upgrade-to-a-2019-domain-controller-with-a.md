---
title: "How to upgrade to a 2019 domain controller with a current 2008 primary controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/80827/how-to-upgrade-to-a-2019-domain-controller-with-a
question_id: 80827
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How to upgrade to a 2019 domain controller with a current 2008 primary controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/80827/how-to-upgrade-to-a-2019-domain-controller-with-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we currently have a 2008 R2 domain controller and a 2012 R2 secondary domain controller. I would like to add a 2019 domain controller and eventually demote the 2008 R2 DC. I understand that the 2019 server schema needs to be upgraded. Is there a set of steps in achieving this? The 2008 R2 DC has DHCP on it as well. I have raised the domain level from Server 2003 to 2008 and when using Get-ADForest command the Forest Mode still shows as Windows2003Forest. This was raised to 2008 yesterday afternoon. Is it still propagating? Best regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-01*

Hello，    

Thank you for update your issue.    

As I mentioned in the reply last day, the minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 forest functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.    

Please check whether the forest function level is 2003 in ADDT (Active Directory Domains and Trusts)    

    

Click Raise Forest Functional Level to pop up the interface in the figure below to check whether the current forest functional level is 2008. According to your description, ensure that the domain functional level is 2008. If the forest functional level is still 2003 in the red box, please click Select 2008 in the drop-down menu and Apply. After the operation is completed, please log in to the interface again to check whether the forest function level has been upgraded to 2008.    

    

Please check if there is any problem with SYSVOL replication. The following is an experiment I did. There are two DCs in the domain. I created a new folder named "Sysvol" in the path of DC1 as shown in the figure below (Figure 1 and Figure 2) ), after the new creation is successful, check that the newly created folder has been successfully replicated in the same path in DC2. You can follow these steps to check whether there is a problem with the replication between DCs, which will affect whether you can successfully be in the domain Add new DC.    

    

    

    

If the above two steps are successful, the forest function level is upgraded to 2008, and there is no problem with SYSVOL replication. You can refer to my previous reply to add 2019DC.    

Hope the information above is helpful. If anything is unclear, please feel free to let us know.    

Best regards,     

Stephanie Yu

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-01*

Thank you Stephanie for your response. I have completed all steps for questions 1. Confimred that Functioanl level is 2008 but Get-ADForest still shows Windows2003. All steps completed successfully except DCDIAG /V command which displayed errors for N abd SystemLog as shown below. I have not continued to Question 2 steps.

Starting test: NCSecDesc  

* Security Permissions check for all NC's on DC GCHC-DC1.  

The forest is not ready for RODC. Will skip checking ERODC ACEs.  

* Security Permissions Check for  

DC=DomainDnsZones,DC=gchc,DC=local  

(NDNC,Version 3)  

Error NT AUTHORITY\ENTERPRISE DOMAIN CONTROLLERS doesn't have  

Replicating Directory Changes In Filtered Set  

access rights for the naming context:  

DC=DomainDnsZones,DC=gchc,DC=local  

* Security Permissions Check for  

DC=ForestDnsZones,DC=gchc,DC=local  

(NDNC,Version 3)  

Error NT AUTHORITY\ENTERPRISE DOMAIN CONTROLLERS doesn't have  

Replicating Directory Changes In Filtered Set  

access rights for the naming context:  

DC=ForestDnsZones,DC=gchc,DC=local  

* Security Permissions Check for  

CN=Schema,CN=Configuration,DC=gchc,DC=local  

(Schema,Version 3)  

* Security Permissions Check for  

CN=Configuration,DC=gchc,DC=local  

(Configuration,Version 3)  

* Security Permissions Check for  

DC=gchc,DC=local  

(Domain,Version 3)  

......................... GCHC-DC1 failed test NCSecDesc

```
Starting test: SystemLog
     * The System Event log test
     An Error Event occurred.  EventID: 0x0000165B
        Time Generated: 08/31/2020   18:33:48
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x000016AD
        Time Generated: 08/31/2020   18:38:48
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0xC000000D
        Time Generated: 08/31/2020   18:54:12
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:18
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:19
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:20
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:23
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:23
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:24
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:25
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:26
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     An Error Event occurred.  EventID: 0x00000457
        Time Generated: 08/31/2020   18:58:27
        EvtFormatMessage failed, error 15100 Win32 Error 15100.
        (Event String (event log = System) could not be retrieved, error
        0x3afc)
     ......................... GCHC-DC1 failed test SystemLog
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-31*

Hello DSPatrick. These are the links. Thanks  

https://1drv.ms/u/s!Av1PEgpeCgHJiX75pGUsrI20nRDh?e=TRff1K  

https://1drv.ms/u/s!Av1PEgpeCgHJiX_lT9vQAjLZeFe7?e=3jOXeT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-30*

Hello, I have complete the Quick Migration as from the link you provided successfully. I run a Get-ADForest and it still shows as Windows2003Forest as Forest Mode.
