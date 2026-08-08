---
title: "How to use this documentation — pages 2321-2360"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2321-2360
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2321-2360
family: powershell
documentKind: "doc"
abstract: "Last updated on 05/20/2025 List View (GroupBy) This example shows how to implement a list view that separates the rows of the list into groups. This list view displays the properties of the System.ServiceProcess.ServiceController objects returned by the Get-Service cmdlet. For m"
---

# How to use this documentation — pages 2321-2360

<!-- p.2321 -->

Last updated on 05/20/2025

<!-- p.2322 -->

List View (GroupBy)
This example shows how to implement a list view that separates the rows of the list into
groups. This list view displays the properties of the System.ServiceProcess.ServiceController
objects returned by the Get-Service cmdlet. For more information about the components of a
list view, see Creating a List View.

Load this formatting file
   1. Copy the XML from the Example section of this topic into a text file.

   2. Save the text file. Be sure to add the format.ps1xml extension to the file to identify it as a
     formatting file.

   3. Open Windows PowerShell, and run the following command to load the formatting file
     into the current session: Update-FormatData -PrependPath PathToFormattingFile .

  ２ Warning

  This formatting file defines the display of an object that is already defined by a Windows
  PowerShell formatting file. You must use the PrependPath parameter when you run the
  cmdlet, and you cannot load this formatting file as a module.

Demonstrates
This formatting file demonstrates the following XML elements:

     The Name element for the view.

     The ViewSelectedBy element that defines what objects are displayed by the view.

     The GroupBy element that defines how a new group of objects is displayed.

     The ListControl element that defines what property is displayed by the view.

     The ListItem element that defines what is displayed in a row of the list view.

     The PropertyName element that defines which property is displayed.

<!-- p.2323 -->

Example
The following XML defines a list view that starts a new group whenever the value of the
System.ServiceProcess.ServiceController.Status property changes. When each group is started,
a custom label is displayed that includes the new value of the property.

 XML

 <Configuration>
   <ViewDefinitions>
     <View>
       <Name>System.ServiceProcess.ServiceController</Name>
       <ViewSelectedBy>
         <TypeName>System.ServiceProcess.ServiceController</TypeName>
       </ViewSelectedBy>
       <GroupBy>
         <PropertyName>Status</PropertyName>
         <Label>New Service Status</Label>
       </GroupBy>
       <ListControl>
         <ListEntries>
           <ListEntry>
             <ListItems>
               <ListItem>
                 <PropertyName>Name</PropertyName>
               </ListItem>
               <ListItem>
                 <PropertyName>DisplayName</PropertyName>
               </ListItem>
               <ListItem>
                 <PropertyName>ServiceType</PropertyName>
               </ListItem>
             </ListItems>
           </ListEntry>
         </ListEntries>
       </ListControl>
     </View>
   </ViewDefinitions>
 </Configuration>

The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController objects after this format file is loaded. The blank lines
added before and after the group label are automatically added by Windows PowerShell.

 PowerShell

 Get-Service f*

<!-- p.2324 -->

 Output

     New Service Status: Stopped

 Name        : Fax
 DisplayName : Fax
 ServiceType : Win32OwnProcess

     New Service Status: Running

 Name        : FCSAM
 DisplayName : Microsoft Antimalware Service
 ServiceType : Win32OwnProcess

     New Service Status: Stopped

 Name        : fdPHost
 DisplayName : Function Discovery Provider Host
 ServiceType : Win32ShareProcess

     New Service Status: Running

 Name        : FDResPub
 DisplayName : Function Discovery Resource Publication
 ServiceType : Win32ShareProcess

 Name        : FontCache
 DisplayName : Windows Font Cache Service
 ServiceType : Win32ShareProcess

     New Service Status: Stopped

 Name        : FontCache3.0.0.0
 DisplayName : Windows Presentation Foundation Font Cache 3.0.0.0
 ServiceType : Win32OwnProcess

     New Service Status: Running

 Name        : FSysAgent
 DisplayName : Microsoft Forefront System Agent
 ServiceType : Win32OwnProcess

 Name        : FwcAgent
 DisplayName : Firewall Client Agent
 ServiceType : Win32OwnProcess

See Also
Examples of Formatting Files

Writing a PowerShell Formatting File

<!-- p.2325 -->

Last updated on 05/20/2025

<!-- p.2326 -->

Format Schema XML Reference
The topics in this section describe the XML elements used by formatting files (Format.ps1xml
files). Formatting files define how the .NET object is displayed; they do not change the object
itself.

In This Section
Alignment Element for TableColumnHeader for TableControl (Format) Defines how the data in a
column header is displayed.

Alignment Element for TableColumnItem for TableControl (Format) Defines how the data in the
row is displayed.

AutoSize Element for TableControl (Format) Specifies whether the column size and the number
of columns are adjusted based on the size of the data.

Autosize Element for WideControl (Format) Specifies whether the column size and the number
of columns are adjusted based on the size of the data.

ColumnNumber Element for WideControl (Format) Specifies the number of columns displayed
in the wide view.

Configuration Element (Format) Represents the top-level element of the formatting file.

Control Element for Controls for Configuration (Format) Defines a common control that can be
used by all the views of the formatting file and the name that is used to reference the control.

Control Element for Controls for View (Format) Defines a control that can be used by the view
and the name that is used to reference the control.

Controls Element for Configuration (Format) Defines the common controls that can be used by
all views of the formatting file.

Controls Element for View (Format) Defines the view controls that can be used by a specific
view.

