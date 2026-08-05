---
title: "double hop passing NT\\ANNONYMOUS with NTLM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/258980/double-hop-passing-ntannonymous-with-ntlm
question_id: 258980
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# double hop passing NT\ANNONYMOUS with NTLM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/258980/double-hop-passing-ntannonymous-with-ntlm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am having issues with both Bulk Load and SSIS packages that are trying to read\write\move files from\to a file server when a double hop is involved. We are not using Kerberos but using NTLM.  

The double hop causes the host login credentials to not get passed correctly so the NT\ANNONYMOUS login is passed instead.   

I do not have a problem if I run the bulk load script or SSIS package from the server hosting the SQL instance but if I try to call these from SSMS or application, not residing on the server hosting the SQL instance I get the dreaded double hop switch in credentials.   

I opened up a ticket with MS support and was told, at least for Bulk Load, that Kerberos had to be used to get the credentials properly sent to the file server. It also seems to be true for SSIS packages. I have set up a proxy account to call the SSIS package, via a SQL Job, and I'm still seeing the access denied error for the files on the file server.  

Is there a work around for NTLM, to pass the correct credentials, when a double hop is initiated?  

Thanks in advance  

Doug T

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-05*

Daisy,  

Thanks for your reply.  

Yes, we have a domain\Windows AD Account that is running an application, outside of the server hosting the SQL Instance. The app, using the domain AD Login is either connecting to the SQL server to get data and then creating a file, on a domain file server or trying to bulk load data, from a file on the domain file server. Either way, unless the application is running directly from the server, hosting the SQL instance, it will fail with a permissions error, from the domain file server, that the login does not have file access. NTLM is not passing the domain\Windows AD login, which has permissions, but instead passing the NT\ANNONYMOUS login, because of the double hop

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-05*

Hello @Douglas Tanner  ,    

Thank you for posting here.    

Based on the description, do i understand your question correctly?    

Assume we have AD domain, domain client1, domain server1 and domain server2, domain user1.    

Assume domain user1 logs on domain client1 and accesses resources on domain server1, you want to domain server1 can use domain user1 credential on domain client1 to access resources on domain server2 (using NTLM authentication), is it right?    

If anything I misunderstood, please correct me.    

Thank you for your understanding.    

Best Regards,    

Daisy Zhou
