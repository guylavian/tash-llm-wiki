---
title: "Can't sign-in through ADFS when ExtranetLockout is enabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/36338/cant-sign-in-through-adfs-when-extranetlockout-is
question_id: 36338
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Can't sign-in through ADFS when ExtranetLockout is enabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/36338/cant-sign-in-through-adfs-when-extranetlockout-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two AD forests with two-way trust (selective authentication): prod.com and clients.com.    

Schemas in both forests were updated to Windows 2019 by adprep.    

There are ADFS and WAP servers with Windows 2019 in prod.com. (Upgraded from Windows 2012 R2 farm by https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server)    

ADFS configured as:    

Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID mail -LookupForests prod.com,clients.com.    

Permission "Allowed to authenticated" on ADFS.prod.com was granted for all users from clients.com.    

When ExtranetLockout is enabled on ADFS, users from clients.com can't sing-in using CLIENTS\username format, but can sign-in by ******@clients.com.    

User receive errors 1210 and 516 in Security logs:    

User:     

clients\user1     

nBad Password Count:     

0     

nLast Bad Password Attempt:     

1/1/0001 12:00:00 AM    

It seems that ADFS can't find user clients\user1 or his attributes badPwdCount and badPasswordTime.    

When ExtranetLockout is disabled, users from clients.com can sing-in as CLIENTS\username and ******@clients.com also.    

Users from prod.com can always sing-in in any way regardless of ExtranetLockout setting.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-06-16*

ADFS service account (from prod.com domain) has permission "Read all properties" for user objects in clients.com

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-06-16*

When using the extranet lockout policy, the ADFS server is trying to lookup the user using LDAP before the authentication. Therefore, the ADFS service account will have to be able (authorized) to make that call.
