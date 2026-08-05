---
title: "Send email via Graph and Exchange Online not delivery message : Access denied, traffic not accepted from this IP (5.7.708)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302065/send-email-via-graph-and-exchange-online-not-deliv
question_id: 302065
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Send email via Graph and Exchange Online not delivery message : Access denied, traffic not accepted from this IP (5.7.708)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302065/send-email-via-graph-and-exchange-online-not-deliv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, Everything working fine to send email via Graph by ASP.NET Core 5.0 Application. Big problem, Exchange Online won't delivery the message like title said. I read documentation and follow instructions to get it working, but it is not working. Someone already have problem like that ? Thank you !

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-29*

i have the same problem here

i bought a licence, but it's on "trial" anyway for 30-90 days (tenant rial)

outlook can perfectly send mail, and receive answer too

microsoft graph have thee same error as this title

same source, same destination as outlook

Why is outlook able to send but not microsoft graph api?

(dmarc, dkim and spf are configured)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Hi @Marco Fillion      

Is there any update about your issue? If you still have issue sending emails from your o365 tenant, you may try contacting the o365 support team with below methods    

Ways to contact support for business products - Admin Help    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-07*

Hello AndyDavid,  

Thank you for your answer. Very appreciated.  

I bought this morning the Exchange Online Basic Plan 1.  

How long to be considered safe ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-06*

This isnt a Graph Issue. You are being blocked because Exchange Online doesnt allow email from IPs it considers untrustworthy  

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/non-delivery-reports-in-exchange-online/fix-error-code-5-7-700-through-5-7-750

5.7.708 Access denied, traffic not accepted from this IP: This error occurs when sending email from known, low reputation IP addresses that are typically used by new customers.

5.7.708 Access denied, traffic not accepted from this IP  

This error can happen when you are trying out a Microsoft 365 trial tenant. If you receive this error before you can purchase licenses, contact support to request an exception for the low reputation IP address until you're able to purchase licenses.
