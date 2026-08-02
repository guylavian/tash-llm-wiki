---
title: "Exchange not receiving and Sending emails from certain addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112624/exchange-not-receiving-and-sending-emails-from-cer
question_id: 112624
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange not receiving and Sending emails from certain addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112624/exchange-not-receiving-and-sending-emails-from-cer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,    

Please kindly assist. My Exchange Server is failing to send and Receive Emails to and from certain Domains.    

-  All Users can't send and receive mail with a specific domain.    

-  I do receive a non-delivery report when sending mail to a specific domain fails.    

Diagnostic information for administrators:    

Generating server: MBX-01.xxx.com    

Receiving server: xxxx.dk (45.100.187.7)    

user1@xxxxxxxxxxxxx  .dk    

Remote Server at xxxx.dk (45.100.187.7) returned '400 4.4.7 Message delayed'    

9/29/2020 8:13:49 AM - Remote Server at xxxx.dk (45.100.187.7) returned '451 4.4.0    

Primary target IP address responded with: "451 4.7.3 The admin has temporarily disallowed this secure domain.    

" Attempted failover to alternate host, but that did not succeed. Either there are no alternate hosts,     

or delivery failed to all alternate hosts. The last endpoint attempted was 45.100.187.7:25'    

Original message headers:    

Received: from MBX-02.xxx.com (192.168.0.91) by MBX-01.xxx.com    

 (192.168.0.90) with Microsoft SMTP Server (TLS) id 15.0.1497.2; Tue, 29 Sep    

 2020 10:18:36 +0300    

Received: from MBX-02.xxx.com ([::1]) by MBX-02.xxx.com ([::1]) with    

 mapi id 15.02.0529.010; Tue, 29 Sep 2020 10:18:36 +0300

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-21*

@Lydia Zhou - MSFT   ,    

Thank so much for your responses and my Apologies for a delayed revert.    

I finally was able to find the root cause of the Issue The domain was blocked in the DomainSecureEnabled flag so I ran the scripts below;    

Set-TransportConfig -TLSReceiveDomainSecureList $null    

Set-TransportConfig -TLSSendDomainSecureList $null    

Thank you.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-01*

@Kaggwa Ronald       

For the message sending issue:    

Since this issue occurs only with specific domain, and agree with udara, your domain may be blocked by the recipient's organization. You can contact that organization for this email issue.    

For the message receiving issue:    

Does it occur after any modification in your organization?    

Do senders from that domain get any NDR messages when send to your organization? You can get and post the screenshot of the NDR message here, and don't forget to cover your personal information.    

Please check if those emails are blocked by the anti-spam protection. Here is a similar issue for your reference: 451 4.7.3 The admin has temporarily disallowed this secure domain???    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-09-30*

check email allowed status from your domain to that domain. Your domain may be blocked from recipient (that domain) side.  

Add that domain which you receiving mail from into safe/allowed list in your mail server and Firewall or spam gateway.  

Please check blacklist status of that domain name.  

Further, Please contact admin of that email domain and check DNS settings(WAN IP, PTR)
