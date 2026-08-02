---
title: "One of the server SYSVOL folder replication not happening properly?."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187573/one-of-the-server-sysvol-folder-replication-not-ha
question_id: 2187573
fetched: 2026-07-25
answer_count: 13
has_accepted_answer: false
upvotes: 4
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# One of the server SYSVOL folder replication not happening properly?.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187573/one-of-the-server-sysvol-folder-replication-not-ha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

We are facing an issue  in Replication, totally we have 15 servers, in that two servers SYSVOL folder replication not happening properly, but connectivty and  replication summary got success without an error, but while comparing the files from other server sysvol folder some are missin, we are not able to track issue, kindly please help us to identy the root cause for the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-14*

I am having the same issue but on mine the server that doesn't have the most updated SYSVOL data is our PDC DC3. Our DC4, DC6 and DC7 are fine. 

The error log I am getting is with Event ID 5002.

The DFS Replication service encountered an error communicating with partner DC4 for replication group Domain System Volume. 

Partner DNS address: DC4.PKEquipment.local 

Optional data if available: 

Partner WINS Address: DC4 

Partner IP Address: 10.77.132.42 

The service will retry the connection periodically. 

Additional Information: 

Error: 9036 (Paused for backup or restore) 

Connection ID: 4B8421FB-BC90-4F46-9CC4-4DD086A8D465 

Replication Group ID: E77A70C1-4989-4D6D-8D1E-9DFD7F604A43

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-10*

Hi Daisy Zhou,

Thanks for you reply 

I have checked with above mentioned commands in the PDC, all the three commands executed successfully, and there in no errors found.

The Type we are using here is DFSR for replication.

Here two of the server sysvol folders files are not get replicated, tried with service restart also. but no luck.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-09*

Hello S Siva1,  

Thank you for posting in Microsoft Community forum.  

Based on the description, you have 15 Domain Controllers, and the SYSVOL folder on two of the 15 Domain Controller do not sync with others, am I right?  

Also, you mean the AD replication between all DCs works fine. You can also confirm AD replication by running commands below on PDC.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

What is the SYSVOL replication type (FRS or DFSR)? Check method:

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
