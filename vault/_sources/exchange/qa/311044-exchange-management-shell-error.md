---
title: "Exchange Management Shell error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/311044/exchange-management-shell-error
question_id: 311044
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Management Shell error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/311044/exchange-management-shell-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Management shell shows below error when opening

New-PSSession : [exchange01] Processing data from remote server exchange01 failed with the  

following error message: [ClientAccessServer=RMLPCEXC02,BackEndServer=exchange01,RequestId=b659941e-3851-4c  

23-8f26-904ff52afb7a,TimeStamp=3/12/2021 4:38:01 AM]  

[AuthZRequestId=8ec8a184-2adf-4a22-955f-d4ed06847411][FailureCategory=AuthZ-TypeInitializationException] The type  

initializer for 'Nested' threw an exception. For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Micr ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : IncorrectProtocolVersion,PSSessionOpenFailed

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi,    

Which version of Exchange are you using and which CU?    

It looks like an old issue that occur with Exchange 2013, please upgrade to latest CU and see if the issue resolved.    

Some other options:    

What changes did you make to your server? If you install some third-party tools, uninstall them and have a reboot.    

Are you using the administrator account?    

Try recreating powershell virtual directory as this blog suggests: https://www.alitajran.com/recreate-virtual-directories-in-exchange-server/#Recreate_PowerShellVirtualDirectory    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
