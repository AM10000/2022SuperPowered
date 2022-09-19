from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from ev3dev2.wheel import EV3EducationSetTire
from commonFunctions import *
from ev3dev2.sound import *
class Kronos:
    def __init__(self):
        self.robot_width = 116
        self.tank = MoveTank(OUTPUT_A, OUTPUT_D)
        self.mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, self.robot_width)
        self.mmL = MediumMotor(OUTPUT_B)
        self.mmR = MediumMotor(OUTPUT_C)


    def lfCColorRangeR(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_2)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange, floor = floor, ceiling = ceiling, port = INPUT_4)

    def lfRColorRangeL(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_4)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange, floor = floor, ceiling = ceiling, port = INPUT_1)
    
    def lfLColorRangeR(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_1)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange, floor = floor, ceiling = ceiling, port = INPUT_4)
    
    def lfCColorRangeL(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_2)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange, floor = floor, ceiling = ceiling, port = INPUT_1)
    
    def lfRColorRangeC(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_4)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange, floor = floor, ceiling = ceiling, port = INPUT_2)
    
    def lfRColorRangeCL(self, speed, offset, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_4)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 100, 0, follow_for=isNotInColorRange2, floor = floor, ceiling = ceiling, port1 = INPUT_2, port2 = INPUT_1)
    
    def lfLColorRangeCR(self, speed, left_side, floor, ceiling, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_1)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, left_side, 80, 100, 0, follow_for=isNotInColorRange2, floor = floor, ceiling = ceiling, port1 = INPUT_4, port2 = INPUT_2)
    
    def lfRTime(self, speed, offset, seconds, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_4)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, offset, 80, 10000, 0, follow_for=follow_for_ms, ms = seconds * 1000)

    def lfLTime(self, speed, left_side, seconds, magnitude=1.9):
        self.tank.cs = ColorSensor(INPUT_1)
        self.tank.follow_line(magnitude, 0, 1.2, SpeedPercent(speed), 49.5, left_side, 80, 100, 0, follow_for=follow_for_ms, ms = seconds * 1000)
    
    def LmediumMotorDegrees(self, speed, degrees, brake=True, block=True):
        self.mmL.on_for_degrees(SpeedPercent(speed), degrees, brake, block=False)
        self._blockMedium(block)
    
    def RmediumMotorDegrees(self, speed, degrees, brake=True, block=True):
        self.mmR.on_for_degrees(SpeedPercent(speed), degrees, brake, False)
        self._blockMedium(block)

    def moveDistance(self, speedL, speedR, distanceCM, brake=True, block=True):
        deg = distanceCM*20.45
        self.mdiff.on_for_degrees(SpeedPercent(speedL),SpeedPercent(speedR), deg, brake, False)        
        self._blockLarge(block)
    
    # def moveDistance(self, speed, distanceCM, radiusCM, brake=True, block=True):
    #     self.mdiff.on_arc_right(SpeedPercent(speed), radiusCM * 10, distanceCM * 10, brake, False)
    #     self._blockLarge(block)
        

    # def moveDistance(self, aSpeed, dSpeed, distanceCM, brake=True, block=True):
    #     if aSpeed == dSpeed:
    #         self.mdiff.on_for_distance(SpeedPercent(aSpeed), distanceCM * 10, brake, block)
    #     if abs(aSpeed) > abs(dSpeed):
    #         self.mdiff.on_arc_right(SpeedPercent((aSpeed + dSpeed)/2), \
    #             calculateRadius(aSpeed, dSpeed, self.robot_width), distanceCM * 10, brake, block)
    #     if abs(dSpeed) > abs(aSpeed):
    #         self.mdiff.on_arc_left(SpeedPercent((aSpeed + dSpeed)/2), \
    #             calculateRadius(aSpeed, dSpeed, self.robot_width), distanceCM * 10, brake, block)
    #def arcUntilColorlteq(self, aSpeed, dSpeed, RLI, port):
        #self.tank.cs=ColorSensor(address=port)
        #if abs(aSpeed) > abs(dSpeed):
            #self.mdiff.on_arc_right(SpeedPercent((aSpeed+dSpeed)/2), calculateRadius(aSpeed,dSpeed, self.robot_width),)
            #while True:
                #if self.tank.reflected_light_intensity<=RLI:
                   # self.tank.stop()
                   # break
 
    def moveUntilColorlteq(self, left_power, right_power, port, RLI):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity<= RLI:
                self.tank.stop()
                break

    def moveUntilColorlt(self, left_power, right_power, port, RLI, brake=True):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity<RLI:
                self.tank.stop(brake=brake)
                break

    def moveUntilColorgteq(self, left_power, right_power, port, RLI):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity>=RLI:
                self.tank.stop()
                break

    def moveUntilColorgt(self, left_power, right_power, port, RLI):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity>RLI:
                self.tank.stop()
                break

    def moveUntilColorRange(self, left_power, right_power, port, floor, ceiling):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity>floor and self.tank.cs.reflected_light_intensity<ceiling:
                self.tank.stop()
                break

    def moveUntilColoreq(self, left_power, right_power, port, RLI):
        self.tank.cs=ColorSensor(address=port)
        self.tank.on(SpeedPercent(left_power), SpeedPercent(right_power))
        while True:
            if self.tank.cs.reflected_light_intensity==RLI:
                self.tank.stop()
                break

    def spinRobot(self, left_power, right_power, degrees, block=True):
        d = (((degrees/10)+degrees)*10.3)/5.6
        self.mdiff.on_for_degrees(left_speed=SpeedPercent(left_power), right_speed=SpeedPercent(right_power), degrees=d, block=False)
        self._blockLarge(block)
        self.mdiff.stop()

    def squareToBlack(self, power, sensor1, sensor2):
        s = Sound()
        cs1=ColorSensor(address= sensor1)
        cs2 = ColorSensor(address= sensor2)
        self.tank.on(SpeedPercent(power), SpeedPercent(power))
        while True:
            if cs1.reflected_light_intensity < 12:
                self.tank.off()
                s.beep()
                self.moveUntilColorlt(0, power, sensor2, 12)
                break
            elif cs2.reflected_light_intensity < 12:
                self.tank.off()
                s.beep()
                self.moveUntilColorlt(power, 0, sensor1, 12)
                break

    def squareToRange(self, power, floor, ceiling, sensor1, sensor2):
        s = Sound()
        cs1=ColorSensor(address=sensor1)
        cs2 = ColorSensor(address=sensor2)
        self.tank.on(SpeedPercent(power), SpeedPercent(power))
        while True:
            if cs1.reflected_light_intensity < ceiling and cs1.reflected_light_intensity > floor:
                self.tank.off()
                s.beep()
                self.moveUntilColorRange(0, power, sensor2, floor, ceiling)
                break
            elif cs2.reflected_light_intensity < ceiling and cs2.reflected_light_intensity > floor:
                self.tank.off()
                s.beep()
                self.moveUntilColorRange(power, 0, sensor1, floor, ceiling)
                break

    def error(self, angleFloor, angleCeiling, mdiffVarName):
        current_degrees = math.degrees(mdiffVarName.theta)
        if current_degrees < 0:
            current_degrees += 360
        if current_degrees < angleCeiling and current_degrees > angleFloor:
            return True
        else:
            return False

    def _blockLarge(self, block):
        if block:
            while self.mdiff.left_motor.is_running or self.mdiff.right_motor.is_running:
                time.sleep(0.005)

    def _blockMedium(self, block):
        if block:
            while self.mmL.is_running or self.mmR.is_running:
                time.sleep(0.005)