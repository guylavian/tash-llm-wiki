---
title: "How to use this documentation — pages 2761-2800"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2761-2800
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2761-2800
family: powershell
documentKind: "doc"
abstract: "SelectionSetName Element for SelectionCondition for EntrySelectedBy for TableControl Specifies the set of .NET types that trigger the condition. When any of the types in this set are present, the condition is met, and the object is displayed by using this definition of the table"
---

# How to use this documentation — pages 2761-2800

<!-- p.2761 -->

SelectionSetName Element for
SelectionCondition for EntrySelectedBy for
TableControl
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this definition of the table
view.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        TableControl Element
        TableRowEntries Element
        TableRowEntry Element
        EntrySelectedBy Element
        SelectionCondition Element
        SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements

<!-- p.2762 -->

None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to use for this
 for TableRowEntry                                definition of the table view.

Text Value
Specify the name of the selection set.

Remarks
The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Sets of Objects.

For more information about other components of a wide view, see Creating a Table View.

See Also
Creating a Table View

Defining Conditions for When Data Is Displayed

TypeName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

SelectionCondition Element for EntrySelectedBy for TableRowEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2763 -->

TypeName Element for SelectionCondition
for EntrySelectedBy for TableControl
Specifies a .NET type that triggers the condition. When this type is present, the condition is
met, and the table row is used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
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

<!-- p.2764 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines the condition that must exist for this table
 TableRowEntry                                        row to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
The selection condition can specify any number of .NET types or selection sets, but cannot
specify both. For more information about how to use selection conditions, see Defining
Conditions for when a View Entry or Item is Used.

For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

Defining Conditions for When Data Is Displayed

SelectionCondition Element for EntrySelectedBy for TableRowEntry

SelectionSetName Element for SelectionCondition for EntrySelectedBy for TableRowEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2765 -->

SelectionSetName Element for
EntrySelectedBy for TableControl
Specifies a set of .NET types the use this entry of the table view. There is no limit to the number
of selection sets that can be specified for an entry.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and parent elements.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2766 -->

                                                                                              ﾉ   Expand table

 Element                      Description

 EntrySelectedBy              Defines the .NET types that use this entry or the condition that must exist for
 Element                      this entry to be used.

Text Value
Specify the name of the selection set.

Remarks
Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you might want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Sets of objects
for a View.

If you specify a selection set for an entry, you cannot specify a type name. For more
information about how to specify a .NET type, see TypeName Element for EntrySelectedBy for
TableRowEntry.

For more information about the components of a table view, see Creating a Table View.

See Also
EntrySelectedBy Element

Defining Sets of objects for a View

Creating a Table View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2767 -->

TypeName Element for EntrySelectedBy for
TableControl
Specifies a .NET type that uses this entry of the table view. There is no limit to the number of
types that can be specified for a table entry.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element
     TableRowEntry Element
     EntrySelectedBy Element
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

<!-- p.2768 -->

                                                                                              ﾉ   Expand table

 Element                      Description

 EntrySelectedBy              Defines the .NET types that use this entry or the condition that must exist for
 Element                      this entry to be used.

Text Value
Specify the name of the .NET type.

Remarks
Each list entry must have at least one type name, selection set, or selection condition defined.

For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

EntrySelectedBy Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2769 -->

Wrap Element for TableRowEntry
Specifies that text that exceeds the column width is displayed on the next line. By default, text
that exceeds the column width is truncated.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     TableControl Element
     TableRowEntries Element for TableControl
     TableRowEntry Element for TableRowEntries for TableControl
     Wrap Element for TableRowEntry for TableControl

Syntax
 XML

 <Wrap/>

Attributes and Elements
The following sections describe attributes, child elements, and parent elements of the Wrap
element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                 ﾉ   Expand table

<!-- p.2770 -->

 Element                                         Description

 TableRowEntry Element for TableRowEntries for   Defines the data that is displayed in a row of the
 TableControl                                    table.

Remarks
For more information about the components of a table view, see Creating a Table View.

See Also
Creating a Table View

TableRowEntry Element for TableRowEntries for TableControl

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2771 -->

ViewSelectedBy Element
Defines the .NET objects that are displayed by the view. Each view must specify at least one
.NET object.

Schema
     ViewDefinitions Element
     View Element
     ViewSelectedBy Element

Syntax
  XML

  <ViewSelectedBy>
    <TypeName>Nameof.NetType</TypeName>
    <SelectionSetName>SelectionSet</SelectionSetName>
  </ViewSelectedBy>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
ViewSelectedBy element. This element must contain at least one TypeName or SelectionSetName

child element. There is no limit to the number of child elements that can be specified nor is
their order significant.

Attributes
None.

Child Elements

                                                                                ﾉ   Expand table

 Element                                    Description

 TypeName Element for ViewSelectedBy        Optional element.

