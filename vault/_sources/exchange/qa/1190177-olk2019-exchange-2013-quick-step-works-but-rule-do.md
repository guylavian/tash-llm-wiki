---
title: "OLK2019+Exchange 2013 - Quick Step Works but rule doesnt"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190177/olk2019-exchange-2013-quick-step-works-but-rule-do
question_id: 1190177
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# OLK2019+Exchange 2013 - Quick Step Works but rule doesnt

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190177/olk2019-exchange-2013-quick-step-works-but-rule-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ENV:

-  OLK 2019

-  Exchange 2013

ISSUE:

I have a situation where a number of quick steps are configured in Outlook to move a message/s from the users inbox to a folder in a shared mailbox.  The quick steps work fine, but you have to select each message or CTRL select multiple then tap on the Quick Step.

When we create a rule and try to select the same Shared Mailbox folder it responds with the error:

"The attempted Operation failed. An object could not be found"

Those affected all have "Owner" permission on the folders involved, and happens with some other folders but not all.

Is this an OLK or EXCH bug?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-19*

Hi Faery Fu-MSFT,

My clients and I have other rules that we use to move inbox items to sub-folder of a shared mailbox that function ok.  I was trying to diagnose why a few I am trying to assemble would not work.

In each case the site uses on Prem Exchange 2013/2016/2019 with OLK 2013/2016/2109/2022 and the shared mailboxes are mapped automatically when outlook first sees the user has access.

I'll keep digging

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-17*

Hi @Shane King ,

Based on my research, there is indeed no direct way to set up a rule for a shared mailbox when it only has been linked to your own Exchange mailbox account. However, there are several other ways to still get this to work:

Method 1: Outlook on the Web

After you log in to OWA, then click on the upper-right corner of your own name to enter the option to open another mailbox. Then set a rule in Outlook on the web for the shared mailbox.

Method 2: Additional Exchange account

Important: 

-  If you already see the shared mailbox folders in the folder list, it is possible that the mailbox is either Auto-mapped or was added using Open these additional mailboxes. You must first remove the configuration that added the mailbox before proceeding with the numbered steps below.

-  To remove an Auto-mapped mailbox, see: https://learn.microsoft.com/en-us/outlook/troubleshoot/profiles-and-accounts/remove-automapping-for-shared-mailbox

-  To remove another person's mailbox from Open these additional mailboxes, see Remove another person's mailbox.

To do this, click on the File tab and choose Add Account. When setting up the account, Auto Account Setup may recognize your main mailbox linked to your user account. When this happens, specify the email address of the shared mailbox or select the option to configure the Exchange account manually.

Once the mailbox has been added, select its Inbox folder and add the rule as you would normally do for your own mailbox.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
