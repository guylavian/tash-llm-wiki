---
title: "Kerberos security error 4 in File servers cluster CAU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1000278/kerberos-security-error-4-in-file-servers-cluster
question_id: 1000278
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-high-availability-clustering-high-availability", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Kerberos security error 4 in File servers cluster CAU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1000278/kerberos-security-error-4-in-file-servers-cluster (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,    

Our file servers cluster are using the CAU to update patch. The cluster aware updating is working properly on both server. But we found a lot of Kerberos error in event log as below:    

ProviderName: Microsoft-Windows-Security-Kerberos    

TimeCreated          Id LevelDisplayName Message                                                                           

-----------    

          -- ---------------- -------                                                                         

9/8/2022 10:56:21 PM  4 Error            The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server          

                                         FS01$. The target name used was HTTP/CAUserver.abc.com. This       

                                         indicates that the target server failed to decrypt the ticket provided by the   

                                         client. This can occur when the target server principal name (SPN) is           

                                         registered on an account other than the account the target service is using.    

                                         Ensure that the target SPN is only registered on the account used by the        

                                         server. This error can also happen if the target service account password is    

                                         different than what is configured on the Kerberos Key Distribution Center for   

                                         that target service. Ensure that the service on the server and the KDC are      

                                         both configured to use the same password. If the server name is not fully       

                                         qualified, and the target domain (abc.com) is different from the       

                                         client domain (abc.com), check if there are identically named server   

                                         accounts in these two domains, or use the fully-qualified name to identify      

                                         the server.   

The SPN record HTTP/CAUserver.abc.com is not exist in AD    

We check the security channel between the server and DC is fine. And there are no duplication SPN and DNS record.    

Any idea?       

Best Regards    

Chong

## Answers

_No answers on this thread._
