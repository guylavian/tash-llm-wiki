---
title: "no certificate in newly created domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/492148/no-certificate-in-newly-created-domain-controller
question_id: 492148
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# no certificate in newly created domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/492148/no-certificate-in-newly-created-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

In our newly created additional domain controller there are no certificates present.    

    

And when I try to enroll say for kerberos authentication it gets an RPC error.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Hi @Janus Bariñan  ,    

Thank you for your reply.    

It is TCP port 135. TCP 135 port should be open on the CA server and this domain controller.     

    

Reference: https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

By the way, will it be okay if i just request a custom certificate request and copy the details of "kerberos authentication" and "domain controller authentication" from other DCs and send the certificate requests to the certificate admin so he can generate the certificates. Then i will install these certificates to the DC.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Hi Hannah,  

I'll try this one out and let you know the result.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Hello @Janus Bariñan  ,

Thank you so much for posting here.

As for the RPC error, the probable cause is port block or insufficient DCOM permission.

May I know there is the same RPC error if we enroll certificate on other domain controllers? If the error only occurred on this newly created domain controller, please follow the steps to have a check:

1.Verify that Remote Procedure Call (RPC) and Windows Management Instrumentation services are running on this DC.  

2.Please ensure that “Authenticated Users” group is in the “Certificate Service DCOM Access” group.  

3.Verify that the Builtin\Users group includes the following member groups.  

4.Run the below commands to test the port 135. If port 135 is blocked, please make it open on the domain controller.

Test-NetConnection(alias tnc) <host name or IP address of CA server> -Port 135 (powershell command)  

telnet <host name or IP address of CA server> 135 (CMD command)

5.Please allow RPC Dynamic Ports TCP port range from 49152 to 65535 on the DC.

For any question, please feel free to contact us.

Best regards,  

Hannah Xiong

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
