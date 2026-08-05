---
title: "Hi. I want to connect to Exchange Online P1 using Outlook 2016 on a Windows Server 2016 platform. It's working for 4 users but not for one. What am I doing wrong?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2280343/hi-i-want-to-connect-to-exchange-online-p1-using-o
question_id: 2280343
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hi. I want to connect to Exchange Online P1 using Outlook 2016 on a Windows Server 2016 platform. It's working for 4 users but not for one. What am I doing wrong?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2280343/hi-i-want-to-connect-to-exchange-online-p1-using-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. I want to connect to Exchange Online P1 using Outlook 2016 on a Windows Server 2016 platform. It's working for 4 users but not for *@.be (all 5 accounts are within the same domain). What am I doing wrong? I tried with MFA enabled and disabled. I have to add, that it worked for all 5 users until a few weeks ago and then suddenly that fifth user lost access and can now only login using a browser or the Outlook app on her iPhone.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-02*

Hi Th Admin,

Thanks for reaching out about the Outlook 2016 connectivity issue to Exchange Online P1 on Windows Server 2016. I understand one user (*.be) can't connect, unlike others, despite working previously. This issue, which started a few weeks ago, persists despite MFA adjustments and upgrading to Microsoft 365 Business Standard. 

Here are the key steps we recommend investigating and resolve the issue: 

1. Account vs. Computer Test

To see if the issue is with the account or the computer, please: 

-  Test the .be account on a different working computer*:** Try signing into Outlook 2016 on a computer using the *.be account. 

-  Test a functional account on the problematic computer: Try signing into Outlook 2016 on the problem computer using one of the other working accounts. 

2. Update Outlook 2016 

-  Ensure the latest updates are installed. 

-  Confirm that the Click-to-Run version is being used, as it supports modern authentication required by Exchange Online. 

3. Reset credentials and Outlook profile 

-  Go to Control Panel > Credential Manager and remove any stored Outlook or Microsoft credentials for the *.be user. 

-  Create a new Outlook profile for the *.be user via Control Panel > Mail (Microsoft Outlook 2016) > Show Profiles > Add. 

4. Use the Windows "Get Help" App for Diagnostics

-  On the affected Windows Server 2016 computer, open the Start Menu and search for "Get Help".

-  Launch the app, describe your issue (e.g., "Outlook won't connect" or "cannot sign in to Outlook") and follow the guided troubleshooting steps. 

For more general details on Outlook connectivity issues, you can also refer to this Microsoft article: Outlook can't connect to Exchange Online or create new profiles 

Please complete these steps to see if they resolve the problem. If the issue persists, as it seems to be related to the Windows Server 2016 environment where Outlook 2016 is installed, we recommend reaching out to the vendor or reseller where you acquired your Windows Server 2016 license. They are best equipped to provide support for the operating system, as this falls outside our support scope. 

Thanks for your patience as we work to resolve this. We look forward to your update. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