CustomControl Element for Control for Configuration (Format) Defines a control. This element
is used when defining a common control that can be used by all the views in the formatting
file.

<!-- p.2327 -->

CustomControl Element for Control for Controls for View (Format) Defines a control that is
used by the view.

CustomControl Element for GroupBy (Format) Defines the custom control that displays the new
group.

CustomControl Element (Format) Defines a custom control format for the view.

CustomControlName Element for ExpressionBinding for Controls for Configuration (Format)
Specifies the name of a common control. This element is used when defining a common
control that can be used by all the views in the formatting file.

CustomControlName Element for ExpressionBindine for Controls for View (Format) Specifies
the name of a common control or a view control. This element is used when defining controls
that can be used by a view.

CustomControlName Element of GroupBy (Format) Specifies the name of a custom control that
is used to display the new group. This element is used when defining a table, list, wide or
custom control view.

CustomEntry Element for CustomControl for Controls for Configuration (Format) Provides a
definition of the common control. This element is used when defining a common control that
can be used by all the views in the formatting file.

CustomEntry Element for CustomEntries for Controls for View (Format) Provides a definition of
the control. This element is used when defining controls that can be used by a view.

CustomEntry Element for CustomEntries for View (Format) Provides a definition of the custom
control view.

CustomEntry Element for CustomControl for GroupBy (Format) Provides a definition of the
control. This element is used when defining how a new group of objects is displayed.

CustomEntries Element for CustomControl for Configuration (Format) Provides the definitions
of a common control. This element is used when defining a common control that can be used
by all the views in the formatting file.

CustomEntries Element for CustomControl for Controls for View (Format) Provides the
definitions for the control. This element is used when defining controls that can be used by a
view.

<!-- p.2328 -->

CustomEntries Element for CustomControl for GroupBy (Format) Provides the definitions for
the control. This element is used when defining how a new group of objects is displayed.

CustomEntries Element for CustomControl for View (Format) Provides the definitions of the
custom control view. The custom control view must specify one or more definitions.

CustomItem Element for CustomEntry for Controls for Configuration Defines what data is
displayed by the control and how it is displayed. This element is used when defining a common
control that can be used by all the views in the formatting file.

CustomItem Element for CustomEntry for Controls for View (Format) Defines what data is
displayed by the control and how it is displayed. This element is used when defining controls
that can be used by a view.

CustomItem Element for CustomEntry for View (Format) Defines what data is displayed by the
custom control view and how it is displayed. This element is used when defining a custom
control view.

CustomItem Element for CustomEntry for GroupBy (Format) Defines what data is displayed by
the custom control view and how it is displayed. This element is used when defining how a new
group of objects is displayed.

DefaultSettings Element (Format) Defines common settings that apply to all the views of the
formatting file. Common settings include displaying errors, wrapping text in tables, defining
how collections are expanded, and more.

DisplayError Element (Format) Specifies that the string #ERR is displayed when an error occurs
displaying a piece of data.

EntrySelectedBy Element for CustomEntry for Controls for Configuration (Format) Defines the
.NET types that use the definition of the common control or the condition that must exist for
this control to be used. This element is used when defining a common control that can be used
by all the views in the formatting file.

EntrySelectedBy Element for CustomEntry for Controls for View (Format) Defines the .NET types
that use this control definition or the condition that must exist for this definition to be used.
This element is used when defining controls that can be used by a view.

EntrySelectedBy Element for CustomEntry for View (Format) Defines the .NET types that use
this custom entry or the condition that must exist for this entry to be used.

<!-- p.2329 -->

EntrySelectedBy Element for EnumerableExpansion (Format) Defines the .NET types that use
this definition or the condition that must exist for this definition to be used.

EntrySelectedBy Element for CustomEntry for GroupBy (Format) Defines the .NET types that use
this control definition or the condition that must exist for this definition to be used. This
element is used when defining how a new group of objects is displayed.

EntrySelectedBy Element for ListEntry for ListControl (Format) Defines the .NET types that use
this list view definition or the condition that must exist for this definition to be used. In most
cases only one definition is needed for a list view. However, you can provide multiple
definitions for the list view if you want to use the same list view to display different data for
different objects.

EntrySelectedBy Element for TableRowEntry (Format) Defines the .NET types whose property
values are displayed in the row.

EntrySelectedBy Element for WideEntry (Format) Defines the .NET types that use this definition
of the wide view or the condition that must exist for this definition to be used.

EnumerableExpansion Element (Format) Defines how specific .NET collection objects are
expanded when they are displayed in a view.

EnumerableExpansions Element (Format) Defines how .NET collection objects are expanded
when they are displayed in a view.

EnumerateCollection Element for ExpressionBinding for Controls for Configuration (Format)
Specified that the elements of collections are displayed by the control. This element is used
when defining a common control that can be used by all the views in the formatting file.

EnumerateCollection Element for ExpressionBinding for Controls for View (Format) Specified
that the elements of collections are displayed. This element is used when defining controls that
can be used by a view.

EnumerateCollection Element for Expression Binding for CustomControl for View (Format)
Specifies that the elements of collections are displayed. This element is used when defining a
custom control view.

EnumerateCollection Element for ExpressionBinding for GroupBy (Format) Specifies that the
elements of collections are displayed. This element is used when defining how a new group of
objects is displayed.

Expand Element (Format) Specifies how the collection object is expanded for this definition.

<!-- p.2330 -->

