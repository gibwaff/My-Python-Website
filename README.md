# My-Python-Website
# My certificate work

---

This website is my graduation thesis from the itProger course. It was developed by me for 7 days and was highly appreciated by the examiner. The task for the thesis was the same for everyone and was set by the course supervisor.

---

The main task of the site is to convert long user links into short, user-defined ones.

**Example:**

**Input:** `"https://github.com/gibwaff/My-Python-Website"` (ref)  | 
           `"My-Website"` (name)

**Output:** `"My-Website"` (ref)

---

The site is developed on the Django framework using css styles and the sqlite3 database. There is registration and authorization on the website with the possibility of changing the username and email. All the links created by the user are stored in the database and displayed on the corresponding page for the user.

---

**To launch the site:**

1.  Navigate to the `"url_shortener/"` directory.
2.  Run the Django development server using the command: `python manage.py runserver`
3.  The server will start on your local host.
4.  Visit the website at `"http://127.0.0.1:8000/"` to evaluate its functionality.
