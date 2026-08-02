---
title: "I am trying to send emails to bigpond email addresses and I am getting error message that states my sender score is too low"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4684354/i-am-trying-to-send-emails-to-bigpond-email-addres
question_id: 4684354
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# I am trying to send emails to bigpond email addresses and I am getting error message that states my sender score is too low

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4684354/i-am-trying-to-send-emails-to-bigpond-email-addres (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It has given me this error message. I have taken out some of the information that is personal. This has happened with multiple BigPond email addresses and with multiple senders within out workplace.

Your message wasn't delivered. Despite repeated attempts to deliver your message, a connection to the remote server couldn't be made.

Contact the recipient by some other means (by phone, for example) and ask them to tell their email admin that it appears that your email system is unable to connecto their email system. Give them the error details shown below. It's likely that the recipient's email admin is the only one who can fix this problem.

For more information and tips to fix this issue see this article: https://go.microsoft.com/fwlink/?LinkId=389361.  

Diagnostic information for administrators:

Generating server: **********************************************************  

Receiving server: **********************************************************

6/13/2024 1:19:40 AM - Server at **********************************************************returned '550 5.4.317 Message expired, cannot connect to remote server(450-4.4.317 Cannot connect to remote server [Message=550-5.7.0 Connection refused - IB116. 40.107.107.122 Senderscore too low.

PII Removed.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-14*

Hello Patrick Nelson1,

Thank you for posting this case in Microsoft Community!

Based on your description: You are trying to send emails to bigpond email addresses and getting error message that states your sender score is too low. I would like to cooperate with you working on this case. To clarify this case, are you using Microsoft 365 or Business account? As further checked your NDR message, your emails could not be sent to bigpond mail side because the remote server not reached. For my suggestion, you may check this article Fix NDR error "550 4.4.7" in Exchange Online to fix this case. Here are the steps you may try to perform further as admin:

-  Solution 1: The MX record for your domain might be missing or incorrect. Get more information about how MX records work at DNS basics.

-  Solution 2: Test your MX record and your organization's ability to send mail by using the Outbound SMTP Email test in the Microsoft Remote Connectivity Analyzer.

-  Solution 3: Your domain might have expired due to non-payment. Verify with your domain registrar that your domain is active and not expired.

By the way, if you are using Microsoft Exchange online and sender score is showing too low, to make sure your organization could send emails to bigpond mail side normally, please also set up SPF, DKIM, DMARC for email authentication completely. You may check following article as reference:

Set up SPF to help prevent spoofing

Set up DKIM to sign mail from your Microsoft 365 domain

Set up DMARC to validate the From address domain for senders in Microsoft 365

Hope the above workaround would be helpful. If you need further assistance, please feel free to let me know, I will keep assisting you.

Your understanding and patience will be appreciated.

Thank you!
