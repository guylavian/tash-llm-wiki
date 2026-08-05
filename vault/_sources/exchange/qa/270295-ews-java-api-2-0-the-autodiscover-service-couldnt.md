---
title: "EWS Java API 2.0 - The Autodiscover service couldn't be located"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/270295/ews-java-api-2-0-the-autodiscover-service-couldnt
question_id: 270295
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# EWS Java API 2.0 - The Autodiscover service couldn't be located

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/270295/ews-java-api-2-0-the-autodiscover-service-couldnt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am using EWS Java API 2.0 to access user mailboxes from Exchange 2019 and O365 using autodiscoverUrl() method as EWS URL might change with new Client Access servers.

PFB the code snippet:

```
private static ExchangeService exchangeService;

    private static void usingAutodiscovery() {
        exchangeService = new ExchangeService();
        try {
            exchangeService.setTraceEnabled(true);
            exchangeService.setCredentials(new WebCredentials("username", "password", "domain.com"));
            // Set the URL.
            exchangeService.autodiscoverUrl(******@domain.com, new RedirectionUrlCallback());

            Folder inbox = Folder.bind(exchangeService, WellKnownFolderName.Inbox);
            System.out.println("messages: " + inbox.getTotalCount());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        usingAutodiscovery();
    }

    public static class RedirectionUrlCallback implements IAutodiscoverRedirectionUrl {
        public boolean autodiscoverRedirectionUrlValidationCallback(String redirectionUrl) {
            return redirectionUrl.toLowerCase().startsWith("https://");
      }
    }
}
```

But I am getting the below error:

```
microsoft.exchange.webservices.data.autodiscover.exception.AutodiscoverLocalException: The Autodiscover service couldn't be located.
    at microsoft.exchange.webservices.data.autodiscover.AutodiscoverService.internalGetLegacyUserSettings(AutodiscoverService.java:742)
    at microsoft.exchange.webservices.data.autodiscover.AutodiscoverService.getLegacyUserSettings(AutodiscoverService.java:521)
    at microsoft.exchange.webservices.data.autodiscover.AutodiscoverService.internalGetLegacyUserSettings(AutodiscoverService.java:959)
    at microsoft.exchange.webservices.data.autodiscover.AutodiscoverService.getUserSettings(AutodiscoverService.java:1846)
    at microsoft.exchange.webservices.data.core.ExchangeService.getAutodiscoverUrl(ExchangeService.java:3615)
    at microsoft.exchange.webservices.data.core.ExchangeService.autodiscoverUrl(ExchangeService.java:3572)
    at com.sample.autodiscover.UsingAutodiscover2.usingAutodiscovery(UsingAutodiscover2.java:47)
    at com.sample.autodiscover.UsingAutodiscover2.main(UsingAutodiscover2.java:60)
```

We have below details configured:  

AutodiscoverInternalUri = https://autodiscover.domainname.com/Autodiscover/Autodiscover.xml  

External EWS URL = https://domainname.com/ews/exchange.asmx

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-15*

Hi @ExchangeOnline444   ,    

Try to replace     

```
exchangeService.setCredentials(new WebCredentials("username", "password", "domain.com"));
```

with    

```
exchangeService.setCredentials(new WebCredentials("emailAddress", "password"));
```

Also test the autodiscover service with ECRCA    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
