---
title: "Not able to send emails to Exchange Online users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2260532/not-able-to-send-emails-to-exchange-online-users
question_id: 2260532
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Not able to send emails to Exchange Online users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2260532/not-able-to-send-emails-to-exchange-online-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I hope someone here can help!

For the past 3-4 weeks, emails I have been sending to my clients (or vendors) have not been received by them.

I noticed that they all use Microsoft Outlook, and many through Exchange Online, so I'm assuming that's where the issue is.

I use Google Workspace. When I contacted Google support, they said (and showed me) that from Google's end, the emails ARE being sent successfully. However, my recipients aren't getting them.

I resorted to using my personal email address, which is a regular Gmail address - and that's working. However, my work email isn't, and it seems that any email from my domain is being rejected and not even reaching my recipients' spam folders.

I cannot reach Microsoft support because I'm not a customer. 

Can anyone here point me in the right direction?

Thank you!

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-24*

Hi @Mony Raanan  ,

 

Thank you for posting your question in the Microsoft Q&A forum.

In general, when you send emails to external recipients, your outbound server have to establish SMTP connection with destination server in recipient organization. So when you send emails to Exchange Online mailboxes, your Google Workspace backend server will try to connect with Exchange Online Protection.

If your Google support confirm that email could be sent out successfully, the connection to EOP should be established successfully and EOP could receive your emails.

Then EOP will scan and filter your email before delivering to O365 mailboxes. Maybe there could be some potential risk for emails sent by your Google Workspace, and email could be quarantined by M365 and cannot deliver to recipient mailboxes.

You can contact your recipient and need administrator from recipient organization to check if previous email is quarantined or blocked by some reasons.

Here are some articles about email quarantine in M365:

Quarantined email messages - Microsoft Defender for Office 365 | Microsoft Learn 

Manage quarantined messages and files as an admin - Microsoft Defender for Office 365 | Microsoft Learn 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
