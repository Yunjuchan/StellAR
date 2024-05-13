import gpiod
import time
from threading import Thread

chip = gpiod.Chip('gpiochip4')

state = 0
out_count = 0
last_num = 0
last_distance = 0
value = 0
wave_num = 0
DISTANCES = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
PINS = [14, 15, 18, 23, 24, 25, 8, 7, 2, 3, 4, 17, 27, 22, 10, 9]

def cal_distance(now_pin):
    break_count = 0
    value = 0

    trigger_line = chip.get_line(now_pin)
    trigger_line.request(consumer="TRIG", type=gpiod.LINE_REQ_DIR_OUT)
    
    trigger_line.set_value(1)
    time.sleep(0.00001)
    trigger_line.set_value(0)
    trigger_line.release()
    
    echo_line = chip.get_line(now_pin)
    echo_line.request(consumer="ECHO", type=gpiod.LINE_REQ_DIR_IN)
    
    while echo_line.get_value() == 0:
        start = time.time()
        break_count += 1
        if break_count > 2000:
            value = 1
            echo_line.release()
            return 10
            
    while echo_line.get_value() != 0:
        stop = time.time()

        
    check_time = stop - start
    distance = check_time * 34300/2
    echo_line.release()

    return distance

def ul_wave(pin):
    break_count = 0
    value0 = 0
    trigger0_line = chip.get_line(pin)
    trigger0_line.request(consumer="TRIG0", type=gpiod.LINE_REQ_DIR_OUT)
        
    trigger0_line.set_value(1)
    time.sleep(0.00001)
    trigger0_line.set_value(0)
    trigger0_line.release()
    
    echo0_line = chip.get_line(pin)
    echo0_line.request(consumer="ECHO0", type=gpiod.LINE_REQ_DIR_IN)
    
    while echo0_line.get_value() == 0:
        start = time.time()
        break_count += 1
        if break_count > 2000:
            value0 = 1
            distance = 10
            
    while echo0_line.get_value() != 0 and value == 0:
        stop = time.time()
        
    
    if value0 == 0:
        check_time = stop - start
        distance = check_time * 34300/2
        echo0_line.release()

    DISTANCES[0] = distance
    time.sleep(0.1)

def ul_wave_0(val):
    while True:

        break_count = 0
        value0 = 0
        trigger0_line = chip.get_line(PINS[0])
        trigger0_line.request(consumer="TRIG0", type=gpiod.LINE_REQ_DIR_OUT)
        
        trigger0_line.set_value(1)
        time.sleep(0.00001)
        trigger0_line.set_value(0)
        trigger0_line.release()
        
        echo0_line = chip.get_line(PINS[0])
        echo0_line.request(consumer="ECHO0", type=gpiod.LINE_REQ_DIR_IN)
        
        while echo0_line.get_value() == 0:
            start = time.time()
            break_count += 1
            if break_count > 2000:
                value0 = 1
                distance = 10
                
        while echo0_line.get_value() != 0 and value == 0:
            stop = time.time()
#        if echo_line.get_value == 1:
#            value =1
#        break_count += 1
#        if break_count > 5000:
#            #print("stop")
#            value = 0
#            break

#    while(break_point):
#        print(echo_line.get_value())
#        if value == 0 and echo_line.get_value() == 0:
#            #print("1")
#            start == time.time()
#            value = 1
#        elif value == 1 and echo_line.get_value() == 0:
#            #print("0")
#            stop = time.time()
#            value = 0
#            break_point = 0

        if value0 == 0:
            check_time = stop - start
            distance = check_time * 34300/2
            echo0_line.release()
    
        DISTANCES[0] = distance
        time.sleep(0.1)

    #if val == 16:
    #    val = 0
    #ul_wave_0(val+1)

def ul_wave_1(val):
    while True:
        #DISTANCES[1] = cal_distance(PINS[1])
        #time.sleep(0.1)
        break_count = 0
        value1 = 0
        trigger1_line = chip.get_line(PINS[1])
        trigger1_line.request(consumer="TRIG1", type=gpiod.LINE_REQ_DIR_OUT)
        
        trigger1_line.set_value(1)
        time.sleep(0.00001)
        trigger1_line.set_value(0)
        trigger1_line.release()
        
        echo1_line = chip.get_line(PINS[1])
        echo1_line.request(consumer="ECHO1", type=gpiod.LINE_REQ_DIR_IN)
        
        while echo1_line.get_value() == 0:
            start = time.time()
            break_count += 1
            if break_count > 2000:
                value1 = 1
                distance = 10
                
        while echo1_line.get_value() != 0 and value1 == 0:
            stop = time.time()

        
        if value == 0:
            check_time = stop - start
            distance = check_time * 34300/2
            echo1_line.release()
    
        DISTANCES[1] = distance
        time.sleep(0.1)

