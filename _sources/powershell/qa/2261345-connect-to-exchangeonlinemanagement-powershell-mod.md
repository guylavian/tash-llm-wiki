---
title: "Connect to ExchangeOnlineManagement powershell module returns error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261345/connect-to-exchangeonlinemanagement-powershell-mod
question_id: 2261345
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Independent Advisor"]
---
# Connect to ExchangeOnlineManagement powershell module returns error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261345/connect-to-exchangeonlinemanagement-powershell-mod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Script is called from Workato, and runs from a virtual machine that has exchange online 3.6.0. This was working up until last week. 

UnAuthorized

At C:\Program 

Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.6.0\netFramework\ExchangeOnlineManagement.psm1:766 char:21

- 

```
throw $_.Exception;
```

- 

```
~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : OperationStopped: (:) [], UnauthorizedAccessException

-  FullyQualifiedErrorId : UnAuthorized

When updating to exchange module 3.7.2 I see this error:

Error Acquiring Token: Unknown Status: Unexpected Error: 0xffffffff80070520 Context: (pii) Tag: 0x21420087 (error code -2147023584) (internal error code 557973639) Unknown Status: Unexpected Error: 0xffffffff80070520 Context: (pii) Tag: 0x21420087 (error code -2147023584) (internal error code 557973639) At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.7.2\netFramework\ExchangeOnlineManagement.psm1:754 char:21 + throw $_.Exception.InnerException; + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + CategoryInfo : OperationStopped: (:) [], MsalServiceException + FullyQualifiedErrorId : Unknown Status: Unexpected Error: 0xffffffff80070520 Context: (pii) Tag: 0x21420087 (error code -2147023584) (internal error code 557973639)

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-07*

Dear Team,

You will need to run the Enable to TLS 1.2 

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

.

Here is the script:

```
# Set TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Import module
Import-Module ExchangeOnlineManagement -RequiredVersion 3.6.0

# Connect to Exchange Online
try {
    Connect-ExchangeOnline -AppId "" -CertificateThumbprint "" -Organization ".onmicrosoft.com" -Verbose
    Write-Host "Connected successfully!"
    # Test a command
    Get-EXOMailbox -ResultSize 1
} catch {
    Write-Host "Error: $_"
} finally {
    Disconnect-ExchangeOnline -Confirm:$false
}
```
