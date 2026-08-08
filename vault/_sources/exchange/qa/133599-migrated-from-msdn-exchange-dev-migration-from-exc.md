---
title: "[Migrated from MSDN Exchange Dev] Migration from Exchange 2010 to Exchange 2016 autoconfiguration does not work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/133599/migrated-from-msdn-exchange-dev-migration-from-exc
question_id: 133599
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Migration from Exchange 2010 to Exchange 2016 autoconfiguration does not work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/133599/migrated-from-msdn-exchange-dev-migration-from-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After you migrate mailboxes from Exchange 2010 to Exchange 2016, autoconfiguration of user profiles does not work by giving two errors:    

The first one keeps requesting the password.    

The second does not connect to the Exchange 2016 server.    

The only solution I've been finding is to create a new profile with it and leave it as a child so that the profile that was first in place can connect to the Exchange 2016 server.    

You have already performed the self-configuration tests by giving me as the only match on all migrated accounts:    

GetLastError-0; httpStatus-401 and GetLastError-0; httpStatus-200    

    

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/7305ed7d-3bc6-4bef-a63c-ed70f515a696/migration-from-exchange-2010-to-exchange-2016-autoconfiguration-does-not-work?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-21*

Hi,

I'm not familiar with language shown in picture, can you run the test again in English?

Let's get started with basic settings:

The users you talking about are all internal, right?

After you migrated the mailboxes, have you changed SCP and the URLs in virtual directories pointing to Ex2016?

See Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2010 if you need further guidance.

Run "Restart-WebAppPool MSExchangeAutodiscoverAppPool" in Powershell as administrator manually on all your servers.

Since creating a new profile would work, what if you re-create the old profiles, would they work?

Also, check the authtification of MAPI virtual directory in Ex2016, make sure "Negotiate" is ticked.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
