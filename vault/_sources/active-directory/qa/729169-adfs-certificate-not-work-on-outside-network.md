---
title: "Adfs Certificate not work on outside network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/729169/adfs-certificate-not-work-on-outside-network
question_id: 729169
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adfs Certificate not work on outside network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/729169/adfs-certificate-not-work-on-outside-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I'm having an issue with the ADFS certificate not working if you are not on the VPN.  

If you are on our VPN, the certificate shows it's valid. But if you are not on VPN, it shows it expired.   

Hopefully get some help.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-14*

Well, you need to type the command on the WAP server. So it's kinda of a catch 22 if you don't know where the WAP is there or where it is.  

On the AD FS server, you can try to run the following to identify the WAP servers in a PowerShell prompt:  

```
dir Cert:\LocalMachine\AdfsTrustedDevices | Where-Object { $_.Subject -like "CN=ADFS ProxyTrust*" }
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-14*

When I type the command for WAP I get can't recognize the cmdlet. Does that me the WAP is not installed. If so I am trying figure out how the last Admin got it to work without WAP. No Load Balancer or anything.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-14*

I am ssuming you mean the TLS/SSL certificate? And I am assuming that the only reason it is not valid is because it has expired (it would be a different story if it were invalid because of CRL check failing for example).    

When you are connected internally (or through VPN if your VPN makes you use internal IPs addresses when using the FQDN of the AD FS farm), you are likelly using the AD FS servers directly. So only the certificates installed on your AD FS servers are considered.    

When you are connected externally (without VPN), you are hitting the WAP or any other services you use to publish the AD FS service externally (like an external load-balancer if you are doing TLS/SSL inspection - which isn't great but out of topic). If you are using a WAP, make sure the certificate is up to date there. You can force the use of a specific certificate using the `Install-WebApplicationProxy` command on your WAP servers (https://learn.microsoft.com/en-us/powershell/module/webapplicationproxy/install-webapplicationproxy). If you are using some external load-balancer on the front of your WAP, check your WAP + those external load-balancers.
