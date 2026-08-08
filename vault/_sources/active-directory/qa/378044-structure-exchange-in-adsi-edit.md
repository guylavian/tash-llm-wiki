---
title: "Structure Exchange in ADSI edit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/378044/structure-exchange-in-adsi-edit
question_id: 378044
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Structure Exchange in ADSI edit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/378044/structure-exchange-in-adsi-edit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys.  

i have this issue, hope some one can give me solution.  

My enviroment is: 1 root 2 child domain. All domain controller is Windows server 2012R2  

My exchange server 2013 CU9 is install in root domain.  

When i use ADSI edit in root domain controller, connect to configuration.  

i see Exchange structure like this picture:  

But when i use ADSI edit in child domain controller, connect to configuration.  

I don't see exchange structure.  

When i check replication from root DC to child DC. Everything is OK.  

Hope anyone can give me solution..  

Thanks guys

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-30*

Hi Zhou.  

I have use command repadmin /showrepl and repadmin /replsum in both root and child domain controller.  

Everything is fine. No error.  

...

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-30*

Hello @Cuong. Tao Minh - CTS TSD  ,

Thank you for posting here.

It looks like there is issue between AD replication.

Please check AD replication in the entire AD forest.

1.Make AD replication forcely by running command: repadmin /syncall /AdeP >c:\rep1.txt

2.Check AD replication by running commands below on PDC in the root domain.

repadmin /showrepl >c:\rep2.txt

repadmin /replsum >c:\rep3.txt

repadmin /showrepl * /csv >c:\repsum.csv

Check all the result of the commands above, if all the result is OK without any error, it means AD replication is OK.

Hope the information above is helpful

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
