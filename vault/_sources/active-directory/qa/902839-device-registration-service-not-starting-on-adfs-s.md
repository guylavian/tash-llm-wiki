---
title: "Device Registration service not starting on adfs server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/902839/device-registration-service-not-starting-on-adfs-s
question_id: 902839
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Device Registration service not starting on adfs server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/902839/device-registration-service-not-starting-on-adfs-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I have a adfs server 2012 with a device registration service. The recent rebooting (after patching) caused it to refuse to start. I also enabled device write back on AD sync on another server, which might be related. I didn't do certificate renewing in recent days.    

Thanks for the help.    

Log Name:      Application    

Source:        Device Registration Service    

Date:          2022-06-23 7:31:10 PM    

Event ID:      0    

Task Category: None    

Level:         Error    

Keywords:      Classic    

User:          N/A    

Computer:      adfs-srvr01.......ca    

Description:    

The description for Event ID 0 from source Device Registration Service cannot be found. Either the component that raises this event is not installed on your local computer or the installation is corrupted. You can install or repair the component on the local computer.    

If the event originated on another computer, the display information had to be saved with the event.    

The following information was included with the event:     

Service cannot be started. The handle is invalid    

the message resource is present but the message is not found in the string/message table    

Event Xml:    

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">    

  <System>    

    <Provider Name="Device Registration Service" />  

    <EventID Qualifiers="0">0</EventID>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Keywords>0x80000000000000</Keywords>  

    <TimeCreated SystemTime="2022-06-24T02:31:10.000000000Z" />  

    <EventRecordID>414342</EventRecordID>  

    <Channel>Application</Channel>  

    <Computer>adfs......a</Computer>  

    <Security />  

  </System>    

  <EventData>    

    <Data>Service cannot be started. The handle is invalid</Data>  

  </EventData>    

</Event>

## Answers

_No answers on this thread._
