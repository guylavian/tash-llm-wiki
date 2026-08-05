---
title: "Scheduled Task to run powershell script via GPO(computer on a particular day)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/688234/scheduled-task-to-run-powershell-script-via-gpo-co
question_id: 688234
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Scheduled Task to run powershell script via GPO(computer on a particular day)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/688234/scheduled-task-to-run-powershell-script-via-gpo-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Reader,     

 How to create a scheduled task to run a powershell script whether user is logged on or not during a specific time via GPO.     

I have implemented it locally using the following settings(attached image), which prompts for the user account password while creating the scheduled task. And, the task executes perfectly.     

    

however, when i configure the same task using GPO, it doesn't apply the policy in the endpoint and it doesn't prompt for a user account password. But when i select "Run only when user is logged on" the task gets created via GPO but it doesn't perform the action.     

Any recommendation would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-11*

Hi there,    

You can use PowerShell cmdlets to create schedule tasks that automate the PowerShell script. It involves following steps,    

-Define time for the scheduler    

-Set Actions to be performed during execution    

-Save scheduler    

New-SchdeuledTaskTrigger creates a scheduled task trigger object. Using this cmdlet, you can specify the starting time of a task or starting a task multiple times on a daily or weekly basis.    

 $Time=New-ScheduledTaskTrigger -At 4.00PM -Once    

Here is a thread as well which discusses the same steps and you can try out some steps from this and see if that helps you to sort the Issue.    

https://learn.microsoft.com/en-us/answers/questions/609608/gmsa-scheduled-task-run-whether-user-is-logged-in.html    

--------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-09*

Hi,

If you'd like to set "Run whether user is logged on or not" at scheduled task's general tab, you need to set "NT AUTHORITY\SYSTEM" user. Please refer to related webpage below.

gpo-issue-deploying-a-scheduled-task-running-as-system
-> The only way I’ve found to work around this issue is to:  

-  Set the user as “NT AUTHORITY\SYSTEM” ～

If you'd like to set "Run only when user is logged on" at scheduled task's general tab, it is ok to set any users such as Domain\Administrator. But you need to enable execution of PowerShell in each client PC in advance, or PowerShell script may be failed to execute. 

I hope this information will be of use to you.

Best Regards,
Zaamasu
