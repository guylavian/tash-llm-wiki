---
title: "Cross-forest certificate enrollment - copying ADCS objects"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/428653/cross-forest-certificate-enrollment-copying-adcs-o
question_id: 428653
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cross-forest certificate enrollment - copying ADCS objects

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/428653/cross-forest-certificate-enrollment-copying-adcs-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am following guide for Cross-forest certificate enrollment. Now it is time for .\PKISync.ps1 -sourceforest forest1DNSName -targetforest forest2DNSName -f but it fails:

Exception calling "GetForest" with "1" argument(s): "A local error has occurred.  

"  

At C:\Temp\PKISync.ps1:288 char:5  

-  $ForObj = [System.DirectoryServices.ActiveDirectory.Forest]::GetF ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (:) [], ParentContainsErrorRecordException  

-  FullyQualifiedErrorId : ActiveDirectoryOperationException

Any help on this would be awesome to proceed.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-10*

Hello @Bojan Zivkovic  ,

Thank you for posting here.

1.Did you follow the article below?

AD CS: Deploying Cross-forest Certificate Enrollment  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff955845(v=ws.10)

2.Did you "Create a two-way forest trust between the resource forest and account forests"? You need to do so.

From the error message "Exception calling "GetForest" with "1" argument(s): "A local error has occurred." you provided, it seems it can not find forest name (maybe source forest or target source), please check both the source forest name and target forest name in the command is correct or not.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
