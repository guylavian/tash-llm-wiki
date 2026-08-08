---
title: "Exchange toolbox, queue view error. Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154944/exchange-toolbox-queue-view-error-exchange-2016
question_id: 2154944
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange toolbox, queue view error. Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154944/exchange-toolbox-queue-view-error-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. When attempting to open the message queue view in Exchange Toolbox, an error occurs: "Failed to enable constraints. At least one row contains a value that violates non-null, uniqueness, or foreign-key constraints."

All columns of this data table are: NextHopDomain DeliveryType Status MessageCount NextRetryTime LastRetryTime LastError Identity CanSuspend CanResume CanRemove CanForceRetry

System.Data.ConstraintException: Failed to enable constraints. At least one row contains a value that violates non-null, uniqueness, or foreign-key constraints.

All columns of this data table are: NextHopDomain DeliveryType Status MessageCount NextRetryTime LastRetryTime LastError Identity CanSuspend CanResume CanRemove CanForceRetry ---> System.Data.ConstraintException: Failed to enable constraints. At least one row contains a value that violates non-null, uniqueness, or foreign-key constraints.

at System.Data.DataTable.EnableConstraints() at System.Data.DataTable.set_EnforceConstraints(Boolean value) at System.Data.DataTable.EndLoadData() at Microsoft.Exchange.Management.SystemManager.DataTableLoader.MoveRows(DataTable sourceTable, DataTable destinationTable, Boolean forceUseMergeTable) --- End of inner exception stack trace --- at Microsoft.Exchange.Management.SystemManager.DataTableLoader.MoveRows(DataTable sourceTable, DataTable destinationTable, Boolean forceUseMergeTable) at Microsoft.Exchange.Management.SystemManager.DataTableLoader.OnDoRefreshWork(RefreshRequestEventArgs e) at Microsoft.Exchange.Management.SystemManager.RefreshableComponent.worker_DoWork(Object sender, DoWorkEventArgs e) at System.ComponentModel.BackgroundWorker.OnDoWork(DoWorkEventArgs e) at System.ComponentModel.BackgroundWorker.WorkerThreadStart(Object argument)

When I check the message queues using the Management Shell with the `Get-Queue` command, everything is fine there are no stuck messages. Mail is being sent and received without any issues. But GUI queue doesn't work. 

What could this be and how to fix it?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-07*

Hi,@Ilya Lubenets

Thanks for posting your question in the Microsoft Q&A forum.

This error doesn’t indicate that your queues are “broken” or that mail is not flowing—it’s really a problem with how the Exchange Toolbox’s queue viewer is assembling the data. 

What’s happening is that the queue viewer builds a DataTable whose columns have non‑null, uniqueness, or foreign-key constraints. For one (or more) of the rows returned, one of the values (often in a field like NextRetryTime, LastRetryTime, or LastError) isn’t what the table expects—for example, it might be null even though the designer of the table expected a value. (Sometimes the value might simply be a “duplicate” for a unique column.) The underlying Get-Queue cmdlet returns the proper data, but when the GUI code loads that data into its DataTable it runs into a row that violates one of the constraints, and you get that error.

To resolve or work around the issue, you can use CU for Ex2016 (CU23) with latest Security Patch https://www.microsoft.com/download/details.aspx?familyID=f15bf797-0ac3-4bff-9483-d8afeef5bdfc

If you’re in an environment where you cannot upgrade immediately, simply be aware that the error is cosmetic and does not affect message delivery or processing.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-07*

As you said, when you check the queues using the PowerShell command `Get-Queue`, everything looks fine, and mail is flowing normally. There could be a corrupted message or queue data that’s not visible through `Get-Queue`. You might need to dig deeper into the logs or use a tool to check for corrupted messages.    

Additionally, you can verify your Exchange server is up to date with the latest Cumulative Update (CU), as these types of issues can sometimes be fixed in updates.   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-07*

As you said, when you check the queues using the PowerShell command `Get-Queue`, everything looks fine, and mail is flowing normally. There could be a corrupted message or queue data that’s not visible through `Get-Queue`. You might need to dig deeper into the logs or use a tool to check for corrupted messages.  

Additionally, you can verify your Exchange server is up to date with the latest Cumulative Update (CU), as these types of issues can sometimes be fixed in updates.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
