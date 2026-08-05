---
title: "Active Directory-based activation. How it works with subdomains/child domains?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197344/active-directory-based-activation-how-it-works-wit
question_id: 197344
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory-based activation. How it works with subdomains/child domains?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197344/active-directory-based-activation-how-it-works-wit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone! I am planning to deploy ADBA in a forest with multiple domains. There is a root domain and a subdomain. The forest is geographically dispersed. Each location has a root domain controller. Schema Version 2012R2. How to properly deploy ADBA? In which domain should I deploy to? ADBA uses Active Directory client-server communication ports https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN Does ADBA use all ports from the list or are several (which ones?) enough? Where will the server or client OS from the domain child-domain2.child-domain1.root.com get the activation object after deployment and reboot? I see this https://social.msdn.microsoft.com/Forums/en-US/a636d389-d947-4843-833f-3da52d0dd2d0/best-practice-for-volume-licensing-with-child-domains?forum=winserver8gen but this solution about KMS and DNS, not about ADBA. Thank you!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-16*

Hi,    

Active Directory-based Activation uses commonly used Active Directory client-server communication ports. Please refer to the following link:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

Based on my understanding , you can just confirm the DNS server if there are the records for the kms host. Normally, if the forest is health, no additional operations needed.    

ADBA stores its activation objects under configuration partition within Active Directory. So it replicates with the forest. This means as long as a client can contact with Active Directory, that client can be activated by receiving the activation object from a DC .No necessary to contact to the specific KMS server.    

But if there are clients with versions ADBA not supported, the client need to contact tot the KMS server.    

For more details about the process, you can refer to  :    

https://learn.microsoft.com/en-us/windows/deployment/volume-activation/activate-using-active-directory-based-activation-client#see-also    

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

The Domain Controller, in witch I deploy Volume Activation Services will be a KMS Host for SRV record in child domains?   

Question: Does ADBA use KMS host to activate operating systems?  

I understand correctly that the SRV record should be like this:  

Service name: _ldap  

Protocol: TCP  

Domain in which service is to be available: <your child domain>  

Time-to-live: 3600 seconds (recommended by Microsoft)  

Record type: SRV  

DNS priority: 0  

DNS weight: 100  

Service port number: 389  

Hostname: FQDN of your KMS Server (NOTE: Append the dot at the end of FQDN)  

will such a setting lead to the direction of all LDAP requests of the child domain to the domain controller with the role Volume Activation Services

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-15*

Hi,  

Active Directory-Based Activatio is forest wide,to use ADBA, one or more KMS Host keys (CSVLKs) must be installed on the AD forest, and client keys (GVLKs) must be installed on the client products. But no need to have a KMS host for every (child) domain.  

You can deploy it on the parent domain or the parent domain.  

Just make sure that the SRV record for the KMS host was added on the DNS server in the child or parent domain .  

For your reference:  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/active-directory-based-activation-vs-key-management-services/ba-p/256016  

Since AD-Based Activation uses AD, we use LDAP instead of the RPC 1688 tcp port used with KMS.  

For your reference:  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/active-directory-based-activation-vs-key-management-services/ba-p/256016  

Best Regards,
