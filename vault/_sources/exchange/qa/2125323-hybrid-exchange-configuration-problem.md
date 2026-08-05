---
title: "Hybrid exchange configuration problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125323/hybrid-exchange-configuration-problem
question_id: 2125323
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Hybrid exchange configuration problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125323/hybrid-exchange-configuration-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,

   I have setup Hybird exchange and trying to migrate on-premise mailbox to M365, and i found the following issue during the office 365 Hybrid configuration, and then i used Test-MigrationServerAvailability, it stated that AutoDiscover failed, amd i use exchange poweshell command to test communication with remote servers (please see bottom result), i dont know if i created correct DNS record for AutoDiscover in godaddy, please find below screenshot, any help would be appreicated

Hybrid Agent setup - validate hybrid agent for exchange usage error

HC.jpg

outlook connectivity test

connectivity test.jpg

godaddy CNAME autodiscovery record

dns1.jpg

godaddy SRV autodiscovery record

dns2.jpg

ping autodiscovery result

ping.jpg

Test-MigrationServerAvailability cmdlet in the Exchange Management Shell to test communication with the remote servers that hosts the mailboxes that you want to move

[PS] C:\Windows\system32>Test-MigrationServerAvailability -ExchangeRemoteMove -Autodiscover -EmailAddress *** Email address is removed for privacy *** -Credentials (Get-Credential) cmdlet Get-Credential at command pipeline position 1 Supply values for the following parameters: Credential RunspaceId : 52ce5014-d5a7-4ae0-9c81-83a5b7ed3b08 Result : Failed Message : AutoDiscover failed with a configuration error: The migration service failed to detect the migration endpoint using the Autodiscover service. Consider using the Exchange Remote Connectivity Analyzer (https://testexchangeconnectivity.com) to diagnose the connectivity issues. ConnectionSettings : SupportsCutover : False ErrorDetail : internal error:Microsoft.Exchange.Migration.AutoDiscoverFailedConfigurationErrorException: AutoDiscover failed with a configuration error: The migration service failed to detect the migration endpoint using the Autodiscover service. Consider using the Exchange Remote Connectivity Analyzer (https://testexchangeconnectivity.com) to diagnose the connectivity issues. at Microsoft.Exchange.Migration.DataAccessLayer.MigrationEndpointBase.InitializeFromAutoDiscove r(MigrationEndpoint presentationObject, SmtpAddress emailAddress, Boolean acceptUntrustedCertificates) at Microsoft.Exchange.Management.Migration.MigrationService.Endpoint.TestMigrationServerAvailab ility.InternalProcessExchangeRemoteMoveAutoDiscover() IsValid : True Identity : ObjectState : New

Keith

## Answers

_No answers on this thread._
