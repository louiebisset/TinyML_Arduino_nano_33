import serial, numpy as np, cv2, time

PORT = "COM15"          # Linux: /dev/ttyACM0   Mac: /dev/cu.usbmodemXXXX
W, H = 176, 144

ser = serial.Serial(PORT, 1000000, timeout=1)
count = 0

while True:
    ser.read_until(b"FRAM")                  # sync to start of frame
    raw = ser.read(W * H)
    if len(raw) != W * H:
        continue
    img = np.frombuffer(raw, np.uint8).reshape(H, W)
    cv2.imshow("OV7675", cv2.resize(img, None, fx=4, fy=4,
                                    interpolation=cv2.INTER_NEAREST))
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):                      # save a frame
        cv2.imwrite(f"sign_{count:04d}.png", img)
        count += 1
        print("saved", count)
    elif key == ord("q"):
        break