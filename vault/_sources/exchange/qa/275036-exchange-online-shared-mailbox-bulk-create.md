---
title: "Exchange Online Shared Mailbox Bulk Create"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275036/exchange-online-shared-mailbox-bulk-create
question_id: 275036
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online Shared Mailbox Bulk Create

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275036/exchange-online-shared-mailbox-bulk-create (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,     

I am currently trying to setup shared mailboxes for an organisation. As it is a Pain in the A** to create them inside the portal one by one (especially if we are talking about ~ 100 Mailboxes). I tried to realize that via Powershell and a CSV file. This is what i got so far:     

Import-Csv "C:\Users\Example\Documents\Mailboxes.csv" | foreach-object {​​​​ New-Mailbox -Name $.MyName -DisplayName $.MyDisplay -Shared }    

And this is the Format of the according csv File:     

MyName,MyDisplay    

test,test    

test1,test1    

So far so good, it creates the Mailboxes out of the CSV file without any Issues. Now I need to assign mailbox permissions for those mailboxes. Sure I could do that with a new CSV File in the same way again:     

Import-Csv "C:\Users\Example\Documents\Access" | foreach-object { Add-MailboxPermission $.Mailbox -User $.User -AccessRights $_.Access }    

With the according CSV File again:     

Mailbox,User,AccessRights    

test,user@keyman  ,FullAccess    

test,user2@keyman  ,FullAccess    

test1,user2@keyman  ,FullAccess    

This way I can already save some time but I still have to created the two CSV files and depending on how many user have permissions to the same mailbox, the CSV file gets rather long and repetitive.     

My Questions now are:    

-  Is there a way to create the mailboxes and assign the permissions in the same step using only one csv file?     

-  Am I taking the wrong approach and is there a better one than working with CSV files ?     

-  If yes please explain other possibilities I have to achieve my goal.    

-  Is there a way to pass an array to the powershell command (for the parameter -User for example) ?    

Looking forward to your inputs and thoughts on this.    

Thank you in advance :)     

Dominik

## Answers

_No answers on this thread._
