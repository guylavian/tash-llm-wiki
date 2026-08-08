---
title: "Exchange 2019 CU12 KB5024269 broke my server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281051/exchange-2019-cu12-kb5024269-broke-my-server
question_id: 1281051
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 CU12 KB5024269 broke my server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281051/exchange-2019-cu12-kb5024269-broke-my-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi i have on-prem exchange 2019  cu12 the latest update i approved for install was kb5024269 ...

The update started to install and after a few minutes got an "error install 0x80070643" all my exchange services was on disable .. and after i changed all to automatic restarted the server all looked fine until i tried to open ECP OR OWA 

i got error 500 on the webpage ?   i tried to restore the configuration files of the web services with APPCMD and got access is denied .. any idea how to fix this ?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-10*

Hi kopels,

I suggest that you can open CMD as an administrator and reinstall the update according to the following steps.

Use elevated permissions to reinstall the security update on the server.

-Select Start, and then type cmd.

-Right-click Command Prompt from the search results, and then select Run as administrator.

-If the User Account Control window appears, select the option to open an elevated Command Prompt window, and then select Continue. If the UAC window doesn’t appear, continue to the next step.

-Type the full path of the .msp file for the security update, and then press Enter.

-After the update installs, restart the server.

Learn more through the link below

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues#http-500-errors-in-owa-or-ecp

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-stops-working-after-update

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
