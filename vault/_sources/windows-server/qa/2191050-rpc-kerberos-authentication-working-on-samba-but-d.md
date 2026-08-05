---
title: "RPC Kerberos authentication working on Samba but dont Windows"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191050/rpc-kerberos-authentication-working-on-samba-but-d
question_id: 2191050
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# RPC Kerberos authentication working on Samba but dont Windows

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191050/rpc-kerberos-authentication-working-on-samba-but-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have implemented an RPC client in C# which uses GSS/SPNEGO authentication. I am trying to connect to the standard/Active Directory services (DRSAPI, SAMR etc...) on the server. The authentication works fine except when using Kerberos authentication and I've been struggling for 1 week now trying to troubleshoot the error.

The use cases are the following:

Samba NTLM => OK

Samba Kerberos => OK

Windows NTLM => OK

Windows (2012, 2016) Kerberos => KO

When trying Kerberos, the authentication to the KDC seems to work just fine, the ticket is obtained, but when trying to connect to the RPC service with the ticket (works on Samba), the server respond with a nca_s_fault_sec_pkg_error (again, only on Windows 2012) and I can't find what is rubbing Windows the wrong way. I am not an expert in Kerberos and there doesn't seem to be any entry in the event viewer. I compared Wireshark traces with a working and non working authentication and I can't see any differences.

Can someone please help me identify what the error is? Let me know if you need more information, I can provide Network traces and logs (samba, app, windows)

Here is a link to working (Samba) and non working (Windows 2012) wireshark traces of the exact same code with only the user password and the address of the server (Samba = 192.168.1.49 and W2K12 = 192.168.1.151) as differences

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-25*

Hello Frederic Kpama,  

Thank you for your reply.  

Did you see any error message on GUI when Kerberos authentication not work on Windows?  

Check Kerberos authentication differences between Samba and Windows.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Daisy and thank you for your response, below are my answer:

-  The server indeed reply an error response (code , see Wireshark traces for details), but I can't find any detail on the error (see below)

-  It may be the case, but what surprises me is that it works fine on a Samba server (see 3)

-  Yes, the code is exactly the same for all the use/test cases. The only differences are the user authentication and server information provided (i.e.: user password, domain, server address).

FYI, the development team is me :). This is an application specific code that I implemented for a client application and I'm not an expert so any documentation is also appreciated. The main problem I have is that I can't find any info or hint as to what causes this error (RPC protocol, Kerberos ticket, wrong SPN etc...).

Thanks for your help

For the error on the server, along side the pcap I provided, here is the event log entry I could find

And here is the details of the extended error returned in the RPC Alter_context response:

Computer: 2

Status: 0x0000000E, Process: 484, Loc: AcceptThirdLeg40, Component: 2, Date: <date>

Status: 0x80090300, Process: 484, Loc: AcceptThirdLeg20, Component: 3, Date: <date>

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Frederic Kpama,  

Thank you for posting in Microsoft Community forum.

1.Did you receive any error message "RPC Kerberos authentication working on Samba but dont Windows"?  

2.Not sure if the issue is related to Code in C#.  

3.If the Code is the same in the four scenarios below?  

Samba NTLM => OK

Samba Kerberos => OK

Windows NTLM => OK

Windows (2012, 2016) Kerberos => KO  

If no, you can try to consult with the development team that wrote this code and ask if they have any idea about this issue.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
