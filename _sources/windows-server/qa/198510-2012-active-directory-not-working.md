---
title: "2012 Active Directory not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/198510/2012-active-directory-not-working
question_id: 198510
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# 2012 Active Directory not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/198510/2012-active-directory-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This server is the owner of the following FSMO role, but does not consider it valid. For the partition which contains the FSMO, this server has not replicated successfully with any of its partners since this server has been restarted. Replication errors are preventing validation of this role.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Hi,  

Thank you for posting in our forum  

There is two way to move FSMO role to another server first is transfer the FSMO role to another server, transfer normally happens when server is going for maintenance like disk crash, driver update, patches updates etc, so you don't want your FSMO role donw you temporary transfer the FSMO roles.  

Another way is to seize the FSMO role on another server, its same like king is dead & assigning his heir to hold the throne further by making him the King, seizing works in same way, if the server holding FSMO role is dead & it can't be revert back, you have to seize the FSMO role on another DC, once you seize the dc you can't bring the crash server back to network even it can be as you have seize the role, the new dc will be treated as authoritative server, so never put back the DC from which you seize the FSMO role.  If you want to reuse the server & DC name or server, perform the metadata cleanup for AD, removed all the left out records from AD DNS manually, allow time for replication to another DC's & once you verify changes are replicated & there is no more traces using repadmin tool, you can format the new server, install the fresh OS & configure as DC & transfer the roles if you wish.  

So Seizing happens in disaster recover scenario where you can't transfer the FSMO role , in your case it looks same to me you can seize the FSMO role on healthy dc but make sure w/o performing metadata steps don't connect the dc even if it can be connected.  

So, if you think you don't wanna bring old dc back seize the FSMO role & also check there is no replication error in your current domain.  

Hope this information can help you  

Best wishes  

Vicky
