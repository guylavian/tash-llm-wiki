---
title: "Internal E-Mails landing in Exchange 365 mailbox instead of external mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1040682/internal-e-mails-landing-in-exchange-365-mailbox-i
question_id: 1040682
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Internal E-Mails landing in Exchange 365 mailbox instead of external mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1040682/internal-e-mails-landing-in-exchange-365-mailbox-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

we have the following problem.    

We have installed a domain example.com with the InternalRelay setting, because we want to use an external hosters mailboxes. Strato.de    

For a certain user, when an internal user sends a mail from usera@ssss  .com to the user userb@ssss  .com, the mails are landing in the exchange 365 mailbox instead of the Strato mailbox.    

External emails are correctly landing in the Strato mailbox.    

For Strato we have set the Mailsettings to:    

No SPF rules    

"v=spf1 include:spf.protection.outlook.com redirect=_spf.strato.com"    

EDIT:    

The MX Record on Strato is set to the Strato Mailserver.    

smtpin.rzone.de 81.1xx.1xx.9x    

smtpin.rzone.de 2axx:2x:x2xx:2xx:5xx0::1097    

I added the domain in the 365 admin center, set most DNS settings as advised and got it in.    

There are no other configurations that I know of or can see, aside from the "Internal Relay" setting that I used in the Exchange Admin panel.    

Two DNS settings are different, than what microsoft wants me to have:    

TXT expected    

v=spf1 include:spf.protection.outlook.com -all    

vs what I have    

v=spf1 include:spf.protection.outlook.com redirect=_spf.strato.com    

MS expected    

example-com0e.mail.protection.outlook.com    

vs what I have    

smtpin.rzone.de    

We have no connectors of any kind defined right now.    

EDIT2:    

For now, we have made a forward from Strato to the exchange mailbox via the onmicrosoft alias and the users now uses the exchange mailbox instead.    

However that's only a current fix, until we know how to get it to work via the Strato mailbox.    

Which additional information do you need?    

Which settings could we search for, that could explain this behaviour?    

Greetings    

Timm

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-11*

Hi @Timm Beckmann   ,    

Can you tell us how did you configure Mx record and your accept domain?    

Did you create a connector to relay emails to your own Strato server?     

     

Please refer to the following links to configurate your accept domain and connector to see if it works：    

Manage accepted domains in Exchange Online | Microsoft Learn    

Set up connectors to route mail between Microsoft 365 or Office 365 and your own email servers | Microsoft Learn     

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
