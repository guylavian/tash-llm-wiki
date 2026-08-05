---
title: "[Migrated from MSDN Exchange Dev]Exchange Server 2010 - removing legacy email addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145591/migrated-from-msdn-exchange-dev-exchange-server-20
question_id: 145591
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Exchange Server 2010 - removing legacy email addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145591/migrated-from-msdn-exchange-dev-exchange-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Non-developer Exchange forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange Server 2010 - removing legacy email addresses  

[Original post]  

Hello folks,  Just checking in to see if there is any risks to simply removing the legacy SMTP email addresses from our email address policy in Exchange 2010. The default (reply to) address isn't being changed, nor the recipient filters.  

We are currently in a state of co-existence with Exchange 2010 & Exchange 2016 (migrating mailboxes shortly) then off to MS365. Prior to going to MS365 we want to clean up the old email addresses (built up during corporate buy-outs).  

So, can I just delete the old ones, and all is good, or is there something else I need to be aware of? I was thinking about deleting those addresses from the policy, and then immediately also removing the corresponding 'accepted domains'.  

Lastly, running a script in AD to remove them from the user accounts.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-30*

Hi,    

To my knowledge,since the legacy addresses added by the customed email address policy are no longer in use,you can delete them if you want.    

It won't do harm to your environment as long as you keep the default address policy.    

Here is a similar case for your reference: Legacy Email Address Polcies - Delete or Upgrade?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
