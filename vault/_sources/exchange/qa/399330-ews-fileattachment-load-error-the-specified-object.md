---
title: "EWS FileAttachment.Load Error.The specified object was not found in the store.,"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/399330/ews-fileattachment-load-error-the-specified-object
question_id: 399330
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# EWS FileAttachment.Load Error.The specified object was not found in the store.,

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/399330/ews-fileattachment-load-error-the-specified-object (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are trying to download attachments to our local server from a Mailbox where we have mails with attachments.  

To download this email Attachments we had build an windows service in our server.   

Steps we are following.  

1)We are filtering in the starting to fetch only unread emails from the inbox folder of the MailBox.  

 2)After that we LoadpropertiesforItem method of the exchange service with propertyset values as IDonly and Itemschema.Attachments.  

3) after that we are loading the attachment to write it in our local path.  

but the attachment.Load is failing with and exception "The specified object was not found in the store., The process failed to get the correct properties.  

Mailbox Error: Attachment Load Error:    at Microsoft.Exchange.WebServices.Data.ServiceResponse.InternalThrowIfNecessary() in \REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Core\Responses\ServiceResponse.cs:line 277  

   at Microsoft.Exchange.WebServices.Data.MultiResponseServiceRequest`1.Execute() in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Core\Requests\MultiResponseServiceRequest.cs:line 166      at Microsoft.Exchange.WebServices.Data.ExchangeService.InternalGetAttachments(IEnumerable`1 attachments, Nullable`1 bodyType, IEnumerable`1 additionalProperties, ServiceErrorHandling errorHandling) in \REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Core\ExchangeService.cs:line 1469  

   at Microsoft.Exchange.WebServices.Data.ExchangeService.GetAttachment(Attachment attachment, Nullable`1 bodyType, IEnumerable`1 additionalProperties) in \REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Core\ExchangeService.cs:line 1532"  

Its happening randomly from the EWS server, can anyone please suggest any round about for this particular issue.

## Answers

_No answers on this thread._
