# Test Cases — Hotel Booking QA Project

## TC-LOGIN-01: Successful admin login
- **Preconditions:** User is on the Admin login page.
- **Test Data:** Username: `admin`, Password: `password`
- **Steps:**
  1. Given the user is on the Admin login page.
  2. When the user enters valid username and password.
  3. And clicks the "Login" button.
- **Expected Result:** User is redirected to the Admin Dashboard, and the "Rooms" page is visible.
- **Actual Result:** User successfully logged in and was redirected to the Admin Dashboard.
- **Status:** Pass

---

## TC-LOGIN-02: Login failure with invalid password
- **Preconditions:** User is on the Admin login page.
- **Test Data:** Username: `admin`, Password: `wrongpassword`
- **Steps:**
  1. Given the user is on the Admin login page.
  2. When the user enters a valid username but an invalid password.
  3. And clicks the "Login" button.
- **Expected Result:** An error message appears stating "Invalid credentials", and the user is not logged in.
- **Actual Result:** An error message appeared stating "Invalid credentials", and login was rejected.
- **Status:** Pass

---

## TC-BOOK-01: Successful room booking with valid dates
- **Preconditions:** User is on the public front page.
- **Test Data:** Check-in date: 3 days from today, Check-out date: 5 days from today.
- **Steps:**
  1. Given the user is on the front page.
  2. When the user selects valid future check-in and check-out dates.
  3. And clicks "Check Availability".
  4. And selects a room and fills in valid guest details (Name, Email, Phone).
  5. And clicks "Reserve Now".
- **Expected Result:** A confirmation screen appears showing the correct booking details and total price.
- **Actual Result:** The page got stuck on an infinite loading spinner and never displayed the form.
- **Status:** Fail (See BUG-001)

---

## TC-CONTACT-01: Submit contact form with invalid email
- **Preconditions:** User is on the public front page.
- **Test Data:** Name: `Test User`, Email: `invalid-email` (missing @), Message: `Hello`
- **Steps:**
  1. Given the user navigates to the "Contact" section.
  2. When the user fills in the Name and Message fields.
  3. And enters an email address without an "@" symbol.
  4. And clicks "Submit".
- **Expected Result:** The form should not submit, and an error message should say "Please enter a valid email address."
- **Actual Result:** The form correctly rejected the submission and displayed 3 validation error messages (Message too short, invalid email, invalid phone).
- **Status:** Pass

---

## TC-CONTACT-02: Submit contact form with valid data
- **Preconditions:** User is on the public front page.
- **Test Data:** Valid Name, valid Email (`test@test.com`), valid 11-digit Phone, valid Subject, and a Message longer than 20 characters.
- **Steps:**
  1. Given the user navigates to the "Contact" section.
  2. When the user fills in all fields with valid data.
  3. And clicks "Submit".
- **Expected Result:** A success message appears stating "Thanks for getting in touch [Name]!" AND the message appears in the Admin dashboard.
- **Actual Result:** Success message displayed correctly, BUT the message did not appear in the Admin dashboard.
- **Status:** Fail (See BUG-002)