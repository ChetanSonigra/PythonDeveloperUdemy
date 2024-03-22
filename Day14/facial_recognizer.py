import cv2, os
import face_recognition as fr

path = os.getcwd()

# load images
control_picture = fr.load_image_file(f'{path}/python1/Day14/Chetan.JPG')
test_picture = fr.load_image_file(f'{path}/python1/Day14/Chetan4.png')

# transform image into RGB
control_picture = cv2.cvtColor(control_picture,cv2.COLOR_BGR2RGB)
test_picture = cv2.cvtColor(test_picture,cv2.COLOR_BGR2RGB)

# show images
#cv2.imshow('My Control Pic',control_picture)
#cv2.imshow('My Test Pic', test_picture)

# locate control faces
face_A_location = fr.face_locations(control_picture)[0]
coded_face_A = fr.face_encodings(control_picture)[0]

face_B_location  = fr.face_locations(test_picture)[0]
coded_face_B = fr.face_encodings(test_picture)[0]
#print(face_A_location)

# show rectangle
control_picture = cv2.rectangle(control_picture,(face_A_location[3], face_A_location[0]),
              (face_A_location[1], face_A_location[2]),
              (0,255,0),
              2)

test_picture = cv2.rectangle(test_picture, (face_B_location[3],face_B_location[0]),
              (face_B_location[1],face_B_location[2]),
              (0,255,0),
              2)

# perform comparison
result = fr.compare_faces([coded_face_A], coded_face_B, 0.5)
print(result)

# Measurement of distances
distance = fr.face_distance([coded_face_A], coded_face_B)
print(distance)

# show result
test_picture = cv2.putText(test_picture,
            f'{result}  {distance.round(2)}',
            (250,250),
            cv2.FONT_HERSHEY_COMPLEX,
            1, (0,255,0), 2)


cv2.imshow('control image',control_picture)
cv2.imshow('test image', test_picture)


# keep the program working.
cv2.waitKey(0)