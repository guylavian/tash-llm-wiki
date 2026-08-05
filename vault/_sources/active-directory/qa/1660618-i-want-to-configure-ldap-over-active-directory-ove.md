---
title: "I want to configure LDAP over Active directory, over internet, but its not accessible"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1660618/i-want-to-configure-ldap-over-active-directory-ove
question_id: 1660618
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# I want to configure LDAP over Active directory, over internet, but its not accessible

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1660618/i-want-to-configure-ldap-over-active-directory-ove (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I reffered the provided Documvslientation

-  Created Extra ID

-  Created USer wit ADmin Group

-  Created and configured Azure AD domain Service

-  Enabled Secure LDAP with SSL self certificate.

-  Allow port 636 for over inrternet access

-  Port is also enabled but when we checking LDAP service its not running.\

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-30*

Hello,

Based on your description, if you have completed the above steps to configure the Microsoft Entra domain service to support secure LDAP, and also confirmed that port 636 has been opened to allow access through the Internet, but found that the LDAP service is not running, this may be caused by several Caused by:

-  Service status check: First, make sure that the running status of the Microsoft Entra domain service itself is normal. Sign in to the Azure portal to view the health status of your managed domain and any possible alerts. Verify there are no service outages or maintenance ongoing.

-  Network configuration: Although you mentioned that the port is enabled, you also need to check the Network Security Group (NSG) rules and firewall settings to ensure that inbound traffic to port 636 is not only open on the local server, but also on the entire network path. allow.

-  SSL certificate issue: Although you enable secure LDAP with a self-signed certificate, sometimes improper certificate configuration may cause the service to fail to start. Verify that the certificate is correctly bound to the LDAP service and is not expired or corrupted.

-  DNS resolution: Verify that external clients can correctly resolve your LDAP service’s FQDN to the correct IP address. Incorrect DNS configuration may prevent clients from connecting.

-  Service restart: Sometimes, even if everything seems to be configured correctly, the service may need to be restarted for the changes to take effect. Try restarting the Microsoft Entra Domain Services related services or the managed domain controller to see if that resolves the issue.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-26*

Entra Domain Services doesn't support exposing LDAP services to the internet

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
