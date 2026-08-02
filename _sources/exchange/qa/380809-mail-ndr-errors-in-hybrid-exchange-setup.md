---
title: "Mail NDR errors in Hybrid Exchange setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380809/mail-ndr-errors-in-hybrid-exchange-setup
question_id: 380809
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Mail NDR errors in Hybrid Exchange setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380809/mail-ndr-errors-in-hybrid-exchange-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All  

i am on project for migrating 2000 mailboxes to Exchange online, i have two Exchange forest environments on premises running Exchange 2013 and 2016 respectively, i am facing a unique problem of NDR these days . scenario is as follows.   

For new joiners i am creating user account in AD(on Premises) and allow it to sync and then create Mailbox on cloud.   

Challenge - existing On premises users are getting NDRs for mails sent to newly created mailboxes on cloud.   

can someone help me to resolve this.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Hi @Royal D Costa      

Agree with the reply above, please make sure you have followed the correct way to create a new o365 mailbox in Exchange hybrid. Several ways available list in the below article: Creating an Office 365 Mailbox in a Hybrid Configuration    

Here is also a related thread discussed the similar issue as yours: There's a problem with the recipient's mailbox. Please try resending the message. If the problem continues, please contact your email admin.    

For this issue we need to check if there are any Internet recipient entry in the domain.     

There was an AD account for which email address was added by mistake. Exchange was unable to deliver and was throwing the error. We remove the email address off the AD account and it got resolved..    

In addition, if you mistakenly have duplicated mailboxes both in Exchange on-prem and online, we will need to follow the guide here to resolve this issue: My user has a mailbox both on-premises and in Exchange Online. Help!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-03*

You probably enabled the mailbox in the cloud only, right?  

Did you run:     Enable-RemoteMailbox "Test User" -RemoteRoutingAddress "******@mydomain.mail.onmicrosoft.com"  ?  

If not, your on-prem Exchange doesn't know where to route the e-mail.
