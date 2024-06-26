# from tkinter import * #To make powerful Ui
# from tkinter import ttk #It contain special tools
# from PIL import Image,ImageTk #(PIL-Pillow library)To use images in our website and ImageTk is used to set the dimension of that image.
# from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import cv2
# # import Silent_Face_Anti_Spoofing_master.test
# from Silent_Face_Anti_Spoofing_master.test import test
# import os
# import numpy as np

# class Face_Recognition:
#     def __init__(self,root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition system")
        
#         #Title
#         title_lbl = Label(self.root, text="FACE RECOGNITION",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
#         title_lbl.place(x=0, y=0, width=1530, height=45)
        
#         #Set images
#         #First Image
#         img_top = Image.open(r"images\17.jfif")
#         img_top = img_top.resize((650, 700), Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
#         self.photoimg_top = ImageTk.PhotoImage(img_top)  # one of the built-in methods which has been used to add the user-defined images in the application.

#         f_lab1 = Label(self.root, image=self.photoimg_top)
#         f_lab1.place(x=0, y=55, width=650, height=700)
        
#         #Second Image
#         img_bottom = Image.open(r"images\16.jpg")
#         img_bottom = img_bottom.resize((950, 700),Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  # one of the built-in methods which has been used to add the user-defined images in the application.

#         f_lab1 = Label(self.root, image=self.photoimg_bottom)
#         f_lab1.place(x=650, y=55, width=950, height=700)
        
#         b1_1 = Button(f_lab1, text="Face Recognition", cursor="hand2",font=("times new roman", 18, "bold"),bg="darkgreen", fg="white",command=self.face_recog)
#         b1_1.place(x=375, y=558, width=200, height=40)
        
#     #======================Attendance=================================
#     def mark_attendance(self,i,r,n,d):
#         with open("temporary.csv","r+",newline="\n") as f:
#             myDataList = f.readlines()
#             name_list = []
#             for line in myDataList:
#                 entry = line.split((","))
#                 name_list.append(entry[0])
#             # print(i not in name_list, i)
#             if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
#                 # print(name_list)
                
        
        
#     #===============================Face Recognition==============================
#     def face_recog(self):
#         def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf,spoofing_value):
#             gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            
#             coord = []
            
#             for(x,y,w,h) in features:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict = clf.predict(gray_image[y:y+h,x:x+w])
#                 confidence = int((100*(1-predict/300)))
                
#                 conn = mysql.connector.connect(host="localhost",username= "root",password="abcd@1234",database="face_recognizer")
#                 my_cursor = conn.cursor()
                
#                 my_cursor.execute("select Name from student where Student_id="+str(id))
#                 n = my_cursor.fetchone()
#                 # n=str(n)
#                 n = "+".join(n)
                
                
#                 my_cursor.execute("select Roll from student where Student_id="+str(id))
#                 r = my_cursor.fetchone()
#                 # r=str(r)
#                 r = "+".join(r)
                
                
#                 my_cursor.execute("select Dep from student where Student_id="+str(id))
#                 d = my_cursor.fetchone()
#                 # d=str(d)
#                 d = "+".join(d)
                
                
#                 my_cursor.execute("select Student_id from student where Student_id="+str(id))
#                 i = my_cursor.fetchone()
#                 # i=str(i)
#                 if i:
#                     i = "+".join(i)

#                 if spoofing_value==1:
#                     if n == "None" or r == "None" or d == "None" or i == "None":
#                         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                         cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     elif confidence>75:
#                         cv2.putText(img, f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         cv2.putText(img, f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         cv2.putText(img, f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         cv2.putText(img, f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         self.mark_attendance(i,r,n,d)
#                     else:
#                         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                         cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Static Image",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)


#                 # if confidence > 75:
#                 #     cv2.putText(img,f"Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                 #     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                 #     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                 #     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                 #     self.mark_attendance(i,r,n,d)
#                 # else:
#                 #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                 #     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
#                 coord = [x,y,w,h]
#             return coord
        
#         def recognize(img,clf,faceCascade,spoofing_value):
#             coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf,spoofing_value)
#             return img
        
#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")
        
#         video_cap = cv2.VideoCapture(0)
        
#         while True:
#             ret,img = video_cap.read()
#             # img = recognize(img,clf,faceCascade)
#             spoofing_value=test(
#                 image=img,
#                 model_dir=r"Silent_Face_Anti_Spoofing_master/resources/anti_spoof_models",
#                 device_id=0
#                 )
#             # print(spoofing_value)
#             img = recognize(img,clf,faceCascade,spoofing_value)
#             cv2.imshow("Welcome to Face Recognition",img)
            
#             if cv2.waitKey(1) == 13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()
        
        
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()



from tkinter import * #To make powerful Ui
from tkinter import ttk #It contain special tools
from PIL import Image,ImageTk #(PIL-Pillow library)To use images in our website and ImageTk is used to set the dimension of that image.
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from Silent_Face_Anti_Spoofing_master.test import test

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")
        
        #Title
        title_lbl = Label(self.root, text="FACE RECOGNITION",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #Set images
        #First Image
        img_top = Image.open(r"images\17.jfif")
        img_top = img_top.resize((650, 700), Image.LANCZOS)  # Image.LANCZOS convert the image from high level to low level.
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab1 = Label(self.root, image=self.photoimg_top)
        f_lab1.place(x=0, y=55, width=650, height=700)

        #Second Image
        img_bottom = Image.open(r"images\16.jpg")
        img_bottom = img_bottom.resize((950, 700),Image.LANCZOS)  # Image.LANCZOS convert the image from high level to low level.
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  # one of the built-in methods which has been used to add the user-defined images in the application.
        

        f_lab1 = Label(self.root, image=self.photoimg_bottom)
        f_lab1.place(x=650, y=55, width=950, height=700)
        
        b1_1 = Button(f_lab1, text="Face Recognition", cursor="hand2",font=("times new roman", 18, "bold"),bg="darkgreen", fg="white",command=self.face_recog)
        b1_1.place(x=375, y=558, width=200, height=40)
        
    #======================Attendance=================================
    def mark_attendance(self,i,r,n,d):
        with open("temporary.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                # print(name_list)
        
        
    #===============================Face Recognition==============================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf,spoofing_value):
            
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            
            coord = []
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image)
                confidence = int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="abcd@1234", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute(f"select Name from student LIMIT 1 OFFSET {id-1}")
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)
                
                my_cursor.execute(f"select Roll from student LIMIT 1 OFFSET {id-1}")
                
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)
                
                my_cursor.execute(f"select Dep from student LIMIT 1 OFFSET {id-1}")
                
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)
                
                my_cursor.execute(f"select Student_id from student LIMIT 1 OFFSET {id-1}")
                i = my_cursor.fetchone()
                if i:
                    i=str(i)
                    i=i[1:-2]
                    # i = "+".join(i)
                if spoofing_value==1:
                    if confidence > 75:
                        cv2.putText(img,f"Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(i,r,n,d)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Static Image",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    
                coord = [x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade,spoofing_value):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf,spoofing_value)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret,img = video_cap.read()
            
            spoofing_value=test(
                image=img,
                model_dir=r"Silent_Face_Anti_Spoofing_master/resources/anti_spoof_models",
                device_id=0
                )
            # print(spoofing_value)
            img = recognize(img,clf,faceCascade,spoofing_value)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()