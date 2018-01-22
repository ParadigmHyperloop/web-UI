#!/usr/bin/env python
import os
from datetime import datetime
from flask import Flask, g, jsonify, current_app, request, \
                  send_from_directory, render_template, redirect, abort


DEFAULT_TITLE = "Control Interface"


app = Flask(__name__)


NAV_BAR = [
  {
    'id': 'index',
    'href': 'index.html',
    'title': 'Vehicle Dashboard',
    'icon': 'pe-7s-graph'
  },
  {
    'id': 'pid',
    'href': 'pid.html',
    'title': 'Air Supply',
    'icon': 'pe-7s-share'
  },
  {
    'id': 'profile',
    'href': 'profile.html',
    'title': 'Flight Profile',
    'icon': 'pe-7s-user'
  },
  {
    'id': 'overrides',
    'href': 'overrides.html',
    'title': 'Sensor Overrides',
    'icon': 'pe-7s-note2'
  },
  {
    'id': 'manual',
    'href': 'manual.html',
    'title': 'Manual Control',
    'icon': 'pe-7s-news-paper'
  },
  {
    'id': 'feeds',
    'href': 'feeds.html',
    'title': 'Live Streams',
    'icon': 'pe-7s-video'
  },
  {
    'id': 'health',
    'href': 'health.html',
    'title': 'Vehicle Health',
    'icon': 'pe-7s-map-marker'
  },
  {
    'id': 'notifications',
    'href': 'notifications.html',
    'title': 'Notifications',
    'icon': 'pe-7s-bell'
  }
]


NAV_IDS = [x['id'] for x in NAV_BAR]


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow(),
            'navigation_bar': NAV_BAR}


@app.route("/ui/", defaults={'path': 'index.html'})
@app.route("/ui/<path:path>")
def ui(path):
    page = path.split('.')[0]
    if page in NAV_IDS:
        title = NAV_BAR[NAV_IDS.index(page)]['title']
    else:
        title = DEFAULT_TITLE
    return render_template(path,
                           active_page=page,
                           title=title)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404


@app.route("/")
def index():
    return redirect('/ui/')


if __name__ == '__main__':
    app.run()
