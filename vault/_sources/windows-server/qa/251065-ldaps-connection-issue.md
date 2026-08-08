---
title: "LDAPs connection issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251065/ldaps-connection-issue
question_id: 251065
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# LDAPs connection issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251065/ldaps-connection-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a new domain controller on Server 2016 set up and for some reason I can't seem to get ldaps connections to succeed to it. I've verified my CA cert is in the trusted root cert authority under local computer. I've verified my client cert is in the personal store under local computer and it's trusted by the CA cert.  

However, whenever I run an openssl command from a linux box I get the following error:  

```
# openssl s_client -connect mytest.domainexample.com:636
CONNECTED(00000003)
write:errno=104
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 0 bytes and written 289 bytes
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID:
    Session-ID-ctx:
    Master-Key:
    Key-Arg   : None
    Krb5 Principal: None
    PSK identity: None
    PSK identity hint: None
    Start Time: 1611932693
    Timeout   : 300 (sec)
    Verify return code: 0 (ok)
---
```

I've seen all sorts of posts online troubleshooting this error, but I'm not having any luck. I've also tried running the Retrieve-ServerCertFromSocket.ps1 script locally on the Windows server, but that won't connect either.   

I can telnet to tcp/636 from my client so I don't believe it's a network issue.  

Any help would be greatly appreciated because I'm stumped!  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-30*

Figured it out. I had to add my server cert on my AD server into the Service (Active Directory Domain Services) store instead of the local computer store. Once I did that it fixed the problem.  

No idea why though because I've set up dozens of these before without having to do that and have never had an issue until now. Not sure if it's something new with the latest patch set.
