---
title: "Exchange IIS authentication for Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1046207/exchange-iis-authentication-for-outlook
question_id: 1046207
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange IIS authentication for Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1046207/exchange-iis-authentication-for-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,     

I have 2 Exchange 2016 on-prem servers. Both were identical in the terms of IIS settings.     

We decided to modify some settings on one server to disable basic authentication for ActiveSync devices. But, some other settings were changed (mostly in IIS - Authentication).     

Result: One server is healthy and accepts Outlook connection, one server asks Outlook for password and refuse to connect.     

Test connection from Outlook looks like this:    

https://mail.contoso.com/mapi/emsmdb/?mailboxid=<GUID> .. and there asks for credentials over and over again..     

There is no difference in Get-MapiVirtualDirectory cmdlet between these two servers. I tried to compare all Virtual Directories and their authentication methods, fixed some but still something is missing ...     

Other services like OWA etc works fine...

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-27*

Hi @Bash   ,    

I wonder if the computer using Outlook Client connect to Server is joined-in domain?    

According to my test, after I disable Basic authentication for ActiveSync, I can successfully connect to the server in the following scenarios:    

-  Disable Basic authentication for Autodiscover.    

-  Enable Windows authentication for ActiveSync.    

-  Remove the Negotiate in Windows authentication for Autodiscover.    

In my opinion, I would suggest that you enable Windows authentication for ActiveSync.    

This article details Windows authentication: Windows Authentication Overview | Microsoft Learn    

This is closer to AD and IIS, hope it helps you a little!    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

Some update..  After we disable Negotiate provider from mapi/windows authentication, leaving only NTLM, the connection from Outlook succeeded.       

After that some prompts appeared again from autodiscover. Removing Negotiate from Autodiscover virtual directory fixed it as well.     

So, one server is working with all "default" options, one server has different configuration (removed Negotiate).    

What could couse the problem with Negotiate option in Windows authentication provider?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-18*

Hi @Bash   ,    

I followed your steps to test in my lab and got the same results as you.    

The Outlook client keeps popping up password input box and trying connection.    

Then, I tried disabling basic authentication for Autodiscover and retrying connecting to the server from Outlook client. Now ,it can be successfully connected.    

    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
