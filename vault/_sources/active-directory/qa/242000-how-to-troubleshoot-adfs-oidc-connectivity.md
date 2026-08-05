---
title: "How to troubleshoot ADFS OIDC connectivity"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/242000/how-to-troubleshoot-adfs-oidc-connectivity
question_id: 242000
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# How to troubleshoot ADFS OIDC connectivity

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/242000/how-to-troubleshoot-adfs-oidc-connectivity (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently having a challenge trying to authenticate via OpenID Connect against an ADFS instance hosted in Azure.  I have a server-based ASP.NET Core MVC app hosted on its own VM in Azure along with a proxy service (hosted on the same VM) that I'm using to route requests through from the app to ADFS.  I can run the app and proxy on localhost and successfully connect to ADFS and display the login page, however, when I run my app and proxy from the Azure VM I get the error:  "IDX20804: Unable to retrieve document from:  [ADFS server]/adfs/.well-known/openid-configuration".  I can directly browse to the OpenID Connect discovery document being served from my ADFS instance and display it.  In terms of setup, I've registered my proxy as both a Server application and a Web API under Application Groups in ADFS.  The Redirect URI in each case correctly points back to my proxy.  Redirect URI is in the format:  https://[public DNS name]:port.  My MVC app has also been registered as a Relying Party Trust in ADFS.  I did also try registering my MVC app as a Server application under Application Groups but this didn't make a difference.  I did try and enable the Trace Log as outlined in MS docs but didn't get any logged information related to this issue.    

Would really appreciate any info on how to troubleshoot this error and identify the root cause.    

FYI - my ADFS product version is:  10.0.14393.4046

## Answers

_No answers on this thread._
