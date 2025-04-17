# uses MySQL install defaults for (local) Host, User Name, Password, and Port
# will need to change if your local MySQL setup is different

class conf:
    db_host = "localhost"
    db_name = "onlinerestaurantordersys_db"
    db_port = 3306
    db_user = "root"  # Replace with your MySQL (localhost) user, if different
    db_password = "adminMOGo1!"  # Replace with your MySQL (localhost) password
    app_host = "localhost"  # Replace with your MySQL local host name, if different
    app_port = 8000