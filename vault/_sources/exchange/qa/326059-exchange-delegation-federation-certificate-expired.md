---
title: "Exchange Delegation Federation certificate expired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326059/exchange-delegation-federation-certificate-expired
question_id: 326059
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Delegation Federation certificate expired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326059/exchange-delegation-federation-certificate-expired (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! Need help with expired Exchange Delegation Federation certificate. I've managed to renew the certificate following this MS sites:    

https://learn.microsoft.com/en-us/exchange/renew-the-federation-certificate-exchange-2013-help#replace-an-expired-federation-certificate    

https://learn.microsoft.com/en-us/exchange/configure-a-federation-trust-exchange-2013-help    

We have hybrid environment where our on-prem users can't see our online users free/busy calendar information. This was because our Exchange Delegation Federation certificate expired. After we renew it the free/busy problem stayed. We figured that it might be the problem with Auth Configuration (get-authconfig |fl) for CurrentCertificateThumbprint value where this value is still from the previous Exchange Delegation Federation certificate.    

Does anybody have experience with this? If we change this value to our new Exchange Delegation Federation certificate thumbprint is there any steps to do after changing that value? Some sites mention that we need to publish this certificate and also start HCW (this site: http://www.wave16.com/2018/06/test-oauthconnectivity-errormissing.html)    

Will changing this Auth Configuration value for CurrentCertificateThumbprint to our new CurrentCertificateThumbprint have impact on our mail-flow or something else?    

Is it possible to auto-renew this certificate?    

Thank you!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-29*

Hello KyleXu, thank you for the response.  

Will things work if I just put the thumbprint of our new Exchange Delegation Federation certificate under Auth Configuration? This was obviously done first time because I have no explanation why Auth Configuration has thumbprint of our old Exchange Delegation Federation certificate. Is this type of configuration acceptable or MS recommends to have one certificate for Exchange Delegation Federation and one certificate for Auth Configuration?  

If we go with the creation of a new Auth Configuration certificate will it have impact on something in our environment because i see that this certificate is used also for Lync, Sharepoint...?  

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

@GK-6729    

The "get-authconfig" is used to check the "Microsoft Exchange Server Auth Certificate" which different from "Exchange Delegation Federation certificate". You can follow this article to renew this certificate and clear old certificate.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

After modify those two certificates, I would suggest you rerun HCW to update this configuration.    

The renewal procedure is simple and will not affect mail flow. But the best practice is to modify the Exchange server when it is idle.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
