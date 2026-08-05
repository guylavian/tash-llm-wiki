---
title: "PowerShell / GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281040/powershell-gpo
question_id: 1281040
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# PowerShell / GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281040/powershell-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am attempting to run a PowwerShell script through Group Policy without success, I believe the issue my be that the script is not allowed to run freely on the PC's, I think I need to change the execution policy? I am running the following in the 'script Parameters' option

Powershell -ExecutionPolicy "bypass" -NoProfile -Command "\PATH TO PS1 FILE"

This is a script that will collect a detailed inentory of each PC at logon.

As of right now It will run successfully if I manually run it from a PC after PS prompts me to select 'R' to run once, But I have to right click on the file and run in powershell, if I simply double-click the file it will open in notepad.

I am fairly new to this process so any assistance would be appreciated. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-23*

To set the execution policy, you can use a Group Policy Object (GPO). In Group Policy Management Console (GPMC), navigate to:

-  Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Windows PowerShell.

-  Look for the setting: Turn on Script Execution.

Set it to Enabled and select the appropriate execution policy (e.g., "Allow all scripts"). This GPO will override the local execution policy.
When you're running scripts via Group Policy, it's common to use a login script or a startup script. Ensure that the script is being run in the context of the system account.

For login scripts:

-  User Configuration -> Policies -> Windows Settings -> Scripts (Logon/Logoff).

For startup scripts:

-  Computer Configuration -> Policies -> Windows Settings -> Scripts (Startup/Shutdown).

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-10*

Hello

Thank you for your question and reaching out.

Go to GPO -> Computer Configuration section -> Administrative Templates -> Windows Components -> Windows PowerShell -> Select  Allow all scripts

To run Powershell scripts using Group Policy, use the Powershell Scripts tab of the Group Policy Startup Scripts Properties page.

You can verify that the user logon script was executed successfully by the Event ID 5018u nder Microsoft-Windows-GroupPolicy/Operational section of Event Viewer.

--If the reply is helpful, please Upvote and Accept as answer--
