---
title: "How to use this documentation — pages 2401-2440"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2401-2440
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2401-2440
family: powershell
documentKind: "doc"
abstract: "Parent Elements ﾉ Expand table Element Description SelectionCondition Element for EntrySelectedBy for Defines a condition that must exist for the Controls for Configuration common control definition to be used. Text Value Specify the script that is evaluated. Remarks The selecti"
---

# How to use this documentation — pages 2401-2440

<!-- p.2401 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 Controls for Configuration                           common control definition to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify a least one script or property name to evaluate, but
cannot specify both. For more information about how selection conditions can be used, see
Defining Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2402 -->

SelectionSetName Element for
SelectionCondition for Controls for
Configuration
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this control. This element is
used when defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
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

<!-- p.2403 -->

None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 Controls for Configuration                           control definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Sets of Objects.

The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for
Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for Configuration

Defining Conditions for When Data Is Displayed

Defining Selection Sets

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2404 -->

TypeName Element for SelectionCondition
for Controls for Configuration
Specifies a .NET type that triggers the condition. This element is used when defining a common
control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName Element.

Attributes
None.

Child Elements
None.

<!-- p.2405 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 CustomEntry for Configuration                        control definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
See Also
SelectionCondition Element for EntrySelectedBy for CustomEntry for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2406 -->

SelectionSetName Element for
EntrySelectedBy for Controls for
Configuration
Specifies a set of .NET types that use this definition of the control. This element is used when
defining a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element of Configuration
     Control Element for Controls for Configuration
     CustomControl Element for Control for Configuration
     CustomEntries Element for CustomControl for Configuration
     CustomEntry Element for CustomControl for Controls for Configuration
     EntrySelectedBy Element for CustomEntry for Controls for Configuration
     SelectionSetName Element for EntrySelectedBy for Controls for Configuration

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None

Child Elements

<!-- p.2407 -->

None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                   Description

 EntrySelectedBy Element for CustomEntry   Defines the .NET types that use this control definition or the
 for Controls for Configuration            condition that must exist for this definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Each control definition must have at least one type name, selection set, or selection condition
defined.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For more information about defining selection sets, see Defining Selection Sets.

See Also
EntrySelectedBy Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2408 -->

TypeName Element for EntrySelectedBy for
Controls for Configuration
Specifies a .NET type that uses this definition of the control. This element is used when defining
a common control that can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
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

<!-- p.2409 -->

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                   Description

 EntrySelectedBy Element for CustomEntry   Defines the .NET types that use this control definition or the
 for Controls for Configuration            condition that must exist for this definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
See Also
EntrySelectedBy Element for CustomEntry for Controls for Configuration

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2410 -->

Name Element for Control for Controls for
Configuration
Specifies the name of the control. This element is used when defining a common control that
can be used by all the views in the formatting file.

Schema
     Configuration Element
     Controls Element
     Control Element
     Name Element

Syntax
 XML

 <Name>NameOfControl</Name>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Name
element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                              ﾉ   Expand table

<!-- p.2411 -->

 Element                        Description

 Control Element for Controls   Defines a common control that can be used by all the views of the
 for Configuration              formatting file and the name that is used to reference the control.

Text Value
Specify the name that is used to reference this control.

Remarks
The name specified here can be used in the following elements to reference this control.

      When creating a table, list, wide or custom control view, the control can be specified by
      the following element: GroupBy Element for View

      When creating another common control, this control can be specified by the following
      element: ExpressionBinding Element for CustomItem for Controls for Configuration

      When creating a control that can be used by a view, this control can be specified by the
      following element: ExpressionBinding Element for CustomItem for Controls for View

See Also
Control Element for Controls for Configuration

ExpressionBinding Element for CustomItem for Controls for Configuration

ExpressionBinding Element for CustomItem for Controls for View

GroupBy Element for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2412 -->

DefaultSettings Element
Defines common settings that apply to all the views of the formatting file. Common settings
include displaying errors, wrapping text in tables, defining how collections are expanded, and
more.

Schema
     Configuration Element
     DefaultSettings Element

Syntax
 XML

 <DefaultSettings>
   <ShowError/>
   <DisplayError/>
  <PropertyCountForTable>NumberOfProperties</PropertyCountFortable>
   <WrapTables/>
   <EnumerableExpansions>...</EnumerableExpansions>
 </DefaultSettings>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
DefaultSettings element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                     Description

 DisplayError Element        Optional element.

<!-- p.2413 -->

 Element                 Description

                         Specifies that the string #ERR is displayed when an error occurs while
                         displaying a piece of data.

 EnumerableExpansions    Optional element.
 Element
                         Defines the different ways that .NET objects are expanded when they are
                         displayed in a view.

 PropertyCountForTable   Optional element.

                         Specifies the minimum number of properties that an object must have to
                         display the object in a table view.

 ShowError Element       Optional element.

                         Specifies that the full error record is displayed when an error occurs while
                         displaying a piece of data.

 WrapTables Element      Optional element.

                         Specifies that data in a table is moved to the next line if it does not fit into
                         the width of the column.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                   Description

 Configuration Element     Represents the top-level element of a formatting file.

