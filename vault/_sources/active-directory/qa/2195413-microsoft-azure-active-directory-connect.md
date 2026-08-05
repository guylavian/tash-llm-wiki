---
title: "Microsoft Azure Active Directory Connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195413/microsoft-azure-active-directory-connect
question_id: 2195413
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Microsoft Azure Active Directory Connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195413/microsoft-azure-active-directory-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to create a On-Site File Server. I am using Microsoft Azure Active Directory Connect V2 to sync my users and groups from my Office 365, so it's easier to manage.

The domain I am trying to Sync is KTBlack.com, and I'm using the domain Cloud.KTBlack.com, and then changing the UPN once the sync is completed.

Here are the System Logs

Error 1:

SynchronizationServiceSetupTask:InstallCore - Caught unexpected exception. Details System.InvalidOperationException: LocalDB powershell operation failed on ADSync Bootstrap service: Enable-ADSyncBootstrapLocalDBInstance     at Microsoft.Azure.ActiveDirectory.Synchronization.Setup.SynchronizationServiceSetupTask.EnableADSyncBootstrapLocalDBInstance(Version targetInstanceVersion, String targetInstanceName, String syncAdminsGroupName, String currentUserAccount)     at Microsoft.Azure.ActiveDirectory.Synchronization.Setup.SynchronizationServiceSetupTask.InstallCore(String logFilePath, String logFileSuffix)

Error 2

LocalDB powershell operation failed on ADSync Bootstrap service: Enable-ADSyncBootstrapLocalDBInstance

I am however getting stuck on this error code below, Any help would be appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Slade Stull,  

Thank you for posting in Microsoft Community forum.  

Based on the description, I understand your question may be related to assign user license assignments to Azure Active Directory.   

Since there are no engineers dedicated to Azure Active Directory in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Azure Active Directory" tag  

Thank you for your understanding and support. If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,  

Daisy Zhou
