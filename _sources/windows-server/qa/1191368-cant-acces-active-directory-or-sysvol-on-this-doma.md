---
title: "Can't acces Active Directory or Sysvol on this Domain Controller Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191368/cant-acces-active-directory-or-sysvol-on-this-doma
question_id: 1191368
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Can't acces Active Directory or Sysvol on this Domain Controller Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191368/cant-acces-active-directory-or-sysvol-on-this-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi to everyone. I recently added a new domain controller to our domain with windows server 2022. The other server have server 2016. Now i am watching Active directory issues with this message "Can't acces Active Directory or Sysvol on this Domain Controller....." i am unable to see/access NETLOGON and SYSVOL shared folders. Does anybody know about this and how to solve it?. Thanks to all of you.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-20*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR

Beyond that you can follow along here.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
