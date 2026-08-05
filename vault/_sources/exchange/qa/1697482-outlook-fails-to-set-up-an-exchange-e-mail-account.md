---
title: "Outlook fails to set up an Exchange e-mail account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1697482/outlook-fails-to-set-up-an-exchange-e-mail-account
question_id: 1697482
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook fails to set up an Exchange e-mail account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1697482/outlook-fails-to-set-up-an-exchange-e-mail-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Outlook fails to set up an Exchange e-mail account. I tried to setup my existing Exchange e-mail account in the Windows desktop version of Outlook. Outlook says "something went wrong...." I don't even get a chance to enter my password I have had an Exchange e-mail account setup in Outlook for years with no problems.  

The Microsoft Community have being trying to help but they have now referred to this channel, as apparently it is an Enterprise User.  I have already contacted my ISP who hosts the e-mail account and the server, they say there isn't an issue with either the account or the mail server. Temporarily I am using another e-mail program and that set up the email account straight away with no issues. 

Below are the settings I have used.  

Kind regards  

Steve

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-07*

Hi  

I just thought I would let you know that the issue has been fixed. I have been able to establish my exchange mailbox with no problems or issues.  

After months of frustrating problems, I think the issue was resolved by one of the latest Windows updates.  

Many thanks to everybody who tried to help, it is appreciated

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-24*

Hi，@Steven Sexton

Based on the screenshots you provided, I have a question that I need to confirm:

Have you tried logging into Outlook with another account? If the same problem occurs when logging into Outlook with another account, the problem occurs because the Autodiscover process used by Outlook receives unexpected results from a third-party web server when performing a root domain lookup.

Here is the official documentation provided by Microsoft on this issue:  Something went wrong and Outlook couldn't set up your account - Microsoft Support

To better understand that document, I found a third-party link for your reference: How to Fix “Something Went Wrong” Error in Microsoft Outlook (helpdeskgeek.com)

 

If the problem is solved, please mark my answer as the answer. Thank you for your support and understanding.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-18*

Hi，@Steven Sexton

Thanks for posting your question in the Microsoft Q&A forum.

When you configure Microsoft Outlook to connect to Microsoft Exchange, you receive the following error message: Logging on to the Exchange ActiveSync mail server (EAS): server not found.

This problem occurs because Outlook doesn't support connections to a server that's running Exchange Server by using the EAS protocol.

This is the official URL provided by Microsoft: Outlook can't use ActiveSync to connect Exchange - Outlook | Microsoft Learn

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
