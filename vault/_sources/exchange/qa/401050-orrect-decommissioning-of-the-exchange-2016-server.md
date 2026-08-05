---
title: "Сorrect decommissioning of the Exchange 2016 server after moving mail to the 365 Сloud"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401050/orrect-decommissioning-of-the-exchange-2016-server
question_id: 401050
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Сorrect decommissioning of the Exchange 2016 server after moving mail to the 365 Сloud

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401050/orrect-decommissioning-of-the-exchange-2016-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All mailboxes have been migrated to Exchange Online.    

Azure AD Connect syncs only passwords (with write-back), hybrid sync and groups sync are not used.    

Distribution groups were not migrated or synchronized, but were created (+new 365 groups) in the cloud instead.    

Now we are going to remove the Exchange server and free up the resources it occupies in the hypervisor for other tasks.    

This will also reduce the attack surface due to recent vulnerabilities.    

There is an official manual:    

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange#why-you-may-not-want-to-decommission-exchange-servers-from-on-premises    

At the same time, there are many other articles in the Internet.    

Some advise to leave the server or only its management console to facilitate account management.    

Others recommend completely removing the server configuration from AD using the ADSIEdit utility, and editing some attributes directly.    

Microsoft has changed a lot lately.    

What are the best practices now?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-27*

Yes, actually you can do that if the Exchange Server is used for just mgmt and nothing else.   

Also ensure its not accessible from the internet and keep it up to date ( Exchange CUs/ Security patches and Windows udpates)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-27*

@KyleXu-MSFT       

Thank you for your answer.    

Yes, I think that Scenario 2 is my case.    

Сan I just turn off on-prem Exchange server to free up the virtualization resources it occupies and turn it on only if necessary?
