## Project:
Movie Queue
## Team Members:
1. Anna Malawista
2. John Baker
3. Jose Gutierrez


# Automated Test Cases:
Automated test cases (unit tests) are located in "./UnitTesting"
1. Run "cd ./UnitTesting"
2. Run "Python3 ./test.py"

## test_filters
Unit test for filtering movie list by category.  
Should pass/test the following: *TESTS CURRENTLY FAIL*

1. Inputing a genre should return all movies with the input genre
2. Inputing an actor should return all movies with the input actor
3. Inputing a genre and actor should return only movies with the input genre and actor
4. If a genre or actor is not present, user should be notified and list proceeds without input

## test_list_create
Unit test to confirm creation of user saved list.  
Should pass/test the following: *TESTS CURRENTLY FAIL*

1. List is created from creation input
2. New file exists
3. File is not empty

## test_user_list
Unit test for confirming user name exists and returns associated list.  
Should pass/test the following: *TESTS CURRENTLY FAIL*

1. Search lists to confirm username exists
2. Return list for given user name
3. Notify user that list does not exist if username is not found


# User Acceptance Testing:

## Test Case 1:
### Use case name
Navigating
### Description
Navigating to new and existing movie lists
### Pre-conditions
Web page loads
### Test steps
1. Load home page
2. Click "Create New List" Page Button
3. Load "Create New List" Page
4. Click "Home" Page Button
5. Return to Home Page
6. Click "View Existing Lists" Page Button
7. Load "View Existing Lists" Page
### Expected result
User should be able navigate to all three pages (Home, Create, View) with each page loading
### Actual result
N/A
### Status (Pass/Fail)
N/A
### Notes
Additional functionality for 'Create' and 'View' pages to be handled in additional test cases
### Post-conditions
User has navigated all three pages


## Test Case 2:
### Use case name
Create New List
### Description
User creates new movie preference settings and list
### Pre-conditions
User has movie preferences
User has navigated to "Create New List" Page
### Test steps
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
### Expected result
Named list of movie preferences is saved to the database
### Actual result
N/A
### Status (Pass/Fail)
N/A
### Notes
N/A
### Post-conditions
List of user's movie choices


## Test Case 3:
### Use case name
View Movie Lists
### Description
User can view and browse created movie lists
### Pre-conditions
Movie lists have been created
User has navigated to "View Existing Lists" Page
### Test steps
1. User can browse list of created movie lists
2. Lists can be sorted alphabetically and by date
3. User can search for a specific list name
4. User can open/view a list of movies

### Expected result
User has navigated and opened an existing list
### Actual result
N/A
### Status (Pass/Fail)
N/A
### Notes
N/A
### Post-conditions
View of existing movie list
