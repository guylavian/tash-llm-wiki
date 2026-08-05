---
title: "Exchange 2016 Migration end point creation fail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1251444/exchange-2016-migration-end-point-creation-fail
question_id: 1251444
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 Migration end point creation fail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1251444/exchange-2016-migration-end-point-creation-fail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016, 1 server
Ran Hybrid Confi Wiz successfully. Ran it a second time just to be certain.
Trying to create the migration end point via the Migration Endpoint Wizard. It fails on auto discover and asks for the FQDN of the server that the MRS Proxy is on. When I enter the FQDN address I get the following error:
|error|error|
| -------- | -------- |
|The connection to the server 'ex2016.skld.net' could not be completedThe connection to the server 'server.company.net' could not be completed|

It does this with the firewall off or on. 
The command:   Get-WebServicesVirtualDirectory | FL Identity,MRSProxyEnabled   returns a TRUE result
Verified that TLS1.2 is enabled.
What am I missing??

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-24*

Please check this similar thread. See if you take insight from this thread - https://community.spiceworks.com/topic/2301316-exchange-2013-1000s-of-event-id-6-logs

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-24*

Hi @ Paul H，

On the Configuration Wizard page, is there a more detailed error report about this failure?

If not, you can run this Test-MigrationServerAvailability command in Exchange Online PowerShell to help you check for potential problems or error resolution.

Example:

```
Test-MigrationServerAvailability -ExchangeRemoteMove -Autodiscover -EmailAddress ******@contoso.com -Credentials (get-credential contoso\administrator)
```

In addition, this link provides solutions to the cause of the error: Troubleshooting Hybrid Migration Endpoints in Classic and Modern Hybrid - Microsoft Community Hub

Hope the above is helpful to you!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-21*

I get "True" returned on both and it still fails. 
MRSProxyEnabled          : True
WSSecurityAuthentication : True

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-04-21*

Hello @Paul H!
Welcome to Microsoft QnA 
I suggest these steps :
IF
Get-WebServicesVirtualDirectory -Identity "Server\EWS (default Web site)" |fl Server,MRSProxyEnabled,WSSecurityAuthentication is TRUE then you are good to go!
Otherwise :
https://learn.microsoft.com/en-us/exchange/troubleshoot/move-or-migrate-mailboxes/troubleshoot-migration-issues-in-exchange-hybrid#ensure-that-the-migration-endpoint-is-enabled-and-that-the-proper-authentication-options-are-in-place
So please sens us an update !
In casethi answer helped kindly mark it as Accepted!
BR
