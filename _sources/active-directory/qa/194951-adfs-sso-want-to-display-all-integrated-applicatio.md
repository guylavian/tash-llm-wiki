---
title: "ADFS SSO: Want to display all integrated applications in one single page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/194951/adfs-sso-want-to-display-all-integrated-applicatio
question_id: 194951
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS SSO: Want to display all integrated applications in one single page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/194951/adfs-sso-want-to-display-all-integrated-applicatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi friends,  

I want to display all integrated applications in one page once the user login to ADFS SSO page. Is that possible? Any way we can achieve it.  

-Manjunath

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-14*

If the applications are using SAML2, you can have a list of all this in a drop down menu in the /adls/ls/idpinitiatedsignon.aspx page (it is disbaled by default since ADFS on Windows Server 2016 but can be re-enabled with Set-ADFSProperties).  

But applications using WS-Federation or OAuth will not show up in this page.
