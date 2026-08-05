---
title: "how to create LDAP query for User profile sync SharePoint on-premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1010419/how-to-create-ldap-query-for-user-profile-sync-sha
question_id: 1010419
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to create LDAP query for User profile sync SharePoint on-premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1010419/how-to-create-ldap-query-for-user-profile-sync-sha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to create LDAP query to sync specific groups from AD instead of syncing all 100's of groups to User profile sync in SharePoint 2019.    

Example: I would like to sync anything that as "Groups", "ServiceAccounts" "Users", "Vendors".    

Can someone please help me out as I don't see any article from Microsoft to filter out and sync/import specific OU's.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-23*

Hi,    

With a standard LDAP query there is not an option to search based on the OU, as the BaseDN in the filter is the method that is normally used.    

One of the options is to set an attribute on the objects that you want to include and then use a standard LDAP query to return the objects with the attribute set.    

Gary.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-19*

Hi @RajKumar  ,    

I found the following link for your reference, hope it would help you.    

Active Directory: LDAP Syntax Filters    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