Remarks
See Also
Configuration Element

DisplayError Element

EnumerableExpansions Element

PropertyCountForTable

ShowError Element

<!-- p.2414 -->

WrapTables Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2415 -->

DisplayError Element
Specifies that the string #ERR is displayed when an error occurs displaying a piece of data.

Schema
     Configuration Element
     DefaultSettings Element
     DisplayError Element

Syntax
 XML

 <DisplayError/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
DisplayError element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                   Description

 DefaultSettings Element   Defines common settings that apply to all the views of the formatting file.

Remarks

<!-- p.2416 -->

By default, when an error occurs while trying to display a piece of data, the location of the data
is left blank. When this element is set to true, the #ERR string will be displayed.

See Also
DefaultSettings Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2417 -->

EnumerableExpansions Element
Defines how .NET collection objects are expanded when they are displayed in a view.

Schema
       Configuration Element
       DefaultSettings Element
       EnumerableExpansions Element

Syntax
 XML

 <EnumerableExpansions>
   <EnumerableExpansion>...</EnumerableExpansion>
 </EnumerableExpansions>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EnumerableExpansions element. There is no limit to the number of child elements that you can

use.

Attributes
None.

Child Elements

                                                                                       ﾉ   Expand table

 Element                       Description

 EnumerableExpansion           Optional element.
 Element
                               Defines the specific .NET collection objects that are expanded when they
                               are displayed in a view.

<!-- p.2418 -->

Parent Elements

                                                                                           ﾉ   Expand table

 Element                      Description

 DefaultSettings Element      Defines common settings that apply to all the views of the formatting file.

Remarks
This element is used to define how collection objects and the objects in the collection are
displayed. In this case, a collection object refers to any object that supports the
System.Collections.ICollection interface.

See Also
Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2419 -->

EnumerableExpansion Element
Defines how specific .NET collection objects are expanded when they are displayed in a view.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element

Syntax
 XML

 <EnumerableExpansion>
   <EntrySelectedBy>...</EntrySelectedBy>
   <Expand>EnumOnly, CoreOnly, Both</Expand>
 </EnumerableExpansion>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EnumerableExpansion element.

Attributes
None.

Child Elements

                                                                                  ﾉ   Expand table

 Element                                   Description

 EntrySelectedBy Element for               Optional element.
 EnumerableExpansion
                                           Defines which .NET collection objects are expanded by
                                           this definition.

<!-- p.2420 -->

 Element                                      Description

 Expand Element                               Specifies how the collection object is expanded for this
                                              definition.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                      Description

 EnumerableExpansions         Defines the different ways that .NET collection objects are expanded when
 Element                      they are displayed in a view.

Remarks
This element is used to define how collection objects and the objects in the collection are
displayed. In this case, a collection object refers to any object that supports the
System.Collections.ICollection interface.

The default behavior is to display only the properties of the objects in the collection.

See Also
Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2421 -->

EntrySelectedBy Element for
EnumerableExpansion
Defines the .NET types that use this definition or the condition that must exist for this definition
to be used.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
     EntrySelectedBy Element for EnumerableExpansion

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

<!-- p.2422 -->

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy       Optional element.
 for EnumerableExpansion
                                                      Defines the condition that must exist to expand the
                                                      collection objects of this definition.

 SelectionSetName Element for EntrySelectedBy         Optional element.
 for EnumerableExpansion
                                                      Specifies a set of .NET types that use this definition of
                                                      how collection objects are expanded.

 TypeName Element for EntrySelectedBy for             Optional element.
 EnumerableExpansion
                                                      Specifies a .NET type that uses this definition of how
                                                      collection objects are expanded.

Parent Elements

                                                                                            ﾉ   Expand table

 Element                       Description

 EnumerableExpansion           Defines how specific .NET collection objects are expanded when they are
 Element                       displayed in a view.

Remarks
You must specify at least one type, selection set, or selection condition for a definition entry.
There is no maximum limit to the number of child elements that you can use.

Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or that a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for Displaying Data.

See Also
Defining Conditions for Displaying Data

EnumerableExpansion Element

SelectionCondition Element for EntrySelectedBy for EnumerableExpansion

<!-- p.2423 -->

SelectionSetName Element for EntrySelectedBy for EnumerableExpansion

TypeName Element for EntrySelectedBy for EnumerableExpansion

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2424 -->

SelectionCondition Element for
EntrySelectedBy for EnumerableExpansion
Defines the condition that must exist to expand the collection objects of this definition.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
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

Child Elements

