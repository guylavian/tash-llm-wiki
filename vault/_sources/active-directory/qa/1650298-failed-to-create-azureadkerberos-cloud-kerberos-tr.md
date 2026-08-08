---
title: "Failed to create AzureadKerberos (Cloud Kerberos Trust)‎"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1650298/failed-to-create-azureadkerberos-cloud-kerberos-tr
question_id: 1650298
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-identity-manager", "microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Failed to create AzureadKerberos (Cloud Kerberos Trust)‎

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1650298/failed-to-create-azureadkerberos-cloud-kerberos-tr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to establish cloud Kerberos trust to enable WHFB in our environment. However, it is giving below error. 

It gives error at command Set-AzureADKerberosServer. Any advise and suggestion will be highly appreciated. 

We have followed below link and commands. 

 

https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust?tabs=intune

 

-  install Required Module

 

Install the AzureADHybridAuthenticationManagement PowerShell module.

Install-Module -Name AzureADHybridAuthenticationManagement -AllowClobber

 

-  Setup Azure AD Kerberos server

 

Specify the on-premises Active Directory domain. A new Azure AD

Kerberos Server object will be created in this Active Directory domain.

$domain = $env:USERDNSDOMAIN

 

Enter an Azure Active Directory global administrator username and password.

$cloudCred = Get-Credential -Message 'An Active Directory user who is a member of the Global Administrators group for Azure AD.'

 

Enter a domain administrator username and password.

$domainCred = Get-Credential -Message 'An Active Directory user who is a member of the Domain Admins group.'

 

Create the new Azure AD Kerberos Server object in Active Directory

and then publish it to Azure Active Directory.

Set-AzureADKerberosServer -Domain $domain -CloudCredential $cloudCred -DomainCredential $domainCred

## Answers

_No answers on this thread._
