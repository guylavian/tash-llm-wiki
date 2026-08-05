---
title: "Modify the way Active Directory creates users and computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1102594/modify-the-way-active-directory-creates-users-and
question_id: 1102594
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Modify the way Active Directory creates users and computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1102594/modify-the-way-active-directory-creates-users-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Im migrating an old OpenLDAP system over to Active Directory and was wondering if it was possible to modify the way that Active Directory does its user and computer creation.    

Currently on the old system when a new User is created, creates it as a Domain Component (DC) rather than the Active Directory method of creating a Common Name (CN) for example:    

DC=john.smith,OU=people,DC=constco,DC=com    

rather than    

CN=john.smith,OU=people,DC=constco,DC=com    

It would be nice if we didn't have to modify decades worth of scripts to fit this difference. While I acknowledge this may not be standard nor is it X.500 Standard I am curious if it is possible to make active directory use / acknowledge DC=john.smith rather than CN=john.smith.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-24*

Hi,    

Technically it might be possible to change the default "CN", you would need to change the rdnAttID attribute of the user object to be "DC", but once changed, there could be loads of downstream impacts, some that will be obvious straight away, then other which will appear later down the track and cause you all sorts of random issues, or low level APIs think the DC is the domain context and fail.  It's difficult to predict what these will be but it could be something as simple like existing queries don't return all entries, or native management tool don't work, to the user is unable to authenticate against the domain for certain applications.    

The recommendation is probably change the scripts and leave AD as default, as this change will be outside the normal support.    

Gary.
