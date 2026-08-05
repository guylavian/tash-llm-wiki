---
title: "ADFS DRS Service won't start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179283/adfs-drs-service-wont-start
question_id: 179283
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS DRS Service won't start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179283/adfs-drs-service-wont-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our Device Registration Service is unable to start and is impacting our WAP setup  

The error in the event log is below. Any ideas?  

The description for Event ID 0 from source Device Registration Service cannot be found. Either the component that raises this event is not installed on your local computer or the installation is corrupted. You can install or repair the component on the local computer.  

If the event originated on another computer, the display information had to be saved with the event.  

The following information was included with the event:  

Service cannot be started. System.InvalidOperationException: Metadata contains a reference that cannot be resolved: 'https://localhost/adfs/services/trust/mex'. ---> System.InvalidOperationException: There is an error in XML document (1, 1535). ---> System.ServiceModel.CommunicationException: The maximum message size quota for incoming messages (65536) has been exceeded. To increase the quota, use the MaxReceivedMessageSize property on the appropriate binding element. ---> System.ServiceModel.QuotaExceededException: The maximum message size quota for incoming messages (65536) has been exceeded. To increase the quota, use the MaxReceivedMessageSize property on the appropriate binding element.  

   --- End of inner exception stack trace ---  

   at System.ServiceModel.Channels.MaxMessageSizeStream.PrepareRead(Int32 bytesToRead)  

   at System.ServiceModel.Channels.MaxMessageSizeStream.Read(Byte[] buffer, Int32 offset, Int32 count)  

   at System.IO.BufferedStream.Read(Byte[] array, Int32 offset, Int32 count)  

   at System.Xml.EncodingStre...  

the message resource is present but the message is not found in the string/message table

## Answers

_No answers on this thread._
