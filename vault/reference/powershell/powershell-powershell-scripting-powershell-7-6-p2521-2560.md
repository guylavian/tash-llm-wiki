---
title: "How to use this documentation — pages 2521-2560"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2521-2560
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2521-2560
family: powershell
documentKind: "doc"
abstract: "Parent Elements ﾉ Expand table Element Description SelectionCondition Element for EntrySelectedBy for Defines a condition that must exist for the CustomControl for View control definition to be used. Text Value Specify the script that is evaluated. Remarks The selection conditio"
---

# How to use this documentation — pages 2521-2560

<!-- p.2521 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 CustomControl for View                               control definition to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify a least one script or property name to evaluate, but
cannot specify both. For more information about how selection conditions can be used, see
Defining Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2522 -->

SelectionSetName Element for
SelectionCondition for Controls for View
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met and the object is displayed using this control. This element is used
when defining controls that can be used by a view.

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
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

<!-- p.2523 -->

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the control
 Controls for View                                    definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Selection Sets.

The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for
Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for Controls for View

Defining Conditions for When Data Is Displayed

Defining Selection Sets

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2524 -->

TypeName Element for SelectionCondition
for Controls for View
Specifies a .NET type that triggers the condition. This element is used when defining controls
that can be used by a view.

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

<!-- p.2525 -->

None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the control
 Controls for View                                    definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
See Also
SelectionCondition Element for EntrySelectedBy for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2526 -->

SelectionSetName Element for
EntrySelectedBy for Controls for View
Specifies a set of .NET types that use this definition of the control. This element is used when
defining controls that can be used by a view.

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
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None

Child Elements

<!-- p.2527 -->

None.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                 Description

 EntrySelectedBy Element for             Defines the .NET types that use this control definition or the
 CustomEntry for Controls for View       condition that must exist for this definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Each control definition must have at least one type name, selection set, or selection condition
defined.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For more information about defining selection sets, see Defining Selection Sets.

See Also
EntrySelectedBy Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2528 -->

TypeName Element for EntrySelectedBy for
Controls for View
Specifies a .NET type that uses this definition of the control. This element is used when defining
controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
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

<!-- p.2529 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                               Description

 EntrySelectedBy Element for           Defines the .NET types that use this control definition or the
 CustomEntry for Controls for View     condition that must exist for this definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
See Also
EntrySelectedBy Element for CustomEntry for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2530 -->

Name Element for Control for Controls for
View
Specifies the name of the control.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     Name Element

Syntax
 XML

 <Name>ControlName</Name>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Name
element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                              ﾉ   Expand table

<!-- p.2531 -->

 Element                        Description

 Control Element for Controls   Defines a control that can be used by the view and the name that is used
 for View                       to reference the control.

Text Value
Specify the name that is used to reference the control.

Remarks
The name specified here can be used in the following elements to reference this control.

      When creating a table, list, wide or custom control view, the control can be specified by
      the following element: GroupBy Element for View

      When creating another control that can be used by a view, this control can be specified
      by the following element: ExpressionBinding Element for CustomItem for Controls for
      View

See Also
GroupBy Element for View

ExpressionBinding Element for CustomItem for Controls for View

Control Element for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2532 -->

CustomControl Element for View
Defines a custom control format for the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element

Syntax
 XML

 <CustomControl>
   <CustomEntries>...</CustomEntries>
 </CustomControl>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControl element. You must specify one child element.

Attributes
None.

Child Elements

                                                                                      ﾉ   Expand table

 Element                                            Description

 CustomEntries Element for CustomControl for View   Required element.

                                                    Provides the definitions of the custom control view.

Parent Elements

<!-- p.2533 -->

                                                                                          ﾉ   Expand table

 Element               Description

 View Element          Defines a view that is used to display one or more .NET objects.

Remarks
In most cases, only one definition is required for each control view, but it is possible to provide
multiple definitions if you want to use the same view to display different .NET objects. In those
cases, you can provide a separate definition for each object or set of objects.

See Also
CustomEntries Element for CustomControl for View

View Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2534 -->

CustomEntries Element for CustomControl
for View
Provides the definitions of the custom control view. The custom control view must specify one
or more definitions.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element

Syntax
 XML

 <CustomEntries>
   <CustomEntry>...</CustomEntry>
 </CustomEntries>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControlEntries element. You must specify one or more child elements.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                                          Description

 CustomEntry Element for CustomEntries for View   Required element.

<!-- p.2535 -->

 Element                                          Description

                                                  Provides a definition of the custom control view.

Parent Elements

                                                                                    ﾉ     Expand table

 Element                                  Description

 CustomControl Element for View           Required element.

                                          Defines a custom control format for the view.

Remarks
In most cases, a control has only one definition, which is defined in a single CustomEntry
element. However it is possible to have multiple definitions if you want to use the same control
to display different .NET objects. In those cases, you can define a CustomEntry element for each
object or set of objects.

See Also
CustomControl Element for View

CustomEntry Element for CustomEntries for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2536 -->

CustomEntry Element for CustomEntries for
CustomControl for View
Provides a definition of the custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2537 -->

 Element                         Description

 EntrySelectedBy Element for     Optional element.
 CustomEntry for View
                                 Defines the .NET types that use the definition of the custom control
                                 view or the condition that must exist for this definition to be used.

 CustomItem Element for          Defines a control for the custom control definition.
 CustomEntry for View

Parent Elements

                                                                                        ﾉ   Expand table

 Element                           Description

 CustomEntries Element for         Provides the definitions of the custom control view. The custom
 CustomControl for View            control view must specify one or more definitions.

Remarks
In most cases, only one definition is required for each custom control view, but it is possible to
have multiple definitions if you want to use the same view to display different .NET objects. In
those cases, you can provide a separate definition for each object or set of objects.

See Also
CustomControl Element for View

CustomItem Element for CustomEntry for View

EntrySelectedBy Element for CustomEntry for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2538 -->

CustomItem Element for CustomEntry for
CustomControl for View
Defines what data is displayed by the custom control view and how it is displayed. This element
is used when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element

Syntax
 XML

 <CustomItem>
   <ExpressionBinding>...</ExpressionBinding>
   <Frame>...</Frame>
   <NewLine/>
   <Text>TextToDisplay</Text>
 </CustomItem>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomItem element.

Attributes
None.

Child Elements

<!-- p.2539 -->

                                                                                      ﾉ   Expand table

 Element                                         Description

 ExpressionBinding Element for CustomItem for    Optional element.
 CustomControl for View
                                                 Defines the data that is displayed by the control.

 Frame Element for CustomItem for                Optional element.
 CustomControl for View
                                                 Defines what data is displayed by the custom control
                                                 view and how it is displayed.

 NewLine Element for CustomItem for Custom       Optional element.
 Control for View
                                                 Adds a blank line to the display of the control.

 Text Element for CustomItem for CustomControl   Optional element.
 for View
                                                 Specifies additional text to the data displayed by the
                                                 control.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                                    Description

 CustomEntry Element for CustomEntries for CustomControl    Provides a definition of the custom control
 for View                                                   view.

Remarks
See Also
CustomEntry Element for CustomEntries for View

ExpressionBinding Element for CustomItem for CustomControl for View

Frame Element for CustomItem for CustomControl for View

NewLine Element for CustomItem for CustomControl for View

Text Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

<!-- p.2540 -->

Last updated on 05/20/2025

<!-- p.2541 -->

ExpressionBinding Element for CustomItem
for CustomControl for View
Defines the data that is displayed by the control. This element is used when defining a custom
control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </ExpressionBinding>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ExpressionBinding element.

Attributes
None.

<!-- p.2542 -->

Child Elements

                                                                                        ﾉ   Expand table

Element                                                     Description

CustomControl Element                                       Optional element.

                                                            Defines a control that is used by this control.

CustomControlName Element for ExpressionBinding for         Optional element.
CustomControl for View
                                                            Specifies the name of a common control or
                                                            a view control.

