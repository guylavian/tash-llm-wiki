---
title: "Identify users and analyze document usage in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-identify-users-and-analyze-document-usage
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/identify-users-and-analyze-document-usage
family: governance
documentKind: "article"
abstract: "Learn how to collect information about document users to plan your SharePoint Server document management solution."
---

# Identify users and analyze document usage in SharePoint Server - SharePoint Server

Note

Identify users and analyze document usage in SharePoint Server

# Identify users and analyze document usage in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The first step to plan your document management solution is to identify users and analyze how documents are used. This article contains guidance to identify users and analyze document usage for your solution that is based on SharePoint Server.

Identify users

## Identify users

To identify the stakeholders and participants in your document management solution, you can use a survey to collect information. For example, your survey might contain the following questions:

Who in your organization creates documents?

What kinds of documents do they create?

What role does the user of the document have?

Who reviews documents?

Who edits documents?

Who uses documents?

Who approves the publication of documents?

Who designs websites used for hosting documents?

Who sets guidelines and policies for managing documents?

Who manages records in your organization?

Who deploys and maintains the servers on which documents are stored?

Identifying content stakeholders can help you make sure that your document management solution is comprehensive and that you design sites and document libraries that suit your enterprise's content needs and processes.

Analyze document usage

## Analyze document usage

After you identify your content stakeholders, collect information from them that will help you analyze how documents are used in your organization. This is an important part of the planning process because the analysis helps you determine:

How document libraries should be structured.

Which SharePoint site templates to use.

How many SharePoint sites you need.

Which physical server topology you must have to implement your solution.

Which information management policies to apply to the sites.

Note

Information management policies are not available in SharePoint Foundation 2013.

What information to collect?

### What information to collect?

The information to collect for document usage analysis includes:

Document type, such as equity research note, employee performance review, internal memo, or product specification.

The purpose of each document type, such as "gives customers recommendations about equities together with supporting data."

The author of each document type (it is helpful to list the role of the author — such as "financial analyst or "product manager" — instead of individual names).

The users of each document type, such as "customers" or "team members."

The format of the document. If the document has to be converted from one format to another at any point in its life cycle, record that information.

Other roles that apply to the document's life cycle, such as "technical reviewer" or "copy editor."

Location of the document, such as "client computer," "web server," or "file server." This question could have multiple answers, for example when a document is authored on a client computer and then published to a web server.

The following are examples of information that might be collected and recorded in the worksheet from two different organizations in an enterprise.

Information collection table: Example with research information

#### Information collection table: Example with research information

| **Type** | **Purpose** | **Author** | **User role** | **Format** | **Other roles** | **Location** |
| --- | --- | --- | --- | --- | --- | --- |
| Equity research note | Gives premium customers of a financial service guidance on whether to buy or sell one or more stocks | Financial analyst | Customer | DOCX (for authoring); PDF (for publishing) | Reviewer (technical); reviewer (legal); approver; copy editor; site administrator | Authoring site  
  Testing site |

Analysis outcome for the example with research information

##### Analysis outcome for the example with research information

The separate authoring and publishing formats require a format conversion. The large number of reviewers requires one or more workflows (business processes implemented on the server). The two sites (authoring and testing) require mechanisms for moving the content from one site to another.

Information collection table: Example with employee information

#### Information collection table: Example with employee information

| **Type** | **Purpose** | **Author** | **User role** | **Format** | **Other roles** | **Location** |
| --- | --- | --- | --- | --- | --- | --- |
| Employee performance review | Evaluates the performance of an employee — including self-evaluation and manager's evaluation | Information worker; manager | Managers; human resources specialists | DOCX | Reviewer (human resources); reviewer (legal); approver (upper manager); records manager | Client computer  
  E-mail server (as attachment)  
  Corporate web server  
  Corporate records center |

Analysis outcome for the example with employee information

##### Analysis outcome for the example with employee information

Two authors and multiple reviewers require one or more workflows. Many people handle the document, then is located in a corporate web server (assumed to be highly secure) and is managed in place or moved to a records center. The sensitive nature of this content requires Information Rights Management (IRM) on the desktops and servers, in addition to corporate policies and best practices (such as auditing) that protect the employee's privacy and the enterprise's legal standing.

Note

The records center is not available in SharePoint Foundation 2013.

Worksheets

## Worksheets

Use the following worksheets to record the information discussed in this article:

Document management participants worksheet

Analyze document usage worksheet

Additional resources

## Additional resources

- Last updated on 
		2025-12-19
