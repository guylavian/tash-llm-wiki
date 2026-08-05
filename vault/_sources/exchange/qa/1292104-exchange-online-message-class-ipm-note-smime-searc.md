---
title: "Exchange Online Message Class \"IPM.Note.SMIME\" Search"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1292104/exchange-online-message-class-ipm-note-smime-searc
question_id: 1292104
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Online Message Class "IPM.Note.SMIME" Search

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1292104/exchange-online-message-class-ipm-note-smime-searc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I need to search SMIME signed/encrypted Mails in every Exchange Online Mailbox. I tried Search-Mailbox cmds, but they dont want to use "ItemClass:IPM.Note.SMIME" or "-MessageClass IPM.Note.SMIME". eDiscovery Standard Search didn't work either. 

In Outlook i can search SMIME mails within the advanced search. But I need to find a solution to trigger this search across all EXO mailboxes. 

What Syntax will allow a search about MessageClass IPM.Note.SMIME?

My final goal is to search and move SMIME Mails to a specife Outlook folder. 

Hope someone knows stuff about that kind of mailbox search. 

Thanks,

Julian

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-29*

Hi @Julian Blechschmidt  ，

To the best of my knowledge, I am afraid this is currently not feasible. 

As regards to "Search-Mailbox", "-MessageClass" is not a valid parameter according to this article. Reviewing the linked article of the "-SearchQuery" parameter, we can learn that there's no searchable property for message class "IPM.Note.SMIME". The same conclusion applies to eDiscovery as well. eDiscovery does have a searchable property "ItemClass", but it's used to search for specific third-party data types and IPM.Note.SMIME is not a valid value of it, see this article.  

Given this, I've just tried reposting this into the official feedback portal for Exchange Online. The link will be left below in case you or other community members would like to vote or comment there. Hopefully this can come true in the future.

https://feedbackportal.microsoft.com/feedback/idea/185930b5-e6fd-ed11-a81c-000d3ae5b6f4  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
