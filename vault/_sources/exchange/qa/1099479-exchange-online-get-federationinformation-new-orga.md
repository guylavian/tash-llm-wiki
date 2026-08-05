---
title: "Exchange Online: Get-FederationInformation / New-OrganizationRelationship"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1099479/exchange-online-get-federationinformation-new-orga
question_id: 1099479
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange Online: Get-FederationInformation / New-OrganizationRelationship

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1099479/exchange-online-get-federationinformation-new-orga (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

A customer has an Exchange hybrid configuration (Exchange 2019/Exchange Online).    

When partners want to create an OrganizationRelationship with our customer, the default domain (CUSTOMER.COM) does not work. To create the OrganizationRelationship you have to use another domain that the customer has. (e.g. TEST.CUSTOMER.COM or CUSTOMER.ONMICROSOFT.COM)    

If the OrganizationRelationship could be created, however, the default domain (CUSTOMER.COM) is always missing in the configuration and it must be added manually.    

If you execute the command Get-FederationInformation -domainname CUSTOMER.COM you will get an error message.    

Write-ErrorMessage : Ex15B18C|Microsoft.Exchange.Management.SystemConfigurationTasks.GetFederationInformationFailedException|Federation information could not be received from the external     

organization.    

If you execute the command Get-FederationInformation -domainname TEST.CUSTOMER.COM, you will get correct result with all DomainNames except CUSTOMER.COM domain.    

TargetApplicationUri  : outlook.com    

DomainNames           : {aaaa.com, ttttt.de, bbbbb.ch, nnnnnn.com...}    

TargetAutodiscoverEpr : https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc/WSSecurity    

TokenIssuerUris       : {urn:federation:MicrosoftOnline}    

IsValid               : True    

ObjectState           : Unchanged    

How can I update the Federation/FederationInformation?    

Regards    

Marc

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-09*

When you get Ex15B18C with Exchange Online and you are really using a valid domain (e.g. contoso.com), with my experience you need to open a Support Case with Microsoft and climb the escalation ladder, until the EXO PG can fix that behavior.
