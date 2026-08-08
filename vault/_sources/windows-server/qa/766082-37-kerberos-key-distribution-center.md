---
title: "37 Kerberos-Key-distribution-Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/766082/37-kerberos-key-distribution-center
question_id: 766082
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# 37 Kerberos-Key-distribution-Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/766082/37-kerberos-key-distribution-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there,   

I have several DCs in my network (2012 Standard , 2016 Standard). One of my DCs keeps repeating the following error :   

 Event ID 37   

Source : Kerberos-Key-Distribution-Center   

The Key Distribution Center (KDC) encountered a ticket that did not contain information about the account that requested the ticket while processing a request for another ticket. This prevented security checks from running and could open security vulnerabilities. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.  

  Ticket PAC constructed by: servername  

  Client: domain\username  

  Ticket for: krbtgt  

I already followed the instructions on this link : https://go.microsoft.com/fwlink/?linkid=2173051 and setup every DC with the enforced registry key :   

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Kdc   

I know this will be deployed by different phases.   

However I still have a few questions :   

-  Is it normal to keep getting the error after we setup the enforced key on every DC ?   

-  Is there a way to make the error go away ?   

-  Is manually entering the enforcement key part of the process ?  

Thanks in Advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-26*

NOT the answer but feeling like I'm getting closer to a solutions.   As mentioned on my earlier post,  I am experiencing the same issue (Event ID 37) as the post above and also prevents users from being able to RDP.   This is not the solution, rather a workaround which is better that having to constantly reboot the DC.  I narrowed it down and found that by temporary disabling the kdc service or disabling the NIC, the affected users were successfully able RDP.   I know it's not much but hoping this information helps someone might use this information to find a permanent solution.  

My setup - 3 Windows 2019 Domain servers, schema 2016 and only one DC is generating Event ID 37.  This culprit DC is also the only one fully patched.  I'm hesitant on patching the rest as I am worried this my trigger more problems afterwards.

I found the following articles/forums useful to some degree, although none helped resolve this issue. 

 https://techcommunity.microsoft.com/t5/windows-it-pro-blog/latest-windows-hardening-guidance-and-key-dates/ba-p/3807832

https://my.f5.com/manage/s/article/K40933118

https://learn.microsoft.com/en-us/windows/release-health/windows-message-center#3052

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-13*

Hi,

Did you find a solution at your problem i Have exactly same issue after first install of 2019DC on 2008R2 forest.

So i don't Know if i have to decommission all 2008R2 DC and it will be find or not.

Or do i have to install all patches included in the article manually because i don't have extended support so no more updates.

I'm a little bit confused about which patch i have to install 

On 2019 they are already up to date do i need to do something ?

Thanks in advanced

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-07*

I am experiencing the same exact problem as Jdharvey. Hoping someone would post a  solutions.  My last resort is to rebuild the DC.  Not even sure if this will resolve this issue.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-23*

I have fully patched all DC's and still receiving Event 37, Kerberos-Key-Distribution-Center repeatedly on accounts.  I read that you should get one per user, I am getting multiple per user, per day.

I am not sure what else to do at this point.  I am having issues with RDP, and other kerberos related authentication.  The only way around the RDP auth issue is to use the IP address, or sometimes to reboot DC's.

App servers will fail SSO using Kerberos, which requires a reboot of the DC that the user is authenticating from.
