---
title: "Having Error of \"550 5.1.10\" in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2147322/having-error-of-550-5-1-10-in-exchange-online
question_id: 2147322
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Having Error of "550 5.1.10" in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2147322/having-error-of-550-5-1-10-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm having an error while sending emails to other domains and am also unable to receive some emails,  

after sending an email a bounce back email will appear by Microsoft having an error of "550 5.1.10" in Exchange Online, however, the recipient email is working fine and also receiving emails from others.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-16*

Hi,@GD

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you are unable to receive and send external emails.

I need to consult you on a few things:

1.Is it possible to send and receive email properly within your organization?

2.Have you tried using OWA to send emails?

3.What is the error message returned when an external mailbox fails to send you an email?

Here are my suggestions:

1.If you are an administrator, check to see if the user has a license.

2.Use Mail Flow to view specific information about email delivery failures.

3.If it's only for a specific external domain, there may be a problem with your Exchange Online's acceptance domain.

4.If you have a custom domain (for example, contoso.com instead of contoso.onmicrosoft.com), it's possible that your domain's MX record isn't configured correctly.

You can refer to this link for the exact method:https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/ndr/fix-error-code-550-5-1-10-in-exchange-online

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-15*

There might be few reasons since you're facing this issue. You can try below ways- 

-  Check the user’s email and make sure that the email address is written correctly and with no spaces or special characters.

-  You can also try to resend the message by clicking on the Send Again button in Outlook.

-  Another thing to do is send a new message to the email address. This will ensure that there is no issue with the content of the message. To ensure that there isn’t a cached email address that could be malformed, send an email to the user by typing the entire email address manually. The last thing to check if any rules are configured in the mailbox. If any, disable them until a test is done.

-  If the above ways fail, you need to look at the Exchange Server Setup for any forwarding rules set on the server. For this you can refer - https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/ndr/fix-error-code-550-5-1-10-in-exchange-online

Let me know if you have any query.
