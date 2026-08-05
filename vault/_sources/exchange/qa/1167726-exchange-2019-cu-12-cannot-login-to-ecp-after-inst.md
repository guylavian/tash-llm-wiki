---
title: "Exchange 2019 CU 12 Cannot login to ECP after installing new SSL certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167726/exchange-2019-cu-12-cannot-login-to-ecp-after-inst
question_id: 1167726
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 CU 12 Cannot login to ECP after installing new SSL certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167726/exchange-2019-cu-12-cannot-login-to-ecp-after-inst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

Recently on our Exchange 2019 CU12 server, I updated an Auth Certificate, installed a new certificate, and verified that I can access ECP and log in to OWA with the IP addresses of two Exchange servers, and I am using the new certificate. But SLB is used in the environment, and SLB VIP is used to log in and access, when I go to ECP URL to log in, it redirects to OWA URL:

.../owa/auth/logon.aspx?replaceCurrent=1&url...

The following IIS recycling commands have been executed, and it does not work.

[PS] C:>Restart-WebAppPool "MSExchangeOWAAppPool"

[PS] C:>Restart-WebAppPool "MSExchangeECPAppPool"

The strange thing is that after waiting for 8 hours, the SLB VIP access is normal. I think the CU12 version still does not solve the problem of UTC time zone, although there is no phenomenon of "ASSERT: HMACProvider.GetCertificates:protectionCertificates.Length<1" in the previous version .

Admin please help, thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-06*

Hi,Now it can be accessed normally after 8 hours. Every time the auth certificate is updated, it is like this. How can I solve this problem? The following link says that CU12 has solved the problem of UTC time zone, but this problem will occur if the access of the load balancing device is used.

https://support.microsoft.com/en-us/topic/invalid-new-auth-certificate-for-servers-that-are-not-on-utc-time-zone-kb5012779-583ad7df-2a41-4479-8f11-e7aa2cb23401

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-06*

Hi @uranus829  

Sorry not sure I understand your question correctly.

Would you please clarify:

Do you still have issues with accessing ECP via SLB vip? Or it is working fine now after 8 hours.

If the issue has gone, the possible cause may be the OAuth certificate needs some time to be published.

Just as you mentioned in the post, it may be 8 hours or more (up to 48 hours).

when I go to ECP URL to log in, it redirects to OWA URL:
.../owa/auth/logon.aspx?replaceCurrent=1&url...

This may be the expected behavior, as this url is for authentication to login ECP.

If the session expired, once you access ECP it would redirect you to this url to authenticate.

I found that the https 443 of the IIS Default Web Site certificate of exchange01 and exchange02 is bound to wmsvc-sha2 at the same time

Do you have a third-party (commercial) certificate?

Normally it is supposed to be the commercial certificate (or Exchange self-signed certificate if you don't want to use commercial certificate) which is bound to the IIS Default Web Site.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-05*

I found that the https 443 of the IIS Default Web Site certificate of exchange01 and exchange02 is bound to wmsvc-sha2 at the same time, and the slb vip will always be redirected to the login page. If the https 443 wmsvc- of one of the Default Web Site certificates is canceled There is no problem with sha2 certificate binding.
