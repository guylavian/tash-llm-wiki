---
title: "AD CS vulnerabilities certificate services, Authentication users permission revoke issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1511236/ad-cs-vulnerabilities-certificate-services-authent
question_id: 1511236
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD CS vulnerabilities certificate services, Authentication users permission revoke issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1511236/ad-cs-vulnerabilities-certificate-services-authent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys,
Ad CS vulnerabilities.
IntuneClientCertificate -> ESC1:  

"Domain Users" can enroll with the CA and specify the "Subject Alternative Name". Therefore, a user can request a client authenticate certificate, specifying a DA as the SAN, and have a certificate to impersonate the DA using the certificate for authentication.
ClientCMGCert -> ESC4:  

"Authenticated Users" have full write permission over this certificate, and therefore, can modify ClientCMGCert to become vulnerable to ESC1 as above.

To Fix this can I go ahead and Edit the authenticated USers' permissions I..e., can I revoke the Authenticated user's (Enroll/Write).
If I do that will there will be any production issues?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-01-26*

Hello Bharath Kotha,

Thank you for posting in Q&A forum.  

"Authenticated Users" have full write permission over this certificate, and therefore, can modify ClientCMGCert to become vulnerable to ESC1 as above.
A: Did you mean "Authenticated Users" have full write permission over this certificate template not certificate? If so, you can only give the "Authenticated Users" read and enroll permissions on the certificate template.
If I do that will there will be any production issues?  

A: I think there is no impact, because the permission on certificate template means who have specific permissions on this certificate template. It will not impact the function of this certificate.
For example:

If you want to modify these permissions, please ensure that you have sufficient permissions.
Before this, you had better back up the certificate authority database and configuration files if there is no such recent back up.
Note: But before revoking the authorization of authenticated users, please make sure to conduct testing to ensure that there are no production issues. You need to test according to the specific situation and make modifications carefully.
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