<!-- p.2772 -->

 Element                                      Description

                                              Specifies a .NET object that is displayed by the view.

 SelectionSetName Element for                 Optional element.
 ViewSelectedBy
                                              Specifies a set of .NET objects that are displayed by the
                                              view.

Parent Elements

                                                                                        ﾉ   Expand table

 Element               Description

 View Element          Defines a view that displays one or more .NET objects.

Remarks
For more information about how this element is used in different views, see Table View
Components, List View Components, Wide View Components, and Custom Control
Components.

The SelectionSetName element is used when the formatting file defines a set of objects that are
displayed by multiple views. For more information about how selection sets are defined and
referenced, see Defining Sets of Objects.

Example
The following example shows how to specify the System.ServiceProcess.ServiceController
object for a list view. The same schema is used for table, wide, and custom views.

 XML

 <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <ListControl>...</ListControl>
 </View>

See Also

<!-- p.2773 -->

Creating a List View

Creating a Table View

Creating a Wide View

Creating Custom Controls

Defining Selection Sets

SelectionSetName Element for ViewSelectedBy

TypeName Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2774 -->

SelectionSetName Element for
ViewSelectedBy
Specifies a set of .NET objects that are displayed by the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ViewSelectedBy Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>Name of selection set<SelectionSetName>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2775 -->

 Element                        Description

 ViewSelectedBy Element         Defines the .NET objects that are displayed by the view.

Text Value
Specify the name of the selection set that is defined by the Name element for the selection set.

Remarks
You can use selection sets when you have a set of related objects that you want to reference by
using a single name, such as a set of objects that are related through inheritance. For more
information about defining and referencing selection sets, see Defining Sets of Objects.

Example
The following example shows how to specify a selection set for a list view. The same schema is
used for table, wide, and custom views.

  XML

  <View>
    <Name>Name of View</Name>
    <ViewSelectedBy>
      <SelectionSetName>NameofSelectionSet</SelectionSetName>>
    </ViewSelectedBy>
    <ListControl>...</ListControl>
  </View>

See Also
Defining Selection Sets

ViewSelectedBy Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2776 -->

TypeName Element for ViewSelectedBy
Specifies a .NET object that is displayed by the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ViewSelectedBy Element
     TypeName Element

Syntax
 XML

 <TypeName>FullyQualifiedTypeName</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent elements of the
TypeName element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                      ﾉ    Expand table

 Element                        Description

 ViewSelectedBy Element         Defines the .NET objects that are displayed by the view.

<!-- p.2777 -->

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
For more information about how this element is used in different views, see Creating a Table
View, Creating a List View, Creating a Wide View, and Custom View Components.

Example
The following example shows how to specify the System.ServiceProcess.ServiceController
object for a list view. The same schema is used for table, wide, and custom views.

  XML

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.ServiceProcess.ServiceController</TypeName>
    </ViewSelectedBy>
    <ListControl>...</ListControl>
  </View>

See Also
Creating a List View

Creating a Table View

Creating a Wide View

Creating Custom Controls

ViewSelectedBy Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2778 -->

WideControl Element
Defines a wide (single value) list format for the view. This view displays a single property value
or script value for each object.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        WideControl Element

Syntax
 XML

 <WideControl>
   <AutoSize/>
   <ColumnNumber>PositiveInteger</ColumnNumber>
   <WideEntries>...</WideEntries>
 </WideControl>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
WideControl element. You cannot specify the AutoSize and ColumnNumber elements at the same

time.

Attributes
None.

Child Elements

                                                                                  ﾉ   Expand table

<!-- p.2779 -->

 Element                              Description

 AutoSize Element for                 Optional element.
 WideControl
                                      Specifies whether the column size and the number of columns are
                                      adjusted based on the size of the data.

 ColumnNumber Element for             Optional element.
 WideControl
                                      Specifies the number of columns displayed in the wide view.

 WideEntries Element                  Required element.

                                      Provides the definitions of the wide view.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                Description

 View Element           Defines a view that is used to display one or more .NET objects.

Remarks
When defining a wide view, you can add the AutoSize element or the ColumnNumber but you
cannot add both.

In most cases, only one definition is required for each wide view, but it is possible to have
multiple definitions if you want to use the same view to display different .NET objects. In those
cases, you can provide a separate definition for each object or set of objects.

For more information about the components of a wide view, see Wide View Components.

Example
The following example shows a WideControl element that is used to display a property of the
System.Diagnostics.Process object.

 XML

 <View>
   <Name>process</Name>
   <ViewSelectedBy>
     <TypeName>System.Diagnostics.Process</TypeName>

<!-- p.2780 -->

   </ViewSelectedBy>
   <WideControl>
     <WideEntries>...</WideEntries>
   </WideControl>
 </View>

