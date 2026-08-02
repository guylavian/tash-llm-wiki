---
title: "ms exchange dkim alignment fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1584944/ms-exchange-dkim-alignment-fails
question_id: 1584944
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# ms exchange dkim alignment fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1584944/ms-exchange-dkim-alignment-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Messages fail to Google with DKIM alignment failure.
Dmarc report from Google:
IP address: 2a01:111:f403:2418::700
Email Volume: 1
Disposition: none
SPF Authentication: Pass
SPF Alignment: Pass
DKIM Authorization: Pass
DKIM Alignment: Fail
Policy: Fail
 
Name Server Settings:
|A|@|Parked|600  

seconds|||
| -------- | -------- | -------- | -------- | -------- | -------- |
|A|@|Parked|600 seconds|||
||NS|@|ns71.domaincontrol.com.|1 Hour|Can't delete|Can't edit|
||NS|@|ns72.domaincontrol.com.|1 Hour|Can't delete|Can't edit|
||CNAME|autodiscover|autodiscover.outlook.com.|1 Hour|||
||CNAME|email|email.secureserver.net.|1 Hour|||
||CNAME|litesrv._domainkey|litesrv._domainkey.mlsend.com.|1 Hour|||
||CNAME|lyncdiscover|webdir.online.lync.com.|1 Hour|||
||CNAME|msoid|clientconfig.microsoftonline-p.net.|1 Hour|||
||CNAME|selector1._domainkey|selector1-dfletcher-net._domainkey.netorg2885737.onmicrosoft.com.|1 Hour|||
||CNAME|selector2._domainkey|selector2-dfletcher-net._domainkey.netorg2885737.onmicrosoft.com.|1 Hour|||

CNAMEsipsipdir.online.lync.com.1 Hour
CNAMEwwwdfletcher.net.1 Hour
CNAME_domainconnect_domainconnect.gd.domaincontrol.com.1 Hour
SOA@Primary nameserver: ns71.domaincontrol.com.1 Hour
@dfletcher-net.mail.protection.outlook.com. (Priority: 0)1 Hour
TXT@MS=ms333969241 Hour
TXT@v=spf1 include:secureserver.net -all1 Hour
TXT_dmarcv=DMARC1; p=none; rua=mailto:@dmarcinput.com,mailto:@dfletcher.net; ruf=mailto:@dmarcinput.com; fo=11 Hour
SRV_sip._tls.@100 1 443 sipdir.online.lync.com.1 Hour
SRV_sipfederationtls._tcp.@100 1 5061 sipfed.online.lync.com.1 Hour

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-26*

Hi @Duncan "Duff" Fletcher,

DKIM alignment checks the From Address in the header.

If it fails it may indicate the domain in the From header does not match the domain in the DKIM signature.

Please have a check if this is the cause of your issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
