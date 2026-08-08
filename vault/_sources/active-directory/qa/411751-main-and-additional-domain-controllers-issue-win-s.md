---
title: "Main and Additional Domain Controllers issue (Win SRV 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/411751/main-and-additional-domain-controllers-issue-win-s
question_id: 411751
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Main and Additional Domain Controllers issue (Win SRV 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/411751/main-and-additional-domain-controllers-issue-win-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

I have 2 sites and MPLS connection with firewall between it. See the sites configuration information  

Site A: 2 domain controllers main and additional installed before.  

Site B: additional domain controller recently installed and open all required ports between the DC’s.  

Everything is ok between the DC’s like sync, replica, … But if I want to join any device in site B that display the below error.  

dcdiag(join error)  

The domain name "DomainName" might be a NetBIOS domain name. If this is the case, verify that the domain name is properly registered with WINS.  

If you are certain that the name is not a NetBIOS domain name, then the following information can help you troubleshoot your DNS configuration.  

The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "DomainName":  

The error was: "DNS name does not exist."  

(error code 0x0000232B RCODE_NAME_ERROR)  

The query was for the SRV record for _ldap._tcp.dc._msdcs.DomainName  

Common causes of this error include the following:  

-  The DNS SRV records required to locate a AD DC for the domain are not registered in DNS. These records are registered with a DNS server automatically when a AD DC is added to a domain. They are updated by the AD DC at set intervals. This computer is configured to use DNS servers with the following IP addresses:  

10.30.100.30  

-  One or more of the following zones do not include delegation to its child zone:  

DomainName  

. (the root zone)  

Note: the device joined if all ports opened between the main DC in site A and clients subnet in site B.  

If I want to join any device in site B to the domain we need to see or access the main domain controller in site A or not.  

Please can you send me a document for this issue.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-31*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-28*

Hi,  

To know the issue more clearly, please confirm the following information.  

1, Did the DC in site B act as a RODC or RWDC? Did it act as a DNS server?  

2, When you join the client to domain, how did you configure the DNS server for the client?  

3, Did you check the DNS records for the DC in site B?  

4, Are there any errors if you run the following commands：  

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps *   

Ipconfig /all  

If there are available DCs in site B, device don't need to access DCs in site A every time.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-27*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
