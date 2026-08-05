---
title: "Query variables in SharePoint Server - SharePoint Server"
description: "Learn about the query variables that you can use when you configure a query."
ms.topic: reference
---
Note

Query variables in SharePoint Server

# Query variables in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Note: This article does not apply to Modern Microsoft Search experiences and APIs. To learn about Modern Search, see Profile Query Variables.

Query variables

## Query variables

The following tables show the query variables for SharePoint Server and SharePoint in Microsoft 365, and examples on how they can be used.

**Site and site collection properties**

| **Query variable** | **Definition** |
| --- | --- |
| {Site} or {Site.URL} | URL of the site from where the query was issued. For example, this value can be used to query content of the managed property Path. |
| {Site.ID} | GUID of site from where the query was issued. This value corresponds to the value of the managed property WebId. |
| {Site.LCID} | Numeric value of the locale as specified by the Regional Settings in the Site Settings on the Site from where the query was issued. |
| {Site.Locale} | Language of the Site from where the query was issued in ll-cc format — for example, en-us. |
| {Site.<property>} | Any property from the property bag of the site (SPWeb) from where the query was issued, including custom properties. |
| {SiteCollection} or {SiteCollection.URL} | URL of site collection from where the query was issued. For example, this value can be used to query content of the managed property Path. |
| {SiteCollection.ID} | GUID of site collection from where the query was issued. This value corresponds to the value of the managed property SiteID. |
| {SiteCollection.LCID} | Numeric value of the locale as specified by the Regional Settings in the Site Settings on the Site Collection from where the query was issued. |
| {SiteCollection.Locale} | Language of the Site Collection from where the query was issued in ll-cc format — for example, en-us. |
| {SiteCollection.<property>} | Any property from the property bag of the root site (SPWeb) in the site collection (SPSite) from where the query was issued, including custom properties. |

**Page, URL token, query string and request properties**

| **Query variable** | **Definition** |
| --- | --- |
| {Page} or {Page.URL} | URL of the page from where the query was issued. For example, this value can be used to query content of the managed property Path. |
| {Page.UsageAnalyticsId} | Item ID for Usage Analytics |
| {Page.<FieldName>} | The value of a field on the page from where the query was issued. For example, if the page from where the query was issued contained a site column named "ContentOwner," specifying {Page.ContentOwner} would allow you to query for the value of "ContentOwner." |
| {URLToken.<integer>} | A value from the URL of a page. The integer represents the position of the value in the URL as counted from right to left. For example, for the page `http://www.contoso/audio/mp3/1010101`, the query variable {URLToken.1} will query for the last value in the URL, 1010101. The query variable {URLToken.3} will query for the third last property in the URL, audio. You can query for values up to the ninth last position in a ULR. |
| {QueryString.<ParameterName>} | A value from a query string in the URL of the current page. For example, if the URL of the current page contains a query string such as ItemNumber=567, you could obtain the value 567 by specifying {QueryString.ItemNumber}. |
| {Request.<PropertyName>} | A value from the current http request - for example, {Request.Url}. |

**User properties**

| **Query variable** | **Definition** |
| --- | --- |
| {User} or {User.Name} | Display name of the user who issued the query. For example, this value can be used to query content of the managed property Author. |
| {User.Email} | Email address of the user who issued the query. For example, this value can be used to query content of the managed property WorkEmail. |
| {User.SID} | SID of the user who issued the query. |
| {User.LCID} | Numeric value of locale as defined in the profile of the user who issued the query. |
| {User.PreferredContentLanguage} | Language as specified as Preferred Content Language in the profile of the user who issued the query. |
| {User.PreferredDisplayLanguage} | Language as specified as Preferred Display Language in the profile of the user who issued the query. |
| {User.<property>} | Any property from the user profile of the user who issued the query — for example, SPS-Interests, including custom properties. |
| {User.Audiences} 

