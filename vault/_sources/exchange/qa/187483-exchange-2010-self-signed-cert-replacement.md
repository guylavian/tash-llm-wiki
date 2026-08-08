---
title: "Exchange 2010 self signed cert replacement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/187483/exchange-2010-self-signed-cert-replacement
question_id: 187483
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2010 self signed cert replacement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/187483/exchange-2010-self-signed-cert-replacement (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am working on an exchange 2010 environment with 100 users. The exchange is configured with self-signed certificate. Outlook & Active Sync is working with a self-signed certificate.  

The certificate has exchange host fqdn server.domain.local and san entries for publicName.domain.com  

Outlook 2016 is connected to exchange and resolves to exchange fqdn.  

I have purchased the trusted cert with publicName.domain.com and applied it too OWA, ActiveSync, EWS, Outlook Anywhere, Autodiscover, etc.  

However, outlook starts throwing certificate prompt. Outlook provider msstd: certificate principal name was configured for server.domain.local and I updated it to publicName.domain.com however this didn't solve the issue.  

Active Sync clients are fine since they use publiName.domain.com. If I configure a new outlook profile, it works fine without any certificate prompt and connects to exchange using publicName.domain.com.  

I had to revert to a self-signed certificate because of the certificate prompt for the already configured outlook profile.  

Is there any way we can update the outlook to use publicName.domain.com without reconfiguring the outlook profile or am I doing something wrong here?  

Appreciate your assistance to address this issue.  

Thanks,  

Nav

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-06*

Thanks @Andy David - MVP   for responding the question. The challenge with this approach is that we have 100 users working from home or site, and it may not be possible for us to reach out to them in short time.    

Is there any other alternate way?
