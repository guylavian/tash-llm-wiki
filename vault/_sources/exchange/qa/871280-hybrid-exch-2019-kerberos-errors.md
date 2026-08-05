---
title: "Hybrid Exch 2019 Kerberos errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/871280/hybrid-exch-2019-kerberos-errors
question_id: 871280
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Hybrid Exch 2019 Kerberos errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/871280/hybrid-exch-2019-kerberos-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A few weeks ago my DC sec.logs started filling up with Event ID 4768, coming from our on-prem Exchange 2019 hybrid server. Both Exchange and DCs are fully patched. Typically:  

TargetUserName host   

  TargetDomainName OurDomain.NO   

  TargetSid S-1-0-0   

  ServiceName krbtgt/OutDomain.NO   

  ServiceSid S-1-0-0   

  TicketOptions 0x40810010   

  Status 0x6   

  TicketEncryptionType 0xffffffff   

  PreAuthType -   

  IpAddress ::ffff:19X.XXX.XXX.XXX  

  IpPort 30544   

We do not have any accounts named "host" in our domain so the error is correct, but what is that coming from? I ran a monitoring tool on the Exchange server and it happens when the Microsoft email-system tries to talk to our on-prem-server. This snippet shows typically that the account "host/mail.protection.outlook.com" is tried authenticated several times, but the DC's initially reject it because it does not exist. But after some tries, SMTP-traffic seems to flow anyhow. Exchange seems to function normally, no major errors elsewhere.  

So what is going on here?  

SMTP:Cmd STARTTLS, Server is currently able to negotiate the use of TLS	{TCP:139, IPv4:138}  

SMTP:Rsp 220  2.0.0 SMTP server ready, 29 bytes	{TCP:139, IPv4:138}  

SSL:SSLv2RecordLayer, Error (needs reassembly)	{SSL:140, TCP:139, IPv4:138}  

SSL:SSLv2RecordLayer, Encrypted Application Data (needs reassembly)	{SSL:140, TCP:139, IPv4:138}  

TCP:Flags=...A...., SrcPort=35552, DstPort=SMTP(25), PayloadLen=0, Seq=1157102882, Ack=1194422529, Win=16425 (scale factor 0x8) = 4204800	{TCP:139, IPv4:138}  

SSL:SSLv2RecordLayer, Encrypted Application Data (needs reassembly)	{SSL:140, TCP:139, IPv4:138}  

