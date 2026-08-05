---
title: "An Application using LDAP for Authentication - get Certificate Unknow - Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186473/an-application-using-ldap-for-authentication-get-c
question_id: 2186473
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# An Application using LDAP for Authentication - get Certificate Unknow - Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186473/an-application-using-ldap-for-authentication-get-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an application integrated with LDAP for Authentication.   

We have Secure LDAP configured and have exchanged Certificates.   

We are seeing some relatively Generic Errors logged in the application and a sniffer trace show some errors:   

We get a friendly Server Hello then a Fatal - Certificate Unknow error.   

This can happen once, twice or more After witch we Do get a successful connection, the authentication request completes and Life goes on...  

Any idea on what might generate this condition ?   

Any where to look on the LDAP servers ( Should I be able to find someone Over there to talk to ??? )   

Thanks, 

Don

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-10*

Hi Dead-Eye-Detective,

Thank you for posting in the Microsoft Community Forums.

The error you're encountering, a "Fatal - Certificate Unknown" error, typically indicates a problem with the server certificate during the SSL/TLS handshake process.  

It is possible that the intermittent errors are due to network fluctuations. Intermittent network problems or packet loss during an SSL/TLS handshake may cause the handshake to fail. Ensure that the network connection between the client application and the LDAP server is stable. 

A high load or resource constraints on the LDAP server may cause the handshake to fail. Monitor server performance during peak hours to identify any resource bottlenecks. 

It is normal for the LDAP server to report errors a small number of times occasionally, and you do not need to worry too much if you are not experiencing problems in your work environment. You can try to check the server at regular intervals to see if it continues to report errors for a long period of time, which would cause problems in your work environment. 

Best regards

Neuvi Jiang

============================================

If the answer is helpful, click "Accept Answer" and vote for it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hello Don,

In your image of the Wireshark trace, the port numbers are not visible in those lines where higher layer protocol data is available (e.g. TLS). That is why I needed to infer the direction of transfer of the TLS alert.

Since you posted in a Windows forum, I assumed that your platforms were Windows too. Obviously, "Event Tracing for Windows" is a Windows technology without an exact Unix equivalent.

My impression is that the problem is purely a client side issue. I doubt that any information available on the server side would help in the diagnosis.

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hello Gary, 

The direction of the packets ( conversation )  would be indicated by the source and destination ports.  

The origin would be on/from an ephemeral port ( any free port between 1024 and 65535 ** ) to the service port, which in our case for Secure LDAP would be the default of 636 ;)   

All the Clients are unix system which is why I had the packet capture ( tcpdump )  

( Wireshark on the windows system would give me the same data.)   

But I don't have access to the LDAP server - nor have we determined who managed it , or we would Enlist them in this troubleshoot.    

I have a test LAB - so I'll try and download - Microsoft-Windows-CAPI2 Event Tracing for Windows (ETW),  to see what insight it might be able to provide from the Target End !  

( Um,  It looks like this is done in the code ... ) 

Thank you for the suggestion. 

Don  

** Depending on how Strict you want to be -   

Ports with numbers 0–1023 are called system or well-known ports; ports with numbers 1024-49151 are called user or registered ports, and ports with numbers 49152-65535 are called dynamic, private or ephemeral ports.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hello Don,

It is a little difficult to be sure in which direction the packets in your Wireshark trace are travelling, but it looks to me as though the TLS alert is being raised by the client.

I would suggest using the Microsoft-Windows-CAPI2 Event Tracing for Windows (ETW) provider on the client to get more insight into the problem.

ETW providers can be controlled with various tools included in the base operating system (logman, netsh, pktmon, WPR, PowerShell, to name but a few).

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hello NeuviJ , you can call me Don, ( Or just Deadeye if you prefer :) )   

You stated:  

"The error you're encountering, a "Fatal - Certificate Unknown" error, typically indicates a problem with the server certificate during the SSL/TLS handshake process."   

Do you mean the server making the request or the LDAP Servers Cert ?   

For this one particular Application suite we have 11 identical Clients ( Not user - there are Many users connecting through these Client systems )  making the Authentication call and only One ( of 4 in a particular Data center ) are having / generating this issue.

Would anything be logged in the Event viewer that would document the problem on the LDAP servers side ?   

If I can find who administers , maybe they can have a look on their Side ? 

Thanks for the reply,   

Don
