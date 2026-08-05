---
title: "Add, edit, or delete custom properties in SharePoint Server user profiles - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-add-edit-or-delete-custom-properties-for-a-user-profile
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/add-edit-or-delete-custom-properties-for-a-user-profile
family: administration
documentKind: "article"
abstract: "Learn how to create, edit, and delete user profile properties in SharePoint Server."
---

# Add, edit, or delete custom properties in SharePoint Server user profiles - SharePoint Server

Note

Add, edit, or delete custom properties in SharePoint Server user profiles

# Add, edit, or delete custom properties in SharePoint Server user profiles

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The **Manage Profile Service** page of a User Profile service application in SharePoint Server is a central location for managing available user profile properties and creating new properties. You need to be a member of the Farm Administrators SharePoint group or a Service Application Administrator for the User Profile service application to make changes.

You can supplement default user profile properties with additional properties to track key information that is not otherwise available. Key business needs might encourage you to create new properties that associate users with important business processes. For example, a sales department can create a specific sales role property to share with a particular audience or audiences. Custom user profile properties can be edited to better suit business needs or they can be deleted when no longer needed.

Add a user profile property

## Add a user profile property

Perform the following procedure to create a user profile property.

**To create a new user profile property**

On Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the link for the User Profile service application.

On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.

On the **Manage User Profile Properties** page, click **New Property**.

On the **Add User Profile Property** page, in the **Property Settings** section, in the **Name** text box, type a name to be used by the User Profile service application for the user profile property.

In the **Property Settings** section, in the **Display Name** box, type the user profile property name that will be displayed to all users.

Note

If you use multiple languages in your deployment, you can provide alternative display names for each language by clicking **Edit Languages**. In the dialog, click **Add Language**, select a language from the menu, and then type the display name in the new language. You can add display names for any of the available languages. The display name that appears depends on the language of the operating system on the computer of the user who views the property.

On the **Type** drop-down list, click the data type for the property.

Note

If you select **string (Multi Value)**, the property will be permanently set as a multivalued property. You cannot change this setting after you click **OK**. You can only delete the property and add it again as a new single value property.

In the **Length** box, type the maximum number of characters that are allowed for values for this property.

Click to select **Configure a Term Set to be used for this property** to associate the profile property with a managed metadata term set and select a term set from the drop-down list.

In the **Sub-type of Profile** section, select the **Default User Profile Subtype** to associate the default user profile subtype with this user profile property.

In the **User Description** section, in the **Description** box, type the instructions or information that is displayed to users about this user profile property.

Note

If you use multiple languages in your deployment, you can provide alternative display names for each language by clicking **Edit Languages**. In the dialog, click **Add Language**, select a language from the menu, and then type the display name in the new language. You can add display names for any of the available languages. The display name that appears depends on the language of the operating system on the computer of the user who views the property.

In the **Policy Settings** section, select the policy setting and default privacy setting that you want for this property. Click to select **User can override box** to enable users to override these settings.

In the **Edit Settings** section, select whether users can edit values for this property.

In the **Display Settings** section, specify if and how the property will be viewed by users.

In the **Search Settings** section, select the **Alias** check box, the **Indexed** check box, or both, depending on the kinds of searches that you want to be associated with this user profile property.

Note

The **Alias** check box is unavailable unless the **Default Privacy Setting** is set to "Everyone".

Note

If you mark a property as indexed, a search for values of that property returns that user profile. For example, if the  *telephone number* property is indexed, a search of telephone numbers finds the employee with that number. If you mark a property as aliased, the property is a suitable alias for this user. For example, if you search for all documents by John Kane, the result returns documents that were written by johnkane@contoso.com and Jonathan Kane if profile properties are marked with those values as aliases.

In the **Property Mapping for Synchronization** section, click **Remove** to delete or change an existing mapping.

In the **Add new Mapping** section, specify the source data connection, attribute, and synchronization direction for the mapping. When you are finished, click **Add**.

Click **OK**.

Edit a user profile property

## Edit a user profile property

Perform the following procedure to edit a user profile property.

**To edit a user profile property**

On Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the link for the User Profile service application.

On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.

On the **Manage User Profile Properties** page, in the **Property Name** column, select the user profile property that you want to change, and then, in the dropdown menu, click **Edit**.

On the **Edit User Profile Property** page, locate the element or elements of the user profile property that you want to change and edit them.

When you are finished, click **OK**.

Delete a user profile property

## Delete a user profile property

Perform the following procedure to delete a user profile property.

**To delete a user profile property profile property by using Central Administration**

On Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.

On the **Manage User Profile Properties** page, in the **Property Name** column, select the user profile property that you want to remove, and then, in the dropdown menu, click **Delete**.

In the dialog, verify that you have selected the correct user profile property, and then click **OK**.

See also

## See also

Concepts

#### Concepts

Administer the User Profile service in SharePoint Server

Plan profile synchronization for SharePoint Server 2013

User Profile service overview

Other Resources

#### Other Resources

Delegate administration of User Profile service applications or features in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
