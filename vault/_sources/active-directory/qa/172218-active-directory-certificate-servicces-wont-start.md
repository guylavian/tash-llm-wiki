---
title: "Active Directory Certificate Servicces wont start Win2019 Core"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/172218/active-directory-certificate-servicces-wont-start
question_id: 172218
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Certificate Servicces wont start Win2019 Core

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/172218/active-directory-certificate-servicces-wont-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

Hoping someone can help me as I am puzzled.   

I currently am building a Sub-CA , I received the signed cert from the Offline root, installed it on the Sub CA and verified it can talk to the keys on the HSM. This all checks out.   

However when I go to start ADCS via the Certification Authority Snap in - I get the following message - "The System cannot find the file specified. 0x2 (WIN32: 2 ERROR_FILE_NOT_FOUND)" " The policy module for the CA is missing or incorrectly registered. To view or change the policy module settings, right-click on the CA, click Properties, and then click the Policy Module tab"  

I do as the above asks me and it shows the Standard Windows 10 policy module loaded.   

I then check the event viewer, and notice this message everytime I try start ADCS I see the following message   

"<CA NAME>   

The system cannot find the file specified. 0x80070002 (WIN32: Error_File_Not_Found)  

The handle is invalid"  

Can someone please help me with this as I am stuck.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-24*

Hi,  

I am glad to hear that your issue was successfully resolved\I am pleased to know that the information is helpful to you. If there is anything else we can do for you, please feel free to post in the forum.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-23*

@Vadims Podāns   Any idea?     

How can I verify where exactly the CA is looking for that file?
