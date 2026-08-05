---
title: "Active Directory Attribute Creation Schema OID Not Showing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160365/active-directory-attribute-creation-schema-oid-not
question_id: 1160365
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Attribute Creation Schema OID Not Showing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160365/active-directory-attribute-creation-schema-oid-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

We want to add some custom AD Attributes and the OID VBS Script from TechNet isn't showing the Root OID to use.

Some of the links are not working, but found the one below and saving the script/renaming to .vbs and when I run it all I get is the regsvr32 showing "dllregisterserver in schmmgmt.dll succeeded" and nothing else.

[https://learn.microsoft.com/en-us/windows/win32/ad/obtaining-an-object-identifier-from-microsoft

I know you're supposed to get a pop-up with your Root OID and more info, but that isn't popping up.

Anybody else getting this issue? Is there another script that I can run to get the X.500 OID so we can add attributes?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-12*

It didn't pop-up, but it did save it on the local administrator account on the machine.  I was logged in with another scheme admin account.

Thanks !!!!