For a complete example of a wide view, see Wide View (Basic).

See Also
Autosize Element for WideControl

ColumnNumber Element for WideControl

View Element

WideEntries Element

Wide View (Basic)

Creating a Wide View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2781 -->

AutoSize Element for WideControl
Specifies whether the column size and the number of columns are adjusted based on the size
of the data.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     Autosize Element

Syntax
 XML

 <AutoSize/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
AutoSize element.

Attributes
None.

Child Elements
None

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2782 -->

 Element                      Description

 WideControl Element          Defines a wide (single value) list format for the view.

Remarks
When defining a wide view, you can add the AutoSize element or the ColumnNumber element,
but you cannot add both.

For more information about the components of a wide view, see Creating a Wide View.

For an example of a wide view, see Wide View (Basic).

See Also
ColumnNumber Element for WideControl

Creating a Wide View

WideControl Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2783 -->

ColumnNumber Element for WideControl
Specifies the number of columns displayed in the wide view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     ColumnNumber Element

Syntax
 XML

 <ColumnNumber>PositiveInteger</ColumnNumber>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ColumnNumber element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                       Description

 WideControl Element           Defines a wide (single value) list format for the view.

<!-- p.2784 -->

Text Value
Specify a positive integer value.

Remarks
When defining a wide view, you can add the AutoSize element or the ColumnNumber element,
but you cannot add both.

For more information about the components of a wide view, see Creating a Wide View.

For an example of a wide view, see Wide View (Basic).

See Also
Autosize Element for WideControl

Creating a Wide View

Wide View (Basic)

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2785 -->

WideEntries Element
Provides the definitions of the wide view. The wide view must specify one or more definitions.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element

Syntax
 XML

 <WideEntries>
   <WideEntry>...</WideEntry>
 </WideEntries>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
WideEntries element. At least one child element must be specified.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                          Description

 WideEntry Element                Provides a definition of the wide view.

Parent Elements

<!-- p.2786 -->

                                                                                            ﾉ   Expand table

 Element                          Description

 WideControl Element              Defines a wide (single value) list format for the view.

Remarks
A wide view is a list format that displays a single property value or script value for each object.
For more information about the components of a wide view, see Wide View Components.

Example
The following example shows a WideEntries element that defines a single WideEntry element.
The WideEntry element contains a single WideItem element that defines what property or script
value is displayed in the view.

  XML

  <WideControl>
    <WideEntries>
      <WideEntry>
        <WideItem>...</WideItem>
      <WideEntry>
    </WideEntries>
  </WideControl>

For a complete example of a wide view, see Wide View (Basic).

See Also
Creating a Wide View

WideControl Element

WideEntry Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2787 -->

WideEntry Element
Provides a definition of the wide view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element

Syntax
 XML

 <WideEntry>
   <EntrySelectedBy>...</EntrySelectedBy>
   <WideItem>...</WideItem>
 </WideEntry>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
WideEntry element. You must specify a single WideItem child element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                       Description

 EntrySelectedBy Element for   Optional element.
 WideEntry

<!-- p.2788 -->

 Element                      Description

                              Defines the .NET types that use this wide entry definition or the condition
                              that must exist for this definition to be used.

 WideItem Element             Required element.

                              Defines the property or script whose value is displayed.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                            Description

 WideEntries Element                Provides the definitions of the wide view.

Remarks
A wide view is a list format that displays a single property value or script value for each object.
Unlike other types of views, you can specify only one item element for each view definition. For
more information about the other components of a wide view, see Creating a Wide View.

Example
The following example shows a WideEntry element that defines a single WideItem element. The
WideItem element defines the property whose value is displayed in the view.

 XML

 <WideEntries>
   <WideEntry>
     <WideItem>
       <PropertyName>ProcessName</PropertyName>
     </WideItem>
   </WideEntry>
 </WideEntries>

For a complete example of a wide view, see Wide View (Basic).

See Also
Creating a Wide View

<!-- p.2789 -->

SelectionCondition Element for WideEntry

SelectionSetName Element for WideEntry

TypeName Element for WideEntry

WideEntries Element

WideItem Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2790 -->

EntrySelectedBy Element for WideEntry
Defines the .NET types that use this definition of the wide view or the condition that must exist
for this definition to be used.

Schema
Configuration Element ViewDefinitions Element View Element WideControl Element
WideEntries Element WideEntry Element EntrySelectedBy Element

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

                                                                                        ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Optional element.
 for WideEntry
                                                  Defines the condition that must exist for this wide view
                                                  definition to be used.

