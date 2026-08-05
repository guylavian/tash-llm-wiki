---
title: "Windows Server GPO SharePoint Synchronization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/703034/windows-server-gpo-sharepoint-synchronization
question_id: 703034
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-business-platform-windows", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server GPO SharePoint Synchronization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/703034/windows-server-gpo-sharepoint-synchronization (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

Can anyone help me. We are in the process of setting up SharePoint and a new Windows Server for a client.  

Now it would be cool if we can, via group policy or otherwise, synchronize the document store in their SharePoint site in Explorer.  

Does anyone have a solution for this?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-21*

Hello Lino,  

This is a regular feature for SharePoint.   

Please check:https://support.microsoft.com/en-us/office/sync-sharepoint-files-and-folders-87a96948-4dd7-43e4-aca1-53f3e18bea9b  

Other option is simply to use the SharePoint folder as a shared folder: https://support.microsoft.com/en-us/office/map-a-network-drive-to-a-sharepoint-library-751148de-f579-42f9-bc8c-fcd80ccf0f53  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-21*

Hi @Lino   ,

Welcome to Q&A Forum!

From my research, I don't find a way to synchronize SharePoint Document libraries via group policy.

We recommend that you can use OneDrive to sync files in your Microsoft 365 or Microsoft SharePoint site library to your computer.

Please follow the steps:

1.In your browser, on your SharePoint site, navigate to the library of files you want to sync with.

2.Select Sync in the toolbar.

Reference:

-  Sync SharePoint files and folders

Thanks,  

Echo Du

===========================================================

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
