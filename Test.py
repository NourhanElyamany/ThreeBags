import cv2
comp_plays=3
user_plays=4
image=cv2.imread('test.jpg',0)
cv2.imshow('image',image)

font= cv2.FONT_HERSHEY_SIMPLEX
if(comp_plays>=user_plays):
    cv2.putText(image,'Computer is the winner',(100,200),font,1,(0,0,255))
    print('computer wins')
else:
    cv2.putText(image,'User is the winner' ,(100,200),font,1,(0,0,255))
    print('user wins')
cv2.imshow('image',image)
cv2.waitkey(0)
cv2.destroyAllWindows()