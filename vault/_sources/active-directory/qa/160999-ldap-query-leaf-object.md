---
title: "LDAP query leaf object"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160999/ldap-query-leaf-object
question_id: 160999
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# LDAP query leaf object

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160999/ldap-query-leaf-object (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Looking for a way to use Powershell to query leaf objects of an AD account. In particular, I am trying to query the ExchangeActiveSync leaf objects under a user account in AD. I am able to query the AD account in Powershell itself, but not sure about a way to view the leaf objects of that account.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Nice. Thanks, that gave me the ideas I needed.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

The data for ActiveSync connections is stored in the leaf objects, every so often I have users that build up a large number of these due to ActiveSync code and they need to be erased. Using Exchange is too slow to run this query against thousands of users, my environment is fortune 20 level. When I run the following command I can see ActiveSync connections in Exchange..  

Get-ActiveSyncDeviceStatistics -Mailbox $user | sort LastSuccessSync -Descending | ft LastSuccessSync,DeviceType,DeviceModel,DeviceOS,Guid,Status  

I am trying to delete the ones in the above list that have a LastSuccessSync date of older than X days, say 30 in this example. I would much rather have this run at the LDAP level than on my Exchange servers.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-12*

Is there a reason you aren't using the Exchange cmdlets to do this?  

I'm pretty sure the cmdlet Get-CASMailbox would return what you need.
