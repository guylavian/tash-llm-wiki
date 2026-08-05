---
title: "Mail Bouncing from MS Exchange-  421 4.4.2 Connection dropped due to SocketError'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1369059/mail-bouncing-from-ms-exchange-421-4-4-2-connectio
question_id: 1369059
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 6
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Mail Bouncing from MS Exchange-  421 4.4.2 Connection dropped due to SocketError'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1369059/mail-bouncing-from-ms-exchange-421-4-4-2-connectio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

This problem is now about 3 weeks with no solution in sight. 

When we email to 3 or more Gmail accounts, (with or without other domains/email addresses & with/without attachments), we find the all the Gmail accounts bouncing with the above (subject line) error message. The other recipients receive their mails. 

When we send mail up to 2 Gmail accounts, (with or without other domains/email addresses), the Gmail accounts receive their mail. 

For example ; 1) [@gmail.com]; 2) [@gmail.com]; 3) three @gmail.com; [@xyz.com]; [@lhr.com] are in the recipient list, the Gmail addresses will bounces and [******@abc.com] will go through. All of these concerns are with same addresses we have been communicating with for years, with no problems prior. 

Our service provider is Office365 / MS Exchange. If we use the Outlook web-app (on Chrome) or MS Outlook client app, it is the same, so it is not my settings nor the application. The way we see it, problem seems to be with MS Exchange and not my end. 

ADDITIONAL INFO - our mail address in concern is [******@dandwassociates.com] & ******@dandwassociates.com

 error code - Generating server: SEYPR06MB5087.apcprd06.prod.outlook.com Receiving server: SEYPR06MB5087.apcprd06.prod.outlook.com Total retry attempts: 14 example .......@gmail.com . 9/12/2023 10:39:23 AM - Server at SEYPR06MB5087.apcprd06.prod.outlook.com returned '550 5.4.300 Message expired -> 421 4.4.2 Connection dropped due to SocketError' 9/12/2023 10:38:18 AM - Server at gmail-smtp-in.l.google.com (2a00:1450:4025:401::1a) returned '421 4.4.2 Connection dropped due to SocketError'

NEW INFO

_*Our email to only 2 gmail addresses bounced as well.   

The mail was sent Outlook on Chrome browser.  

Please do help us urgently.  

Thank you  

Manjula*_

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-05*

Hello,  

Further my comment of 19 Sept, the problem did not get resolved.  So, we kept chasing and "tickets".  

Today, the "Senior Engineer" who spoke to me, resolved it.  

He looked at the DKIM settings on the O365 security settings. In it, there is an "enable/disable" switch. Ours was off and we couldn't switch it to Enable. However it gave a text box.  

The MS engineer got us to copy the text, and we had to visit our Domain host (Go Daddy for us). And, in their DNS Management / DNS Records settings, under Cname settings, we had to enter some new components twice.   

Your support engineer will take you through this.  

Hope this helps you.  

Cheers,

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-19*

Hi,  

From the Admin page of the Office 365 account, I clicked on the Help & Support and raised a "ticket". A "Support Ambassador" called (within an hour) and went through the process.  

At the moment, it looks like resolved :).  

Having said that, there were 3 calls from MS. The first 2 thought it was resolve, but, No. The 3rd person (on day 3 & ticket #3), took about 30 to 40 minutes with us, and (fingers crossed) resolved. There was a time that he took a minimum of 10 minutes on behind the scenes work he did.  

What he looked for on our system ?  

From the admin account, he accesses Exchange. From there he looked at the email addressed that bounced, got reports for those that bounced and then put me on hold for 10 minutes or so.   

Hope this helps.  

I can't help you guys beyond that as I'm not tech-savvy beyond this :(.  

Cheers

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-27*

I have been having this exact issue now for 3 weeks. I opened a service ticket with Microsoft. 

OP, please check what message you get back from your Microsoft server (the error email). Three weeks ago it was error '550 5.4.300 Message expired -> 421 4.7.28 [2a01:111:f400:fe5a::61d 15] - which is a bulk email error, even though the message was to only 4 Gmail recipients and was in reply to their message.

The suggestion my MS was that Google introduced a change, and is now unable to translate an IPv6 IP address for Exchange Emails, whereas IPv4 works, so they recommended I create an MX connector in my Exchange admin, you can find the instructions on Reddit. It is what the MS Help Desk told me.  Create a connector and set for "lookup MX for domain", the idea is this forces MS into an IPv4.

I did this and it worked for a while, but stopped last week. Now some emails time out with a socket error returned '421 4.4.2 Connection dropped due to SocketError' whereas before they just timed out. This error implies a TLS encryption error I think, but not sure. Any admins here would be helpful.

To be clear, the emails are not bouncing, they are timing out because Gmail cannot/will not receive the email from O365.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-15*

Hi,  

Check if the sender is blacklisted. Have you tried using a different device?

Also please check if this helps:

421 4.4.2 Connection dropped due to SocketError

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
