---
title: "Network Policy Server: No Domain Controller Available"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2617618/network-policy-server-no-domain-controller-availab
question_id: 2617618
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Network Policy Server: No Domain Controller Available

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2617618/network-policy-server-no-domain-controller-availab (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When attempting to configure our domain controller as a Network Policy Server, I am receiving an error message stating that there is no domain controller available for domain K12.TX.US (which is the NETBIOS name of our domain).

Log Name:      System  

Source:        NPS  

Date:          3/7/2014 12:55:51 PM  

Event ID:      4402  

Task Category: None  

Level:         Error  

Keywords:      Classic  

User:          N/A  

Computer:      ADMIN-PDC.nederland.k12.tx.us  

Description:  

There is no domain controller available for domain K12.TX.US.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

  <System>  

    <Provider Name="NPS" />  

    <EventID Qualifiers="49152">4402</EventID>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Keywords>0x80000000000000</Keywords>  

    <TimeCreated SystemTime="2014-03-07T18:55:51.000000000Z" />  

    <EventRecordID>84518</EventRecordID>  

    <Channel>System</Channel>  

    <Computer>ADMIN-PDC.nederland.k12.tx.us</Computer>  

    <Security />  

  </System>  

  <EventData>  

    <Data>K12.TX.US</Data>  

  </EventData>  

</Event>

Please help, as I believe that this is causing the following error:

Log Name:      Security  

Source:        Microsoft-Windows-Security-Auditing  

Date:          3/7/2014 12:55:51 PM  

Event ID:      6273  

Task Category: Network Policy Server  

Level:         Information  

Keywords:      Audit Failure  

User:          N/A  

Computer:      ADMIN-PDC.nederland.k12.tx.us  

Description:  

Network Policy Server denied access to a user.  

Contact the Network Policy Server administrator for more information.  

User:  

Security ID:
NULL SID  

Account Name:
abusby  

Account Domain:
K12.TX.US  

Fully Qualified Account Name:
K12.TX.US\abusby  

Client Machine:  

Security ID:
NULL SID  

Account Name:

Fully Qualified Account Name:

OS-Version:

Called Station Identifier:
00-19-92-0C-E4-E9:NISD_Testing  

Calling Station Identifier:
B8-E8-56-A8-D4-D9  

NAS:  

NAS IPv4 Address:
10.250.1.15  

NAS IPv6 Address:

NAS Identifier:

NAS Port-Type:
Wireless - IEEE 802.11  

NAS Port:
0  

RADIUS Client:  

Client Friendly Name:
Testing Access Point  

Client IP Address:
10.250.1.15  

Authentication Details:  

Connection Request Policy Name:
BlueSocket Wireless Connections  

Network Policy Name:

Authentication Provider:
Windows  

Authentication Server:
ADMIN-PDC.nederland.k12.tx.us  

Authentication Type:
PEAP  

EAP Type:
Microsoft: Secured password (EAP-MSCHAP v2)  

Account Session Identifier:

Logging Results:
Accounting information was written to the local log file.  

Reason Code:
7  

Reason:
The specified domain does not exist.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

  <System>  

    <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" />  

    <EventID>6273</EventID>  

    <Version>1</Version>  

    <Level>0</Level>  

    <Task>12552</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x8010000000000000</Keywords>  

    <TimeCreated SystemTime="2014-03-07T18:55:51.061488000Z" />  

    <EventRecordID>3106129068</EventRecordID>  

    <Correlation />  

    <Execution ProcessID="584" ThreadID="4712" />  

    <Channel>Security</Channel>  

    <Computer>ADMIN-PDC.nederland.k12.tx.us</Computer>  

    <Security />  

  </System>  

  <EventData>  

    <Data Name="SubjectUserSid">S-1-0-0</Data>  

    <Data Name="SubjectUserName">abusby</Data>  

    <Data Name="SubjectDomainName">K12.TX.US</Data>  

    <Data Name="FullyQualifiedSubjectUserName">K12.TX.US\abusby</Data>  

    <Data Name="SubjectMachineSID">S-1-0-0</Data>  

    <Data Name="SubjectMachineName">-</Data>  

    <Data Name="FullyQualifiedSubjectMachineName">-</Data>  

    <Data Name="MachineInventory">-</Data>  

    <Data Name="CalledStationID">00-19-92-0C-E4-E9:NISD_Testing</Data>  

    <Data Name="CallingStationID">B8-E8-56-A8-D4-D9</Data>  

    <Data Name="NASIPv4Address">10.250.1.15</Data>  

    <Data Name="NASIPv6Address">-</Data>  

    <Data Name="NASIdentifier">-</Data>  

    <Data Name="NASPortType">Wireless - IEEE 802.11</Data>  

    <Data Name="NASPort">0</Data>  

    <Data Name="ClientName">Testing Access Point</Data>  

    <Data Name="ClientIPAddress">10.250.1.15</Data>  

    <Data Name="ProxyPolicyName">BlueSocket Wireless Connections</Data>  

    <Data Name="NetworkPolicyName">-</Data>  

    <Data Name="AuthenticationProvider">Windows</Data>  

    <Data Name="AuthenticationServer">ADMIN-PDC.nederland.k12.tx.us</Data>  

    <Data Name="AuthenticationType">PEAP</Data>  

    <Data Name="EAPType">Microsoft: Secured password (EAP-MSCHAP v2)</Data>  

    <Data Name="AccountSessionIdentifier">-</Data>  

    <Data Name="ReasonCode">7</Data>  

    <Data Name="Reason">The specified domain does not exist.</Data>  

    <Data Name="LoggingResult">Accounting information was written to the local log file.</Data>  

  </EventData>  

</Event>

## Answers

_No answers on this thread._
