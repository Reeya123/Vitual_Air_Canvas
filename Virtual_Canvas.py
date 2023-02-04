import numpy as np
import cv2
import keyboard
import time
from collections import deque
import sys

# Print the first argument after the name of file
color = sys.argv[1]

color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
                  'white': [[180, 18, 255], [0, 0, 231]],
                  'red': [[180, 255, 255], [159, 50, 70]],
                  'red2': [[9, 255, 255], [0, 50, 70]],
                  'green': [[89, 255, 255], [36, 50, 70]],
                  'blue': [[128, 255, 255], [90, 50, 70]],
                  'yellow': [[35, 255, 255], [25, 50, 70]],
                  'purple': [[158, 255, 255], [129, 50, 70]],
                  'orange': [[24, 255, 255], [10, 50, 70]],
                  'gray': [[180, 18, 230], [0, 0, 40]]
                  }


###CODE FOR DETECTION OF BLUE OBJECTS
# default called trackbar function
def setValues(x):
    print("")


# background captured parameters
isBgCaptured = False
bgSubThreshold = 50
learningRate = 0.005
brush = 3
maxi = 16
mini = 2
ev = 1
# Creating the trackbars needed for adjusting the marker colour
# =============================================================================
# cv2.namedWindow("Color detectors")
# cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
# cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
# cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
# cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
# cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255,setValues)
# cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)
# =============================================================================


# Giving different arrays to handle colour points of different colour
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
wpoints = [deque(maxlen=1024)]
ppoints = [deque(maxlen=1024)]
bkpoints = [deque(maxlen=1024)]
brpoints = [deque(maxlen=1024)]
epoints = [deque(maxlen=1024)]

last_blue_index = set()
last_green_index = set()
last_red_index = set()
last_yellow_index = set()
last_white_index = set()
last_pink_index = set()
last_black_index = set()
last_brown_index = set()
last_eraser_index = set()

# These indexes will be used to mark the points in particular arrays of specific colour
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
white_index = 0
pink_index = 0
black_index = 0
brown_index = 0
eraser_index = 0

# The kernel to be used for dilation purpose
kernel = np.ones((5, 5), np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255), (84,255,159), (138,43,226), (139,0,139 ),
          (0, 0, 0)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((720, 1280, 3)) + 255
cv2.namedWindow('WhiteBoard', cv2.WINDOW_NORMAL)


# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cv2.namedWindow('Canvas', cv2.WINDOW_NORMAL)


def removeBG(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


def drawPoints(points, colors, this_frame):
    for i in range(len(points)):

        for j in range(len(points[i])):

            for k in range(1, len(points[i][j])):

                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue

                cv2.line(this_frame, points[i][j][k - 1], points[i][j][k], (colors[i] * ev), brush)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], (colors[i] * ev), brush)


def drawBoardPoints(points, this_frame):
    for i in range(len(points)):

        for j in range(len(points[i])):

            for k in range(1, len(points[i][j])):

                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue

                cv2.line(this_frame, points[i][j][k - 1], points[i][j][k], ((255, 255, 255) * ev), brush)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], ((255, 255, 255) * ev), brush)


iteration = 0

