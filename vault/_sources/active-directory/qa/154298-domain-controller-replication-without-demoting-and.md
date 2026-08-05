---
title: "Domain Controller Replication without demoting and promoting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/154298/domain-controller-replication-without-demoting-and
question_id: 154298
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Replication without demoting and promoting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/154298/domain-controller-replication-without-demoting-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I need help regarding an issue with replicating Domain Controller. Since I don't have any backup and I don't have any information about the administrator local user account for the domain controllers once I demoted and the administrator user account does not work I can not promote it back. The other option is I have to create a new domain controller and promote that to take over the primary of our current domain controllers, but I don't want to do that before I try other solutions, and my question that is there any other way to make this work?   

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

 Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-06*

How can I resolve this issue    

Something here may help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8614    

What problem does demoting cause? Demote / promo it again is the simplest solution.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-06*

Hi,  

When you demote a domain controller , there is a step where you will asked to define the password of local admin account. Because a domain controller doesn't have a local account.  we talk about a local administrator account only in workgroup or members machine.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-06*

looking for another option to sync the two DCs  

What problems are you having?  

If you forgot the domain admin password something here might help.  

https://4sysops.com/archives/forgot-the-domain-admin-password/  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-06*

If you demoted the last domain controller in a domain then there's not much you can do aside from restoring from a recent backup.  

--please don't forget to Accept as answer if the reply is helpful--
