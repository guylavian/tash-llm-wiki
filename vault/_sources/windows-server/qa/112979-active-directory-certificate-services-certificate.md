---
title: "Active Directory Certificate Services - Certificate enrollment process is stuck in MMC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112979/active-directory-certificate-services-certificate
question_id: 112979
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Certificate Services - Certificate enrollment process is stuck in MMC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112979/active-directory-certificate-services-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning all,  

When I request a certificate at my enterprise CA using MMC, the enrollment process keeps getting stuck at the progress bar shown in the picture below.  

  

I checked that the service is running and event logs show no warnigs/errors (neither on the CA nor in CAPI2 logs on the client computer) for enrollment for affected users. I verified, that the CA is available via certutil -ping -config and all green on PKIVIEW. I noticed, that this behaviour does not occur all the time but noticably often.  

I also checkd the solution attempt from https://community.spiceworks.com/topic/2168954-user-is-stuck-in-certificate-enrollment, but the permissions are absolutely correct (as sometimes the enrollment works and sometimes not) and restarting CertSrv service each time this happens is not a feasable solution to me.  

Does anyone have an idea about the cause of the issue or suggestions, where I could do additional research?  

Thank you in advance.  

Kind regards,  

Chris

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-13*

Hello,    

Thank you so much for your kindly reply.    

Since this issue is a little weird, it might be hard to find the root issue here. I will continue to search for this issue. If it is urgent, I would suggest you contact Microsoft Customer Services and Support to get an efficient solution:    

https://support.microsoft.com/en-in/hub/4343728/support-for-business    

As for the error 1053, here is the discussion. We could kindly have a check whether it helps.     

https://social.technet.microsoft.com/Forums/en-US/b146cc3b-09b1-48cc-b756-377369cc856b/error-1053-the-server-did-not-respond-to-the-start-or-control-request-in-a-timely-fashion?forum=win10itprohardware    

Besides, we would like to share with you the information about How to troubleshoot Certificate Enrollment in the MMC Certificate Snap-in. The discussion here might not be suitable for our issue. But we could kindly have a check whether it could give us some insights.     

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/how-to-troubleshoot-certificate-enrollment-in-the-mmc/ba-p/394973    

Thank you so much for your understanding and support.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-12*

Anyone else having ideas ore recommendations?  

We are still facing this issue from time to time.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-05*

Hi all,  

I madre some further tests today. I enrolled for a certificate and the issue occured again. I restarted the AD CS service while keeping the enrollment window open. The restart operation failed with error 1053 (example image below, because I took no screenshot myself). Starting the service worked properly and the client recognized the RPC server of the CA not being available anymore.  

I retried the enrollment immediately after and it finished without an issue. Therefore I assume the issue is related to a stuck/overloaded certificate service.  

Any idea to dig deeper into this service and find the root issue?  

Kind regards,  

Christopher Ehrit

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-01*

Hello Hannah,  

It seems that restarting the services solves the issue temporarily, but it is hard to proof as the issue occurs so randomly.   

The second solution attempt in the link you sent, is not really applicable to me, and I'll explain why.  

After more investigation I noticed, that the certificate requests do indeed arrive in the pending requests view in the certification authority. They can be issued and the certificate can be exported properly, but on the client computer, I realized that the original request containing the private key is not listed in the Certificate Enrollment Requests in MMC. So I am not able to use the certificate with the private key on the requesting machine/user.  

I guess this is a consequence of the enrollment process not finalizing properly.  

Best regards,  

Chris

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Hello Chris,    

Thank you so much for posting here.    

According to our description, this behavior does not occur all the time but often.  Sometimes it works but sometimes not. Restarting CertSrv server could solve the issue, right? But it is not a feasible solution to us. We would like to figure out the cause of this issue.     

As per my understanding, it is a little hard to figure it out since it is not continuous behavior. Here is the discussion about this similar case, and we could kindly have a check whether it helps.    

https://social.technet.microsoft.com/Forums/ie/en-US/c29b8541-5563-451f-8d26-afce06689df8/pki-certificate-request-stuck-in-certificate-enrollment-requests?forum=winserversecurity    

For any question, please contact us. Thanks.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
