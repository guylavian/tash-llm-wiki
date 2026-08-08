---
title: "Exchange 2019 to Exchange Online EWS Wont Connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2184984/exchange-2019-to-exchange-online-ews-wont-connect
question_id: 2184984
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange 2019 to Exchange Online EWS Wont Connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2184984/exchange-2019-to-exchange-online-ews-wont-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I'm at a loss here trying to configure a new migration endpoint for a new tenant, and it works for me but not for this one.

Below is the error i get when i do Test-MigrationServerAvailability, I have tried the following:

-  Verified MRS proxy is running

-  Basic is not enabled but i also have basic not enabled for another tenant and that works just fine

-  Tried different accounts with exchange privileges

4, Verified the passwords are correct 

Result          : Failed

Message         : The connection to the server 'owa.domain.com' could not be completed.

SupportsCutover : False

ErrorDetail     : Microsoft.Exchange.Migration.MigrationServerConnectionFailedException: The connection to the server

                  'owa.domain.com' could not be completed.

                   ---> Microsoft.Exchange.MailboxReplicationService.MRSRemoteTransientException: The call to

                  'https://owa.domain.com/EWS/mrsproxy.svc' failed. Error details: The HTTP request was

                  forbidden with client authentication scheme 'Negotiate'..

                   ---> Microsoft.Exchange.MailboxReplicationService.MRSRemotePermanentException: The HTTP request was

                  forbidden with client authentication scheme 'Negotiate'.

                  OriginalFailureType: MessageSecurityException, WellKnownException: MRSRemote None MRSRemote

                  Remote stack trace:

Anything else i should be looking at? Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-11*

Hello

Thank you for posting in Microsoft Community forum.

Based on the description, I understand your question is related to Exchange.

Since there are no engineers dedicated to this topic in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.

Questions - Microsoft Q&A

Click the "Ask a Question" button in the upper right corner to post your question and select any tags related to your productions.

Thank you for your understanding and support. If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Molly
