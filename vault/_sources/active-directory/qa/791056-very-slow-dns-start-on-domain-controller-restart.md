---
title: "Very Slow DNS start on domain controller restart"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/791056/very-slow-dns-start-on-domain-controller-restart
question_id: 791056
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Very Slow DNS start on domain controller restart

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/791056/very-slow-dns-start-on-domain-controller-restart (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Every time I restart my domain controller, it first hangs at the following screen:    

    

After 2-4 minutes, it will finally load into the desktop. But if I click on "DNS" application, it will say the following:    

    

If I try to open group policy editor, it will not load until DNS loads.    

DNS will finally load after about another 5 minutes.    

In event viewer, under "DNS Server" I see this warning:    

    

I haven't had a clue why this issue is occurs yet.    

Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2022-03-29*

Hi,  

It's normal behavior when the first replication is not yet completed because the DNS zone is integrated DNS zone  therefore it's saved in active directory.  

So to load DNS zone and connect to another service depending on DNS service you have to wait to complete the first AD replication.  

Please don't forget to mark helpful reply as answer
