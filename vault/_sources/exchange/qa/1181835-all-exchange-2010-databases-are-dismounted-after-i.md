---
title: "All Exchange 2010 databases are dismounted after Installing Exchange 2016 coexist 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181835/all-exchange-2010-databases-are-dismounted-after-i
question_id: 1181835
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# All Exchange 2010 databases are dismounted after Installing Exchange 2016 coexist 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181835/all-exchange-2010-databases-are-dismounted-after-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,

All Exchange 2010 databases are dismounted after Installing Exchange 2016 coexist 2010.

Please help me how to resolve this issue? sir.

Thank you in advance,

Tanisorn

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-20*

Hi @Tanisorn Sowudomsilp  ，

First, please check if TempDB exists under the exchange database path.

For a database that cannot be mounted, please run the following command in PowerShell as an administrator to check whether the database is in a Dirty Shutdown state or a Clean Shutdown state:

eseutil /mh "PATH TO EDB FILE\Database.EDB”

If the database is in a dirty shutdown state, run Eseutil/ml to check the log files. If the log file is functioning correctly, use Eseutil/r to repair the database. If the log file is unhealthy, use Eseutil/p.

In addition, if the public folder database is deleted in your environment, refer to the following link to remove the entry from ADSI to resolve Event ID: 2937

Exchange 2013 Troubleshooting: Event ID 2937 Public Folder database is pointing to the Deleted Objects container in Active Directory - TechNet Articles - United States (English) - TechNet Wiki (microsoft.com)

 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-17*

Do you have any solution? 

Thank you in advance,

Tanisorn
