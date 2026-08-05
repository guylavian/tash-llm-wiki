---
title: "DCdiag System logs is getting failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4244537/dcdiag-system-logs-is-getting-failed
question_id: 4244537
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# DCdiag System logs is getting failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4244537/dcdiag-system-logs-is-getting-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

On my DC I run AD healthchecks >"Dcdiag"  it getting failed on system logs.   

I have cleared replication logs and rebooted the server still persisting same issue. The replication is working fine. 

Below are the test results.,  

Directory Server Diagnosis 

Performing initial setup: 

   Trying to find home server... 

   Home Server = Test-DC1 

   * Identified AD Forest.  

   Done gathering initial info. 

Doing initial required tests 

   Testing server: ACT\Test-DC1 

```
Starting test: Connectivity 

     ......................... Test-DC1 passed test Connectivity
```

Doing primary tests 

   Testing server: ACT\Test-DC1 

```
Starting test: Advertising 

     ......................... Test-DC1 passed test Advertising 

  Starting test: FrsEvent 

     ......................... Test-DC1 passed test FrsEvent 

  Starting test: DFSREvent 

     ......................... Test-DC1 passed test DFSREvent 

  Starting test: SysVolCheck 

     ......................... Test-DC1 passed test SysVolCheck 

  Starting test: KccEvent 

     ......................... Test-DC1 passed test KccEvent 

  Starting test: KnowsOfRoleHolders 

     ......................... Test-DC1 passed test KnowsOfRoleHolders 

  Starting test: MachineAccount 

     ......................... Test-DC1 passed test MachineAccount 

  Starting test: NCSecDesc 

     ......................... Test-DC1 passed test NCSecDesc 

  Starting test: NetLogons 

     ......................... Test-DC1 passed test NetLogons 

  Starting test: ObjectsReplicated 

     ......................... Test-DC1 passed test ObjectsReplicated 

  Starting test: Replications 

     ......................... Test-DC1 passed test Replications 

  Starting test: RidManager 

     ......................... Test-DC1 passed test RidManager 

  Starting test: Services 

     ......................... Test-DC1 passed test Services 

  **Starting test: SystemLog**
```

```
**An error event occurred.  EventID: 0xC0001B63**
```

```
**Time Generated: 06/17/2021   02:51:56**
```

```
**Event String:**
```

```
**A timeout (30000 milliseconds) was reached while waiting for a transaction response from the UmRdpService service.**
```

```
**An error event occurred.  EventID: 0xC0001B63**
```

```
**Time Generated: 06/17/2021   02:52:26**
```

```
**Event String:**
```

```
**A timeout (30000 milliseconds) was reached while waiting for a transaction response from the ScDeviceEnum service.**
```

```
**An error event occurred.  EventID: 0xC0001B58**
```

```
**Time Generated: 06/17/2021   02:52:26**
```

```
**Event String:**
```

```
**The Smart Card Device Enumeration Service service failed to start due to the following error:**  

     ......................... Test-DC1 failed test SystemLog 

  Starting test: VerifyReferences 

     ......................... Test-DC1 passed test VerifyReferences
```

   Running partition tests on : ForestDnsZones 

```
Starting test: CheckSDRefDom 

     ......................... ForestDnsZones passed test CheckSDRefDom 

  Starting test: CrossRefValidation 

     ......................... ForestDnsZones passed test 

     CrossRefValidation
```

   Running partition tests on : DomainDnsZones 

```
Starting test: CheckSDRefDom 

     ......................... DomainDnsZones passed test CheckSDRefDom 

  Starting test: CrossRefValidation 

     ......................... DomainDnsZones passed test 

     CrossRefValidation
```

   Running partition tests on : Schema 

```
Starting test: CheckSDRefDom 

     ......................... Schema passed test CheckSDRefDom 

  Starting test: CrossRefValidation 

     ......................... Schema passed test CrossRefValidation
```

   Running partition tests on : Configuration 

```
Starting test: CheckSDRefDom 

     ......................... Configuration passed test CheckSDRefDom 

  Starting test: CrossRefValidation 

     ......................... Configuration passed test CrossRefValidation
```

   Running partition tests on : gang 

```
Starting test: CheckSDRefDom 

     ......................... gang passed test CheckSDRefDom 

  Starting test: CrossRefValidation 

     ......................... gang passed test CrossRefValidation
```

   Running enterprise tests on : gang.local 

```
Starting test: LocatorCheck 

     ......................... gang.local passed test LocatorCheck 

  Starting test: Intersite 

     ......................... gang.local passed test Intersite
```

Can you pls assist me on this.,

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-17*

Thank you Jazlyn ! to shows up right community group.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-17*

Hi Bkumar_007,

Thank you for posting your query in our community.

Based on your description, you have problem about Dcdiag command in Windows.

Since your problem is related to the Windows Command-Line Reference DCdiag, we suggest you can go to dedicated Microsoft Q & A community. The members there are good at this aspect. You will get a more detailed and professional answer to your query there.

We appreciate your understanding.

Best regards,

Jazlyn
