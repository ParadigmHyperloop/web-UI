# web-UI
Paradigm Pod control point UI

This serves as the primary point of interaction with the Paradigm Hyperloop Pod for Competition 3 at SpaceX and allows us to send commands to and receive data from the pod.

Overall Control Point Deliverables:
  - Realtime updates to badges and sensor readouts (WebSocket Stream)
  - Ability to enter flight profile information (distance to travel, max speed, length of track, checkboxes to enable or
    disable features, etc)
  - An event viewer box to stream updates with timestamps to
  - A way to drive the vehicle in manual mode:
    - Joystick?
    - Screen Slider?
    - Preconfigured actions?
    - Mouse Wheel?

  - There should also be a new modal created called Change State with a dropdown/list of all the states to change to and a
    button to execute the state change. This will allow the pod to be taken in and out of manual mode
  .
  .
  .
