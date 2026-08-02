---
title: "No sysvol and Netlogon folders in branch office DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/231180/no-sysvol-and-netlogon-folders-in-branch-office-dc
question_id: 231180
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# No sysvol and Netlogon folders in branch office DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/231180/no-sysvol-and-netlogon-folders-in-branch-office-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have 2 DCs in Heaf Office and 1 in a branch office connected to head office by IPsec tunnel. When I am browsing the domain in the branch office by entering domain.com, it is not showing sysvol and netlogon folders. Thus users are facing problems with the domain logon process. I checked replication health and it shows everything is fine with no errors. What else should I check to resolve this issue?  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-16*

ok going for removal.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-16*

Simplest solution may be to demote, reboot, promo the problematic one again.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-16*

running Repadmin /showreps *      

shows    

LDAP error 81 (Server Down) Win32 Err 58.    

The other files are attached. Seems a lot of errors are there.    

57323-dcdiag1.log57295-repl.txt    

Edit: HO DCs are win 2012 and BO DC is 2016.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-15*

You might work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

or a simpler solution may be to demote, reboot, promo it again.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-15*

Hi,    

Was the DC in branch office new promoted?    

Did you confirm that sysvol and Netlogon folders was created locally on the branch office DC?    

What's the result of the following commands:    

Dcdiag /v >c:\dcdiag1.log        

Repadmin /showrepl >C:\repl.txt     

Repadmin /showreps *     

If there are any errors in the report (it is not recommended share all the logs here due to the security reason), you can share a screenshot here!(Please hide the private information)    

Following link for your reference:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

Best Regards,
