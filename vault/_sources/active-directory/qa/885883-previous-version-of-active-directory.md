---
title: "previous version of active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/885883/previous-version-of-active-directory
question_id: 885883
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# previous version of active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/885883/previous-version-of-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello friends    

Me again. Last time I said I need to have way to go back previous version of AD. And I know backup is the only way.    

After many days, I made many research. I understand authoritative restore and non-authoritative restore.    

Most video in youtube teach me do not select "performance an authoritative restore of active directory file.". After restore complete, use below way to restore.    

 ntdsutil -> active instance ntds -> authoritative restore -> restore object or subtree.    

I had try this way restore ou or users, it work, But not enough. I would like to restore schema.     

Some other Q&A said 1. ntdsutil not support resotre whole database, this function had been removed. 2. ntdsutil not support restore schema.     

If this is true, why I don't use AD recycle bin instead of use this dumb way?    

Q1. I try to select " "performance an authoritative restore of active directory file.", and direct reboot after recover backup complete. I suppose whole AD will go back, but in fact nothing happen, nothing restored. What's wrong on my step? how does this option use?    

Q2. is there a way to whole AD go back to previous version?    

Thanks for your time and help

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-14*

-  An authoritative restore will push the designated source sysvol to other domain controllers    

-  Not sure what you're asking, may mean doing a bare metal restore, but this isn't recommended when there are multiple domain controllers unless all is lost.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-12*

The difference between an authoritative or non-authoritative restore is simply the source and or destinations for repair of sysvol (broken replication).    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
