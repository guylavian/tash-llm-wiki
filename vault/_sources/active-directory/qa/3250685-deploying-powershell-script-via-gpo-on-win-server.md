---
title: "Deploying Powershell Script via GPO on Win Server 2008 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3250685/deploying-powershell-script-via-gpo-on-win-server
question_id: 3250685
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Deploying Powershell Script via GPO on Win Server 2008 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3250685/deploying-powershell-script-via-gpo-on-win-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,

I'm trying to deploy a PS script via GPO. 

I've tried to deploy it as a logon script and separately as a startup script.

It does not seem to execute the script.

When I try to run the script on my own machine I receive the following message:

Set-ExecutionPolicy : Windows PowerShell updated your execution policy successfully, but the setting is overridden by  

a policy defined at a more specific scope. Due to the override, your shell will retain its current effective  

execution policy of RemoteSigned. Type "Get-ExecutionPolicy -List" to view your execution policy settings. For more  

information please see "Get-Help Set-ExecutionPolicy".  

At line:1 char:46  

-  ... -ne 'AllSigned') { Set-ExecutionPolicy -Scope Process Bypass }; & '\ ...  

-                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

    + CategoryInfo         : PermissionDenied: (:) [Set-ExecutionPolicy], SecurityException  

    + FullyQualifiedErrorId : ExecutionPolicyOverride,Microsoft.PowerShell.Commands.SetExecutionPolicyCommand

When I elevate the permissions to admin, it works and I can run the script manually on the machine.

Is there any way in which I can deploy this so that it runs with elevated admin permissions?

Or is there something I need to change or add in order for this to run?

Thanks

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2019-10-23*

Hi Dwayne

Community is just a consumer forum, due to the scope of your question (Server 2008) can you please post this question to our sister forum on TechNet in the Server 2008 section (linked below)

Over there you will have access to a host of Server 2008 experts and will get a knowledgeable and quick answer to this question . .. 

https://social.technet.microsoft.com/Forums/win...
