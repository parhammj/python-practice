# setup.py
import turtle, time

# ---------- screen ----------
screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("grey")
screen.tracer(0)

drawer = turtle.Turtle(); drawer.hideturtle(); drawer.penup()
hud = turtle.Turtle(); hud.hideturtle(); hud.penup(); hud.goto(-360,150)
status = turtle.Turtle(); status.hideturtle(); status.penup(); status.goto(0,150)

# ---------- world ----------
LEFT_X = -350
RIGHT_X = 350
GROUND_Y = -120
SAFE_ZONE_X = -230
VIEWER_X = 0
WORK_X = 230
STEP = 4
DT = 0.05

# ---------- internal robot state ----------
robot_x = SAFE_ZONE_X
direction = 1
battery = 100
carrying_box = True


# ---------- drawing helpers ----------
def rect(x0, y0, w, h, color):
    drawer.penup(); drawer.goto(x0,y0); drawer.pendown()
    drawer.pencolor("black"); drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(w); drawer.left(90)
        drawer.forward(h); drawer.left(90)
    drawer.end_fill(); drawer.penup()

def environment():
    rect(SAFE_ZONE_X-60, GROUND_Y, 120,60, "cyan")
    drawer.goto(SAFE_ZONE_X, GROUND_Y+70); drawer.write("Safe zone",align="center")

    rect(VIEWER_X-60, GROUND_Y, 120,60, "yellow")
    drawer.goto(VIEWER_X, GROUND_Y+70); drawer.write("People area",align="center")

    rect(WORK_X-80, GROUND_Y+35, 160,20, "lightgray")
    drawer.goto(WORK_X, GROUND_Y+70); drawer.write("Work table",align="center")

    drawer.penup(); drawer.goto(LEFT_X,GROUND_Y)
    drawer.pendown(); drawer.forward(RIGHT_X-LEFT_X); drawer.penup()

def draw_robot():
    # torso
    rect(robot_x-15, GROUND_Y+30, 30,50, "#1fb36c")
    # head
    rect(robot_x-12, GROUND_Y+80, 24,20, "white")
    # arms
    rect(robot_x-30, GROUND_Y+60, 15,4, "gray")
    rect(robot_x+15, GROUND_Y+60, 15,4, "gray")
    # legs
    rect(robot_x-7, GROUND_Y+10, 5,20, "gray")
    rect(robot_x+2, GROUND_Y+10, 5,20, "gray")
    # box
    if carrying_box:
        rect(robot_x+22, GROUND_Y+60, 20,16, "orange")

def draw_robot_collapse():
    # lying on the ground near people
    rect(robot_x - 30, GROUND_Y + 10, 60, 18, "#1fb36c")   # torso sideways (Digit green)
    rect(robot_x + 30, GROUND_Y + 10, 18, 18, "white")     # head on side
    # small legs/arms hints (optional)
    rect(robot_x - 35, GROUND_Y + 10, 10, 4, "gray")
    rect(robot_x + 15, GROUND_Y + 10, 10, 4, "gray")

# ---------- student-facing API ----------
def prepare_frame():
    drawer.clear()
    environment()
    update_battery_text()
    
def update_battery_text():
    hud.clear()
    hud.write("Battery: " + str(int(battery)) + "%", font=("Arial",16,"normal"))

def finish_frame():
    screen.update()
    time.sleep(DT)

def set_status(msg):
    status.clear()
    status.write(msg, align="center", font=("Arial", 12, "normal"))

def move_back_and_forth():
    global robot_x, direction
    robot_x += direction * STEP
    if robot_x >= WORK_X:
        direction = -1
    elif robot_x <= SAFE_ZONE_X:
        direction = 1

def use_battery(amount):
    global battery
    battery -= amount
    if battery < 0: battery = 0

def collapse():
    set_status("Robot collapses near people (unsafe).")
    draw_robot_collapse()
    finish_frame()
