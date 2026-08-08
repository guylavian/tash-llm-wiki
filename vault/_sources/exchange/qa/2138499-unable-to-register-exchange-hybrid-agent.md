---
title: "Unable to Register Exchange Hybrid Agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2138499/unable-to-register-exchange-hybrid-agent
question_id: 2138499
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to Register Exchange Hybrid Agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2138499/unable-to-register-exchange-hybrid-agent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

We were originally having some issues migrating mailboxes and the advice I found was to uninstall the hybrid agent and run the Hybrid Configuration Wizard again, so that is what I did, however when trying to run the HCW it fails to register the agent. I have checked all the prerequisites and we seem to meet all the requirements.

Looking at the logs the only error appears to be the bellow:

```
2024.12.27 01:51:17.046         10332 [Client=UX, fn=SendAsync, Thread=19] START PATCH https://graph.microsoft.com/beta/XXXXXXXX {"onPremisesPublishing":{"applicationServerTimeout":"Default","applicationType":"microsoftapp","externalAuthenticationType":"passthru","externalUrl":"https://XXXX.resource.mailboxmigration.his.msappproxy.net:443/","internalUrl":"https://XXXXXXX:443/","isOnPremPublishingEnabled":true,"isTranslateHostHeaderEnabled":false,"isTranslateLinksInBodyEnabled":false,"singleSignOnSettings":null,"verifiedCustomDomainCertificatesMetadata":null,"verifiedCustomDomainKeyCredential":null,"verifiedCustomDomainPasswordCredential":null}} 
2024.12.27 01:51:17.230         10333 [Client=UX, fn=SendAsync, Thread=19] FINISH Time=184.1ms Results=BadRequest {"error":{"code":"Invalid_App","message":"The application with objectId XXXXXXXX is soft-deleted","innerError":{"date":"2024-12-27T01:51:17","request-id":"XXXXXX","client-request-id":"XXXXXX"}}}
```

I have used MS Graph explorer to view all the soft deleted apps and this is not one of them. In fact I cannot find any reference to this app ID in our tenancy. I am guessing this is some leftover config from the last time HCW was ran, but I am unsure on how to clear it? My thoughts were maybe a registry Key somewhere.

Any help or suggestions would be appreciated as I have been unable to find any information on this issue.

## Answer (community) — community member

*upvotes: 1 · updated: 2025-02-11*

Hi All,   

Logged a ticket with Microsoft and they were able to restore the missing Application, after which I could remove it properly and re-run the Hybrid agent.   

Issue was definitely on the Azure side rather than any local configuration. While waiting for MS support I ended up building a new exchange server and it ended up having the same issue.   

Unfortunately this is one only MS support can help with. Very thankful the Tech's I got were able to help though.   

Thanks,   

Oscar Downing

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-30*

Hi,@OscarNHD

Thanks for posting your question in the Microsoft Q&A forum.

Based on the information you provided, it appears that the application has been “soft deleted” when using the PATCH operation to update certain configurations.

Here are my suggestions:

1.Access Azure AD for Deleted Applications:-

-  Go to the Azure portal. 

-  Navigate to Azure Active Directory. 

-  Select "App registrations". 

-  Look for a "Deleted applications" section to see if the application in question is listed there.

2.Clean Up Registry Keys (if applicable):  

-  Sometimes stale entries related to the HCW might reside in the registry. 

-  Open the Registry Editor on the server where HCW was run. 

-  Carefully navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\Hybrid` (the actual path may vary slightly depending on your environment). 

-  Look for any keys that might be related to the old configuration and remove them.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
