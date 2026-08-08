---
title: "Not able to connect LDAP Server from Azure App Service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1104262/not-able-to-connect-ldap-server-from-azure-app-ser
question_id: 1104262
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Not able to connect LDAP Server from Azure App Service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1104262/not-able-to-connect-ldap-server-from-azure-app-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have  built a webapp whose backend is Python Flask. We are using ldap3 library to integrate with Microsoft AD residing in AWS. And using this library, we are managing the user login process by looking into ldap and then authenticating. We are also leveraging ldap3 to get the attributes from AD.     

This whole set up is running well in Azure VM. But the moment we are deploying our code base to Azure App Service (in the same subscription group) it is giving 503 error.    

Really don't know what is happening here in Azure. I had tried whitelisting all the Outbound IP addresses of Azure App Service in the MS AD Server (being hosted on AWS), but no luck.     

One option is to deploy the whole service in AWS but that is not desirable.     

Please suggest. Appreciate a quick response.

## Answers

_No answers on this thread._
