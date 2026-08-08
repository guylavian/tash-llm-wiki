---
title: "How to use this documentation — pages 2681-2720"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2681-2720
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2681-2720
family: powershell
documentKind: "doc"
abstract: "Parent Elements ﾉ Expand table Element Description SelectionCondition Element for EntrySelectedBy for Defines the condition that must exist for this list ListControl entry to be used. Text Value Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo ."
---

# How to use this documentation — pages 2681-2720

<!-- p.2681 -->

Parent Elements

                                                                                          ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines the condition that must exist for this list
 ListControl                                          entry to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
The selection condition can specify any number of .NET types or selection sets, but cannot
specify both. For more information about how to use selection conditions, see Defining
Conditions for when Data is Displayed.

For more information about other the components of a list view, see Creating a List View.

See Also
Creating a List View

Defining Conditions for When Data Is Displayed

SelectionCondition Element for EntrySelectedBy for ListControl

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2682 -->

SelectionSetName Element for
EntrySelectedBy for ListControl
Specifies a set of .NET objects for the list entry. There is no limit to the number of selection sets
that can be specified for an entry.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
SelectionSetName element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2683 -->

                                                                                        ﾉ   Expand table

 Element                       Description

 EntrySelectedBy Element for   Defines the .NET types that use this list entry or the condition that must
 ListEntry                     exist for this entry to be used.

Text Value
Specify the name of the selection set.

Remarks
Each list entry must have at least one type name, selection set, or selection condition defined.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you might want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Sets of objects
for a View.

For more information about the components of a list view, see Creating a List View.

Example
The following example shows how to specify a selection set for an entry of a list view.

 XML

 <ListEntry>
   <EntrySelectedBy>
     <SelectionSetName>NameofSelectionSet</SelectionSetName>
   </EntrySelectedBy>
   <ListItems>...</ListItems>
 </ListEntry>

See Also
Creating a List View

EntrySelectedBy Element for ListEntry

Writing a PowerShell Formatting File

<!-- p.2684 -->

Last updated on 05/20/2025

<!-- p.2685 -->

TypeName Element for EntrySelectedBy for
ListControl
Specifies a .NET type that uses this entry of the list view. There is no limit to the number of
types that can be specified for a list entry.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2686 -->

                                                                                        ﾉ   Expand table

 Element                       Description

 EntrySelectedBy Element for   Defines the .NET types that use this list entry or the condition that must
 ListEntry                     exist for this entry to be used.

Text Value
Specify the fully-qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
Each list entry must have at least one type name, selection set, or selection condition defined.

For more information about how this element is used in a list view, see List View.

Example
The following example shows how to specify a selection set for an entry of a list view.

  XML

  <ListEntry>
    <EntrySelectedBy>
      <TypeName>Nameof.NetType</TypeName>
    </EntrySelectedBy>
    <ListItems>...</ListItems>
  </ListEntry>

See Also
Creating a List View

EntrySelectedBy Element for ListEntry

SelectionSetName Element for EntrySelectedBy for ListEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2687 -->

ListItems Element
Defines the properties and scripts whose values are displayed in the rows of the list view.

     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element

Syntax
 XML

 <ListItems>
   <ListItem>...</ListItem>
 </ListItems>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
ListItems element. There is no limit to the number of child elements that can be specified. The

order of the child elements defines the order that values are displayed in the list view.

Attributes
None.

Child Elements

                                                                                           ﾉ   Expand table

 Element                            Description

 ListItem Element for ListControl   Required element.

                                    Defines the property or script whose value is displayed by the list view.

<!-- p.2688 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                      Description

 ListEntry Element for ListControl            Provides a definition of the list view.

Remarks
For more information about this type of view, see Creating a List View.

Example
This example shows the XML elements that define three rows of the list view.

  XML

  <ListEntry>
      <ListItems>
        <ListItem>
          <Label>Property1: </Label>
          <PropertyName>.NetTypeProperty1</PropertyName>
        </ListItem>
        <ListItem>
          <PropertyName>.NetTypeProperty2</PropertyName>
        </ListItem>
        <ListItem>
          <ScriptBlock>$_.ProcessName + ":" $_.Id</ScriptBlock>
        </ListItem>
    </ListEntry>

See Also
ListEntry Element for ListControl

ListItem Element for ListControl

Creating a List View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2689 -->

FormatString Element for ListItem for
ListControl
Specifies a format pattern that defines how the property or script value is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     FormatString Element

Syntax
 XML

 <FormatString>PropertyPattern</FormatString>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
FormatString element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2690 -->

                                                                                            ﾉ   Expand table

 Element              Description

 ListItem Element     Defines the property or script whose value is displayed in a row of the list view.

