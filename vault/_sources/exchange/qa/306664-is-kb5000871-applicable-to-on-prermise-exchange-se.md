---
title: "Is KB5000871 applicable to on-prermise Exchange servers with no mailboxes?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/306664/is-kb5000871-applicable-to-on-prermise-exchange-se
question_id: 306664
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Is KB5000871 applicable to on-prermise Exchange servers with no mailboxes?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/306664/is-kb5000871-applicable-to-on-prermise-exchange-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have hybrid setup with all mailboxes in OS365 in the cloud. No mailboxes on premise. On-premise we have a Exchange server without mailboxes which is used purely to route emails from our internal applications.  

Is this patch applicable to us? Also is there a level of Exchange CU required for the patch.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-14*

I think that maybe the issue is that the Edition of Exchange Server we are running is "Coexistence".

Could it be that the CU packages do not work correctly for these editions??

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-10*

Hi @SeekingTruth   ,    

Yes, the update is for every On-prem Exchange no matter it has mailboxes or not.    

Note the Exchange version requirement: Exchange 2013 CU23, 2016 CU18 & 19, 2019 CU7 & 8.    

For more details you can read: FAQ for March 2021 Exchange Server Security Updates    

Best regards,    

Zhengqi Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
