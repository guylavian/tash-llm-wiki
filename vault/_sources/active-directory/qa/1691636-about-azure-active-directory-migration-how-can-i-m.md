---
title: "About Azure Active directory Migration. How can I migrate half of the users to another vm?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1691636/about-azure-active-directory-migration-how-can-i-m
question_id: 1691636
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# About Azure Active directory Migration. How can I migrate half of the users to another vm?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1691636/about-azure-active-directory-migration-how-can-i-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. About the situation, currently the Active Directory has 3000+ users on-premises. What I want do is to Migrate half the users to another Virtual machine/ server/ new environment. One way to put it is, Active Directory Migration on-premises to on-premises. So my questions are:

-  How can I do this? the over all process/ walk through or any documentation that i can follow?

-  What are the dependencies for these case?

-  Do I have to use any Migration tool?

-  What can be the important facts that I need to consider as a per-requisite before starting the migration process?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-05*

Hi Israt Jahan Tulin,

Thank you for posting in the Q&A Forums.

Before the migration begins you need to:

Define the scope of the migration. Define the number of users and objects to be migrated (e.g., users, groups, computers).

Assess the current environment. Examine the existing AD architecture, site and service configuration, group policies, and dependencies.

Determine the target environment. Design the new AD architecture, including domain, site, and service configurations.

Backup existing AD data. Ensure that a full AD backup is available in case something goes wrong during the migration.

Install and configure the new AD server: Install Windows Server in the target environment and configure it as a domain controller.

Synchronize time and network settings: Ensure that the time is synchronized between the new server and the existing environment and configure appropriate network settings.

Migrate users and other AD objects

Use the migration tool: You can use Microsoft's Active Directory Migration Tool (ADMT).

Create Trust Relationship: Establish a trust relationship between the source and target domains to securely migrate objects.

Migrate Users: Migrate user accounts, passwords, SID history, etc. using ADMT.

Migrate Groups and Computers: Migrate group and computer objects also using ADMT.

The prerequisites are as follows:

Evaluate and Backup: Before starting the migration, it is important to thoroughly evaluate the existing environment and ensure that a full backup is available.

Test Migration: Simulate the migration in a test environment to identify and resolve potential issues prior to the actual migration.

Documentation and planning: Detailed documentation of the migration plan, steps and configurations to ensure an organized migration process.

Training and communication: Ensure that the IT team is familiar with the migration tools and steps, and communicate the migration plan and possible impacts to relevant users and departments.

This article is about ADMT Migration Guide:https://www.microsoft.com/en-us/download/details.aspx?id=19188&

However, AD migration is not a simple process, and I suggest you seek offline help to be on the safe side.

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
