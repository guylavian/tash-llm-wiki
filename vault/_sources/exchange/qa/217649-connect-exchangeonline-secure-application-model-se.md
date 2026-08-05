---
title: "Connect-ExchangeOnline  Secure Application Model set Culture"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/217649/connect-exchangeonline-secure-application-model-se
question_id: 217649
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Connect-ExchangeOnline  Secure Application Model set Culture

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/217649/connect-exchangeonline-secure-application-model-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I have setup »Secure Application Model« to connect o Exchange online for my automation scripts.  

Issue that I have is Culture. Im running under “CultureInfo de-DE” but return is En-US. This  has an issue with retuned date time format with generic error “Invalid datetime value for property”.  I solved  this issue setting Set-Culture -CultureInfo En-US.  

Question is, if there is workaround to set  Culture when connecting to exchanger online with app model.  Because this will effect other automation scripts, that run on system.  

Thank you,   

Borut

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-13*

@Borut Puhar       

Could you say how you got ExchangeOnlineManagement to connect using Secure Application Model? I've made it work with the v2 module, but not the ExchangeOnlineManagement module yet.    

```
# Get access token  
$CustomerExToken = New-PartnerAccessToken -Tenant $CustomerInitialDomain -ApplicationId $RefreshTokenIdentifier -RefreshToken $RefreshToken -Scopes 'https://outlook.office365.com/.default'  
$CustomerCredential = [PSCredential]::new(  
  $CustomerExToken.'Account'.'Username',  
  $(ConvertTo-SecureString -String ('Bearer {0}' -f ($CustomerExToken.'AccessToken')) -AsPlainText -Force)  
)  
          
# Connect  
$PSSession = New-PSSession -ConfigurationName 'Microsoft.Exchange' -ConnectionUri ('https://ps.outlook.com/powershell-liveid?DelegatedOrg={0}&BasicAuthToOAuthConversion=true' -f ($CustomerExToken.'TenantId')) -Credential $CustomerCredential -Authentication 'Basic' -AllowRedirection -WarningAction 'SilentlyContinue'  
  
# Import modules - Enter-PSSession if $RunFromOnprem      
$null = Import-PSSession $PSSession -DisableNameChecking -ErrorAction 'Stop'
```

Edit:    

-  https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps#setup-app-only-authentication    

So we must use certificates? But I don't want to..

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-05*

Hi,   

For example :  

Get-EXOMailboxFolderStatistics *****************  

Default  : Set-Culture -CultureInfo de-DE <- This is my default local language setting  

WARNING: Invalid datetime value for property CreationTime. Value= 11/25/2019 9:29:51 AM.  

WARNING: Invalid datetime value for property LastModifiedTime. Value= 12/23/2020 7:12:59 AM.  

Name                              : Calendar  

SearchFolder                      : False  

CreationTime                      :   

LastModifiedTime                  :   

FolderPath                        : /Calendar  

WARNING: Invalid datetime value for property CreationTime. Value= 11/25/2019 9:29:51 AM.  

Name                              : Contacts  

SearchFolder                      : False  

CreationTime                      :     <- 25/11/2019 woud be correct  

LastModifiedTime                  : 01.04.2021 20:13:05 **<- wrong 1.April. / 4. Januar **   

FolderPath                        : /Contacts  

No WARNING <- both are wrong for En-US  

Name                              : BIG  

SearchFolder                      : False  

CreationTime                      : 08.02.2020 17:34:14  <-this is  8th of Feb not  2th of Aug.  

LastModifiedTime                  : 01.05.2021 00:34:01  

FolderPath                        : /Inbox/BIG  

Now change to  Set-Culture -CultureInfo En-US  

Name                              : Calendar  

SearchFolder                      : False  

CreationTime                      : 11/25/2019 9:29:51 AM  

LastModifiedTime                  : 12/23/2020 7:12:59 AM  

FolderPath                        : /Calendar  

Name                              : Contacts  

SearchFolder                      : False  

CreationTime                      : 11/25/2019 9:29:51 AM  

LastModifiedTime                  : 1/4/2021 8:13:05 PM  

FolderPath                        : /Contacts  

Name                              : BIG  

SearchFolder                      : False  

CreationTime                      : 8/2/2020 5:34:14 PM  

LastModifiedTime                  : 1/5/2021 12:34:01 AM  

FolderPath                        : /Inbox/BIG
