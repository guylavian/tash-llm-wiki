---
title: "Active Directory Reset pasword vs lastLogonTimestamp"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327493/active-directory-reset-pasword-vs-lastlogontimesta
question_id: 327493
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Reset pasword vs lastLogonTimestamp

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327493/active-directory-reset-pasword-vs-lastlogontimesta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We noticed that in Active Directory configured at Windows Server 2019 reset password is changing lastLogonTimestamp. Is it correct behavior?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-24*

Hi,    

Interactive, Network, and Service logons will update the lastLogontimeStamp . So if a user logs on interactively, browses a network share, access the email server, runs an LDAP query etc… the lastLogontimeStamp attribute will updated if the right condition is met.    

The lastLogontimeStamp attribute is not updated every time a user or computer logs on to the domain. The decision to update the value is based on the current date minus the value of the ( ms-DS-Logon-Time-Sync-Interval attribute minus a random percentage of 5).    

For more information , you can refer to the following link:    

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/8220-the-lastlogontimestamp-attribute-8221-8211-8220-what-it-was/ba-p/396204    

When you reset the password through the ADUC, It will not effect the lastLogonTimestamp attribute .    

The Lastlogon attribute will change immediately, but not the lastLogonTimestamp attribute.