ExpressionBinding Element for CustomItem for Controls for Configuration (Format) Defines the
data that is displayed by the control. This element is used when defining a common control
that can be used by all the views in the formatting file.

ExpressionBinding Element for CustomItem for Controls for View (Format) Defines the data that
is displayed by the control. This element is used when defining controls that can be used by a
view.

ExpressionBinding Element for CustomItem for CustomControl for View (Format) Defines the
data that is displayed by the control. This element is used when defining a custom control view.

ExpressionBinding Element for CustomItem for GroupBy (Format) Defines the data that is
displayed by the control. This element is used when defining how a new group of objects is
displayed.

FirstLineHanging Element for Frame for Controls for Configuration (Format) Specifies how
many characters the first line of data is shifted to the left. This element is used when defining a
common control that can be used by all the views in the formatting file.

FirstLineHanging Element of Frame of Controls of View (Format) Specifies how many characters
the first line of data is shifted to the left. This element is used when defining controls that can
be used by a view.

FirstLineHanging Element for Frame for CustomControl for View (Format) Specifies how many
characters the first line of data is shifted to the left. This element is used when defining a
custom control view.

FirstLineHanging Element for Frame for GroupBy (Format) Specifies how many characters the
first line of data is shifted to the left. This element is used when defining how a new group of
objects is displayed.

FirstLineIndent Element for Frame for Controls for Configuration (Format) Specifies how many
characters the first line of data is shifted to the right. This element is used when defining a
common control that can be used by all the views in the formatting file.

FirstLineIndent Element of Frame of Controls of View (Format) Specifies how many characters
the first line of data is shifted to the right. This element is used when defining controls that can
be used by a view.

FirstLineIndent Element Specifies how many characters the first line of data is shifted to the
right. This element is used when defining a custom control view.

<!-- p.2331 -->

FirstLineIndent Element for Frame for GroupBy (Format) Specifies how many characters the first
line of data is shifted to the right. This element is used when defining how a new group of
objects is displayed.

FormatString Element for ListItem (Format) Specifies a format pattern that defines how the
property or script value is displayed.

FormatString Element for TableColumnItem (Format) Specifies a format pattern that defines
how the property or script value of the table is displayed.

FormatString Element for WideItem for WideControl (Format) Specifies a format pattern that
defines how the property or script value is displayed in the view.

Frame Element for CustomItem for Controls for Configuration (Format) Defines how the data is
displayed, such as shifting the data to the left or right. This element is used when defining a
common control that can be used by all the views in the formatting file.

Frame Element for CustomItem for Controls for View (Format) Defines how the data is
displayed, such as shifting the data to the left or right. This element is used when defining
controls that can be used by a view.

Frame Element for CustomItem for CustomControl for View (Format) Defines how the data is
displayed, such as shifting the data to the left or right. This element is used when defining a
custom control view.

Frame Element for CustomItem for GroupBy (Format) Defines how the data is displayed, such
as shifting the data to the left or right. This element is used when defining how a new group of
objects is displayed.

GroupBy Element for View (Format) Defines how Windows PowerShell displays a new group of
objects.

HideTableHeaders Element (Format) Specifies that the headers of the table are not displayed.

ItemSelectionCondition Element for ExpressionBinding for Controls for Configuration (Format)
Defines the condition that must exist for this control to be used. This element is used when
defining a common control that can be used by all the views in the formatting file.

ItemSelectionCondition Element of ExpressionBinding for Controls for View (Format) Defines
the condition that must exist for this control to be used. This element is used when defining
controls that can be used by a view.

<!-- p.2332 -->

ItemSelectionCondition Element for Expression Binding for CustomControl for View (Format)
Defines the condition that must exist for this control to be used. There is no limit to the
number of selection conditions that can be specified for a control item. This element is used
when defining a custom control view.

ItemSelectionCondition Element for ExpressionBinding for GroupBy (Format) Defines the
condition that must exist for this control to be used. There is no limit to the number of
selection conditions that can be specified for a control item. This element is used when
defining how a new group of objects is displayed.

ItemSelectionCondition Element for ListItem (Format) Defines the condition that must exist for
this list item to be used.

Label Element for ListItem for ListControl(Format) Specifies the label for the property or script
value in the row.

Label Element for GroupBy (Format) Specifies a label that is displayed when a new group is
encountered.

Label Element for TableColumnHeader (Format) Defines the label that is displayed at the top of
a column.

LeftIndent Element for Frame for Controls for Configuration (Format) Specifies how many
characters the data is shifted away from the left margin. This element is used when defining a
common control that can be used by all the views in the formatting file.

LeftIndent Element of Frame of Controls of View (Format) Specifies how many characters the
data is shifted away from the left margin. This element is used when defining controls that can
be used by a view.

LeftIndent Element for Frame for CustomControl for View (Format) Specifies how many
characters the data is shifted away from the left margin. This element is used when defining a
custom control view.

LeftIndent Element for Frame for GroupBy (Format) Specifies how many characters the data is
shifted away from the left margin. This element is used when defining how a new group of
objects is displayed.

ListControl Element (Format) Defines a list format for the view.

ListEntry Element (Format) Provides a definition of the list view.

<!-- p.2333 -->

ListEntries Element (Format) Defines how the rows of the list view are displayed.

ListItem Element (Format) Defines the property or script whose value is displayed in a row of
the list view.

ListItems Element (Format) Defines the properties and scripts that are displayed in the list view.

Name Element for Control for Controls for Configuration (Format) Specifies the name of the
control. This element is used when defining a common control that can be used by all the
views in the formatting file.

