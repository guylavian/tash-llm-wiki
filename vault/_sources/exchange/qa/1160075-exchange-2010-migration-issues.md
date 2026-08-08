---
title: "Exchange 2010 migration issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160075/exchange-2010-migration-issues
question_id: 1160075
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 migration issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160075/exchange-2010-migration-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to migrate to o365 the remaining local mailboxes on an old Exchange 2010 hybrid server, facing a number of issues

First, when I try doing it in the mgmt console it says, "Add a remote forest to the Exchange management console root node"

I've looked at articles that talk about this, I don't recall ever seeing the 0365 org connected in the local mgmt console on this or other ex2010 server, but migrations have happened in the past.

I then tried to do it from PS, first got error "Target user ‎'User‎' already has a primary mailbox.'. - OK so I cleared the AD attributes homeMDB and homeMTA and tried again. Now got this error

 "You must specify the RemoteOrganizationName parameter.   - Not certain what this should be but made it the same as the 'RemoteHostName' parameter for now.

Now it comes up with this errror

What's my best course of action here, should I proceed with 'Adding the Echange forest to console root' as the GUI migration error suggested?  are there any other pitfalls to doing this?

Note, this customer on-prem server is also configued to route mail via our DNS mail domain such as 'webmail.customer.ourorg.com.  The certificate bound on the on-prem server root domain belongs to our org, not theirs. I don't know if this is affecting it, but it's a thing still.  Eventually we are planning to decom this server, so I don't want to reinvent the mail routing at this stage preferably.

Sorry if any of this sounds off, I am not especially familiar with any of this

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-19*

Further, the connection to smtp.office365.com:587 is working, are all those ports really required if I can get to the service url?

No IT network team wants to open their firewalls to 1/2 the internet subnets that those MS service address documents refer to.  This server has been working as an Exchange server for nearly two decades and been connected to O365 Hybrid for many years, would a firewall issue not have presented before now?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-18*

I'll check those url are whitelisted, but the server is working otherwise doing it email thing.

I was looking at this article as this is the error I am getting but the string mentioned "DataImportTimeout" does not exist in the file 'MSExchangeMailboxReplication.exe.config'

[https://learn.microsoft.com/en-au/archive/blogs/asiasupp/when-you-attempt-to-move-mailbox-fromto-exchange-online-you-receive-the-error-the-call-to-microsoft-exchange-mailboxreplicationservice-timed-out

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-17*

Hi @Bob Pants  

Please make sure you have whitelisted the Microsoft IP addresses in your company firewall.

If you follow this link to use migration batches to move mailboxes, would it succeed?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-12*

Is TLS 1.2 enabled on the 2010 Exchange Servers?

[https://jaapwesselius.com/2018/10/05/exchange-2010-and-tls-1-2/

I have never had to use the RemoteOrganizationName

In fact this says its not needed:

[https://learn.microsoft.com/en-us/powershell/module/exchange/new-moverequest?view=exchange-ps

The RemoteHostName is the FQDN of the local on-prem Exchange Server if you are moving a mailbox to 365. 

and you should not be clearing anything in the attributes  :)

You can use this guide:

[https://www.alitajran.com/move-mailbox-to-exchange-online-with-powershell/
