---
title: "Connect-ExchangeOnline Unauthorized"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187882/connect-exchangeonline-unauthorized
question_id: 1187882
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Connect-ExchangeOnline Unauthorized

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187882/connect-exchangeonline-unauthorized (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to connect exchange online service through powershell. I use the EXO V3 for that.

I use access token as authentication mechanism. I created an app on azure active directory and give it permission of Exchange.ManageAsApp  and also add this app in Exchange Administrator role. But when I connects it using command

```
Connect-ExchangeOnline -AccessToken $token -Organization company.onmicrosoft.com

// For creating access token I use 

$body =  @{
    Grant_Type    = “refresh_token”
    Scope         = "https://outlook.office365.com/.default"
    Client_Id     = $client_id
    Client_Secret = $secret
    Refresh_Token = $refresh_token
}

$connection = Invoke-RestMethod `
    -Uri https://login.microsoftonline.com/common/oauth2/v2.0/token `
    -Method POST `
    -Body $body

$token = $connection.access_token
```

but it gives me "OperationStopped: UnAuthorized" this error. While running using verbose parameter it gives me this.

VERBOSE: Returning precomputed version info: 3.1.0

VERBOSE: ModuleVersion: 3.1.0

VERBOSE: [ThreadID: #] Returning the provided AccessToken

VERBOSE: Failed to fetch banner content from server. Reason: Object reference not set to an instance of an object.

VERBOSE: ConnectionContext Removed

OperationStopped: UnAuthorized

Please help me out with it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-11*

Check this links and review the API permissions for the App:

https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps#step-5-assign-azure-ad-roles-to-the-application

https://techlabs.blog/categories/automation/solved-azure-powershell-runbook-error-failed-unauthorized-incorrect-permissions

https://techlabs.blog/categories/automation/connect-to-exchange-online-using-app-registration-and-certificate

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-12-07*

Hello , you can follow this steps:

Make a request to get the Token

```
Import-Module MSAL.PS
Import-Module ExchangeOnlineManagement
$graphAppId = 'APP_ID'
$graphAppSecret = ConvertTo-SecureString -String 'YOUR_SECRET_APP_AZURE' -AsPlainText -Force
$tenantId = 'TENANT_ID'
$tokenGraph = Get-MsalToken -ClientId $graphAppId -ClientSecret $graphAppSecret -TenantId $tenantId -Scopes "https://outlook.office365.com/.default"
```

Open the connection using the Token

```
Connect-ExchangeOnline -AccessToken $($tokenGraph.AccessToken) -AppId $graphAppI -Organization "YOUR_DOMAIN"
```
