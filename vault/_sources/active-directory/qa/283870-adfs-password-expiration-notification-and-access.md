---
title: "ADFS Password expiration notification and access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283870/adfs-password-expiration-notification-and-access
question_id: 283870
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Password expiration notification and access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283870/adfs-password-expiration-notification-and-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to know if this    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-to-send-password-expiry-claims    

applies for AD on 2008 R2 domain and forest functional levels.     

So far I know this is only for password expiration notification.    

I also need to find out if there is a way ADFS can feed back M365/Azure AD password expiration status so that a remote user get blocked after a certain days their password expires and they will require to call support to reset.     

Current situation is remote users can login to M365 services (via ADFS authentication to AD), if there password expires on-premise, they still can access those Microsoft services for a long time (think default value is 90days).     

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-02-23*

The claim rule to send the claim expiry will be working as long as the user used FBA or WH4B to authenticate (irrespective of the version of AD). This is just for notification in some applications (Exchange Online only as far I as recall). This is a feature to allow notification, it does not help or impact the lifetime of the user's token.  

By default, Azure AD Connect is synchronizing the pwdLastSet attribute of the users. So Azure AD knows when a password is supposed to expire. If you do not synchronize the attribute (because you customized the default rules - bad idea to start with), then the maximum age for token refresh is limited to 12 hours.  

Also, there is an endpoint in ADFS that can be used for users with an expired password (or with an account for which the box "User must change password at next logon" is checked). It is the URL https://......../adfs/portal/updatepassword. It is disabled by default and needs to be enabled. It does not help all the time though. But it does exist.
