---
title: "Setting up SMTP Authentication on Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188729/setting-up-smtp-authentication-on-exchange-2019
question_id: 2188729
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Setting up SMTP Authentication on Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188729/setting-up-smtp-authentication-on-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in need of a little help with enabling SMTP authentication with Exchange 2019.  

I am using the guide at this link
https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-authenticated-smtp?view=exchserver-2019

However, when I execute this command
$TLSCertName = "<I>$($TLSCert.Issuer)<S>$($TLSCert.Subject)"

I receive this error"Microsoft.Exchange.Data.SmtpX509Identifier". Error: ""<I><S>" isn't a valid Certificate Identifier."+ CategoryInfo : InvalidData: ) [Set-ReceiveConnector], ParameterBindin...mationException+ FullyQualifiedErrorId : ParameterArgumentTransformationError,Set-ReceiveConnector+ PSComputerName : mail.mydomain.us
I have tried executing each command separately as they do in the guide above. I have also created a script with the three commands.I am of course using the thumbprint of my own certificate.Thank You

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-26*

Hello Kevin Watkins1，

Thank you for posting on the Microsoft Community Forums.

Based on the description, I understand that your issue is related to Microsoft Authenticator and Exchange 2019.

Since there are no engineers dedicated to Microsoft Authenticator and Exchange 2019. In order to be able to deal with your questions quickly and efficiently, I recommend that you repost your questions in the Q&A forum, where there will be dedicated engineers to provide you with professional and effective responses.

Here is the link to the Q&A forum: https://learn.microsoft.com/en-us/answers/questions/

Have a good day.

Best regards,

Lei