Text Value
Specify the pattern that is used to format the data. For example, you can use this pattern to
format the value of any property that is of type System.TimeSpan: {0:MMM}{0:dd}{0:HH}:
{0:mm}.

Remarks
Format strings can be used when creating table views, list views, wide views, or custom views.
For more information about formatting a value displayed in a view, see Formatting Displayed
Data.

For more information about using format strings in list views, see Creating List View.

Example
The following example shows how to define a formatting string for the value of the StartTime
property.

  XML

  <ListItem>
    <PropertyName>StartTime</PropertyName>
    <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
  </ListItem>

See Also
Creating a List View

ListItem Element

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2691 -->

<!-- p.2692 -->

ItemSelectionCondition Element for
ListItem for ListControl
Defines the condition that must exist for this list item to be used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     ItemSelectionCondition Element

Syntax
 XML

 <ItemSelectionCondition>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </ItemSelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ItemSelectionCondition element.

Attributes
None.

Child Elements

<!-- p.2693 -->

                                                                                          ﾉ   Expand table

 Element                                                    Description

 PropertyName Element for ItemSelectionCondition for        Optional element.
 ListControl
                                                            Specifies the .NET property that triggers the
                                                            condition.

 ScriptBlock Element for ItemSelectionCondition for         Optional element.
 ListControl
                                                            Specifies the script that triggers the condition.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                                Description

 ListItem Element for ListItems for     Defines the property or script whose value is displayed in a row
 ListControl                            of the list view.

Remarks
You can specify one property name or a script for this condition but cannot specify both.

See Also
ListItem Element for ListItems for ListControl

PropertyName Element for ItemSelectionCondition for ListControl

ScriptBlock Element for ItemSelectionCondition for ListControl

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2694 -->

PropertyName Element for
ItemSelectionCondition for ListControl
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the view is used. This element is used when
defining a list view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     ItemSelectionCondition Element
     PropertyName Element

Syntax
  XML

  <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent elements of the
PropertyName element.

Attributes
None.

Child Elements

<!-- p.2695 -->

None.

Parent Elements

                                                                               ﾉ   Expand table

 Element                                                                      Description

 ItemSelectionCondition Element for ListItem for ListControl

Text Value
Specify the name of the property whose value is displayed.

Remarks
If this element is used, you cannot specify the ScriptBlock element when defining the selection
condition.

See Also
ScriptBlock Element for ItemSelectionCondition for ListIControl

ItemSelectionCondition Element for ListItem for ListControl

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2696 -->

ScriptBlock Element for
ItemSelectionCondition for ListControl
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the list item is used. This element is used when defining a list view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element for ListControl
     ListEntry Element for ListEntries for ListControl
     ListItems Element for ListEntry for ListControl
     ListItem Element for ListItems for List Control
     ItemSelectionCondition Element for ListItem for ListControl
     ScriptBlock Element for ItemSelectionCondition for ListControl

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent elements of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

<!-- p.2697 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                           Description

 ItemSelectionCondition Element for ListItem for   Defines the condition that must exist for this list
 ListControl                                       item to be used.

Text Value
Specify the script that is evaluated.

Remarks
If this element is used, you cannot specify the PropertyName element when defining the
selection condition.

See Also
Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2698 -->

Label Element for ListItem for ListControl
Specifies the label that is displayed to the left of the property or script value in the row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     Label Element

Syntax
 XML

 <Label>Label for displayed value</Label>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Label element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2699 -->

                                                                                       ﾉ   Expand table

 Element                               Description

 ListItem Element for ListItems for    Defines the property or script whose value is displayed in a row
 ListControl                           of the list view.

Text Value
Specify the label to be display to the left of the property or script value.

Remarks
If a label is not specified, the name of the property or the script is displayed. For more
information about using labels in a list view, see Creating a List View.

Example
The following example shows how to add a label to a row.

  XML

  <ListItem>
    <Label>Property1: </Label>
    <PropertyName>DotNetProperty1</PropertyName>
  </ListItem>

See Also
Creating a List View

ListItem Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2700 -->

ListItem Element
Defines the property or script whose value is displayed in a row of the list view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element

Syntax
 XML

 <ListItem>
   <PropertyName>PropertyToDisplay</PropertyName>
   <ScriptBlock>ScriptToExecute</ScriptBlock>
   <Label>LabelToDisplay</Label>
   <FormatString>FormatPattern</FormatString>
   <ItemSelectionCondition>...</ItemSelectionCondition>
 </ListItem>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
ListItem element. Only one property or script can be specified.

Attributes
None

Child Elements

                                                                                 ﾉ   Expand table

