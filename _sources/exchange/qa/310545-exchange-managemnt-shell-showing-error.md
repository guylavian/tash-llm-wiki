---
title: "exchange managemnt shell showing error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310545/exchange-managemnt-shell-showing-error
question_id: 310545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange managemnt shell showing error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310545/exchange-managemnt-shell-showing-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange management shell showing the below error.How can I fix this  

New-PSSession : [exchange01.contoso.local] Processing data from remote server exchange01.contoso.local failed with the  

following error message: [ClientAccessServer=exchange01,BackEndServer=exchange01.contoso.local,RequestId=4dd03ed3-b7ea-44  

9f-899f-8764d9fbda08,TimeStamp=3/11/2021 7:35:03 PM]  

[AuthZRequestId=8ec8a184-2adf-4a22-955f-d4ed06847411][FailureCategory=AuthZ-TypeInitializationException] The type  

initializer for 'Nested' threw an exception. For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Micr ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : IncorrectProtocolVersion,PSSessionOpenFailed

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-12*

Hi @Muhammed Shehim  ,    

What's the version of your Exchange server?    

Any changes were made to your Exchange environment before this issue occurred?    

Please go to Event Viewer and see if there are any relevant events?    

Besides, it's suggested to check the Exchange Back End website bindings via IIS manager > Exchange Back End, right click and choose Bindings, highlight https and click Edit, make sure a proper certificate is bound to the site:    

    

Furthermore, please have a look at the authentication settings of Powershell in both the Default Web Site and the Exchange Back End, see if they are same as the default settings:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
