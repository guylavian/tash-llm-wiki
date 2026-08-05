---
title: "Active Directory Replication authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401393/active-directory-replication-authentication
question_id: 401393
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory Replication authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401393/active-directory-replication-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our Network admin resigned, when I try to disable his admin account active directory replication fails.   

I cannot find how to change what account AD replication is using.   

Paul

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-20*

Please provide the files I mentioned above.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-20*

DaisyZhou-MSFT   

-  we have single forest and single domain environment.   

-  There are 2 DC  

-  To clarify a bit more, we us PRTG to monitor our environment. When I inactivate the old users Domain admin account, PRTG flags "Active Directory Replication Errors" Message "The RPC server is unavailable". Once you enable the account PRTG clears the error. With the account inactive I notice AD is still replicating new users account across the two DC, as will any changes to the sysvol folder we the user bat files are kept.   

-  The account in question is a member of the Domain administrator group.   

-  There are now errors in the logs when the account is inactive.   

I am wondering if this is a PRTG issue and not AD. RDP service is still running after the account is inactive, and seems AD Replication is still functioning.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-20*

Hello @Paul Lapierre  ,

Thank you for posting here.

To better understand your question, please confirm the following information at your convenience.

1.Is your AD forest single forest and single domain environment or single forest and multiple domains environment?

2.If your AD forest is single forest and multiple domains environment. How many domains are there in your AD forest?

For example:  

3.How many DCs are there in each domain? Please run nltest /dclist:domain.com to check.

4.Based on the description "when I try to disable his admin account active directory replication fails.", do you mean enable his admin account active directory replication works fine?

5.Is your account a domain administrator account or a member of the domain administrator group?

Please check AD replication status before disabling his admin account and after disabling his admin account, run the following commands on PDC to check.

repadmin /syncall /AdeP C:\rep1.txt

repadmin /showrepl C:\rep2.txt

repadmin /replsum C:\rep3.txt

repadmin /showrepl * /csv >c:\repsum.csv

Tip: Please do not upload these log files, because private information may be involved. If you confirm that the command result has error information, please provide us with part of the error code and error information (if private information is involved, please obfuscate).

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-19*

Do you have any more details? Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
