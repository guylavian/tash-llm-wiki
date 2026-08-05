---
title: "Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185340/active-directory
question_id: 2185340
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185340/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi, we had one active directory 2008 that we upgrade and raise to 2016. but since when we had this job. every another active directory that we joind in our network, sysvol and netlogon folder had lost. after I changed the registery key in path: "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" this folder was apeared but does not working well and sometimes the command gpupdate working and reply successful, but ocationally doesnt work and it's reply screenshot was attached.  what should we do?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-01*

Hello mahnaz_116,  

Good day!  

When the problem reoccurs, please check:

1.Please check if the file \domain-name\SysVol\domain-name\Policies{7B64FFF8-08E5-4788-81D4-C31EE85D46B6}\gpt.ini exists on each domain controller.  

2.Can you read the file \domain-name\SysVol\domain-name\Policies{7B64FFF8-08E5-4788-81D4-C31EE85D46B6}\gpt.ini from each domain controller one by one.  

3.Please check the Name Resolution/Network Connectivity to each domain controller one by one.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-01*

hi. I checked this issue and DFSR is being used. and check all the repadmin command, conclude OK! I wanned to know: why happened this problem? I just Raise the old AD and it succeeded. so I check all of this and I have this problem yet...I appreciate if you could help me to solve this problem. 

Thanks in advance...

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

Hello   

Good day！  

3-how to check SYSVOL replication engine is DFSR?  

A: Please check it via HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

Please check if AD replication works fine between all the DCs in the forest. Run commands below on PDC to check, if all the result is OK, then AD replication works fine.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

hi,thank you for your response. 1-we have single forest and domain. 

2-the OS version of main AD that I raised is: windows server 2008 R2 Enterprise raised to windows server 2016 datacenter, the new AD's OS is windows server 2019 Datacenter.

3-how to check SYSVOL replication engine is DFSR?

5- sysvol apear after changed the registery key but dont present the GPO folder in sysvol folder.

and the Error when we use the command: gpupdate is:

""Computer policy could not be updated successfully. The following errors were encountered: 

The processing of Group Policy failed. Windows attempted to read the file \domain-name\SysVol\domain-name\Policies{7B64FFF8-08E5-4788-81D4-C31EE85D46B6}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

a) Name Resolution/Network Connectivity to the current domain controller. 

b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). 

c) The Distributed File System (DFS) client has been disabled. 

User Policy update has completed successfully. 

To diagnose the failure, review the event log or run GPRESULT /H GPReport.html from the command line to access information about Group Policy results.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

Hello mahnaz_116,  

Thank you for posting in Microsoft Community forum. 

1.Is your forest single forest with only one domain? If so, how many Domain Controllers are there in the domain?  

2.What are the operating system version of all the domain controllers in this domain?  

3.Please check if the SYSVOL replication engine is DFSR.

4.Please check if AD replication works fine between all the DCs in the forest.  

5.Now please check if SYSVOL and Netlogon folder are on all the Domain Controllers.

6.Please check if SYSVOL and Netlogon folder are shared on all the Domain Controllers.  

Meanwhile, based on "but ocationally doesnt work and it's reply screenshot was attached.", please provide the screenshot you mentioned.  

I hope the information above is helpful. 

If you have any question or concern, please feel free to let us know. 

Best Regards, 

Daisy Zhou
