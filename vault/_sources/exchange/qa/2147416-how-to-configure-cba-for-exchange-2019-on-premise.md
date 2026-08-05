---
title: "How to Configure CBA for exchange 2019 on premise??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2147416/how-to-configure-cba-for-exchange-2019-on-premise
question_id: 2147416
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How to Configure CBA for exchange 2019 on premise??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2147416/how-to-configure-cba-for-exchange-2019-on-premise (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

I was setting up CBA for active sync and owa on exchange on premise 2019 following this guide https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-certificate-based-auth?view=exchserver-2019 on my test environment.

Everything went smoothly, but when I Check OWA or ActiveSync virtual directory to require client certificate and connect through browser and prompt to choose user certificate I get error 403 "You don't have the user rights to view this page." Without virtual directory set to requiring client certificate everything works great.

Here is log of 403 in IIS: 2025-01-15 09:15:24 ::1 GET /OWA/auth.owa &encoding=; 443 - ::1 AMProbe/Local/ClientAccess - 403 7 5 19.

For CA I am using AD CA installed on domain controller, and for certificates issuance to user I use copy of user template and autoenrollment. User certificate picture is attached.

Server certificate is generated on offline Linux server CA, and this CA is trusted on domain. I really have no idea what else to do to make CBA work, maybe somebody can give some more suggestions??? certif.PNG

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-20*

Hi @Evald Gruzdev ,

Based on your description, you managed to get OWA to work with certificates on both the PC and iPhone. For ActiveSync issues, here are some additional suggestions that may help you resolve 403 errors:

-  Make sure the client certificate is correctly mapped to the user account in Active Directory. The certificate must contain the User Principal Name (UPN) in the Subject or Subject Alternative Name field.

-  Double-check the IIS settings for the ActiveSync virtual directory. Make sure SSL is enabled and that the Client Certificate Mapping authentication feature is properly installed and configured.

-  Verify that the iPhone trusts the entire chain of trust for the client certificate, including the root certificate and any intermediate CAs.

-  Check if there are any ActiveSync mailbox policies that may be causing this issue. Sometimes, specific policies can interfere with certificate-based authentication.

-  Make sure the Autodiscover service is correctly configured and available for ActiveSync. This service helps the device locate the Exchange server and configure connection settings3.

-  Since you mentioned that Edge may have cached data that caused the problem, you can try clearing the browser cache and cookies again, or resetting the Edge settings to default. Alternatively, testing with a different browser can help isolate the issue.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-16*

Hi @Evald Gruzdev  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you have completed many settings correctly, but the 403 error indicates that there may be a problem with the client certificate authentication configuration. There are several things you can check and try:

-  Make sure that the client certificate is correctly mapped to the user account in Active Directory. The certificate must contain the User Principal Name (UPN) in the Subject or Subject Alternative Name field.

-  Verify that all servers and devices involved in accessing OWA and ActiveSync trust the entire trust chain of the client certificate, including the root certificate and any intermediate CAs.

-  Double-check the IIS settings for the OWA and ActiveSync virtual directories. Make sure SSL is enabled and that the Client Certificate Mapping authentication feature is correctly installed and configured.

-  Make sure that the user account has the required permissions to access the OWA and ActiveSync virtual directories. Sometimes, certificate-based authentication may require specific permissions.

-  Make sure that the client certificate is valid and has not expired. In addition, check that the certificate is correctly issued for client authentication.

Refer to: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-certificate-based-auth?view=exchserver-2019

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-15*

Could be a cert trust issue:

https://stackoverflow.com/questions/26247462/http-error-403-16-client-certificate-trust-issue
