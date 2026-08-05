---
title: "Create a custom ranking model by using the Ranking Model Tuning App - SharePoint Server"
description: "If the standard SharePoint ranking models don't satisfy the relevance requirements you have, you can create a custom ranking model for the classic search experience. With the Ranking Model Tuning App, you can do this more easily than before. The app provides a user interface for copying an existing ranking model, judge the results for a set of queries, add or remove rank features, and adjust the weight of these features. Finally, you can evaluate the changes, and publish the new ranking model when you're satisfied with the results."
ms.topic: how-to
---
Note

Create a custom ranking model by using the Ranking Model Tuning App

# Create a custom ranking model by using the Ranking Model Tuning App

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

If the standard ranking models don't satisfy the relevance requirements you have, you can create a custom ranking model for the classic search experience. With the Ranking Model Tuning App, you can do this more easily than before. The app provides a user interface for copying an existing ranking model, judge the results for a set of queries, add or remove rank features, and adjust the weight of these features. Finally, you can evaluate the changes, and publish the new ranking model when you're satisfied with the results.

Why create a custom ranking model?

## Why create a custom ranking model?

In most cases, the ranking models in SharePoint Server provide good search result ranking, and you can also influence the ranking of search results with query rules. However, if you have a particular relevance need for search results that the standard ranking models don't provide, you can create a custom ranking model.

Here are some typical use cases:

- You have added a specific managed property that you think should influence ranking of items on your site.

Example: A food store has added a new managed property "gluten-free" and wants to include this managed property in the ranking calculations of search results.

- You want to give one or more of the managed properties in a standard ranking model more ranking weight than what it gets by default.

Example: An accountancy company wants Excel workbooks (file type) to have higher ranking weight than what they get when using the standard ranking model.

Important

Creating a custom ranking model is rather complex, and you should not take this lightly. For a good result, expect to invest time on tasks such as judging a considerable number of queries.

Learn more about ranking and ranking models:

Overview of search result ranking in SharePoint Server

Customizing ranking models to improve relevance in SharePoint

Get the app for SharePoint Server

## Get the app for SharePoint Server

Important

For SharePoint Server 2013 we recommend that you have installed the SharePoint Server 2013 cumulative update from March 2014.

Install the app and prepare the SharePoint farm to allow apps by using the same standard processes as for all SharePoint Server apps: Install and manage apps for SharePoint.

To use the app, you must be a Search service application administrator.

Create a custom ranking model-main steps

## Create a custom ranking model-main steps

- Click the app icon  to go to the starting page of the app.

Follow these main steps to create a custom ranking model. Expect to go back and forth between the different steps as you fine-tune your model.

Step 1: Copy an existing ranking model and give it a name

Step 2: Add a judgment set

Step 3: Judge the results for the queries in the set

Step 4: Add rank features and tune the weight

Step 5: Evaluate the changes

Step 6: Publish the ranking model

Step 1: Copy an existing ranking model and give it a name

## Step 1: Copy an existing ranking model and give it a name

When you start the app, you see a list of all available ranking models. On first use, this will be the set of standard ranking models delivered with SharePoint. These ranking models are marked with **Base model**, and the only action allowed, is to  *copy*  . To create a custom ranking model, you copy an existing model and then modify the copy. Any models created by using the app are marked with **Not base model**, and these you can also  *edit*,  *publish*, or  *delete*.

Most standard ranking models delivered with SharePoint have a linear stage and a neural stage. With this app, you can only customize the linear stage of a ranking model, as a linear stage is easier to tune and customize.

We recommend that you use the **Search Ranking Model with Two Linear Stages** as the basis for your custom ranking model, then it will be easier to re-tune and customize your ranking model.

In the list of existing ranking models, select the model you want to copy.

Click the arrow to the right and select **Copy**.

On the **Edit ranking model** page, type a name for your new ranking model.

Select the result source you want to test queries against.

Step 2: Add a judgment set

## Step 2: Add a judgment set

You can add one or more judgment sets to your ranking model. A judgment set typically consists of queries that are popular, queries that are important for the business, or queries that the current ranking model doesn't handle sufficiently well. On the **Edit ranking model** page, under **Judge queries**, choose **Add judgment set**.

- On the **Edit judgment set** page, choose one or more of these options:

