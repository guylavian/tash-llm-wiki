---
title: "Account Policies and others missing in GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185618/account-policies-and-others-missing-in-gpo
question_id: 2185618
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Account Policies and others missing in GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185618/account-policies-and-others-missing-in-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i noticed in the Default Domain Policy that items such as Account Policies are missing in the GPO  

Computer Configuration > Policies > Windows Settings > "Account Policies"

  

normally it would look like this.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-19*

Hello Jeff Uson,  

Thank you for posting in Microsoft Community forum.  

Please check or troubleshoot the issue as below.  

1.How many Domain Controllers are there in your domain?  

2.If you edit other GPOs on the same Domain Controller, can you see Account Policies and other missing settings?  

3.If you edit the same GPO (Default Domain Policies) on other Domain Controllers, can you see Account Policies and other missing settings?  

4.Please check AD replication status if you have more than one Domain Controllers in the domain.  

Please run commands below on PDC.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep1.txt  

repadmin /showrepl * /csv >c:\repsum.csv

5.From the screenshot you provided, I can see the ADMX files and ADML files are retrieved from Central Store. Please check the SYSVOL replication status on Domain Controllers.  

For example 1:  

If you have two Domain Controllers in this domain.  

Create a file named F1 under path \domain.com\SYSVOL\domain.com\policies on DC1.  

Create a file named F2 under path \domain.com\SYSVOL\domain.com\policies on DC2.  

Check if F1 is replicated to DC2 and if F2 is replicated to DC1.  

For example 2:  

If you have three Domain Controllers in this domain.  

Create a file named F1 under path \domain.com\SYSVOL\domain.com\policies on DC1.  

Create a file named F2 under path \domain.com\SYSVOL\domain.com\policies on DC2.  

Create a file named F3 under path \domain.com\SYSVOL\domain.com\policies on DC3.  

Check if F1 and F2 is replicated to DC3  

 And check if F1 and F3 is replicated to DC2.  

 And check if F2 and F3 is replicated to DC1.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
