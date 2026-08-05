---
title: "GPO Error on client pc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194420/gpo-error-on-client-pc
question_id: 2194420
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# GPO Error on client pc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194420/gpo-error-on-client-pc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello in here. 

I have a problem with GPO´s on our server, and i just cant figure out why this problem occurs. So i hope that you guys can help me :) 

We are running a 2019 server. And im setting up a GPO that deploys printers to our users. Im testing if the GPO does what is intended. 

The GPO is very simple, it is setup as user configuration > Preferences > Control panel settings > Printers.  

I just add the shared printer path and in the "common" tab i checked "run in logged-on user...." and the item level target is set to a specified user and thats it. When i update the gpo on the server there is no problem, but when i update the gpo on the client machine, in this case my own pc, then cmd gives me the error as shown below: 

"The processing of Group Policy failed. Windows attempted to read the file \COMPANYNAME.local\SysVol\COMPANYNAME.local\Policies{903D47C3-8D0E-4C5B-9E46-5AC32793574F}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

a) Name Resolution/Network Connectivity to the current domain controller. 

b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). 

c) The Distributed File System (DFS) client has been disabled. 

To diagnose the failure, review the event log or run GPRESULT /H GPReport.html from the command line to access information about Group Policy results." 

I really dont know why this is, when i delete the gpo it doesnt give me this error. It even comes if i create another gpo with different settings too. I have also edit the user version and computer version, so they are 100% same on the replicant server. Hope you can help me solve this.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-25*

Hello  

Good day!  

The only error i could find is that the C:\Windows\SYSVOL\SYSVOL\Policies path to the GPI.ini file had different version number than the other DC.  

A: This is the problem. It is also SYSVOL replication problem.  

Is your SYSVOL replication DFSR replication engine?  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

If SYSVOL replication is DFSR replication engine, how many Domain Controllers in your domain?   

You can back up all the Domain Controllers one by one (back up system status or full server if you have no recent backups). Then please back up all the SYSVOL folder one by one.  

Please perform the steps in the part of "How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)" in the link below.  

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-24*

The error is only for 2 GPO´s the rest of the gpo´s is running fine, theese 2 gpo´s has also been running without issues before. 

I have been googleing the whole day now, and i just dont find the problem. A bit confused about this problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-24*

Hello   

Good day!  

it seems there is SYSVOL replication problem, please check it.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-24*

Thank you for the feedback.

However none of this did work.

The only error i could find is that the C:\Windows\SYSVOL\SYSVOL\Policies path to the GPI.ini file had different version number than the other DC. After i changed this, the problem still is the same.

But the problem is not on all client pc´s, some of the client pc´s dont get this error, i cant figure out why this is.

the 3 repadmin commands didnt show any errors as well.

I can find articles that say you can make some changes in the GPO, and then delete it again, to force another version number and sync between the DC, but this has no affect as well.

I hope some of you have a solution.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Hello Peter Wang Jensen,  

Thank you for posting in Microsoft Community forum.

Please check information below:  

1.Please check if the corresponding GPO name of GUID {903D47C3-8D0E-4C5B-9E46-5AC32793574F} is shared printer GPO.  

2.Please check if you log on server and this client using the same specified user.

3.please check the Network Connectivity between this client and the current domain controller.  

4.Please check if you can ping the DCName.domain.com and IP of the Domain Controller and the Domain.com on this client.  

5.If you have more than one Domain Controller in domain, please check the AD replication between all the domain controllers.  

Run commands below on PDC to check.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

6.If you have more than one Domain Controller in domain, and the AD replication works fine, please check the SYSVOL replication.  

That is to check if all the contents under C:\Windows\SYSVOL\SYSVOL\Policies on all the DCs are the same.  

7.Please check if you can access the file \COMPANYNAME.local\SysVol\COMPANYNAME.local\Policies{903D47C3-8D0E-4C5B-9E46-5AC32793574F}\gpt.ini on this client.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
