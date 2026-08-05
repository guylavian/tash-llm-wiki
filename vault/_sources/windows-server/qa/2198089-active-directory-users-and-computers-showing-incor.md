---
title: "Active Directory Users and Computers Showing incorrect Mapping"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198089/active-directory-users-and-computers-showing-incor
question_id: 2198089
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory Users and Computers Showing incorrect Mapping

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198089/active-directory-users-and-computers-showing-incor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Geeks,

I recently updated the AD Schema for Exchange 2019, but since the upgrade, the AD Users and Computers are displaying incorrect mappings for several columns, as shown in the picture below. For example, the Email Address is now showing as Mailnickname, the Job Title is appearing as UPN, and many other fields have similar mapping issues.

I’ve tried the following steps, and everything seems to be fine:

-  The AD Schema under the ADSI tool shows the correct mappings.

-  PowerShell retrieves the correct information.

-  LDAP and saved LDAP queries display the correct data.

-  The Attribute Editor also shows the correct information.

-  The Active Directory Administrative Center is showing the correct details.

We have multiple domain controllers across our network (connected through VPN), and the same issue is occurring on all of them. I’ve also tried installing RSAT on different servers and on Windows 10/11, but the issue persists.

I’ve attempted deleting the XML and opening DSA in MMC snap-ins, but nothing seems to work.   

Can anyone please help resolve this issue?

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-27*

Hello  

Greetings!  

I have set Title attribute on both users TestA and TestB, how can I check these column name with Job Title? Advanced?

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-24*

Hello Daisy,

Thank you for your quick response.

-  I have already checked all these commands during my troubleshooting, and there are no errors. Replication is occurring every 30 to 60 minutes, depending on business requirements:

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

-  The screenshot is taken from one of the affected DCs. I created these demo users for reference.

-  The "Job Title" is displayed as the column name, while the attribute name is Title.

All attributes show the correct values when verified through PowerShell, the Attribute Editor, LDAP, or any third-party tool.  

Kind Regards,  

Irfan

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-24*

Hello Muhammad-Irfan，  

Thank you for posting in Microsoft Community forum.

1.Please check AD replication in the entire forest. Run commands below on PDC.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

2.How and where did you get the screenshot above?

3.I do not find Job Title attribute of the domain users (User Properties\Attribute Editor tab) on Domain Controller in my lab.

You can try to check the attribute value of Job Title on these domain users, if the attribute values of Job Title corresponding to these domain users are correct.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
