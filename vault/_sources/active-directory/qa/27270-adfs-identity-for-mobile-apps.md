---
title: "ADFS - Identity for Mobile Apps"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/27270/adfs-identity-for-mobile-apps
question_id: 27270
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - Identity for Mobile Apps

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/27270/adfs-identity-for-mobile-apps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI Guys,  

I have requirement is to use Application from Browser and Mobile App as well.  

ADFS infra running 2016 & 2019.   

If i create Relay Party it is working only in Browser. How i can make identity with Both?  

How to create the identity for mobile application.   

Please guide me.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-21*

Thanks for the article.   

can you please refer any article which configure identity to make use of Web Browser and mobile.  

For mobile app, customer asking to provide the client ID.  

I have created  Application Group with only client ID and share to the same. But, when customer trying to connect with client its going on my Azure tenant return with error since application group created on AD FS.  

any help?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-19*

Usually mobile applications will work well with OAuth2. But it depends how your develop it really. They are many ways to do it. ADFS just plays the role of your Identity Provider here, nothing more. It is actually agnostic of where and what the application really is. So I suggest you look up OAuth and devl. Here will be a good start: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-development.
