---
title: "Time Sync Issue on Domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188071/time-sync-issue-on-domain-controller
question_id: 2188071
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Time Sync Issue on Domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188071/time-sync-issue-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All

We have Single forest multiple domain controller environment and currently we are also managing the different forest due to migration. 

Example : We have forest with the name  "Test.com" and another forest with the name  "Best.com" . Due to migration, we have created one domain controller with the name "A.Test.com" and this VM hosted in Best.com Hyper V . We are trying to sync time with Test.com PDC server but this domain controller A.Test.com is not syncing with the test.com domain and showing local time after running the command w32tm /quey /status.

We have checked all the required ports are open and 123 port also opened and network team confirmed that there is no issue with the network side. Please help me to resolve this issue. 

I would really appreciate for your response.

* Moved from Community Center

## Answer (community) — community member

*upvotes: 3 · updated: 2023-09-10*

Hi Rakesh,

Make sure the integration for time sync with the hyper-v host is turned of on the VM or this will overrule the sync

run the following commands on the guest  to restore the domain sync:

w32tm /config /syncfromflags:domhier

(this will make the server resolve the PDC as timesource)

wait a minutes, then run

Net stop "Windows Time"

Net start "Windows Time"

after a few minutes run 

w32tm /query /source

to confirm success

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-11*

Hello RakeshKumar0219,  

Thank you for posting in Microsoft Community forum.  

Based on the description, I understand the information below:  

You have two forests:  

Forest one: test.com  

Forest two: best.com  

You have created one domain controller (the name of this Domain Controller is "A.Test.com", this Domain Controller is a VM hosted in Hyper V.   

Would you please confirm if this Domain Controller is in test.com domain? If so, the time on this Domain Controller should be synchronized with the time on the PDC in test.com.

You can try to check the information/setting below:  

1.Turn off the time sync in Hyper-V.  

2.Check the registry setting on this DC.  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\Type

Key Name: Type

Type: REG_SZ(String Value)

Data: NT5DS

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config

Key Name: AnnounceFlags

Type: REG_DWORD (DWORD Value )

Data: 0xa

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-04*

Hi Daisy,

Good day! what if the value of what you have mentioned above is different from the settings i have for our environment should I change it to the one you have mentioned?

Thanks,

Charlie
