---
title: "Active Directory LDAP replication errors and Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/59998/active-directory-ldap-replication-errors-and-excha
question_id: 59998
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory LDAP replication errors and Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/59998/active-directory-ldap-replication-errors-and-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm at a complete loss of what to do. I've been battling an unstable domain, which is affecting my company's Exchange Server. The first issue started last Friday when a coworker could not connect. Since then I've been through a number of tech websites and how-to's only to end up with no fix.  

One forest with two domains. First domain has three DCs, and where Exchange resides. The second domain was setup in 2016 after a merger. At the time it was easier to attach it to the existing forest.  

The PDC in the first domain appears to be the culprit. It's running 2003, and was in the process of being migrated to one of the 2012 R2 DCs.   

I can ping and run nslookup without error between all the DCs. I cannot get them to replicate. Last successful replication was on July 3. I cannot transfer or seize the FSMO to the 2012 R2 DC from the PDC.  

I've run dcdiag, netdom (query fsmo, and resetpwd), and repadmin commands. Everything appears to point back to LDAP issue(s), or the target principal name is incorrect, or that RPC is not running on any of the DCs.  

I can supply reports for anyone willing to help.  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-06*

Hello,  

Thank you so much for posting here.  

According to our description, we have 2 domains in one forest. First domain has 3 DCs. There are some issues with the 3 DCs now. Before going further, we would like to configure out all the detailed error messages and then check how to solve the issues.   

Please run the below commands:   

-  We should check if all DCs work fine by running Dcdiag /v on every DC.  

-  And check if AD replication is working properly by running repadmin /showrepl and repadmin /replsum on every DC.  

-  Run repadmin /showrepl * /csv >C:\showrepl.csv on one of the DCs.  

Please kindly check the reports and tell us the specific error messages. For any question, please feel free to contact us.  

Best regards,  

Hannah Xiong
