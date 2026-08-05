---
title: "[Migrated from MSDN Exchange Dev] Server busy. Please try again later (S77714)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/174866/migrated-from-msdn-exchange-dev-server-busy-please
question_id: 174866
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Server busy. Please try again later (S77714)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/174866/migrated-from-msdn-exchange-dev-server-busy-please (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/9c11eec2-78d8-4d8c-abec-375b1e1c5768/server-busy-please-try-again-later-s77714?forum=exchangesvrdevelopment  

Hi, we're an email service provider and have recently changed the IP address of one of our servers. This appears to have resulted in many emails being deferred such as this:  

9631D173B8F5A  198276 Tue Nov 24 08:48:36  AAEVbZ4L2SLa1WIuIyBmdng==_1101345894578_GGSWUN9MEeKL+NSuUoRDcg==@in.constantcontact.com  

(host company-com.mail.protection.outlook.com[104...] said: 452 4.5.3 Too many recipients (AS780090) [.protection.outlook.com] (in reply to RCPT TO command))  

                                         ******@company1.com

This email was also originally destined for a local user on our system, but they have chosen to forward it on to their own company domain managed by Outlook/Office 365.  

How can I request my IP to be whitelisted or at least verified in some way that we're not trying to spam someone?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-25*

Hi,    

Are you sending to large number of recipients? It seems the amount of recipients for a single email has exceeded the limit. Try combining those recipients to a group and sending to that group directly instead.    

If you are Not sending to large number of recipients, you might need to set up a rule for whitelist your domain/IP, follow this blog please: https://infimasec.com/support/o365-whitelist/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
