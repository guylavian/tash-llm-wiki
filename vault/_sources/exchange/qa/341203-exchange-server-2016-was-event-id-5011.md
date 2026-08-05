---
title: "Exchange Server 2016 WAS Event ID 5011"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341203/exchange-server-2016-was-event-id-5011
question_id: 341203
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2016 WAS Event ID 5011

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341203/exchange-server-2016-was-event-id-5011 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We noticed this morning that our exchange server stopped receiving mail. When i checked event logs on the server i noticed several Warning in the event logs for Event ID 5011 WAS  

It seems that several AppPool suffered a fatal communication error with the windows process activation service.

What would cause this error and how can I resolve this one?  

We are running latest CU20 for Exchange 2016

I have included 1 sample of the event log.  

Log Name: System  

Source: Microsoft-Windows-WAS  

Date: 4/1/2021 4:25:03 AM  

Event ID: 5011  

Task Category: None  

Level: Warning  

Keywords: Classic  

User: N/A  

Computer: EXCHANGE.DOMAIN.local  

Description:  

A process serving application pool 'MSExchangeMapiFrontEndAppPool' suffered a fatal communication error with the Windows Process Activation Service. The process id was '4528'. The data field contains the error number.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="Microsoft-Windows-WAS" Guid="{524B5D04-133C-4A62-8362-64E8EDB9CE40}" EventSourceName="WAS" />  

<EventID Qualifiers="32768">5011</EventID>  

<Version>0</Version>  

<Level>3</Level>  

<Task>0</Task>  

<Opcode>0</Opcode>  

<Keywords>0x80000000000000</Keywords>  

<TimeCreated SystemTime="2021-04-01T09:25:03.024615800Z" />  

<EventRecordID>221001</EventRecordID>  

<Correlation />  

<Execution ProcessID="0" ThreadID="0" />  

<Channel>System</Channel>  

<Computer>EXCHANGE.DOMAIN.local</Computer>  

<Security />  

</System>  

<EventData>  

<Data Name="AppPoolID">MSExchangeMapiFrontEndAppPool</Data>  

<Data Name="ProcessID">4528</Data>  

<Binary>6D000780</Binary>  

</EventData>  

</Event>

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-02*

yes a reboot on the server does help.   

but why is this happening ?  

sometimes the CPU is high like 100% - is this the the cause of this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-02*

Hi @dirkdigs  

What changes have been made on your server recently? Please check if Exchange server has high CPU usage

You could follow below suggestions to resolve this issue:

1.try to recycle the application pool "MSExchangeMapiFrontEndAppPool" from IIS Manager. IIS Manager > Application Pools > MSExchangeMapiFrontEndAppPool > Recycle  

2.if not working, use the following cmdlet to reset IIS

```
iisreset /noforce
```

3.if not working, also try rebooting your sever

You may also check if the Microsoft Exchange Transport service and other transport related services are running properly on your server, we could restart them manually.

Some related official document about eventid 5011 for your reference as well:  

Event ID 5011 — IIS Application Pool Availability  

IIS Application Pool Crash and Debug Diag

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