Name Element for SelectionSet (Format) Specifies the name used to reference the selection set.

Name Element for View (Format) Specifies the name that is used to identify the view.

NewLine Element for CustomItem for Controls for Configuration (Format) Adds a blank line to
the display of the control. This element is used when defining a common control that can be
used by all the views in the formatting file.

NewLine Element for CustomItem for Controls for View (Format) Adds a blank line to the
display of the control. This element is used when defining controls that can be used by a view.

NewLine Element for CustomItem for CustomControl for View (Format) Adds a blank line to the
display of the control. This element is used when defining a custom control view.

NewLine Element for CustomItem for GroupBy (Format) Adds a blank line to the display of the
control. This element is used when defining how a new group of objects is displayed.

PropertyName Element for ExpressionBinding for Controls for Configuration (Format) Specifies
the .NET property whose value is displayed by the common control. This element is used when
defining a common control that can be used by all the views in the formatting file.

PropertyName Element for ExpressionBinding for Controls for View (Format) Specifies the .NET
property whose value is displayed by the control. This element is used when defining controls
that can be used by a view.

PropertyName Element for ExpressionBinding for CustomControl for View (Format) Specifies
the .NET property whose value is displayed by the control. This element is used when defining
a custom control view

PropertyName Element for ExpressionBinding for GroupBy (Format) Specifies the .NET property
whose value is displayed by the control. This element is used when defining how a new group
of objects is displayed.

<!-- p.2334 -->

PropertyName Element for GroupBy (Format) Specifies the .NET property that starts a new
group whenever its value changes.

PropertyName Element for ItemSelectionCondition for Controls for Configuration (Format)
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining a common control that can be used by all the views in the formatting file.

PropertyName Element for ItemSelectionCondition for Controls for View (Format) Specifies the
.NET property that triggers the condition. When this property is present or when it evaluates to
true , the condition is met, and the control is used. This element is used when defining controls

that can be used by a view.

