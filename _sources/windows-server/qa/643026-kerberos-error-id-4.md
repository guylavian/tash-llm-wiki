---
title: "Kerberos error id 4"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/643026/kerberos-error-id-4
question_id: 643026
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Kerberos error id 4

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/643026/kerberos-error-id-4 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,    

May I kindly ask you for help?     

I'm trying to resolve below Kerberos error:    

    

-  Please correct me if I'm worng but probably some user or application is trying to get access from my server(my_server) to share on remote server1, right?    

This application or user use DNS share alias (there is DNS alias added - share) and not SPN is added for this remote server1.    

Now to resolve this issue I need to add SPN for server1, correct?    

-  How can I check which user or application is trying to get access to this share from my server for example my_server?    

Regards,    

Sebastian

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-09*

Correct.  

KRB_AP_ERR_MODIFIED is most of the time caused by a SPN that is not set on the correct AD Account.  

From your DC or any Windows 2016+, you can run the following command:  

setspn -Q CIFS/Share  

setspn -Q CIFS/Share.yourdomain.com  

This will query your AD Database to see if this SPN exist and on which account it is currently set.  

Please note that CIFS/Share may not be set and it is not required because the SPN HOST/Share also work for this.  

To add the CIFS/Share SPN on the Server1 account, run the following command:  

setspn -S CIFS/share Server1  

setspn -S CIFS/share.yourdomain.com Server1  

The reason why i suggest you to add the FDQN as well as the short name is because you don't know how the client could connect to your server.  

hth
