---
title: "ADFS 2016 - requirements - does it work with 2003 domain and forest functional levels?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106515/adfs-2016-requirements-does-it-work-with-2003-doma
question_id: 106515
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_affiliations: ["Mvp"]
---
# ADFS 2016 - requirements - does it work with 2003 domain and forest functional levels?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106515/adfs-2016-requirements-does-it-work-with-2003-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

 We're looking to upgrade our ADFS from 2012 to 2016.     

Currently we have 2012 DCs running at 2003 domain and forest functionality level. Can ADFS 2016 work with 2012 DCs running at 2003 domain and forest functionality levels?    

Looking at below, it requires a 2016 schema, but I'm not sure what version of DC and functional level that requires.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-requirements    

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-24*

A 2003 domain functional level is sufficient to add the first 2016 domain controller.  

--please don't forget to Accept as answer if the reply is helpful--
