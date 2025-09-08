# SASS/SCSS Advanced Project

This project contains advanced SASS/SCSS exercises covering various preprocessor features including variables, nesting, mixins, loops, functions, and more complex programming concepts.

## Project Overview

This collection of SASS files demonstrates mastery of CSS preprocessor concepts from basic variables to advanced programming features like custom functions and sorting algorithms.

## Prerequisites

- Node.js (v20.16.0 or higher)
- SASS compiler (`npm install -g sass`)
- Basic understanding of CSS
- Text editor or IDE

## Installation & Setup

1. Install Node.js from [nodejs.org](https://nodejs.org)
2. Install SASS globally:

   ```bash
   npm install -g sass
   ```

3. Verify installation:

   ```bash
   sass --version
   ```

## Usage

To compile any SASS file:

```bash
sass filename.scss
```

To compile with output file:

```bash
sass input.scss output.css
```

## Tasks Checklist

### Basic SASS Features

- [ ] **0. Always debugging!** (`0-debug_log.scss`)
  - Write a SASS file that prints "Hello world" in the debug output
  - Uses `@debug` directive

- [ ] **1. Color variable** (`1-color_variable.scss`)
  - Assigns text color `#3D3D3D` to `body` and `p` tags using a SASS variable
  - Demonstrates basic variable usage

- [ ] **2. Colors** (`2-color_variables.scss`)
  - Uses two SASS variables for text color `#3D3D3D` and background color `#6D6D6D`
  - Applies to `body`, `p`, and `h2` tags

### Nesting Features

- [ ] **3. Nested tag** (`3-nested_tag.scss`)
  - Sets margin and padding for `body` tags
  - Uses nested declarations for `p` tags inside `body`

- [ ] **4. Nested class** (`4-nested_class.scss`)
  - Applies text color to elements inside `body` tags
  - Uses nested `.red` class selector

- [ ] **5. Nested child** (`5-nested_child.scss`)
  - Uses direct child selector (`>`) for `.red` class
  - Demonstrates parent-child relationship in nesting

- [ ] **6. Nested hover** (`6-nested_hover.scss`)
  - Implements hover states using nested pseudo-classes
  - Uses `&:hover` syntax for button elements

- [ ] **7. Nested and nested again** (`7-nested_deeper.scss`)
  - Demonstrates deep nesting with multiple levels
  - Font sizes for `body`, `h1`, and `h1.smaller`

### Advanced Features

- [ ] **8. Margin mixin** (`8-mixin_margins.scss`)
  - Creates reusable mixin for left and right margins
  - Applies to `body` and `div` tags with different values

- [ ] **9. Extended** (`9-extend_list.scss`)
  - Uses `@extend` to share styles between classes
  - Creates `.info`, `.success`, and `.warning` classes

- [ ] **10. Import colors** (`10-import_colors.scss` & `10-colors.scss`)
  - Demonstrates `@import` functionality
  - Separates color variables into external file

### Loops and Control Structures

- [ ] **11. For each** (`11-loop_photos.scss` & `11-photos.scss`)
  - Uses `@each` statement to iterate through list
  - Creates dynamic photo classes with background images

- [ ] **12. Loop Headers** (`12-loop_header.scss`)
  - Uses `@for` loop to create `h1` through `h5` with progressive font sizes
  - Demonstrates loop iteration from 1 to 5

- [ ] **13. Columns and operators** (`100-loop_col.scss`)
  - Creates responsive column classes using mathematical operators
  - Uses `@for` loop with division operations

### Responsive Design

- [ ] **14. Media query #0** (`101-media_query.scss`)
  - Basic media query implementation
  - Responsive font sizes for different screen widths

- [ ] **15. Media query #1** (`102-media_query.scss`)
  - Multiple nested media queries
  - Complex responsive behavior with class-specific rules

### Advanced Programming

- [ ] **16. Sort!** (`103-sort_strings.scss` & `103-sort_list.scss`)
  - Custom sorting function implementation
  - Advanced string manipulation and comparison
  - Demonstrates SASS programming capabilities

## File Structure

```text
sass_scss/
├── 0-debug_log.scss          # Debug output
├── 1-color_variable.scss     # Single variable
├── 2-color_variables.scss    # Multiple variables
├── 3-nested_tag.scss         # Basic nesting
├── 4-nested_class.scss       # Nested classes
├── 5-nested_child.scss       # Child selectors
├── 6-nested_hover.scss       # Pseudo-classes
├── 7-nested_deeper.scss      # Deep nesting
├── 8-mixin_margins.scss      # Mixins
├── 9-extend_list.scss        # Extend functionality
├── 10-colors.scss            # Color variables file
├── 10-import_colors.scss     # Import usage
├── 11-photos.scss            # Names list
├── 11-loop_photos.scss       # Each loop
├── 12-loop_header.scss       # For loop
├── 100-loop_col.scss         # Mathematical operations
├── 101-media_query.scss      # Basic media queries
├── 102-media_query.scss      # Advanced media queries
├── 103-sort_list.scss        # Data for sorting
└── 103-sort_strings.scss     # Sorting algorithm
```

## Key SASS Concepts Covered

### Variables

```scss
$primary-color: #3D3D3D;
$background-color: #6D6D6D;
```

### Nesting

```scss
.parent {
  property: value;
  
  .child {
    property: value;
  }
  
  &:hover {
    property: value;
  }
}
```

### Mixins

```scss
@mixin margin-lr($left, $right) {
  margin-left: $left;
  margin-right: $right;
}

.element {
  @include margin-lr(10px, 15px);
}
```

### Extend

```scss
.base-class {
  font-size: 12px;
}

.extended-class {
  @extend .base-class;
  color: red;
}
```

### Loops

```scss
@for $i from 1 through 5 {
  .col-#{$i} {
    width: 100% / $i;
  }
}

@each $name in $list {
  .#{$name} {
    background: url("#{$name}.jpg");
  }
}
```

### Functions

```scss
@function calculate-width($columns) {
  @return 100% / $columns;
}
```

## Testing Your Code

To test each file, use the SASS compiler:

```bash
# Basic compilation
sass 0-debug_log.scss

# With specific output format
sass 1-color_variable.scss | tail -n +2

# Check debug output
sass 0-debug_log.scss | head -n 0
```

## Expected Output Examples

### Debug Output

```text
0-debug_log.scss:2 DEBUG: Hello world
```

### Color Variables

```css
body {
  color: #3D3D3D; 
}

p {
  color: #3D3D3D;
}
```

### Nested Declarations

```css
body {
  margin: 0px;
  padding: 0px; 
}
  body p {
    margin: 10px; 
}
```

## Real-World Applications

- **Component Libraries**: Organizing styles with nesting and mixins
- **Design Systems**: Using variables for consistent theming
- **Responsive Design**: Media queries with nested selectors
- **Performance**: Extends for efficient CSS output
- **Maintainability**: Functions and loops for DRY principles

## Contributing

This project is part of the ALX curriculum. Follow the specific requirements for each task and ensure your SASS compiles without errors.

## Repository Information

- **Repository**: alx-frontend-for-fun
- **Directory**: sass_scss
- **Level**: Advanced

## Author

ALX Student - Advanced Frontend Development

## License

Educational use - ALX Curriculum
