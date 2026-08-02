---
title: "the active directory schema version (17001) is higher than setups version (15333)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/570345/the-active-directory-schema-version-17001-is-highe
question_id: 570345
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# the active directory schema version (17001) is higher than setups version (15333)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/570345/the-active-directory-schema-version-17001-is-highe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm tryin to install MS exchange 2016 CU20 and my AD is also 2016 but I'm getting this error, somebody please help.     

Note: before this i tried to install exchange 2019 but then quit it because some future compatibility issues.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-29*

I think it is because your AD Schema has been upgraded for 2019 Schema, that's the error seems to be. It also means that your AD is prepared to host Exchange 2019 or lower, so when you are installing Exchange 2016, you really do not need to update schema. I am not exchange expert but there is a way to avoid AD scheme upgrade and install Exchange.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-04*

Hello @Hamza Pasha       

The issue is that you have a 2019 version of the FFL and DFL while preparing the environment for a 2016 level.    

Hope this helps with your query,    

-------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-30*

Hi @Hamza Pasha       

Have look at this article it will tell you what AD and Exchange schema changes have been made you your AD https://nettools.net/schemaversions/    

Gary.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-29*

Hi,    

Agree with @Jai Verma  . Based on schema version value 17001,the last upgrade of schema version has been done with Exchange 2019 setup, if you want upgrade again the schema version with the last  Exchange cumulative update , you have to use Exchange 2019 or higher:    

prepare-ad-and-domains    

Please don't forget to mark helpful reply as answer
