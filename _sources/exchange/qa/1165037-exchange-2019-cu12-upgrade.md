---
title: "Exchange 2019 CU12 upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165037/exchange-2019-cu12-upgrade
question_id: 1165037
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 CU12 upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165037/exchange-2019-cu12-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have ROOT and CHILD domain where Exchange2019 CU11 is installed in CHILD domain while schema role is in ROOT domain. All is running good without issue since a year ago. Currently, we're planning to upgrade from CU11 to CU12 and surprisingly we're hit with weird issue when try to perform upgrade, see below:

[ERROR] Setup encountered a problem while validating the state of Active Directory: Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master.  Run setup with the /prepareAD parameter on a computer in the domain "ROOT" and site "MAIN", and wait for replication to complete.  See the Exchange setup log for more information on this error.

My question, Do I need to run the /prepareAD again ? I have been running this command a year ago when we upgrade from Exchange 2016 to Exchange 2019. Is there any impact if running it again ? thank you ALL.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-01-29*

Did /PrepareSchema run succesfully for CU12? I wouldnt think it would have. You can check the Exchange Setup logs, but it does not hurt to re-run if you have already, however its not required because when you run PrepareAD, it will run PrepareSchema automatically, just be sure to run in the root domain where the schema master role is:

Run the command with necessary perms:

-  Your account needs to be a member of the Schema Admins and Enterprise Admins security groups. If you have multiple Active Directory forests, make sure you're logged into the right one.

for question 3, security updates are generally just updates for the Exch server binaries and rarely require schema changes. If they do , that will be called out in the documentation.
