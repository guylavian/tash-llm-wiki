---
title: "Some questions regarding LDAPS certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/966213/some-questions-regarding-ldaps-certificates
question_id: 966213
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Some questions regarding LDAPS certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/966213/some-questions-regarding-ldaps-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon,

I’m starting the process to move my email archiving to the cloud. I’ve already been shown three different web pages with instructions in getting settings configured, and now I see I need to configure LDAPS before the first step. To do that I need to create a(n) LDAPS certificate. At this time my system is using Server 2016 for domain controllers and I have a couple of questions regarding certificates:

1) My current CA server is running Server 2012 (an upgrade is in its future). Do I need a CA server running Server 2016? Would Server 2019 work? 2022?  

2) Will configuring LDAPS alter the ability to use non-SSL connections?  

3) If I use self-signed certificates will I hate life down the road?  

4) Follow-up to #3, is buying a commercial certificate worth the cost? I’m not cheap, I’m frugal.  

5) If I bungle the creation of the certificate can the domain controller lose connectivity to other devices on the network?  

6) Are there any other caveats or “gotchas” I need to watch out for?

Yes, I'm cautious. I find I make fewer mistakes this way. Any ideas, suggestions, or recommendations would be greatly appreciated.

Thanks,

Joe B

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-15*

Hi Gary, I don't work weekends so nothing to report at this time. Hopefully soon, but my plate has a tendency to remain quite full no matter what projects I complete.  :^|     

Thanks,     

Joe B

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-13*

Hi

1) My current CA server is running Server 2012 (an upgrade is in its future). Do I need a CA server running Server 2016? Would Server 2019 work? 2022?

No, your current CA can issue the certificate that can be used on 2016 DCs

2) Will configuring LDAPS alter the ability to use non-SSL connections?

No, LDAPS connection are on port 636, while non-SSL connections will be on 389

3) If I use self-signed certificates will I hate life down the road?

Not really, the only issue is that you will need to trust the self-signed certificate on the systems connecting on the LDAPS connection

4) Follow-up to #3, is buying a commercial certificate worth the cost? I’m not cheap, I’m frugal.

I wouldn't waste your money, as you have an internal CA which will work

5) If I bungle the creation of the certificate can the domain controller lose connectivity to other devices on the network?

Nope, if you don't have a certificate on the DC already it's unlikely that anything is making LDAPS connections

6) Are there any other caveats or “gotchas” I need to watch out for?

You just need to install the certificate correct in the right certificate store and everything should be good.

If you do have problems or you want to check the current status of your LDAPS connections, check out this article.  

https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/

Gary.
