---
title: "Domain controller certificate renewal issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2236195/domain-controller-certificate-renewal-issue
question_id: 2236195
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controller certificate renewal issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2236195/domain-controller-certificate-renewal-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   Domain controller certificate auto renewal is not happening. I'm using Microsoft CA server and have to manually renew the certificates in the domain controller. Is there anyway to automatically renew this certificate without manual intervention?  Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-19*

Hello VIGNESHWARAN M,  

Thank you for posting in Q&A forum. 

Is there anyway to automatically renew this certificate without manual intervention? 

A: Yes, you automatically renew this certificate without manual intervention, please set two steps to automatically renew Domain Controller certificate.

Step 1

Configure "Read and Enroll and Autoenroll" permissions on the specific Domain Controller Certificate Template you configured.

Issue this certificate tempalte.

Step 2

Set Auto-Enrollment policy and apply it to Domain Controllers.

1.Open Group Policy Management, edit the Default Domain Controller Policy (or create a new GPO and link this new GPO to Domain Controllers OU and edit this new GPO).

2.Navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Public Key Policies. Here you will see Certificates Services Client – Auto-Enrollment policy.

3.Open its properties and choose Enabled on the Configuration Model box, then check the boxes Renew expired certificates, update pending certificates, and remove revoked certificates and Update certificates that use certificate templates. Click OK when you are done. As you can see this policy will automatically renew any expired certificates and also cleans up the certificates store of any certificates that expired.

At last, run gpupdte /force on Domain Controller or wait for the group policy to refresh in the background (by default it refreshes every five minutes on DC).

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
