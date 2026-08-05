---
title: "Drive mapping GPO take time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3194962/drive-mapping-gpo-take-time
question_id: 3194962
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Drive mapping GPO take time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3194962/drive-mapping-gpo-take-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

I've a drive mapping GPO. It takes more than 1 minute to logon. I've try several options (create/update/recreate) reconnect or not & wait network & logon without success. Now I've enable the GPO trace on my windows 10 laptop. I see more than 1 minute for
 ServiceIdleTimerCallback. Do you have an idea about the reason?

Regards

GPSVC(5a0.730) 15:38:32:999 PolicyApplicationState is False.

GPSVC(5a0.730) 15:38:32:999 lpGPInfoHandle->bValid is True.

GPSVC(5a0.730) 15:38:32:999 lpGPInfoHandle->dwExtnCount is 2.

GPSVC(5a0.730) 15:38:32:999 AsyncThreadsProcessing is True.

GPSVC(5a0.730) 15:38:32:999 CGPUserCollection::RWUnlock called

GPSVC(5a0.730) 15:38:32:999 Setting lock state as notLocked

GPSVC(5a0.730) 15:38:32:999 CGPUserCollection::RWUnlock exited with 0x0

GPSVC(5a0.730) 15:38:32:999 CGPApplicationService::IsAnEventProcessing.

GPSVC(5a0.730) 15:38:32:999 CGPService::IsServiceIdle: bPolicyProcessing=1. bEventProcessing=1. bLockInPlace= 1. bResult=0.

GPSVC(5a0.730) 15:38:32:999 ServiceIdleTimerCallback: Service is busy; not stopping.

GPSVC(5a0.217c) 15:39:49:761 ProcessGroupPolicyCompletedExInternal: Entering. Extension = {5794DAFD-BE60-433F-88A2-1A31939AC01F}, dwStatus = 0x0

GPSVC(5a0.217c) 15:39:49:762 ReadGPOList:++

GPSVC(5a0.217c) 15:39:49:762 ReadGPOList: Read Key:0

GPSVC(5a0.217c) 15:39:49:762 ReadGPOList:-- (Result:TRUE)

GPSVC(5a0.217c) 15:39:49:764 GetWbemServices: CoCreateInstance succeeded

GPSVC(5a0.217c) 15:39:49:766 ConnectToNameSpace: ConnectServer returned 0x0

GPSVC(5a0.217c) 15:39:49:767 ProcessGroupPolicyCompletedExInternal: Extension {5794DAFD-BE60-433F-88A2-1A31939AC01F} was able to log data. Error = 0x0, dwRet = 0. Clearing the dirty bit

GPSVC(5a0.217c) 15:39:49:768 CExtSessionLogger::Log: Didn't find an instance of the extension object when trying to set the dirty flag.

GPSVC(5a0.217c) 15:39:49:769 ProcessGroupPolicyCompletedExInternal: Finished processing extension <Group Policy Drive Maps> at 684390 ticks (ms)

GPSVC(5a0.217c) 15:39:49:769 ProcessGroupPolicyCompletedExInternal: Leaving. Extension = {5794DAFD-BE60-433F-88A2-1A31939AC01F}, Return status dwRet = 0x0

GPSVC(5a0.217c) 15:39:49:769 ProcessGPOList: Extension Group Policy Drive Maps returned 0x0.

GPSVC(5a0.217c) 15:39:49:770 ProcessGPOList: Extension Group Policy Drive Maps was able to log data. RsopStatus = 0x0, dwRet = 0, Clearing the dirty bit

## Answer (community) — community member

*upvotes: 0 · updated: 2019-05-23*

For information it was with the commande line gpupdate /force. After a reboot I've got:

GPSVC(58c.1c98) 15:55:31:562 ProcessGPOList: lpGPOInfo->lpGPInfoHandle->dwExtnCount is 2 for Group Policy Drive Maps.

GPSVC(1c18.1c30) 15:55:32:382 CGPNotify::UnregisterNotification: Entering with event 0000000000000488

GPSVC(1c18.1c30) 15:55:32:382 CGPNotify::UnregisterNotification: Exiting with dwStatus = 0x0

GPSVC(1ee4.1efc) 15:55:45:872 CGPNotify::RegisterForNotification: Entering with target Machine and event 0000000000000528

GPSVC(1ee4.1efc) 15:55:45:872 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(1ee4.1efc) 15:55:45:873 CGPNotify::RegisterForNotification: Entering with target User and event 000000000000056C

GPSVC(1ee4.1efc) 15:55:45:873 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(1ae8.1fc8) 15:56:06:752 CGPNotify::RegisterForNotification: Entering with target Machine and event 00000000000003C0

GPSVC(1ae8.1fc8) 15:56:06:752 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(1ae8.1fc8) 15:56:06:752 CGPNotify::RegisterForNotification: Entering with target User and event 0000000000000278

GPSVC(1ae8.1fc8) 15:56:06:752 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Entering with target User and event 0000000000001708

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Entering with target User and event 0000000000001480

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Entering with target User and event 0000000000000CB8

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Entering with target User and event 00000000000017F0

GPSVC(36c.3bc) 15:56:09:387 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(2048.2064) 15:56:15:578 CGPNotify::RegisterForNotification: Entering with target Machine and event 0000000000000438

GPSVC(2048.2064) 15:56:15:578 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(2048.2064) 15:56:15:578 CGPNotify::RegisterForNotification: Entering with target User and event 0000000000000484

GPSVC(2048.2064) 15:56:15:578 CGPNotify::RegisterForNotification: Exiting with status = 0

GPSVC(58c.1c98) 15:56:59:962 ProcessGroupPolicyCompletedExInternal: Entering. Extension = {5794DAFD-BE60-433F-88A2-1A31939AC01F}, dwStatus = 0x0

GPSVC(58c.1c98) 15:56:59:962 ReadGPOList:++

GPSVC(58c.1c98) 15:56:59:978 ReadGPOList: Read Key:0

GPSVC(58c.1c98) 15:56:59:978 ReadGPOList:-- (Result:TRUE)

GPSVC(58c.1c98) 15:56:59:978 GetWbemServices: CoCreateInstance succeeded
