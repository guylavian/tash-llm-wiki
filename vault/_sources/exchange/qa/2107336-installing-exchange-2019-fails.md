---
title: "Installing Exchange 2019 Fails."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2107336/installing-exchange-2019-fails
question_id: 2107336
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Installing Exchange 2019 Fails.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2107336/installing-exchange-2019-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently running one Exchange 2016 Server in Hybrid mode, all our mailboxes are in M365. I am running an upgrade to Exchange 2019 and the installation fails at Mailbox role. I have run the installation from the command line and made sure its run as an admin and cannot get past this error. Does anyone have any suggestions?

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-21*

Turns out the script could not make changes to the reg key (I manually ran it). I tested the script on another system and it ran fine. Going to decommission this server and build a new one.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-21*

Here is the screenshot, the error message happened at step 10 of 12. I made sure all the pre-reqs have been set, not sure why it would error out at this step.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-21*

Hi,@Gavin Ross

Thanks for posting your question in the Microsoft Q&A forum.

I agree with S. Sengupta 's suggestion and here are my additions.

Based on your description, you are having issues upgrading from Exchange 2016 Server to Exchange 2019 Server. We recommend you to use the officially recommended Exchange Deployment Assistant, which will help you to avoid many problems.

You can upgrade according to the guide.

I found a detailed hybrid upgrade guide for your reference:https://www.linkedin.com/pulse/how-upgrade-exchange-hybrid-server-2016-2019-stellardatarecovery

Finally, if the issue still hasn't been resolved, I'd like you to provide specific information or screenshots.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-19*

It may be due to several factors:

-  Make sure you have fulfilled all the pre-requisites for upgrading to Exchange 2019.

-  Check the ExchangeSetup.log located in the C:\ExchangeSetupLogs\ directory for any specific errors.

-  If the installation fails repeatedly, consider trying the installation on a clean Windows Server 2019 installation

-  Temporarily disable any antivirus or firewall.
