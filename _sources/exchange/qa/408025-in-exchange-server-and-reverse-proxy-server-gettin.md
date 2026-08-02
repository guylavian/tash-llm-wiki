---
title: "In Exchange Server and Reverse Proxy Server, Getting 401 status with Null User Information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/408025/in-exchange-server-and-reverse-proxy-server-gettin
question_id: 408025
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# In Exchange Server and Reverse Proxy Server, Getting 401 status with Null User Information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/408025/in-exchange-server-and-reverse-proxy-server-gettin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Exchange server Hybrid Environment, we are getting 401  status with Null User for MAPI, EWS and Active Sync.    

D:\RPIISLog\Exmbx-dc-2\u_ex210523.log 831406 2021-05-23 06:44:09 10.96.64.101 NULL NULL EXMBX-DC-2 10.96.36.101 443 POST /EWS/Exchange.asmx &CorrelationID=<empty>;&cafeReqId=36f2e160-e8db-4b7e-a8ff-0255b433d25f; 401 0 0 NULL NULL 19 NULL NULL Microsoft+Office/16.0+(Windows+NT+6.2;+Microsoft+Outlook+16.0.4417;+Pro) OutlookSession="{6F1FF216-ADBC-449A-BF0D-DFBF373ECE29}" NULL NULL NULL NULL NULL NULL NULL NULL NULL    

D:\RPIISLog\Exmbx-dc-2\u_ex210523.log 831646 2021-05-23 06:44:13 10.96.64.100 NULL NULL EXMBX-DC-2 10.96.36.101 443 POST /EWS/Exchange.asmx &CorrelationID=<empty>;&cafeReqId=c6a4fd6f-1502-4195-9a6a-4a4cf7b9658d; 401 0 0 NULL NULL 30 NULL NULL Microsoft+Office/16.0+(Windows+NT+6.2;+Microsoft+Outlook+16.0.4266;+Pro) OutlookSession="{83BE22C9-1E53-46A8-993F-50B3F01C9795}" NULL NULL NULL NULL NULL NULL NULL NULL NULL    

D:\RPIISLog\Exmbx-dc-2\u_ex210523.log 831533 2021-05-23 06:44:12 10.21.26.51 NULL NULL EXMBX-DC-2 10.96.36.101 443 POST /mapi/emsmdb/ MailboxId=******@mydomain.com&CorrelationID=<empty>;&cafeReqId=39a29516-633d-48ff-b93f-9de29984dfec; 401 0 0 NULL NULL 9 NULL NULL Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.4549;+Pro) MapiContext=MAPIAAAAAOC49bfvwobF6Nn6yPjK+9bm0/7M/Nzt1e/c7dfj0oirmaCQpJKnl6KW9zIAAAAAAAA=;MapiRouting=UlVNOjVhOWFjMWU1LTM4ZTktNGY0Yy04OTFmLWYyNDFjODNhMzI5MzpiAs7xtR3ZCA==;MapiSequence=493-9Bw/Aw==;X-BackEndCookie=3142a0b8-351f-49e4-9067-08c5ddcc2bbc=u56Lnp2ejJqBxsfLmZuZz8vSzpnNzdLLy5uc0p7IxpzSm8aazs2ayZ3Lx5ucgYHNz83O0s/J0s3Nq8/JxcvLxc7O NULL NULL NULL NULL NULL NULL NULL NULL NULL    

D:\RPIISLog\Exmbx-dc-2\u_ex210523.log 831606 2021-05-23 06:44:13 10.21.92.109 NULL NULL EXMBX-DC-2 10.96.36.101 443 POST /autodiscover/autodiscover.xml &CorrelationID=<empty>;&cafeReqId=7dad860b-73c7-4d17-9ae0-417d6fdeb98a; 401 0 0 NULL NULL 53 NULL NULL Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.4954;+Pro) OutlookSession="{CD7A4BC8-E0AA-4B82-BBC6-AE4C48F55FB6}" NULL NULL NULL NULL NULL NULL NULL NULL NULL    

D:\RPIISLog\Exmbx-dc-2\u_ex210523.log 831646 2021-05-23 06:44:13 10.96.64.100 NULL NULL EXMBX-DC-2 10.96.36.101 443 POST /EWS/Exchange.asmx &CorrelationID=<empty>;&cafeReqId=c6a4fd6f-1502-4195-9a6a-4a4cf7b9658d; 401 0 0 NULL NULL 30 NULL NULL Microsoft+Office/16.0+(Windows+NT+6.2;+Microsoft+Outlook+16.0.4266;+Pro) OutlookSession="{83BE22C9-1E53-46A8-993F-50B3F01C9795}" NULL NULL NULL NULL NULL NULL NULL NULL NULL

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-25*

Hi @Nur Hossain  

Try enabling advanced logging in IIS and see if the usernames are logged. Also, could you please let us know the below,

1.What authentication is enabled on the virtual directories  

2.Are there any impact for the users like disconnection/not working/functionality not working, etc  

3.If you open the IIS log in notepad, does it show the cs-username or is it still NULL. This is just to isolate if there could be issues with loading the IIS log to the log parser studio

https://learn.microsoft.com/en-us/iis/extensions/advanced-logging-module/advanced-logging-for-iis-custom-logging#server_logging
