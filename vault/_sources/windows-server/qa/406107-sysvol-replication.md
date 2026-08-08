---
title: "SYSVOL Replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/406107/sysvol-replication
question_id: 406107
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL Replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/406107/sysvol-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The whole purpose of the SYSVOL folder is that is is replicated to all domain controllers throughout the domain. This looks like another replication that has to be set up using DFSR.  When there are Windows Server 2019 servers what kinds of replication have to be set up?     

https://learn.microsoft.com/en-us/answers/questions/406107/edit.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-24*

What I am finding is that DFR will create a Domain System Volume replication group when I create the first replication group. I am not able to delete Domain System Volume replication group.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-24*

FanFan answered the question.   

DSPatrick posted useful information. (Can not select more than one answer).

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-24*

Kind of vague but replication is a part of active directory no matter the version. The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to Accept as answer if the reply is helpful--
