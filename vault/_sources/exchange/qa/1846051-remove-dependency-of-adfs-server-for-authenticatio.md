---
title: "Remove Dependency of ADFS server for authentication of OWA and ECP of Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1846051/remove-dependency-of-adfs-server-for-authenticatio
question_id: 1846051
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Remove Dependency of ADFS server for authentication of OWA and ECP of Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1846051/remove-dependency-of-adfs-server-for-authenticatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 2 Hybrid server and 2 Edge server, but the authentication is redirected via WAP(ADFS) server.

We need to remove dependency from the ADFS server, what modification needs to do in Exchange Server. Currently we are having Windows Authentication and ADFS Authentication to True.  

We tried to move the authentication to Azure APP Proxy but 2016 donot support Hybrid modern Authentication.  

Then How to remove the dependency from ADFS.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-30*

Hi，@Sayantan Raha

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, do you want to disable the ADFS service?

Microsoft provides guidance on how to deactivate the ADFS service: Active Directory Federation Services (AD FS) decommission guide | Microsoft Learn

Exchange 2016 does not support Modern Authentication. To use Modern Auth, all servers used for client connections must have Exchange Server 2019 CU13 installed.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-29*

The commands will remove the ADFS dependency:.

If you dont want to use basic auth or forms based auth,  then set to $false for it.

Get-OwaVirtualDirectory -Server <server> | Set-OwaVirtualDirectory -BasicAuthentication $true -AdfsAuthentication $false -FormsAuthentication $true

Get-EcpVirtualDirectory -Server <server> | Set-EcpVirtualDirectory -AdfsAuthentication $false -BasicAuthentication $true -FormsAuthentication $true

followed by IISRESET
You can also clear the org config in Exchange ) set those values to $null 

 but its not required if you just want to set -AdfsAuthentication $false in the above commands

Set-OrganizationConfig -AdfsIssuer https://<FederationServiceName>/adfs/ls/ -AdfsAudienceUris "<OotwURL>","<EACURL>" -AdfsSignCertificateThumbprint "<Thumbprint>"

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-29*

Start with Step 6 and reverse the settings back to the default:

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019#step-6-configure-the-exchange-organization-to-use-ad-fs-authentication

Essentially:

Run commands in order:

Get-OwaVirtualDirectory -Server <server> | Set-OwaVirtualDirectory -BasicAuthentication $true  -AdfsAuthentication $false -FormsAuthentication $true

Get-EcpVirtualDirectory -Server <server> | Set-EcpVirtualDirectory -AdfsAuthentication $false  -BasicAuthentication $true -FormsAuthentication $true

 followed by IISRESET
