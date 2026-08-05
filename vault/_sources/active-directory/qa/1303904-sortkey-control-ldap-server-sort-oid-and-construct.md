---
title: "SortKey Control (LDAP_SERVER_SORT_OID) and constructed attribute \"msDS-ReplValueMetaData\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1303904/sortkey-control-ldap-server-sort-oid-and-construct
question_id: 1303904
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# SortKey Control (LDAP_SERVER_SORT_OID) and constructed attribute "msDS-ReplValueMetaData"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1303904/sortkey-control-ldap-server-sort-oid-and-construct (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can the SortKey control ( [MS-ADTS].pdf -> 3.1.1.3.4.1.13 LDAP_SERVER_SORT_OID ) be applied to constructed attributes, such as 'msDS-ReplValueMetaData' as well? I want to search the metadata for linked attributes. For groups with several 10.000 members, this is time-consuming. For the 'member' attribute, either 'pszObjectDn' could be returned in ascending order for a b-tree search or 'usnLocalChange' in descending order for the latest changes in Page 'range=0-999'.

A dirSync search returns only changed members. I would like to read out the metadata for changed linked values as soon as possible.

/Volker

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-12*

Hi Volker,

I've tested it on a Windows 2019 DC, and it doesn't support the sort control with a constructed attribute.  If you do include the control specifying the msDS-ReplValueMetaData attribute you get the following error:

`Error: (0x0C) The control is critical and the server does not support the control, Server Error: 0000217A: SvcErr: DSID-03140452, problem 5010 (UNAVAIL_EXTENSION), data 0, Ext Error: (8570) The sort order requested is not supported.`

I think the return order is based on the last changed returned first.

Gary.
