import setup

# ===============================
# STUDENT CONTROLS
# ===============================
BATTERY_DRAIN = 0.2                 # Battery lost each step

# ===============================
# MAIN LOOP — UNSAFE BEHAVIOR
# ===============================
robot.set_status("Robot working near people (unsafe).")

while robot.battery > 0:
    robot.prepare_frame()                   # clear + redraw environment

    robot.move_back_and_forth()             # robot walks left/right
    robot.use_battery(BATTERY_DRAIN)        # drain battery each step

    robot.draw_robot()                            # draw the robot each frame
    robot.finish_frame()                    # update screen + wait

robot.prepare_frame()                   # clear + redraw environment
robot.collapse()