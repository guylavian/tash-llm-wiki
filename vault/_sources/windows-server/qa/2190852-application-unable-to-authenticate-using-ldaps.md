---
title: "Application unable to authenticate using LDAPS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190852/application-unable-to-authenticate-using-ldaps
question_id: 2190852
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Application unable to authenticate using LDAPS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190852/application-unable-to-authenticate-using-ldaps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 4 Domain controllers with Windows server 2012R2 deployed in our environment which are servicing LDAP Secure authentication. We have VIP on our Loadbalancer created for these DCs and external SSL certificate is deployed.

We have an issue where one application using the LDAPS VIP is unable to authenticate to AD. No detailed logs are available on the application side.

Other apps using the same VIP are able to authenticate fine.

What could be the possible cause for this? the certificates are valid and will expire next year.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-06*

Hello Sweta Prasad,  

Thank you for your reply.  

  ****Does the authentication within "Other apps using the same VIP are able to authenticate fine." using domain user name and password?  

Can you check any security logs on DC if Other apps using the same VIP are able to authenticate fine.  

You can try to check if there is any event ID 4771 (Kerberos authentication) or 4776 (NTLM authentication) or 4525 (logon success) or 4624 (logon failure) related to application authentication on DC.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Hi Daisy,

Thanks for the response. refer below details:

If the issue occurs the first time? And only this time during all the time? - This is the first time. Issue hasn't resurfaced since then.  

If it is the first time and only this time it occurs, we can keep monitoring later. - Any specific logs we can enable or capture to identify the problem?  

Or if the issue occurs often or more than one time, and the issue can not resolve by restarting Domain Controller. Maybe we need to check something or troubleshoot it.  

If it only appears this time, and it will not appear in the future, I think it may have something to do with the unstable network, or for some reason it cannot contact DC at that moment. - Is there anything else we can check in future to better identify what might have caused this?

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-12*

Hello Sweta Prasad,  

Thank you for your reply.  

If the issue occurs the first time? And only this time during all the time?  

If it is the first time and only this time it occurs, we can keep monitoring later.  

Or if the issue occurs often or more than one time, and the issue can not resolve by restarting Domain Controller. Maybe we need to check something or troubleshoot it.  

If it only appears this time, and it will not appear in the future, I think it may have something to do with the unstable network, or for some reason it cannot contact DC at that moment.

Here is a third-part thread may be related to the "error message" but not the same issue (similar issue) for your reference.  

operating system - sgslufread: Hard error on read, OS error = 104 Linux - Stack Overflow  

Hope the information above is helpful.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-11*

Hi Daisy,

Please refer below details:

Thank you for posting in Microsoft Community forum.  

1.Based on the description "We have an issue where one application using the LDAPS VIP is unable to authenticate to AD.", what error message did you see when the LDAPS VIP is unable to authenticate to AD? - <<username>>: Hard error on read, OS error = 104  

2.What application did you use? Microsoft application or non-Microsoft application? - Non-Microsoft  

3.Can this application be authenticated properly before? If so, did the issue come up suddenly? Or is it a newly deployed application with LDAPS VIP that cannot be authenticated? - Yes, it was authenticating properly earlier. We rebooted the DCs which restored authentication as part of troubleshooting.  

4.Did you install external SSL certificate on all the Domain Controllers? - Only 4 Domains controllers are being used behind the VIP for LDAPS. Certificate is installed on all 4 DCs  

5.Where did you install certificate on Domain Controllers? - Both locations  

Certificates- Local Computer  

Personal container  

OR  

Certificates - Service (Active Directory Domain Services) on Local Computer  

NTDS\Personal container

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-08*

Hello Sweta Prasad,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description "We have an issue where one application using the LDAPS VIP is unable to authenticate to AD.", what error message did you see when the LDAPS VIP is unable to authenticate to AD?  

2.What application did you use? Microsoft application or non-Microsoft application?  

3.Can this application be authenticated properly before? If so, did the issue come up suddenly? Or is it a newly deployed application with LDAPS VIP that cannot be authenticated?  

4.Did you install external SSL certificate on all the Domain Controllers?   

5.Where did you install certificate on Domain Controllers?  

Certificates- Local Computer  

Personal container  

OR  

Certificates - Service (Active Directory Domain Services) on Local Computer  

NTDS\Personal container  

  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
