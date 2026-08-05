---
title: "Active Directory Administrator Center: Cannot Connect to Any Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2080653/active-directory-administrator-center-cannot-conne
question_id: 2080653
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Administrator Center: Cannot Connect to Any Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2080653/active-directory-administrator-center-cannot-conne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

How can I fix the "Cannot connect to any domain" error that I receive when opening the Active Directory Administrative Center? I have two servers and two domain controllers, and DNS is pointing to PDC itself and secondary DC points to PDC's IP address. The firewall is off, DFS Replication is active, and Active Directory Web Services is running on both servers. Active Directory Users and Computers work fine.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-27*

Good morning Daisy,

Thank you for your reply. I ran the two commands on my two servers 

nltest /dsgetdc:<domain NetBIOS name> /ws /force 

nltest /dsgetdc:<domain fully qualified DNS name> /ws /force

Both servers work properly. 

```
Server1:
      DC: \\DC1
 Address: \\192.168.100.180
 Dom Guid: xx
 Dom Name: test
 Forest Name: test.domain
 Dc Site Name: Default-First-Site-Name
 Our Site Name: Default-First-Site-Name
 Flags: GC DS LDAP KDC WRITABLE DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8
The command completed successfully

Server2:

       DC: \\DC2
 Address: \\192.168.100.181
 Dom Guid: xx
 Dom Name: test
 Forest Name: test.domain
 Dc Site Name: Default-First-Site-Name
 Our Site Name: Default-First-Site-Name
 Flags: GC DS LDAP KDC WRITABLE DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8 DS_9
The command completed successfully

--------------------------------------

I have checked the ports on both servers and ADWS are running. 
I found [Microsoft.ActiveDirectory.WebServices.exe] is listening different ports. 

Server1:
[svchost.exe]
TCP   0.0.0.0:5985   0.0.0.0   LISTENING   4
Can not obtain ownership information
TCP   0.0.0.0:9389   0.0.0.0   LISTENING   14312
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   0.0.0.0:17779  0.0.0.0   LISTENING   4
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   [::]:17779  [::]:0   LISTENING   4
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   127.0.0.1:59241  127.0.0.1:3268   ESTABLISHED    14312
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   127.0.0.1:59241  127.0.0.1:389   ESTABLISHED    14312
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   127.0.0.1:59375  127.0.0.1:59376  ESTABLISHED  3508

Server2:
[svchost.exe]
TCP   0.0.0.0:5985   0.0.0.0   LISTENING   4
Can not obtain ownership information
TCP   0.0.0.0:9389   0.0.0.0   LISTENING   3716
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   0.0.0.0:47001   0.0.0.0   LISTENING   4
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   [::]:47001   [::]:0   LISTENING   4
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   127.0.0.1:56333   127.0.0.1:3268   ESTABLISHED   3716
[Microsoft.ActiveDirectory.WebServices.exe]
TCP   127.0.0.1:56334   127.0.0.1:56335   TIME_WAIT   0
TCP   127.0.0.1:56340   127.0.0.1:56341   TIME_WAIT   0
TCP   127.0.0.1:57787   127.0.0.1:389     ESTABLISHED  1848
```

How should I solve this problem? Hope to hear from you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-27*

Hello Chris Fu,

Thank you for posting in Q&A forum.

The following errors are shown when no Active Directory Web Services instances are available: Expand table ErrorOperation"Cannot connect to any domain. Refresh or try again when connection is available"Shown at start of the Active Directory Administrative Center application"Cannot find an available server in the <NetBIOS domain name> domain that is running the Active Directory Web Service (ADWS)"Shown when trying to select a domain node in the Active Directory Administrative Center applicationTo troubleshoot this issue, use these steps:

-  Validate the Active Directory Web Services service is started on at least one domain controller in the domain (and preferably all domain controllers in the forest). Ensure that it's set to start automatically on all domain controllers as well.

-  From the computer running the Active Directory Administrative Center, validate that you can locate a server running ADWS by running these NLTest.exe commands:

nltest /dsgetdc:<domain NetBIOS name> /ws /force nltest /dsgetdc:<domain fully qualified DNS name> /ws /force If those tests fail even though the ADWS service is running, the issue is with name resolution or LDAP and not ADWS or Active Directory Administrative Center. This test fails with error "1355 0x54B ERROR_NO_SUCH_DOMAIN" if ADWS isn't running on any domain controllers though, so double-check before reaching any conclusions.

-  On the domain controller returned by NLTest, dump the listening port list with command:

Copy Netstat -anob > ports.txt Examine the ports.txt file and validate that the ADWS service is listening on port 9389. Example: Copy TCP    0.0.0.0:9389    0.0.0.0:0    LISTENING    1828 [Microsoft.ActiveDirectory.WebServices.exe] TCP    [::]:9389       [::]:0       LISTENING    1828 [Microsoft.ActiveDirectory.WebServices.exe] If listening, validate the Windows Firewall rules and ensure that they allow 9389 TCP inbound. By default, domain controllers enable firewall rule "Active Directory Web Services (TCP-in)". If not listening, validate again that the service is running on this server and restart it. Validate that no other process is already listening on port 9389.

-  Install NetMon or another network capture utility on the computer running Active Directory Administrative Center and, on the domain, controller returned by NLTEST. Gather simultaneous network captures from both computers, where you start Active Directory Administrative Center and see the error before stopping the captures. Validate that the client is able to send to and receive from the domain controller on port TCP 9389. If packets are sent but never arrive or arrive and the domain controller replies but they never reach the client, it's likely there's a firewall in between the computers on the network dropping packets on that port. This firewall may be software or hardware and may be part of third-party endpoint protection (antivirus) software.

For more information, please refer to link below.  

Advanced AD DS Management Using Active Directory Administrative Center (Level 200) | Microsoft Learn

Here is a similar thread for your reference.  

Active Directory Web Service is missing - Microsoft Community

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
