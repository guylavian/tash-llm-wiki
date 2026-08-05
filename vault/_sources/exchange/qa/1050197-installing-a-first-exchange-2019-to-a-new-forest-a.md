---
title: "Installing a first Exchange 2019 to a new Forest, at Setup.exe /PrepareAD, getting an error: Active Directory operation failed on dc01.company1.com. The object 'CN=Microsoft Exchange System Objects,DC=company1,DC=com' already exists."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1050197/installing-a-first-exchange-2019-to-a-new-forest-a
question_id: 1050197
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Installing a first Exchange 2019 to a new Forest, at Setup.exe /PrepareAD, getting an error: Active Directory operation failed on dc01.company1.com. The object 'CN=Microsoft Exchange System Objects,DC=company1,DC=com' already exists.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1050197/installing-a-first-exchange-2019-to-a-new-forest-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

At Setup.exe /PrepareAD /OrganizationName:"company1" /IAcceptExchangeServerLicenseTerms_DiagnosticDataOn    

" was run:    

Microsoft.Exchange.Data.Directory.ADObjectAlreadyExistsException: Active Directory operation failed on    

dc01.company1.com. The object 'CN=Microsoft Exchange System Objects,DC=company1,DC=com' already    

exists.  ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object exists.    

 at    

System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll    

resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)    

 at    

System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)    

 at    

Microsoft.Exchange.Data.Directory.GuardedDirectoryExecution.ExecuteT    

 at Microsoft.Exchange.Data.Directory.PooledLdapConnection.GuardedSendRequest(String forestName,    

GuardedDirectoryExecution guardedDirectoryExecution, DirectoryRequest request, TimeSpan timeout, Func`3    

sendRequestDelegate, Int64& concurrency)    

We don't have any Exchange server 2019 in Forest,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-03*

My mistake with I've manually created the "Microsoft Exchange System Objects" in the new forest Active Directory Users and Computers, once I deleted the "Microsoft Exchange System Objects" I was able ran Setup.exe /PrepareAD /OrganizationName:"company1" /IAcceptExchangeServerLicenseTerms_DiagnosticDataOn  and  installed Exchange 2019 successfuly.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-18*

This may be related to a previously unavailable domain controller or tasks being run manually in the incorrect order. Or, possibly, the object was created on the backend without POA interference.    

Remove conflicting objects using Exchange Management Shell, e.g. for address list: `PS> remove-addresslist "S001059833 AL"`    

That can also be a Global Address List. In that case: `PS> remove-globaladdresslist "S001059833 GAL`"    

Restart failed task. Exchange hosting will be recreated from scratch. GAL and AL will be recreated during the task execution.    

Also, check these thread for help - https://learn.microsoft.com/en-us/answers/questions/774581/ms-exchange-2019-install-error-active-directory-op.html

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

Hi @Happee  ,    

Welcome to our forum!    

-  Please use ADSI Edit to check if anything else exists in CN=Microsoft Exchange System Objects. For example, there are SystemMailboxes, etc., please delete them.    

-  And check Active Directory Users and Computers for duplicate Microsoft Exchange System Objects, and if so, remove the duplicates. Please refer to: ms-exch-setupreadiness-adiniterrorrule    

Besides, you could refer to the following similar issue. Make a backup and remove the 'CN=Microsoft Exchange System Objects, DC=company1, DC=com' via ADSI Edit, run PrepareAD again.    

the_problem_of_installing_exchange_server_2016    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If methods above do not solve the issue, please check the Exchange setuplog and post the error information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
