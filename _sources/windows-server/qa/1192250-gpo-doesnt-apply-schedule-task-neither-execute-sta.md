---
title: "GPO doesnt apply schedule task neither execute startup script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192250/gpo-doesnt-apply-schedule-task-neither-execute-sta
question_id: 1192250
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO doesnt apply schedule task neither execute startup script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192250/gpo-doesnt-apply-schedule-task-neither-execute-sta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Please help me, I'm getting crazy and I think I'm gonna suicide in the next days it this continue.

I need to execute a vbs script. The script works perfectly stored in local computer, then I put it on a shared folder, same shared folder for other apps that I want to deploy throught GPO and also works when I execute that in local computer.

I tried to deploy the script in 3 ways: 

-  I created policy to run script at startup, nothing happened;

-  I created policy to use a .cmd file to execute the vbs, nothing happened again;

-  I create a policy to do a schedule task to execute the cmd and unfortunately nothing happened again.

Looks like the policy doesn't apply, for example, the scheduled task was not even created.

I already did a gpresult and check in rsop.msc and the policy is applied.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-23*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to schedule task or Startup script not working.

-  Please Do not enable the Run in logged-on user's security context (user policy option) Common option when configuring user.

-  As you have mentioned  that script is not running even in from logon or startup script , please try to put some logs file to check where its stuck.

https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/whats-new/script-logging?view=powershell-7.3

-  Configure Logon Script Delay from GPO -> Computer Configuration\Administrative Templates\System\Group Policy\Configure Logon Script Delay  

-  Please also make sure User and Computer is placed in right OU or Security Group on which this GPO is applied.

Reference :

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/user-gpp-scheduled-task-item-fails-apply

--If the reply is helpful, please Upvote and Accept as answer--
