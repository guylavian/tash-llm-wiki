---
title: "eventid 8229 error on Primary Domain Controller."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195426/eventid-8229-error-on-primary-domain-controller
question_id: 2195426
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# eventid 8229 error on Primary Domain Controller.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195426/eventid-8229-error-on-primary-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since November 2024 updates my PDC has been kicking out SPP errors:

Role: Primary Domain Controller

OS: Windows Server 2019

eventid 8229

eventsourcename  Software Protection Platform Service

"The rules engine failed to perform one or more scheduled actions.

Error Code:0x80070005

Path:SERIALIZE_INTERNAL

Arguments:"

I have checked online for solutions but have not found any that work. I know that this may be a hidden task for activation. Our licenses are Active Directory Based Activation.

Network Service has appropriate permissions.

Task Scheduler Service is running.

Anyone have a suggestion on what to look at or may be having the same issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-19*

Event ID 8229 is an error level. Active Directory Based Authentication is installed on this Domain Controller and it is my PDC. No other Domain Controller is showing this error. The Self account has the correct permissions. In addition, the Task Scheduler service is running, tasks are run with Network Service account, and the Network Service account has read access to the SPP folder.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-12*

Hello  

Greetings!  

Do you mean you only saw the event id 8229, but you do not se any problem in your environment?

Is event id 8229 warning instead of error? If so, you can keep morning later.

If there is any question, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-11*

I inherited this DC with Active Directory Based Activation already in place on it. I have already checked that the Self account has the correct privileges. I understand that error code is linked to the activation, but I am not getting any 'Access Denied' or failed activations.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-11*

Hello Jeffrey Boyles,

Thank you for posting in Microsoft Community forum.

Did you install Active Directory Based Activation on this Domain Controller?

What is the path?

Path:SERIALIZE_INTERNAL

Arguments:"

Here is a link for your reference.

Error 0x80070005 (Access denied) when you activate Windows - Windows Server | Microsoft Learn

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
