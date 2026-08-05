---
title: "Issue with Microsoft Azure Active Directory single sign-on for JIRA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3719716/issue-with-microsoft-azure-active-directory-single
question_id: 3719716
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Issue with Microsoft Azure Active Directory single sign-on for JIRA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3719716/issue-with-microsoft-azure-active-directory-single (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

We have uploaded latest JIRA Microsoft JIRA plugin which is showing version as 1.0.6. However, after installing it it is shown as 1.0.9 and we could see some issues like Project Settings page is showing blank
 page and workflow page is showing blank.

https://www.microsoft.com/en-us/download/details.aspx?id=56506

=================================================================

ERROR:

Uncaught ReferenceError: getQueryVariable is not defined  

at HTMLDocument. (batch.js?agile_global_admin_condition=true&healthcheck-resources=true&jag=true&jaguser=true&jmbonb=1&locale=en-US:2038)  

at c (batch.js?locale=en-US:65)  

at Object.fireWith [as resolveWith] (batch.js?locale=en-US:65)  

at Function.ready (batch.js?locale=en-US:65)  

at HTMLDocument.H (batch.js?locale=en-US:65)

/* module-key = 'com.microsoft.MSSsoJiraPlugin:admin-resources1.0.9', location = '/js/JiraSSOLogoutAction.js' */  

AJS.$(function(){var a=getQueryVariable("atl_token");console.log("ServiceDesk url found.....atl_token: "+a);AJS.$(document).ready(function(){setTimeout(function(){if(AJS.$("#log_out").length){var b=getCookie("atlassian.xsrf.token");AJS.$("#log_out").attr("href",AJS.contextPath()+"/plugins/servlet/saml/logout?atl_token="+b)}if(AJS.$(".js-logout").length){console.log("ServiceDesk
 url found");var b=getCookie("atl_token");if(!b){b=getCookie("atlassian.xsrf.token")}getGlobalLogoutValue(b);AJS.$(".js-logout").unbind("click");AJS.$(".js-logout").attr("href",AJS.contextPath()+"/plugins/servlet/saml/logout?atl_token="+b)}},4000)})});function
 getCookie(d){var b=d+"=";var f=decodeURIComponent(document.cookie);var a=f.split(";");for(var e=0;e<a.length;e++){var g=a[e];while(g.charAt(0)==" "){g=g.substring(1)}if(g.indexOf(b)==0){return g.substring(b.length,g.length)}}return""}function getGlobalLogoutValue(a){AJS.$.ajax({url:AJS.contextPath()+"/plugins/servlet/saml/getLoginButtonConfFields",type:"GET",success:function(b){if(b!=""){var
 c=getResponseValueOfForceAzureLogin(b,"isForceAzureLogin");if(c!="on"){AJS.$(".js-logout").bind("click",function(){console.log("User clicked on logout ");AJS.$.ajax({url:AJS.contextPath()+"/servicedesk/customer/user/logout?atl_token="+a,type:"GET",success:function(d){console.log("Succusfully
 local logout completed");window.location.href=AJS.contextPath()+"/plugins/servlet/saml/logout"},error:function(d,f,e){console.log("Something really bad happened while ServiceDesk logOut "+f)}})})}}},error:function(b,d,c){console.log("Something really bad happened
 "+d)}})}function getResponseValueOfForceAzureLogin(b,a){console.log("parameterName :"+a);var c=b.split("~");if(a=="isForceAzureLogin"){console.log("isForceAzureLogin :"+c[1]);return c[1]}};;

===========================================  

1 hour back we have downloaded version 1.0.11 and uploaded. Still we can see the same issues and version is showing as 1.0.9 only.

Could you please check and update.

Regards,  

Prasanna

* Moved from Garage

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-04*

This consumer oriented community is not the place for a technical question like this.

You might try The Atlassian Community https://community.atlassian.com/

Or the appropriate Windows Server forum at TechNet https://social.technet.microsoft.com/Forums/en-us/home 

Don
