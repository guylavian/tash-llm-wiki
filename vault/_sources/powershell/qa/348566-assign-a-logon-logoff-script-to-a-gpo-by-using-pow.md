---
title: "Assign a logon/logoff script to a GPO by using PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348566/assign-a-logon-logoff-script-to-a-gpo-by-using-pow
question_id: 348566
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# Assign a logon/logoff script to a GPO by using PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348566/assign-a-logon-logoff-script-to-a-gpo-by-using-pow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can assign a script to a GPO by using Group Policy Management and Group Policy Management Editor, and i can use PowerShell to create a new GPO, and link it to an OU, setting the policy by using cmdlet Set-GPRegistryValue. But  I cannot find a way to assign a script to logon/logoff in the GPO.  

I had tried to create the directory \domain\sysvol\domain\gp-guid\User\Scripts\Logon, copy the script into it, and then create the scripts.ini file under the User\Scripts. After this, you can see the configuration in Group Policy Management Editor. However, this configuration is not showed in the "Setting" tab page of the GPO in Group Policy Management. Moreover, it is not applied to the target users.  

So, my question is how to assign a script to GPO by using PowerShell, or any other CLI tools?   

Thanks!

## Answers

_No answers on this thread._
