# login-register-a

uses django authentication
-----------------------
Fieds in register api:
1.Firstname
2.Lastname
3.Email
4.Password

Fields in login:
1.Username
2.Password



Change Password:
1.Old password
2.New password

--------------------
How it works
--------------------
Register a user:
---------------------
  http://127.0.0.1:8000/api/users/
  ------------------------------
Create a token:
---------------------
  http://127.0.0.1:8000/gettoken/
  --------------------------------
Login using the following url:
-----------------------
  http://127.0.0.1:8000/user-login/
  ----------------------------------
For logout:
---------------------
  http://127.0.0.1:8000/logout/
  -------------------------
To change a password:
----------------------------
  When you login we'll get a uuid and a token  
  -----------------------------------------------
  http://127.0.0.1:8000/change_password/<int:pk>/
  ---------------------------
  note:in the given url replace <int:pk> with your uuid
  ----------------------------------
  use the token for the authorization
  --------------------------------------



