---
title: "Exchange 2016 / Outlook 2016 Mailbox Size Is Wrong"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/119364/exchange-2016-outlook-2016-mailbox-size-is-wrong
question_id: 119364
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Exchange 2016 / Outlook 2016 Mailbox Size Is Wrong

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/119364/exchange-2016-outlook-2016-mailbox-size-is-wrong (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note that we went through a full system loss in May and had to rebuild a failed 2010 installation as 2016 and import old user mailboxes in as .pst files.   

I have users who are showing an odd issue.  The total mailbox size in there Outlook is wrong but on the server it's correct.  I've gone through the below items and do not see any issues yet.  Has anyone seen this before?  

-  Exchange OWA has the correct info  

-  Outlook does not have the correct info. Both the total size of the mailbox and space used are wrong.  

-  The client is warning people that their mailbox is filling up even though the server still has the correct information.    

-  The feature that shows you space used locally disappears when you turn off Exchange Cached Mode. It might be related to caching?  

-  Building a new user profile in Outlook did not fix the issue.  

-  Deleting the .ost file and restarting Outlook makes it so the total size disappears.    

-  My account has this issue. I completely rebuilt my account from scratch in AD and Exchange after the rebuild in Exchange 2016.    

Before the move to 2016 user mailboxes sizes were configured at the mailbox.  I configured the sizes on the DB and set all users to use the DB settings.  Is it possible some of the user accounts are trying to retain old settings?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-27*

Helped me too, Exchange 2019 environment
