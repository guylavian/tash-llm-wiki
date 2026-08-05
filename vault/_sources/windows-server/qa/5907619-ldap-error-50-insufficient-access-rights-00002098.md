---
title: "LDAP ERROR: 50 (Insufficient Access Rights)  00002098: SecErr: DSID-031538AF, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5907619/ldap-error-50-insufficient-access-rights-00002098
question_id: 5907619
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP ERROR: 50 (Insufficient Access Rights)  00002098: SecErr: DSID-031538AF, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5907619/ldap-error-50-insufficient-access-rights-00002098 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,

I am trying to reproduce the following Active Directory domain join failure in a lab environment:

Failed to join domain: User specified does not have administrator privileges

LDAP ERROR: 50 (Insufficient Access Rights)

00002098: SecErr: DSID-031538AF, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0

Could anyone explain which AD permissions or configurations can specifically trigger this error?

I am particularly interested in understanding:

What permissions are required for a user to join a computer to the domain?

-  Which permission removals or restrictions will cause LDAP Error 50 / problem 4003?

Are there any Microsoft documents describing the exact conditions that generate this error?

My goal is to reproduce the issue for validation and troubleshooting purposes.

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-06-01*

rhis error occurs when the account lacks rights to create or modify computer objects in Active Directory. By default, any authenticated user can join up to 10 machines due to the `ms-DS-MachineAccountQuota` attribute. Setting that quota to 0 or removing Create/Delete Computer Object permissions on the target OU will trigger LDAP error 50.
