---
title: "Additional Domain controller W32time - Free-running System Clock"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1370517/additional-domain-controller-w32time-free-running
question_id: 1370517
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Additional Domain controller W32time - Free-running System Clock

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1370517/additional-domain-controller-w32time-free-running (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 1- PDC which has all role holds and 3 Additional DC.

PDC- Win 2008 R2 Ent

ADC- Win 2008 R2 Ent

ADC -DC01-Win2k12 R2

ADC-DC02-Win2k12 R2

I have External NTP Server. Our PDC - sync time from this NTP server.

PDC:- source of NTP is our NTP server. Configuration of PDC is..

C:\Users\administrator.IDMC>w32tm /query /configuration

[Configuration]

EventLogFlags: 2 (Local)

AnnounceFlags: 5 (Local)

TimeJumpAuditOffset: 28800 (Local)

MinPollInterval: 6 (Local)

MaxPollInterval: 10 (Local)

MaxNegPhaseCorrection: 172800 (Local)

MaxPosPhaseCorrection: 172800 (Local)

MaxAllowedPhaseOffset: 300 (Local)

FrequencyCorrectRate: 4 (Local)

PollAdjustFactor: 5 (Local)

LargePhaseOffset: 50000000 (Local)

SpikeWatchPeriod: 900 (Local)

LocalClockDispersion: 10 (Local)

HoldPeriod: 5 (Local)

PhaseCorrectRate: 7 (Local)

UpdateInterval: 100 (Local)

[TimeProviders]

NtpClient (Local)

DllName: C:\Windows\system32\w32time.dll (Local)

Enabled: 1 (Local)

InputProvider: 1 (Local)

CrossSiteSyncFlags: 2 (Local)

AllowNonstandardModeCombinations: 1 (Local)

ResolvePeerBackoffMinutes: 15 (Local)

ResolvePeerBackoffMaxTimes: 7 (Local)

CompatibilityFlags: 2147483648 (Local)

EventLogFlags: 1 (Local)

LargeSampleSkew: 3 (Local)

SpecialPollInterval: 3600 (Local)

Type: NT5DS (Local)

NtpServer (Local)

DllName: C:\Windows\system32\w32time.dll (Local)

Enabled: 1 (Local)

InputProvider: 0 (Local)

AllowNonstandardModeCombinations: 1 (Local)

VMICTimeProvider (Local)

DllName: C:\Windows\System32\vmictimeprovider.dll (Local)

Enabled: 1 (Local)

InputProvider: 1 (Local)

In Additional DC - Time Sync source is Free-running System Clock. Other DC -1 & DC-2 Sync time from ADC which source is not NTP or PDC.

in ADC-1

C:\Users\administrator.IDMC>w32tm /query /configuration

[Configuration]

EventLogFlags: 2 (Local)

AnnounceFlags: 5 (Local)

TimeJumpAuditOffset: 28800 (Local)

MinPollInterval: 6 (Local)

MaxPollInterval: 10 (Local)

MaxNegPhaseCorrection: 172800 (Local)

MaxPosPhaseCorrection: 172800 (Local)

MaxAllowedPhaseOffset: 300 (Local)

FrequencyCorrectRate: 4 (Local)

PollAdjustFactor: 5 (Local)

LargePhaseOffset: 50000000 (Local)

SpikeWatchPeriod: 900 (Local)

LocalClockDispersion: 10 (Local)

HoldPeriod: 5 (Local)

PhaseCorrectRate: 7 (Local)

UpdateInterval: 100 (Local)

[TimeProviders]

NtpClient (Local)

DllName: C:\Windows\system32\w32time.dll (Local)

Enabled: 1 (Local)

InputProvider: 1 (Local)

CrossSiteSyncFlags: 2 (Local)

AllowNonstandardModeCombinations: 1 (Local)

ResolvePeerBackoffMinutes: 15 (Local)

ResolvePeerBackoffMaxTimes: 7 (Local)

CompatibilityFlags: 2147483648 (Local)

EventLogFlags: 1 (Local)

LargeSampleSkew: 3 (Local)

SpecialPollInterval: 3600 (Local)

Type: NT5DS (Local)

NtpServer (Local)

DllName: C:\Windows\system32\w32time.dll (Local)

Enabled: 1 (Local)

InputProvider: 0 (Local)

AllowNonstandardModeCombinations: 1 (Local)

VMICTimeProvider (Local)

DllName: C:\Windows\System32\vmictimeprovider.dll (Local)

Enabled: 1 (Local)

InputProvider: 1 (Local)

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-09-19*

I'd suggest starting a case here with product support.        

https://support.serviceshub.microsoft.com/supportforbusiness         

--please don't forget to close up the thread here by marking answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-09-19*

I posted above the commands but it sounds like you may have some other issues. What's in the event logs? Sysvol and netlogon shares present?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-09-17*

Some general info

-  All domain members should use NT5DS domain time. 

-  Desktops and member servers sync with any domain controller. 

-  Domain controllers sync with PDC emulator (one per domain) 

-  PDC emulator in child domain can sync with any domain controller in parent domain. 

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/      

Might try resetting the problematic one.       

```
w32tm /unregister
net stop w32time
w32tm /register
net start w32time
w32tm /config /syncfromflags:domhier /update  
net stop w32time
net start w32time
```

then check

```
w32tm /query /source
w32tm /query /configuration
```

--please don't forget to close up the thread here by marking answer if the reply is helpful--
