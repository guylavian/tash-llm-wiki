---
title: "Trouble with group policy probably due to SYSVOL DFRS replication issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/367658/trouble-with-group-policy-probably-due-to-sysvol-d
question_id: 367658
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Trouble with group policy probably due to SYSVOL DFRS replication issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/367658/trouble-with-group-policy-probably-due-to-sysvol-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.    

It's some time I notice clients apply some group policy after a high delay and at times they don't even get applied. In particular a policy that adds Shared Printers.    

Yesterday I noticed that three (out of six) DCs are always in status "replication in progress"    

    

Could somebody please help me out?    

Thank you and best regards.    

Roberto

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-27*

Hello @Roberto  ,

I am sorry for the late reply.

Thank you so much for your update.

And from the information you have checked and provided, it seems or I can see:

1.The AD replication in your domain works fine  

2.The SYSVOL folder is synchronized （the number of items in the same path on all DCs is the same--157）.

Now based on the error message, we can compare the permissions of one GPO on baseline DC (SV-102-DC) and another DC (sv-108-dc)

1.Find the GPO with the following GUID on both DC.  

2.Right click this GPO and select Properties.  

3.Security tab and Advanced button and compare "Permission entries".  

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-26*

You can try a non authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

or simply move roles off, demote, reboot, promo it again.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-23*

Hello @Roberto  ,

Thank you for posting here.

Based on the description, I understand you have one domain with five DCs.

Before we troubleshoot SYSVOL DFSR replication issue, we must check whether AD replication between the five DCs works fine.

If there is any issue about AD replication between all the five DCs, we should fix AD replication issue first, then trouble SYSVOL DFSR replication issue.

If AD replication between all the five DCs works fine, then if there is indeed SYSVOL DFSR replication issue, we can troubleshoot SYSVOL DFSR replication issue.

Check AD replication status:

1.On the PDC, run the command below to force AD replication immediately and check if there is any error message.

repadmin /syncall /AdeP

2.On the PDC, run the three commands below to check there is any error message in the result.

repadmin /showrepl >c:\rep1.txt

repadmin /replsum >c:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

If all the results of the four commands above are OK without any error message, it means AD replication in your AD environment is OK.

Then check SYSVOL DFSR replication issue:

1.On all DCs, we can check if the number of the items under C:\Windows\SYSVOL\domain\Policies is the same or not.

2.If the number of the items under C:\Windows\SYSVOL\domain\Policies on the three DC you mentioned is not the same as baseline DC (SV-102-DC).

Tip: the number of the items under C:\Windows\SYSVOL\domain\Policies is the largest on baseline DC.

3.It means SYSVOL DFSR replication on the three DCs is not in sync.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-22*

You can try a non authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

or simply move roles off, demote, reboot, promo it again if tombstoned. The event log should have more details.  

--please don't forget to Accept as answer if the reply is helpful--
