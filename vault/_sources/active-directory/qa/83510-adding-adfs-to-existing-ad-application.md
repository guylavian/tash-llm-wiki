---
title: "Adding ADFS to existing AD Application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/83510/adding-adfs-to-existing-ad-application
question_id: 83510
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Adding ADFS to existing AD Application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/83510/adding-adfs-to-existing-ad-application (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an existing .NET application that uses Active Directory to authenticate users and search for user/OU data using DirectorySearcher object. Our customer has several AD servers and would like our existing application to authenticate/search from a single endpoint. Can we leverage our existing application by adding ADFS service to the customer's network to authenticate/search across several AD servers? Our application uses .NET System.DirectoryServices.DirectorySearch object using LDAP queries to authenticate and search for user/OU data.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-30*

You can leverage Active Directory Federation Services (ADFS) to achieve a unified authentication and authorization experience across multiple Active Directory (AD) servers in a network. ADFS provides a way to establish trust between different AD domains and forests, allowing for a single sign-on (SSO) experience across them.
