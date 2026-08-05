---
title: "Unable to make LDAPS(636) call to Untrusted External Forest domain Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/515648/unable-to-make-ldaps-636-call-to-untrusted-externa
question_id: 515648
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Unable to make LDAPS(636) call to Untrusted External Forest domain Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/515648/unable-to-make-ldaps-636-call-to-untrusted-externa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When LDAPS(636) call made to external forest domain Active Directory, the connection is getting failed and the below error message has been logged in the event viewer log.   

"The certificate received from the remote server was issued by an untrusted certificate authority."  

We have 2 untrusted forests, Forest-A and Forest-B, both the forests have it's own CA servers and during LDAPS call from Forest-A to Forest-B, certificates are involved, hence the call is failing with the error message.  

In my understanding, I need to share the same certificate between the untrusted forests to make LDAPS calls, please correct me if I am wrong.  

I found out that we have to implement "cross-forest certificate enrollment" in order to achieve the LDAPS communication between the Untrusted External Forest Domains. Is that correct?  

Please suggest me, how should I make LDAPS(636) call to Untrusted External Forest Domains Active Directory. (I still want to keep the forests untrusted)  

I am implementing this using .net framework.  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-23*

Hi @Preetham Anandaram  ,    

You are receiving the error because the certificate that has been used for the LDAPS connection on the remote server is not trusted by the machine that is making the connection to the server.  The root certificate of the certificate chain needs to be added to the trust root container.    

Have a look at this article which may help troubleshoot the connection error.    

https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/