<!-- p.2701 -->

 Element                                         Description

 FormatString Element for ListItem for           Optional element.
 ListControl
                                                 Specifies a format string that defines how the property or
                                                 script value is displayed.

 ItemSelectionCondition Element for ListItem     Optional element.
 for ListControl
                                                 Defines the condition that must exist for this list item to
                                                 be used.

 Label Element for ListItem for ListControl      Optional element

                                                 Specifies the label that is displayed to the left of the
                                                 property or script value in the row.

 PropertyName Element for ListItem for           Optional element.
 ListControl
                                                 Specifies the .NET property whose value is displayed in
                                                 the row.

 ScriptBlock Element for ListItem for            Optional element.
 ListControl
                                                 Specifies the script whose value is displayed in the row.

Parent Elements

                                                                                            ﾉ    Expand table

 Element                           Description

 ListItems Element for List        Defines the properties and scripts whose values are displayed in the list
 Control                           view.

Remarks
For more information about the components of a list view, see Creating a List View.

Example
This example shows the XML elements that define three rows of the list view. The first two rows
display the value of a .NET property, and the last row displays a value generated by a script.

 XML

<!-- p.2702 -->

  <ListEntry>
      <ListItems>
        <ListItem>
          <Label>Property1: </Label>
          <PropertyName>DotNetProperty1</PropertyName>
        </ListItem>
        <ListItem>
          <PropertyName>DotNetProperty2</PropertyName>
        </ListItem>
        <ListItem>
          <ScriptBlock>$_.ProcessName + ":" $_.Id</ScriptBlock>
        </ListItem>
      </ListItems>
  </ListEntry>

See Also
ListItems Element

FormatString Element for ListItem

Label Element for ListItem

PropertyName Element for ListItem

ScriptBlock Element for ListItem

Creating a List View

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2703 -->

PropertyName Element for ListItem for
ListControl
Specifies the .NET property whose value is displayed in the list.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2704 -->

                                                                                            ﾉ   Expand table

 Element              Description

 ListItem Element     Defines the property or script whose value is displayed in the row of the list view.

Text Value
Specify the name of the property whose value is displayed.

Remarks
When this element is specified, you cannot specify the ScriptBlock element.

In addition to displaying the property value, you can also specify a label for the value or a
format string that can be used to change the display of the value. For more information about
specifying data in a list view, see Creating a List View.

Example
The following example shows how to specify the label and property whose value is displayed.

  XML

  ListItem>
    <Label>NameOfProperty</Label>
    <PropertyName>.NetTypeProperty</PropertyName>
  </ListItem>

See Also
ScriptBlock Element for ListItem for ListControl

Creating a List View

ListItem Element for ListControl(Format)

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2705 -->

ScriptBlock Element for ListItem for
ListControl
Specifies the script whose value is displayed in the row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     ListItems Element
     ListItem Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2706 -->

                                                                                            ﾉ   Expand table

 Element              Description

 ListItem Element     Defines the property or script whose value is displayed in a row of the list view.

Text Value
Specify the script whose value is displayed in the row.

Remarks
When this element is specified, you cannot specify the PropertyName element.

For more information about specifying scripts in a list view, see List View.

Example
The following example shows how to specify the property whose value is displayed.

  XML

  <ListItem>
    <ScriptBlock>$_.ProcessName + ":" $_.Id</ScriptBlock>
  </ListItem>

See Also
PropertyName Element for ListItem for ListControl

Creating a List View

ListItem Element for ListItems for ListControl

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2707 -->

Name Element for View
Specifies the name that is used to identify the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Name Element

Syntax
 XML

 <Name>ViewName</Name>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Name
element. Only one Name element is allowed for each view.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                      ﾉ   Expand table

 Element         Description

 View Element    Defines a view that is used to display the members of one or more .NET objects.

<!-- p.2708 -->

Text Value
Specify a unique friendly name for the view. This name can include a reference to the type of
the view (such as a table view or list view), which object or set of objects use the view, what
command returns the objects, or a combination of these.

Remarks
For more information about the different types of views, see the following topics: Table View,
List View, Wide View, and Custom View.

Example
The following example shows a View element that defines a table view for the
System.ServiceProcess.ServiceController object. The name of the view is "service".

  XML

  <View>
    <Name>service</Name>
    <ViewSelectedBy>
      <TypeName>System.ServiceProcess.ServiceController</TypeName>
    </ViewSelectedBy>
    <TableControl>...</TableControl>
  </View>

See Also
Creating a List View

Creating a Table View

Creating a Wide View

Creating Custom Controls

View Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2709 -->

