---
title: "Domain Controller Promotion - Install From Media - IFM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/740459/domain-controller-promotion-install-from-media-ifm
question_id: 740459
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Domain Controller Promotion - Install From Media - IFM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/740459/domain-controller-promotion-install-from-media-ifm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need to promote a few domain controllers and am looking to use "Install From Media" option. Cut back on the time to replicate over the network. being that I have to be cautious about the DIT being out there unsecured looking to see if there is a way to store the DIT locally while maintaining control of access  to only the engineer promoting and the server consuming. I am thinking copying over the DIT to the server using NTDSUTIL.... not sure if there is way to encrypt in transit using NTDSUTIL... removing default permissions... (Local Admins should not have access) add the engineer and server to the ACL for the DIT. in the end run the promotion in a unattended state. Could this be done on a network share... that would help for not having copies on all the servers.  

any thoughts and feedback would be appreciated  

thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-03*

It is entirely possible to send your .dit to a network share using ntdsutil encrypted (ifm: create full \\servername\sharename). As long as you are running at least SMB 3.0 (Windows server 2012 and later) you can enable SMB encryption on the wire. (https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security )

Modify the ACL on the network share so that only the personnel that you desire would have access to the DIT  You could then use a PowerShell script that prompts for credentials (Get-Credential) to run the IFM unattended.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-23*

Hello @Luis Gonzales       

Yes, this is not recommended since the DCs are quite important and you want to make sure that everything is under control and goes smooth.     

About your question of the DIT database, NTDS is unique for each Domain Controller, and besides it can be replicated it is never a good option to "transport" the NTDS database.    

The best cut of time would be:    

-  Unatended deployment of Windows Server using MDT or WDS    

-  DCPROMO the server to DC using an unanttended file: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/syntax-build-answer-files-unattended-installation-ad-ds    

-  replicate NTDS using the command: repadmin /replicate <DC1Name> <DC2Name> <NamingContextDN>    

Hope this helps with your query,    

--    

--If the reply is helpful,please Upvote and Accept as answer--
