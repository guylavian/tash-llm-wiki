---
title: "[Migrated from MSDN Exchange Dev]Event ID: 4625 & 4771"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143884/migrated-from-msdn-exchange-dev-event-id-4625-4771
question_id: 143884
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Event ID: 4625 & 4771

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143884/migrated-from-msdn-exchange-dev-event-id-4625-4771 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]    

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.    

As the former Non-developer Exchange forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.    

[MSDN Link]    

Event ID: 4625 & 4771    

[Original post]    

Hello,    

It was unclear on which forum to select.    

We have been starting to get a number of entries for event IDs: 4625 and 4771.  I see this article https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625 but it does not show how to correct this.    

It shows:    

Failure Information:    

```
Failure Reason:                 Unknown user name or bad password.  

            Status:                                  0xC000006D  

            Sub Status:                         0xC000006A
```

The users which show up in the event viewer are not entering the incorrect user name or password multiple times.  How can this be corrected?    

Thanks,    

Roger    

r

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

This is all set now.  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Hello Kael,    

Yes, the 4625 event is on the exchange server and the 4771 event is on the domain controller. The users changed their passwords in September and October.  When you say it may be resulting from cached credentials which are outdated on users' devices, are you saying on their PCs or mobile phones?  They both use their PCs each day and have exchange configured on their iphones which they use daily.      

I have checked the credential manager on one of the user's PC and do not see any cached credentials other than a generic windows credential "virtualapp/didlogical" which has the current date. This appears to be since I logged on to his PC.    

I also ran rundll32.exe keymgr.dll,KRShowKeyMgr and only the same  "virtualapp/didlogical" (windows live) credential appears.    

Our firewall doesn't indicate an attack. The syslog server doesn't indicate an attack.      

If it is from cached credentials, where else do I need to search to remove stale credentials. Yes, the IPs shown are for their PCs.    

Log Name:      Security    

Source:        Microsoft-Windows-Security-Auditing    

Date:          10/29/2020 6:09:18 AM    

Event ID:      4625    

Task Category: Logon    

Level:         Information    

Keywords:      Audit Failure    

User:          N/A    

Computer:      XXXX.XXXX.com    

Description:    

An account failed to log on.    

Subject:    

	Security ID:		NULL SID  

	Account Name:		-  

	Account Domain:		-  

	Logon ID:		0x0  

Logon Type:			3    

Account For Which Logon Failed:    

	Security ID:		NULL SID  

	Account Name:		XXXX@xxxxxxxxxxxxx  .com  

	Account Domain:		  

Failure Information:    

	Failure Reason:		Unknown user name or bad password.  

	Status:			0xC000006D  

	Sub Status:		0xC000006A  

Process Information:    

	Caller Process ID:	0x0  

	Caller Process Name:	-  

Network Information:    

	Workstation Name:	XXXX-PC  

	Source Network Address:	XXXX  

	Source Port:		61076  

Detailed Authentication Information:    

	Logon Process:		NtLmSsp   

	Authentication Package:	NTLM  

	Transited Services:	-  

	Package Name (NTLM only):	-  

	Key Length:		0  

This event is generated when a logon request fails. It is generated on the computer where access was attempted.    

The Subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.    

The Logon Type field indicates the kind of logon that was requested. The most common types are 2 (interactive) and 3 (network).    

The Process Information fields indicate which account and process on the system requested the logon.    

The Network Information fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.    

The authentication information fields provide detailed information about this specific logon request.    

	- Transited services indicate which intermediate services have participated in this logon request.  

	- Package name indicates which sub-protocol was used among the NTLM protocols.  

	- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.  

Event Xml:    

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">    

  <System>    

    <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" />  

    <EventID>4625</EventID>  

    <Version>0</Version>  

    <Level>0</Level>  

    <Task>12544</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x8010000000000000</Keywords>  

    <TimeCreated SystemTime="2020-10-29T10:09:18.063423700Z" />  

    <EventRecordID>97899359</EventRecordID>  

    <Correlation ActivityID="{037D9A44-A43C-0000-579A-7D033CA4D601}" />  

    <Execution ProcessID="672" ThreadID="708" />  

    <Channel>Security</Channel>  

    <Computer>XXXX.XXXX.com</Computer>  

    <Security />  

  </System>    

  <EventData>    

    <Data Name="SubjectUserSid">S-1-0-0</Data>  

    <Data Name="SubjectUserName">-</Data>  

    <Data Name="SubjectDomainName">-</Data>  

    <Data Name="SubjectLogonId">0x0</Data>  

    <Data Name="TargetUserSid">S-1-0-0</Data>  

    <Data Name="TargetUserName">XXXX@xxxxxxxxxxxxx  .com</Data>  

    <Data Name="TargetDomainName">  

    </Data>  

    <Data Name="Status">0xc000006d</Data>  

    <Data Name="FailureReason">%%2313</Data>  

    <Data Name="SubStatus">0xc000006a</Data>  

    <Data Name="LogonType">3</Data>  

    <Data Name="LogonProcessName">NtLmSsp </Data>  

    <Data Name="AuthenticationPackageName">NTLM</Data>  

    <Data Name="WorkstationName">XXXX-PC</Data>  

    <Data Name="TransmittedServices">-</Data>  

    <Data Name="LmPackageName">-</Data>  

    <Data Name="KeyLength">0</Data>  

    <Data Name="ProcessId">0x0</Data>  

    <Data Name="ProcessName">-</Data>  

    <Data Name="IpAddress">XXXX</Data>  

    <Data Name="IpPort">61076</Data>  

  </EventData>    

</Event>

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-29*

Hi,Roger.    

Since you posted the question in an Exchange forum,I suppose you have an Exchange server in your environment.    

Did you get the event 4625 on your Exchange server and event 4771 on the domain controller?    

Have the users in the event changed their passwords recently?    

If so,it may be resulted from cached credentials which are outdated in users' devices.    

Please have a check if it's the cause of the problem.    

Meanwhile,please also check if the source ip addresses in the event are actually used by the users.    

Or it may be an attack.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
