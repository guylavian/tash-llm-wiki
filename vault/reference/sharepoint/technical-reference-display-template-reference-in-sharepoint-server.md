---
title: "Display template reference in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-display-template-reference-in-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/display-template-reference-in-sharepoint-server
family: technical-reference
documentKind: "reference"
abstract: "Learn about the different display templates that are available in SharePoint Server."
---

# Display template reference in SharePoint Server - SharePoint Server

Note

Display template reference in SharePoint Server

# Display template reference in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Display templates for the Content Search Web Part

## Display templates for the Content Search Web Part

You can use the following display templates to change the appearance of content that is shown in a Content Search Web Part. These display template files are located in the Content Web Parts subfolder in the Display Templates folder in the Master Page Gallery.

| **Display template type** | **Name in Web Part Tool Pane** | **Name in Master Page Gallery** | **Description** |
| --- | --- | --- | --- |
| Control display template | List | Control_List | Displays the items in the Web Part as a list. It is the default control display template when you add a new Content Search Web Part to a page. |
| Control display template | List with Paging | Control_ListWithPaging | Displays the items in the Web Part as a list, and lets users page through the items by using arrows. It is the default control display template for Content Search Web Parts on Category pages. |
| Control display template | Slideshow | Control_Slideshow | Displays the items in the Web Part as a picture slide show that rotates through a set of images every 5 seconds. It shows one item at a time, with the title of the item overlaying the picture. |
| Item display template | Diagnostic | Item_Diagnostic | Displays the underlying values for items returned by the query specified in the Web Part. This item display template can be very helpful when troubleshooting why items do not appear correctly in the Web Part. |
| Item display template | Large picture | Item_LargePicture | Displays an image of the item returned by the query specified in the Web Part, with the title of the item overlaying the image. This item display template should be used with the **Slideshow** control display template, and with images that are more than 400 pixels wide. |
| Item display template | Picture on left, 3 lines on right | Item_Picture3Lines | Displays a 100 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed to the right of the image. An additional line is available as a placeholder that can be used to display a managed property. |
| Item display template | Picture on top, 3 lines on bottom | Item_PictureOnTop | Displays a 304 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed below the image. An additional line is available as a placeholder that can be used to display a managed property. |
| Item display template | Recommended Items: Picture on left, 3 lines on right | Item_RecommendationsClickLogging | Displays a 100 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed to the right of the image. An additional line is available as a placeholder that can be used to display a managed property. |
| Item display template | Two lines | Item_TwoLines | Displays a small thumbnail icon next to a hyperlink of the title of the item returned by the query specified in the Web Part. An additional line is available as a placeholder that can be used to display a managed property. |
|  |  | Group_Content | This file is used to render the different display templates. You should not change this file. |

Display templates for the Refinement Web Part and the Taxonomy Refinement Web Part

## Display templates for the Refinement Web Part and the Taxonomy Refinement Web Part

You can use the display templates listed in the following table to change the appearance of content that is shown in a Refinement Web Part and a Taxonomy Refinement Web Part. These display template files are located in the Filters subfolder in the Display Templates folder in the Master Page Gallery. Note that there are different display templates for different refiner types.

| **Display template type** | **Name in Web Part Tool Pane** | **Name in Master Page Gallery** | **Description** |
| --- | --- | --- | --- |
| Control display template | Vertical | Control_Refinement | The control display template for the Refinement Web Part. |
| Control display template | Default Taxonomy Refinement | Control_TaxonomyRefinement | The control display template for the Taxonomy Refinement Web Part. |
| Item display template | Refinement Item | Filter_Default | Item display template for refiners of type Text, Decimal, and Date. Displays the refiners in a list. Users can click a specific refiner to narrow the search results. |
| Item display template | Multi-value Refinement Item | Filter_MultiValue | Item display template for refiners of type Text, Decimal, and Date. Displays the refiners in a list that has a check box next to each refiner. Users can select multiple refiners to narrow the search results. If you want to change how multi-value refiners are shown on a page, you should not change this display template, but instead use the Multi-value Refinement Item Body template. |
| Item display template | Multi-value Refinement Item Body | Filter_MultiValue_Body | Item display template that works together with Multi-value Refinement Item file. If you want to change how multi-value refiners are shown on a page, you should change this display template. |
| Item display template | Slider | Filter_Slider | Item display template for refiners of type Decimal. Displays the refiners according to ranges in a slider bar. Users can slide the bar to narrow search results. |
| Item display template | Slider with bar graph | Filter_SliderBarGraph | Item display template for refiners of type Decimal. Displays the refiners according to ranges in a slider bar and bar graph. Users can slide the bar or click a bar graph to narrow search results. |
| Item display template | Link with count | Filter_TaxonomyRefinement | The default item display template for the Taxonomy Refinement Web Part. Displays the refiners in a list. For each refiner, the number of items that contains the refiner value is displayed. Users can click a specific taxonomy refiner to narrow the search results. |
|  | User Specified Refinement Exchange | Filter_eDiscoveryExchangeRefinement | This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file. |
|  | Message Type Refinement | Filter_eDiscoveryExchangeTypeRefinement | This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file. |
|  | User Specified Refinement SharePoint | Filter_eDiscoverySharepointRefinement | This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file. |

Display templates for the Search Results Web Part

## Display templates for the Search Results Web Part

You can use the display templates in the following table to change the appearance of content shown in a Search Results Web Part. Note that the hover panels for the different result types have separate display templates. These display template files are located in the Search subfolder in the Display Templates folder in the Master Page Gallery.

