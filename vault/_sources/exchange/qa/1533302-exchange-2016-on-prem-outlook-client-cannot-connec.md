---
title: "Exchange 2016 on prem - Outlook Client cannot connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1533302/exchange-2016-on-prem-outlook-client-cannot-connec
question_id: 1533302
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 on prem - Outlook Client cannot connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1533302/exchange-2016-on-prem-outlook-client-cannot-connec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community!  

I'm asking for suggestions about Exchange in an AD environment (W2K16) and a non-working Outlook client.  

Exchange Server 2016 Std runs on a Windows Server 2016.  

Installation, configuration and commissioning without any problems so far.  

Mail accounts set up in the EAC (from AD) can be used for the first time without any problems and the mail flow also works perfectly; but only in the Outlook Web Client.  

Every previous attempt to persuade Outlook to connect to Exchange has failed with the terse message "Something didn't work."  

What is striking in this context is the fact that a 1:1 modeled structure works flawlessly.  

Outlook of a logged in AD user starts, sets up the connection and then opens without any problems.  

The only difference between the productive and test environment is an Ubuntu LTS server with Squid proxy, which establishes the Internet connection for the employees. Maybe there is a problem with a missing whitelist entry or a TLS issue??  

Maybe someone has a tip where I can start?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-16*

Hi @HK@BfW  ,

Every previous attempt to persuade Outlook to connect to Exchange has failed with the terse message "Something didn't work."

Does this issue occur to both domain-joined and non-domain joined Outlook clients?   

What's the detailed version of the Outlook clients? You can check the build number via File > Office Account > About Outlook, confirm if the version information is the same in product and test environment.  

Besides, to help narrow down the problem, I'd recommend trying to use the Test E-Mail Autoconfiguration service within Outlook and see if the affected client can connect to the AutoDiscover service：

-  Launch Outlook using a profile with no email account, see Use Outlook without an email account.

-  Use the Test E-mail AutoConfiguration tool to help determine if AutoDiscover can success.

Additionally, as regards to your concern about the whitelist entry, sounds like a reasonable cause as well. You can go through the document below and make sure the exclusions are configured properly:  

Running Windows antivirus software on Exchange servers

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
