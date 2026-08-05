---
title: "DCdiag System logs is getting failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/440699/dcdiag-system-logs-is-getting-failed
question_id: 440699
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# DCdiag System logs is getting failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/440699/dcdiag-system-logs-is-getting-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On DC server I run AD healthchecks >"Dcdiag"  it getting failed only system logs.  

I have cleared logs and rebooted the server still persisting same issue. replication are working fine.  

Able to ping between the DC's.  

replication are working fine.  

Below are the test results.,  

Directory Server Diagnosis  

Performing initial setup:  

Trying to find home server...  

Home Server = Test-DC1  

-  Identified AD Forest.  

Done gathering initial info.  

Doing initial required tests  

Testing server: ACT\Test-DC1  

Starting test: Connectivity  

......................... Test-DC1 passed test Connectivity  

Doing primary tests  

Testing server: ACT\Test-DC1  

Starting test: Advertising  

......................... Test-DC1 passed test Advertising  

Starting test: FrsEvent  

......................... Test-DC1 passed test FrsEvent  

Starting test: DFSREvent  

......................... Test-DC1 passed test DFSREvent  

Starting test: SysVolCheck  

......................... Test-DC1 passed test SysVolCheck  

Starting test: KccEvent  

......................... Test-DC1 passed test KccEvent  

Starting test: KnowsOfRoleHolders  

......................... Test-DC1 passed test KnowsOfRoleHolders  

Starting test: MachineAccount  

......................... Test-DC1 passed test MachineAccount  

Starting test: NCSecDesc  

......................... Test-DC1 passed test NCSecDesc  

Starting test: NetLogons  

......................... Test-DC1 passed test NetLogons  

Starting test: ObjectsReplicated  

......................... Test-DC1 passed test ObjectsReplicated  

Starting test: Replications  

......................... Test-DC1 passed test Replications  

Starting test: RidManager  

......................... Test-DC1 passed test RidManager  

Starting test: Services  

......................... Test-DC1 passed test Services  

Starting test: SystemLog  

An error event occurred. EventID: 0xC0001B63  

Time Generated: 06/17/2021 02:51:56  

Event String:  

A timeout (30000 milliseconds) was reached while waiting for a transaction response from the UmRdpService service.  

An error event occurred. EventID: 0xC0001B63  

Time Generated: 06/17/2021 02:52:26  

Event String:  

A timeout (30000 milliseconds) was reached while waiting for a transaction response from the ScDeviceEnum service.  

An error event occurred. EventID: 0xC0001B58  

Time Generated: 06/17/2021 02:52:26  

Event String:  

The Smart Card Device Enumeration Service service failed to start due to the following error:  

......................... Test-DC1 failed test SystemLog  

Starting test: VerifyReferences  

......................... Test-DC1 passed test VerifyReferences  

Running partition tests on : ForestDnsZones  

Starting test: CheckSDRefDom  

......................... ForestDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... ForestDnsZones passed test  

CrossRefValidation  

Running partition tests on : DomainDnsZones  

Starting test: CheckSDRefDom  

......................... DomainDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... DomainDnsZones passed test  

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

Running partition tests on : gang  

Starting test: CheckSDRefDom  

......................... gang passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... gang passed test CrossRefValidation  

Running enterprise tests on : gang.local  

Starting test: LocatorCheck  

......................... gang.local passed test LocatorCheck  

Starting test: Intersite  

......................... gang.local passed test Intersite  

Can you pls assist me on this.,  

Thanks in advance!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-21*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-18*

Hi,

For the ADDS, it is suggested to monitor for a period if there are any other issues.

I did a research about the error, for your reference:  

http://www.networksteve.com/forum/topic.php/RDS_2012_R2:\_A_timeout\_(30000_milliseconds)\_was_reached_while_wa/?TopicId=66971&Posts=1  

http://www.networksteve.com/forum/topic.php/A_timeout\_(30000_milliseconds)\_was_reached_while_waiting_for_a\_t/?TopicId=87209&Posts=6  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-17*

How many domain controllers? What problems are you having? For system log events you'll always find more details in the event logs `eventvwr.msc`  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
