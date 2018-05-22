# Blogger-App-Django-Bootstrap
Note: Haven't done error handling!
<h3> Install the following dependencies for this to work </h3>
<b>Note: Make sure you have python 3 and not 2!!</b>
<ul> 
	<li>pip install django</li>
	<li>pip install channels</li>
	<li>pip install channels_redis</li>
	<li>pip install pillow</li>
<ul>
<b>Before running , make sure you run the redis server first </b>
To run the chat,first run : sudo  docker run -p 6379:6379 -d redis:2.8

<b>After this to run, type python3 manage.py runserver </b>
Note: This is still in debug mode!


<h2>Features</h2>
<ul>
	<li><h4>View All Blogs, View Specific Blogs based on search or category tags. (Note: you can search the title,author or tags in the search bar)</h4></li>
	<li><h4>Add Blogs, Edit Blogs and Each Blog has an Image Field as well</h4></li>
	<li><h4>Each Blog has Comments and Likes </h4></li>
	<li><h4>Live Notifications for Comments and Likes using Channels</h4></li>
	<li><h4>Profile Page to display profile pic, description and social media links and that user's blogs</h4></li>
	<li><h4>Each Blog has a Question & Answer Section, where the author can answer questions and others who view that blog can ask questions</h4></li>
	<li><h4>Chat Rooms using channels, where the default chatroom is room1 and the user can create a new room as per wish </h4></li>
	<li><h4>Pagination of Blogs in the home page, only 5 blogs are shown and the rest of the blogs (if more than 5) are shown in new page dynamically </h4></li>
	<li><h4>Authentication using Login and Logout</h4></li>
	<li><h4>Sign Up for new users</h4></li>
</ul>
