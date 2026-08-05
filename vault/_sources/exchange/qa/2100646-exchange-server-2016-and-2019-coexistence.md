---
title: "Exchange server 2016 and 2019 coexistence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2100646/exchange-server-2016-and-2019-coexistence
question_id: 2100646
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange server 2016 and 2019 coexistence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2100646/exchange-server-2016-and-2019-coexistence (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 2016 and 2019 servers both on premises.  

if we create and account which resides on database on 2019 authorization issues happen

like you open OWA properly login and no error message just login does not happen.

if you misspel password red message appears.  

So far we see only when account resides on 2019 database.  

total 3 servers, 1 CU 20 2016, 2 CU 23 2016 and 3 CU 14 2019  

1 and 2 have DAG

3 has no DAG as it is not allowed to DAG 2016 and 2019

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-10*

Hi @George Gaprindashvili  ,

Welcome to the Microsoft Q&A platform!

 

Based on your description, it looks like you are experiencing OWA authentication issues when the user account is in the database of an Exchange 2019 server. Here are a few steps you can take to troubleshoot and potentially resolve this issue:

 

-  Look for any relevant errors in Event Viewer on the Exchange 2019 server. This can provide more insight into the issue that is occurring during the logon process.

 

-  Since you are using a hybrid of Exchange 2016 and 2019 servers, make sure that Kerberos authentication is configured correctly. Misconfiguration can cause authentication issues.

 

-  Verify that the OWA virtual directory URL on the Exchange 2019 server is configured correctly. Mismatched URLs can cause redirection issues.

 

-  Compare the authentication settings for the OWA virtual directory on the Exchange 2019 server with the authentication settings on the Exchange 2016 server. They should be consistent on all servers.

 

-  Make sure that the SCP for the Exchange 2019 server is configured correctly. The client uses the SCP to locate the Autodiscover service.

 

-  Make sure the DNS records for your Exchange environment are configured correctly. Incorrect DNS settings can cause clients to connect to the wrong server.

 

-  If you use a load balancer, check the configuration to make sure traffic is being directed correctly to the Exchange 2019 server.

 

-  Make sure the SSL certificate on the Exchange 2019 server is valid and matches the name the client is using to connect.

 

-  Make sure your Exchange 2019 server is updated with the latest cumulative updates and security patches.

 

-  Sometimes browser-specific issues can cause problems with OWA. Test the sign-in process with different browsers to rule this out.

 

Because this issue does not occur when explicitly using the address of the Exchange 2019 server, this indicates that the issue may be related to how the request is routed or authenticated when it passes through the Exchange 2016 server. By following the steps above, you should be able to narrow down the cause of the issue and find a solution.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
