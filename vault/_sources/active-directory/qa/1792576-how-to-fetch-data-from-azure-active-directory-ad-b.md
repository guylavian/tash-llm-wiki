---
title: "how to fetch data from Azure Active Directory(AD) by using either ADF or databricks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792576/how-to-fetch-data-from-azure-active-directory-ad-b
question_id: 1792576
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-data-factory", "azure-databricks", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to fetch data from Azure Active Directory(AD) by using either ADF or databricks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792576/how-to-fetch-data-from-azure-active-directory-ad-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

To fetch data from Azure Active Directory (AD) using either Azure Data Factory (ADF) or Azure Databricks, Pleae let me know in detail. thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 2 · updated: 2024-07-05*

Hi Lakshmi Narayana Sarma Bhamidipati,

Thank you for posting in the Q&A Forums.

Extracting data from Azure Active Directory (AD), including information about users, groups, and so on, can be done in a number of ways, but usually does not directly involve Azure Data Factory (ADF) or Azure Databricks for LDAP queries (although Azure Databricks can execute code that supports LDAP queries , but Azure AD interactions are more commonly through its Graph API or SDK).

Microsoft Graph is a unified API platform provided by Microsoft for accessing various data and services in Microsoft 365, including Azure Active Directory.By using the Graph API, you can write code to query users, groups, and other information in Azure AD.

Register an application: register an application in the Azure portal to obtain the necessary authentication information (such as client ID, client key, and redirect URI).

Obtain an access token: Use the OAuth 2.0 protocol to obtain an access token to access Microsoft Graph.

Build the query: Build the request using the Graph API's endpoints and query parameters to get the required Azure AD data.

Process response: parse the JSON response returned by the API to get information about users, groups, etc.

Example:

Query information about a specific user using the Graph API: GET https://graph.microsoft.com/v1.0/users/{user-id}

Query the members of a specific group: GET https://graph.microsoft.com/v1.0/groups/{group-id}/members

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-07-05*

Hi @Lakshmi Narayana Sarma Bhamidipati    

Thanks for the question and using MS Q&A platform.

To fetch data from Azure Active Directory (AD) using either Azure Data Factory (ADF) or Azure Databricks, you can use the Microsoft Graph API. The Microsoft Graph API is a RESTful web API that provides access to data in Microsoft 365 services, including Azure AD.  

Here are the high-level steps to fetch data from Azure AD using the Microsoft Graph API:

-  Register an Azure AD application in the Azure portal and grant it the necessary permissions to access the Microsoft Graph API.

-  Use the Azure AD application's client ID and client secret to authenticate your requests to the Microsoft Graph API.

-  Use the Microsoft Graph API to fetch the data you need from Azure AD.

To know more in detail, check out this video  

Hope this helps. Do let us know if you any further queries. 

If this answers your query, do click `Accept Answer` and `Yes` for was this answer helpful. And, if you have any further query do let us know.
