---
title: "ADFS / Server 2019 / AZURE-O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/61160/adfs-server-2019-azure-o365
question_id: 61160
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS / Server 2019 / AZURE-O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/61160/adfs-server-2019-azure-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have recently built and ADFS server and WAP in 2019 Server.  I have Azure AD Connect working.  I have not deployed this in production at this time and want t work out all the bugs and ensure it is 100%.   

I go to https://fs.(removed)/adfs/ls/idpinitiatedsignon from the ADFS server and client PC (me) and I am able to reach the page and sign in along with a test user.   

Myself and the test user, when we go to the application page which I have configured through Azure AD/O365.  First, it redirects to a Microsoft login page, we attempt to login using our domain credentials and it gives an error:  AADSTS50107: The requested federation realm object 'http://fs.(removed)/adfs/services/trust' does not exist.   

I believe the issue is with ADFS but I do not have the experience in ADFS to know.   

I am having a hard time locating any definitive cause reading articles.  Anyone have an idea that can point me in the right direction?   

Much appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-10*

After I was redirected back to the login page. I created a test user "Jane Doe" and attempted login with this new user.  Still same thing, redirected back and it appeared I did not login.     

I went to the Azure Portal and viewed the user sign -in and it looks like it shows it as successful?? weird.     

I also noticed that the user correctly has the alternate sign-in name listed which I thought is a good sign.     

Date	    

8/10/2020, 12:02:56 PM    

Request ID	    

c23b6251-7bea-4696-8864-ca66b951b400    

Correlation ID	    

3d2cbb6f-a2f9-4c86-8055-2bf264d06130    

Status	    

Success    

User	    

Jane Doe    

Username	    

******@my.domain.com    

User ID	    

f3a82835-7171-4bdb-9da0-34774b4104ff    

Alternate sign-in name	    

jdoe@keyman  .com    

Application	    

Tyler_Prod    

Application ID	    

e57f0213-e5d8-4e15-a39d-79471984ed33    

Resource	    

Windows Azure Active Directory    

Resource ID	    

00000002-0000-0000-c000-000000000000    

Client app	    

Browser    

Token issuer type	    

Azure AD    

Token issuer name	    

Latency	    

210ms    

User agent	    

Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-10*

PS C:\Users\Administrator> Convert-MsolDomainToFederated -domain mydomain.com  

Convert-MsolDomainToFederated : This domain already uses single sign-on.  

At line:1 char:1  

-  Convert-MsolDomainToFederated -domain mydomain.com  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : InvalidData: (:) [Convert-MsolDomainToFederated], FederationException  

-  FullyQualifiedErrorId : VerifiedFederatedDomainAlreadyExists,Microsoft.Online.Identity.Federation.Powershell.Con  

vertDomainToFederated

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-10*

I ran the scripts from the link  

Federation is enabled for the domain as see in the Azure portal  

I did not have the server in the local intranet zone so I added it.   

In ADFS, the Relying Party Trust has the Office 365 connection and it is enabled.  I can test the URL and it comes back good.   

When I attempt to log into the application I am given a redirect to fs.domain.com but then it immediately reverts back to the login page and states the federation realm object does not exist.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-07*

ADFS was configured in conjunction with the AD Connect.  I can see the Trust built for O365 in the ADFS console.    

I did not perform the final step as you stated.  I will do this shortly and let you know the results.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-06*

Hello FrancisIlisie-7917    

Did you process the configuration of your ADFS (associated Claims for O365, etc.) ? After you've processed the configuration of your ADFS + WAP, you should process the associated configuration in the AAD Connect. By selecting ADFS Authentication, throw AAD Connect wizard, it will automatically configure your ADFS farm with the required configuration steps (Claims, etc.).    

Finally, when you're ready. You just need to move your Domain to a Federated Domain. This step can be processed thanks to PowerShell. It's described in the Part 6 on the following link : https://learn.microsoft.com/fr-fr/office365/troubleshoot/active-directory/set-up-adfs-for-single-sign-on#step-6-connect-adfs-to-office-365.