EnumerateCollection Element for ExpressionBinding for       Optional element.
CustomControl for View
                                                            Specified that the elements of collections
                                                            are displayed.

ItemSelectionCondition Element for ExpressionBinding for    Optional element.
CustomControl for View
                                                            Defines the condition that must exist for this
                                                            control to be used.

PropertyName Element for ExpressionBinding for              Optional element.
CustomControl for View
                                                            Specifies the .NET property whose value is
                                                            displayed by the control.

ScriptBlock Element for ExpressionBinding for               Optional element.
CustomCustomControl for View
                                                            Specifies the script whose value is displayed
                                                            by the control.

Parent Elements

                                                                                        ﾉ   Expand table

Element                                          Description

CustomItem Element for CustomEntry for           Defines what data is displayed by the custom control
CustomControl for View                           view and how it is displayed.

Remarks
See Also

<!-- p.2543 -->

CustomControlName Element for ExpressionBinding for CustomControl for View

EnumerateCollection Element for ExpressionBinding for CustomControl for View

ItemSelectionCondition Element for ExpressionBinding for CustomControl for View

PropertyName Element for ExpressionBinding for CustomControl for View

ScriptBlock Element for ExpressionBinding for CustomControl for View

CustomItem Element for CustomEntry for CustomControl for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2544 -->

CustomControlName Element for
ExpressionBinding for CustomControl for
View
Specifies the name of a common control or a view control. This element is used when defining
a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     CustomControlName Element

Syntax
 XML

 <CustomControlName>NameofCustomControl</CustomControlName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControlName element.

Attributes
None.

Child Elements

<!-- p.2545 -->

None.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                      Description

 ExpressionBinding Element for CustomItem     Defines the data that is displayed by the control.

Text Value
Specify the name of the control.

Remarks
You can create common controls that can be used by all the views of a formatting file and you
can create view controls that can be used by a specific view. The names of these controls are
specified by the following elements.

      Name Element for Control for Controls for Configuration

      Name Element for Control for Controls for View

See Also
Name Element for Control for Controls for Configuration

Name Element for Control for Controls for View

ExpressionBinding Element for CustomItem

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2546 -->

EnumerateCollection Element for
ExpressionBinding for CustomControl for
View
Specifies that the elements of collections are displayed. This element is used when defining a
custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     EnumerateCollection Element

Syntax
 XML

 <EnumerateCollection/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EnumerateCollection element.

Attributes
None.

Child Elements

<!-- p.2547 -->

None.

Parent Elements

                                                                                  ﾉ   Expand table

 Element                                    Description

 ExpressionBinding Element for CustomItem   Defines the data that is displayed by the control.

Remarks

See Also
ExpressionBinding Element for CustomItem

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2548 -->

ItemSelectionCondition Element for
ExpressionBinding for CustomControl
Defines the condition that must exist for this control to be used. There is no limit to the
number of selection conditions that can be specified for a control item. This element is used
when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
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

<!-- p.2549 -->

Child Elements

                                                                                  ﾉ    Expand table

 Element                                                    Description

 PropertyName Element for ItemSelectionCondition for        Optional element.
 CustomControl for View (Format
                                                            Specifies the .NET property that
                                                            triggers the condition.

 ScriptBlock Element for ItemSelectionCondition for         Optional element.
 CustomControl for View
                                                            Specifies the script that triggers the
                                                            condition.

Parent Elements

                                                                                  ﾉ    Expand table

 Element                                                 Description

 ExpressionBinding Element for CustomItem for            Defines the data that is displayed by the
 CustomControl for View                                  control.

Remarks
You can specify one property name or a script for this condition but cannot specify both.

See Also
Writing a PowerShell Formatting File

ExpressionBinding Element for CustomItem for CustomControl for View

 Last updated on 05/20/2025

<!-- p.2550 -->

PropertyName Element for
ItemSelectionCondition for CustomControl
for View
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element for CustomControl for View
     CustomEntry Element for CustomEntries for View
     CustomItem Element for CustomEntry for View
     ExpressionBinding Element for CustomItem for CustomControl for View
     ItemSelectionCondition Element for Expression Binding for CustomControl for View
     PropertyName Element for ItemSelectionCondition for CustomControl for View (Format

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

<!-- p.2551 -->

Child Elements
None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                     Description

 ItemSelectionCondition Element for Expression Binding for   Defines the condition that must exist for
 CustomControl for View                                      this control to be used.

Text Value
Specify the name of the .NET property that triggers the condition.

Remarks
If this element is used, you cannot specify the ScriptBlock element when defining the selection
condition.

See Also
ScriptBlock Element for ItemSelectionCondition for CustomControl for View

ItemSelectionCondition Element for Expression Binding for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2552 -->

ScriptBlock Element for
ItemSelectionCondition for CustomControl
for View
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the control is used. This element is used when defining a custom control
view.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        CustomControl Element
        CustomEntries Element
        CustomEntry Element
        CustomItem Element
        ExpressionBinding Element
        ItemSelectionCondition Element
        ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

<!-- p.2553 -->

Child Elements
None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                     Description

 ItemSelectionCondition Element for Expression Binding for   Defines the condition that must exist for
 CustomControl for View                                      this control to be used.

Text Value
Specify the script that is evaluated.

Remarks
If this element is used, you cannot specify the PropertyName element when defining the
selection condition.

See Also
PropertyName Element for ItemSelectionCondition for CustomControl for View

ItemSelectionCondition Element for Expression Binding for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2554 -->

PropertyName Element for
ExpressionBinding for CustomControl for
View
Specifies the .NET property whose value is displayed by the control. This element is used when
defining a custom control view

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
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

<!-- p.2555 -->

None.

Parent Elements

                                                                                 ﾉ   Expand table

 Element                                                 Description

 ExpressionBinding Element for CustomItem for            Defines the data that is displayed by the
 CustomControl for View                                  control.

Text Value
Specify the name of the .NET property whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2556 -->

ScriptBlock Element for ExpressionBinding
for CustomControl for View
Specifies the script whose value is displayed by the control. This element is used when defining
a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
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

<!-- p.2557 -->

Parent Elements

                                                                                      ﾉ   Expand table

 Element                                                      Description

 ExpressionBinding Element for CustomItem for                 Defines the data that is displayed by the
 CustomControl for View                                       control.

Text Value
Specify the script whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2558 -->

Frame Element for CustomItem for
CustomControl for View
Defines how the data is displayed, such as shifting the data to the left or right. This element is
used when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element

Syntax
 XML

 <Frame>
   <LeftIndent>NumberOfCharactersToShift</LeftIndent>
   <RightIndent>NumberOfCharactersToShift</RightIndent>
   <FirstLineHanging>NumberOfCharactersToShift</FirstLineHanging>
   <FirstLineIndent>NumberOfCharactersToShift</FirstLineIndent>
   <CustomItem>...</CustomItem>
 </Frame>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Frame
element.

Attributes
None.

<!-- p.2559 -->

Child Elements

                                                                                            ﾉ   Expand table

 Element                    Description

 CustomItem Element         Required Element

 FirstLineHanging Element   Optional element.

                            Specifies how many characters the first line of data is shifted to the left.

 FirstLineIndent Element    Optional element.

                            Specifies how many characters the first line of data is shifted to the right.

 LeftIndent Element         Optional element.

                            Specifies how many characters the data is shifted away from the left margin.

 RightIndent Element        Optional element.

                            Specifies how many characters the data is shifted away from the right margin.

Parent Elements

                                                                                            ﾉ   Expand table

 Element                                     Description

 CustomItem Element for CustomEntry for      Defines what data is displayed by the control and how it is
 View                                        displayed.

Remarks
You cannot specify the FirstLineHanging and the FirstLineIndent elements in the same Frame
element.

See Also
FirstLineHanging Element

FirstLineIndent Element

LeftIndent Element

<!-- p.2560 -->

RightIndent Element

CustomItem Element for CustomEntry for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025
