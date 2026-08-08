---
title: "Removing AD DS role from server with (AD CS and DHCP Role)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/131974/removing-ad-ds-role-from-server-with-ad-cs-and-dhc
question_id: 131974
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Removing AD DS role from server with (AD CS and DHCP Role)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/131974/removing-ad-ds-role-from-server-with-ad-cs-and-dhc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I got a question.  

I have a domain controller server that has -> AD DS, AD CS, DHCP roles. I installed a new DC in this domain.  

I need to remove AD DS role from old server that has AD CS and DHCP roles.  

My plan:  

-  On old DC:  

Backup AD CS - then remove AD CS role  

Remove AD DS role  

Restart server - add AD CS role and return it from backup.  

Is this will work?  

And what about DHCP? - could i remove AD DS without removing DHCP?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Don't forget to transfer FSMO roles from the old DC to the new one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

P.S. You should have at least two DC's in production, as per best practice recommendations. Not only will this make your AD more resilient in case one DC goes down, you can configure DHCP Failover on them, making the DHCP service highly available.     

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831385(v=ws.11)
