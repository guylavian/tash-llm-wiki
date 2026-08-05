---
title: "adfs using simultaneously forms aunthentications and certificated authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305017/adfs-using-simultaneously-forms-aunthentications-a
question_id: 1305017
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# adfs using simultaneously forms aunthentications and certificated authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305017/adfs-using-simultaneously-forms-aunthentications-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, how are you?

Within the ADFS service, is it possible to enable the simultaneous authentication of the user, password and certificate ?

When editing the authentication methods at Extranet level, enabling Forms Authentication and Certified Authentication, at the time of validating the login, only requests one or the other.

Greetings.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-14*

Hello Raul,

Thank you for your question and for reaching out with your question today.

In Active Directory Federation Services (ADFS), it is not possible to enable simultaneous authentication of user credentials (username/password) and client certificates out of the box. ADFS supports multiple authentication methods, but it typically follows a fallback mechanism where it tries one authentication method and if it fails, it moves on to the next method.

When you enable both Forms Authentication and Certificate Authentication in ADFS, it will prioritize one method over the other based on the configuration. For example, if Forms Authentication is listed before Certificate Authentication in the authentication methods configuration, it will prompt for username and password first and only fall back to certificate authentication if the user doesn't provide valid credentials. The order of the authentication methods can be modified to change the priority.

To achieve simultaneous authentication of both username/password and client certificate, you would need to customize the ADFS authentication pipeline. This involves creating a custom authentication provider or using third-party solutions that offer this capability. Customization of the ADFS authentication pipeline is an advanced task and requires in-depth knowledge of ADFS and development skills.

If you require simultaneous authentication of user credentials and client certificates, it is recommended to consult with an experienced ADFS specialist or consider using alternative solutions that provide this functionality out of the box.

I used AI provided by ChatGPT to formulate part of this response. I have verified that the information is accurate before sharing it with you.

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
