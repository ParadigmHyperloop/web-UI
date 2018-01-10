#!/usr/bin/env python
import os
from datetime import datetime
from flask import Flask, g, jsonify, current_app, request, \
                  send_from_directory, render_template, redirect, abort


app = Flask(__name__)


NAV_BAR = {
  'index': {
    'href': 'index.html',
    'title': 'Vehicle Dashboard',
    'icon': 'pe-7s-graph'
  },
  'profile': {
    'href': 'profile.html',
    'title': 'Flight Profile',
    'icon': 'pe-7s-user'
  },
  'overrides': {
    'href': 'overrides.html',
    'title': 'Sensor Overrides',
    'icon': 'pe-7s-note2'
  },
  'manual': {
    'href': 'manual.html',
    'title': 'Manual Control',
    'icon': 'pe-7s-news-paper'
  },
  'feeds': {
    'href': 'feeds.html',
    'title': 'Live Streams',
    'icon': 'pe-7s-science'
  },
  'health': {
    'href': 'health.html',
    'title': 'Vehicle Health',
    'icon': 'pe-7s-map-marker'
  },
  'notifications': {
    'href': 'notifications.html',
    'title': 'Notifications',
    'icon': 'pe-7s-bell'
  },
}


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow(),
            'navigation_bar': NAV_BAR}


@app.route("/ui/", defaults={'path': 'index'})
@app.route("/ui/<path:path>")
def ui(path):
    page = path.split('.')[0]
    return render_template(path,
                           active_page=page,
                           title=NAV_BAR[page]['title'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404


@app.route("/")
def index():
    return redirect('/ui/')


if __name__ == '__main__':
    app.run()
