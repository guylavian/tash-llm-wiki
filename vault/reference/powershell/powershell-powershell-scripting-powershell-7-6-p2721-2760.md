---
title: "How to use this documentation — pages 2721-2760"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2721-2760
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2721-2760
family: powershell
documentKind: "doc"
abstract: "TableColumnHeader Element Defines the label, the width of the column, and the alignment of the label for a column of the table. Schema Configuration Element ViewDefinitions Element View Element TableControl Element TableHeaders Element TableColumnHeader Element Syntax XML <Table"
---

# How to use this documentation — pages 2721-2760

<!-- p.2721 -->

TableColumnHeader Element
Defines the label, the width of the column, and the alignment of the label for a column of the
table.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableHeaders Element
     TableColumnHeader Element

Syntax
  XML

  <TableColumnHeader>
    <Label>DisplayedLabel</Label>
    <Width>NumberOfCharacters</Width>
    <Alignment>Left, Right, or Centered</Alignment>
  </TableColumnHeader>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TableColumnHeader element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

<!-- p.2722 -->

 Element                            Description

 Label Element For                  Optional element.
 TableColumnHeader for
 TableControl                       Defines the label that is displayed at the top of the column. If no
                                    label is specified, the name of the property whose value is
                                    displayed in the rows is used.

 Width Element for                  Required element.
 TableColumnHeader for
 TableControl                       Specifies the width (in characters) of the column.

 Alignment Element for              Optional element.
 TableColumnHeader for
 TableControl                       Specifies how the label of the column is displayed. If no alignment
                                    is specified, the label is aligned on the left.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                Description

 TableHeaders Element                   Defines the columns of a table view.

Remarks
Specify a header for each column of the table. The columns are displayed in the order in which
the TableColumnHeader elements are defined.

A table must have the same number of TableColumnHeader elements as TableRowEntry
elements. The column header defines how the text at the top of the table is displayed. The row
entries define what data is displayed in the rows of the table.

For more information about the components of a table view, see Table View.

Example
The following example shows two TableColumnHeader elements. The first element defines a
column whose label is "Column 1", has a width of 16 characters, and whose label is aligned on
the left. The second element defines a column whose label is "Column 2", has a width of 10
characters, and whose label is centered in the column.

<!-- p.2723 -->

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
Alignment Element for TableColumnHeader for TableControl

Creating a Table View

Label Element for TableColumnHeader for TableControl

TableHeaders Element for TableControl

Width for TableColumnHeader for TableControl Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2724 -->

Alignment Element for TableColumnHeader
Defines how the data in a column header is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableHeaders Element
     TableColumnHeader Element
     Alignment Element

Syntax
 XML

 <Alignment>AlignmentType</Alignment>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
Alignment element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2725 -->

 Element                      Description

 TableColumnHeader            Defines a label, the width, and the alignment of the data for a column of
 Element                      the table.

Text Value
Specify one of the following values. These values are not case-sensitive.

      Left - Aligns the data displayed in the column on the left This is the default if this element
      is not specified.
      Right - Aligns the data displayed in the column on the right.
      Center - Centers the data displayed in the column.

Remarks
For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableColumnHeader element whose data is aligned on the center.

  XML

  <TableColumnHeader>
    <Label>Column 1</Label>
    <Width>16</Width>
    <Alignment>Center</Alignment>
  </TableColumnHeader>

See Also
Creating a Table View

TableColumnHeader Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2726 -->

Label Element for TableColumnHeader for
TableControl
Defines the label that is displayed at the top of a column. This element is used when defining a
table view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableHeaders Element
     TableColumnHeader Element
     Label Element

Syntax
 XML

 <Label>DisplayedLabel</Label>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Label element. Only one label is allowed for each column.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2727 -->

                                                                                     ﾉ   Expand table

 Element                                      Description

 TableColumnHeader Element for TableHeaders   Defines a label, the width, and the alignment of the data
 for TableControl                             for a column of the table.

Text Value
Specify the text that is displayed at the top of the column of the table. There are no restricted
characters for the column label.

Remarks
If no label is specified, the name of the property whose value is displayed in the rows is used.

