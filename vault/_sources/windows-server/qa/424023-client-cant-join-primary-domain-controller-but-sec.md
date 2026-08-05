---
title: "Client can't join primary domain controller but secondary domain controller is working normal?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/424023/client-cant-join-primary-domain-controller-but-sec
question_id: 424023
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Client can't join primary domain controller but secondary domain controller is working normal?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/424023/client-cant-join-primary-domain-controller-but-sec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,    

I have two domain controller primary and secondary domain controller on windows server 2016 Standard. Now i have some issue with my client any new client PC with windows 10 can't join primary domain controller but my secondary domain controller is working fine. I notice that yesterday i have try to install WSUS server ( But this server is other Host ) then a new PC can't join and also client configure DNS primary domain controller also can't access to website but ping to IP is working fine. I'm not sure 100% with WSUS server.    

Any idea?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-08*

Glad to hear it helps. There appears to be some replication problems between domain controllers. You'll need to examine the event logs on both for more details. This is the reason the policy is not replicated. Depending on the errors found you may need to perform a non-authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-08*

On TT-DC01-2k16 I'd add domain controller's own static ip address (10.10.101.101) listed for DNS, then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service    

There may be some replication problems between domain controllers. You'll need to examine the event logs on both for more details    

I'd check the the required ports are flowing between the networks 172.21.11.1 and 10.10.101.1    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-07*

Hello @kimseng vit  ,

Thank you for posting here.

Based on the description, I understand you want to join a WSUS server to the existing domain with two DCs (a primary domain controller and a secondary domain controller).

Please troubleshoot as below:

-   Before we do any change in existing AD domain environment, we had better do:  

    1-1Check if AD environment is healthy. Check all DCs in this domain is working fine by running command Dcdiag /von each DC.  

    1-2Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on primary DC.  

    1-3Check if both SYSVOL folder and Netlogon folder are shared by running net share on each DC.  

    1-4Check if we can update GPO by running command gpupdate /force on each DC successfully.

2.Check if you set static IP addresses for both DCs.

For example:  

3.Check if primary domain controller and secondary domain controller are all DNS server (I mean check if you install and configure DNS role on both DCs).

Or check if there is NS record for both DCs in the DNS manager.

For example:  

4.Check if you set the correct preferred DNS server on WSUS server （Please double check here, no one number can be wrong ）.

For example:

5.Check if you type the correct domain name when joining the server into domain.

If it does not work, please confirm:

1.Based on "Now i have some issue with my client any new client PC with windows 10 can't join primary domain controller but my secondary domain controller is working fine. ", did you mean when you set the Preferred DNS server using the IP address of primary domain controller on WSUS server, you cannot join the WSUS server to domain, but when you set referred DNS server using the IP address of secondary domain controller on WSUS server, you can join the WSUS server to domain, is it right?

2.What did you mean "also can't access to website"?

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-07*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