<!-- p.2425 -->

                                                                                         ﾉ   Expand table

 Element                                                           Description

 PropertyName Element for SelectionCondition for                   Optional element.
 EntrySelectedBy for EnumerableExpansion
                                                                   Specifies the .NET property that
                                                                   triggers the condition.

 ScriptBlock Element for SelectionCondition for EntrySelectedBy    Optional element.
 for EnumerableExpansion
                                                                   Specifies the script that triggers the
                                                                   condition.

 SelectionSetName Element for SelectionCondition for               Optional element.
 EntrySelectedBy for EnumerableExpansion
                                                                   Specifies the set of .NET types that
                                                                   triggers the condition.

 TypeName Element for SelectionCondition for EntrySelectedBy       Optional element.
 for EnumerableExpansion
                                                                   Specifies a .NET type that triggers the
                                                                   condition.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                        Description

 EntrySelectedBy Element for                    Defines which .NET collection objects are expanded by
 EnumerableExpansion                            this definition.

Remarks
Each definition must have at least one type name, selection set, or selection condition defined.

When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

For more information about how to use selection conditions, see Defining Conditions for
Displaying Data.

<!-- p.2426 -->

For more information about other components of a wide view, see Wide View.

See Also
Defining Conditions for When Data Is Displayed

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2427 -->

PropertyName Element for
SelectionCondition for Controls for View
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the entry is used. This element is used when
defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element for Controls for View
     CustomControl Element for Control for Controls for View
     CustomEntries Element for CustomControl for Controls for View
     CustomEntry Element for CustomEntries for Controls for View
     EntrySelectedBy Element for CustomEntry for Controls for View
     SelectionCondition Element for EntrySelectedBy for Controls for View
     PropertyName Element for SelectionCondition for Controls for View

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

<!-- p.2428 -->

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the control
 Controls for View                                    definition to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify a least one property name or a script, but cannot specify
both. For more information about how selection conditions can be used, see Defining
Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2429 -->

ScriptBlock Element for SelectionCondition
for Controls for View
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the definition is used. This element is used when defining controls that
can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
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

<!-- p.2430 -->

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the control
 Controls for View                                    definition to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify a least one script or property name to evaluate, but
cannot specify both. For more information about how selection conditions can be used, see
Defining Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2431 -->

SelectionSetName Element for
SelectionCondition for EntrySelectedBy for
EnumerableExpansion
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansions Element
     EntrySelectedBy Element
     SelectionCondition Element
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

<!-- p.2432 -->

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to expand the
 for EnumerableExpansion                          collection objects of this definition.

Text Value
Specify the name of the selection set.

Remarks
The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for
Displaying Data.

Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Selection Sets.

See Also
Defining Selection Sets

SelectionCondition Element for EntrySelectedBy for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2433 -->

TypeName Element for SelectionCondition
for EntrySelectedBy for
EnumerableExpansion
Specifies a .NET type that triggers the condition.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansions Element
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

Parent Elements

<!-- p.2434 -->

                                                                                     ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to expand the
 for EnumerableExpansion                          collection objects of this definition.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks

See Also
SelectionCondition Element for EntrySelectedBy for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2435 -->

SelectionSetName Element for
EntrySelectedBy for EnumerableExpansion
Specifies the set of .NET types that are expanded by this definition.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
     EntrySelectedBy Element
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
None.

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2436 -->

 Element                                   Description

 EntrySelectedBy Element for               Defines the .NET collection objects that are expanded by
 EnumerableExpansion                       this definition.

Text Value
Specify the name of the selection set.

Remarks
Each definition must specify one or more type names, a selection set, or a selection condition.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you might want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Sets of Objects
for a View.

See Also
Defining Selection Sets

EntrySelectedBy Element for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2437 -->

TypeName Element for EntrySelectedBy for
EnumerableExpansion
Specifies a .NET type that is expanded by this definition. This element is used when defining a
default settings.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
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

<!-- p.2438 -->

                                                                                        ﾉ   Expand table

 Element                               Description

 EntrySelectedBy Element for           Defines the .NET types that use this definition or the condition
 EnumerableExpansion                   that must exist for this definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks

See Also
EntrySelectedBy Element for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2439 -->

Expand Element
Specifies how the collection object is expanded for this definition.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
     Expand Element

Syntax
 XML

 <Expand>EnumOnly, CoreOnly, Both</Expand>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
Expand element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                     Description

 EnumerableExpansion         Defines how specific .NET collection objects are expanded when they are
 Element                     displayed in a view.

<!-- p.2440 -->

Text Value
Specify one of the following values:

      EnumOnly: Displays only the properties of the objects in the collection.

      CoreOnly: Displays only the properties of the collection object.

      Both: Displays the properties of the objects in the collection and the properties of the
      collection object.

Remarks
This element is used to define how collection objects and the objects in the collection are
displayed. In this case, a collection object refers to any object that supports the
System.Collections.ICollection interface.

The default behavior is to display only the properties of the objects in the collection.

See Also
Writing a PowerShell Formatting File

 Last updated on 05/20/2025