(SharePoint only) | Used with modern SharePoint audience targeting filtering on the managed property `ModernAudienceAadObjectIds`. Example: `ModernAudienceAadObjectIds:{User.Audiences}`. |

**Term and term set properties**

| **Query variable** | **Definition** |
| --- | --- |
| {Term} or {Term.ID} or {Term.IDNoChildren} | GUID of current site navigation node with a prefix of #0 — for example, #083e99dcb-7907-4dc9-abc8-b5614a284f1c. For example, this value can be used to query content of the managed property owstaxIdMetadataAllTagsInfo or owstaxIdProductCatalogItemCategory in a Product Catalog Site Collection. |
| {Term.IDWithChildren} | GUID of current site navigation node with a prefix of # — for example, #83e99dcb-7907-4dc9-abc8-b5614a284f1c. This will return all items tagged with the current site navigation term, or children of the current site navigation term. For example, this value can be used to query content of the managed property owstaxIdProductCatalogItemCategory in a Product Catalog Site Collection. This value cannot be used to query the content of the managed property owstaxidmetadataalltagsinfo. |
| {Term.Name} | Label of the site navigation node — for example, Audio. |
| {Term.<property>} | Any property from the property bag of the term, including custom properties. |
| {TermSet} or {TermSet.ID} | GUID of the term set used for current site navigation. |
| {TermSet.Name} | Label of the term set used for current site navigation. |

**List and list item properties**

| **Query variable** | **Definition** |
| --- | --- |
| {List} | URL of the current list. |
| {List.<property>} | Any property of the current list. |
| {ListItem} | URL of the current list item. |
| {ListItem.<property>} | Any property of the current list item. |

**Other properties**

| **Query variable** | **Definition** |
| --- | --- |
| {Today+/- <integer value for number of days>} | A date calculated by adding/subtracting the specified number of days to/from the date when the query is issued. Date format is YYYY-MM-DD. For example, this value can be used to query content of the managed property LastModifiedTime. |
| {SearchBoxQuery} | The query value entered into a search box on a page. |
| {CurrentDisplayLanguage} | The current display language based on MUI in ll-cc format. |
| {CurrentDisplayLCID} | Numeric value of the current display language based on MUI in ll-cc format. |

Dealing with spaces in values

### Dealing with spaces in values

Search queries use the space character to tokenize query values issued by users. When a query variable is expanded to a value that contains a space, the complete value is enclosed in double quotations. For example, for the query author:{User}, the expanded value becomes author:"John Smith".

If you don't want the value to be enclosed with double quotations — for example, when concatenating multiple values — you can use the escape character in the query variable. For example: customProperty:"{\User.Name};{\User.ZipCode}" would become customProperty:"John Smith;98109".

Query variables with multiple values

### Query variables with multiple values

Some query variables may return multiple values. For query variables that return multiple values, the following syntax must be used: {|ManagedProperty:{QueryVariable}}. All the query variable values will be combined by using the bitwise OR operation. For example, say that you have a term set that is used to categorized interest of users. All users are configured to have one or more interests using the multi-value property SPS-Interests in the User Profile Service Application. To issue a query for any of the interests of the current user, the following syntax could be used: {|owstaxIdMetadataAllTagsInfo:{User.SPS-Interests}}. If the current user is configured to have two interests — football (#0f95d1fdf-781f-42f4-99f9-c656c1341b2e) and basketball (#0c2cff933-9377-4692-aa98-ce59768aa38b) — the query will be transformed to  *(owstaxIdMetadataAllTagsInfo:#0f95d1fdf-781f-42f4-99f9-c656c1341b2e) OR (owstaxIdMetadataAllTagsInfo:#0c2cff933-9377-4692-aa98-ce59768aa38b)*  .

There are some restrictions with using multiple values. Only the OR operator ({|) is supported for multiple values. The AND operator is not supported. Also, only columns of type Managed Metadata work correctly for multiple value cases. Other types of columns that may use multiple values, such as columns of type Person or Group or Choice, the items will be expanded into a delimited string.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
