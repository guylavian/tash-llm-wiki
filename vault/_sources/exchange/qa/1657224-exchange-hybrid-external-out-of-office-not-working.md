---
title: "Exchange Hybrid - External Out of Office not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657224/exchange-hybrid-external-out-of-office-not-working
question_id: 1657224
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid - External Out of Office not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657224/exchange-hybrid-external-out-of-office-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

We have a hybrid configuration where some mailboxes are still on premises.  

In- and outbound mail flow is already configured to be routed through Exchange Online.

Everything works, means on premises mailboxes are able to send external emails through EXO.  

But external out of office messages, are not working for on premises mailboxes.  

On the on premises Exchange Server message trace I always see a FAIL with the error message "550 5.7.64 TenantAttribution: Relay Access Denied".

Why is that happening, while the same user is able to send emails to external email addresses?

Regards  

Peter

## Answer (community) — community member

*upvotes: 1 · updated: 2024-07-25*

We are facing exactly the same issue. 

There is not even a sending-attempt of the OOF-Reply visible in the onprem-exchange 2019 Mail-Flow logs.

Internal OOF is working fine, remote mailboxes can use external OOF just fine - but for onpremise mailboxes, external OOF is not working anymore. Used to work at least 6 months ago.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-19*

Hi @Noah Ma-MSFT

Thanks for answering. Out of office for external is working fine for online mailboxes, but as I wrote, not for mailboxes that are still on premises.

The Remote Domain setting are configured as follows:

Online - Default Remote Domain:

-  Allo only external out of office replies

-  Allow automatic replies = True

On Prem - Default Remote Domain:

-  AutoReplyEnabled = True

-  AllowedOOFType = External Already tried using ExternalLegacy, but with the same result.

As said, there is no problem for on premises mailboxes to send emails to external users, the issue only exist for out of office sent to external.

Regards PeterHi @Noah Ma-MSFT

Thanks for answering.  

Out of office for external is working fine for online mailboxes, but as I wrote, not for mailboxes that are still on premises.

The Remote Domain setting are configured as follows:

Online - Default Remote Domain:

-  Allo only external out of office replies

-  Allow automatic replies = True

On Prem - Default Remote Domain:

-  AutoReplyEnabled = True

-  AllowedOOFType = External  

Already tried using ExternalLegacy, but with the same result.

As said, there is no problem for on premises mailboxes to send emails to external users, the issue only exist for out of office sent to external.

Regards  

Peter

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-18*

Hi @Peter,

Based on your description, I understand that you have an issue that out of office not working for external. For this situation, have you configured the remote domain allow external out-of-office message? Please check if settings for that remote domain are correct as the following steps:

-  Sign in to the EAC.

-  Go to Mail flow > Remote domains in the left-hand and click the affected remote domain on the list.

-  Click Edit reply types. 

-  Make sure that the Allow only external out of office replies option is selected and that the Allow automatic replies checkbox is checked.   

-  Click Save to apply your changes.

If you have any questions, please feel free to contact me.
