---
title: "Connect-ExchangeOnline started giving a strange error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1694872/connect-exchangeonline-started-giving-a-strange-er
question_id: 1694872
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-partner-center-api", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Connect-ExchangeOnline started giving a strange error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1694872/connect-exchangeonline-started-giving-a-strange-er (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I created a script in powershell to collect mailbox information from our tenants on Exchange Online. It stopped working somewhere aroung the 1st of May. Im going to explain what my process is in some detail and when the error occurs.

There are some prerequisites:

-  Import needed modules into Powershell: PartnerCenter, ExchangeOnlineManagement

-  Have an account ready from my CSP organization with Global Administrator on Azure

-  $CSPTenantGUID - Azure GUID from CSP organization

-  Registered an app and generated a secret string. Gathered the following information

-  $AzureAppGUID - the GUID of the registered application

-  $AzureAppSecret - the generated Secret of the registered application

-  $CSPCredential - generated new System.Management.Automation.PSCredential from $AzureAppGUID and $AzureAppSecret

-  Get certain scopes

-  $PartnerCenterScope = "https://api.partnercenter.microsoft.com/user_impersonation"

-  $ExchangeOnlineApplicationGUID = "a0c73c16-a7e3-4564-9a95-2bdf47383716"

-  $ExchangeOnlineScope = "https://outlook.office365.com/.default"

-  Get the customers GUIDs that I want to gather information on:

-  $CustomerMicrosoftGUID

The process I use is as follows:

-  Generate Access and Refresh tokens for Partner Center for our organisation (we are a CSP) using New-PartnerAccessToken.  

First interactive time:

```
New-PartnerAccessToken -ServicePrincipal -ApplicationId $AzureAppGUID -Credential $CSPCredential -Scopes $PartnerCenterScope -Tenant $CSPTenantGUID -UseAuthorizationCode
```

Every other time using previously generated and non-expired refresh token: 

```
New-PartnerAccessToken -ApplicationId $AzureAppGUID -RefreshToken $CSPPartnerRefreshToken -Scopes $PartnerCenterScope -Tenant $CSPTenantGUID -Credential $CSPCredential
```

-  Generate Access and Refresh tokens for Exchange Online for our organization using New-PartnerAccessToken:  

First interactive time:

```
New-PartnerAccessToken -Module ExchangeOnline
```

Every other time using refresh token: 

```
New-PartnerAccessToken -Module ExchangeOnline -ApplicationId $ExchangeOnlineApplicationGUID -RefreshToken $CSPExchangeRefreshToken -Scopes $ExchangeOnlineScope -Tenant $CSPTenantGUID
```

-  Generate Access and Refresh tokens for customer tenant using our CSP Exchange refresh token:

```
New-PartnerAccessToken -RefreshToken $CSPExchangeRefreshToken -Scopes $ExchangeOnlineScope -Tenant $TenantMicrosoftGUID -ApplicationId $ExchangeOnlineApplicationGUID
```

-  Connect to tenant Exchange Online:

```
Connect-ExchangeOnline -DelegatedOrganization $CustomerMicrosoftGUID -AccessToken $CustomerExchangeAccessToken -ShowBanner:$False -Verbose -EnableErrorReporting -LogDirectoryPath $LogPath -LogLevel All
```

Step #4 is where I get an error. When I use the -Verbose and -Debug parameters with the Connect-ExchangeOnline command I get the following error message:

```
VERBOSE: Returning precomputed version info: 3.4.0
VERBOSE: ModuleVersion: 3.4.0
VERBOSE: [ThreadID: #] Returning the provided AccessToken
VERBOSE: ConnectionContext Removed
Unexpected character encountered while parsing value: F. Path '', line 1, position 1.
At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.4.0\netFramework\ExchangeOnlineManagement.psm1:766 char:21
+                     throw $_.Exception;
+                     ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (:) [], JsonReaderException
    + FullyQualifiedErrorId : Unexpected character encountered while parsing value: F. Path '', line 1, position 1.
```

I have no clue what this error even means. I have used a JWT explorer to validate the token is okay, and all scopes are included, the signature is verified in HS256 alg. I have no clue where to continue my search for a solution.

Pls halp!

Thanks in advace.  

Peace!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

Found the issue:

https://techcommunity.microsoft.com/t5/exchange-team-blog/mfa-app-id-deprecation-in-exchange-online/ba-p/4036067
