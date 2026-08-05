---
title: "Adding customers back into Exchange after they were created in Office 365 using ADSIEdit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150025/adding-customers-back-into-exchange-after-they-wer
question_id: 150025
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Adding customers back into Exchange after they were created in Office 365 using ADSIEdit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150025/adding-customers-back-into-exchange-after-they-wer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a hybrid Office 365 setup, with a local Exchange 2010 server which is now used solely for configuring mailboxes.  

Before now however, it was understood that managing mailboxes (including creating new mailboxes) could be correctly carried out using ADSIEdit.  

Since then we've discovered this isn't the supported method and we've started creating mailboxes using the exchange server instead.  

We are now left however, with several users who aren't listed as a remote mailbox in exchange even though they do have a mailbox in Office 365 and of course do have an object in AD.  

The question is, is there a way to make them appear in the list of remote mailboxes? And can that be done without any risk to the existing Office 265 mailboxes?  

Thanks - Lawrence

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hi @Lawrence Marigold | Telitec  

Agree with the reply above from Andy, make sure you have taken the right methods to create an o365 mailbox in Exchange hybrid environment: Creating an Office 365 Mailbox in a Hybrid Configuration

1.Using EAC ( 2013 and later version ) : Recipients > Mailboxes > new “Office 365 mailbox.” Sync the directory using AD Connect, License the User  

2.Using EMS ( 2010 and later version ) : Enable-RemoteMailbox -identity “Tom”- –RemoteRoutingAddress Tom@keyman  .mail.onmicrosoft.com.

For your question above, some users are not listed as a remote mailbox, if a Remote Mailbox isn’t present or has been accidentally deleted, you can create one and link it up to the Office 365 mailbox. Like this link introduces: Remote Mailboxes in Exchange Hybrid configuration

```
Enable-RemoteMailbox username –RemoteRoutingAddress ******@domain.mail.onmicrosoft.com  
Get-Mailbox –Identity emailaddress | fl Identity,ExchangeGUID  
Set-RemoteMailbox username –ExchangeGUID 8e992097-24c1-432c-8a89-98e3c7a7d283
```

In addition, Exchange 2010 reached its end of support on October 13, 2020. It's better for you to upgrade your Exchange 2010 hybrid to 2016 hybrid.  

Detailed information here: Exchange 2010 end of support roadmap

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-03*

Sure, you can do that. Simply provision the remote mailbox on-prem. NO risk to the 365 mailbox     

```
Enable-RemoteMailbox -identity  -PrimarySmtpAddress ******@contoso.com -RemoteRoutingAddress ******@contoso.mail.onmicrosoft.com  -Alias 
```

I like to set the alias as well. The RemoteRoutingAddress will be <user>@<yourdomain>.mail.onmicrsoft.com.    

The <user> for the remote routing address can be anything, just has to be unique!     

https://learn.microsoft.com/en-us/powershell/module/exchange/enable-remotemailbox?view=exchange-ps    

If you want, you can also set the ExchangeGUID on the remotemailbox using the ExchangeGUID of the mailbox in Exchange Online, but not required if you dont plan to move the mailbox back on-prem    

https://support.microsoft.com/en-us/help/2956029/migrationpermanentexception-cannot-find-a-recipient-that-has-mailbox-g
