---
title: "Sync exchange on cloud with on-premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2120302/sync-exchange-on-cloud-with-on-premise
question_id: 2120302
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Sync exchange on cloud with on-premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2120302/sync-exchange-on-cloud-with-on-premise (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI,

in my company when i must create  a new mail, i buy a licence on microsoft 365 and i find the mail both on the cloud and on premise.

Lately we have problems with two mail , we can find they on cloud but the mail are not created on premise.

There is a way to sync admin exchange on cloud with on premise ? Can i force the process ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-19*

Hello, @StefanoB,

Welcome to the Microsoft Q&A platform!

You can sync your on-premises Exchange with Exchange Online using a hybrid deployment. This setup allows you to manage both environments as a single entity. Here are the steps to enable and force the synchronization:

1.Prerequisites: Ensure that all prerequisites are met and that your provisioning agent is up to date before the configuration.

2.Set Up Hybrid Configuration: Use the Hybrid Configuration Wizard (HCW) to configure your hybrid environment. You can download and run HCW from the Exchange Admin Center in your Office 365 portal.

3.Enable Exchange Hybrid Writeback: Sign in to the Microsoft Entra admin center as a Hybrid Administrator and enable Exchange Hybrid Writeback with the help of https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/exchange-hybrid#how-to-enable.

4.Force Synchronization: Force the synchronization of Active Directory objects with Office 365 using the following PowerShell cmdlet. This command initiates a delta sync, which synchronizes only the changes since the last sync.

```
Start-ADSyncSyncCycle -PolicyType Delta
```

5.Provisioning On-Demand: Sign in to the Microsoft Entra admin center, navigate to your configuration, and use the Provision on demand feature by following https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/exchange-hybrid#provisioning-on-demand.

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
