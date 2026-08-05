---
title: "Active Directory Groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1031778/active-directory-groups
question_id: 1031778
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1031778/active-directory-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All    

I have an AD group lets say TEST1 and i have a testuser1 and this user is managing the membership of this AD groups i.e add/remove members.    

Below is the settings of this group.    

Group:TEST1-Properties-ManagedBy    

Name: TestUser1    

Manager can update membership list is checked.    

I want to provide access to two more users lets say testuser2 and testuser3 to manage this AD group.    

I am following the below steps    

TEST1-security-Add the user(testuser2 & testuser3)-Advanced-    

Double click the user and  edit->give Write Members access.    

Is there any powershell syntax using which i can provide access to testuser2 and testuser2 instead of following the GUI steps( i only want to provide Write Members access i.e testuser2 and testuser3 can add/remove members)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-05*

Thanks all    

script is executed successfully but for the AD group-->right click properties-->security-->testuser1-Advanced-->Double click the user testuser1 and edit-> Write Members    

i dont see Write members box checked

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-02*

please correct me if i am wrong, i will want to make the below changes in DillonJS script. will it work for me.    

 $owner = "test.user2","test.user3";        //test.user2 and test.user3 are sAMAccountNames    

 $group = "TEST1";    

 $objectguid = [Guid]"bf9679c0-0de6-11d0-a285-00aa003049e2";     //bf9679c0-0de6-11d0-a285-00aa003049e2 is the Objectguid of the AD group TEST1

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-01*

Hi     

The ManageBy attribute is only providing a lookup or reference to who manages the groups, however, when the "Manager can update membership list" option is checked an new ACE is added to the object DACL.  DillonJS has provided a powershell script to do this, however, this is the dsacls command to do the same thing, which you can use a group to allocate the right.    

```
dsacls "" /G ":WP;member"
```

Gary.
