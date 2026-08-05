---
title: "Whats using LDAPS, Check in event viewer."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228923/whats-using-ldaps-check-in-event-viewer
question_id: 228923
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Whats using LDAPS, Check in event viewer.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228923/whats-using-ldaps-check-in-event-viewer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

How do I know what is using LDAPS in event viewer, what clients are using LDAPS in my domain controller. Basically want to know the event id for LDAPS events in event viewer.  

By normally looking the event viewer I am not finding any events related to LDAPS.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

Hello,    

Thank you so much for your posting.    

According to my research, there is only one Event ID that is directly related to LDAP over SSL, which is Event 1220. For more information, we could refer to:    

https://social.technet.microsoft.com/wiki/contents/articles/2979.event-id-1220-ldap-over-ssl-ldaps.aspx    

There seems to be no event ID for LDAPS events in event viewer showing that what is using LDAPS based on my research. There are some events which are related to LDAP signing, such as Event 2887, 2888 and 2889.     

    

Reference:     

2020 LDAP channel binding and LDAP signing requirements for Windows    

https://support.microsoft.com/en-us/help/4520412/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows    

Have we enable LDAPS?     

LDAP over SSL/TLS (LDAPS) is automatically enabled when you install an Enterprise Root CA on a domain controller (although installing a CA on a domain controller is not a recommended practice).    

We could follow these steps to verify that LDAPS is enabled:     

-  On the client, start Ldp.exe     

For example:    

    

-  On the Connection menu, click Connect.     

-  Type the name of the LDAP server (e.g. domain controller or AD LDS/ADAM server) to which you want to connect.     

-  Type 636 as the port number.     

-  Click OK.     

Besides, there is no way to make clients prefer LDAPS because the type of connection depends on the application that is running on the client computer.    

Thanks so much.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
