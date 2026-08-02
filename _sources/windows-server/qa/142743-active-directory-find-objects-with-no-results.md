---
title: "Active Directory find objects with no results"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142743/active-directory-find-objects-with-no-results
question_id: 142743
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory find objects with no results

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142743/active-directory-find-objects-with-no-results (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Find object function in active directory has stopped working for some reason? On the screen shot's, I have searched the entire directory and with no filters in place for the name Mark. No results are found yet we have 3 Mark users! This is the same result no matter what name I search for?    

We have 3 DC's and this has replicated around them all even for all other technicians which cancel's out any profile issues.    

Any help would be much appreciated.    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

Hi Hannah,  

Unfortunately I have tried this on all domains and all DC's with no change in results. What I have noticed is that when I go to add users to groups and via the advanced method, click find now which should give me a massive selection of all users if no filter is applied...I get the attached error and only selecting the last group/user I looked at previously? Not sure if this information helps at all?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*



## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-02*

Hi Mark,    

You are welcome. Thank you so much for your feedback.    

It is a little weird. If we narrow down the scope to the specific domain, could the user be found? Such as:     

    

    

Besides, have we tried to check the Find object function on all the three DCs? Does this function not work on all the three DCs?    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

Hi,  

Thanks for getting back to me.  

To answer your questions:

1, Could we find other users except Mark? No other users can be found  

2, Could we find the Groups? No groups can be found  

3, If we select other choices, such as Computers, Shared Folders, could we find them? No results for any search can be found

Secondly, we would suggest to have a check whether our AD environment is healthy:  

1.We should check if all DCs work fine by running Dcdiag /v on every DC. All completed Successfully

2.And check if AD replication is working properly by running repadmin /showrepl and repadmin /replsum on every DC. All completed Successfully

3.To check the whole AD replication status by running **Repadmin /showrepl /csv >showrepl.csv* on one of the DCs. No failures with a replication time stamp of 6:05 this morning

All replication and server services seem fine so i'm unsure what this could be?  

The funny this is that is have replicated round all 3 of our dc's so a change has been made somewhere! We had a few updates that were installed but this is normal.  

Thanks  

Mark

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Hello @M Lewin  ,    

Thank you so much for posting here.    

Firstly we need to check whether it is the specific users could not be found or the Find object function does not work. To narrow down the issue, we would like to get more information from you.     

1, Could we find other users except Mark?    

2, Could we find the Groups?     

3, If we select other choices, such as Computers, Shared Folders, could we find them?    

    

Secondly, we would suggest to have a check whether our AD environment is healthy:    

-  We should check if all DCs work fine by running Dcdiag /v on every DC.    

-  And check if AD replication is working properly by running repadmin /showrepl and repadmin /replsum on every DC.    

-  Check the whole AD replication status by running Repadmin /showrepl * /csv >showrepl.csv on one of the DCs.     

Last, if it is the specific user could not be found. We could try below to see whether it could solve the issue.     

When the user object is found in a container, right click and move the object to a different container. Then check whether the object becomes visible when using the Find function. If it is visible, we could move it back and then have a recheck.     

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