For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableColumnHeader element whose label is "Column 1".

  XML

  <TableColumnHeader>
    <Label>Column 1</Label>
    <Width>16</Width>
    <Alignment>Left</Alignment>
  </TableColumnHeader>

See Also
Creating a Table View

TableColumnHeader Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2728 -->

Width Element for TableColumnHeader
Defines the width (in characters) of a column.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableHeaders Element
     TableColumnHeader
     Width Element

Syntax
 XML

 <Width>NumberOfCharacters</Width>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the Width
element used when defining column headers.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                              ﾉ   Expand table

<!-- p.2729 -->

 Element                                        Description

 TableColumnHeader Element for TableHeaders     Defines a label, width, and alignment of the data for a
 for TableControl                               column of the table.

Text Value
When at all possible, specify a width (in characters) that is greater than the length of the
displayed property values.

Remarks
For more information about the components of a table view, see Creating a Table View.

Example
The following example shows a TableColumnHeader element whose width is 16 characters.

  XML

  <TableColumnHeader>
    <Label>Column 1</Label>
    <Width>16</Width>
    <Alignment>Left</Alignment>
  </TableColumnHeader>

See Also
Creating a Table View

TableColumnHeader Element for TableHeader for TableControl

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2730 -->

TableRowEntries Element
Defines the rows of the table.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element

Syntax
 XML

 <TableRowEntries>
   <TableRowEntry>...</TableRowEntry>
 </TableRowEntries>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
TableRowEntries element.

Attributes
None.

Child Elements

                                                                                   ﾉ   Expand table

 Element                                           Description

 TableRowEntry Element for TableRowEntries for     Required element.
 TableControl
                                                   Defines the data that is displayed in a row of the
                                                   table.

<!-- p.2731 -->

Parent Elements

                                                                            ﾉ   Expand table

 Element                               Description

 TableControl Element                  Defines a table format for a view.

Remarks
You must specify one or more TableRowEntry elements for the table view. There is no
maximum limit to the number of TableRowEntry elements that can be added nor is their order
significant.

For more information about the components of a table view, see Creating a Table View.

Example
The following example shows a TableRowEntries element that defines a row that displays the
values of two properties of the System.Diagnostics.Process object.

  XML

  <TableRowEntries>
    <TableRowEntry>
      <EntrySelectedBy>
        <TypeName>System.Diagnostics.Process</TypeName>
      </EntrySelectedBy>
      <TableColumnItems>
        <TableColumnItem>
          <PropertyName> Property for first column</PropertyName>
        </TableColumnItem>
        <TableColumnItem>
          <PropertyName> Property for second column</PropertyName>
        </TableColumnItem>
      </TableColumnItems>
    </TableRowEntry>
  </TableRowEntries>

See Also
Creating a Table View

TableControl Element

<!-- p.2732 -->

TableRowEntry Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2733 -->

TableColumnItems Element
Defines the properties or scripts whose values are displayed in a row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element for TableControl
     TableRowEntry Element for TableRowEntries for TableControl
     TableColumnItems Element for TableControlEntry for TableControl

Syntax
 XML

 <TableColumnItems>
   <TableColumnItem>...</TableColumnItem>
 </TableColumnItems>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
TableColumnItems element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                                      Description

 TableColumnItem Element for                  Required element.
 TableColumnItems for TableControl

<!-- p.2734 -->

 Element                                         Description

                                                 Defines the property or script whose value is displayed
                                                 in a column of the row.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                              Description

 TableRowEntry Element for TableRowEntries for        Defines the data that is displayed in a row of the
 TableControl                                         table.

Remarks
A TableColumnItem element is required for each column of the row. The first entry is displayed
in first column, the second entry in the second column, and so on.

For more information about the components of a table view, see Creating a Table View.

Example
The following example shows a TableColumnItems element that defines three properties of the
System.Diagnostics.Process object.

 XML

 <TableColumnItems>
   <TableColumnItem>
     <PropertyName>Status</PropertyName>
   </TableColumnItem>
   <TableColumnItem>
     <PropertyName>Name</PropertyName>
   </TableColumnItem>
   <TableColumnItem>
     <PropertyName>DisplayName</PropertyName>
   </TableColumnItem>
 </TableColumnItems>

