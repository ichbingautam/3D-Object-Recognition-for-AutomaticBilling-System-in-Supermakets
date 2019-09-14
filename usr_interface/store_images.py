import cv2
def main():
    
    cam = cv2.VideoCapture(1)
    cv2.namedWindow("Grocery-Object Recognition Phase-1")
    img_counter = 1
    while True:
        ret, frame = cam.read()
        cv2.imshow("Grocery-Object Recognition Phase-1", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "../saved_image/image{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
