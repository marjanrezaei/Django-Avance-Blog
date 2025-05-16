{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src='https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg'>
{% endblock %}