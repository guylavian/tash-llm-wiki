---
title: "Migrating active directory and pointing exchange to new active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193796/migrating-active-directory-and-pointing-exchange-t
question_id: 1193796
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Migrating active directory and pointing exchange to new active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193796/migrating-active-directory-and-pointing-exchange-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have migrated to the windows 2019 active directory server.

I have an exchange server 2019 which defaultGlobalCatalogsForAllForests, DefaultPreferredDomainControllers, DefaultConfigurationDomainControllersForAllForests are still pointing to the old active directory.

I already changed some other parameters like DefaultGlobalCatalog, PreferredDomainControllerForDomain, DefaultConfigurationDomainController, UserPreferredGlobalCatalog, UserPreferredConfigurationDomainController, UserPreferredDomainControllers to the new AD server.

any advice on how to configure the other 3 parameters?

Thanks

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-03-28*

please test before 

-  Open the Exchange Management Shell on your Exchange Server.

-  To set the new Active Directory server as the default global catalog for all forests, run the following command:
    Set-AdServerSettings -DefaultGlobalCatalog 'new-AD-server'
    Replace 'new-AD-server' with the FQDN of your new Active Directory server.

-  To set the new Active Directory server as the default preferred domain controller for all Exchange services, run the following command:
    Set-AdServerSettings -PreferredServer 'new-AD-server'
    Replace 'new-AD-server' with the FQDN of your new Active Directory server.

-  To set the new Active Directory server as the default configuration domain controller for all forests, run the following command:    Set-ExchangeServer -Identity 'your-Exchange-server' -StaticConfigDomainController 'new-AD-server'    Replace 'your-Exchange-server' with the name of your Exchange server, and 'new-AD-server' with the FQDN of your new Active Directory server.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-29*

Hi @Amir ，

The Set-AdServerSettings command syntax has no modifiable default parameters. According to my research, there is no need to change the parameters starting with "Default" to point to the new AD.

It is not recommend anyone to hardcode a domaincontroller in Exchange. 

Running Get-ExchangeServer | fl Name,domain should return $null values.

You can shutdown the old DC for a few days, then go to the application log and lock event ID 2080 to see if Exchange has "picked up" the new DC.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-29*

SMTP code "554 5.7.1" is a rejection from the receiving mail server and means email delivery is 'Not allowed' and that redelivery should not be attempted. A 5xx level status code indicates a "terminal" status, and SMG will not attempt to redeliver the message. 

-  Ensure that Messaging Gateway is scanning outbound messages for spam and that spam filters are updated.

-  Follow the standard recommendations for SMTP validation on your DNS records: implement Reverse DNS and Sender Policy Framework.

-  Ensure that your internal network is not compromised by ensuring local antivirus is installed and updated.

-  Ensure that the firewall only allows connections on port 25 to your antispam or mail servers. Also, ensure that outbound connections to port 25 are limited to SMG or other trusted mail sources.

-  Confirm that your externally facing IP address or network is not listed as a spam source.
