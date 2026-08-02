---
title: "how to add 2019 domain controller to a windows 2012 essentials domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275249/how-to-add-2019-domain-controller-to-a-windows-201
question_id: 275249
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# how to add 2019 domain controller to a windows 2012 essentials domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275249/how-to-add-2019-domain-controller-to-a-windows-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am adding a 2019 Standard server to replace the 2012 Essentials server. I have added it to the AD and in the process of making it a domain controller. I am running onto some issues when I attempt to setup the DNS, Wins and AD Certificate authority. I was of the understanding that I could do this the same as going from2012 std. to 2019 std. as long as you had the proper licenses. - Pat Cameron

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-17*

Hi,    

Usually it requires additional preparation or steps even in the supported upgrade paths from previous version to higher ones when the server has installed specific roles.    

Server role upgrade and migration matrix for Windows Server 2016    

https://learn.microsoft.com/en-us/windows-server/get-started/server-role-upgradeability-table    

Per searching, there is no exact answer for your question but someone shared his experience when upgrade from windows 2012 essential to 2016 standard.    

Join newly created 2016 standard server as 2nd DC and transfer AD roles and data then decommission 2012 essential.    

Details and more suggestions could be found in below link.    

https://social.technet.microsoft.com/Forums/en-US/d38b412f-bfbc-4dc7-8e47-307e091357d4/windows-server-2012-essentials-upgrade-to-windows-server-2016-standard?forum=winserveressentials    

I am running onto some issues when I attempt to setup the DNS, Wins and AD Certificate authority.    

Any error messages or could you describe the issue you encountered?    

----------    

Hope this helps and please help to accept as Answer if the response is useful.    

Thanks,    

Jenny
