---
title: "Exchange Online Management v3.0.0 Connect-IPPSsession failing using CBA in Azure Automation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1072584/exchange-online-management-v3-0-0-connect-ippssess
question_id: 1072584
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-automation", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Exchange Online Management v3.0.0 Connect-IPPSsession failing using CBA in Azure Automation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1072584/exchange-online-management-v3-0-0-connect-ippssess (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Azure Automation Runbook that uses the Security and Compliance cmdlets that are in Exchange Online Management module to set retention policies for Teams.  We currently have version 2.0.6 Preview 7 loaded in Azure Automation.  The following code works with this version of the module:    

$org = "<domain>"    

$connection = get-automationconnection -name "AzureRunAsConnection"    

connect-exchangeonline -CertificateThumbPrint $connection.CertificateThumbprint -AppID $connection.ApplicationId -Organization $org    

Connect-IPPSSession -CertificateThumbPrint $connection.CertificateThumbprint -AppID $connection.ApplicationId -Organization $org    

Without changing the code in the runbook, if I upgrade to v3.0.0 of the Exchange Online Management module, the code results in the following error:    

Unable to load DLL 'IEFRAME.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E) (There was an error connecting to an Azure Resource. Error: Unable to load DLL 'IEFRAME.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E))    

What changed between version 2.0.6 preview 7 and version 3.0.0 that CBA would fail to work?    

I would love to use the managed identity instead but connect-ippssession does not support managed ids yet???   If I rewrite connect-ippssession with my own function and change the call to connect-exchangeonline to managed ID, the security and compliance cmdlets work just fine.  But that is for another QA.     

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-07*

In case anyone was interested, I received a response from Microsoft and there is an issue with the connect-ippssession cmdlet and using thumbprints.   They are working on resolving the issue - not sure if that means by the next release.    

They recommend using the certificate instead of the thumbprint.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-03*

I think the best way forward is if you open a service ticket in your tenant so this can get resolved ASAP. Based on the outcome, let me know if it can be called out in the docs.    

Please follow this link to contact support for business products: https://learn.microsoft.com/office365/admin/contact-support-for-business-products.
