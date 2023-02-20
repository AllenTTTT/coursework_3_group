from machine import Pin as p
import utime

led_g = p(13, p.OUT) 
led_a = p(14, p.OUT)
led_r = p(15, p.OUT)

pushbutton = p(16, p.IN, p.PULL_DOWN)
#Push button

led_g.value(0)
led_a.value(0)
led_r.value(0)

def toggle_all_LEDs():
    led_g.toggle()
    led_a.toggle()
    led_r.toggle()
    
def turn_off_all_LEDs():
    led_g.value(0)
    led_a.value(0)
    led_r.value(0)
    
count = 0;
    
while True:
    if pushbutton.value():
        toggle_all_LEDs()
        utime.sleep(1)
        toggle_all_LEDs()
        utime.sleep(1)
        toggle_all_LEDs()
        utime.sleep(1)
        while count <= 100:
            count = count + 1
            led_g.toggle()
            utime.sleep(0.5)
        
    else:
        turn_off_all_LEDs()
        
    
