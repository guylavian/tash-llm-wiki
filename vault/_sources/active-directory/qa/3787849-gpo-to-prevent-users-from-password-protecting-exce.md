---
title: "GPO to prevent users from Password Protecting Excel files in O365/ Office 2019 and Office 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3787849/gpo-to-prevent-users-from-password-protecting-exce
question_id: 3787849
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# GPO to prevent users from Password Protecting Excel files in O365/ Office 2019 and Office 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3787849/gpo-to-prevent-users-from-password-protecting-exce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I used the GPO :  https://admx.help/?Category=Office2016&Policy=office16.Office.Microsoft.Policies.Windows::L\_DisablepasswordtoopenUI

I also manually tried this on another test client:

Registry Hive
HKEY_CURRENT_USER

Registry Path
software\policies\microsoft\office\16.0\common\security

Value Name
disablepasswordui

Value Type
REG_DWORD

Enabled Value
1

Disabled Value
0

But it did not work.  Users can still password protect the files.  This is causing a great deal of problems, with people leaving the company, etc. Or just multiple users and one password protects an Excel spreadsheet, etc.  Does anyone have a suggestion, or even a reason why the GPO doesn't work although I used the latest templates : admintemplates_x64_5140-1000_en-us  

Test client is running 20H2, and the Excel is Version 2102 (Build 13801.20294 Click-to-Run)

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2021-03-15*

Hello GaryOsbourne,

I'm John an Independent Advisor and a Microsoft user like you. I'll be happy to assist you today.

I want to apologize that this is just a consumer forum. Due to the scope of your question, I recommend posting your query on our sister forum Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue. They have IT experts there that can assist you better especially about Windows Servers, Active Directory and Group Policy configurations, etc.

Microsoft Site Q&A

https://docs.microsoft.com/en-us/answers/products/

Sincerely,

John DeV

Independent Advisor
