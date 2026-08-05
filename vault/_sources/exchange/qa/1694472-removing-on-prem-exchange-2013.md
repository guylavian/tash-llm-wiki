---
title: "Removing on-prem Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1694472/removing-on-prem-exchange-2013
question_id: 1694472
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Removing on-prem Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1694472/removing-on-prem-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an old Exchange 2013 server still hanging around which I want to get rid of. We have migrated all mailboxes to EXO years ago and all the public MX records point to our in-line mail filter.  There's still a fair few DG left that haven't been migrated yet. - Outside of management which we can do with PS, do these still depend on the CAS server being up at all?.  It has not been used for SMTP relay for many years either.

What are the minimum steps I need to do to get rid of this CAS box with the least likelihood of breaking things? Note, we still have on-prem AD and sync local AD to MSO via Azure AD Connect.  I've also installed the Ex2019 PS tools on another server if they are needed to manage anything left.

Theres a lot of lengthy articles than can be complex and they don't always say the same things. I wasn't intending to "uninstall" Exchange, I am just going to switch it off and make it disappear so the Schema attributes aren't removed.

Some steps I think would be

-  Remove-HybridConfiguration

-  Get-IntraOrganizationConnector (returns no result)

-  Outodiscover already points to outlook.office365.com for Outlook clients. Idc about the internal config since I'm turning it off

-  Delete the send/receive connectors in EXO

Is there a dummies guide to the required steps?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-12*

Can I clarify this point which is at the bottom of the linked article.

How and when to decommission your on-premises Exchange servers in a hybrid deployment | Microsoft Learn  

"if you maintain identity synchronization from Active Directory, you'll need to continue to maintain at least one Exchange server on-premises."

I see a lot of conflicting info about this. Some articles say you can remove the last Exchange server some say you can't. Which is it?

As stated before, we still run an on-premise AD and run AAD sync and will for the foreseeable future. And I've installed the Exchange PS tools on another server in case something needs to be managed on-prem. We are already doing all of our new user and mailbox setup via PS.

Our only local Exchange server has been turned off for a month now. why do I need to keep it?
