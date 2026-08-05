---
title: "Nov 08, 2022 updates broke ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1105569/nov-08-2022-updates-broke-adfs
question_id: 1105569
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Nov 08, 2022 updates broke ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1105569/nov-08-2022-updates-broke-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After rebooting the domain controllers ADFS stopped working in our environment.  We applied the Nov 17 OOB update and restart the domain controllers then the ADFS cluster, still does not work.    

https://support.microsoft.com/en-us/topic/november-17-2022-kb5021656-os-build-20348-1251-out-of-band-b165e8dd-cc02-4912-9cfa-a6b2b1016c37    

On the ADFS servers we see the following errors:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-28*

What fixed this for us was ensuring all accounts used for Kerberos auth had ms-DS-SupportedEncryptionTypes AD attribute cleared.  If there was any data, even 0x0 in this field we encountered authentication issues.
