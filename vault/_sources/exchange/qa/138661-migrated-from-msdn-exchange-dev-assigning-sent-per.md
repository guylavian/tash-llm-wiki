---
title: "[Migrated from MSDN Exchange Dev] Assigning sent permission for Shared mailbox not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138661/migrated-from-msdn-exchange-dev-assigning-sent-per
question_id: 138661
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev] Assigning sent permission for Shared mailbox not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138661/migrated-from-msdn-exchange-dev-assigning-sent-per (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Assigning sent permission for Shared mailbox not working  

Hi,  

successfully configured shared mailbox and assigned users to access, configured full permission and send as permission to the required users but clients cant find the option to send from the shared mailbox.  Kindly advise what step have missed

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Thank you AndyDavid   

Using Exchange 10 on premises.  

Will follow as advised and let you know the result soon.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-26*

HI @Rmartin0000      

What version of Exchange is this? With Exch 2013 CU9 and above:    

You can follow this:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/sent-mail-is-not-saved    

```
set-mailbox  -MessageCopyForSentAsEnabled $True
```

this will put the sent items in the shared mailbox as you want.    

If Exch 2010 :    

https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/sent-mail-is-not-saved#exchange-server-2010-service-pack-2-update-rollup-4-or-later-update

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Thank you Joyceshan  

By default all my sent emails of shared mailbox appearing in regular send box searched few threads and found it should be manually move it which is not good suggestion as multiple users accessing this shared mailbox.  

Any feasible suggestion?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi,    

In outlook, when you write a new email, Options > From    

    

Then you choose the other mailbox in the from field, and enter the shared mailbox there    

    

    

In OWA, choose show from then enter the shard mailbox    

    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
