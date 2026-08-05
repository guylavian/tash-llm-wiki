---
title: "Connect to Exchange Management Shell using an account in a trusted domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1851682/connect-to-exchange-management-shell-using-an-acco
question_id: 1851682
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connect to Exchange Management Shell using an account in a trusted domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1851682/connect-to-exchange-management-shell-using-an-acco (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There are a couple of AD DS Domains relevant here, which I'll call USER (users log into here on a day-to-day basis, workstations and the majority of servers in the estate are all joined here) and RESOURCE (Exchange is installed here).  Exchange Mailboxes have an AD User object in RESOURCE Domain, which is disabled, and have the LinkedMasterAccount set as the user's account in USER.

A Two-way External trust exists between USER and RESOURCE domains.  IT Staff have admin accounts in both USER and RESOURCE domains.

We've recently audited the RBAC roles we have set up in Exchange, and they need a little care and attention.  One of the issues is that admin accounts in the RESOURCE domain aren't maintained anywhere near as well as those in the USER domain, so I'm trying to delegate all the necessary access to manage Exchange to the admin accounts in USER instead, so that we don't have separate admin accounts in RESOURCE to maintain.

I've managed to set up Linked Role Groups in the USER Domain, mirroring the built-in ones as well as creating some more granular ones that we need, and these seem to work as expected in ECP.  However, they don't seem to be able to connect to any of the Exchange servers from Exchange Management Shell, instead giving the error:

```
New-PSSession : [exchangeserver1.resource.org] Connecting to remote server exchangeserver1.resource.org failed with the
following error message : WinRM cannot process the request. The following error occurred while using Kerberos
authentication: Cannot find the computer exchangeserver1.resource.org. Verify that the computer exists on the network
and that the name provided is spelled correctly. For more information, see the about_Remote_Troubleshooting Help topic.
```

It loops through all the Exchange servers in the environment, giving the same error.

This error occurs from a management box with the Exchange Tools installed, as well as from an Exchange server itself, when logged in as a USER admin account.  Logging into the same servers with a RESOURCE admin account connects and works as expected.

Is there something else I need to set up or configure to allow USER accounts to authenticate?  As far as I can tell, the permissions are all delegated correctly.

Many thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-01*

This may help:

https://techcommunity.microsoft.com/t5/exchange-team-blog/how-to-enable-kerberos-authentication-for-accessing-exchange-in/ba-p/605166
