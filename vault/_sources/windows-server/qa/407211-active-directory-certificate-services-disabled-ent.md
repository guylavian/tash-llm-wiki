---
title: "Active Directory Certificate Services Disabled- Enterprise SubCA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/407211/active-directory-certificate-services-disabled-ent
question_id: 407211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Certificate Services Disabled- Enterprise SubCA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/407211/active-directory-certificate-services-disabled-ent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Active Directory Certificate Services is getting disabled automatically on the SubCA which is in Azure. Any reason why that would happen?  

There is no issue with CDP/AIA. Once the service is manually enabled, CA service runs without any issue. I have another SubCA in the same subnet and it doesn't have any issue like this.  

Any leads in this regard would be appreciated. Thank you.  

Regards,  

Chaitanya.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-27*

Hello @Venkata Chaitanya Raju Konduru  ,

Thank you for posting here.

Hope the information provided by Crypt32 is helpful.

If now the issue still occurs. Can you start the AD CS service after it is disabled?

If so, you can start the AD CS service and check whether the service will be disabled again?

If the AD CS service is disabled at a specific time or regularly, you can grab Process Monitor to see if it helps when the problem occurs.

1.Download and install Process Monitor tool on the machine here.  

https://learn.microsoft.com/en-us/sysinternals/downloads/procmon

2.Run Network Monitor as administrator.

3.Wait for the issue reproduces (remember/write the timestamp the issue reoccurs) and stop the trace after the AD CS is disabled.

4.Save the process monitor trace.

Note:  

As private information and security information may be involved, the forum does not collect log information. Please try to view the saved logs yourself (look for processes or applications that may disable the service based on the point in time when the problem occurred).

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