| **Option** | **Description** |
| --- | --- |
| Import judged queries | If you already have a set of queries and labels for documents returned for the queries, you can import them. Choose the file to upload, and then click **Import queries**.  
 The import file must be of type XML with the following schema:  
 `  <QuerySet Name="testRM - JudgementSet"><Query QueryString="query1" ><Judgements><Document Url="docUrl1" Label="Excellent" /><Document Url="docUrl2" Label="Good" /><Document Url="docUrl3" Label="Fair" /><Document Url="docUrl4" Label="Bad" /></Judgements></Query></QuerySet>`You can use four labels to indicate how desirable a result is for a query: **Excellent**, **Good**, **Fair**, and **Bad**. |
| Add sampled queries | If search has been active on the site, you can have the app pick a random set of queries from the existing query logs. The app will choose the queries that are more popular.  
 Specify the number of queries to sample in the box, and click **Add queries**. |
| Add queries manually | Type queries directly in the app, one query per line, and then click **Add queries**.  
 You can add all queries this way, or you can manually add more queries to an existing set of queries. |

- If you imported judged queries with labels, click **Done** to save the judgment set. If you added queries from the query log or manually, you can start judging the queries, see step 3.

To ensure that the relevance metrics are reliable indicators for how good the ranking model is for a particular site, make sure that:

There are sufficient queries in the judgment set. The more queries, and the more judged documents in the top 10 for these queries, the better.

There is a representative mix from the range of queries you expect to have.

Step 3: Judge the results for the queries in the set

## Step 3: Judge the results for the queries in the set

Now, go through all queries and evaluate the results for each one. Determine how relevant or desirable a particular document in the index is as a search result for the specific query. The more relevant or desirable you think a document is, the higher in the ranked list it is expected to be.

Note

If you imported already judged queries in the previous step, results already have a rating, and you can skip this step.

On the **Edit judgment set** page, for each query, click the query text and choose **Judge results**.

On the **Evaluate query** page, you see two sets of results side by side: **Results with base model** and **Results with current model**. Before you make any changes to your new ranking model, the two result sets will be the same.

For each result, evaluate the result and give it a rating (label) by choosing the number of stars, from one to five. The one star option, "Broken link," can be used for documents you can't access.

After you've made the first round of changes to the ranking model, you can compare two result sets side by side in this view. Compare the current ranking model with the base model or with the last saved version of the new model. This way you can evaluate the effect of the different customizations you've made.

When you've rated the results for a query, click **Next query** to continue through the judgment set.

Click **Done** to save the set.

When you've gone through and evaluated the queries in the judgment set, you'll see the judgment coverage for that set. After you've made changes to the model, you can see how much relevance has improved with the new ranking model for the different judgment sets.

| **This column** | **Shows the following information** |
| --- | --- |
| Query text | The queries in the judgment set. |
| Judgment coverage | The percentage of document URLs in the current top ten that have been rated.  
 **NOTE:** Relevance metrics are only reliable when the judgment coverage is high. To increase coverage, judge more of the results for the query. |
| Relevance vs. Base ranking | After you've made changes to the ranking model, this figure shows how much relevance has improved for the query with the new ranking model compared to the base model. If the score is 0.00%, there's no difference between the two models for that query. If the score is negative, relevance has decreased. |
| Vs. Saved model | The app keeps a draft version of the ranking model while you work on it. You can compare the current draft version to the last saved version of the new ranking model.  
 This figure shows how much relevance has improved or decreased with the current draft of the model compared to the last saved version. |

The metric of relevance used in the app is "Discounted Cumulative Gain" calculated for the top five results.

Step 4: Add rank features and tune the weight

## Step 4: Add rank features and tune the weight

When you copy an existing ranking model, the new ranking model contains the same rank features and weights as in the base model. You can add more managed properties as additional rank features, remove existing features, or tune the weight of existing features.

Note

You can only choose managed properties that have already been created and configured. Managing managed properties, such as creating new ones or setting them to be searchable or sortable, is out of scope for this app.

Step 4a: Add rank features

### Step 4a: Add rank features

On the **Edit ranking model** page, under **Add and tune features**, click **Add features to customize**.

On the **Add a ranking feature to customize** page, choose between these types of rank features:

| **Ranking feature type** | **Description** |
| --- | --- |
| Suggested feature based on judged queries | The app can suggest features to add when feature vectors have been extracted for a sufficient number of judged documents. Suggestions will be rank features that have a strong correlation (negative or positive) with the relevance jugdements provided by the automated tuning. This option is only available after you have run automated tuning on this ranking model at least once. See more about automated tuning later in this article. |
| Searchable text managed property | Choose a managed property to be used in the search result ranking calculations.  
 If you select that proximity of query terms in the property value is important, you can later enter a Proximity weight for the feature. The app uses the variants isExact=1 and isDiscounted=1. |
| Sortable numeric managed property | Also called static rank feature.  
 The managed property must be of type Integer. The app uses the Rational transform.  
 Choose a managed property, and enter a default value for the property. The default value will be used if an item doesn't have a value explicitly set. |
| Sortable property with a specific value | Also called bucketed static rank feature. Choose a managed property, and enter the default value for the property.  
 **Having value**: This number is the specific bucket that is being tuned. |
| Ranking feature from the base model | Use this option to tune the weight of existing features. Choose between existing rank features. |

- Click **Add feature**. Repeat steps to add more features to customize. The selected rank features are shown on the **Edit ranking model** page.

You can also remove features from the model.

Read more about rank features and aggregation of rank features in Customizing ranking models to improve relevance in SharePoint.

Step 4b: Tune the weights

### Step 4b: Tune the weights

Initially, new features have a zero weight, except existing rank features from the base model. To give rank features a different weigth, you can use automated tuning or manual tuning.

**Automated tuning**:

With automated tuning, the judgments provided for your judgment set are used to automatically set the weight of features in a way that attempts to maximize relevance. The auto-tune option is available when you have at least 10 queries with at least 10 judgments each. The more judgments you have, the more reliable the automatic tuning will be.

On the **Automated tuning** tab, click the **Autotune weights** button.

Note

The autotune option includes a considerable amount of computation, and may take around 5 minutes for a judgment set of 10 queries.

**Manual tuning**:

With manual tuning, you can set or change weights of individual rank features. Avoid very large values (negative or positive).

On the **Manual tuning** tab, set or change the weight for a feature by entering or changing a value in the **Weight** box.

Click **Save weights** to run evaluation on all judgment sets associated with this model.

Evaluate changes, see step 5.

Step 5: Evaluate the changes

## Step 5: Evaluate the changes

The app lets you evaluate how a custom ranking model changes relevance. This is especially useful for queries that you consider *important*.

Important

When you create a custom ranking model, this influences all the queries using that ranking model. Test the effect of the custom ranking model on many queries.

Type queries in the **Sample query** box below the **Manual tuning** list to see the results for a specific query. You can compare results with the base model  *or*  the last saved model to the left, and results with the current model to the right. You can also add queries to a judgment set from this page if you want to.

You can also evaluate the effect of a particular setting by running an evaluation on a judgment set. In the list of judgment sets under **Judge queries**, click the arrow to the right of the set, and choose **Evaluate relevance** from the menu.

Note

Changing the weight of a rank feature will affect the ordering of results, hopefully to provide improved relevance. As a result of the re-ordering, new documents that are not yet judged may enter the top 10 results for a query. If this happens, the **judgment coverage** value will go down for a judgment set, and you may have to provide additional judgments.

- When you are done adding, removing, and tuning features, save your changes. The new custom ranking model is shown in the list of available ranking models that you started off with. It is marked as **Not base model**.

Step 6: Publish the ranking model

## Step 6: Publish the ranking model

The new ranking model is by default available for the site where you added the app. If you want to use your custom ranking model more broadly, you must publish it.

In the **Select ranking model** list, click the arrow to the right, and choose **Publish** from the menu.

Choose one of the following:

Current site (available by default)

Current site collection

**All site collections** (the whole Search Service Application)

- Click **Publish**.

When you publish your ranking model, you'll get a GUID that identifies the ranking model. You can use the GUID in search, for example when configuring the **Search Results Web Part**, or to programmatically set the **RankingModelId** property of a query.

More info about ranking and ranking models

## More info about ranking and ranking models

Overview of search result ranking in SharePoint Server

Customizing ranking models to improve relevance in SharePoint Server

Manage query rules in SharePoint Server

Configure properties of the Search Results Web Part in SharePoint Server

Manage the search schema in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2021-11-02
