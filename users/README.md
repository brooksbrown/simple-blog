flask-users-blueprint
=====================

A Flask Blueprint for user functionality.  
  
  

At 1.0 this Blueprint will contain  
- User and Role models
- A UserWrapper for Flask-Login
- Login, logout, register, and other account forms  
- A more complete README



Requirements
------------------
    from flask.ext.login import LoginManager	
    login_manager = LoginManager()
    login_manager.setup_app(app)
    
    @login_manager.user_loader
    def load_user(userid):
	user = User.query.get(userid)
	if user:
		return FLUserWrapper(user)
	else:
		return None
    pass


