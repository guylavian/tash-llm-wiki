---
title: "ADFS/IWA Integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/173710/adfs-iwa-integration
question_id: 173710
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS/IWA Integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/173710/adfs-iwa-integration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I successfully got SAML setup with ADFS with a third party site. I am attempting to have someone login to windows and access the third party site and auto logins to ADFS. To do this, I read that i needed to enable WIA and make sure the browsers are configured to allow it.

These were the articles I followed:  

Below are the articles I followed:  

https://help.hcltechsw.com/domino/11.0.1/admin/secu_creating_the_spn.html  

https://help.hcltechsw.com/domino/11.0.1/admin/secu_enabling_iwa_adfs30.html  

https://help.hcltechsw.com/domino/11.0.1/admin/secu_preparing_ie_for_adfs.html  

https://help.hcltechsw.com/domino/11.0.1/admin/secu_creating_the_spn.html  

https://support.classlink.com/hc/en-us/articles/360010601593-ADFS-Windows-Integrated-Authentication-WIA-

When i go to the thirdparty site after making the configurations, I get redirected to our ADFS client page and prompted for signin.

Can someone provide me with some guidance on what i am doing wrong?

see my browser developer info below. I added all browsers and everything that the other articles described  

I also setup the SPNS

setspn -s host/{your_Federation_Service_name} {domain_name}{service_account}

I also tried to set the SPNs for HTTP to my adfs federation name as well as the actual adfs server name and no matter which settings i have added, it makes no difference. When you go to the thirdparty site which then redirects you to ADFS, It continues to ask for a login.  

setspn -s HTTP/adfsfederationname.com admin  

setspn -s HTTP/adfsfederationname admin

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-25*

I know, me again :)

I'll try to be generic here as it is difficult to answer questions without traces. Sometimes the issue lies in small details that is obfuscated when we anonymize the scenario.

Assuming you are using a supported version of ADFS (2012 R2 or higher), assuming that you mean a WIA prompt and not a web form type of prompt. If what you are getting is a web form it could just the application that is configured to ask for form based auth. And we would see that in a Fiddler trace or browser debug network trace.

So let's review everything if what you get is a WIA prompt.

-   Make sure the Authentication Policy has Windows Integrated Authentication:  

      

    If you are running ADFS 2019 (you don't specify the version you are using in the question), you can check the following property and value:  

    

-   Make sure the user agent string of the browser you use for test is listed in here:  

      

    You can check the user agent string you send with the developer mode of your browser.

-   Make sure the FQDN of the farm is a A record in DNS and not a CNAME.  

    

-   Make sure FQDN of the machine where ADFS is installed is different from the FQDN of the ADFS farm (if your ADFS server is adfs.contoso.com you cannot call your farm adfs.contoso.com).

-   Make sure the SPN is positioned ONLY on the service account used for ADFS. Note that this account should just be a regular  

    domain user. No need to be an admin of the domain nor the server. Not recommended to use the builtin administrator account for anything (expect recovery scenarios).  

      

    You should have only 1 account returned, and it should be the service account for ADFS.

-   Check with a test account just member of Domain Users as accounts can carry restrictions (privilege limitations, logon restrictions, member of too many groups...). Check the User Right Assignment section on the ADFS server with gpedit.msc:  

    

-   If you are using some SSL offloading, or if the browser doesn't support channel binding token, you can try to disable it.  

    

-   Make sure the URL of the ADFS farm is listed as trusted in your browser (either in the local intranet zone or trusted zone) and check the zone settings, if they are default it should look like this for Intranet:  

    
    10. Try to bypass the load balancer if you have any using a HOSTS file to see if the issue is there.
