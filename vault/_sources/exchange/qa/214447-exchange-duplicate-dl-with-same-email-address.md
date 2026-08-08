---
title: "Exchange Duplicate DL with same email address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/214447/exchange-duplicate-dl-with-same-email-address
question_id: 214447
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Duplicate DL with same email address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/214447/exchange-duplicate-dl-with-same-email-address (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I noticed the is duplicate display name & smtp address for below account. And 1 of them is no longer exist on AD. No matter how i trying to delete is not successfully.     

Pls help to advise.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-31*

Hi @Russell Ang  ，    

Is this only affecting the particular distribution group?    

What's the version of your Exchange server? Are you in a hybrid environment?    

And do you have any idea about how this duplicate account was created?    

Please try running the cmdlet below to see if the the duplicated account can be removed:    

```
Remove-DistributionGroup -Identity 
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
