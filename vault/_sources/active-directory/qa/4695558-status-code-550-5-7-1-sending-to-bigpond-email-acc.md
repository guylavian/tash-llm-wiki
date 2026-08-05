---
title: "Status code: 550 5.7.1 sending to bigpond email account with email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4695558/status-code-550-5-7-1-sending-to-bigpond-email-acc
question_id: 4695558
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# Status code: 550 5.7.1 sending to bigpond email account with email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4695558/status-code-550-5-7-1-sending-to-bigpond-email-acc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I cant send emails from my microsoft email account to any bigpond email acccounts.

thank you

More Info for Email Admins

Status code: 550 5.7.1  <br>  <br>This error occurs when the recipient's domain has security or policy settings that reject the sender's message. However, we were unable to determine the specific setting that's causing this rejection. Usually the error is reported by an email server outside of Office 365. Common issues include the following: the receiving server suspects the message is malicious or spam; the Sender Policy Framework (SPF) record for ****.com is incorrectly configured or doesn't exist;

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-03*

Hi david coulter1

Greetings!

Thank you for posting on Microsoft Community!

Based on your description, I understand you are unable to send emails to any bigpond email account and NDR's status code 550 5.7.1.

There are many possible causes to this issue, so you may kindly try below troubleshooting steps in:

-  Check instructions in: Fix NDR error 550 5.7.1 in Exchange Online - Exchange | Microsoft Learn.

-  According to the error message, your email messages were rejected due to the recipient's domain security or policy settings. So please make sure you followed the steps in Add or edit an SPF TXT record to help prevent email spam (Outlook, Exchange Online) to set up and validate your SPF record correctly.    (Please note: There are spoofing techniques that SPF cannot protect against. To protect against them, you should also set up DKIM and DMARC for Microsoft 365. Kindly check Use DKIM to validate outbound email sent from your domain in Microsoft 365 and Use DMARC to validate email in Microsoft 365.)

If the above methods failed to you, we highly recommend you contact Microsoft Online Technical support team directly. Unlike our forum team, this team has higher permission and would be able to access into the backend and check it for you.  Please refer to: Get support - Microsoft 365 admin | Microsoft Learn.

Appreciate your patience and understanding and thank you for your time and cooperation. Have a nice day!

Sincerely,

Connery You
