---
title: "Transport Rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412717/transport-rule
question_id: 412717
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Transport Rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412717/transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All    

I am using exchange 2016 hybrid environment, i have a remote shared mailbox. I have a requirement, i.e. i have a shared mailbox and any email coming to this shared mailbox with an attachment containing pdf file or jpg file should be forwarded to external email address. i.e abc@Company portal   .com    

I created a external contact lets say ******@mydomain.com in exchange onprem.    

if i perform the below steps will it work for me. is there a way which will work without creating transport rule. I am adding message header in transport rule, i am not sure is it right way.    

-  Create a transport rule in exchange 2016.    

Apply this if--The recipient is '******@mydomain.com'    

and    

Any attachment's file name matches--'.pdf' or '.jpg'    

Do the following:    

Set the message header to this value-->Set the message header 'APPTEST' to the value '1'    

-  Outlook Rule in the shared mailbox    

Add a condition    

Message header includes: APPTEST    

Has attachment    

Add an action    

Move to--Folder01    

Forward to-->mysharedmailbox@Company portal   .com

## Answers

_No answers on this thread._
