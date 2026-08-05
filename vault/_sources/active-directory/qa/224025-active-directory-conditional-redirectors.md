---
title: "Active Directory : Conditional redirectors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/224025/active-directory-conditional-redirectors
question_id: 224025
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory : Conditional redirectors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/224025/active-directory-conditional-redirectors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I have two domain in two forests with conditional redirectors.    

However, it displays : Unable to Resolve. Is this normal?    

    

When i do Nslookup NameOfMyDC.com    

Server: UnKnown    

Address: :: 1    

Non-authoritative response:    

Name: NameOfMyDc.com    

Address: 172.31.150.20    

Why Server : Unknown ?    

Thanks in advance for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-15*

Hello,  

Thanks a lot for your help. I could correct the problem and above all understand.  

THanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Hi, Thanks for your answer.    

I have build the two conditional redirector for the 2 forest.    

From computer on Domain A    

C:\Users\Test>nslookup Computer.domainB    

 Serveur :   DC.DomainA    

 Address:  172.31.150.20    

 Réponse ne faisant pas autorité :    

 Nom :    Computer.domainB    

 Address:  172.31.160.92    

 C:\Users\Test>nslookup DC.domainB    

 Serveur :   DC.DomainA    

 Address:  172.31.150.20    

 Réponse ne faisant pas autorité :    

 Nom :    DC.DomainB    

 Address:  172.31.160.20    

 From computer on Domain B    

 C:\Users\test>nslookup computer.domainB    

 Serveur :   Unknown    

 Address:  172.31.160.20    

 Réponse ne faisant pas autorité :    

 Nom :    Computer.domainA    

 Address:  172.30.10.100    

 C:\Users\test>nslookup dc.domainA    

 Serveur :   Unknown    

 Address:  172.31.160.20    

 Réponse ne faisant pas autorité :    

 Nom :    DC.domainA    

 Address:  172.31.150.20    

Why i got Server : Unknown ? is it's normal ?    

    

On control panel of redirector : Resolution Impossible    

Thanks in advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-11*

Hi,    

Based on my understanding , you want to set up Conditional Forwarders  between 2 forests for  name resolution ,right?    

When you set up Conditional Forwarders :    

Type the IP address of the DNS server that will resolve queries from the domain you entered in the previous step and press ENTER.    

If the DNS server can be reached, after a few seconds the Server FQDN name field will display the name of the DNS server.    

And you can check if the DNS can be resolved as following :    

    

If the Conditional Forwarders created successfully, then when you run nslookup, the dns name should be able to resolved :    

    

Best Regards,
