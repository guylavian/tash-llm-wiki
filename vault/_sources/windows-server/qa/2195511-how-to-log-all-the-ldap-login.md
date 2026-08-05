---
title: "How to log all the LDAP login ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195511/how-to-log-all-the-ldap-login
question_id: 2195511
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# How to log all the LDAP login ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195511/how-to-log-all-the-ldap-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to know the network systems are using LDAP protocol on the Windows Server 2016/2022 Domain Controllers.

I enable the NTDS Diagnostics settings to log the EventId 2889 which allow us to identify the ClientIP and Username of established LDAP sessions.

What I cannot find is a way to log all the LDAPs (636/tcp) sessions.

Enabling the NTDS Diagnostic:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics\15 Field Engineering = 5

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics\16 LDAP Interface Events = 5

I cannot find any useful detail about LDAPs sessions

Using a firewall or wireshark I find the SourceIP address without details of user account.

Is there any Windows settings to identify the client are logging on LDAPs protocol ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-10*

Hello  

Good day!  

After a lot of my researching, I only find information below about LDAPS on Domain Controller.

Event ID 1220 — LDAP over SSL (LDAPS) | Microsoft Learn

When you have issues with LDAPS, there are several different things that can be wrong. One of the best walkthrough documents regarding troubleshooting LDAPS is on the Ask DS Blog in which a Senior Escalation engineer walks through verification and troubleshooting: Troubleshooting LDAP over SSL. There is only one Event ID that is directly related to LDAP over SSL, which is Event 1220.

LDAP over SSL (LDAPS) Certificate | Microsoft Learn

Here is a similar thread for your references.

Whats using LDAPS, Check in event viewer. - Microsoft Q&A

Best Regards，  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-10*

Hello Daisy Zhou,

thanks again for your effort.

Unfortunately the EventIDs recorded on Security category do not report details to identify sessions established on LDAPS protocol

-  Use Event Viewer:

Once auditing is enabled, you can use the Event Viewer to view the logs.

-  Open Event Viewer (eventvwr.msc).

-  Navigate to `Windows Logs -&gt; Security`.

-  Look for events such as:

Event ID 4624: An account was successfully logged on.

Event ID 4648: A logon attempt was made with explicit credentials.

Event ID 4769: A Kerberos service ticket (TGS) was requested.

in case of the LDAPS session, an EventId 4624 record a generic Kerberos authentication without specify the protocol used by the client neither destination port 636 to recognize the LDAPS protocol.

EventId 4648 and 4869 are not generated during LDAPS session.

Also, Microsoft Defender for Identity is implemented on the system, useful to identify suspected activity but does not produce logs to identify LDAPS sessoin

-  Third-Party Tools:

You may also consider third-party solutions that can monitor and analyze LDAP traffic more effectively, such as:

Azure ATP / Microsoft Defender for Identity:

Provides monitoring and analysis of AD-related activities with detailed reporting.

Also LepideAuditor has not feature to identify LDAPS sessions

LepideAuditor:

Offers auditing and reporting on AD changes, including authentication activities.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-09*

Hello    

Greetings!

In addition to the information mentioned above, you can also refer to the following suggestions:

-  Use Event Viewer: 

Once auditing is enabled, you can use the Event Viewer to view the logs. 

-  Open Event Viewer (eventvwr.msc). 

-  Navigate to `Windows Logs -&gt; Security`. 

-  Look for events such as: 

Event ID 4624: An account was successfully logged on. 

Event ID 4648: A logon attempt was made with explicit credentials. 

Event ID 4769: A Kerberos service ticket (TGS) was requested. 

-  Third-Party Tools: 

You may also consider third-party solutions that can monitor and analyze LDAP traffic more effectively, such as: 

Azure ATP / Microsoft Defender for Identity:

Provides monitoring and analysis of AD-related activities with detailed reporting. 

LepideAuditor: 

Offers auditing and reporting on AD changes, including authentication activities. 

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-08*

Hello Daisy Zhou,

thank you very much for the suggestions provided but I still not reached the goal.

What we are looking for, is the identification of all LDAP clients are connecting with LDAPs protocol to the Windows Domain Controllers.

The needs is related the Root Certification Authority with the certificate is expiring soon, we need to know all the network devices (non Windows based) that are using LDAPs to update the Trusted Root CA.

