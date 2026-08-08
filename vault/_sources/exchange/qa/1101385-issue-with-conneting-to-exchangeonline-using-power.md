---
title: "Issue with conneting to ExchangeOnline using PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1101385/issue-with-conneting-to-exchangeonline-using-power
question_id: 1101385
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Issue with conneting to ExchangeOnline using PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1101385/issue-with-conneting-to-exchangeonline-using-power (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

Today morning I experience an issue with connecting ExchangeOnline using ExchangeOnlineManagement PowerShell module (I'm using 2.0.6-Preview6 version) from AzureFunction.    

For more than 20 minutes (6.45-7:05 UTC) I was getting ERROR: Your attempt to connect to this Exchange server was denied because your account isn't enabled for Remote PowerShell. Your Exchange administrator can use the Set-User -RemotePowerShellEnabled command to enable your account. errors. The problem occurred on tenant located in EU and also on other one located in US.    

It looks like a transient issue because later everything returned to normal without any intervention from my side.    

Am I wondering if I can check anywhere if any maintenance was done during that time and where can I check it?      

EU    

    

US    

    

Error message

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2022-11-23*

Check the Service Health Dashbord for your tenant:    

https://admin.microsoft.com/Adminportal/Home?source=applauncher#/servicehealth    

There was an issue that has since been resolved that may be related:    

Some users may have been unable to access the Exchange Online service via any connection method    

EX469330, Last updated: November 21, 2022 9:06 AM    

Start time: November 21, 2022 5:40 AM, End time: November 21, 2022 7:40 AM    

Final status: We’ve determined that an unexpected issue with a section of infrastructure, responsible for regulating user traffic throughout the affected infrastructure, was causing impact. Our automated recovery systems returned the service to acceptable performance thresholds, and we’ve confirmed via service monitoring telemetry that impact is remediated.    

Scope of impact: Impact was specific to some users who were served through the affected infrastructure in the Netherlands.    

If that wasnt your issue:  you can report it as well in that portal:
