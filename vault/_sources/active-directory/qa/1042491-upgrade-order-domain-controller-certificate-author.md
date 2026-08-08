---
title: "upgrade order domain controller, certificate authority server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1042491/upgrade-order-domain-controller-certificate-author
question_id: 1042491
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# upgrade order domain controller, certificate authority server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1042491/upgrade-order-domain-controller-certificate-author (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i need a instruction. i have two domain controllers on windows server 2008 and one certificate autohority server. i prepared domain controllers for upgrading, but i don't know what i must to upgrade first.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-12*

in-place upgrade is not recommended?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-10-10*

Hi,    

The process will be to upgrade one DC to the operating System that you are planning to upgrade, move the FSMO roles to the new OS DC, make sure you have backups and recovery options. Upgrade the other DC and retest all the authentication and DNS resolution.    

Backup the CA Server, system state backup, carry out in place upgrade or do a migration to another server with new OS. Windows 2003 server link but similar process to migrate migrate-CA-from-Windows-2003R2-to-2019-Server    

Hope this helps.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-10*

my certificate authority server is on virtual machine. can i copy the virtual machine. i make in-place upgrading on copied vm, and the ol vm i shut down, i start upgraded vm?
