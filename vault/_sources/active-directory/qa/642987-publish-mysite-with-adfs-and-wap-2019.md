---
title: "Publish Mysite with ADFS and WAP 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/642987/publish-mysite-with-adfs-and-wap-2019
question_id: 642987
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Publish Mysite with ADFS and WAP 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/642987/publish-mysite-with-adfs-and-wap-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our previous environment had SharePoint 2013 Publishing Portal and Mysite Site Collection on the Same Web Application.   

What we did then was to create SPN for the SharePoint Application Pool Service Account and add it under the Delegation tab of the Web Application Proxy Server. After that, we configured Non-Claims Aware Rule for the SharePoint URL in ADFS and created an ADFS Authenticated Publishing Rule for SharePoint Portal in the WAP Server.  

SharePoint Site was extended and the extended site had authentication changed from NTLM to Kerberos. Both SharePoint 2013 and MySite worked Externally.  

Currently, we have the following Separate Web Applications:  

-  SharePoint 2019 Communication Site Collection (Extended with Kerberos Authentication and ADFS Non Claims Aware and WAP ADFS Authentication Publishing Rule Created)  

-  MySite Host Site Collection  

Want to publish Mysite via ADFS and WAP. (Mysite in on another Web Application)  

Have added the MySite SPNS to the Application Pool Account that runs both SharePoint Portal and My Site. I have also created a Non-Claims Aware Rule for My Site too in ADFS.  

I have extended the Mysite with Kerberos Authentication and have an external DNS record for the Mysite Host created But do I have to create an ADFS Authenticated Publishing rule for Mysite in WAP? If I do this, would the user have to login into another ADFS Login Page? Is this the right way? or should I just use a Passthrough Rule?  

Have used the following guide: http://www.sharepoint4developers.net/en-nz/post/wap-adfs-sp2013-kerberos.aspx (However the WAP Rule for Mysite is not mentioned)...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-16*

Found out that you do need to create a WAP Publishing Rule for Mysites too. Whereas the authentication goes, since both SharePoint and MySites are on separate Web Applications, will the external user need to authenticate twice, firstly for the SharePoint Site and Secondly for the MySite Employee Profile. The answer to that is no, as once the user is authenticated via ADFS, access to both SharePoint Portal and Mysites is granted via SSO.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-29*

When publishing a non-claim aware application with WAP you need to:    

-  Create a non claim aware relying party trust in ADFS    

-  Crate a publication for the site in the WAP console (referencing this relying party trust) using ADFS pre-authentication.    

There are some examples here: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/web-application-proxy/publishing-applications-using-ad-fs-preauthentication

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-29*

Hi @Sheldon D'souza   ,    

As I don't have a environment which integrates with ADFS and WAP, I am not able to have a test on my side for you. You can open a ticket with Microsoft, experts there will give you instant help and professional suggestions.    

----------    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
