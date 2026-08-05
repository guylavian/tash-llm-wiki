---
title: "Exchange 2013 Version 15.0 ‎(Build 847.32)‎ Security Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334662/exchange-2013-version-15-0-build-847-32-security-u
question_id: 334662
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 Version 15.0 ‎(Build 847.32)‎ Security Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334662/exchange-2013-version-15-0-build-847-32-security-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange 2013 Version 15.0 ‎(Build 847.32)‎ with Security Update For Exchange Server 2013 SP1 and need to install the update CU 23. Can I install CU 23 directly or do I have to install all older Updates before? Is there a good explanation on the web, how to do it?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-29*

Hi @Dominique Siegfried  

To get the latest version of Exchange 2013, download and install Microsoft Exchange Server 2013 Cumulative Update 23. Because each CU is a full installation of Exchange and includes updates and changes from all previous CUs, you don't need to install any previous CUs or service packs first.

And the links peovided above should be helpful to you. Below is an article which include step-by-step guide to upgrade your Exchange server to the latest CU for your reference:

Exchange 2013 Cumulative Update installation tips and best practices

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

After you upgrade your server to CU23, install the Security Update For Exchange Server 2013 CU23 (KB5000871)

1.Disable the anti-virus software.  

2.Open an elevated Command Prompt window (not PowerShell) as an administrator, like this:

-   Select Start and then enter cmd .

-   Right-click Command Prompt in the results and select Run as administrator .

-   If the User Account Control dialog box appears, select Yes and then Next .

3.At the command prompt, enter the full path to the folder that contains the 'MSP file', then press 'Enter'.  

Note: Do not double-click the 'MSP file' to run it.  

4.When the installation is complete, re-enable the antivirus software and restart your computer. (The installation program may prompt you to restart.)

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-28*

Hi @Dominique Siegfried   ,

You can install the Cumulative update 23 but it will be a big jump from SP1 to CU23. Pre-requisites needs to be carefully installed.

Since you are in SP1, I believe the .NET will be 4.5.2 which needs to be upgraded to 4.8. So, below will be the steps,

1.Install .NET 4.8  

2.Install other pre-requisites  

3.Prepare Active Directory  

4.Install CU

https://learn.microsoft.com/en-us/exchange/upgrade-exchange-2013-to-the-latest-cumulative-update-or-service-pack-exchange-2013-help

Preparing Active Directory  

https://learn.microsoft.com/en-us/exchange/prepare-active-directory-and-domains-exchange-2013-help#exchange-2013-active-directory-versions

Pre-requisites  

https://learn.microsoft.com/en-us/exchange/exchange-2013-prerequisites-exchange-2013-help

Supportability matrix:  

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework

If the above suggestion helps, please click on "Accept Answer" and upvote it. Thanks for understanding.
