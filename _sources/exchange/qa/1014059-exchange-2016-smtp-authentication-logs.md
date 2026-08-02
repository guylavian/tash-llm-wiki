---
title: "Exchange 2016 - SMTP authentication logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1014059/exchange-2016-smtp-authentication-logs
question_id: 1014059
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 - SMTP authentication logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1014059/exchange-2016-smtp-authentication-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

we are suffering a brute force attack via SMTP (port 587) and we would like to identify the public IP of such attack.    

Via ECP, the logging is enabled in verbose mode in bothreceive connectors, FrontendTransport and HubTransport.    

I checked the logs included in the official documentation without success.    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/protocol-logging?view=exchserver-2016    

Front End Transport service on Mailbox servers:    

Receive connectors: %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive    

Transport service on Mailbox servers:    

Receive connectors: %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpReceive    

could someone tell me how to find those remote authentication attempts?    

Many thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-20*

Hi again Andy. My problem is a bit more complex.     

The goal is indeed to know the remote client IP of the eSMTP connection so I started with the windows security logs. We did some tests and we see the windows for the logon failure but there is no trace of a remote IP. That is why we started looking for SMTP logs.    

LogName=Security    

SourceName=Microsoft Windows security auditing.    

EventCode=4625    

EventType=0    

Type=Information    

ComputerName=XXXX.yyy.zzz  (Exchange host)    

TaskCategory=Logon    

OpCode=Info    

RecordNumber=1004515810    

Keywords=Audit Failure    

Message=An account failed to log on.    

Subject:    

	Security ID:		NULL SID  

	Account Name:		-  

	Account Domain:		-  

	Logon ID:		0x0  

Logon Type:			3    

Account For Which Logon Failed:    

	Security ID:		NULL SID  

	Account Name:		testaccount  

	Account Domain:		  

Failure Information:    

	Failure Reason:		Unknown user name or bad password.  

	Status:			0xC000006D  

	Sub Status:		0xC0000064  

Process Information:    

	Caller Process ID:	0x0  

	Caller Process Name:	-  

Network Information:    

	Workstation Name:	WORKSTATION  

	Source Network Address:	-  

	Source Port:		-  

Then I looked into the logs in %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive but no traces of authentication in there.    

The external connection arrives to our first netscaler in our DMZ, then it jumps to our internal Netscaler and from there, to the exchange server.     

I looked into the netscaler logs and I could see layer3 traces, containing remote client and DMZ loadbalancer IP addresses . But that´s all, no layer 7 log is included.     

That is why I was expecting a SMTP log similar to what I can find for OWA, where the field X-forwarding field appears containing the original remote IP.    

But it seems like it does not exist. Do you have any idea on how I could managed to solve this ?    

thanks once again.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-20*

Ok, I thought you were looking for the remote IPs. the logon failures should show up in the regular standard security event log in event viewer.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-19*

I just tested this and if you enable logging on the client FrontEnd <server> receive connector ( that one that uses port 587), then its recorded here:    

 %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive
