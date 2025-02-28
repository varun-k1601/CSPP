door_open=input()
window_open=input()
motion_detected=input()
alarm_deactivated=input()
def example(door_open,window_open,motion_detected,alarm_detected):
    return (door_open=="True" and alarm_deactivated=="False") or (window_open=="True" and alarm_deactivated=="False") or(motion_detected=="True" and alarm_deactivated=="False")
output=example(door_open,window_open,motion_detected,alarm_deactivated)
print(output)