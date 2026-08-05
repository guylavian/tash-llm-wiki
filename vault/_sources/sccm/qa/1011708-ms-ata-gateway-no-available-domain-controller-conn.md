---
title: "MS ATA Gateway - No Available Domain Controller Connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1011708/ms-ata-gateway-no-available-domain-controller-conn
question_id: 1011708
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# MS ATA Gateway - No Available Domain Controller Connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1011708/ms-ata-gateway-no-available-domain-controller-conn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Ran into this error and can't find any solutions, not even a fresh install.    

Installing ATA Center goes smoothly. Installing Lightweight Gateway on a DC goes smoothly. The error occurs when configuring the Gateway. Under Service Status, it repeatedly stops and restarts.    

Microsoft.Tri.Gateway reports: Warn [DirectoryServicesClient] Disconnected domain controller [DomainControllerDnsName=dc-name.domain.local] // Error [DirectoryServicesClient] There are no available domain controller connections, exiting.    

Microsoft.Tri.Gateway-Errors reports: Error [DirectoryServicesClient] There are no available domain controller connections, exiting.    

Need some help to figure out what I'm doing wrong, or what is going wrong here.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-09-16*

Take a look in the full gateway log.    

Not only the error log, and look for LDAP related warnings  that might explain why we are failing to open a connection to a DC