See Also
Creating a Table View

<!-- p.2735 -->

TableColumnItem Element

TableRowEntry Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2736 -->

TableColumnItem Element
Defines the property or script whose value is displayed in the column of the row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     TableColumnItems Element
     TableColumnItem Element

Syntax
 XML

 <TableColumnItem>
   <Alignment>Left, Right, or Center</Alignment>
   <FormatString>FormatPattern</FormatString>
   <PropertyName>Nameof.NetProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </TableColumnItem>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
TableColumnItem element.

Attributes
None.

Child Elements

                                                                               ﾉ    Expand table

<!-- p.2737 -->

 Element                                       Description

 Alignment Element for TableColumnItem for     Optional element.
 TableControl
                                               Defines how the data in a column of the row is displayed.

 FormatString Element for TableColumnItem      Specifies a format pattern that is used to format the data
 for TableControl                              in the column of the row.

 PropertyName Element for TableColumnItem      Optional element.
 for TableControl
                                               Specifies the name of the property whose value is
                                               displayed.

 ScriptBlock Element for TableColumnItem for   Optional element.
 TableControl
                                               Specifies the script whose value is displayed in the
                                               column of a row.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                            Description

 TableColumnItems Element for TableControlEntry     Defines the properties or scripts whose values are
 for TableControl                                   displayed in the row.

Remarks
You can specify a property of an object or a script in each column of the row. If no child
elements are specified, the item is a placeholder, and no data is displayed.

For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableColumnItem element that displays the value of the Status property
of the System.Diagnostics.Process object.

 XML

 <TableColumnItem>
    <Alignment>Centered</Alignment>
   <PropertyName>Status</PropertyName>

<!-- p.2738 -->

 </TableColumnItem>

See Also
Creating a Table View

Alignment Element for TableColumnItem for TableControl

TableColumnItems Element

FormatString Element for TableColumnItem for TableControl

PropertyName Element for TableColumnItem for TableControl

ScriptBlock Element for TableColumnItem for TableControl

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2739 -->

Alignment Element for TableColumnItem
Defines how the data in a column of the row is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     TableColumnItems Element
     TableColumnItem Element
     Alignment Element

Syntax
 XML

 <Alignment>AlignmentType</Alignment>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
Alignment element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2740 -->

                                                                                          ﾉ   Expand table

 Element                      Description

 TableColumnItem              Defines a label, the width, and the alignment of the data for a column of the
 Element                      table.

Text Value
Specify one of the following values. (These values are not case-sensitive.)

      Left - Shifts the data displayed in the column to the left. (This is the default if this element
      is not specified.)
      Right - Shifts the data displayed in the column to the right.
      Center - Centers the data displayed in the column.

Remarks
For more information about the components of a table view, see Table View.

See Also
Table View

TableColumnItem Element

 Last updated on 05/20/2025

<!-- p.2741 -->

FormatString Element for TableColumnItem
for TableControl
Specifies a format pattern that defines how the property or script value of the table is
displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     TableColumnItems Element
     TableColumnItem Element
     FormatString Element

Syntax
 XML

 <FormatString>FormatPattern</FormatString>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
FormatString element.

Attributes
None.

Child Elements
None.

<!-- p.2742 -->

Parent Elements

                                                                                      ﾉ   Expand table

 Element                  Description

 TableColumnItem          Defines the property or script whose value is displayed in the column of the
 Element                  row.

Text Value
Specify the pattern that is used to format the data. For example, this pattern can be used to
format the value of any property that is of type System.TimeSpan: {0:MMM}{0:dd}{0:HH}:
{0:mm}.

Remarks
Format strings can be used when creating table views, list views, wide views, or custom views.
For more information about formatting a value displayed in a view, see Formatting Displayed
Data.

For more information about the components of a table view, see Table View.

Example
The following example shows how to define a formatting string for the value of the StartTime
property.

 XML

 <TableColumnItem>
   <PropertyName>StartTime</PropertyName>
   <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
 </TableColumnItem>

See Also
Creating a Table View

Formatting Displayed Data

TableColumnItem Element

<!-- p.2743 -->

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2744 -->