| **Display template type** | **Name in Web Part Tool Pane** | **Name in Master Page Gallery** | **Description** |
| --- | --- | --- | --- |
| Control display template | Default Search Box | Control_SearchBox | Displays the search box in a Search Box Web Part. It is the default control display template for the Search Box Web Part. |
| Control display template | Site Search Box | Control_SearchBoxCompact | Displays the search box in a Search Box Web Part in a compact form. |
| Control display template | Default Result | Control_SearchResults | The default control display template for the Search Results Web Part. |
| Control display template | Default Group | Group_Default | Displays the default group template. Items can be arranged horizontally or vertically depending on how the item template styled. Note that this control display is hidden, so that you will not be able to select this in the Web Part tool pane. |
| Item display template | Best Bet Item | Item_BestBet | Displays a single promoted result that is specified by using query rules. |
| Hover panel | Common Hover Panel Actions | Item_CommonHoverPanel_Actions | Displays the hover panel actions that are common to all search results. |
| Hover panel | Common Hover Panel Body | Item_CommonHoverPanel_Body | Displays the hover panel footer elements that are common to all search results. |
| Hover panel | Common Hover Panel Header | Item_CommonHoverPanel | Displays the hover panel header elements that are common to all search results. |
| Item display template | Common Item Body | Item_CommonItem_Body | Displays the inline search result body elements that are common to all search results. |
| Item display template | Community Item | Item_Community | Displays a search result that is customized for community posts and replies. |
| Hover panel | Community Hover Panel | Item_Community_HoverPanel | Displays a search result hover panel that is customized for community posts and replies. |
| Item display template | Default Item | Item_Default | Displays the default search result item template. |
| Hover panel | Default Hover Panel | Item_Default_HoverPanel | Displays the default search hover panel template. |
| Item display template | Discussion Item | Item_Discussion | Displays a search result that is customized for community discussions. |
| Hover panel | Discussion Hover Panel | Item_Discussion_HoverPanel | Displays a search result hover panel that is customized for community discussions. |
| Item display template | Excel Item | Item_Excel | Displays a search result that is customized for Microsoft Excel documents. |
| Hover panel | Excel Hover Panel | Item_Excel_HoverPanel | Displays a search result hover panel that is customized for Microsoft Excel documents. |
| Item display template | Microblog Item | Item_MicroBlog | Displays a search result that is customized for microblog feed posts and replies. |
| Hover panel | Microblog Hover Panel | Item_MicroBlog_HoverPanel | Displays a search result hover panel that is customized for microblog feed posts and replies. |
| Item display template | Office Document Item | Item_OfficeDocument | Displays a search result that is customized for Microsoft Office documents. |
| Hover panel | Office Document Hover Panel | Item_OfficeDocument_HoverPanel | Displays a search result hover panel that is customized for a Microsoft Office document. |
| Item display template | OneNote Item | Item_OneNote | Displays a search result that is customized for Microsoft OneNote documents. |
| Hover panel | OneNote Hover Panel | Item_OneNote_HoverPanel | Displays a search result hover panel that is customized for Microsoft OneNote document. |
| Item display template | PDF Item | Item_PDF | Displays search results that are customized for Portable Document Format (PDF) documents. |
| Hover panel | PDF Hover Panel | Item_PDF_HoverPanel | Displays a search result hover panel that is customized for a PDF document. |
| Item display template | People Item | Item_Person | Displays a search result that is customized for a person. |
| Item display template | People Intent Item | Item_Person_CompactHorizontal | Displays a search result that is customized for showing a person in a compact and horizontal layout. |
| Hover panel | People Hover Panel | Item_Person_HoverPanel | Displays a search result hover panel that is customized for a person. |
| Item display template | Personal Result Item | Item_PersonalFavorite | Displays a personal favorite search result. |
| Item display template | Picture Item | Item_Picture | Displays a search result that is customized for a picture. |
| Hover panel | Picture Hover Panel | Item_Picture_HoverPanel | Displays a search result hover panel that is customized for a picture. |
| Item display template | PowerPoint Item | Item_PowerPoint | Displays a search result that is customized for a Microsoft PowerPoint document. |
| Hover panel | PowerPoint Hover Panel | Item_PowerPoint_HoverPanel | Displays a search result hover panel that is customized for a Microsoft PowerPoint document. |
| Item display template | Reply Item | Item_Reply | Displays a search result that is customized for a reply in community discussions. |
| Hover panel | Reply Hover Panel | Item_Reply_HoverPanel | Displays a search result hover panel that is customized for a reply in community discussions. |
| Item display template | Site Item | Item_Site | Displays a search result that is customized for a SharePoint site. |
| Hover panel | Site Hover Panel | Item_Site_HoverPanel | Displays a search result hover panel that is customized for a SharePoint site. |
| Item display template | Video Item | Item_Video | Displays a search result that is customized for a video file. |
| Item display template | Video | Item_VideoCompactHorizontal | Displays a search result that is customized for a video file horizontal layout.  
 > [!NOTE]> The Video Hover Panel will not work with this display template |
| Hover panel | Video Hover Panel | Item_Video_HoverPanel | Displays a search result hover panel that is customized for video file. |
| Item display template | Web Page Item | Item_WebPage | Displays a search result that is customized for a web page. |
| Hover panel | Web page Hover Panel | Item_WebPage_HoverPanel | Displays a search result hover panel that is customized for a web page. |
| Item display template | Word Item | Item_Word | Displays a search result that is customized for a Microsoft Word document. |
| Hover panel | Word Hover Panel | Item_Word_HoverPanel | Displays a search result hover panel that is customized for a Microsoft Word document. |

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
