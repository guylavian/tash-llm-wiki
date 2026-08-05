---
title: "DFS using NTLM instead of Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/734043/dfs-using-ntlm-instead-of-kerberos
question_id: 734043
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# DFS using NTLM instead of Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/734043/dfs-using-ntlm-instead-of-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I try to access the DFS shres, i can see that events logged into Microsoft/NTML even logs. It means it is using ntlm protocol. 1 or 2 i dont know.  

How do i make sure that clients use kerberos rather than NTLM protocols when accessing DFS.?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-02-15*

Hi

I'm assuming that you are using DFS-N and you have created a Domain namespace and the target folder which is pointing to NetApp share. You have a namespace something like \domain\<share>\<netapp share>

For Kerberos to be used you will need an SPN entry for namespace server. You will also need an SPN for the NetApp based on the Path defined in the Folder Target. Here is an example based on the DFS-N in my test environment, which is \w2k12.local\sharefolder\sales.

For the namespace server, there should be an SPN for the server i.e. host/w2k19.w2k12.local

In this example, the NetApp would be member19.

The NetApp computer object needs to have an SPN of host/member19.w2k12.local

You can use setspn /q host/member19.w2k12.local to confirm that the SPN exists

You need to search for the host and not cifs, as host is used represent a number of service names including cifs and will not exist as an entry.

When using the klist command to clear existing tickets, klist can still show no tickets after connecting to the share again, as a session connection could still be open and reauthentication and a new ticket request is not required to read the share.

Gary.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-02-14*

Hello @Anonymous       

I would recommend to try to generate again the Kerberos ticket. It is possible that a bad cached ticket will force to fallback into NTLM authentication for SMB share.     

-  Open command prompt    

-  type: klist purge    

-  Access to your remote server using Windows Explorer (\servername\share)    

-  In the command prompt, type the following command: klist    

-  You should see the Kerberos tickets that has been cached    

Hope this helps with your query,    

--------    

--If the reply is helpful, please Upvote and Accept as answer--
