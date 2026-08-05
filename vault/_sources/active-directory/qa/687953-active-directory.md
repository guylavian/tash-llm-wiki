---
title: "Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/687953/active-directory
question_id: 687953
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-vpn-gateway", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/687953/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support,  

I have deployed AD environemnt in the local ( ADDS, DNS, DHCP ), and now I want to know if there is any solution you could share like VPN to help me make the remote machine (not in the intranet, this means it doesn't have the same subnet as DC, for example the computer in the home) to join the AD domain?  Any guidance would be appreciated!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-10*

entered the VPN server address ( my AD server's public IP  

Not sure what is meant here. Active directory cannot function on a public network. Also installing a VPN on a domain controller is also not going to work as already mentioned.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-09*

You can follow along here but do not install RRAS role on domain controller as the multi-homing will cause no end to grief for active directory DNS  

https://www.thomasmaurer.ch/2018/05/how-to-install-vpn-on-windows-server-2019/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-09*

Thanks for all your help, however, my main point is how to establish the VPN ( how to deploy it) and then make my remote machine can connect to the DC?  Could you share the detailed steps or articles?  

Thx

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-01-08*

Hi,    

There is many solution to establish VPN solution , below a exemple:    

enable-directaccess    

If you have only one AD site , you have to open required network flows to let remote machine contact domain controllers:    

UDP and TCP Port 135     

UDP Port 389 for LDAP : LDAP queries.    

TCP and UDP Port 464 : Kerberos Password Change    

TCP and UDP Port 53 : DNS queries .    

UDP Port 88 : Kerberos authentication     

TCP and UDP Port 445:SMB    

TCP Port 3268 and 3269 : from client to domain controller for Global Catalog service    

You can click here to have more details about required network flows between client and domain controllers: config-firewall-for-ad-domains-and-trusts    

If in your active directory topology you have many sites , you should add the subnet of remote machine to closest site and open required network flows.    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-08*

Something here may help.  

https://theitbros.com/join-domain-and-login-over-a-vpn-connection/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
