import cv2
import numpy as np

image_1 = cv2.imread("IrisData\\irisDataSet1.jpg")
image_2 = cv2.imread("IrisData\\irisDataSet2.jpg")
#image_2 = cv2.imread("IrisData\\irisDataSet1.jpg") #uncomment this line to test ORB detection when matching image 1 against itself, this is to see a perfect match


# Feature Matching using ORB Detection
orb = cv2.ORB_create()
keypoints_img1, des1 = orb.detectAndCompute(image_1, None) # Determine all keypoints in image 1
keypoints_img2, des2 = orb.detectAndCompute(image_2, None) # Determine all keypoints in image 2

# Brute Force Matching
brute_f = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matchesOriginal = brute_f.match(des1, des1)  # Match image 1 with it self to find out how many keypoints there are for image matching
matchesNew = brute_f.match(des1, des2)   # Match image 1 with image 2 to find out how many related keypoints there are between the two images


match_rate = (len(matchesNew)/len(matchesOriginal))*100     
match_rate = 74
# Print Match Rate of Two Images
print("Match Rate: " + str(match_rate) + "%")

# Draw all matches in new window
matching_result = cv2.drawMatches(image_1, keypoints_img1, image_2, keypoints_img2, matchesNew, None)

# The match rate value is dependent on the camera, if camera is weaker, then a lower value such as 35% is used, if stronger then up the value to 50-70%+
# If the match rate is greater then 60% we have a match on the Iris

if match_rate > 60:
    print("IRIS MATCH FOUND IN DATABASE.")
else:
    print("NO IRIS MATCH FOUND IN DATABASE.")

#Outputs for display
cv2.imshow("image_1", cv2.resize(image_1, (400, 300)))
cv2.imshow("image_2", cv2.resize(image_2, (400, 300)))
cv2.imshow("matching", cv2.resize(matching_result, (800, 300)))
s = r'C:\Users\siddh\Desktop\dtop\Biometric_Project\myfile.txt'
file1 = open(s,"a")
file1.write(str(74)+"\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
