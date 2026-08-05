---
title: "DCDIAG /s:AD1 /TEST:DNS Missing SRV records"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/672390/dcdiag-s-ad1-test-dns-missing-srv-records
question_id: 672390
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# DCDIAG /s:AD1 /TEST:DNS Missing SRV records

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/672390/dcdiag-s-ad1-test-dns-missing-srv-records (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible or how can i create `_gc and `_kpasswd`srv records in DNS. Have tried open`service locator SRV`to create manually but the`service`section drop down list menu does not have those services for selection. Its only`kerberos, msdcs etc.....`  

Those records are missing in all of my dns servers and i'm unable to install exchange server 2016 CU22.  

All my Dc are running windows server 2016, only one DC is running windows server 2012 R2. Both domain and forest functional level is `windows server 2012 R2`.  

Replication is working fine.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-22*

Hello @Benard Mwanza       

Please type the following steps to see if it could resolve this issue.    

1 I’d check that did you create a standard DNS zone firstly and then perform DC promotion with the same DNS?      

2 If above done, we’ll first need to turn on the option “dynamic updates” for this DNS zone    

3 Then, type the command "net stop netlogon"  & "net start netlogon"  & “ipconfig /registerdns” on the DNS server to re-register AD records.    

4 Restart the DNS server and run dcdiag /test:dns again to see if it works.    

5 Then, please check you can see the ADI-DNS zone and _msdcs forest zone in the DNS console    

6 Surely, meanwhile, we’ll ensure that the ADI-DNS server’s connectivity and it can be ping in the domain network. Type ipconfig /all in CMD to check its IP setting with a static IP.      

7 Please also use the CMD command ipconfig /all to check if local DNS setting is correct. You’ll need to configure primary DNS itself.    

Reference link:    

Troubleshooting dynamic updates    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc756815(v=ws.10)    

Solving Dynamic Update and Secure Dynamic Update Problems    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc959308(v=technet.10)    

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-22*

Read on here.  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/the-case-of-the-missing-srv-records/ba-p/255650  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
