---
title: "DCDIAG errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/318867/dcdiag-errors
question_id: 318867
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# DCDIAG errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/318867/dcdiag-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft Windows [Version 6.3.9600]  

(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\administrator.WSCHD>ADSIEDIT.MSC

C:\Users\administrator.WSCHD>dmdiag  

'dmdiag' is not recognized as an internal or external command,  

operable program or batch file.

C:\Users\administrator.WSCHD>dfdiag  

'dfdiag' is not recognized as an internal or external command,  

operable program or batch file.

C:\Users\administrator.WSCHD>dcdiag

Directory Server Diagnosis

Performing initial setup:  

Trying to find home server...  

Home Server = CODC1  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: ------------------\CODC1  

Starting test: Connectivity  

......................... CODC1 passed test Connectivity

Doing primary tests

Testing server: ------------------\CODC1  

Starting test: Advertising  

Warning: DsGetDcName returned information for \CODC2.WSCHD.local,  

when we were trying to reach CODC1.  

SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.  

......................... CODC1 failed test Advertising  

Starting test: FrsEvent  

......................... CODC1 passed test FrsEvent  

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the  

SYSVOL has been shared. Failing SYSVOL replication problems may cause  

Group Policy problems.  

......................... CODC1 failed test DFSREvent  

Starting test: SysVolCheck  

......................... CODC1 passed test SysVolCheck  

Starting test: KccEvent  

......................... CODC1 passed test KccEvent  

Starting test: KnowsOfRoleHolders  

......................... CODC1 passed test KnowsOfRoleHolders  

Starting test: MachineAccount  

......................... CODC1 passed test MachineAccount  

Starting test: NCSecDesc  

......................... CODC1 passed test NCSecDesc  

Starting test: NetLogons  

Unable to connect to the NETLOGON share! (\CODC1\netlogon)  

[CODC1] An net use or LsaPolicy operation failed with error 67,  

The network name cannot be found..  

......................... CODC1 failed test NetLogons  

Starting test: ObjectsReplicated  

......................... CODC1 passed test ObjectsReplicated  

Starting test: Replications  

......................... CODC1 passed test Replications  

Starting test: RidManager  

......................... CODC1 passed test RidManager  

Starting test: Services  

......................... CODC1 passed test Services  

Starting test: SystemLog  

A warning event occurred. EventID: 0x00000087  

Time Generated: 03/16/2021 16:53:22  

Event String:  

NtpClient was unable to set a manual peer to use as a time source be  

cause of duplicate error on '3.us.pool.ntp.org'. The same time source '0.us.pool  

.ntp.org' has been either specified as manual peer in NtpServer or selected as d  

omain peer. NtpClient will try again in 15 minutes and double the reattempt int  

erval thereafter. The error was: The entry already exists. (0x800706E0)  

......................... CODC1 passed test SystemLog  

Starting test: VerifyReferences  

......................... CODC1 passed test VerifyReferences

Running partition tests on : DomainDnsZones  

Starting test: CheckSDRefDom  

......................... DomainDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... DomainDnsZones passed test  

CrossRefValidation

Running partition tests on : ForestDnsZones  

Starting test: CheckSDRefDom  

......................... ForestDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... ForestDnsZones passed test  

CrossRefValidation

Running partition tests on : Schema  

Starting test: CheckSDRefDom  

......................... Schema passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Schema passed test CrossRefValidation

Running partition tests on : Configuration  

Starting test: CheckSDRefDom  

......................... Configuration passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Configuration passed test CrossRefValidation

Running partition tests on : WSCHD  

Starting test: CheckSDRefDom  

......................... WSCHD passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... WSCHD passed test CrossRefValidation

Running enterprise tests on : WSCHD.local  

Starting test: LocatorCheck  

......................... WSCHD.local passed test LocatorCheck  

Starting test: Intersite  

......................... WSCHD.local passed test Intersite

C:\Users\administrator.WSCHD>dcdiag

Directory Server Diagnosis

Performing initial setup:  

Trying to find home server...  

Home Server = CODC1  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: -----------------\CODC1  

Starting test: Connectivity  

......................... CODC1 passed test Connectivity

Doing primary tests

Testing server: -------------\CODC1  

Starting test: Advertising  

Warning: DsGetDcName returned information for \CODC2.WSCHD.local,  

when we were trying to reach CODC1.  

SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.  

......................... CODC1 failed test Advertising  

Starting test: FrsEvent  

......................... CODC1 passed test FrsEvent  

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the  

SYSVOL has been shared. Failing SYSVOL replication problems may cause  

Group Policy problems.  

......................... CODC1 failed test DFSREvent  

Starting test: SysVolCheck  

......................... CODC1 passed test SysVolCheck  

Starting test: KccEvent  

......................... CODC1 passed test KccEvent  

Starting test: KnowsOfRoleHolders  

......................... CODC1 passed test KnowsOfRoleHolders  

Starting test: MachineAccount  

......................... CODC1 passed test MachineAccount  

Starting test: NCSecDesc  

......................... CODC1 passed test NCSecDesc  

Starting test: NetLogons  

Unable to connect to the NETLOGON share! (\CODC1\netlogon)  

[CODC1] An net use or LsaPolicy operation failed with error 67,  

The network name cannot be found..  

......................... CODC1 failed test NetLogons  

Starting test: ObjectsReplicated  

......................... CODC1 passed test ObjectsReplicated  

Starting test: Replications  

......................... CODC1 passed test Replications  

Starting test: RidManager  

......................... CODC1 passed test RidManager  

Starting test: Services  

......................... CODC1 passed test Services  

Starting test: SystemLog  

......................... CODC1 passed test SystemLog  

Starting test: VerifyReferences  

......................... CODC1 passed test VerifyReferences

Running partition tests on : DomainDnsZones  

Starting test: CheckSDRefDom  

......................... DomainDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... DomainDnsZones passed test  

CrossRefValidation

Running partition tests on : ForestDnsZones  

Starting test: CheckSDRefDom  

......................... ForestDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... ForestDnsZones passed test  

CrossRefValidation

Running partition tests on : Schema  

Starting test: CheckSDRefDom  

......................... Schema passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Schema passed test CrossRefValidation

Running partition tests on : Configuration  

Starting test: CheckSDRefDom  

......................... Configuration passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Configuration passed test CrossRefValidation

Running partition tests on : WSCHD  

Starting test: CheckSDRefDom  

......................... WSCHD passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... WSCHD passed test CrossRefValidation

Running enterprise tests on : WSCHD.local  

Starting test: LocatorCheck  

......................... WSCHD.local passed test LocatorCheck  

Starting test: Intersite  

......................... WSCHD.local passed test Intersite

C:\Users\administrator.WSCHD>

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

I have two domain controllers and one is in state 5. The new dc which was just promoted yesterday is in state 4. I did run across the the second article, however i was not able to execute the instructions. Would you be able to provide a little more detail about the second article.   

THE NTDS automatically generated shows the oposite server as the from server on both my dcs.   

CODC1 shows from CODC2  

CODC2 shows from CODC1  

Both commands the following commands return "LDAP error 81 <server down> Win32 Err 58  

REPADMIN /SHOWREPS %UPSTREAMCOMPUTER%  

REPADMIN /SHOWREPS %DOWNSTREAMCOMPUTER%

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-17*

You can follow along here.    

DFSR    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

FRS    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

This is server 2012 r2   

Unable to connect to the NETLOGON share!   

Sysvol hasn't been shared on a newly promoted dc.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-17*

What problem are you trying to solve?
