---
title: "Attachment size issue Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/188695/attachment-size-issue-exchange-2013
question_id: 188695
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Attachment size issue Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/188695/attachment-size-issue-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are not able to send attachment of 10 MB from mobile only in exchange 2013 environment and we are able to send email from OWA and outlook with attachment of 25 MB.  

Please assist us how to resolve it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-08*

@Mohammed Nadeem    

Hi,

Just in addition to Andy's answer,here are some detailed steps on how to do it:  

1.Locate %ExchangeInstallPath%FrontEnd\HttpProxy\Sync\web.config and %ExchangeInstallPath%ClientAccess\Sync\web.config  

Find the maxRequestLength in both web.config files and change the value to a larger one which you'd like to apply to the ActiveSync limit.  

By default it is 10240 KB(10 MB).  

  

2.Locate %ExchangeInstallPath%ClientAccess\Sync\web.config  

Find the MaxDocumentDataSize and also change its value.  

By default it is 10240000 bytes(10 MB).  

3.Restart IIS and see if the changes have taken effect.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
