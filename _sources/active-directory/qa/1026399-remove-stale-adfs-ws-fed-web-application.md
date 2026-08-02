---
title: "Remove stale ADFS WS-Fed web application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1026399/remove-stale-adfs-ws-fed-web-application
question_id: 1026399
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Remove stale ADFS WS-Fed web application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1026399/remove-stale-adfs-ws-fed-web-application (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an ADFS server farm that had 2 relying party trusts - one WS-Fed for Office 365 federation and another SAML-based. The Office 365 authentication has been transitioned to managed authentication long time ago and now the sign-in page remains in ADFS. The problem is that it is cached in Google and some users try to sign in directly to the ADFS sign-in page, which of course returns an error. I want to remove the web app, but leave the ADFS farm operational as the other SAML relying party trust is still in use. How do I do this? Every article I found concerns connecting to Azure AD using PowerShell, converting the domain to standard and then decomissioning the servers, which is not what I want.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-01*

The ADFS sign-in page is cached in Google and if you click the link, it opens the username and password login form. If you try to log on, it returns an error since the federation trust does not exist anymore. This is a problem only if users try to find the service using the search engine, we have migrated to pass-through authentication years ago, so this sign-in page is no longer needed, but I don't know how to remove it. ADFS is on Windows Server 2016.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-10-01*

What do you mean by "the sign-in page remains in ADFS"?
