---
title: "Get-AdGroupMember and LDAP Query Disagree"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387303/get-adgroupmember-and-ldap-query-disagree
question_id: 387303
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Get-AdGroupMember and LDAP Query Disagree

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387303/get-adgroupmember-and-ldap-query-disagree (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a group in Active Directory; let's call it DSA.  If I run Get-AdGroupMember on it, then I get 64 members. But if I use LDAP, such as "(&(objectCategory=user)(memberof=$($DSA.DistinguishedName)))", then I only get 59 members.  If I look at DSA in ADUC/ADAC, I see 64 members, but if I look at (get-adgroup $DSAgroup -Properties member).member, then I only get 59 members.  

It seems to be the same five accounts that don't show up in all cases (even though I am always logged on as me). What could cause them to not be produced sometimes?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Thank you for your response, @Anonymous   .  I can Get-ADUser $user successfully for all five of the users that are missing, so I suppose that means I have appropriate permission.      

And now for some more-interesting evidence: if I enumerate another group that contains these users, using the methods above, I get these users in question, but a different user doesn't show up consistently.      

So I'm not sure what else to do to get consistent results.      

However, as a workaround, I used DSGET in a script and got the results I wanted.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-12*

Hello @Roger Seekell  ,    

Thank you for your update.    

Please check if your account has permission to read the five accounts that don't appear via PS or GUI.    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

Thank you for your reply.  The DSA group is a Global Security group.    

All the group members are in the same domain, as well as the group itself.    

It's the same five accounts that don't appear depending upon the method.  The five are direct members of the group.  All but one of the five are enabled and used daily.    

Unfortunately, I am not a domain admin, so I cannot log into a DC and run REPLADMIN.  

I can say that these accounts and this group have existed for years.   

Maybe there's something different about these users. Or maybe just the group.  Any ideas?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-10*

Hello @Roger Seekell  ,

Thank you for posting here.

I check two groups based on the methods you mentioned above.

The result is: the number of the members in the two groups is the same.

For example:  

One built-in Administrators group.  

One custom a group named group00.  

Please check:

1.Please check the group scope and group type of this DSA group.  

2.Can you find the same five accounts that don't show up in all cases? If the same five accounts that don't show up in all cases are still in the AD forest or not (check if the five accounts are disabled or deleted)?  

You can try to search in the forest.

3.Check whether your AD replication works fine by running commands below on PDC.

repadmin /syncall /AdeP >c:\rep1.txt

repadmin /showrepl >c:\rep2.txt

repadmin /replsum >c:\rep3.txt

repadmin /showrepl * /csv >c:\repsum.csv

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
