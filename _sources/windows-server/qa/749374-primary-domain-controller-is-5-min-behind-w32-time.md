---
title: "Primary Domain Controller is 5 min behind - W32 Time Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/749374/primary-domain-controller-is-5-min-behind-w32-time
question_id: 749374
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Primary Domain Controller is 5 min behind - W32 Time Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/749374/primary-domain-controller-is-5-min-behind-w32-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello   

can you please help to correct the time on my primary domain controller it is 5-6 min faster than actual time i have windows 2019 primary domain and all clients takes the time from PDC but PDC doesn't show actual time it is 5-6 min faster   

when i try to update manually i am getting the following error  

All W32TM Commands Failing with W32TM Access is denied. (0x80070005)  

i am unable to stop the W32 service neither it accept other time command it says Access Denied   

Please help to solve the problem   

Regards,  

Ehsan

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-28*

Some GPO is also not working with the error code 0x80070005 Access is denied   

how to solve the above error code  

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-28*

Hello DS,

I found the below error system log in AD i dont know if it is related to time

Log Name: System  

Source: Microsoft-Windows-DistributedCOM  

Date: 2/28/2022 8:47:26 AM  

Event ID: 10036  

Task Category: None  

Level: Error  

Keywords: Classic  

User: NASCO\administrator  

Computer: PDC2019.nasco.local  

Description:  

The server-side authentication level policy does not allow the user NASCO\Administrator SID (S-1-5-21-4172167730-1548360163-1099057067-500) from address 192.168.21.100 to activate DCOM server. Please raise the activation authentication level at least to RPC_C_AUTHN_LEVEL_PKT_INTEGRITY in client application.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="Microsoft-Windows-DistributedCOM" Guid="{1B562E86-B7AA-4131-BADC-B6F3A001407E}" EventSourceName="DCOM" />  

<EventID Qualifiers="0">10036</EventID>  

<Version>0</Version>  

<Level>2</Level>  

<Task>0</Task>  

<Opcode>0</Opcode>  

<Keywords>0x8080000000000000</Keywords>  

<TimeCreated SystemTime="2022-02-28T05:47:26.303038600Z" />  

<EventRecordID>1001267</EventRecordID>  

<Correlation />  

<Execution ProcessID="1408" ThreadID="10036" />  

<Channel>System</Channel>  

<Computer>PDC2019.nasco.local</Computer>  

<Security UserID="S-1-5-21-4172167730-1548360163-1099057067-500" />  

</System>  

<EventData>  

<Data Name="Domain Name">NASCO</Data>  

<Data Name="User Name">Administrator</Data>  

<Data Name="SID">S-1-5-21-4172167730-1548360163-1099057067-500</Data>  

<Data Name="Client IP Address">192.168.21.100</Data>  

</EventData>  

</Event>

Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-24*

What's in the system event log?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-24*

Hi DS,  

When run those two commands again it's said access denied   

Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-24*

What is the result of?  

w32tm /query /source  

w32tm /query /configuration
