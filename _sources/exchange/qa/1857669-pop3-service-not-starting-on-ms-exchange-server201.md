---
title: "POP3 Service not starting on Ms Exchange Server2019 with error\"The Microsoft Exchange POP3 service on local computer started and then stopped...\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1857669/pop3-service-not-starting-on-ms-exchange-server201
question_id: 1857669
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# POP3 Service not starting on Ms Exchange Server2019 with error"The Microsoft Exchange POP3 service on local computer started and then stopped..."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1857669/pop3-service-not-starting-on-ms-exchange-server201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there, I'm having trouble starting POP3 Service on Ms Exchange Server2019 with error"The Microsoft Exchange POP3 service on local computer started and then stopped. Some services stop automatically if they are not in use by other services or program"

Any help please!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-11*

Hi Jake 

I have exactly the same problem with my 2019 exchange. I already had the same problem with the CU14, and it's still the case with the recent CU15.

Maybe you can help me.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-09*

Hi @Germain,

Welcome to the Microsoft Q&A platform!

I'm sorry to hear you're having trouble with the POP3 service on Microsoft Exchange Server 2019. Here are some steps you can follow to troubleshoot and resolve the issue:

-  Ensure that all necessary services that POP3 depends on are up and running. For instance, the Microsoft Exchange Active Directory Topology service must be running.

-  Verify that the POP3 service is correctly configured. Double-check the settings in the Exchange Admin Center (EAC) or use the Exchange Management Shell (EMS) to verify configurations.

-  Ensure that the ports used by the POP3 service (generally 110 for standard POP3 and 995 for secure POP3) are not being blocked by a firewall or used by another service.

-  Make sure that the credentials and authentication methods configured for the service are correct and have the necessary permissions.

-  Ensure that your Exchange Server and all related software are up to date with the latest patches and updates.

-  Check the configuration files for any errors or misconfigurations. Sometimes manual edits can cause problems.   Here's an example of a command you can use in the Exchange Management Shell to check the POP3 settings:

```
Get-PopSettings | Format-List
```

   This will display the current settings for the POP3 service. If you see anything unusual, you may want to reset it to default values and try starting the service again.

-  Sometimes, a simple server restart can resolve issues with services not starting correctly.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
