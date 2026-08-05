---
title: "Unexpected timeout and logoff in custom OWA client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163949/unexpected-timeout-and-logoff-in-custom-owa-client
question_id: 1163949
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Unexpected timeout and logoff in custom OWA client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163949/unexpected-timeout-and-logoff-in-custom-owa-client (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a custom OWA client to enforce 2FA for Outlook.  

It's pretty standard: it intercepts original logon with our custom page and after 2FA login redirects user back to normal OWA inbox.  

The problem:

When the user is idle for approximately 20-23 minutes he is logged off automatically.  

The details:  

-  All idle-related timeouts (known through Windows documentation) do not affect the behavior.  

-  Only happens when custom OWA client is enabled.  

Technically:

Every 5 minutes 20 seconds OWA client sends API call to outlook server:

/owa/ev.owa2?ns=PendingRequest&ev=FinishNotificationRequest...

Usually it gets OK (200). At some point it gets 440 (Login Time-out) and OWA will log out automatically.  

There is no difference (from a client's perspective) between calls with successful (200) response and the bad (440) one.  

Actual log output:

2022-02-25 20:14:12 10.203.20.202 POST /owa/ev.owa2 ns=PendingRequest&ev=FinishNotificationRequest&UA=0&cid=fc2fb607-f9bd-40b7-8e9e-406c22604a9c&ClientId=8CD4CEC6BFFD4323B47BCFC56B08D9DA&CorrelationID=<empty>;&LogoffReason=LoginTimeoutPost&cafeReqId=4f3a79d6-35f6-4f43-8cdc-8317ee9effd2;&encoding=; 443 - 10.203.140.1 Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/95.0.4638.69+Safari/537.36 - 440 0 0 121 - X-BackEndCookie=S-1-5-21-1760168264-536541648-2087994650-23692=u56Lnp2ejJqBycjMmZ7KzpvSyszLzNLLmZvO0sbJzc3SzJ7GyMvNmcbKzZnLgYHNz83N0s/M0s3Iq83Pxc/HxcrM;+ASP.NET_SessionId=oqovibc4pboilsv1vkiuz2ii;+PBack=0;+cadata=D3eGEum5KD3cdk/KSHhd1mZsXU4TQVSLRKdKoi1ScOU68PIYGW/fYOhyzO7ululdbMDcVTMQIls3OeZA59GzTyA4fKoI3QlrkoOPAUTtXnPlQdpv0SxBU2TFr7Qi4RSw;+cadataTTL=Us7DwpqDkIM4wFmwR9wt3A==;+cadataKey=l8nAcT3BdCaTvJKsU7W+lZBhM0lto+zD2uQDSQ6o7fY38WOVpy7VfBxVwwvdW8gFGrRuPV0C0Aqva/GKMS3R/3MljwawNkNENtgDsLDV2RnSTZbQDXj3jLWfeuGMtQoAzFN+/gnHP22KQrh+au4sxzYc0Gb+QR1nP6B2CJ8dNf+4L34vcBFDqa8GRCPQYs3SDjpCoxqMAKgiSNHk/ih9Dx1SZN9UbqWTtLzweC7cPmKZE1XNbDKAK+VBfe0p73lhxN4pinIj7304Eoap3yOluG4r1EFj6dV1ptJisx+RD8QsMiRM+t/kuA6tZktu5WImv2jgxpWLLg1Z8j+2FXy0IA==;+cadataIV=Hja2spUUv3jOf6TXmt1n3wIE6BCKQt1qIu+qkte0taRSJjjAFKCCFSZz4Nwa+tjoWqwHPIw6tq8NShWdf+BRuxpaYUichoDwmqaC4xIpmfqYa1QOaNELhh581RxZeDvek2PWXOFAecPLcIG34QN780+Rj+OLyYIAB3YIFA1XWHeiFxxD5CFNGIErhHFMbcn9tICPIpF5aete3lzrrTT3sebyNRxvW1X/AB/YkCEM16TvZysna9U9wrMoOVGj3cjo+e8hvAzChpid0IE/pG67RW/d08QiR0KT+XR1HUfuRwZUADtM42N1dTou3criy/SEGpVjRWfMp5D9Fe6TOMVrMQ==;+cadataSig=R8qr9QBFcCjJjm1JoProrG4VKu4BHS3e3wFuHRZnmIw=;+ClientId=8CD4CEC6BFFD4323B47BCFC56B08D9DA;+UC=c7d6c1df06cc43bfb72babd9c3de122d;+OutlookSession=f7a7e0a3e69c40ae830664cb8811aaaf;+mkt=en-US;+X-OWA-JS-PSD=1;+X-OWA-CANARY=7hkyTCswb0GkrGrC4WvX76D4O6Wa-NkIrhCUBMOtgskuBNiZ5KaBVwg7dM6QTLqS2NfrMVMtRMI.  

Any ideas?  

Any hidden settings somewhere?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-27*

As far as I can tell, the problem is due to the login session timeout for your webmail session not matching the login session timeout for your session to the server where attachments are held. These should be the same in my opinion, so that when the session expires to the attachment server, your session also expires to webmail, and webmail is forcefully either refreshed (if Keep Me Signed In is checked at the login screen), or you're bumped back to the login screen.
