---
title: "Publish SharePoint to internet via WAP / ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192101/publish-sharepoint-to-internet-via-wap-adfs
question_id: 192101
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Publish SharePoint to internet via WAP / ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192101/publish-sharepoint-to-internet-via-wap-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello together,  

we are going to publish a SharePoint Website (on-premise) to the WWW via Microsoft Web Application Server / ADFS. Question, WAP is redirectiong the request to the ADFS login and the URL changes. Can this be avoided? We don't want to change the URL, we would like to have the whole request as one URL from the WAP. Many thanks in advance!

## Answer (community) — community member

*upvotes: 2 · updated: 2020-12-10*

Hello @Sibylla   ,

Please follow steps to publish SharePoint Site externally using Web Application Proxy ​(WAP):

Step1
 Configure SharePoint Web Applications to use Kerberos authentication

-    It is worth noting that configuring Kerberos authentication is a key step in exposing the SharePoint to the outside world through WAP

-    Please refer to "Plan for Kerberos authentication in SharePoint Server" to configure Kerberos authentication.

Step2
 Install and Configure WAP and AD FS

Step3
 Create a non-claims aware relying party trust

-    When ADFS and WAP servers have been built, the next step involves configuring ADFS so that Internet can handle the authentication of external users against your SharePoint web applications.

-    The following steps:

1) Within the ADFS Management console click Add Non-Claims-Aware Relying Party Trust on the left hand side of the screen.  

2) Click Start on the first page and then enter a name such as "Non-claims provider for SharePoint".  

3) In the Add Non-Claims-Aware Relying Party Trust Wizard, on the Welcome page, click Start.  

4) On the next page click next and when prompted to enter a relying party trust identifier, enter any URL (it really doesn't matter what this, but useful to be something you recognize).  

5) Click Next, Next, Next and finish, and when the Edit Claim Rules window appears, click Add rules.  

6) On the Edit Claim Rules click Add Rule, and from the drop down select Permit All Users and then click Next and then Finish.

Step4
 Configure constrained delegation

Step5
 Publish SharePoint Web Applications in WAP

Step6
 Verify external access to SharePoint Web Applications

More information, please refer to the below article:

-    Securely publishing SharePoint externally using Web Application Proxy ​(WAP)

Thanks,  

Echo Du

======================

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-12-09*

There are different ways to integrate with SharePoint.     

-  You can configure Sharepoint to use ADFS for authentication instead of Windows Integrated Authentication. It has some effect has it changes the way the people picker works. And probably other side effects.    

-  You can publish Sharepoint as a Kerberos application through WAP (aka Non claim aware application in ADFS/WAP).    

For that 2 point, the URL can (even should) be the same. It would be a split brain DNS situation.    

-  When users are connected on-prem, the URL of your Sharepoint server will point to the IP address of your Sharepoint server (or load balancers).     

-  When users are connected on the Internet, the URL of your Sharepoint server will point to the public IP address of your WAP server (or servers behind a load balancer).    

It has some requirements you can find here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/create-a-non-claims-aware-relying-party-trust

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Hi @Echo Du_MSFT  ,    

I changed the following parts:    

-  URL in Non-claims-aware relying party trust identifier    

-  Publishing the Application in WAP with the new Relying Party Trust    

-  Change the internal certificate to the one with the correct URL    

But it still forwards me to the ADFS URL.     

Any ideas?    

Many thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

Hello @Echo Du_MSFT   and @Pierre Audonnet - MSFT   ,    

thanks a lot for your answers. The authentication via Login is already working.    

But we still have this URL change. The behavior is like in this article https://learn.microsoft.com/en-us/archive/blogs/sambetts/sharepoint-web-application-proxy-2016-edition where you can see that the link changed in the browser to ADFS for the login form     

    

This is happening for us too. We have a rewriting configured before the proxy and this does not work as the URL changes. If I understand your answers correctly it is possible to keep one URL. Where can this be configured?    

Thank your very much.    

Best regards    

Sibylla
