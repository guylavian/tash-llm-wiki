---
title: "working with EWS webservice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841856/working-with-ews-webservice
question_id: 1841856
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# working with EWS webservice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841856/working-with-ews-webservice (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

the server is working, and I copied the code from MSDN

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-authenticate-an-ews-application-by-using-oauth#add-an-authentication-token-to-ews-requests

 But the response is "The request failed. The remote server returned an error: (403) Forbidden."

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-29*

Hi @Abdulqader Al-Jupeh,

Welcome to the Microsoft Q&A platform!

Based on your description, a 403 Disabled Access Error usually indicates that your request was denied due to permissions or authentication issues. Here are some possible solutions:

-  Make sure the OAuth credentials you are using have sufficient permissions to access the EWS API. You may need to assign appropriate permissions to your app in the Azure portal (e.g. `EWS.AccessAsUser.All`).

-  Make sure the access token you obtain is valid, not expired, and is correctly added to the Authorization header in the request.

-  The scope of the request must be consistent with the scope set when your application is registered in Azure Active Directory.

-  Make sure your EWS request URL is correct and conforms to the required format. For example, if you are using Office 365, the URL should be similar to `https://outlook.office365.com/EWS/Exchange.asmx`.

Here is a concise sample code to refer to how to add an OAuth token:

```
ExchangeService service = new ExchangeService(ExchangeVersion.Exchange2013_SP1);
service.Url = new Uri("https://outlook.office365.com/EWS/Exchange.asmx");
service.Credentials = new OAuthCredentials("YOUR_ACCESS_TOKEN");

try
{
    // Example request to test the connection
    Folder inbox = Folder.Bind(service, WellKnownFolderName.Inbox);
    Console.WriteLine("Inbox folder display name: " + inbox.DisplayName);
}
catch (ServiceRequestException ex)
{
    Console.WriteLine("Service request failed: " + ex.Message);
}
catch (UnauthorizedAccessException ex)
{
    Console.WriteLine("Unauthorized: " + ex.Message);
}
catch (Exception ex)
{
    Console.WriteLine("An error occurred: " + ex.Message);
}
```

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