PropertyName Element for
TableColumnItem for TableControl
Specifies the property whose value is displayed in the column of the row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     TableColumnItems Element
     TableColumnItem Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
PropertyName element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2745 -->

                                                                                         ﾉ   Expand table

 Element                     Description

 TableColumnItem             Defines the property or script whose value is displayed in the column of the
 Element                     row.

Text Value
Specify the name of the property whose value is displayed.

Remarks
For more information about the components of a table view, see Creating a Table View.

Example
This example shows a TableColumnItem element that specifies the Status property of the
System.Diagnostics.Process object.

 XML

 <TableColumnItem>
    <Alignment>Centered</Alignment>
   <PropertyName>Status</PropertyName>
 </TableColumnItem>

See Also
Creating a Table View

TableColumnItem Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2746 -->

ScriptBlock Element for TableColumnItem
for TableControl
Specifies the script whose value is displayed in the column of the row.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     TableColumnItems Element
     TableColumnItem Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2747 -->

                                                                                          ﾉ   Expand table

 Element                      Description

 TableColumnItem              Defines the property or script whose value is displayed in the column of the
 Element                      row.

Text Value
Specify the script whose value is displayed.

Remarks
For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

TableColumnItem Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2748 -->

TableRowEntry Element
Defines the data that is displayed in a row of the table.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element for TableControl
     TableRowEntry Element for TableRowEntries

Syntax
 XML

 <TableRowEntry>
   <Wrap/>
   <EntrySelectedBy>...</EntrySelectedBy>
   <TableColumnItems>...</TableColumnItems>
 </TableRowEntry>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
TableRowEntry element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

<!-- p.2749 -->

 Element                                         Description

 EntrySelectedBy Element for TableRowEntry for   Required element.
 TableControl
                                                 Defines the objects whose property values are
                                                 displayed in the row.

 TableColumnItems Element for TableRowEntry      Required element.
 for TableControl
                                                 Defines the properties or scripts whose values are
                                                 displayed.

 Wrap Element for TableRowEntry for              Optional element.
 TableControl
                                                 Specifies that text that exceeds the column width is
                                                 displayed on the next line.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                       Description

 TableRowEntries Element for TableControl                      Defines the rows of the table.

Remarks
One TableColumnItems element and one EntrySelectedBy element must be specified.

For more information about the components of a table view, see Creating a Table View.

Example
The following example shows a TableRowEntry element that defines a row that displays the
values of two properties of the System.Diagnostics.Process object.

 XML

 <TableRowEntry>
   <EntrySelectedBy>
     <TypeName>System.Diagnostics.Process</TypeName>
   </EntrySelectedBy>
   <TableColumnItems>
     <TableColumnItem>
       <PropertyName> Property for first column</PropertyName>
     </TableColumnItem>

<!-- p.2750 -->

     <TableColumnItem>
       <PropertyName> Property for second column</PropertyName>
     </TableColumnItem>
   </TableColumnItems>
 </TableRowEntry>

See Also
Creating a Table View

EntrySelectedBy Element for TableRowEntry for TableControl

TableColumnItems Element for TableRowEntry for TableControl

TableRowEntries Element for TableControl

Wrap Element for TableRowEntry for TableControl

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2751 -->

EntrySelectedBy Element for
TableRowEntry
Defines the .NET types that use this definition of the table view or the condition that must exist
for this definition to be used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element

Syntax
 XML

 <EntrySelectedBy>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <SelectionCondition>...</SelectionCondition>
 </EntrySelectedBy>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EntrySelectedBy element.

Attributes
None.

Child Elements

<!-- p.2752 -->

                                                                                        ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Optional element.
 for TableControl
                                                  Defines the condition that must exist for this table
                                                  view definition to be used.

 SelectionSetName Element for EntrySelectedBy     Optional element.
 for TableControl
                                                  Specifies a set of .NET types that use this table view
                                                  definition.

 TypeName Element for EntrySelectedBy for         Optional element.
 TableControl
                                                  Specifies a .NET type that uses this table view
                                                  definition.

Parent Elements

                                                                                        ﾉ    Expand table

 Element                                     Description

 TableRowEntry Element for TableControl      Defines the data that is displayed in a row of the table.