def ul_wave_2(val):
    while True:
        #DISTANCES[2] = cal_distance(PINS[2])
        #time.sleep(0.1)
        break_count = 0
        value2 = 0
        trigger2_line = chip.get_line(PINS[2])
        trigger2_line.request(consumer="TRIG2", type=gpiod.LINE_REQ_DIR_OUT)
        
        trigger2_line.set_value(1)
        time.sleep(0.00001)
        trigger2_line.set_value(0)
        trigger2_line.release()
        
        echo2_line = chip.get_line(PINS[2])
        echo2_line.request(consumer="ECHO2", type=gpiod.LINE_REQ_DIR_IN)
        
        while echo2_line.get_value() == 0:
            start = time.time()
            break_count += 1
            if break_count > 2000:
                value2 = 1
                distance = 10
                
        while echo2_line.get_value() != 0 and value2 == 0:
            stop = time.time()

        
        if value == 0:
            check_time = stop - start
            distance = check_time * 34300/2
            echo2_line.release()
    
        DISTANCES[2] = distance
        time.sleep(0.1)

def ul_wave_3(val):
    while True:
        DISTANCES[3] = cal_distance(PINS[3])
        time.sleep(0.1)

def ul_wave_4(val):
    while True:
        DISTANCES[4] = cal_distance(PINS[4])
        time.sleep(0.1)

def ul_wave_5(val):
    while True:
        DISTANCES[5] = cal_distance(PINS[5])
        time.sleep(0.1)

def ul_wave_6(val):
    while True:
        DISTANCES[6] = cal_distance(PINS[6])
        time.sleep(0.1)

def ul_wave_7(val):
    while True:
        DISTANCES[7] = cal_distance(PINS[7])
        time.sleep(0.1)

def ul_wave_8(val):
    while True:
        DISTANCES[8] = cal_distance(PINS[8])
        time.sleep(0.1)

def ul_wave_9(val):
    while True:
        DISTANCES[9] = cal_distance(PINS[9])
        time.sleep(0.1)
        

def ul_wave_10(val):
    while True:
        DISTANCES[10] = cal_distance(PINS[10])
        time.sleep(0.1)

def ul_wave_11(val):
    while True:
        DISTANCES[11] = cal_distance(PINS[11])
        time.sleep(0.1)

def ul_wave_12(val):
    while True:
        DISTANCES[12] = cal_distance(PINS[12])
        time.sleep(0.1)

def ul_wave_13(val):
    while True:
        DISTANCES[13] = cal_distance(PINS[13])
        time.sleep(0.1)

def ul_wave_14(val):
    while True:
        DISTANCES[14] = cal_distance(PINS[14]) 
        time.sleep(0.1)

def ul_wave_15(val):
    while True:
        DISTANCES[15] = cal_distance(PINS[15])
        time.sleep(0.1)

t0 = Thread(target = ul_wave_0, args=(1,))
t1 = Thread(target = ul_wave_1, args=(1,))
t2 = Thread(target = ul_wave_2, args=(1,))
t3 = Thread(target = ul_wave_3, args=(1,))
t4 = Thread(target = ul_wave_4, args=(1,))
t5 = Thread(target = ul_wave_5, args=(1,))
t6 = Thread(target = ul_wave_6, args=(1,))
t7 = Thread(target = ul_wave_7, args=(1,))
t8 = Thread(target = ul_wave_8, args=(1,))
t9 = Thread(target = ul_wave_9, args=(1,))
t10 = Thread(target = ul_wave_10, args=(1,))
t11 = Thread(target = ul_wave_11, args=(1,))
t12 = Thread(target = ul_wave_12, args=(1,))
t13 = Thread(target = ul_wave_13, args=(1,))
t14 = Thread(target = ul_wave_14, args=(1,))
t15 = Thread(target = ul_wave_15, args=(1,))

t0.start()
t1.start()
t2.start()
#t3.start()
#t4.start()
#t5.start()
#t6.start()
#t7.start()
#t8.start()
#t9.start()
#t10.start()
#t11.start()
#t12.start()
#t13.start()
#t14.start()
#t15.start()

while (1):
    visited_count = 0
    last_visited = 0
    visited_nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    visited_distances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("0 : %.1f" %DISTANCES[0])
    print("1 : %.1f" %DISTANCES[1])
    print("2 : %.1f" %DISTANCES[2])
    #print("3 : %.1f" %DISTANCES[3])
    #print("6 : %.1f" %DISTANCES[6])
    #print("7 : %.1f" %DISTANCES[7])


    for i in range(6):
        if 30<= DISTANCES[i] <=110:
            visited_nums[visited_count] = i
            visited_distances[visited_count] = DISTANCES[i]
            visited_count += 1
            last_visited = i

    #print(visited_count)
    if visited_count > 0:
        ul_num = 0
        ul_distance = 0
        for i in range(visited_count):
            ul_num += visited_nums[i]
            ul_distance += visited_distances[i]
        ul_num = ul_num/visited_count
        ul_distance = ul_distance/visited_count
        out_count = 0
        
        if state == 0:
            state = 1
            last_num = ul_num
            last_distance = ul_distance
            print("Sensor %.1f: Down - Height: %.2f cm" % (ul_num, ul_distance))
            #print("Down")
        else:
            last_num = ul_num
            last_distance = ul_distance
            #last_distance = now_distances[last_visited]
            print("Sensor %.1f: Move - Height: %.2f cm" % (ul_num, ul_distance))
            #print("Move")


    else:
        out_count += 1
        if out_count == 3:
            state = 0
            print("Sensor %.1f: Up - Height: %.2f cm" % (last_num, last_distance))

    time.sleep(0.1)
