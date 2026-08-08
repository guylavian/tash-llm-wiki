---
title: "AD replication between site - LDAP error 32 (No Such Object) Win32 Err 1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/406370/ad-replication-between-site-ldap-error-32-no-such
question_id: 406370
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD replication between site - LDAP error 32 (No Such Object) Win32 Err 1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/406370/ad-replication-between-site-ldap-error-32-no-such (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When i run repadmin /showrepl. I found this error at the picture.     

I run repadmin /replsum is success.      

But AD can replicate USER object and GPOs object are success

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-25*

Hello @Kittiphol Tubtimsri  ,

Thank you for your update.

From the error, maybe this DC (you run command repadmin /showrepl in the post) can not replicate with its replication partner.

1.So please check if there is new promotred DC or old failed DC (removed DC but not be removed completely) that cannot replicate with this DC (you run command repadmin /showrepl in the post).

2.How many DCs do you have in your AD forest? We can run nltest /dclist:domain.com to check.

3.Compare the number/the DC name of all DCs in the result of all the commands.

For example:  

We can see SVR05 after running dcdiag, but we can only see SVR01,SVR02,SVR03 and SVR04 after running repadmin /replsum.  

Here is a similar case you can refer to. And you can troubleshoot the issue based on the steps in this case.

Non replicating DC  

https://community.spiceworks.com/topic/1951176-non-replicating-dc

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-24*

Hello @Kittiphol Tubtimsri  ,

Thank you for posting here.

1.Could you show me all the result after the command above?

Meanwhile, please check AD replication after running the following commands.

repadmin /syncall /AdeP >c:\rep1.txt

repadmin /replsum >c:\rep2.txt (It is successsful you mentioned.)

repadmin /showrepl * /csv >c:\repsum.csv

If there is no any error message about all the result, it means AD replication works fine.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
