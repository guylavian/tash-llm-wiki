---
title: "Changed Exchange 2019 DNS MX Records for Spam Filter Service and Exchange Active Sync Now Fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1842122/changed-exchange-2019-dns-mx-records-for-spam-filt
question_id: 1842122
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Changed Exchange 2019 DNS MX Records for Spam Filter Service and Exchange Active Sync Now Fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1842122/changed-exchange-2019-dns-mx-records-for-spam-filt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an on-premises Exchange Server 2019.  Everything was working fine until we got an external spam filtering service.  We changed our MX records to point to the spam filtering service, and then the filtering service sends the emails to the Exchange Server.  That part works great.

 

The problem is when we try to add an account to Outlook or a smartphone, it won't connect to the Exchange Server to setup the account.  The only records changed were the MX records.  Autodiscover, mail.{domain].com, and autodiscover records still point to the Exchange server.

 

Here are the error messages I get.

 

 

If I manually setup the Outlook profile putting in the mail server name (mail.{domain}.com, domain\username, password, etc., then I get this.

 

 

I ran the Microsoft Remote Connectivity Analyzer for Activesync, and it passed.

 

The autodiscover records look like this.

A   autodiscover.mydomain.com   XXX.XXX.XXX.XXX where XXX.XXX.XXX.XXX is the server public IP address.

A   mail.mydomain.com     XXX.XXX.XXX.XXX where XXX.XXX.XXX.XXX is the server public IP address.

SRV  _autodiscover._tcp.mydomain.com     0 443 mail.mydomain.com

Some people use a CNAME instead of an A record for autodiscover.mydomain.com.  I don't know if that makes a difference.

Anyone have any ideas or workarounds?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-04*

duplicate.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-29*

Hi,

Welcome to the Microsoft Q&A forum.

When this message comes up, click Back, select Manually configure server settings then click Next.

You'll need to enter your account information and server names then click More Settings and configure your SSL or TLS settings on the Advanced tab.

Also, I recommend you update your SPF records to include the spam filtering service. If you're using DKIM, make sure the service is correctly signing outgoing emails.
