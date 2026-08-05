---
title: "On premise Exchange SPF/DKIM authentication - google saying I don't got it"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1517606/on-premise-exchange-spf-dkim-authentication-google
question_id: 1517606
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# On premise Exchange SPF/DKIM authentication - google saying I don't got it

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1517606/on-premise-exchange-spf-dkim-authentication-google (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019.
I have SPF and DKIM enabled on my microsoft admin portal.
Google is still saying I don't have those authentications enabled.
I have owa.contoso.com as my email domain and is my custom domain in the microsoft portal. I do not have just contoso.com as a domain on my admin portal.
This is the message I get from google:
mx.google.com gave this error:  

This mail has been blocked because the sender is unauthenticated. Gmail requires all senders to authenticate with either SPF or DKIM. Authentication results: DKIM = did not pass SPF [contoso.com] with ip: [ipv4] = did not pass For instructions on setting up authentication,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-30*

Hi @Susan Dodds  

Do you have an Exchange hybrid deployment and all outbound emails are routed through Exchange Online to internet?

I have owa.contoso.com as my email domain and is my custom domain in the microsoft portal. I do not have just contoso.com as a domain on my admin portal.

According to the NDR message from Google, your email domain is contoso.com.

Have you enabled DKIM for contoso.com following this link?

Use DKIM to validate outbound email sent from your custom domain

Do you have your on-premises Exchange server's ip address in the SPF record?

Set up SPF to help prevent spoofing

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
