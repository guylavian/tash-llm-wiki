---
title: "Plan and manage cases in the eDiscovery Center - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-plan-and-manage-cases-in-the-ediscovery-center
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/plan-and-manage-cases-in-the-ediscovery-center
family: governance
documentKind: "concept-article"
abstract: "Electronic Discovery, or eDiscovery, is the discovery of content in electronic format for litigation or investigation. This typically requires identifying content spread across laptops, email servers, file servers, and many other sources."
---

# Plan and manage cases in the eDiscovery Center - SharePoint Server

Note

Plan and manage cases in the eDiscovery Center

# Plan and manage cases in the eDiscovery Center

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Electronic Discovery, or eDiscovery, is the discovery of content in electronic format for litigation or investigation. This typically requires identifying content spread across laptops, email servers, file servers, and many other sources.

The eDiscovery Center is a SharePoint site collection used to perform electronic discovery actions. In an eDiscovery Center, you can create cases, which are SharePoint sites that allow you to identify, hold, search, and export content from SharePoint sites, and searchable file shares.

Note

Once you add content sources or queries to an eDiscovery case, changing the regional settings for the site is not supported. >  In order for content to be discovered, it must be crawled by search. For more information about the default file types that are crawled, see the article Default crawled file name extensions and parsed file types in SharePoint Server 2013.

Planning and creating cases

## Planning and creating cases

If you anticipate managing multiple cases in your eDiscovery Center, consider whether you want to define consistent processes for people in your organization to follow.

Naming conventions for cases - Could matter if you anticipate a larger number of cases, or different types or classifications of cases, for different departments,

Additional data to describe cases

Defining and communicating permissions for managing cases.

Guidelines on creating queries

Standard procedures for communicating when content is placed on hold

Standard procedure for retaining and closing cases

Example lifecycle of an eDiscovery case

### Example lifecycle of an eDiscovery case

Create the site to manage a case

Add sources

Place sources on hold

Create queries

Export case content

Close case

Create a case

## Create a case

In an eDiscovery Center, select **Create new case**.

Enter a title and description for your case.

In the **Web Site Address** box, enter the last part of the URL you want for the case, such as ContosovsFabrikam.

Under **Select a template**, make sure that **eDiscovery Case** is selected.

Under **User Permissions**, select whether to keep the same permissions as the parent site or use unique permissions. If specific people will need access to this case, but not to other cases, you should choose **Use unique permissions**.

Add sources and place them on hold

## Add sources and place them on hold

In the eDiscovery Center, open the case that you want to add a source to.

Select **eDiscovery Sets**.

Enter a name for the eDiscovery Set, such as Executive Correspondence.

Next to **Sources**, select **Add & Manage Sources**.

Under **Locations**, enter the URL or file share address for the content you want to use as the source. Any content you include must be indexed by search.

Select **Save**.

In the box under **Filter**, enter any keywords you want to use to narrow down the source.

To narrow down content by a date range, enter the **Start Date** and **End Date**.

To limit results to the author of a document or list item, or to a specific sender of email messages, in the **Author/Sender** box, enter the names or email addresses.

Select **Apply Filter**.

Select **Enable In-Place** hold.

To verify that you've selected the right content, select **Preview Results**.

Select **Save**.

For more info, see Add content to a case and place sources on hold in the eDiscovery Center.

Run queries and export content

## Run queries and export content

After you have defined your sources, and placed them on hold if necessary, you can run queries to narrow down and extract exactly the content you need for a particular case. SharePoint has some tools that can help you refine your queries.

You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. The content is exported in a format that is compatible with the Electronic Discovery Reference Model standard.

Close cases

## Close cases

When you close a case, in-place holds will be released for all of its sources, and you will no longer be able to put sources on hold for this case.

Select **Settings** , and then select **Case Closure**.

Select **Close this case**.

Find more info about eDiscovery

## Find more info about eDiscovery

For more info about eDiscovery cases, see the following articles:

Add content to a case and place sources on hold in the eDiscovery Center

Searching and using keywords in the eDiscovery Center

Default crawled file name extensions and parsed file types in SharePoint Server

Overview of crawled and managed properties in SharePoint Server

Create and run queries in the eDiscovery Center

Export content and create reports in the eDiscovery Center

Additional resources

## Additional resources

- Last updated on 
		2023-04-24
