---
title: "Windows 11 22h2 Problem with Active directory after update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1048276/windows-11-22h2-problem-with-active-directory-afte
question_id: 1048276
fetched: 2026-07-25
answer_count: 19
has_accepted_answer: false
upvotes: 6
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Windows 11 22h2 Problem with Active directory after update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1048276/windows-11-22h2-problem-with-active-directory-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

After updating or installing a fresh Windows 11 22H2, the computer can't contact the active directory.  

GPO seems to be not applied and it's impossible to reach any ressources on the network.

It seems that the user can't get a TGT from the domain controller.

When I do a `klist` it's empty.

With wireshark, I see at each attempt an "AS-REQ" but no "AS-REP".

> nltest /dclist:mydomain.local

`Get list of DCs in domain 'mydomain.local' from '\\dc01.mydomain.local'.`  

`Cannot DsBind to mydc.laz (\\dc01.mydomain.local).Status = 2148074320 0x80090350 SEC_E_DOWNGRADE_DETECTED.`

> nltest /sc_query:mydomain.local

`Flags: 30 HAS_IP HAS_TIMESERV Authentication Service: Netlogon`  

`Trusted DC Name \\dc02.mydomain.local`  

`Trusted DC Connection Status Status = 0 0x0 NERR_Success`  

`The command completed successfully`

When I try to reach an SMB share i have this message :

`The sytem cannot contact a domain controller to service the authentication request. Please try again later`

All the DCs are in Windows 2016.

I'm not sure where to look to fix this. I've looked everywhere but no answer.  

Can you help me please?

Thank you.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-15*

This is pretty ridiculous. I've been having this issue since updating with 22H2. The only way I can access my account is by disconnecting my internet every time and logging in with saved cached passwords. How does Microsoft release a major update that majorly ruins a lot of peoples systems?    

I've tried accessing our AD and changing my password, but that has not solved anything other than a notification that says I need to lock and unlock to give windows my new password - but of course this doesn't work and I have to keep disconnecting my internet, logging in, then reconnecting.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-11-15*

I faced the same problem, do not have crowdstrike !!  I'm using simple NAS Synology Directory Server (Samba), just to control access on a file server, no group policy management, I faced this with two windows devices, was running well till the 22H2 update, I have tried removing the device from the domain, deleting it from the active directory computers, tried with same user, different users, it seems the device and DC are talking different languages now.     

hope someone come up with solution or workaround

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-09*

As I've been facing this myself and spent the day on it and there doesn't seem to be much information around.    

Would any of you be facing issue soely on sites with RODC, as adding the machine to the password replication policy of the RODC 'might' have resolved for me.  Too early to confirm, but i appear to have one working this way.  We've 3 sites and only facing it on the one, this the only one with the RODC as a factor.    

I'm also only so far facing it on machines on Win 11 22H2

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-10-14*

Hi,    

Do you have any local firewall or any AV that might be blocking the connections, please check the firewall policies and connectivity and also VPN software?    

Hope this helps.    

JS    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
