---
title: "SYSVOL Replication Issues Windows Server 2019 Eval"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/292420/sysvol-replication-issues-windows-server-2019-eval
question_id: 292420
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# SYSVOL Replication Issues Windows Server 2019 Eval

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/292420/sysvol-replication-issues-windows-server-2019-eval (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I have not been able to find someone with this exact issue however I have three Windows Server 2019 Evaluation Editions running for testing and educational purposes. I created this active directory on Windows Server 2019 and I had group policies set to auto config for Windows Hello For Business. I am looking at the local group policy folder on my PC which is joined to the AD and it has not synced my AD polices.  

I have each servers DNS pointing at each other and 127.0.0.1 as the third DNS option in each server.   

I go to run the command "dfrs /setglobalstate 1" and it will return with   

Unable to create DFSR Migration log file.   

Unable to create DFSR Migration log file. Error 5                                                                                                                                                                                            Current DFSR global state: 'Eliminated' New DFSR global state: 'Prepared'   

Invalid state change requested.  

I think this is because Windows Server 2019 does not need to migrate but every guide that I have read uses this to sync between their servers or maybe I am reading false sources.  

Any help is appreciated,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-04*

Hi,    

Since there are 1726 error and 1722 error, i would also suggest you check if DFS Replication service is running on all members and the firewall configuration .    

Following link for your reference:    

Active Directory replication error 1722: The RPC server is unavailable    

https://social.technet.microsoft.com/Forums/WINDOWS/en-US/d27bd902-034e-4230-9516-0ede42308193/event-5014-dfsr-error1726?forum=winserverfiles    

I would delete the logs due to security reason.    

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-02*

I'd check the DFS Replication service is running on all members and that ports required are flowing between sites.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-01*

Might check the event logs for clues, other things to try are a non-authoritative synchronization, or try demote, reboot, promo again.  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-01*

That's correct. Server 2019 OOB uses DFSR, Server 2016 is the last operating system where FRS was an option (from directory upgrade) for active directory replication technology. Server 2003 was the last operating system to use FRS OOB when creating a new domain.  

--please don't forget to Accept as answer if the reply is helpful--
