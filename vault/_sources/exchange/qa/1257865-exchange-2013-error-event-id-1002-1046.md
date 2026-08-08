---
title: "Exchange 2013 Error Event ID 1002 & 1046"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1257865/exchange-2013-error-event-id-1002-1046
question_id: 1257865
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 Error Event ID 1002 & 1046

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1257865/exchange-2013-error-event-id-1002-1046 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am wondering if someone might be able to disipher this error code we started getting, it is a bunch of info I can't make heads or tails of.

```
Microsoft.Exchange.Server.Storage.Common.StoreException: ErrorCode: CorruptStore, LID: 55324 at Microsoft.Exchange.Server.Storage.LogicalDataModel.Conversations.TrackConversationUpdateForMessageDelete(Context context, Mailbox mailbox, TopMessage message, ModifiedSearchFolders modifiedSearchFolders) at Microsoft.Exchange.Server.Storage.LogicalDataModel.Conversations.TrackConversationUpdateForMessageReplace(Context context, Mailbox mailbox, TopMessage message, ModifiedSearchFolders modifiedSearchFolders) at Microsoft.Exchange.Server.Storage.LogicalDataModel.TopMessage.TrackUpdate(Context context, LogicalOperation operation, Nullable`1 userIdentityContext) at Microsoft.Exchange.Server.Storage.LogicalDataModel.TopMessage.OnAfterDataRowFlushOrDelete(Context context, Boolean delete) at Microsoft.Exchange.Server.Storage.StoreCommonServices.ObjectPropertyBag.Flush(Context context, Boolean flushLargeDirtyStreams) at Microsoft.Exchange.Server.Storage.LogicalDataModel.Item.Flush(Context context, Boolean flushLargeDirtyStreams) at Microsoft.Exchange.Server.Storage.LogicalDataModel.Message.Flush(Context context, Boolean flushLargeDirtyStreams) at Microsoft.Exchange.Server.Storage.LogicalDataModel.Item.SaveChanges(Context context) at Microsoft.Exchange.Server.Storage.LogicalDataModel.Message.SaveChanges(Context context) at Microsoft.Exchange.Server.Storage.LogicalDataModel.TopMessage.SaveChanges(Context context, SaveMessageChangesFlags flags) at Microsoft.Exchange.Protocols.MAPI.MapiFolder.MoveMessageTo(MapiContext context, MapiFolder destination, ExchangeId mid, Properties propertyOverrides, ExchangeId& outputMid, ExchangeId& outputCn) at Microsoft.Exchange.Protocols.MAPI.BulkOperation.MoveMessages(MapiContext context, MapiFolder source, MapiFolder destination, IList`1 mids, Properties propsToSet, BulkErrorAction notFoundAction, BulkErrorAction softErrorAction, IList`1 outputMids, IList`1 outputCns, Int32& progressCount, Boolean& incomplete, ErrorCode& error) at Microsoft.Exchange.Protocols.MAPI.MoveCopyMessagesOperation.ProcessMessages(MapiContext context, MapiFolder folder, IList`1 midsToProcess, Int32& progressCount, Boolean& incomplete, ErrorCode& error) at Microsoft.Exchange.Protocols.MAPI.MessageListBulkOperation.DoChunk(MapiContext context, Boolean& progress, Boolean& incomplete, ErrorCode& error) at Microsoft.Exchange.Server.Storage.MapiDisp.RopHandler.MoveCopyMessages(MapiContext context, MapiFolder sourceFolder, MapiFolder destinationFolder, ExchangeId[] messageIds, Boolean reportProgress, Boolean copyMessages, Boolean& partiallyCompleted, MoveCopyMessagesResultFactory resultFactory) at Microsoft.Exchange.Server.Storage.MapiDisp.RopHandlerBase.MoveCopyMessages(IServerObject sourceServerObject, IServerObject destinationServerObject, StoreId[] messageIds, Boolean reportProgress, Boolean isCopy, MoveCopyMessagesResultFactory resultFactory) 
   5B444941475F4354585D000074000000FF4B00000000000000025800000018FF40100F0104801CD8401000060480E0F71010E0B7000080A18030BDE82E2EFE7EEA459E107C368F2E296730303A4580891010BC33000080A18030BDE82E2EFE7EEA459E107C368F2E29670500078080891010BC330000
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-26*

Event ID 1146 is related to Microsoft Windows Failover Clustering. Check if your Cluster Resource Host Subsystem has stopped working. To troubleshoot the issue, you need first to check which DLL file is causing the issue, apart from reporting this to your Exchange Server expert or supplier. It would be best if you investigated more to understand the root cause of the problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-26*

Hi @Fenton, Mark ,  

This issue can have multiple forms. In order to help you better, can you share with us the scene you are in and what operations you have performed?  

This is usually caused by a corrupted mailbox or database, try using the New-MailboxRepairRequest cmdlet to detect and repair.
If you have problems with your current mailbox database, you can create a new mailbox database in Exchange Server and move all mailboxes and resources to this new database.  

You can check out this article about database repairs with events 1002 & 1046: How to restore Exchange Databases from a Storage failure.  

Note: Microsoft is providing this information as a convenience to you. The sites are not controlled by Microsoft. Microsoft cannot make any representations regarding the quality, safety, or suitability of any software or information found there. Please make sure that you completely understand the risk before retrieving any suggestions from the above link. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
