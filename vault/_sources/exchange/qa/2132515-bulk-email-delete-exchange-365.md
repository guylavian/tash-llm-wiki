---
title: "Bulk Email delete exchange 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2132515/bulk-email-delete-exchange-365
question_id: 2132515
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Bulk Email delete exchange 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2132515/bulk-email-delete-exchange-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm looking for a way to bulk delete all emails from year 2023 using powershell like I did last year with 2022 emails, as far as I know there's no way to use Search-Mailbox since the cmdlet is deprecated (thanks Microsoft) and now the only way to do this is by using Compliance Search.

Well, 1st I created a new compliance search and I started it:

$Search=New-ComplianceSearch -Name "2023" -ExchangeLocation ******@pln.es -ContentMatchQuery '(Received:1/1/2023..12/31/2023) AND (Sent:1/1/2023..12/31/2023)'

Start-ComplianceSearch -Identity $Search.Identity

I waited until I see it's finished using "Get-ComplianceSearch"

As you can see, it found some emails that I want to delete:

PS C:\WINDOWS\system32> get-compliancesearch -identity "2023" | format-list

Language                              :

StatusMailRecipients                  : {}

LogLevel                              : Suppressed

IncludeUnindexedItems                 : True

ContentMatchQuery                     : (Received:1/1/2023..12/31/2023) AND (Sent:1/1/2023..12/31/2023)

SearchType                            : EstimateSearch

HoldNames                             : {}

SearchNames                           : {}

RefinerNames                          : {}

Region                                :

Refiners                              :

Items                                 : 0

Size                                  : 0

UnindexedItems                        : 0

UnindexedSize                         : 0

SuccessResults                        : {}

SearchStatistics                      :

Errors                                :

ErrorTags                             : {}

NumFailedSources                      : 0

JobId                                 : ab07db83-e81b-41e2-5e7e-08dd1e778c25

Name                                  : 2023

CreatedTime                           : 17/12/2024 8:48:15

LastModifiedTime                      : 17/12/2024 8:48:15

JobStartTime                          : 17/12/2024 8:48:21

JobEndTime                            :

Description                           :

CreatedBy                             : Administrador Portal Office365

RunBy                                 : Administrador Portal Office365

TenantId                              : 69774f3f-de5b-47b9-b84a-71db0b84d494

NumBindings                           : 0

Status                                : Starting

ExchangeLocation                      : {******@pln.es}

PublicFolderLocation                  :

SharePointLocation                    :

OneDriveLocation                      :

ExchangeLocationExclusion             :

PublicFolderLocationExclusion         :

SharePointLocationExclusion           :

OneDriveLocationExclusion             :

JobRunId                              : ff136739-b330-43e8-3bac-08dd1e778f4b

Retry                                 : False

AllowNotFoundExchangeLocationsEnabled : False

JobOptions                            : 272

JobProgress                           : 0

CaseId                                :

CaseName                              :

PagingState                           :

Identity                              : ff136739-b330-43e8-3bac-08dd1e778f4b

ContentURL                            :

ResultInEOP                           : False

AzureBatchFrameworkEnabled            : True

IsValid                               : True

ObjectState                           : New

PS C:\WINDOWS\system32> get-compliancesearch -identity "2023" | format-list

Language                              :

StatusMailRecipients                  : {}

LogLevel                              : Suppressed

IncludeUnindexedItems                 : True

ContentMatchQuery                     : (Received:1/1/2023..12/31/2023) AND (Sent:1/1/2023..12/31/2023)

SearchType                            : EstimateSearch

HoldNames                             : {}

SearchNames                           : {}

RefinerNames                          : {}

Region                                :

Refiners                              :

Items                                 : 25443

Size                                  : 2674526518

UnindexedItems                        : 31

UnindexedSize                         : 430339341

SuccessResults                        : {Location: ******@pln.es, Item count: 25443, Total size: 2674526518}

