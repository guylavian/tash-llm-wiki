---
title: "How to change the order in which classic search results are displayed in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-how-to-change-the-order-in-which-search-results-are-displayed
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/how-to-change-the-order-in-which-search-results-are-displayed
family: search
documentKind: "how-to"
abstract: "Learn how to change the order in which search results are displayed in SharePoint Server."
---

# How to change the order in which classic search results are displayed in SharePoint Server - SharePoint Server

Note

How to change the order in which classic search results are displayed in SharePoint Server

# How to change the order in which classic search results are displayed in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In the series How to change the way search results are displayed in SharePoint Server we explained how to customize the way search results are displayed by adding custom icons and properties.

When it comes to displaying search results, design and content are indeed important. However, there's one thing that often trumps them both: the order in which search results are displayed.

Think of your own behavior when looking at search results. How often do you click to view the second page of search results? Often, the answer is "rarely."

So, when displaying search results, it's important that the results that your users are looking for are displayed as high up in the search results list as possible. This article, an addendum to the How to change the way search results are displayed in SharePoint Server series, explains how to use a query rule to change the order in which classic search results are displayed. To demonstrate how query rules work, we'll use an example from an internal Microsoft Search Center.

In this article, you'll learn:

What was the problem again?

When using query rules: define before you assign

How to create a query rule that will change the order in which classic search results are displayed

How do I know that the query rule's been applied?

Think two times before you apply a query rule

What was the problem again?

## What was the problem again?

As you know, Microsoft publishes thousands of articles across TechNet, MSDN, and Office.com. To help in the publishing process, we use several SharePoint lists. Each item in a list represents an article or a media file. To make it easy to find information about a particular list item, we created a Search Center that searches across these lists.

The following screenshot shows the default order in which search results were displayed in our Search Center. Notice that search results for articles and images were displayed in a mixed order.

When users search for something in this Search Center, they're usually looking for information about an article. So, to make it easier for users to find information about articles, we wanted to change the order of the search results so that images would be displayed at the bottom. To do this, we had to create a query rule.

When using query rules: define before you assign

## When using query rules: define before you assign

A query rule is largely what the name implies: a rule that can be applied to queries. But before you start to assign rules to your queries, you should define what you want the query rule to do.

Basically, you have to define two things: a condition and an action. Simply put, this comes down to defining the following:

*"when X (condition), do Y (action)."*

In our Search Center scenario, we knew the action part:  *Display list items that represent images at the bottom of the search results list*.

In our lists, we use the site column  *Content Type*  to differentiate between the type of articles or media types a list item represents. For example, all images have the value "Art" for  *Content Type*.

Based on this, we were able to define the condition part so that my final definition was:

*When list items are of Content Type "Art," display these at the end of the search results list.*

So, with the definition in place, we could begin to create the query rule that would make this happen.

How to create a query rule that will change the order in which search results are displayed

## How to create a query rule that will change the order in which search results are displayed

Depending on your permission level, you can create a query rule on three levels:

| **Permission level** | **Where the query rule will be applied** |
| --- | --- |
| Search service application administrator | To all site collections within the farm |
| Site collection administrator | To all sites inside a site collection |
| Site collection owner | To a single site |

To save space, we'll only show you how to create a query rule as a Site collection administrator.

Go to **Site Settings** --> **Search Query Rules**.

On the **Manage Query Rules** page, from the **Select a Result Source** menu, select the result source to which the query rule should be applied.

Select **New Query Rule**.

On the **Add Query Rule** page, in the **Rule name** field, enter a name for the query rule.

In our Search Center scenario, we named the query rule  *Demote Art*.

In the **Query Conditions** section, specify the conditions that will trigger the query rule.

In our Search Center scenario, we wanted the query rule to be triggered every time that a user entered a query. In other words, we didn't want the query rule to be triggered by a specific condition. Therefore, we selected **Remove Condition**.

In the Actions section, specify what you want the query rule to do when it's triggered.

In our Search Center scenario, we selected **Change ranked results by changing the query**. This opened a dialog where we could define what we wanted the query rule to do.

We wanted to change the order of search result. Therefore, in the **Build Your Query** dialog, we selected the **SORTING** tab.

From the **Sort by** menu, we selected **Rank**.

From the **Dynamic ordering section**, we selected **Add dynamic ordering rule**.

From the **Change ranking when** menu, we selected **Manual condition**.

Remember, we wanted list items of Content Type  *Art*  to be displayed at the end of the search results list. So, in the **Manual condition** field, we entered  *ContentType: Art*, and selected **Demote to bottom**.

Now, before we move on, let's analyze what we entered:

**ContentType** is the managed property that represents the site column Content Type. How to display values from custom managed properties in search results - option 1 in SharePoint Server explains how to find managed property names.

The colon: means "contains".

**Art** is the managed property value.

**Demote to bottom** is the action that should be taken.

Put it together, and it matches the definition we specified:  *When list items are of Content Type "Art," display these at the end of the search results list*.

Select **OK**, and then **Save**.

Your newly created query rule will be listed on the Manage Query Rules page.

In our Search Center scenario, we could see that the Demote Art query rule was created.

When we now entered a search in the Search Center, we could see that articles were displayed at the top of the search results list, and images were displayed at the bottom. Nice!

How do I know that the query rule's been applied?

## How do I know that the query rule's been applied?

In our Search Center scenario, we could easily verify that the query rule we created was being applied. But, if you're uncertain about whether your query rule is being applied, the **Search Results Web Part** can give you an answer.

Here are the steps to verify that a query rule is being applied:

On your search results page, select to edit the **Search Results Web Part**.

In the Web Part tool pane, select **Change query**.

In the **Build Your Query** dialog, select the **TEST** tab, and then **Show more**.

In the **{searchboxquery}** field enter a query that you know should cause the query rule to be triggered, and then select **Test query**.

In our Search Center scenario, we could verify that our query rule was working by looking at the following:

In the field **Applied query rules**, the name of our query rule, Demote art, was shown.

In the **Query text** section, XRANK was applied to  *ContentType: Art*.

Think two times before you apply a query rule

## Think two times before you apply a query rule

Even though this was a fairly simple query rule, we saw that the effect was noticeable. So a word of warning: even though query rules are great for changing the order in which classic search results are displayed, you should think carefully before you apply too many of them. The effects can be large, and the more complex query rules that you have, the more performance resources each query will require.

But, if they're used with caution, you can make the users of your Search Center happy customers.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
