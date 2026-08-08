---
title: "Exchange 2016 (Room mailboxes stopped opening in ECP)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251314/exchange-2016-room-mailboxes-stopped-opening-in-ec
question_id: 251314
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 (Room mailboxes stopped opening in ECP)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251314/exchange-2016-room-mailboxes-stopped-opening-in-ec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When launching the Exchange 2016 ECP (on the server or remotely), when we browse User mailboxes and double click them they open normally (although the mailbox delegation link on the left takes a long time).  However, when we go to the Resource mailboxes and try to double click any of those, we see the window pop up, but it eventually times out with the error  

500  

Unexpected Error :(  

An error occurred and your request couldn't be  

completed. Please try again.  

Any suggestions on what might can cause such a strange occurrence?  

Note:  One thing I have noticed is that the pop up box that states waiting for a response to the room mailbox information depicts the red URL status bar as red with the certificate error.  When I review the certificate details it is definitely a valid certificate, but the address points to https://localhost/ecp/UserGroups/EditRoomMailboxes.aspx which is expected since localhost is not listed in the SAN list of the cert.  Diving into this side of things also as this seems new (might be unrelated).  

Might have found something using what others have:  

Get-ADPermission -Identity "room_mailbox" | sort user | ft user,rights  

That command does list a SID as the user for several AccessRights.  Before removing it as others have tried, is there a quick way to see what account that is associated with?  I see references to BUILTIN\Administrators user and that seems like it would be required/needed  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi,     

Which CU of Exchange 2016 are you using? Update to latest CU might solve the issue: https://www.microsoft.com/en-us/download/details.aspx?id=102532    

Can you find any related errors with "MSExchange Control Panel" in source in Event log? We need more information for better troubleshooting.    

When searching in old threads(Ex2013), there are two solutions for similar issue:    

 1 . Remove permission for "SID S-1-5-32-548", you can find what SID means here: Well-Known SID Structures    

 For a normal room mailbox, permissions look like this:    

    

 2 . Run "Set-calendarprocessing conferenceroom -BookInPolicy $null -RequestInPolicy $null – RequestOutOfPolicy $null" to clear all policies, which might include a corrupted entry: https://social.technet.microsoft.com/wiki/contents/articles/36535.exchange-server-2013-troubleshooting-unable-to-access-resource-mailbox-using-ecp-encounter-500-unexpected-error.aspx    

I'm not sure if these steps would work as they all found in Exchange 2013 threads, take a backup before try them.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