It is very easy for LDAP protocol because Windows records the EventId 2889 with clear clientIP and username (setting the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics\16 LDAP Interface Events = 5), but it is very complex for LDAPS protocol (636/tcp) which seams not provide enough logs on the Event Viewer.

From out test, using ETW or WPR or WireSharek I was able to collect the encrypted packets which include the ClientIP details but without any information regarding the LDAPs sessions (username used, authentication success/failed, etc.)

Also the logman generate empty ETL files, without details

Setting up ETW for LDAP/LDAPS:

-  Open CMD or PowerShell as an Administrator.

-  Start the ETW trace:

logman create trace "LDAP_Trace" -p "Microsoft-Windows-LDAP-Client" 255 -o "C:\LDAP_Trace.etl" -ets

-  Reproduce the LDAPS activity you want to trace.

-  Stop the ETW trace:

logman stop "LDAP_Trace" -ets

-  Analyze the trace data using Windows Performance Analyzer (WPA), which comes with the Windows Performance Toolkit.

The Audit policies allow us to record the logon sessions, without details if the authentications are generated by kerberos protocol or LDAPs protocol

-  Additional logging:

If you need to track authentication events specifically, adjust the Domain Controller security policy:

-  Open the Group Policy Management Console (GPMC) and edit the Default Domain Controllers Policy.

-  Navigate to `Computer Configuration -&gt; Policies -&gt; Windows Settings -&gt; Security Settings -&gt; Advanced Audit Policy Configuration -&gt; Audit Policies -&gt; Logon/Logoff -&gt; Audit Logon`.

-  Enable "Success" for detailed auditing of logon events, including those over LDAPS.

By the way, I can use packet capture (like ETW, WPR, WireShark) to collect the client IP of each LDAPs session, I supposed there was a best way on Domain Controllers to collect details of LDAPs authentications

Any tips to collect from Active Directory Domain Controllers LDAPs authentications details is appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-25*

Hello castluca,

Thank you for posting in Microsoft Community forum.

To log and identify LDAP over SSL (LDAPS) sessions, you can use Event Tracing for Windows (ETW) for more detailed monitoring. While the NTDS Diagnostics settings you mentioned are helpful for LDAP logging, LDAPS sessions require additional setup. 

Here's a detailed approach to help you: 

-  Enable audit logging:

Enable LDAP Interface Events (event ID 2889) using the registry settings you mentioned. This enables informative logging but might not capture all LDAPS details required: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics\15 Field Engineering = 5 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics\16 LDAP Interface Events = 5 

-  ETW tracing for LDAPS:

Use Event Tracing for Windows (ETW) to capture detailed information. Install and configure Microsoft Message Analyzer (discontinued but still usable, or use Windows Performance Recorder (WPR) if you need a current tool). 

Setting up ETW for LDAP/LDAPS:

-  Open CMD or PowerShell as an Administrator. 

-  Start the ETW trace: 

logman create trace "LDAP_Trace" -p "Microsoft-Windows-LDAP-Client" 255 -o "C:\LDAP_Trace.etl" -ets 

-  Reproduce the LDAPS activity you want to trace. 

-  Stop the ETW trace:  

logman stop "LDAP_Trace" -ets 

-  Analyze the trace data using Windows Performance Analyzer (WPA), which comes with the Windows Performance Toolkit. 

-  Additional logging: 

If you need to track authentication events specifically, adjust the Domain Controller security policy: 

-  Open the Group Policy Management Console (GPMC) and edit the Default Domain Controllers Policy. 

-  Navigate to `Computer Configuration -&gt; Policies -&gt; Windows Settings -&gt; Security Settings -&gt; Advanced Audit Policy Configuration -&gt; Audit Policies -&gt; Logon/Logoff -&gt; Audit Logon`. 

-  Enable "Success" for detailed auditing of logon events, including those over LDAPS. 

-  Using Network Monitoring Tools: 

Wireshark and other network monitoring tools can help to identify the source IP addresses and ports but might lack detailed user information due to encryption. 

Combine these tools with ETW traces to correlate network activity with authenticated users. 

Note: Please test it in lab first, if it is OK, you can try to set them in production environment.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
