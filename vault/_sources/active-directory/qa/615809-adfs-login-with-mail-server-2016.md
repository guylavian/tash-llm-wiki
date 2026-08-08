---
title: "ADFS Login with mail (Server 2016)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/615809/adfs-login-with-mail-server-2016
question_id: 615809
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Login with mail (Server 2016)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/615809/adfs-login-with-mail-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have an ADFS server running Windows Server 2016. our structure looks like this:    

UPN: username@keyman  .lokal    

Mail: name.surname@keyman  .de    

The login to the ADFS via UPN works. Now we have the requirement to be able to log in with the email address.    

We have already configured the following option but without success.    

Command: Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID mail -LookupForests domain.local    

As error message we get an ID 4625 Error (Unknown User or Password)    

Thanks a lot    

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-11*

Hi,  

the user has a filled mail attribute.  The login should be done with a external website. However, if I want to log on directly to the ADFS server (internal) using the form-based logon (adfs/ls/IdpInitiatedSignOn.aspx), this does not work either.  

However, externally no Form Based login is used, but here the error is the same.  

Kind Regards  

Michael

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-09*

The config looks about right. Maybe the user doesn't have a mail attribute? Were you using Form Based Authentication (the actual HTML form) to log in?