PropertyName Element for ItemSelectionCondition for CustomControl for View (Format
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining a custom control view.

PropertyName Element for ItemSelectionCondition for GroupBy (Format) Specifies the .NET
property that triggers the condition. When this property is present or when it evaluates to
true , the condition is met, and the control is used. This element is used when defining how a

new group of objects is displayed.

PropertyName Element for ItemSelectionCondition for ListItem (Format) Specifies the .NET
property that triggers the condition. When this property is present or when it evaluates to
true , the condition is met, and the view is used. This element is used when defining a list view.

PropertyName Element for ListItem for ListControl (Format) Specifies the .NET property whose
value is displayed in the list.

PropertyName Element for SelectionCondition for EntrySelectedBy for ListEntry (Format)
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the entry is used. This element is used when
defining a common control that can be used by all the views in the formatting file.

PropertyName Element for SelectionCondition for Controls for View (Format) Specifies the .NET
property that triggers the condition. When this property is present or when it evaluates to
true , the condition is met, and the entry is used. This element is used when defining controls

that can be used by a view.

<!-- p.2335 -->

PropertyName Element for SelectionCondition for CustomControl for View (Format) Specifies
the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used. This element is used when
defining a custom control view.

PropertyName Element for SelectionCondition for EntrySelectedBy for EnumerableExpansion
(Format) Specifies the .NET property that triggers the condition. When this property is present
or when it evaluates to true , the condition is met, and the definition is used.

PropertyName Element for SelectionCondition for GroupBy (Format) Specifies the .NET
property that triggers the condition. When this property is present or when it evaluates to
true , the condition is met, and the definition is used. This element is used when defining how

a new group of objects is displayed.

PropertyName Element for SelectionCondition for EntrySelectedBy for ListEntry (Format)
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the list entry is used.

PropertyName Element for SelectionCondition for EntrySelectedBy for TableRowEntry (Format)
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the table entry is used.

PropertyName Element for SelectionCondition for EntrySelectedBy for WideEntry (Format)
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used.

PropertyName Element for TableColumnItem (Format) Specifies the property whose value is
displayed in the column of the row.

PropertyName Element for WideItem (Format) Specifies the property of the object whose value
is displayed in the wide view.

RightIndent Element for Frame for Controls for Configuration (Format) Specifies how many
characters the data is shifted away from the right margin. This element is used when defining a
common control that can be used by all the views in the formatting file.

RightIndent Element of Frame of Controls of View (Format) Specifies how many characters the
data is shifted away from the right margin. This element is used when defining controls that
can be used by a view.

<!-- p.2336 -->

RightIndent Element Specifies how many characters the data is shifted away from the right
margin. This element is used when defining a custom control view.

RightIndent Element for Frame for GroupBy (Format) Specifies how many characters the data is
shifted away from the right margin. This element is used when defining how a new group of
objects is displayed.

ScriptBlock Element for ExpressionBinding for Controls for Configuration (Format) Specifies the
script whose value is displayed by the common control. This element is used when defining a
common control that can be used by all the views in the formatting file.

ScriptBlock Element for ExpressionBinding for Controls for View (Format) Specifies the script
whose value is displayed by the control. This element is used when defining controls that can
be used by a view.

ScriptBlock Element for ExpressionBinding for CustomCustomControl for View (Format)
Specifies the script whose value is displayed by the control. This element is used when defining
a custom control view.

ScriptBlock Element for ExpressionBinding for GroupBy (Format) Specifies the script whose
value is displayed by the control. This element is used when defining how a new group of
objects is displayed.

ScriptBlock Element for GroupBy (Format) Specifies the script that starts a new group whenever
its value changes.

ScriptBlock Element for ItemSelectionCondition for Controls for Configuration (Format)
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the control is used. This element is used when defining a common
control that can be used by all the views in the formatting file.

ScriptBlock Element for ItemSelectionCondition for Controls for View (Format) Specifies the
script that triggers the condition. When this script is evaluated to true , the condition is met,
and the control is used. This element is used when defining controls that can be used by a
view.

ScriptBlock Element for ItemSelectionCondition for CustomControl for View (Format) Specifies
the script that triggers the condition. When this script is evaluated to true , the condition is
met, and the control is used. This element is used when defining a custom control view.

<!-- p.2337 -->

ScriptBlock Element for ItemSelectionCondition for GroupBy (Format) Specifies the script that
triggers the condition. When this script is evaluated to true , the condition is met, and the
control is used. This element is used when defining how a new group of objects is displayed.

ScriptBlock Element for ItemSelectionCondition for ListControl (Format) Specifies the script that
triggers the condition. When this script is evaluated to true , the condition is met, and the list
item is used. This element is used when defining a list view.

ScriptBlock Element for ListItem (Format) Specifies the script whose value is displayed in the
row of the list.

ScriptBlock Element for SelectionCondition for Controls for Configuration (Format) Specifies
the script that triggers the condition. When this script is evaluated to true , the condition is
met, and the definition is used. This element is used when defining a common control that can
be used by all the views in the formatting file.

ScriptBlock Element for SelectionCondition for Controls for View (Format) Specifies the script
that triggers the condition. When this script is evaluated to true , the condition is met, and the
definition is used. This element is used when defining controls that can be used by a view.

ScriptBlock Element for SelectionCondition for CustomControl for View (Format) Specifies the
script that triggers the condition. When this script is evaluated to true , the condition is met,
and the definition is used. This element is used when defining a custom control view.

ScriptBlock Element for SelectionCondition for EntrySelectedBy for EnumerableExpansion
(Format) Specifies the script that triggers the condition.

ScriptBlock Element for SelectionCondition for GroupBy (Format) Specifies the script that
triggers the condition. When this script is evaluated to true , the condition is met, and the
definition is used. This element is used when defining how a new group of objects is displayed.

ScriptBlock Element for SelectionCondition for EntrySelectedBy for ListEntry (Format) Specifies
the script that triggers the condition. When this script is evaluated to true , the condition is
met, and the list entry is used.

ScriptBlock Element for SelectionCondition for EntrySelectedBy for TableRowEntry (Format)
Specifies the script block that triggers the condition. When this script is evaluated to true , the
condition is met, and the table entry is used.

ScriptBlock Element for SelectionCondition for EntrySelectedBy for WideEntry (Format)
Specifies the script that triggers the condition. When this script is evaluated to true , the

<!-- p.2338 -->

condition is met, and the wide entry definition is used.

ScriptBlock Element for TableColumnItem (Format) Specifies the script whose value is displayed
in the column of the row.

ScriptBlock Element for WideItem (Format) Specifies the script whose value is displayed in the
wide view.

SelectionCondition Element for EntrySelectedBy for CustomEntry for Configuration (Format)
Defines a condition that must exist for a common control definition to be used. This element is
used when defining a common control that can be used by all the views in the formatting file.

SelectionCondition Element for EntrySelectedBy for Controls for View (Format) Defines a
condition that must exist for the control definition to be used. This element is used when
defining controls that can be used by a view.

SelectionCondition Element for EntrySelectedBy for CustomControl for View (Format) Defines a
condition that must exist for a control definition to be used. This element is used when
defining a custom control view.

SelectionCondition Element for EntrySelectedBy for EnumerableExpansion (Format) Defines the
condition that must exist to expand the collection objects of this definition.

SelectionCondition Element for EntrySelectedBy for GroupBy (Format) Defines a condition that
must exist for a control definition to be used. This element is used when defining how a new
group of objects is displayed.

SelectionCondition Element for EntrySelectedBy for ListEntry (Format) Defines the condition
that must exist to use this definition of the list view. There is no limit to the number of selection
conditions that can be specified for a list definition.

SelectionCondition Element for EntrySelectedBy for TableRowEntry (Format) Defines the
condition that must exist to use for this definition of the table view. There is no limit to the
number of selection conditions that can be specified for a table definition.

SelectionCondition Element for EntrySelectedBy for WideEntry (Format) Defines the condition
that must exist for this definition to be used. There is no limit to the number of selection
conditions that can be specified for a wide entry definition.

SelectionSet Element (Format) Defines a set of .NET objects that can be referenced by the
name of the set.

<!-- p.2339 -->

SelectionSetName Element for EntrySelectedBy for Controls for Configuration (Format)
Specifies a set of .NET types that use this definition of the control. This element is used when
defining a common control that can be used by all the views in the formatting file.

SelectionSetName Element for EntrySelectedBy for Controls for View (Format) Specifies a set of
.NET types that use this definition of the control. This element is used when defining controls
that can be used by a view.

SelectionSetName Element for EntrySelectedBy for CustomEntry (Format) Specifies a set of
.NET objects for the list entry. There is no limit to the number of selection sets that can be
specified for an entry.

SelectionSetName Element for EntrySelectedBy for EnumerableExpansion (Format) Specifies
the set of .NET types that are expanded by this definition.

SelectionSetName Element for EntrySelectedBy for GroupBy (Format) Specifies a set of .NET
objects for the list entry. There is no limit to the number of selection sets that can be specified
for an entry. This element is used when defining how a new group of objects is displayed.

SelectionSetName Element for EntrySelectedBy for ListEntry (Format) Specifies a set of .NET
objects for the list entry. There is no limit to the number of selection sets that can be specified
for an entry.

SelectionSetName Element for EntrySelectedBy for TableRowEntry (Format) Specifies a set of
.NET types the use this entry of the table view. There is no limit to the number of selection sets
that can be specified for an entry.

SelectionSetName Element for EntrySelectedBy for WideEntry (Format) Specifies a set of .NET
objects for the definition. The definition is used whenever one of these objects is displayed.

SelectionSetName Element for SelectionCondition for Controls for Configuration (Format)
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this control. This element is
used when defining a common control that can be used by all the views in the formatting file.

SelectionSetName Element for SelectionCondition for Controls for View (Format) Specifies the
set of .NET types that trigger the condition. When any of the types in this set are present, the
condition is met and the object is displayed using this control. This element is used when
defining controls that can be used by a view.

<!-- p.2340 -->

EntrySelectedBy Element for CustomEntry for View (Format) Specifies the set of .NET types that
trigger the condition. When any of the types in this set are present, the condition is met and
the object is displayed using this control. This element is used when defining a custom control
view.

SelectionSetName Element for SelectionCondition for EntrySelectedBy for
EnumerableExpansion (Format) Specifies the set of .NET types that trigger the condition. When
any of the types in this set are present, the condition is met.

SelectionSetName Element for SelectionCondition for GroupBy (Format) Specifies the set of
.NET types that trigger the condition. When any of the types in this set are present, the
condition is met, and the object is displayed by using this control. This element is used when
defining how a new group of objects is displayed.

SelectionSetName Element for SelectionCondition for EntrySelectedBy for ListEntry (Format)
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this definition of the list
view.

SelectionSetName Element for SelectionCondition for EntrySelectedBy for TableRowEntry
(Format) Specifies the set of .NET types that trigger the condition. When any of the types in this
set are present, the condition is met, and the object is displayed by using this definition of the
table view.

SelectionSetName Element for SelectionCondition for EntrySelectedBy for WideEntry (Format)
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this definition of the wide
view.

SelectionSetName Element for ViewSelectedBy (Format) Specifies a set of .NET objects that are
displayed by the view.

SelectionSets Element (Format) Defines the sets of .NET objects that can be used by individual
format views.

ShowError Element (Format) Specifies that the full error record is displayed when an error
occurs while displaying a piece of data.

TableColumnHeader Element for TableHeaders for TableControl (Format) Defines the label, the
width of the column, and the alignment of the label for a column of the table.

<!-- p.2341 -->

TableColumnItem Element (Format) Defines the property or script whose value is displayed in
the column of the row.

TableColumnItems Element (Format) Defines the properties or scripts whose values are
displayed in the row.

TableControl Element (Format) Defines a table format for a view.

TableHeaders Element (Format) Defines the headers for the columns of a table.

TableRowEntries Element (Format) Defines the rows of the table.

TableRowEntry Element (Format) Defines the data that is displayed in a row of the table.

Text Element for CustomItem for Controls for Configuration (Format) Specifies text that is
added to the data that is displayed by the control, such as a label, brackets to enclose the data,
and spaces to indent the data. This element is used when defining a common control that can
be used by all the views in the formatting file.

Text Element for CustomItem for Controls for View (Format) Specifies text that is added to the
data that is displayed by the control, such as a label, brackets to enclose the data, and spaces
to indent the data. This element is used when defining controls that can be used by a view.

Text Element for CustomItem (Format) Specifies text that is added to the data that is displayed
by the control, such as a label, brackets to enclose the data, and spaces to indent the data. This
element is used when defining a custom control view.

Text Element for CustomItem for GroupBy (Format) Specifies text that is added to the data that
is displayed by the control, such as a label, brackets to enclose the data, and spaces to indent
the data. This element is used when defining how a new group of objects is displayed.

TypeName Element for EntrySelectedBy for Controls for Configuration (Format) Specifies a .NET
type that uses this definition of the control. This element is used when defining a common
control that can be used by all the views in the formatting file.

TypeName Element for EntrySelectedBy for Controls for View (Format) Specifies a .NET type
that uses this definition of the control. This element is used when defining controls that can be
used by a view.

TypeName Element for EntrySelectedBy for CustomEntry for View (Format) Specifies a .NET
type that uses this definition of the custom control view. There is no limit to the number of
types that can be specified for a definition.

<!-- p.2342 -->

TypeName Element for EntrySelectedBy for EnumerableExpansion (Format) Specifies a .NET
type that is expanded by this definition. This element is used when defining a default settings.

TypeName Element for EntrySelectedBy for GroupBy (Format) Specifies a .NET type that uses
this definition of the custom control. This element is used when defining how a new group of
objects is displayed.

TypeName Element for EntrySelectedBy for ListControl (Format) Specifies a .NET type that uses
this entry of the list view. There is no limit to the number of types that can be specified for a list
entry.

TypeName Element for EntrySelectedBy for TableRowEntry (Format) Specifies a .NET type that
uses this entry of the table view. There is no limit to the number of types that can be specified
for a table entry.

TypeName Element for EntrySelectedBy for WideEntry (Format) Specifies a .NET type for the
definition. The definition is used whenever this object is displayed.

TypeName Element for SelectionCondition for Controls for Configuration (Format) Specifies a
.NET type that triggers the condition. This element is used when defining a common control
that can be used by all the views in the formatting file.

TypeName Element for SelectionCondition for Controls for View (Format) Specifies a .NET type
that triggers the condition. This element is used when defining controls that can be used by a
view.

TypeName Element for SelectionCondition for CustomControl for View (Format) Specifies a
.NET type that triggers the condition. This element is used when defining a custom control
view.

TypeName Element for SelectionCondition for EntrySelectedBy for EnumerableExpansion
(Format) Specifies a .NET type that triggers the condition.

TypeName Element for SelectionCondition for GroupBy (Format) Specifies a .NET type that
triggers the condition. This element is used when defining how a new group of objects is
displayed.

TypeName Element for SelectionCondition for EntrySelectedBy for ListControl (Format)
Specifies a .NET type that triggers the condition. When this type is present, the list entry is
used.

<!-- p.2343 -->

TypeName Element for SelectionCondition for EntrySelectedBy for TableRowEntry (Format)
Specifies a .NET type that triggers the condition. When this type is present, the condition is
met, and the table row is used.

TypeName Element for SelectionCondition for EntrySelectedBy for WideEntry (Format) Specifies
a .NET type that triggers the condition. When this type is present, the definition is used.

TypeName Element for Types (Format) Specifies the .NET type of an object that belongs to the
selection set.

TypeName Element for ViewSelectedBy (Format) Specifies a .NET object that is displayed by the
view.

Types Element (Format) Defines the .NET objects that are in the selection set.

View Element (Format) Defines a view that is used to display one or more .NET objects.

ViewDefinitions Element (Format) Defines the views used to display objects.

ViewSelectedBy Element (Format) Defines the .NET objects that are displayed by the view.

WideControl Element (Format) Defines a wide (single value) list format for the view. This view
displays a single property value or script value for each object.

WideEntries Element (Format) Provides the definitions of the wide view. The wide view must
specify one or more definitions.

WideEntry Element (Format) Provides a definition of the wide view.

WideItem Element (Format) Defines the property or script whose value is displayed.

Width Element (Format) Defines the width (in characters) of a column.

Wrap Element (Format) Specifies that text that exceeds the column width is displayed on the
next line.

WrapTables Element (Format) Specifies that data in a table cell is moved to the next line if the
data is longer than the width of the column.

See Also
Writing a PowerShell Formatting File

<!-- p.2344 -->

Last updated on 05/20/2025

<!-- p.2345 -->

Configuration Element
Represents the top-level element of a formatting file.

Schema
     Configuration Element

Syntax
 XML

 <Configuration>
   <DefaultSettings>...</DefaultSettings>
   <SelectionSets>...</SelectionSets>
   <Controls>...</Controls>
   <ViewDefinitions>...</ViewDefinitions>
 </Configuration>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Configuration element. This element must be the root element for each formatting file, and

this element must contain at least one child element.

Attributes
None.

Child Elements

                                                                                    ﾉ   Expand table

 Element                      Description

 Controls Element for         Optional element.
 Configuration
                              Defines the common controls that can be used by all views of the
                              formatting file.

<!-- p.2346 -->

 Element                        Description

 DefaultSettings Element        Optional element.

                                Defines common settings that apply to all the views of the formatting
                                file.

 SelectionSets Element Format   Optional element.

                                Defines the common sets of .NET objects that can be used by all views of
                                the formatting file.

 ViewDefinitions Element        Optional element.

                                Defines the views used to display objects.

Parent Elements
None.

Remarks
Formatting files define how objects are displayed. In most cases, this root element contains a
ViewDefinitions element that defines the table, list, and wide views of the formatting file. In
addition to the view definitions, the formatting file can define common selection sets, settings,
and controls that those views can use.

See Also
Controls Element for Configuration

DefaultSettings Element

SelectionSets Element

ViewDefinitions Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2347 -->

Controls Element for Configuration
Defines the common controls that can be used by all views of the formatting file.

Schema
     Configuration Element
     Controls Element

Syntax
 XML

 <Controls>
   <Control>...</Control>
 </Controls>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Controls element.

Attributes
None.

Child Elements

                                                                                   ﾉ   Expand table

 Element                              Description

 Control Element for Controls for     Required element.
 Configuration
                                      Defines a common control that can be used by all views of the
                                      formatting file.

Parent Elements

<!-- p.2348 -->

                                                                                       ﾉ   Expand table

 Element                      Description

 Configuration Element        Represents the top-level element of a formatting file.

Remarks
You can create any number of common controls. For each control, you must specify the name
that is used to reference the control and the components of the control.

See Also
Configuration Element

Control Element for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2349 -->

Control Element for Controls for
Configuration
Defines a common control that can be used by all the views of the formatting file and the
name that is used to reference the control.

Schema
     Configuration Element
     Controls Element
     Control Element

Syntax
 XML

 <Control>
   <Name>NameOfControl</Name>
   <CustomControl>...</CustomControl>
 </Control>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element for the
Control element. You must specify only one of each child element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                                                Description

 CustomControl Element for Control for Controls for     Required element.
 Configuration
                                                        Defines the control.

<!-- p.2350 -->

 Element                                                      Description

 Name Element for Control for Configuration                   Required element.

                                                              Specifies the name used to reference the
                                                              control.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                      Description

 Controls Element of          Defines the common controls that can be used by all views of the
 Configuration                formatting file or by other controls.

Remarks
The name given to this control can be referenced in the following elements:

     ExpressionBinding Element for CustomItem

     GroupBy Element for View

See Also
Controls Element of Configuration

CustomControl element for Control for Configuration

ExpressionBinding Element for CustomItem

GroupBy Element for View(Format)

Name Element for Control for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2351 -->

CustomControl Element for Control for
Controls for Configuration
Defines a control. This element is used when defining a common control that can be used by
all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element

Syntax
  XML

  <CustomControl>
    <CustomEntries>...</CustomEntries>
  </CustomControl>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
CustomControl element. This element must have at least one child element. There is no

maximum limit to the number of child elements that can be specified.

Attributes
None.

Child Elements

                                                                                 ﾉ   Expand table

 Element                                                     Description

 CustomEntries Element for CustomControl for Configuration   Required element.

<!-- p.2352 -->

 Element                                                          Description

                                                                  Provides the definitions of a control.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                        Description

 Control Element for Controls   Defines a common control that can be used by all the views of the
 for Configuration              formatting file and the name that is used to reference the control.

Remarks
See Also
Control Element for Controls for Configuration

CustomEntries Element for CustomControl for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2353 -->

CustomEntries Element for CustomControl
for Controls for Configuration
Provides the definitions of a common control. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element

Syntax
 XML

 <CustomEntries>
   <CustomEntry>...</CustomEntry>
 </CustomEntries>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomEntries element. You must specify one or more child elements.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

<!-- p.2354 -->

 Element                                                    Description

 CustomEntry Element for CustomControl for Controls for     Provides a definition of the common
 Configuration                                              control.

Parent Elements

                                                                                 ﾉ   Expand table

 Element                                                         Description

 CustomControl Element for Control for Configuration             Defines a common control.

Remarks
In most cases, a control has only one definition, which is defined in a single CustomEntry
element. However it is possible to have multiple definitions if you want to use the same control
to display different .NET objects. In those cases, you can define a CustomEntry element for each
object or set of objects.

See Also
CustomControl Element for Control for Configuration

CustomEntry Element for CustomControl for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2355 -->

CustomEntry Element for CustomControl
for Controls for Configuration
Provides a definition of the common control. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element

Syntax
 XML

 <CustomEntry>
   <EntrySelectedBy>...</EntrySelectedBy>
   <CustomItem>...</CustomItem>
 </CustomEntry>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomEntry element. You must specify the items displayed by the definition.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

<!-- p.2356 -->

 Element                                 Description

 EntrySelectedBy Element for             Optional element.
 CustomEntry for Controls for
 Configuration                           Defines the .NET types that use the definition of the common
                                         control or the condition that must exist for this control to be
                                         used.

 CustomItem Element for CustomEntry      Required element.
 for Controls for Configuration
                                         Defines what data is displayed by the control and how it is
                                         displayed.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                  Description

 CustomEntries Element for CustomControl for              Provides the definitions of the common
 Configuration                                            control.

Remarks
In most cases, only one definition is required for each common custom control, but it is
possible to have multiple definitions if you want to use the same control to display different
.NET objects. In those cases, you can provide a separate definition for each object or set of
objects.

See Also
CustomEntries Element for CustomControl for Configuration

CustomItem Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2357 -->

CustomItem Element for CustomEntry for
Controls for Configuration
Defines what data is displayed by the control and how it is displayed. This element is used
when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element

Syntax
 XML

 <CustomItem>
   <ExpressionBinding>...</ExpressionBinding>
   <NewLine/>
   <Text>TextToDisplay</Text>
   <Frame>...</Frame>
 </CustomItem>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomItem element. For more information, see Remarks.

Attributes
None.

Child Elements

<!-- p.2358 -->

                                                                                       ﾉ   Expand table

 Element                                            Description

 ExpressionBinding Element for CustomItem for       Optional element.
 Controls for Configuration
                                                    Defines the data that is displayed by the control.

 Frame Element for CustomItem for Controls for      Optional element.
 Configuration
                                                    Defines how the data is displayed, such as shifting
                                                    the data to the left or right.

 NewLine Element for CustomItem for Controls for    Optional element.
 Configuration
                                                    Adds a blank line to the display of the control.

 Text Element for CustomItem for Controls for       Optional element.
 Configuration
                                                    Adds text, such as parentheses or brackets, to the
                                                    display of the control.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                              Description

 CustomEntry Element for CustomControl for Controls for               Provides a definition of the
 Configuration                                                        control.

Remarks
When specifying the child elements of the CustomItem element, keep the following in mind:

     The child elements must be added in the following sequence: ExpressionBinding ,
      NewLine , Text , and Frame .

     There is no maximum limit to the number of sequences that you can specify.
     In each sequence, there is no maximum limit to the number of ExpressionBinding
     elements that you can use.

See Also
ExpressionBinding Element for CustomItem for Controls for Configuration

<!-- p.2359 -->

Frame Element for CustomItem for Controls for Configuration

NewLine Element for CustomItem for Controls for Configuration

Text Element for CustomItem for Controls for Configuration

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2360 -->

ExpressionBinding Element for CustomItem
for Controls for Configuration
Defines the data that is displayed by the control. This element is used when defining a
common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element

Syntax
 XML

 <ExpressionBinding>
   <CustomControl>...</CustomControl>
   <CustomControlName>NameofCommonCustomControl</CustomControlName>
   <EnumerateCollection/>
   <ItemSelectionCondition>...</ItemSelectionCondition>
   <PropertyName>Nameof.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate></ScriptBlock>
 </ExpressionBinding>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ExpressionBinding element.

Attributes
None.
