---
title: "AD CS Ports"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/472219/ad-cs-ports
question_id: 472219
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# AD CS Ports

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/472219/ad-cs-ports (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys! I have ad cs infrustructure with root ca (offline) and SubCA. On my firewall i openned tcp 80,443,135 in both side (client -> ca, ca->client). In documentation i see that i need tcp port 49152-65535. Can i openned it from client to ca?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-07-13*

Hello @Алюшин Владислав  ,    

Thank you so much for posting here.    

Certificate Services relies on RPC and DCOM to communicate with clients by using random TCP ports that are higher than port 1024. So please open TCP port 49152-65535.     

For more information, please refer to:    

https://learn.microsoft.com/zh-tw/archive/blogs/pki/firewall-rules-for-active-directory-certificate-services    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-23*

You will need high-range ports 49152-65535 for the Auto-enrollment to work properly. I captured the traffic from Clients to CA and found this out.

For enrollment alone, you will need RPC port 135.

from CA servers to clients, you don't need any ports to be opened.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-12*

Hi,  

a modern firewall should be able to handle ephemeral RPC high ports but you will probably have to enable that functionality for a specific source/target pair.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-12*

i have hardware firewall and i need open ports    

Ok, new info. These ports should be allowed to flow through firewall.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-12*

The client should get the domain firewall profile then the required ports are automatically part of the profile.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

When NLA starts to detect the network location, the machine will contact a domain controller via port 389. If this detection is successful, it will get the domain firewall profile (allowing for correct ports) and we cannot change the network location profile.     

If the domain was not found or process failed, NLA will let you to determine which firewall profile will be used, private or public.     

The Network Location Awareness (NLA) service expects to be able to enumerate the domain’s forest name to choose the right network profile for the connection. The service does this by calling DsGetDcName on the forest root name and issuing an LDAP query on UDP port 389 to a root Domain Controller. The service expects to be able to connect to the PDC in the forest domain to populate the following registry subkey:     

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Nla\Cache\IntranetForests     

If something hinders the DNS name resolution or the connection attempt to the DC, NLA is not able to set the appropriate network profile on the connection.    

So I'd check the domain controller and problem client have the static address of DC listed for DNS and no others such as router or public DNS    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
