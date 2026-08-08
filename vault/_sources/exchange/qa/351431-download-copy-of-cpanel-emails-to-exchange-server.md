---
title: "Download copy of cpanel emails to Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351431/download-copy-of-cpanel-emails-to-exchange-server
question_id: 351431
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Download copy of cpanel emails to Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351431/download-copy-of-cpanel-emails-to-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have my domain emails at cpanel.    

I deployed a local Exchange server. I want to download a copy of cpanel emails to Exchange server, so that inhouse users can send/receive emails directly from exchange server.    

What is the possible solution to achieve this?    

    

Thanks,    

Anees

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-17*

As far as downloading the emails are concerned, above given could be the solution but how exchange users can send email?  

Is it even possible to send emails if cPanel is the primary server and we need to send emails through local exchange server?

]1

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-12*

Hi Anees,    

Sorry I am not very familiar with the cpanel email server.    

To my knowledge, you may need to export the emails via cpanel and use some third-party tools to convert the file format (supposed to be MBOX file format) to pst.    

Then you may import the pst file to users' mailboxes via Exchange Admin Center or via Outlook.    

If you are using the Exchange Admin Center, the account you are using requires to be assigned the "Mailbox Import Export" role.    

If the users are using Outlook and imap to connect to cpanel server, I suppose that exporting the emails to pst files via Outlook and importing the pst files to their mailboxes on the Exchange server would also be a solution.    

Here are some links on this topic for your reference:     

How do I Export All Emails from cPanel Email to Outlook PST format?     

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)    

Procedures for mailbox imports from .pst files in Exchange Server    

Back up your email    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
