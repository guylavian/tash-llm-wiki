---
title: "AD CS Web Enrollment: Invalid pointer 0x80004003 (-2147467261 E_POINTER)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1471099/ad-cs-web-enrollment-invalid-pointer-0x80004003-21
question_id: 1471099
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# AD CS Web Enrollment: Invalid pointer 0x80004003 (-2147467261 E_POINTER)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1471099/ad-cs-web-enrollment-invalid-pointer-0x80004003-21 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Windows 2019 server set up as a CA in my environment. It's tied to my DC. I have IIS installed and certificate web enrollment is in use. I can browse to my https://CA/certsrv no problem. The websites certificate is valid and trusted. I can log in with AD credentials for a test user I'm using.  

When I log into certsrv as the test user, and attempt to request a new user certificate, the following issues are present:

-  My custom "Domain Users" template is not visible. That's probably the biggest issue right now.

-  I am unable to choose a key-bit length (such as 2048) with the default user template.

-  I try to submit a request anyway and receive the following error:  

Your request failed. An error occurred while the server was processing your request.

Contact your administrator for further assistance.

Request Mode:newreq NN - New Request (keygen)

Disposition:(never set)

Disposition message:(none)

__Result:__Invalid pointer 0x80004003 (-2147467261 E_POINTER)

__COM Error Info:__CCertRequest::Submit: Invalid pointer 0x80004003 (-2147467261 E_POINTER)

__LastStatus:__The operation completed successfully. 0x0 (WIN32: 0)__Suggested Cause:__No suggestions.

Please advise, and thank you for being generous with your time.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-12*

looks like they are ignoring this
