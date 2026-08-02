---
title: "LDAP issue with powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3759258/ldap-issue-with-powershell
question_id: 3759258
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# LDAP issue with powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3759258/ldap-issue-with-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have created one PowerShell script to get the Active directory data. In which I used Active Directory Domain Services to get the data. 

I am using the JSON file to provide the Input.

The command is as below

"$allGroups = Find-LdapObject -SearchFilter $settings.ldapSettings.Filter -SearchBase $settings.ldapSettings.BasePath -LdapConnection $ADDPConnect

        -PageSize $settings.ldapSettings.PageSize -PropertiesToLoad $settings.ldapSettings.PropertiesToLoad -BinaryProperties $settings.ldapSettings.BinaryPropertiesToLoad"

but it giving me error "The object does not exist".

" ERROR: System.Management.Automation.MethodInvocationException: Exception calling "SendRequest" with "2" argument(s): "The object does not exist." ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object does not exist.

at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)

at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)

at CallSite.Target(Closure , CallSite , LdapConnection , Object , Object )

--- End of inner exception stack trace ---

at System.Management.Automation.ExceptionHandlingOps.CheckActionPreference(FunctionContext funcContext, Exception exception)

at System.Management.Automation.Interpreter.ActionCallInstruction`2.Run(InterpretedFrame frame)

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)

at System.Management.Automation.Interpreter.Interpreter.Run(InterpretedFrame frame)

at System.Management.Automation.Interpreter.LightLambda.RunVoid1T0

at System.Management.Automation.PSScriptCmdlet.RunClause(Action`1 clause, Object dollarUnderbar, Object inputToProcess)

at System.Management.Automation.PSScriptCmdlet.DoProcessRecord()

at System.Management.Automation.CommandProcessor.ProcessRecord()"

Am I missing something in this?

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-15*

Hello Paul,

Thank You for the advice

I have raised a question on forum.

Thank you

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2020-07-14*

Good day! I am Independent Advisor Paul R. and also a Microsoft/Windows user like you. Kindly post this query to our neighbor forum and link will be below.

There will be community members/IT Pros who are available that will be able to fulfill your query.

https://social.technet.microsoft.com/Forums/

Regards,

Paul R.