SearchStatistics                      : {"ExchangeBinding":{"Search":{"Name":null,"Sources":"1","SourcesRaw":1,"ContentItems":25443,"ContentSize":"2.49

```
GB","ContentSizeRaw":2674526518,"HasFaults":false},"Queries":[{"Name":"_PrimaryQuery","Sources":"1","SourcesRaw":1,"ContentItems":25443,"ContentSize":"2.49

                                    GB","ContentSizeRaw":2674526518,"Query":"((((received\u003e=\"01-Jan-2023 00:00:00 AM\") AND (received\u003c\"01-Jan-2024 00:00:00 AM\"))) AND (((sent\u003e=\"01-Jan-2023 00:00:00 AM\") AND

                                    (sent\u003c\"01-Jan-2024 00:00:00 AM\"))))","Type":"Primary"},{"Name":"_UnindexedQuery","Sources":"1","SourcesRaw":1,"ContentItems":31,"ContentSize":"410.40

                                    MB","ContentSizeRaw":2674526518,"Query":"((((((received\u003e=\"01-Jan-2023 00:00:00 AM\") AND (received\u003c\"01-Jan-2024 00:00:00 AM\"))) AND (((sent\u003e=\"01-Jan-2023 00:00:00 AM\") AND

                                    (sent\u003c\"01-Jan-2024 00:00:00 AM\"))))) AND (((IndexingErrorCode\u003c0) OR (IndexingErrorCode\u003e0) OR

                                    (IsPartiallyIndexed=True))))","Type":"Unindexed"}],"Sources":[{"Name":"******@pln.es","ContentItems":25443,"ContentSize":"2.49 GB"}]}}
```

Errors                                :

ErrorTags                             : {}

NumFailedSources                      : 0

JobId                                 : ab07db83-e81b-41e2-5e7e-08dd1e778c25

Name                                  : 2023

CreatedTime                           : 17/12/2024 8:48:15

LastModifiedTime                      : 17/12/2024 8:49:07

JobStartTime                          : 17/12/2024 8:48:21

JobEndTime                            : 17/12/2024 8:49:07

Description                           :

CreatedBy                             : Administrador Portal Office365

RunBy                                 : Administrador Portal Office365

TenantId                              : 69774f3f-de5b-47b9-b84a-71db0b84d494

NumBindings                           : 1

Status                                : Completed

ExchangeLocation                      : {******@pln.es}

PublicFolderLocation                  :

SharePointLocation                    :

OneDriveLocation                      :

ExchangeLocationExclusion             :

PublicFolderLocationExclusion         :

SharePointLocationExclusion           :

OneDriveLocationExclusion             :

JobRunId                              : ff136739-b330-43e8-3bac-08dd1e778f4b

Retry                                 : False

AllowNotFoundExchangeLocationsEnabled : False

JobOptions                            : 272

JobProgress                           : 100

CaseId                                :

CaseName                              :

PagingState                           :

Identity                              : ff136739-b330-43e8-3bac-08dd1e778f4b

ContentURL                            :

ResultInEOP                           : False

AzureBatchFrameworkEnabled            : True

IsValid                               : True

ObjectState                           : New

I now use the cmdlet New-CompianceSearchAction to hard delete them:

PS C:\WINDOWS\system32> New-ComplianceSearchAction -SearchName "2023" -Purge -PurgeType HardDelete

Confirmar

¿Está seguro de que desea realizar esta acción?

This operation will make message items meeting the criteria of the compliance search "2023" completely inaccessible to users. There is no automatic method to undo the removal of these message items.

[S] Sí  [O] Sí a todo  [N] No  [T] No a todo  [U] Suspender  [?] Ayuda (el valor predeterminado es "S"): S

Name       SearchName Action RunBy                          JobEndTime Status

2023_Purge 2023       Purge  Administrador Portal Office365            Starting

PS C:\WINDOWS\system32> Get-ComplianceSearchAction

Name                         SearchName             Action  RunBy                          JobEndTime          Status

2023_Purge                   2023                   Purge   Administrador Portal Office365 17/12/2024 9:07:13  Completed

Once is finished I go into my outlook and I see nothing has happened, 2023 emails are still there.

I don't know what I'm doing wrong. Please, help.

Thanks a lot, regards.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-18*

Hi @Sergio,

Welcome to the Microsoft Q&A platform!

Based on your description, you have followed the correct steps to create and launch a compliance search, but emails are not being deleted as expected. You can check the following items and try to resolve the issue:

-  Make sure the mailbox is not subject to any retention policies or holds (such as Litigation Hold, In-Place Hold). These can prevent items from being permanently deleted.

You can check the hold status using the following command:

```
Get-Mailbox -Identity "******@pln.es" | Format-List LitigationHoldEnabled, InPlaceHolds
```

-  Deleted items may be moved to the Recoverable Items folder instead of being permanently deleted. You can check this folder and delete items from it if necessary.

To delete items from the Recoverable Items folder, use:

```
Search-Mailbox -Identity "******@pln.es" -SearchDumpsterOnly -DeleteContent
```

-  Make sure the account running the compliance search and purge operation has the necessary permissions. The account should be assigned the Mailbox Import Export role.

-  Double-check that the search name used in New-ComplianceSearchAction exactly matches the search name created.

-  Review any errors or logs that may provide more details about why the purge did not complete as expected. You can use:

```
Get-ComplianceSearchAction -Identity "2023_Purge" | Format-List
```

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