# Keep looping
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    if ret == False:
        print("failed to utilize default camera 0")
        exit(1)
    # Flipping the frame to see same side of yours

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Upper_hsv = np.array([u_hue,u_saturation,u_value])
    # Lower_hsv = np.array([l_hue,l_saturation,l_value])

    upper = color_dict_HSV[color][0]
    lower = color_dict_HSV[color][1]

    Upper_hsv = np.array(upper)
    Lower_hsv = np.array(lower)

    # Adding the colour buttons to the live frame for colour access
    frame = cv2.rectangle(frame, (40, 2), (140, 65), colors[8], -1)
    frame = cv2.rectangle(frame, (275, 2), (370, 65), colors[0], -1)
    frame = cv2.rectangle(frame, (390, 2), (485, 65), colors[1], -1)
    frame = cv2.rectangle(frame, (505, 2), (600, 65), colors[2], -1)
    frame = cv2.rectangle(frame, (620, 2), (715, 65), colors[3], -1)
    frame = cv2.rectangle(frame, (735, 2), (830, 65), colors[4], -1)
    #frame = cv2.rectangle(frame, (735, 1), (830, 65), colors[5], -1)
    #frame = cv2.rectangle(frame, (850, 1), (945, 65), colors[6], -1)
    #frame = cv2.rectangle(frame, (965, 1), (1060, 65), colors[7], -1)
    #frame = cv2.rectangle(frame, (1080, 1), (1175, 65), colors[8], -1)
    # frame = cv2.rectangle(frame, (505,1), (600,65), colors[4], -1)
    cv2.putText(frame, "CLEAR ALL", (49, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (305, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (413, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (538, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (634, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "PINK", (763,38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    #cv2.putText(frame, "PINK", (763, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    #cv2.putText(frame, "BLACK", (885, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    #cv2.putText(frame, "BROWN", (985, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    #cv2.putText(frame, "ERASER", (1085, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    if colorIndex == 0:
        frame = cv2.rectangle(frame, (270, 1), (375, 70), colors[0], 8)
        cv2.putText(frame, 'Color Selected: BLUE', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colors[0], 3)
        c = 'BLUE'
        paintWindow[67:, :, :] = 255
    elif colorIndex == 1:
        frame = cv2.rectangle(frame, (385, 1), (490, 70), colors[1], 8)
        cv2.putText(frame, 'Color Selected: GREEN ', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colors[1], 3)
        c = 'GREEN'
        paintWindow[67:, :, :] = 255
    elif colorIndex == 2:
        frame = cv2.rectangle(frame, (500, 1), (605, 70), colors[2], 8)
        cv2.putText(frame, 'Color Selected: RED', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colors[2], 3)
        c = 'RED'
        paintWindow[67:, :, :] = 255
    elif colorIndex == 3:
        frame = cv2.rectangle(frame, (615, 1), (720, 70), colors[3], 8)
        cv2.putText(frame, 'Color Selected: YELLOW ', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colors[3], 3)
        c = 'YELLOW'
        paintWindow[67:, :, :] = 255
    elif colorIndex == 4:
        frame = cv2.rectangle(frame, (730, 1), (835, 70), colors[4], 8)
        cv2.putText(frame, 'Color Selected: PINK', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colors[4], 3)
        c = 'PINK'
        paintWindow[67:, :, :] = 255
    #elif colorIndex == 5:
        #frame = cv2.rectangle(frame, (730, 1), (835, 70), colors[8], 8)
        #paintWindow[67:, :, :] = 255
    #elif colorIndex == 6:
        #frame = cv2.rectangle(frame, (845, 1), (950, 70), colors[8], 8)
        #paintWindow[67:, :, :] = 255
    #elif colorIndex == 7:
        #frame = cv2.rectangle(frame, (960, 1), (1065, 70), colors[8], 8)
        #paintWindow[67:, :, :] = 255
    #elif colorIndex == 8:
        #frame = cv2.rectangle(frame, (1075, 1), (1180, 70), colors[8], 8)
        #paintWindow[67:, :, :] = 255

        # Identifying the pointer by making its mask
    if isBgCaptured == True:
        foreground = removeBG(hsv).copy()
        Mask = cv2.inRange(foreground, Lower_hsv, Upper_hsv)
    else:
        Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
        Mask = cv2.erode(Mask, kernel, iterations=1)
        Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
        Mask = cv2.dilate(Mask, kernel, iterations=1)

    # Find contours for the pointer after idetifying it
    cnts, _ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # Ifthe contours are formed
    if len(cnts) > 0 and keyboard.is_pressed(" "):
        # sorting the contours to find biggest
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        if M["m00"]!=0:
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
        else:
            center = 0,0
            frame = cv2.rectangle(frame, (40, 1), (140, 70), (0,0,0), 8)
            cv2.putText(frame, 'Object not detected', (200, 410), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 3)

        # Now checking if the user wants to click on any button above the screen
        if center[1] <= 75:
            if 40 <= center[0] <= 140:  # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                wpoints = [deque(maxlen=512)]
                #ppoints = [deque(maxlen=512)]
                #bkpoints = [deque(maxlen=512)]
                #brpoints = [deque(maxlen=512)]
                #epoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                white_index = 0
                #pink_index = 0
                #black_index = 0
                #brown_index = 0
                #eraser_index = 0

                paintWindow[67:, :, :] = 255
                frame = cv2.rectangle(frame, (40, 1), (140, 70), (0,0,0), 8)
                cv2.putText(frame, 'Screen Cleared', (275, 410), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 5)
            elif 275 <= center[0] <= 370:
                colorIndex = 0  # Blue
            elif 390 <= center[0] <= 485:
                colorIndex = 1  # Green
            elif 505 <= center[0] <= 600:
                colorIndex = 2  # Red
            elif 620 <= center[0] <= 715:
                colorIndex = 3  # Yellow
            elif 735 <= center[0] <= 830:
                colorIndex = 4  # white
            #elif 735 <= center[0] <= 830:
                #colorIndex = 5  # pink
            #elif 850 <= center[0] <= 945:
                #colorIndex = 6  # black
            #elif 965 <= center[0] <= 1060:
                #colorIndex = 7  # bROWN
            #elif 1080 <= center[0] <= 1175:
                #colorIndex = 8  # eraser
        else:

            last_blue_index.add(blue_index)
            last_green_index.add(green_index)
            last_red_index.add(red_index)
            last_yellow_index.add(yellow_index)
            last_white_index.add(white_index)
            #last_pink_index.add(pink_index)
            #last_black_index.add(black_index)
            #last_brown_index.add(brown_index)
            #last_eraser_index.add(eraser_index)
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 4:
                wpoints[white_index].appendleft(center)
            #elif colorIndex == 5:
             #   ppoints[pink_index].appendleft(center)
           # elif colorIndex == 6:
            #    bkpoints[black_index].appendleft(center)
            #elif colorIndex == 7:
             #   brpoints[brown_index].appendleft(center)
            #elif colorIndex == 8:
             #   epoints[eraser_index].appendleft(center)
                # Append the next deques when nothing is detected to avois messing up
    else:
        if bpoints[-1] != deque(maxlen=512):
            bpoints.append(deque(maxlen=512))
            blue_index += 1

        if gpoints[-1] != deque(maxlen=512):
            gpoints.append(deque(maxlen=512))
            green_index += 1

        if rpoints[-1] != deque(maxlen=512):
            rpoints.append(deque(maxlen=512))
            red_index += 1

        if ypoints[-1] != deque(maxlen=512):
            ypoints.append(deque(maxlen=512))
            yellow_index += 1

        if wpoints[-1] != deque(maxlen=512):
            wpoints.append(deque(maxlen=512))
            white_index += 1

    

            # Draw lines of all the colors on the canvas and frame
    points = [bpoints, gpoints, rpoints, ypoints, wpoints]
    drawPoints(points, colors, frame)
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], (colors[i] * ev), 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], (colors[i] * ev), 2)

    # Show all the windows
    cv2.imshow("Canvas", frame)
    cv2.imshow("WhiteBoard", paintWindow)
    # cv2.imshow("mask",Mask)

    # Keyboard OP
    k = cv2.waitKey(10)
    if k == 27 or k == ord('q'):  # press ESC to exit
        cap.release()
        cv2.destroyAllWindows()
        break
    elif k == ord('1'):
        colorIndex = 0  # Blue
    elif k == ord('2'):
        colorIndex = 1  # Green
    elif k == ord('3'):
        colorIndex = 2  # Red
    elif k == ord('4'):
        colorIndex = 3  # Yellow
    elif k == ord('5'):
        colorIndex = 4  # Blue
    #elif k == ord('6'):
        #colorIndex = 5  # Green
    #elif k == ord('7'):
        #colorIndex = 6  # Red
    #elif k == ord('8'):
        #colorIndex = 7  # Yellow
    #elif k == ord('9'):
        #colorIndex = 8  # Yellow    
    elif k == ord('c'):  # press c to clear
        canvas = np.zeros_like(frame)
        bpoints = [deque(maxlen=512)]
        gpoints = [deque(maxlen=512)]
        rpoints = [deque(maxlen=512)]
        ypoints = [deque(maxlen=512)]
        wpoints = [deque(maxlen=512)]
        ppoints = [deque(maxlen=512)]
        bkpoints = [deque(maxlen=512)]
        brpoints = [deque(maxlen=512)]
        epoints = [deque(maxlen=512)]
       

        blue_index = 0
        green_index = 0
        red_index = 0
        yellow_index = 0
        white_index = 0
        pink_index = 0
        black_index = 0
        brown_index = 0
        eraser_index = 0
        paintWindow[67:, :, :] = 255
        frame = cv2.rectangle(frame, (40, 1), (140, 70), (0,0,0), 8)
        cv2.putText(frame, 'Screen Cleared', (275, 410), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 5)
        #cv2.putText(frame, 'Screen Cleared', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)

    elif k == ord('b') or iteration % 1000 == 2:  # press 'b' to capture the background
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        isBgCaptured = True
        print('Background Captured')
    elif k == ord('+') or k == ord('='):  # brush size

        if brush <= maxi:
            brush = brush + 1
            # paintWindow[67:,:,:] = 255
        else:
            print("Maximum limit reached")
            #cv2.putText(frame, 'Maximum limit Reached!', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
            brush = 16
            # paintWindow[67:,:,:] = 255

    elif k == ord('-'):  # brush size
        if brush >= mini:
            brush = brush - 1
            paintWindow[67:, :, :] = 255
        else:
            print("Minimum limit reached")
            #cv2.putText(frame, 'Minimum limit Reached!', (885, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
            brush = 3
            paintWindow[67:, :, :] = 255
    elif k == ord('e'):
        ev = 0
    elif k == ord('s'):  # press 's' to save the screen
        board = np.zeros([frame.shape[0], frame.shape[1]], np.uint8)  # initialize white board
        drawBoardPoints(points, board)
        cv2.imshow("Blackboard", board)
        filename = time.strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
        cv2.imwrite(filename, board)
        print('Screen Shot Taken ' + filename)
    elif k == ord('z'):  # press 'z' undo
        try:
            if colorIndex == 0:
                bpoints.pop(max(last_blue_index))
                last_blue_index.remove(max(last_blue_index))
                blue_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 1:
                gpoints.pop(max(last_green_index))
                last_green_index.remove(max(last_green_index))
                green_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 2:
                rpoints.pop(max(last_red_index))
                last_red_index.remove(max(last_red_index))
                red_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 3:
                ypoints.pop(max(last_yellow_index))
                last_yellow_index.remove(max(last_yellow_index))
                yellow_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 4:
                wpoints.pop(max(last_white_index))
                last_white_index.remove(max(last_white_index))
                white_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 5:
                ppoints.pop(max(last_pink_index))
                last_pink_index.remove(max(last_pink_index))
                pink_index -= 1
                paintWindow[67:, :, :] = 255    
            elif colorIndex == 6:
                bkpoints.pop(max(last_black_index))
                last_black_index.remove(max(last_black_index))
                black_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 7:
                brpoints.pop(max(last_brown_index))
                last_brown_index.remove(max(last_brown_index))
                brown_index -= 1
                paintWindow[67:, :, :] = 255
            elif colorIndex == 8:
                epoints.pop(max(last_eraser_index))
                last_eraser_index.remove(max(last_eraser_index))
                eraser_index -= 1
                paintWindow[67:, :, :] = 255
                
        except:
            pass
        print('Return One Stroke')

    iteration += 1

    # If the 'q' key is pressed then stop the application
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
