---
title: "ADFS authentication from outside the domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/950371/adfs-authentication-from-outside-the-domain
question_id: 950371
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS authentication from outside the domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/950371/adfs-authentication-from-outside-the-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,     

I have my ADFS server up and it works for authentication to my SaaS CRM when users are internal to the domain.  I have an entry in the HOSTS file directing internal traffic and it works well.  But when a user is outside of the domain it just times out.  What is interesting is that both PING to the DNS name of the ADFS server and HTTPS over telnet work.  Does anyone know what I may be missing in configuration?  I had the DC team check the firewall and the rules appear to be right and I would think that the ability to PING and telnet proves that.      

Any help would be much appreciated.     

Thanks,     

Brandon

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-09*

Ok I will look into this method.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-09*

I'm a bit confused.      

-  What is the WAP server?     

-  This worked in the beginning with no issues.     

-  I can PING and telnet to the public DNS name already     

-  I use a HOSTS file entry to direct the internal traffic.     

Is there nothing I can do or gather to test what piece may be broken?  Any logs, even viewer?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-09*

We would need to know more about your CRM configuration as I have seen many deployment oddities there.    

But in general, external access is agnostic of the application.    

It requires to deploy a WAP server and configure a split-brain DNS.    

In a nutshell, let's say your AD FS farm is `https://adfs.contoso.com`    

-  You deploy a WAP server. You make sure it is reachable externally with a public IP address on port TCP 443 (it doesn't have to be directly on the internet, you can use some NAT or publishing devices on the front of the WAP).    

-  You configure your public DNS to make sure `adfs.contoso.com` resolves to the public IP of the WAP    

-  You configure your internal DNS to make sure `adfs.contoso.com` resolves to the private IP of the AD FS server.    

Then you can also publish the CRM externally through the WAP but that's where it depends on how it has been configured...
