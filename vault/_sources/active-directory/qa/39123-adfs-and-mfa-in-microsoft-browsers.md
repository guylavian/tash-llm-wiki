---
title: "ADFS and MFA in Microsoft Browsers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/39123/adfs-and-mfa-in-microsoft-browsers
question_id: 39123
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS and MFA in Microsoft Browsers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/39123/adfs-and-mfa-in-microsoft-browsers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I'm after some help or suggestions as to what could be causing some odd behaviour in ADFS. A little background first. We have 2 WAP severs sitting in front of 2 ADFS servers which cal on 2 third party MFA severs, in our case Securenvoy.   

I'm using a per relying party trust for testing purposes and getting for following behaviour. When I hit the URL using Chrome I can authenticate and get the token prompt successfully after the initial username and password prompmt as expected. However if I use IE (and version) or Edge, instead of the token prompt I immediately get an error page after the initial username and password:  

For security reasons, we require additional information to verify your account  

An error occurred   

An error occurred. Contact your administrator for more information.   

Has anyone come across anything similar before? I am assuming there is some option or setting in either WAP or ADFS that isn't set correctly but I just can't see anything obvious.

## Answers

_No answers on this thread._
