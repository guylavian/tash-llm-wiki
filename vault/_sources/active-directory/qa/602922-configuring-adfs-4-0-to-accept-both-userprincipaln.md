---
title: "Configuring ADFS 4.0 to accept both UserPrincipalName and the Default AD Domain name?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/602922/configuring-adfs-4-0-to-accept-both-userprincipaln
question_id: 602922
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Configuring ADFS 4.0 to accept both UserPrincipalName and the Default AD Domain name?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/602922/configuring-adfs-4-0-to-accept-both-userprincipaln (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

My current ADFS server and AD Domain is: Domain1.com (single AD forest)    

I've also added the additional UPN so the user can log in as NewCompany.Net domain.    

Using ADFS 4.0 on Windows Server 2016 https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/whats-new-active-directory-federation-services-windows-server#whats-new-in-active-directory-federation-services-for-windows-server-2016    

How can I configure so the Claims of my user can accept both?    

User PrincipalName and the default AD Domain name?    

Thanks in advance.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

There's nothing special to do unless you have done some customization of the login page.   

Of course if you have rules that parse the UPN and look for something special, then yes you would need to update those (eventually). But in any cases, we would need more info from you.
