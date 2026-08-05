---
title: "Exchange 2016 OWA Appointment Invitation link IMAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365600/exchange-2016-owa-appointment-invitation-link-imap
question_id: 365600
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 OWA Appointment Invitation link IMAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365600/exchange-2016-owa-appointment-invitation-link-imap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!    

We´re right in the move from Exchange 2010 (on prem) to Exchange 2016 (on  prem) and I observed the following behavior:    

If an account (migrated to 2016) receives an appointment invitation / meeting request and this account is connected to the exchange 2016 server via IMAP, it will receive a link to OWA (we´ve  set it to OWA´s InternetURL). When the user clicks on the link, OWA opens, he logs in and then he gets the message “The action couldn´t be completed. The Item wasn´t found”    

If the receiving account is on Exchange 2010, the link of course looks different and works works without problems.    

Any Ideas?    

I´m talking of OnPremise Installations, there is no Office365 in place. I was aware of that PowerShell cmd-let and we don´t want our IMAP Users to get meeting invitations in iCal-Format, we want them to confirm meetings using OWA / OutlookOnTheWeb. In Exchange 2010 this worked as expected.    

Output from Get-CasMailbox shows the correct URLs, FQDNs of our Exchange environment.    

Internal: https://FQDN/owa    

External: https://FQDN/owa    

The Meeting is initiated from one Exchange 2016 user (User1) and sent to another Exchange 2016 user (User2) on the same ExchangeForest/Domain. When User2 connects to his Mailbox using IMAP Protocol (p.e. using Thunderbird or Outlook using IMAP), the invitation contains a Link to the invitation in OWA (when the option InternetURL ist set in Set-ImapSettings..., see below). When the "receiving" User (User2) is on Exchange 2010 (same Forest/Domain), the invitation Link is correct and he is able to confirm the meeting in OWA 2010, when User2 is on Exchange 2016, the Link seem to be wrong,  he logs in and then he gets the message “The action couldn´t be completed. The Item wasn´t found”    

    

regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-28*

Hi,  

thanks for your reply. Since time goes by, we finished our Migration from 2010 to 2016 (all on prem, no 365) successfully, but the Invitation Link-Problem still exists.  

I knew, that switching to iCal for IMAP and POP solves the Link-problem, because the invitation is sent as iCal-Attachment. But it has a big disadvantage: Confirmations for invitations are saved outside Exchange, when using Thunderbird or Outlook connecting to Exchange 2016 using IMAP and setting the switch to send iCAL invitations (Set-CASMailbox –identity <NAME> –PopUseProtocolDefaults:$FALSE –ImapUseProtocolDefaults:$FALSE –PopForceICalForCalendarRetrievalOption:$TRUE –ImapForceICalForCalendarRetrievalOption:$TRUE). The confirmation (and calendar item) for this invitation is save in Thunderbird´s local Calendar or Outlook´s local Calendar in a .pst file.  

To nail it down once more:  

The Meeting is initiated from one Exchange 2016 user (User1 using OWA) and sent to another Exchange 2016 user (User2 using IMAP) on the same ExchangeForest/Domain.   

When User2 connects to his Mailbox (using IMAP Protocol p.e. using Thunderbird or Outlook using IMAP), the invitation contains a Link to the invitation in OWA (see below). When User2 klicks this link to confirm the invitation, he logs into OWA and then he gets the message “The action couldn´t be completed. The Item wasn´t found”. The user has to switch to his Inbox-Folder in OWA, then he sees the invitation mail to confirm it…   

Example for Invitation Mail:  

Microsoft Outlook Web Access: https://mail.domain.com/owa?itemid=AAMkADRlZjJkZDEBLABNLABLAmE2LWZiZjE4Zjk2NjFiZQBGAAAAAADGj6Vx5dyBQYzpnJMrfOcIBwCn6YwrqJhtQbR%2B1b3JWyVwAAAAmobWAADVGCO8mKjfRrhvh56ZtzjbAAC4BhGyAAA%3D&exvsurl=1&path=/calendar/item  

To receive meeting invitations as .iCalendar attachments instead of Outlook Web App links, go to https://mail.domain.com/owa?path=/options/popandimap and select Send meeting invitations in iCalendar format.  

regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-27*

Hi,    

Does the issue only exist when the sender using Office 365 to send the invitation?     

If yes, I'm afraid the following command is the correct solution:    

```
Set-CASMailbox –identity  –PopUseProtocolDefaults:$FALSE –ImapUseProtocolDefaults:$FALSE –PopForceICalForCalendarRetrievalOption:$TRUE –ImapForceICalForCalendarRetrievalOption:$TRUE
```

As you may know, Office 365 supports a number of different client protocols, including POP and IMAP and a variety of POP and IMAP clients. By default, POP or IMAP clients will be configured to use Outlook Web App (OWA) for handling calendar invitations. When these clients receive a meeting request, within the body of the invite is a link. Clicking on the link allows the user to open their mailbox via OWA so they can accept or decline the request.    

The link you cover in the picture, is it mail.domain.com? Which server does mail.domain.com point to in your DNS? It should be pointing to Ex2016 as higher version of Exchange can handle all request, while lower version can't.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
