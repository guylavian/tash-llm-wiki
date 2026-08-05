---
title: "New to ADFS (setup/diagram)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/33004/new-to-adfs-setup-diagram
question_id: 33004
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# New to ADFS (setup/diagram)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/33004/new-to-adfs-setup-diagram (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am new to ADFS and I want to use one but don't know what the architecture would look like.    

For Internal use. Am I right to use this diagram?    

    

What ports are needed to communicate between the ADFS and DC?    

Do I need to use ADFS proxy for internal network use?    

Do internal clients need certificate of ADFS server?    

For External use (internet). Would this be the right diagram?    

    

Am I right to say that only port 443 is used between ADFS proxy and ADFS Server?    

ADFS proxy should be the only connected to the internet?    

And that only traffic from port 443 should be allowed to the ADFS proxy ?    

Do External users need a certificate from ADFS proxy or ADFS Server?    

Should the ADFS proxy be joined to the domain?    

How to secure ADFS proxy since it is facing the internet?    

I am planning only 1 ADFS Server, is the ADFS farm a failover solution? Can I easily add new one ADFS server to an existing one to form a FARM?    

I have been searching  the internet and there are tons of resource that so much information it's hard to have an answer to my questions. I hope somebody could give clarity to my questions.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-06-07*

Hi Janus,  

Welcome to ADFS ... haven't posted in a while so this whole new Q&A setup is new to me :) .. Let's try and help with some of your questions. Your diagrams are looking pretty good. One thing you might want to add by way of explanation is the external/internal representation of how ADFS works with regards to DNS. AD FS uses split(brain) DNS. In a basic ADFS Internet-facing configuration, the external name will resolve to the internet registered IP address of your AD FS proxy, more commonly known as Web Application Proxy (WAP), or the external firewall in front of it, which is then doing NAT to the proxy.  Internally, on the LAN, via AD, the federation service will point to the internal address of your AD FS farm nodes. This is an important distinction because externals connect to the Web Application Proxy (WAP) and do forms-based logon, entering username/password by way of a web form. Your internal clients point to the AD FS farm nodes, and, having line-of-sight to domain controllers get transparent login to web resources protected by AD FS, by way of Single-Sign On (SSO), for domain-joined machines.  The ADFS management interface, allows tweaking authentication options based around Extranet (Internet) and Intranet (Internal), according to the desired authentication methods that need to be supported.  

"What ports are needed to communicate between the ADFS and DC?" ... your AD FS farm nodes should be right next to your DC, since they are security-equivalent to domain controllers. If they happen to be in a different zone/compartment of your network, then you'll need to open all the usual Windows firewall ports expected of communication between a member server and a domain controller on the firewall. Check here for more information. Port 443 is the only port required between the WAP and AD FS farm, until we add more complex configurations like load balancers between WAP.    

On the question of scaling out, you can begin with single nodes and expand to more nodes later. If your organization doesn't have hardware load balancers in place, you could use Windows Load Balancing to load balance traffic across multiple WAP or farm nodes in each respective segment. It's a limited solution feature-wise compared to dedicated offerings in the market, but might afford some availability should you wish to expand to the configuration.  

On the certificate side of things, it depends on what is in place and the size of your organization. If you have an AD Certificate Services (AD CS) platform in place, it's quite common to see the AD FS farm nodes using a service communications certificate issued to it from that PKI platform. The WAP, conversely, would have a certificate issued to it from one of the many commerical SSL certificate providers available on the Internet. In smaller configurations, the latter 3rd party certificate is often shared between AD FS farm and WAP, or a wildcard certificate is purchased and shared between front and back-ends.  

As you state, yes, the ADFS proxy should be the only thing connected to the Internet and normally this will be behind a NAT firewall of some sort (in a DMZ). In most configurations, the WAP does not need to be domain-joined, although mileage does vary on this. For example, if your DMZ has a dedicated domain, the WAP might be joined to that for management purposes. Another reason might be if you need to provide Kerberos SSO to on-premise web applications using constrained delegation.  

Security ADFS is a layered approach and the best practises that are applicable, often apply to the platform as a whole. Here a few:  

-  Disable AD FS endpoints you are not using. WAP endpoints can be disabled, independent of the AD FS farm nodes.  

-  Use Multi-Factor Authentication (MFA) either through Azure MFA or a 3rd party MFA provider for all Extranet clients.  

-  Enable Smart Extranet Lockout to shield AD passwords from attacks and build-out risk-based access.  

-  Use a gMSA instead of a standard service account  

-  Add the ADFS farm URL to the Local Intranet Zone of your (IE) browser, so that clients do Kerberos to AD FS instead of NTLM.   

-  Disable idpinitiatedsignon.aspx to prevent password spray attacks against AD, if the version you are using has it enabled (check via PowerShell --- Get-ADFSProperties)  

-  Use "Conditional Access" policies to differentiate between managed/unmanaged clients and/or IP location or user/groups  

-  Download the Microsoft Security Compliance Toolkit 1.0 and apply Group Policy (GPO) baselines to your servers (as a whole). You can use LGPO as a tool to export server baselines to your WAP if not domain-joined.  

-  Use Fine-Grained Password Policies  

-  Disable weaker SSL ciphers (SSL 3.0,TLS 1.0,1.1)  

-  Patch regularly!  

There are lots of other things that deserve mention security-wise, such as further OS/AD/application security points, or those that my memory and ignorance preclude/elude me respectively. Let's call this a starter :) Good luck!  

Regards,  

Mylo
