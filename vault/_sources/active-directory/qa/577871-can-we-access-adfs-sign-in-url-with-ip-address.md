---
title: "Can we access ADFS sign in url with IP address?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/577871/can-we-access-adfs-sign-in-url-with-ip-address
question_id: 577871
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Can we access ADFS sign in url with IP address?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/577871/can-we-access-adfs-sign-in-url-with-ip-address (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

I am able to access ADFS sign in url with FQDN https://<server-FQDN>/adfs/ls/IdpInitiatedSignon.aspx  

However,I am not able to access aDFS sign in url with IP address https://<server-IPAddress>/adfs/ls/IdpInitiatedSignon.aspx  

Is it possible to use with IP address? If yes, please help me to asccess the adfs url with IP address

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-06*

The real question is should you? :)  

The ADFS server doesn't listen on the <IP>:443. It uses the SNI extension of TLS and needs the connexion to be established with the FQDN.  

In theory you could add an HTTPS listener for <IP>:443 using NETSH. But then you would also add the IP address as a Subject Alternative Name in your certificate extension. And that's frown upon as IP address could change (so not easy to maintain a certificate) and could be spoofed (although name could also be spoofed). You could also add a default listener for HTTPS with NETSH.  

So although possible, I would not advise to do so. Why are you looking at this? Is that for monitoring? If so, let us know what you use for that because most of the load balancer health probing mechanisms do support SNI nowaday.
