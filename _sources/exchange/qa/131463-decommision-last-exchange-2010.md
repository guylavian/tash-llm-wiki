---
title: "Decommision last Exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/131463/decommision-last-exchange-2010
question_id: 131463
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Decommision last Exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/131463/decommision-last-exchange-2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a 2010 Exchange on premises configured with Hybrid right now.  We have 3 mailboxes left on prem that should be moved to 365 in the next week or so.  The objective is not to have any mailboxes hosted on prem, but install one 2016 or 2019 server for management, since that's still the requirement from MS.  My questions are:  

-  Should we install 2016 while 2010 is still in production?  If so, I'm having some issues with that where 2016 throws a "Deserialization error:..." and would not let me proceed with the installation.  

-  Should we decommission 2010 completely, then install 2016 or 2019 and use that for recipient management?  

Would really appreciate some clarification and guidance on that.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-22*

anonymous userDavid @Lydia Zhou - MSFT   Thank you both for your assistance!    

When you get a moment, no rush, I'm curious which user attributes are being managed by the on-prem exchange in this configuration?  Other people are talking about using ADSIEdit to manage them.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-20*

@YuriyK-1490     

As Andy mentioned, we can install and upgrade to Exchange 2016 before uninstalling Exchange 2010.     

There are two Exchange server roles for Exchange 2016. They are Mailbox server role and Edge Transport server role. If you still need to manage users from on-premises, Mailbox server role is suggested to install. You can check this for more information about Exchange 2016 server roles: Server role architecture.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-19*

I would install 2016 now before removing 2010.    

What is the exact error and have you prepped the AD Forest and are following the guidance to install 2016 into the forest and installing the latest 2016 CU?    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

https://learn.microsoft.com/en-us/windows-server/get-started/system-requirements
