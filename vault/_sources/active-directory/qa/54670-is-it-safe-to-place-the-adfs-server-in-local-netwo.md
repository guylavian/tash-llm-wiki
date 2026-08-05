---
title: "Is it safe to place the ADFS server in local network for claims-based application authentication."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/54670/is-it-safe-to-place-the-adfs-server-in-local-netwo
question_id: 54670
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Is it safe to place the ADFS server in local network for claims-based application authentication.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/54670/is-it-safe-to-place-the-adfs-server-in-local-netwo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;  

I just created my first AD FS on Windows Server 2012 R2 on LAN which is used to authenticate the claims-based application on cloud which provided by my SaaS service provider.  

I can authenticate with their application properly but they told me that they do not support ADFS Proxy, in this case; what is the best practice to secure my ADFS server.  Currently; I have to do natting on firewall to allow inbound traffic to ADFS.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-30*

This claim makes no sense. What do they mean by they don't support ADFS Proxy (which is called Web Application Proxy [aka WAP] in Windows Server 2012 R2 by the way)? The SaaS is agnostic of the IDP infrastructure. Federation protocols in this scenario is entirely driven by the user. The application doesn't know if there is a proxy in the mix.  

Besides, WAP are not used when a user is connected from the LAN.  

We'll need to know a bit more about the infrastructure here to help you. So far, this doesn't make a lot of sense :(
