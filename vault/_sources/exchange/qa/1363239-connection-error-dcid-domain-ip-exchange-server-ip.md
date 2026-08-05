---
title: "Connection Error: DCID domain: IP: <Exchange Server IP> port: 25 details: [Errno 0] Error interface: reason: network error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1363239/connection-error-dcid-domain-ip-exchange-server-ip
question_id: 1363239
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Connection Error: DCID domain: IP: <Exchange Server IP> port: 25 details: [Errno 0] Error interface: reason: network error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1363239/connection-error-dcid-domain-ip-exchange-server-ip (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Server

MS Exchange Server 2013 U23 Standard

AdminDisplayVersion 15.0 (Build 1497.2

We are using an Microsoft exchange server 2013/2016 U23 to deliver and route our emails. Our product is Cisco Email Security Appliance We are getting [Errno 0] Error  interface: reason network error when connecting to server with ECDHE-RSA-AES256-SHA384.But the same connection works for other cipher suites such as ECDHE-RSA-AES128-SHA.We are having compatibility issues between Exchange 2013 and OpenSSL 1.1.1 when specific cipher strings are used.

Our observations

With 'ECDHE-RSA-AES128-SHA' (Working):

Wed Sep  6 13:13:16 2023 Info: MID 14 ICID 14 From: ******@domainsample1.com

Wed Sep  6 13:13:16 2023 Info: MID 14 SDR: Domains for which SDR is requested: reverse DNS host: Not Present, helo: smtp.spa

m.test, env-from: cisco.com, header-from: Not Present, reply-to: Not Present

Wed Sep  6 13:13:16 2023 Info: MID 14 SDR: Message was not scanned for Sender Domain Reputation. Reason: Unknown error.

Wed Sep  6 13:13:16 2023 Info: MID 14 ICID 14 RID 0 To: ******@domainsample2.com

Wed Sep  6 13:13:16 2023 Debug: MID 14 ICID 14 TLS read 126 bytes (0.0 seconds)

Wed Sep  6 13:13:16 2023 Info: MID 14 Message-ID '20230906131316.23631.70662@esa008.cs18'

Wed Sep  6 13:13:16 2023 Info: MID 14 Subject "Testing"

Wed Sep  6 13:13:16 2023 Info: MID 14 SDR: Domains for which SDR is requested: reverse DNS host: Not Present, helo: smtp.spa

m.test, env-from: cisco.com, header-from: cisco.com, reply-to: Not Present

Wed Sep  6 13:13:16 2023 Info: MID 14 SDR: Message was not scanned for Sender Domain Reputation. Reason: Unknown error.

Wed Sep  6 13:13:16 2023 Info: MID 14 SDR: Tracker Header : 64f87aec_N/6TpU9YN1dsVJ3pDujDlS+RmDQQrvukNy6A4SuBgUlLDZTOZ+Q0VzN

T8knnL5YbaLJfrrVUCS68IDBDu1uiyg==

Wed Sep  6 13:13:16 2023 Info: MID 14 ready 280 bytes from ******@domainsample1.com

Wed Sep  6 13:13:16 2023 Info: MID 14 matched all recipients for per-recipient policy DEFAULT in the inbound table

Wed Sep  6 13:13:16 2023 Trace: GRAYMAIL: shouldn't scan?

Wed Sep  6 13:13:16 2023 Trace: MID 14: Skip AMP Engine check

Wed Sep  6 13:13:16 2023 Trace: GRAYMAIL: No Actions Applied

Wed Sep  6 13:13:16 2023 Trace: Data will be sent to ECS client only when there is cloud license, urlscanning is enabled and

 retro service is enabled

Wed Sep  6 13:13:16 2023 Info: MID 14 queued for delivery

Wed Sep  6 13:13:16 2023 Info: New SMTP DCID 30 interface 10.13.102.10 address 10.13.101.31 port 25

Wed Sep  6 13:13:16 2023 Info: DCID 30 TLS success protocol TLSv1.2 cipher ECDHE-RSA-AES256-SHA384

Wed Sep  6 13:13:16 2023 Info: Delivery start DCID 30 MID 14 to RID [0]

Wed Sep  6 13:13:16 2023 Trace: MID 14 DKIM: signing context (profile - ) : profile names are not present/not set

Wed Sep  6 13:13:16 2023 Trace: RPC client _message_loop sleeping when dequeuing a null entry

Wed Sep  6 13:13:16 2023 Info: Message done DCID 30 MID 14 to RID [0]

With 'ECDHE-RSA-AES256-SHA384' (Not Working):

i Sep  8 05:21:31 2023 Info: MID 4 ICID 4 From: ******@domainsample1.com

Fri Sep  8 05:21:31 2023 Info: MID 4 SDR: Domains for which SDR is requested: reverse DNS host: Not Present, helo: smtp.spam

.test, env-from: cisco.com, header-from: Not Present, reply-to: Not Present

Fri Sep  8 05:21:31 2023 Info: MID 4 SDR: Message was not scanned for Sender Domain Reputation. Reason: Service Temporarily

Unavailable.

Fri Sep  8 05:21:31 2023 Info: MID 4 ICID 4 RID 0 To: ******@domainsample2.com

Fri Sep  8 05:21:31 2023 Info: MID 4 Message-ID '20230908052134.74591.43891@esa008.cs18'

Fri Sep  8 05:21:31 2023 Info: MID 4 Subject "Testing"

Fri Sep  8 05:21:31 2023 Info: MID 4 SDR: Domains for which SDR is requested: reverse DNS host: Not Present, helo: smtp.spam

.test, env-from: cisco.com, header-from: cisco.com, reply-to: Not Present

Fri Sep  8 05:21:33 2023 Info: MID 4 SDR: Message was not scanned for Sender Domain Reputation. Reason: Service Temporarily

Unavailable.

Fri Sep  8 05:21:33 2023 Info: MID 4 SDR: Tracker Header : 64faaf5e_fDzl9+YzU8++fc0v3rIygyoIu4poY9OPeCVCyvcuNc1MHUeLzvw76Rs0

2ou3TJ/uI6rKlKWef5cHeLqGUH4qyQ==

Fri Sep  8 05:21:33 2023 Info: MID 4 ready 280 bytes from ******@domainsample1.com

Fri Sep  8 05:21:33 2023 Info: MID 4 matched all recipients for per-recipient policy DEFAULT in the inbound table

Fri Sep  8 05:21:33 2023 Info: MID 4 queued for delivery

Fri Sep  8 05:21:34 2023 Info: ICID 4 TLS failed: [Errno 54] Connection reset by peer

Fri Sep  8 05:21:34 2023 Info: ICID 4 lost

Fri Sep  8 05:21:34 2023 Info: ICID 4 close

Fri Sep  8 05:22:23 2023 Info: New SMTP DCID 63 interface 10.10.192.50 address 10.13.101.31 port 25

Fri Sep  8 05:22:23 2023 Info: Connection Error: DCID 63 domain: domainsample2.com IP: 10.13.101.31 port: 25 details: [Errno 0] E

rror interface: 10.10.192.50 reason: network error

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-14*

Hi Kael,

My responses are getting deleted, am unsure why.

The ciphers are enabled on both sides but still not helping with our solution

Health Check Logs on Exchange Server.txt

Attaching the logs for your reference.

```
TlsCipherSuiteName                            CipherSuite  Cipher  Certificate  Protocols  
        ------------------                            -----------  ------  -----------  ---------  
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256    N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P384    N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256    N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P384    N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256       N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P384       N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P256       N/A          N/A     N/A          N/A        
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P384       N/A          N/A     N/A          N/A        
        TLS_DHE_RSA_WITH_AES_256_GCM_SHA384           N/A          N/A     N/A          N/A        
        TLS_DHE_RSA_WITH_AES_128_GCM_SHA256           N/A          N/A     N/A          N/A        
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA              N/A          N/A     N/A          N/A        
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA              N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_256_GCM_SHA384               N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_128_GCM_SHA256               N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_256_CBC_SHA256               N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_128_CBC_SHA256               N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_256_CBC_SHA                  N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_AES_128_CBC_SHA                  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384_P384  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P256  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P384  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384_P384  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256_P256  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256_P384  N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA_P256     N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA_P384     N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA_P256     N/A          N/A     N/A          N/A        
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA_P384     N/A          N/A     N/A          N/A        
        TLS_DHE_DSS_WITH_AES_256_CBC_SHA256           N/A          N/A     N/A          N/A        
        TLS_DHE_DSS_WITH_AES_128_CBC_SHA256           N/A          N/A     N/A          N/A        
        TLS_DHE_DSS_WITH_AES_256_CBC_SHA              N/A          N/A     N/A          N/A        
        TLS_DHE_DSS_WITH_AES_128_CBC_SHA              N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_3DES_EDE_CBC_SHA                 N/A          N/A     N/A          N/A        
        TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA             N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_RC4_128_SHA                      N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_RC4_128_MD5                      N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_NULL_SHA256                      N/A          N/A     N/A          N/A        
        TLS_RSA_WITH_NULL_SHA                         N/A          N/A     N/A          N/A        
        SSL_CK_RC4_128_WITH_MD5                       N/A          N/A     N/A          N/A        
        SSL_CK_DES_192_EDE3_CBC_WITH_MD5              N/A          N/A     N/A          N/A
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-11*

Hi @Reena Thomas (reenthom)  

You can run the health checker script in Exchange Management Shell as an administrator to list all the currently enabled cipher suites.

Example (in the result):

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
