---
title: "Exchange 2016 Setup fails. Hybrid Exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1850887/exchange-2016-setup-fails-hybrid-exchange-2010
question_id: 1850887
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 Setup fails. Hybrid Exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1850887/exchange-2016-setup-fails-hybrid-exchange-2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one on-prem Exchange 2010 Hybrid server and a couple Hub Transport servers, and a Mailbox server. I'm trying to install an Exchange 2016 server so I can migrate off 2010.I'm running:

Setup.exe /PrepareAD /TenantOrganizationConfig d:\exchangeserver2016-cu23\MyTenantOrganizationConfig.xml /IAcceptExchangeServerLicenseTerms_DiagnosticDataON

I get:

A hybrid deployment with Office 365 has been detected. Please ensure that you are running setup with the /TenantOrganizationConfig switch. To use the TenantOrganizationConfig switch you must first connect to your Exchange Online tenant via PowerShell and execute the following command: "Get-OrganizationConfig | Export-Clixml -Path MyTenantOrganizationConfig.XML". Once the XML file has been generated, run setup with the TenantOrganizationConfig switch as follows "/TenantOrganizationConfig MyTenantOrganizationConfig.XML". If you continue to see this this message then it indicates that either the XML file specified is corrupt, or you are attempting to upgrade your on-premises Exchange installation to a build that isn't compatible with the Exchange version of your Office 365 tenant. Your Office 365 tenant must be upgraded to a compatible version of Exchange before upgrading your on-premises Exchange installation.

I've exported the xml file 2 times, so it isn't corrupt.  I've never seen anything about upgrading a O365 tenant.

How can I find the problem?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-09*

Hi @Kent Hanna,

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )     

--------------   

Issue Symptom: 

 A compatibility issue between  on-premises Exchange 2010 Hybrid server and the Exchange 2016 server trying to install

 

Resolution: 

There is an expired certificate on the Federation Trust. Remove the trust, export the XML again, and setup with the prepareAD switch was able to update the schema.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-01*

Try running setup without all that.

If this is a single domain AD forest, 

just run the 2016 setup wizard and let it update the schema , AD etc...

see if it fails after that. Ensure you running under the right perms

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/install-mailbox-role?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-01*

If you are trying to install Exchange 2016 in a hybrid environment with your existing Exchange 2010 server, it can be a complex process. You can refer this guide.

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-01*

Hi @Kent Hanna,

Welcome to the Microsoft Q&A platform!

According to your description, it sounds like you’re encountering a compatibility issue between your on-premises Exchange 2010 Hybrid server and the Exchange 2016 server you’re trying to install. Here are a few steps you can take to troubleshoot and resolve the issue:

-  Ensure that your Office 365 tenant is running a version of Exchange that is compatible with Exchange 2016. You can check the compatibility requirements on the Microsoft documentation.

-  Make sure you are using the latest version of the Hybrid Configuration Wizard. You can download it from the Exchange Online Admin Center.

-  Although you’ve already done this, try exporting the XML file again using the exact command provided:

-  Connect to your Exchange Online tenant using PowerShell:

```
$UserCredential = Get-Credential $Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection Import-PSSession $Session -DisableNameChecking
```

-  Export the Organization Configuration to an XML file:

```
Get-OrganizationConfig | Export-Clixml -Path MyTenantOrganizationConfig.xml
```

-  Ensure that the file is saved correctly and try to use a different path to avoid any possible path-related issues.

-  Double-check the setup command you are using. It should look like this:

```
Setup.exe /PrepareAD /TenantOrganizationConfig d:\exchangeserver2016-cu23\MyTenantOrganizationConfig.xml /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
```

-  Ensure your existing Exchange 2010 servers are fully up-to-date with the latest service packs and rollups. Also, make sure that the Exchange 2016 installation files are the latest available version.

Refer to: https://learn.microsoft.com/en-us/exchange/exchange-hybrid

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
