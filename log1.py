{% extends "base.html" %}

{% block content %}

    {% if form.errors %}
        <p class="error"> Not valid username or password</p>
    {% endif %}

    <form action="/accounts/auth/" method="post">{csrf_token %} #csrf_token security mechanism
        <label for="username">User name:</label>
        <input type="text" name+"username" value="" id="username">
        <label for="password">Password:</label>
        <input type="password" name="password" value="" id="password">

        <input type="submit" value="login" />

    </form>

{% endblock %}  # this base.html is used for login validation 

