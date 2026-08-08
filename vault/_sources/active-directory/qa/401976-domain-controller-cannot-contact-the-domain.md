---
title: "Domain controller cannot contact the domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401976/domain-controller-cannot-contact-the-domain
question_id: 401976
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Domain controller cannot contact the domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401976/domain-controller-cannot-contact-the-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain with few domain controllers. I'm having issue with one specific domain controller. Whenever I try to search for a user to select one, I get error saying, "Windows cannot process the object with the name "Domain User"  because of following error: The specified domain either does not exist or could not be contacted."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-20*

I just found out this issue might be there with other domain controllers as well.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-20*

Hi, all domain controllers have static IP addresses. Primary DNS is configured remote domain controller and secondary with local.     

C:\Windows\system32>Repadmin /showreps *    

LDAP error 81 (Server Down) Win32 Err 58.98057-rep-sync.txt

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-20*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-20*

Hi，  

For troubleshooting, please confirm the following information：  

Did you do any changes recently?  

Confirm if there are any errors in the output of the following commands:  

ipconfig /all > C:\dc.txt make sure the DNS server was configured correctly.  

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps *   

Repadmin /syncall /APeD  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-19*

Sounds like problematic DNS. I'd check the domain controllers all have own static ip address, plus other DC ip address, plus loopback (127.0.0.1) listed for DNS and no others such as router or public DNS  

--please don't forget to Accept as answer if the reply is helpful--
