---
title: "Changes to Exchange SMTP Relay"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380039/changes-to-exchange-smtp-relay
question_id: 380039
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Changes to Exchange SMTP Relay

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380039/changes-to-exchange-smtp-relay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My business uses MS Exchange SMTP Relay to send payslips to our employees from an old payroll application.    

Specifically this is what we have used https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365#option-3-configure-a-connector-to-send-mail-using-microsoft-365-or-office-365-smtp-relay    

We have been using this happily for several years, but as of this week it has stopped working.    

The payroll software reports: Message 550 5.7.1 Service Unavailable.    

I have checked and our public IP address has not changed.    

Has MS changed the settings? What do we need to do to get this working again?    

Thanks for any help.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-03*

Two other possibilities:

-   Your sending IP is o the 365 blocklist:  

    https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/non-delivery-reports-in-exchange-online/fix-error-code-550-5-7-1-in-exchange-online#the-sender-is-external-and-their-source-ip-address-is-on-microsofts-blocklist

To Fix;

5.7.1 Service unavailable; Client host [xxx.xxx.xxx.xxx] blocked using Blocklist 1; To request removal from this list please forward this message to ******@messaging.microsoft.com

To remove the restriction on the sender's source email system, forward the NDR message to ******@messaging.microsoft.com.

OR:  

Your firewall is blocking the outbound connection

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

Thanks Eric for the suggestion.  

The results from Office 365 Anti-Spam IP Delist Portal is  

"The IP address in question is not currently blocked in our system. "

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Thanks Eric for your suggestions.    

I have tried the Connectivity Test.    

The results show everything is OK.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Agreed with Andy, you can try removing the domain from Microsoft 365 and re-add it back: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain?view=o365-worldwide    

Have test with EXRCA -Office 365 Exchange Domain Name Server (DNS) Connectivity Testto check the DNS, post the results back with personal information covered: https://testconnectivity.microsoft.com/tests/O365ExchangeDns/input    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-03*

Thanks for your help, but I do not think that TLS levels is the problem.  

We are using Office 365 SMTP relay (Option 3) BECAUSE our device does not support TLS.  

To quote from above "If your device or application does not support TLS 1.2 or above Use direct send (Option 2) or Microsoft 365 or Office 365 SMTP relay (Option 3) for sending mail instead"  

I am sure that there much be some other reason that our emails have stopped sending.
