---
title: "Exchange 2019 OWA Issue with Attaching Files when logged in via multiple sessions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167157/exchange-2019-owa-issue-with-attaching-files-when
question_id: 167157
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 OWA Issue with Attaching Files when logged in via multiple sessions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167157/exchange-2019-owa-issue-with-attaching-files-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

Since installing CU6 to our Exchange Servers we have an issue where if the mailbox is logged in more than once via OWA then the users cannot attach files to new messages.   

To replicate this issue log on to OWA via Chrome and IE at the same time and try attaching even a small file and you get a Spinning Circle for ages whilst it tries to attach the file.  

This is causing an issue as we have generic mailboxes that are logged in by multiple users via OWA, this was not an issue with CU1 but since updating to CU7 this has started happening  

Any idea on how to fix?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-19*

Hi @Stephen Cox  ,    

this was not an issue with CU1 but since updating to CU7 this has started happening    

You also mentioned "since installing CU6" at the beginning of the post, so do you mean this issue started to occur since CU6 and it continues after upgrading to CU7?    

I tried to search around as per your concern but hardly find any similar reports.  However, as far as I know, recently there is a known issue related to view/download attachments from a shared mailbox in OWA in Exchange 2019 CU7, and personally I am assuming if that could be relevant to the issue you described. See:     

Attachments can’t be downloaded or previewed from Outlook Web App    

According to the official article above, the issue is under investigation and the current workaround methods are to use Outlook client or accessing additional mailboxes by using the OWA light version.    

Given this, I'd like to suggest trying the methods provided in the article and check if the attachment can be uploaded properly. If it works, we could keep an eye on the article for the status or progress on it.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
