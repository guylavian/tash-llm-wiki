---
title: "SMTP: Connector Exchange on Sharp printer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2084395/smtp-connector-exchange-on-sharp-printer
question_id: 2084395
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SMTP: Connector Exchange on Sharp printer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2084395/smtp-connector-exchange-on-sharp-printer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,I am having a problem sending e-mail from the "Scan to e-mail" function of several customers' photocopiers, but I have complied with the recommendations of the Microsoft article that recommends:Create an Exchange SMTP connector with the company's public IP address.Configuring the photocopier with the MX server of the Office 365 holder.Setting port 25, activating SSL/TLS and disabling SMTP authentication.Entering the correct SPF/TXT value on the DNS provider with the ip4:202.22.X.X.XLThe photocopier indicates that the connection to the SMTP server is functional, but when I send e-mail to an address that is part of the Office 365 holder, the Sharp MX-C304W photocopier generates an "80-0000" error that corresponds to an authentication error, or a wrong identifier.

Has anyone ever encountered this error?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-01*

Hello, thank you for your response. I have already configured the connector as it is written in the procedure and it worked. It is only for 2 weeks that it no longer works while I have not changed the configuration.I specify that I do it for several printers and it worked

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-01*

Hi，@Vincent Heidelberger

Thank you for connecting with us in Microsoft community.

Based on your description, you seem to be using Option 3.

Do you have to send emails to external recipients? If not, it is recommended that you choose option 2 for easier implementation.

You can refer to this link for details:https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?source=recommendations#option-2-send-mail-directly-from-your-printer-or-application-to-microsoft-365-or-office-365-direct-send

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
