'''import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from keras.preprocessing import image
import numpy as np
#load the trained model to classify the images
from keras.models import load_model
model = load_model('monkey_bred_model.h5')
classes = { 
   
	0:'mantled_howler', 
	1:'patas_monkey', 
	2:'bald_uakari', 
	3:'japanese_macaque', 
	4:'pygmy_marmoset', 
	5:'white_headed_capuchin',
	6:'silvery_marmoset',
	7:'common_squirrel_monkey', 
	8:'black_headed_night_monkey',
	9:'nilgiri_langur' 
	
}
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Monkey Breed Classification')


def classify(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32')/255
    pred = np.argmax(model.predict(x))
    res="It's a {}.".format(classes[pred])
    lbl3=Label(top,text=res,font='Helvetica 12 bold')
    lbl3.pack()


def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
   command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(bg="Aqua",fg="black",font="Helvetica 12 bold")
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
        (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image = Label(top)
        sign_image.configure(image=im)
        sign_image.pack(side=BOTTOM,expand=True)
        sign_image.image=im
        #label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,
  padx=10,pady=5)
upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)

#label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Monkey Breed Classification",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()



'''
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from keras.preprocessing import image
import numpy as np
#load the trained model to classify the images
from keras.models import load_model
model = load_model('monkey_bred_weights.h5')
#dictionary to label all the CIFAR-10 dataset classes.
classes = { 
   
	0:'mantled_howler', 
	1:'patas_monkey', 
	2:'bald_uakari', 
	3:'japanese_macaque', 
	4:'pygmy_marmoset', 
	5:'white_headed_capuchin',
	6:'silvery_marmoset',
	7:'common_squirrel_monkey', 
	8:'black_headed_night_monkey',
	9:'nilgiri_langur' 
	
}
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Monkey Breed  Classifier')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    img = image.load_img(file_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32')/255
    pred = np.argmax(model.predict(x))
    sign="It's a {}.".format(classes[pred])

    '''image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)'''
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
   command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
        (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,
  padx=10,pady=5)
upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Monkey Breed Classification",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()