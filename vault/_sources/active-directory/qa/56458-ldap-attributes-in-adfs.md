---
title: "LDAP Attributes in ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56458/ldap-attributes-in-adfs
question_id: 56458
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# LDAP Attributes in ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56458/ldap-attributes-in-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;  

In ADFS, when configure a claim rules for Relying Parties, when I specify "E-mail-Addresses" in LDAP Attributes, how do I know what actual email address is being used for authentication?  

thanks!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-31*

What you pick in the issuance transform rules is not used to authenticate the user, it is what is sent to the application as a claim in the token.  

Do you mean that you would like to use the email instead of the UPN or the samaccountname to log in?