<!-- p.2791 -->

 Element                                          Description

 SelectionSetName Element for EntrySelectedBy     Optional element.
 for WideEntry
                                                  Specifies a set of .NET types that use this wide view
                                                  definition.

 TypeName Element for EntrySelectedBy for         Optional element.
 WideEntry
                                                  Specifies a .NET type that uses this wide view
                                                  definition.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                            Description

 WideEntry Element                  Provides a definition of the wide view.

Remarks
You must specify at least one type, selection set, or selection condition for a wide view
definition. There is no maximum limit to the number of child elements that you can use.

Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or that a specific property value or script
value evaluates to true . For more information about selection conditions, see Defining
Conditions for Displaying Data.

For more information about other components of a wide view, see Creating a Wide View.

See Also
WideEntry Element

SelectionCondition Element for EntrySelectedBy for WideEntry

SelectionSetName Element for EntrySelectedBy for WideEntry

TypeName Element for EntrySelectedBy for WideEntry

Creating a Wide View

<!-- p.2792 -->

Defining Conditions for Displaying Data

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2793 -->

SelectionCondition Element for
EntrySelectedBy for WideControl
Defines the condition that must exist for this definition to be used. There is no limit to the
number of selection conditions that can be specified for a wide entry definition.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
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
SelectionCondition element. You must specify a single PropertyName or ScriptBlock element.

The SelectionSetName and TypeName elements are optional. You can specify one of either
element.

Attributes
None.

<!-- p.2794 -->

Child Elements

                                                                                            ﾉ   Expand table

 Element                                                          Description

 PropertyName Element for SelectionCondition for                  Optional element.
 EntrySelectedBy for WideEntry
                                                                  Specifies the .NET property that triggers
                                                                  the condition.

 ScriptBlock Element for SelectionCondition for                   Optional element.
 EntrySelectedBy for WideEntry
                                                                  Specifies the script block that triggers the
                                                                  condition.

 SelectionSetName Element for SelectionCondition for              Optional element.
 EntrySelectedBy for WideEntry
                                                                  Specifies the set of .NET types that
                                                                  triggers the condition.

 TypeName Element for SelectionCondition for                      Optional element.
 EntrySelectedBy for WideEntry
                                                                  Specifies a .NET type that triggers the
                                                                  condition.

Parent Elements

                                                                                            ﾉ   Expand table

 Element                          Description

 EntrySelectedBy Element for      Defines the .NET types that use this wide entry or the condition that
 WideEntry                        must exist for this entry to be used.

Remarks
Each wide entry must have at least one type name, selection set, or selection condition defined.

When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

<!-- p.2795 -->

For more information about how to use selection conditions, see Defining Conditions for when
a View Entry or Item is Used.

For more information about other components of a wide view, see Creating a Wide View.

See Also
Creating a Wide View

Defining Conditions for When Data Is Displayed

EntrySelectedBy Element for WideEntry

PropertyName Element for SelectionCondition for EntrySelectedBy for WideEntry

ScriptBlock Element for SelectionCondition for EntrySelectedBy for WideEntry

SelectionSetName Element for SelectionCondition for EntrySelectedBy for WideEntry

TypeName Element for SelectionCondition for EntrySelectedBy for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2796 -->

PropertyName Element for
SelectionCondition for EntrySelectedBy for
WideEntry
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used.

      Configuration Element
      ViewDefinitions Element
      View Element
      WideControl Element
      WideEntries Element
      WideEntry Element
      EntrySelectedBy Element
      SelectionCondition Element
      PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

 C#

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

<!-- p.2797 -->

Child Elements
None.

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this
 for WideEntry                                    definition to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify at least one property name or a script to evaluate, but
cannot specify both. For more information about how to use selection conditions, see Defining
Conditions for when Data is Displayed.

For more information about other components of a wide view, see Wide View.

See Also
Creating a Wide View

Defining Conditions for When Data Is Displayed

ScriptBlock Element for SelectionCondition for EntrySelectedBy for WideEntry

SelectionCondition Element for EntrySelectedBy for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2798 -->

ScriptBlock Element for SelectionCondition
for EntrySelectedBy for WideControl
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the wide entry definition is used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     EntrySelectedBy Element
     SelectionCondition
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

<!-- p.2799 -->

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this
 for WideEntry                                    definition to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify at least one script or property name to evaluate, but
cannot specify both. For more information about how to use selection conditions, see Defining
Conditions for when Data is Displayed.

For more information about other components of a wide view, see Wide View.

See Also
Creating a Wide View

Defining Conditions for When Data Is Displayed

PropertyName Element for SelectionCondition for EntrySelectedBy for WideEntry

SelectionCondition Element for EntrySelectedBy for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2800 -->

SelectionSetName Element for
SelectionCondition for EntrySelectedBy for
WideEntry
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this definition of the wide
view.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        WideControl Element
        WideEntries Element
        WideEntry Element
        EntrySelectedBy Element
        SelectionCondition Element
        SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements
