## Test Cases

# Use case name
    Navigating
# Description
    Navigating to new and existing movie lists
# Pre-conditions
    Web page loads
# Test steps
    1. Load home page
    2. Click/Navigate to "Create New List" Page/Button
    3. Return to Home Page
    4. Click/Navigate to "View Existing Lists" Page/Button
# Expected result
    User should be able navigate to all three pages (Home, Create, View)
# Actual result
    xxx
# Status (Pass/Fail)
    Pass
# Notes
    Additional functionality for 'Create' and 'View' to be handled in additional test cases
# Post-conditions
    User has navigated all three pages



# Use case name
    Create New List
# Description
    User creates new movie preference settings and list
# Pre-conditions
    User has movie preferences
    User has navigated to "Create New List" Page
# Test steps
    1. Enter new list name
    2. Enter genre preferences
    3. Enter actor/actress preferences
    4. Enter date preferences
    5. Enter language preferences
    6. Enter rating preferences
    7. Enter location preferences
    8. Enter user rating range preferences
    9. Generate preview list
    10. Save list
# Expected result
    Named list of movie preferences is saved to the database
# Actual result
    xxx
# Status (Pass/Fail)
    Pass
# Notes
    N/A
# Post-conditions
    List of user's movie choices



# Use case name
    View Movie Lists
# Description
    User can view and browse created movie lists
# Pre-conditions
    Movie lists have been created
    User has navigated to "View Existing Lists" Page
# Test steps
    1. User can browse list of created movie lists
    2. Lists can be sorted alphabetically and by date
    3. User can search for a specific list name
    4. User can open/view a list of movies

# Expected result
    User has navigated and opened an existing list
# Actual result
    xxx
# Status (Pass/Fail)
    Pass
# Notes
    N/A
# Post-conditions
    View of existing movie list