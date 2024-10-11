CORE
========================
### Authentication
1. Signup a new user
    * Successful signup with redirect (should be logged in?)
    * Unsuccessful signup with errors on screen
2. Login a user
    * Successful login with redirect to home/desired page
    * Unsuccessful login with errors on screen
3. Logout a user
----------------------------------------------
#### User Model
- [x] User email should be unique
  
#### User Signup
- [x] Automated login after signup
- [x] Errors displayed on form with a red-ish color
- [x] Integration tests to avoid painful regressions
  
#### Login
- [ ] ~Show login as modal dialog when requested inside another page~
- [ ] Alternatively cached the initial page before login
- [x] Errors displayed on form with a red-ish color
- [x] Template refactoring
- [x] Move label declaration to forms.py
- [x] Labels are using the default text color
  
#### Refactor
- [x] Change view to match-case instead of multiple ifs