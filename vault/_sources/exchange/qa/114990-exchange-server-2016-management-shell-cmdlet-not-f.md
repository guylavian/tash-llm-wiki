---
title: "Exchange Server 2016 Management Shell - CMDLET not found"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/114990/exchange-server-2016-management-shell-cmdlet-not-f
question_id: 114990
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2016 Management Shell - CMDLET not found

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/114990/exchange-server-2016-management-shell-cmdlet-not-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a full read only access to our Exchange org. I am running the mgmt. shell locally with my Exchange server remote. What I am finding is that some CMDLETS work fine like get-mailbox whereas when I run other like get-mailboxpermission result in command not found:

Get-Mailboxpermission : The term 'Get-Mailboxpermission' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a  

path was included, verify that the path is correct and try again.  

At line:1 char:1

-  Get-Mailboxpermission

-  ~~~~~~~~~~~~~~~~~~~~~

-  CategoryInfo : ObjectNotFound: (Get-Mailboxpermission:String) [], CommandNotFoundException

-  FullyQualifiedErrorId : CommandNotFoundException

Now if I run the shell directly on the server there no issue. What am I doing wrong ?

## Answers

_No answers on this thread._
