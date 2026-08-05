---
title: "ADCS: Key Recovery Agent template - Changes and Renewal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/77850/adcs-key-recovery-agent-template-changes-and-renew
question_id: 77850
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADCS: Key Recovery Agent template - Changes and Renewal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/77850/adcs-key-recovery-agent-template-changes-and-renew (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Configuring KRA template for auto cert enrollment is pretty straightforward. However I can't find any info on steps how to :

1) Renew it- once is about to expire. Renew with same key or new? Why?  

2)What if you do changes to the template over the course of time. What needs to be updated? Steps?

References:  

https://download.microsoft.com/download/0/2/c/02c2ca18-1ed8-414c-b883-1753cd2a8b63/KeyArchivalandManagementinLonghornBeta3_pub.doc  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755395(v=ws.10)?redirectedfrom=MSDN  

https://social.technet.microsoft.com/wiki/contents/articles/7573.active-directory-certificate-services-pki-key-archival-and-management.aspx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-31*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-08-26*

There are lots of issues with straightforward way. Every KRA certificate renewal, replacement reduces chances to successfully decrypted key, because you need to find exact KRA cert that is capable to do this, not all are capable. You increase KRA management costs and reduce flexibility for nothing. I have quite long experience (10yrs) with this and what I expressed is fairly solid solution: you have minimum KRA certs, every is capable to recover every key.

Renew it- once is about to expire. Renew with same key or new? Why?

doesn't much matter which one you choose, because you have to update KRA list on CA in all cases.

What if you do changes to the template over the course of time.

I can't imagine what you would change in KRA certificate. If something still requires to be changed, then follow standard enrollment and KRA configuration on CA server procedure. However, as said I'm against this route, I wouldn't consider it good enough.

BTW, same practice I use for EFS recovery, when it is used.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-26*

@Vadims Podāns   Thank you. What if I have to this regular/ painful way? Any suggested steps?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-08-26*

I ended up without using certificate template for KRA. Instead, I would suggest to:  

generate a long-lived self-signed certificate for key recovery. Make it valid long enough (for example, 5-10 years) add it to Trusted Root CAs store on CA servers. Backup KRA certificate and keys to removable media (make multiple copies) and store them in different secure locations. Then configure CA servers to use this self-signed KRA certificate in KRA tab.  

Any other strategy is very fragile in long-term when you need to recover very old key.
