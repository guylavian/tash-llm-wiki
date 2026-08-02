---
title: "How to get OWA enabled users Login time information on Outlook Web (OWA)?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1424936/how-to-get-owa-enabled-users-login-time-informatio
question_id: 1424936
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to get OWA enabled users Login time information on Outlook Web (OWA)?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1424936/how-to-get-owa-enabled-users-login-time-informatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

How can I get on Exchange 2019 the last login time information for OWA users when they try to log in Outlook Web (OWA)? I need only OWA information. (OWA enabled user's username, last logon time etc.)

If there is any documentation from Microsoft or suggest please help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-15*

Hi @Baylar_Ismayil  ,

Welcome to our Q&A forum!

I couldn’t find any official documentation from Microsoft that provides the last logon time information for OWA users only. As far as I know, we can use Get-MailboxStatistics cmdlets to get the last logon time for users. As below:

In addition, I found a thread introduce the way to try using MS Logparser to extract the relevant logon information from IIS logs. For your reference: https://serverfault.com/questions/558215/find-out-if-user-logged-in-to-owa-read-his-emails

Another possible solution is that you can try to enable Audit logging for the specific user, it will record IP address and logon information. See: Want Audit of a specific user logon attempts on to the Exchange mailbox using any client, OWA, Active sync, Outlook etc

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
