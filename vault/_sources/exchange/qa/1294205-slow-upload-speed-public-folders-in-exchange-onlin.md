---
title: "Slow upload speed Public Folders in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294205/slow-upload-speed-public-folders-in-exchange-onlin
question_id: 1294205
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Slow upload speed Public Folders in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294205/slow-upload-speed-public-folders-in-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day all,

Hope everyone is well.

I have 2 long ongoing cases that are not going in the direction i would like them to go so therefore i ask my question here.  

Summary:

We migrated from Exchange 2010 on premise to Exchange Online. The migration itself went fine, we set up a Hybrid and moved everything over gradually.

120+ somewhat mailboxes but than the issue; 250+ GB of Public Folders and around 9000 folders at that time. Everything was moved via Powershell scripts, took some good preparation and some figuring out along the way but in the end everything migrated without issues. Read operations of the Public Folders are fine, but write operations to the Public folders are not great.

Outlook hangs from time to time and is not useable in the time it is uploading.

The time needed to upload is ridiculous in my opinion, so far i have tested this from 3 different locations and the upload does not go higher than 1 mb/sec (8mbits), so it must the throttled, while the internet lines have 13 mbps - 45 mbps - 100mbps upload. So you can imagine if you want to move some mails with attachments and folders that are over 25 mb you can wait some sweet time and do nothing in Outlook. Since the company i work for uses Public Folders as a collaboration tool as has been used in the company for years we cannot simply switch or choose something else for it. In the 2 cases that have been going since February no one has even mentioned this, only request logs logs and more logs that lead to not much. I read no limitations of this online in Microsoft's documentation. Support pointed towards Outlook limitations but those are not valid since on-premise everything worked fine with the same amount of folders.  

Is there any way to improve this?   

Has anyone encountered the same behaviour?  

Are there alternatives for this?

We looked into Shared mailboxes but i have heard similar issues on performance and Microsoft 365 groups the same. Only things left for me to consider are Sharepoint and moving back to Exchange on-prem to resolve this matter.  

I can provide more information if needed.  

All help and information is welcome on this topic.  

Thanks in advance!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-31*

Hi @ Fernand Schins,

For public folders that have been running for many years, orphaned ACLs, mismatched mail-enabled public folder objects (MEPFs), or corrupted dumpster folders can cause public folder migrations to slow down considerably.

 

There is a script that scans for and reports issues found in public folder deployments that you can use to scan public folder deployments and fix any issues reported before the migration begins.

（Kindly note: Users with similarly large environments have indicated that this scan may also take a significant amount of time. ）

In addition, it is also mentioned in the official documentation that the public folder migration takes a long time to complete, depending on the number of folders, the number of items (equal to the data), and the presence of corrupted ACLs in the source public folder.

 

And, when I was researching related issues, many users also reported slowness during the migration process. So in my opinion, this should be by design.

Therefore, I recommend that you choose to migrate data from public folders to Exchange Online in batches during your off-hours.

Hope the above information is helpful to you!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