TCP:[Continuation to #1036]Flags=...A...., SrcPort=35552, DstPort=SMTP(25), PayloadLen=1460, Seq=1157104342 - 1157105802, Ack=1194423482, Win=16421 (scale factor 0x8) = 4203776	{TCP:139, IPv4:138}  

TCP:[Continuation to #1036]Flags=...AP..., SrcPort=35552, DstPort=SMTP(25), PayloadLen=612, Seq=1157105802 - 1157106414, Ack=1194423482, Win=16421 (scale factor 0x8) = 4203776	{TCP:139, IPv4:138}  

TCP:Flags=...A...., SrcPort=SMTP(25), DstPort=35552, PayloadLen=0, Seq=1194423482, Ack=1157106414, Win=65534 (scale factor 0x8) = 16776704	{TCP:139, IPv4:138}  

TCP:Flags=CE....S., SrcPort=7445, DstPort=Kerberos(88), PayloadLen=0, Seq=4044519019, Ack=0, Win=64240 ( Negotiating scale factor 0x8 ) = 64240	{TCP:141, IPv4:31}  

TCP:Flags=.E.A..S., SrcPort=Kerberos(88), DstPort=7445, PayloadLen=0, Seq=1896283979, Ack=4044519020, Win=8192 ( Negotiated scale factor 0x8 ) = 2097152	{TCP:141, IPv4:31}  

TCP:Flags=...A...., SrcPort=7445, DstPort=Kerberos(88), PayloadLen=0, Seq=4044519020, Ack=1896283980, Win=65534 (scale factor 0x8) = 16776704	{TCP:141, IPv4:31}  

KerberosV5:AS Request Cname: host/mail.protection.outlook.com Realm: OURDOMAIN.NO Sname: krbtgt/OURDOMAIN.NO 	{TCP:141, IPv4:31}  

KerberosV5:KRB_ERROR  - KDC_ERR_C_PRINCIPAL_UNKNOWN (6)	{TCP:141, IPv4:31}  

TCP:Flags=...A...F, SrcPort=7445, DstPort=Kerberos(88), PayloadLen=0, Seq=4044519274, Ack=1896284076, Win=65534 (scale factor 0x8) = 16776704	{TCP:141, IPv4:31}  

TCP:Flags=CE....S., SrcPort=7446, DstPort=Kerberos(88), PayloadLen=0, Seq=4015489666, Ack=0, Win=64240 ( Negotiating scale factor 0x8 ) = 64240	{TCP:142, IPv4:31}  

TCP:Flags=...A...., SrcPort=Kerberos(88), DstPort=7445, PayloadLen=0, Seq=1896284076, Ack=4044519275, Win=8212 (scale factor 0x8) = 2102272	{TCP:141, IPv4:31}  

TCP:Flags=...A.R.., SrcPort=Kerberos(88), DstPort=7445, PayloadLen=0, Seq=1896284076, Ack=4044519275, Win=0 (scale factor 0x8) = 0	{TCP:141, IPv4:31}  

TCP:Flags=.E.A..S., SrcPort=Kerberos(88), DstPort=7446, PayloadLen=0, Seq=1613145770, Ack=4015489667, Win=8192 ( Negotiated scale factor 0x8 ) = 2097152	{TCP:142, IPv4:31}  

TCP:Flags=...A...., SrcPort=7446, DstPort=Kerberos(88), PayloadLen=0, Seq=4015489667, Ack=1613145771, Win=65534 (scale factor 0x8) = 16776704	{TCP:142, IPv4:31}  

KerberosV5:AS Request Cname: host/mail.protection.outlook.com Realm: OURDOMAIN.NO Sname: krbtgt/OURDOMAIN.NO 	{TCP:142, IPv4:31}  

KerberosV5:KRB_ERROR  - KDC_ERR_C_PRINCIPAL_UNKNOWN (6)	{TCP:142, IPv4:31}  

TCP:Flags=...A...F, SrcPort=7446, DstPort=Kerberos(88), PayloadLen=0, Seq=4015489921, Ack=1613145867, Win=65534 (scale factor 0x8) = 16776704	{TCP:142, IPv4:31}  

9922, Win=8212 (scale factor 0x8) = 2102272	{TCP:142, IPv4:31}  

TCP:Flags=...A.R.., SrcPort=Kerberos(88), DstPort=7446, PayloadLen=0, Seq=1613145867, Ack=4015489922, Win=0 (scale factor 0x8) = 0	{TCP:142, IPv4:31}  

TCP:Flags=CE....S., SrcPort=7447, DstPort=49158, PayloadLen=0, Seq=1303772489, Ack=0, Win=64240 ( Negotiating scale factor 0x8 ) = 64240	{TCP:143, IPv4:4}  

TCP:Flags=.E.A..S., SrcPort=49158, DstPort=7447, PayloadLen=0, Seq=3024248101, Ack=1303772490, Win=8192 ( Negotiated scale factor 0x8 ) = 2097152	{TCP:143, IPv4:4}  

TCP:Flags=...A...., SrcPort=7447, DstPort=49158, PayloadLen=0, Seq=1303772490, Ack=3024248102, Win=65534 (scale factor 0x8) = 16776704	{TCP:143, IPv4:4}  

MSRPC:c/o Bind: Netlogon(NRPC) UUID{12345678-1234-ABCD-EF00-01234567CFFB}  Call=0x6F20  Assoc Grp=0x0  Xmit=0x16D0  Recv=0x16D0 	{MSRPC:144, TCP:143, IPv4:4}  

MSRPC:c/o Bind Ack:  Call=0x6F20  Assoc Grp=0x4B313  Xmit=0x16D0  Recv=0x16D0 	{MSRPC:144, TCP:143, IPv4:4}  

NRPC:NetrLogonSamLogonEx Request, Encrypted	{MSRPC:144, TCP:143, IPv4:4}  

TCP:Flags=...A...., SrcPort=49158, DstPort=7447, PayloadLen=0, Seq=3024248230, Ack=1303775397, Win=4106 (scale factor 0x8) = 1051136	{TCP:143, IPv4:4}  

NRPC:NetrLogonSamLogonEx Response, Encrypted	{MSRPC:144, TCP:143, IPv4:4}  

SSL:SSLv2RecordLayer, Error (needs reassembly)	{SSL:140, TCP:139, IPv4:138}  

SSL:SSLv2RecordLayer, Error (needs reassembly)	{SSL:140, TCP:139, IPv4:138}

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-19*

Hey there. Got the same issue with my environment. AD AuditPlus started freaking out over User: Null bad login creds, error 4625. Found out it was a health mailbox (after disabling them). This issue came up around October 2022's .net and monthly security updates.

Logged a case with Microsoft

Ended up being the cname mail.protection.outlook.com is not registered as an SPN (Service Principal Name) host for mail.protection.outlook.com. Recommend to verify the configuration of mail.protection.outlook.com for constrained delegation

But don't know how to fix this

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-08*

No solution. Seeing others also having this problem - quite annoying.. https://learn.microsoft.com/en-us/answers/questions/917013/event-id-4768?page=2#answers

-Ray-

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-08*

Did you ever get a resolution to this issue? The exact same thing is occurring on my hybrid Exchange 2019 servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-07*

Thank you for your suggestion, but that did not work.  

HCW is running just fine. (Also ran it very recently in conj. with cert renewal)
