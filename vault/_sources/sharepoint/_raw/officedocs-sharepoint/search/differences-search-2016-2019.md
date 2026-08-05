---
title: "Differences between the search experiences in SharePoint Server - SharePoint Server"
description: "Learn about the differences between the search experiences in SharePoint Server"
ms.topic: article
---
Note

Differences between the search experiences in SharePoint Server

# Differences between the search experiences in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In addition to the classic search experience, SharePoint Server 2019 comes with a modern search experience. Both search experiences use the same search index to find results.

As a user, the most visual difference is that in modern search, you see results even before you start typing in the search box, and the results update as you type. Learn about the modern search experience.

As a search administrator, you can not disable classic or modern search. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the modern search experience on the SharePoint home page, communication sites, and modern team sites. There are some differences between the search experiences from a search administrator's perspective.

Search administrators can customize the *classic* search experience, but only impact some aspects of the modern search experience. There aren't separate search settings for the modern search experience. Instead certain of the classic search settings **also** apply to the modern search experience:

- Sortable

- Refinable

- Company name extraction

- Custom entity extraction

- The modern search experience only shows results from the default result source. If you change the default result source, both search experiences are impacted.

- If you temporarily remove a search result, the result is removed in both search experiences.

- When you create a promoted result at the tenant level, users can see it in both search experiences. In the modern search experience, users only see promoted results when they’ve filtered to All result types (default filter) on the search results page and only when they search across all sites.

Unlike the classic search results page, the modern search results page isn’t built with web parts. You can’t customize the modern search results page or create additional search results pages.

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
