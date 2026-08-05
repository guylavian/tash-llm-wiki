---
title: "[Migrated from MSDN Exchange Dev]Hybrid Configuration Wizard Failing to download updater agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/140614/migrated-from-msdn-exchange-dev-hybrid-configurati
question_id: 140614
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev]Hybrid Configuration Wizard Failing to download updater agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/140614/migrated-from-msdn-exchange-dev-hybrid-configurati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

[MSDN thread link] Hybrid Configuration Wizard Failing to download updater agent

Hello,

I am trying to rerun the HCW but its failing contacting MS for the updater agent. I am unable to reach the following sites

https://aka.ms/HybridWizardz and https://aka.ms/hybridagentinstaller I receive "this site cant be reached.

This is what the log says at AppData\Roaming\Microsoft\Exchange Hybrid Configuration

2020.10.26 17:38:44.877 10439 [Client=UX, fn=.ctor, Thread=20] Downloading https://hybridconfiguration.blob.core.windows.net/connector/MSHybridAutoUpdater.msi  

2020.10.26 17:38:47.789 ERROR 10318 [Client=UX, fn=.ctor, Thread=22]  

System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 13.88.145.64:443  

at System.Net.Sockets.Socket.InternalEndConnect(IAsyncResult asyncResult)  

at System.Net.Sockets.Socket.EndConnect(IAsyncResult asyncResult)  

at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-04*

https://learn.microsoft.com/en-us/answers/questions/27267/hcw-hybrid-agent-failing-to-register.html    

i hope it will help thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-04*

I recommend downloading and running the Wizard from a domain-joined regular workstation. There is no need to run in on the Exchange Server itself.   

You dont temporarily install the Wizard when you do this, it can be run from any domain-joined machine. Workstations are better since they typically do not have the same security restrictions and lock downs as a server.  All the Wizard is doing is setting the endpoints and configuration settings, there is no need to run this from any server.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

The issue is only with the exchange server, It has previously worked I do not know why it stopped. When I copy the file from another machine I get     

    

When I select more details I get this    

PLATFORM VERSION INFO    

	Windows 			: 10.0.14393.0 (Win32NT)  

	Common Language Runtime 	: 4.0.30319.42000  

	System.Deployment.dll 		: 4.8.3761.0 built by: NET48REL1  

	clr.dll 			: 4.8.3928.0 built by: NET48REL1  

	dfdll.dll 			: 4.8.3761.0 built by: NET48REL1  

	dfshim.dll 			: 10.0.14393.0 (rs1_release.160715-1616)  

SOURCES    

	Deployment url			: file:///C:/Users/adminga/Desktop/Microsoft%20Office%20365%20Hybrid%20Configuration%20Wizard.appref-ms%7C  

ERROR SUMMARY    

	Below is a summary of the errors, details of these errors are listed later in the log.  

	* Activation of C:\Users\adminga\Desktop\Microsoft Office 365 Hybrid Configuration Wizard.appref-ms| resulted in exception. Following failure messages were detected:  

		+ Downloading https://shcwreleaseprod.blob.core.windows.net/shcw/Microsoft.Online.CSE.Hybrid.Client.application did not succeed.  

		+ Unable to connect to the remote server  

		+ A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 52.239.237.36:443  

COMPONENT STORE TRANSACTION FAILURE SUMMARY    

	No transaction error was detected.  

WARNINGS    

	There were no warnings during this operation.  

OPERATION PROGRESS STATUS    

	* [11/4/2020 1:59:09 PM] : Activation of C:\Users\adminga\Desktop\Microsoft Office 365 Hybrid Configuration Wizard.appref-ms| has started.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-28*

Hello Joy,    

When I try to click the link https://aka.ms/HybridWizard  on my exchange server I get "shcwreleaseprod.blob.core.windows.net took too long to respond."     

    

I currently have HCW  version 17.0.4.544.0 but it fails and it has worked in the past. Disabling windows firewall did not help.     

its an on premise exchange server     

Edition             : Enterprise    

AdminDisplayVersion : Version 15.1 (Build 1979.3)    

This issue only applies to the exchange server I had to temporarily install HCW on another server to get mail flow to 365 going.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Hi，    

Are you going to download HCW? You could access the link here: https://aka.ms/HybridWizard    

For the error log you received below, I want to know more information about your environment.     

What's your on-premise Exchange server version?    

Where did you run the HCW? Did you configure any firewall in your environment? You could disable it temporarily and check the result again。    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
