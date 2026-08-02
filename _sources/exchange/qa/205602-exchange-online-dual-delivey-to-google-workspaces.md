---
title: "Exchange Online: Dual delivey to Google Workspaces"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/205602/exchange-online-dual-delivey-to-google-workspaces
question_id: 205602
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online: Dual delivey to Google Workspaces

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/205602/exchange-online-dual-delivey-to-google-workspaces (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

is possible to do a dual delivery from exchange online to google workspace ? I need to keep both systems and main will remain Office365 (mx records doesn't change), but  i need that mail received from some user (at first), must be in the two system. The domain is the same  

have you any advice ?  

thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-22*

Thanks to everyone  i will try asap

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Hi anonymous user    

Agree with the suggestions above from Andy, mail forwarding and transport rule (configured in Exchange online) can be used to meet your need keep mails on both server side.    

You could refer to Option 3: Setup Mailbox Forwarding With PowerShell in this link to get more detailed information: Microsoft Exchange – Forwarding Mail To External Email Addresses    

And the mailflow rule can be set like below:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-21*

Only with "forwarding" from one system to the other and leaving the message in the mailbox.    

From the Exchange Online side, you would need to set each mailbox to forward to the matching google Email address and deliver to the Exchange Online mailbox    

https://learn.microsoft.com/en-us/exchange/recipients/user-mailboxes/email-forwarding?view=exchserver-2019#:~:text=In%20the%20Exchange%20admin%20center%2C%20navigate%20to%20Recipients%20%3E%20Mailboxes.&text=Select%20the%20Deliver%20message%20to,then%20click%20or%20tap%20Save.    

```
Set-Mailbox -Identity "Douglas Kohn" -DeliverToMailboxAndForward $true -ForwardingSMTPAddress "******@fineartschool.net"
```

Alternatively, you could create a transport rule for each mailbox to CC: top google but that would probably be too much to actually manage.     

Thats the only way you could meet the requirement:    

I need to keep both systems and main will remain Office365 (mx records doesn't change), but i need that mail received from some user (at first), must be in the two system.     

As far as the domain sharing,  I dont see how that could be possible since Exchange Online and Google wont be able to share the same namespace.     

(If that is what you are proposing)
