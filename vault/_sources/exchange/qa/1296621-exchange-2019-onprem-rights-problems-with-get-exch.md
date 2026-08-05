---
title: "Exchange 2019 onprem: rights problems with Get-ExchangeDiagnosticInfo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1296621/exchange-2019-onprem-rights-problems-with-get-exch
question_id: 1296621
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 onprem: rights problems with Get-ExchangeDiagnosticInfo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1296621/exchange-2019-onprem-rights-problems-with-get-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
According to MS we need to use Get-ExchangeDiagnosticInfo to check Back Pressure. I want to automate that with a script running in task scheduler.
Understanding back pressure | Microsoft Learn

The user must have one of these roles:

Get-ManagementRole -Cmdlet Get-ExchangeDiagnosticInfo
Name                    RoleType
----                    --------
Support Diagnostics     SupportDiagnostics
View-Only Configuration ViewOnlyConfiguration
O365SupportViewConfig   O365SupportViewConfig

The User is in "View-Only Configuration" and for testing i made a new admin roll copying "View-Only Organization Management" and add "Support Diagnostics" to this new admin role.

When I use a user in "Organization Management" to check for back pressure, all is fine. But a user only in the roles I mentioned gets an error:

[xml]$bp=Get-ExchangeDiagnosticInfo -Server testserver -Process EdgeTransport -Component ResourceThrottling; $bp.Diagnostics.Components.ResourceThrottling.ResourceTracker.ResourceMeter 

The output is empty.
I checked the details:

PS C:\it\scripts\Exchange> $bp
Diagnostics
-----------
Diagnostics

So, we have some values. Lets go deeper:

PS C:\it\scripts\Exchange> $bp.Diagnostics | ft -wrap

error                            action                     message
-----                            ------                     -------
ProcessAccessManager RPC Error 5 Query registered processes Error 0x5 (Access is denied) from RunProcessCommand
                                                            EEInfo: ComputerName:
                                                            EEInfo: ProcessID: 14004
                                                            EEInfo: Generation Time: 6/2/2023 8:03:12 AM
                                                            EEInfo: Generating component: 2
                                                            EEInfo: Status: 0x00000005
                                                            EEInfo: Detection location: 1750
                                                            EEInfo: Flags: 0
                                                            EEInfo: NumberOfParameters: 1
                                                            EEInfo: prm[0]: Long: 5 (0x00000005)

I run the command on a member server with installed Exchange Shell, not directly on an Exchange server. That worked so far without any problems. The RPC error seems to point to a problem with this method, but an admin user can run the command the same way with no errors and output (example below). So what rights is my user missing to run it?

Resource            : PrivateBytes
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=75 HighToMedium=73 LowToMedium=72 MediumToLow=71]
Pressure            : 0

Resource            : SystemMemory
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=94 HighToMedium=89 LowToMedium=88 MediumToLow=84]
Pressure            : 42

Resource            : UsedVersionBuckets[C:\Program Files\Microsoft\Exchange
                      Server\V15\TransportRoles\data\Queue\mail.que]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=1500 HighToMedium=1000 LowToMedium=999 MediumToLow=800]
Pressure            : 1

Resource            : JetSessions[C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue\mail.que]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=1500 HighToMedium=1400 LowToMedium=1000 MediumToLow=900]
Pressure            : 9

Resource            : CheckpointDepth[C:\Program Files\Microsoft\Exchange
                      Server\V15\TransportRoles\data\Queue\mail.que]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=300 HighToMedium=280 LowToMedium=250 MediumToLow=230]
Pressure            : 0

Resource            : DatabaseUsedSpace[C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=99 HighToMedium=97 LowToMedium=96 MediumToLow=94]
Pressure            : 55

Resource            : UsedDiskSpace[C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=99 HighToMedium=94 LowToMedium=90 MediumToLow=88]
Pressure            : 56

Resource            : UsedDiskSpace[C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data]
CurrentResourceUse  : Low
PreviousResourceUse : Low
PressureTransitions : [PressureTransitions: MediumToHigh=99 HighToMedium=94 LowToMedium=90 MediumToLow=88]
Pressure            : 56
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-20*

I give up now. It only works when the user is member of the admin role "organization management". I tried to add make a new admin role and assigned all kind of rule combinations, it does simply not work.

Since a task user will never be assigned full rights in our exchange server, we simply cant monitor back pressure this way. Why Microsoft does not honor the assigned roles it explains to be needed for this command i really don't understand. It's the first time this happened and I use tasks and scripting a lot with exchange. Feels like a bug.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-20*

IT sadly got worse.  After the tasked script ran for a few days on the exchange server directly, it has now the same error

error                            action                     message  

ProcessAccessManager RPC Error 5 Query registered processes Error 0x5 (Access is denied) from RunProcessCommand ...

Running the command as domain admin still works fine.  

Now I have no idea anymore.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-15*

I made another test and run the script directly on the exchange servers (without local admin rights).

That worked. So the new question is: which rights does a user need to to execute "[xml]$bp=Get-ExchangeDiagnosticInfo -Server testserver -Process EdgeTransport -Component ResourceThrottling; $bp.Diagnostics.Components.ResourceThrottling.ResourceTracker.ResourceMeter" from a remote Exchange management shell.

I don't have problems to execute other commands with this user, eg get mailbox infos. Only this one command gives me troubles.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-15*

Sadly adding the user to the local administrator group of the exchange server did not solve the problem. Same error as described above.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-05*

Hi @TRÖSTER Joachim

You can try to add your user to the local administrator group, and then open EMS as an administrator to run Get-ExchangeDiagnosticInfo.

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