OutOfBand Element
In a pipeline, the first object emitted is chosen as the type to format the output of the pipeline.
PowerShell attempts for format subsequent objects using the same view. If the object does not
fit the view, it is not displayed. You can create OutOfBand views that can be used for format
these other types.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     OutOfBand Element

Syntax
 XML

 <OutOfBand/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
OutOfBand element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                  ﾉ   Expand table

<!-- p.2710 -->

 Element                  Description

 View Element             Defines a view that displays one or more .NET objects.

Remarks
When the "shape" of formatting (view) has been determined by previous objects, you may
want objects of different types to continue using that shape (table, list, or whatever) even if
they specify their own views. Or sometimes you want your view to take over. When OutOfBand
is true, the view applies regardless of previous objects that may have selected a different view.

See Also
View Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2711 -->

TableControl Element
Defines a table format for a view.

Schema
     ViewDefinitions Element
     View Element
     TableControl Element

Syntax
 XML

 <TableControl>
   <AutoSize/>
   <HideTableHeaders/>
   <TableHeaders>...</TableHeaders>
   <TableRowEntries>...</TableRowEntries>
 </TableControl>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
TableControl element. You must specify the rows of the table. All other child elements are

optional.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                             Description

 AutoSize Element for                Optional element.
 TableControl

<!-- p.2712 -->

 Element                           Description

                                   Specifies whether the column size and the number of columns are
                                   adjusted based on the size of the data.

 HideTableHeaders Element for      Optional element.
 TableControl
                                   Indicates whether the header of the table is not displayed.

 TableHeaders Element for          Required element.
 TableControl
                                   Defines the labels, the widths, and the alignment of the data for the
                                   columns of the table view.

 TableRowEntries Element for       Optional element.
 TableControl
                                   Provides the definitions of the table view.

Parent Elements

                                                                                        ﾉ   Expand table

 Element          Description

 View Element     Defines a view that is used to display the members of one or more objects.

Remarks
For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableControl element that is used to display the properties of the
System.ServiceProcess.ServiceController object.

 XML

 <View>
   <Name>service</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <TableControl>
     <TableHeaders>...</TableHeaders>
     <TableRowEntries>...</TableRowEntries>
   </TableControl>

<!-- p.2713 -->

 </View>

See Also
Creating a Table View

View Element

AutoSize Element for TableControl

HideTableHeaders Element

TableHeaders Element

TableRowEntries Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2714 -->

AutoSize Element for TableControl
Specifies whether the column size and the number of columns are adjusted based on the size
of the data.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     AutoSize Element

Syntax
 XML

 <AutoSize/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
AutoSize element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2715 -->

 Element                               Description

 TableControl Element                  Defines a table format for a view.

Remarks
For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

TableControl Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2716 -->

HideTableHeaders Element
Specifies that the headers of the table are not displayed.

Schema
      ViewDefinitions Element
      View Element
      TableControl Element
      HideTableHeaders Element

Syntax
 VB

 <HideTableHeaders/>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
HideTableHeaders element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                               ﾉ   Expand table

 Element                                Description

 TableControl Element                   Defines a table format for a view.

<!-- p.2717 -->

Text Value
Specify true to hide the headers of the table.

Remarks
For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

TableControl Element

 Last updated on 05/20/2025

<!-- p.2718 -->

TableHeaders Element
Defines the headers for the columns of a table.

Schema
     ViewDefinitions Element
     View Element
     TableControl Element
     TableHeaders Element for TableControl

Syntax
 XML

 <TableHeaders>
   <TableColumnHeader>...</TableColumnHeader>
 </TableHeaders>

Attributes and Elements
The following sections describe the attributes, child elements, and parent elements of the
TableHeaders element. There must be a child element for each property of the object that is to

be displayed. The column header information is displayed in the order that the child elements
are specified.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                    Description

 TableColumnHeader          Optional element.
 Element

<!-- p.2719 -->

 Element                   Description

                           Defines the label, the width, and the alignment of the data for a column of
                           a table view.

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                 Description

 TableControl Element                    Defines a table format for a view.

Remarks
For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableHeaders element that defines two column headers.

 XML

 <TableHeaders>
   <TableColumnHeader>
     <Label>Column 1</Label>
     <Width>16</Width>
     <Alignment>Left</Alignment>
   </TableColumnHeader>
   <TableColumnHeader>
     <Label>Column 2</Label>
     <Width>10</Width>
     <Alignment>Centered</Alignment>
   </TableColumnHeader>
 </TableHeaders>

See Also
Creating a Table View

TableColumnHeader Element

TableControl Element

Writing a PowerShell Formatting File

<!-- p.2720 -->

Last updated on 05/20/2025
