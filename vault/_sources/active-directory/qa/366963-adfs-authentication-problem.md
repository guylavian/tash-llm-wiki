---
title: "ADFS authentication problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/366963/adfs-authentication-problem
question_id: 366963
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS authentication problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/366963/adfs-authentication-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two environment of ADFS. One is sts.Employee.abc.com for our internal employee and second is sts.Partners.xyz.com for our external partner. AD domain are different for the both the environment. For example our local employee are in abc.com and for partner AD it is xyz.com.  

We have added trusted party MS in both environment for share point and other access. Recently, I saw that some of the share point for our partner portal is going through our local ADFS one sts.Employee.abc.com while, it should go through sts.Partnes.xyz.com. I do not know what is causing this issue. please help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-01*

Thank you very much. yeah , this was share point issue and they fixed it.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-25*

Is there a trust between the two ADFS farms? Like one farm is a Claim Provider trust for the other one? If so, you will need to share more config about this trust.  

If there is no trust between the two ADFS farms, then it's a SharePoint Configuration thing. And we would need to add some SharePoint tags to the question.
