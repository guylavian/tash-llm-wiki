---
title: "Exchange 2013 - Junk E-mail List Size Limit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123762/exchange-2013-junk-e-mail-list-size-limit
question_id: 123762
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 - Junk E-mail List Size Limit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123762/exchange-2013-junk-e-mail-list-size-limit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We're running 'Exchange 2013' and have a user who is being presented with the message below in 'Outlook 2016'.    

    

The user doesn't want to start deleting addresses from their current 'Blocked Senders' entries in Outlook because that would defeat the object of this facility.    

Is there a way to increase the default size (510KB) of the Junk E-mail lists for this user?    

Any help gratefully received.    

Kind regards,    

Glen

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-13*

Hi @GlenV  ,    

Andy has shared a great official article about his and hopefully you can find that helpful:     

Outlook error indicates that you are over the Junk E-mail list limit    

As mentioned in the article, the Max Extended Rule Size registry value does not apply to Exchange Server 2013 so it's now not feasible to increase the default size (510KB). Given this, please have a check and try to disable the "Trust e-mail from my Contacts" setting in Outlook if the user in question is currently having it enabled:     

    

With the above setting confirmed, you can download the MFCMAPI tool and check the PR_RULE_MSG_STATE property using the steps in the article.    

If the error still persists, then it's likely this is due to the large number of entries in the Junk E-mail lists, you'll then have suggest the user to deleting some entries or using workarounds like creating Outlook rules as provided by Andy.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
