---
title: "Segregate DNS from Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163042/segregate-dns-from-active-directory
question_id: 1163042
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Segregate DNS from Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163042/segregate-dns-from-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,  

I hope all of you are doing great,  

There are 4 domain controllers at the same time they are DNS servers 

I would like to know how to Segregate the DNS from the domain controller to make it a separate server to prevent the active directory from the internet.

I would like to avoid any issues with the DNS records or a

I really appreciate any help you can provide.  

Thanks in advance

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-22*

Hi @Husam Eldin Elbagir Mohamed  

You can create  secondary DNS zone on windows server or on another appliance. The secondary zone is a read-only copy of the primary zone that is stored on a your domain controllers. 

The secondary zone cannot process DNS records updates and can only retrieve updates from the primary zone.

Another feature may help you .It's to create  conditional forwarders to forward any DNS request of your internal DNS zone to one of your domain controllers.

DNS forwarder

Please o't forget to mark helpful answer as accepted

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-23*

I can't thank you enough for response I will try to follow your advice if there is anything I will get back to you