Remarks
You must specify at least one type, selection set, or selection condition for a table view
definition. There is no maximum limit to the number of child elements that you can use.

Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or that a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for when a View Entry or Item is Used.

For more information about the components of a table view, see Creating a Table View.

Example
The following example shows a TableRowEntry element that is used to display the properties of
the System.Diagnostics.Process object.

<!-- p.2753 -->

 XML

 <TableRowEntry>
   <EntrySelectedBy>
     <TypeName>System.Diagnostics.Process</TypeName>
   </EntrySelectedBy>
   <TableColumnItems>
     <TableColumnItem>
       <PropertyName>PropertyForFirstColumn</PropertyName>
     </TableColumnItem>
     <TableColumnItem>
       <PropertyName>PropertyForSecondColumn</PropertyName>
     </TableColumnItem>
   </TableColumnItems>
 </TableRowEntry>

See Also
Creating a Table View

SelectionCondition Element for EntrySelectedBy for TableControl

SelectionSetName Element for EntrySelectedBy for TableControl

TableRowEntry Element for TableControl

TypeName Element for EntrySelectedBy for TableControl

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2754 -->

SelectionCondition Element for
EntrySelectedBy for TableControl
Defines the condition that must exist to use for this definition of the table view. There is no
limit to the number of selection conditions that can be specified for a table definition.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
     SelectionCondition Element

Syntax
 XML

 <SelectionCondition>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </SelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionCondition element.

Attributes
None.

Child Elements

<!-- p.2755 -->

                                                                                            ﾉ   Expand table

 Element                                                            Description

 PropertyName Element for SelectionCondition for                    Optional element.
 EntrySelectedBy for TableRowEntry
                                                                    Specifies the .NET property that triggers
                                                                    the condition.

 ScriptBlock Element for SelectionCondition for EntrySelectedBy     Optional element.
 for TableRowEntry
                                                                    Specifies the script that triggers the
                                                                    condition.

 SelectionSetName Element for SelectionCondition for                Optional element.
 EntrySelectedBy for TableRowEntry
                                                                    Specifies the set of .NET types that
                                                                    trigger the condition.

 TypeName Element for SelectionCondition for EntrySelectedBy        Optional element.
 for TableRowEntry
                                                                    Specifies a .NET type that triggers the
                                                                    condition.

Parent Elements

                                                                                            ﾉ   Expand table

 Element                             Description

 EntrySelectedBy Element for         Defines the .NET types that use this table entry or the condition that
 TableRowEntry                       must exist for this entry to be used.

Remarks
Each list entry must have at least one type name, selection set, or selection condition defined.

When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

For more information about how to use selection conditions, see Defining Conditions for when
a View Entry or Item is Used.

<!-- p.2756 -->

For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

Defining Conditions for When Data Is Displayed

EntrySelectedBy Element

PropertyName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

ScriptBlock Element for SelectionCondition for EntrySelectedBy for TableRowEntry

SelectionSetName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

TypeName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

Writing a Windows PowerShell Formatting and Types File

Last updated on 05/20/2025

<!-- p.2757 -->

PropertyName Element for
SelectionCondition for EntrySelectedBy for
TableRowEntry
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the table entry is used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements

<!-- p.2758 -->

None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines the condition that must exist for this table
 TableRowEntry                                        entry to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify at least one property name or a script block, but cannot
specify both. For more information about how selection conditions can be used, see Defining
Conditions for when a View Entry or Item is Used.

For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

Defining Conditions for When Data Is Displayed

ScriptBlock Element for SelectionCondition for EntrySelectedBy for TableRowEntry

SelectionCondition Element for EntrySelectedBy for TableRowEntry

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2759 -->

ScriptBlock Element for SelectionCondition
for EntrySelectedBy for TableControl
Specifies the script block that triggers the condition. When this script is evaluated to true , the
condition is met, and the table entry is used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

<!-- p.2760 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines the condition that must exist for this table
 TableRowEntry                                        entry to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify at least one script block or property name, but cannot
specify both. For more information about how to use selection conditions, see Defining
Conditions for when a View Entry or Item is Used.

For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

Defining Conditions for When Data Is Displayed

PropertyName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

SelectionCondition Element for EntrySelectedBy for TableRowEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025
