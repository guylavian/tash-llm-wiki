---
title: "The property Hashtags is valid only for Exchange Exchange2015 or later versions issue is keep hitting during email sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/296928/the-property-hashtags-is-valid-only-for-exchange-e
question_id: 296928
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# The property Hashtags is valid only for Exchange Exchange2015 or later versions issue is keep hitting during email sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/296928/the-property-hashtags-is-valid-only-for-exchange-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When the oAuth is turned off and on it is working

var exchangeVersion = Exchange2007AutoDiscover == true ? ExchangeVersion.Exchange2016 : Exchange2007Version;  

ExchangeService service = new ExchangeService(exchangeVersion);  

FindItemsResults<Item> inboxItems = null;  

EmailMessage message = null;  

Exchange07MessageEventArgs MsgEventArgs = null;  

try  

{  

if (Exchange2007AutoDiscover)  

{  

if (isEwsActiveCompany && isEwsActiveUser)  

{  

try  

{  

Task<ExchangeService> task = System.Threading.Tasks.Task.Run(async () => await AuthenticateAccountWithEwsOauthService(POPMailAddress, AzureAppId, azureTenantId, azureSecretKey));  

service = task.Result;  

}  

catch (Exception exc)  

{  

ErrorLogger.LogError(exc, rootFolder);  

}  

}  

else  

{  

service.Url = new Uri("https://outlook.office365.com/ews/Exchange.asmx");  

service.Credentials = new WebCredentials(POPMailAddress,POPMailPass);  

}  

}  

else  

{  

service.Url = new Uri(ExchangeURL);  

service.Credentials = new WebCredentials(POPMailAddress, POPMailPass);  

}  

service.Timeout = 300000;  

System.Net.ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls12 | SecurityProtocolType.Tls;  

if (service == null) return;

```
SearchFilter.IsNotEqualTo restriction = new SearchFilter.IsNotEqualTo(ItemSchema.ItemClass, "IPM.Schedule.Meeting.Request");
            SearchFilter.ContainsSubstring restriction1 = new SearchFilter.ContainsSubstring(ItemSchema.Attachments, "invite.ics", ContainmentMode.Prefixed, ComparisonMode.IgnoreCase);
            SearchFilter.Not restriction1_1 = new SearchFilter.Not(restriction1);
            SearchFilter.SearchFilterCollection restriction2 = new SearchFilter.SearchFilterCollection(Microsoft.Exchange.WebServices.Data.LogicalOperator.And);
            restriction2.Add(restriction);
            restriction2.Add(restriction1_1);
            //item shape left out 
            ItemView view = new ItemView(1000, 0, OffsetBasePoint.Beginning);

            ExtendedPropertyDefinition extendedProperty = new ExtendedPropertyDefinition(0x1013, MapiPropertyType.String);

            PropertySet propertySet = new PropertySet(PropertySet.FirstClassProperties.BasePropertySet, ItemSchema.MimeContent, extendedProperty);
            propertySet.Add(extendedProperty);
            propertySet.Add(ItemSchema.Body);
            propertySet.RequestedBodyType = BodyType.HTML;

            //PropertySet propertySet = (BasePropertySet.FirstClassProperties);

            if (latestDate != DateTime.MinValue)
            {
                SearchFilter.IsGreaterThanOrEqualTo restriction3 = new SearchFilter.IsGreaterThanOrEqualTo(ItemSchema.DateTimeReceived, latestDate);
                SearchFilter.SearchFilterCollection restriction4 = new SearchFilter.SearchFilterCollection(Microsoft.Exchange.WebServices.Data.LogicalOperator.And);
                restriction4.Add(restriction2);
                restriction4.Add(restriction3);
                try
                {
                    inboxItems = service.FindItems(WellKnownFolderName.Inbox, restriction4, view);
                    service.LoadPropertiesForItems(inboxItems, propertySet);

                }
                catch (Exception err)
                {
                    ErrorLogger.LogError(err, rootFolder);
                }
            }
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-04*

Hi @Noel   ,    

It seems like you are using the EMS Managed API, right?    

And I found     

service.Url = new Uri("https://outlook.office365.com/ews/Exchange.asmx";);    

service.Credentials = new WebCredentials(POPMailAddress,POPMailPass);    

Is it using the Exchange online accounts/credentials to logon? Sorry I don't know too much about this API and script.    

And are you using the hybrid Exchange? If it's only the on-prem(Exchange 2016) server, I couldn't get out why it will use Office 365 URL...    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
