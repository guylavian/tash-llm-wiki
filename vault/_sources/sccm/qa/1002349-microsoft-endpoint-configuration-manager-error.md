---
title: "Microsoft Endpoint configuration manager error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002349/microsoft-endpoint-configuration-manager-error
question_id: 1002349
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-application", "microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Endpoint configuration manager error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002349/microsoft-endpoint-configuration-manager-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi     

Please can somebody help me.    

I have a urgent issue which I have inherited from a member of staff who is no longer at the company.    

I am receiving 2 critical warnings in Microsoft Endpoint configuration manager in monitoring, component status    

SMS_DISTRIBUTION_MANAGER (Availability online)    

SMS_MP_CONTROL_MANAGER (Availability online)    

SMS_CLIENT_CONFIG_MANAGER (Availability online)    

On the server in event viewer I am also seeing these alerts     

The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server machinename. The target name used was cifs/machinename.domain.com. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (domainname.com) is different from the client domain (domainname.com), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.    

I think this maybe related to Kerberos?    

I found a article here but not sure what to do    

https://learn.microsoft.com/en-us/windows/win32/secauthn/key-distribution-center    

Can somebody advise on what I can do to fix this? or provide a guide?    

This issue is now causing problems with users trying to connect to the software center (Some users get a blank screen) Where do I change the password to match according to the error in the event viewer? what settings can I check to see mismatches? How do I fix this?    

I have checked the certificate store on the SCCM server and everything is there in the right place with the correct thumbprints so maybe it's just a case of updating something but i'm not sure?    

Windows version - WIndows server Hyper-V 2019    

Endpoint configuration manager version 2203 console version 5.2203.1063.1500 Site version 5.0.9078.1000    

Any help would be greatly appreciated    

Best regards Mr B

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-13*

Hi,    

About the Kerberos error, please check the Active Directory related logs and make sure the domain controllers are healthy. From Configuration Manager perspective, we can check the corresponding logs about the warning components:    

1,SMS_DistributionPoint represents a distribution point from which a given package has been distributed to clients. Can we find any useful information in distmgr.log?    

2,SMS_CLIENT_CONFIG_MANAGER is responsible for deploying the client agent to systems. We can check the ccm.log.    

3,About the SMS_MP_CONTROL_MANAGER, we can check if there is any error in the mpcontrol.log.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-11*

Hi,    

Can you check the DNS IP address of the server is unique and does not have a conflict in DNS, also check the SPN if it is setup correctly via this article. kerberos-event-4-access-denied    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
