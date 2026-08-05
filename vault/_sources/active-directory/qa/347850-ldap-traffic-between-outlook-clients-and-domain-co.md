---
title: "LDAP traffic between Outlook clients and domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/347850/ldap-traffic-between-outlook-clients-and-domain-co
question_id: 347850
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAP traffic between Outlook clients and domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/347850/ldap-traffic-between-outlook-clients-and-domain-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm trying to figure out the reason for some LDAP traffic between our root and subdomains. Using Process Monitor I was able to find out that Oultook.exe is connecting to every domain controller from every subdomain using LDAP. Please see the screenshot I attached.    

Basically we have some Terminal servers running in the root Domain and Users connecting to them. Our users mailboxes are running on Office 365 and we have several instances of Azure AD Sync which sync our users to multiple O365 tenants.    

    

After blocking LDAP between our root and subdomains, everything still seems to work fine. But I wanted to find out why Outlook is trying to connect to other subdomain controllers?    

Do you have any idea?    

Regards,    

Philipp

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-22*

Hello Daisy,  

sorry for my late reply.  

Yes, I'm aware that it's possible to manually configure LDAP servers as an additional Adress Book. I also checked and non of our users enabled this feature.  

But we still see LDAP traffic coming from Outlook.exe, trying to reach all Domain Controllers from all subdomains.  

Regards,  

Philipp

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-04-08*

Hello @Philipp Mair  ,    

Thank you for posting here.    

I asked the engineer from outlook team, they told me we can see LDAP information of outlook below.    

    

Internet directory services, also known as LDAP services, are used to find e-mail addresses that are not in your local Outlook contacts. Directory services search directories on other servers to look up names and other information that can then be viewed in Outlook. You can locate an LDAP server on the Internet, on your organization's intranet, or through another company that hosts an LDAP server.    

For more information, we can read the third-part link .    

Setting up Outlook to Use LDAP Address Book    

https://support.kerioconnect.gfi.com/hc/en-us/articles/360015199019-Setting-up-Outlook-to-Use-LDAP-Address-Book    

LDAP in Outlook 2013 & 2016 (Windows)    

https://help.uis.cam.ac.uk/service/email/hermes/ldap-settings/outlook-2013-and-2016-windows    

Please note: I am sorry, I can not find official link to explain it. Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best Regards,    

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

Ok thank you Daisy!
