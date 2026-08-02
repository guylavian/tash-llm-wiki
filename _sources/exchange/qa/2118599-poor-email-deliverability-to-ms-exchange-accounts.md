---
title: "Poor Email deliverability to MS-Exchange accounts / emails wrongly classified as spam"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118599/poor-email-deliverability-to-ms-exchange-accounts
question_id: 2118599
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Poor Email deliverability to MS-Exchange accounts / emails wrongly classified as spam

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118599/poor-email-deliverability-to-ms-exchange-accounts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our web platform sends transactional emails to Microsoft exchange accounts. We have an issue that these emails are being flagged as spam. It is critical to our business success that these emails get delivered. We need to understand MS Exchange Anti-Spam policies or be able to have our business whitelisted! 

Some context:

-  kind of email: buyers inviting suppliers to collaborate

-  dedicated sender IP

-  SpamAssassin score of -2.2, Barracuda score of 0

-  X-Forefront-Antispam-Report (redacted): SCL:5;SRV:;IPV:NLI;SFV:SPM;;CAT:SPM;SFS:(13230040)(29132699027)(8096899003)(136100200026)

Thank you in advance!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-14*

Hi, @Daniel Häberle

The answers above are all good explanations.

I'll just add a little more.

To improve the security of messages, Microsoft has been enhancing the accuracy of spam detection. Microsoft Exchange uses a combination of connection filtering, content filtering, outbound spam handling, and more to prevent spam.

You can learn more about anti-spam here Anti-spam protection - Microsoft Defender for Office 365 | Microsoft Learn

Your X-Forefront-Antispam-Report shows an SCL of 5, indicating that the email is considered spam. You can try this Use mail flow rules to the SCL in messages in Exchange Online | Microsoft Learn

Although both SpamAssassin and Barracuda believe that your message is not spam, Microsoft Exchange's anti-spam policy may mark it as spam based on other factors.

There are a few things you can do to reduce the likelihood of being identified as spam:

1.Don't just insert large images. Don't insert "IP-address only" links. Make it easy to unsubscribe or opt-out, or users will simply press the "spam" button and affect your reputation.

2.Choose a good SMTP server to avoid the IP address being often blacklisted by other providers.

3.Use SPF and DKIM.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-11-13*

Hi Daniel!

From what I understand, you use a non-Microsoft platform to send commercial emails to other providers and are being blocked on Exchange Online servers. I would say that this is completely normal, since the AntiSpam service will block any suspicious email and it does not depend on you, but on the client that will receive this email. It certainly will not lower the security level.

What you could do in this case would be to try to send more assertive emails to users, trying to avoid the issues that identify them as commercial contacts or spam.

Here are some tips to avoid lowering your domains' reputation:

-  Only contact recipients who authorize sending  

-  Make the process of unsubscribing easy for those who no longer wish to receive your emails  

-  Create forms for customers to request to receive emails  

-  Avoid using free domains  

-  In the case of sending mass emails, use an email platform suitable for this  

-  Avoid sending excessive emails  

-  Try to clean your mailing list regularly

These are some tips that can be useful in your day-to-day life to try to reduce the risk of being blocked by spam services.

Best!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-13*

From your side ensure you have DKIM, SPF and the DMARC correctly setup:

https://learn.microsoft.com/en-us/defender-office-365/email-authentication-about

If those are all valid, then that is all you can do really. The recipients can still choose to mark your messages as spam if they choose. If the recipient admins want to allow these then they can or allow in the Tenant Allow List:

https://learn.microsoft.com/en-us/defender-office-365/create-safe-sender-lists-in-office-365
