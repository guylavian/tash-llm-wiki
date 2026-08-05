---
title: "IMAP setup and Exchange SMTP default self-signed certificate overwrite"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1153116/imap-setup-and-exchange-smtp-default-self-signed-c
question_id: 1153116
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# IMAP setup and Exchange SMTP default self-signed certificate overwrite

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1153116/imap-setup-and-exchange-smtp-default-self-signed-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, as an EAS "backup" connectivity protocol I need to enable IMAP for my user's mobile devices. Lately I have some problems with EAS and MS support is digging into them. In the meanwhile I want to give a reliable and working alternative to my users.    

The official procedure (https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-imap4?view=exchserver-2016) consists of:    

-  to enable imap services    

-  set imap settings (fqdn and connectivity bindings/protocols)    

-  Configure the authenticated SMTP settings for internal and external clients since, when you enable imap to read emails, you must also provide a valid smtp server to be able to send emails as well. Unless you have some 3rd party smtp server to relay on (your ISP for example). This step consists of overwriting the default Exchange self-signed certificate.    

The fact is that by reading technical articles (for example https://blog.rmilne.ca/2021/04/26/should-i-overwrite-the-default-exchange-smtp-certificate/ - ), they state that the default self-signed smtp exchange certificate should not be overwritten. . My guess is that I should replace the default Exchange self-signed certificate for my goal, otherwise the subject name in the certificate does not match the dns name set in the imap settings.     

But I am concerned about the fact that the default Exchange self-signed certificate is also used to encrypt SMTP communication between internal Exchange servers.     

Is not that, by repalcing the default Exchange self-signed certificate, something gets broken? Is the official MS procedure linked above safe or is there something that should I be made aware of before continuing on this way?    

Thank you,    

Francesco

## Answers

_No answers on this thread._
