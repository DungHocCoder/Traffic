import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model

model = load_model('model1.h5')

classes = {1: 'Giới hạn tốc độ (20km/h)',
           2: 'Giới hạn tốc độ (30km/h)',
           3: 'Giới hạn tốc độ (50km/h)',
           4: 'Giới hạn tốc độ (60km/h)',
           5: 'Giới hạn tốc độ (70km/h)',
           6: 'Giới hạn tốc độ (80km/h)',
           7: 'Kết thúc giới hạn tốc độ (80km/h)',
           8: 'Giới hạn tốc độ (100km/h)',
           9: 'Giới hạn tốc độ (120km/h)',
           10: 'Cấm vượt',
           11: 'Cấm vượt xe tải trên 3.5 tấn',
           12: 'Quyền ưu tiên tại giao lộ',
           13: 'Đường ưu tiên',
           14: 'Nhường đường',
           15: 'Stop',
           16: 'Cấm xe cơ giới',
           17: 'Cấm xe tải',
           18: 'Cấm vào',
           19: 'Cảnh báo chung',
           20: 'Curve nguy hiểm bên trái',
           21: 'Curve nguy hiểm bên phải',
           22: 'Cua hai chiều',
           23: 'Đường gập ghềnh',
           24: 'Đường trơn trượt',
           25: 'Đường hẹp bên phải',
           26: 'Công trường đang thi công',
           27: 'Đèn giao thông',
           28: 'Người đi bộ',
           29: 'Băng qua đường có trẻ em',
           30: 'Băng qua đường có xe đạp',
           31: 'Cảnh báo đường trơn',
           32: 'Cảnh báo vượt qua nơi thường có động vật hoang dã',
           33: 'Kết thúc các giới hạn tốc độ và vượt quá',
           34: 'Chỉ đường rẽ phải tiếp theo',
           35: 'Chỉ đường rẽ trái tiếp theo',
           36: 'Chỉ được phép đi thẳng',
           37: 'Chỉ được phép đi thẳng hoặc rẽ phải',
           38: 'Chỉ được phép đi thẳng hoặc rẽ trái',
           39: 'Phía bên phải đi',
           40: 'Phía bên trái đi',
           41: 'Buồng lái bắt buộc',
           42: 'Hết cấm vượt',
           43: 'Hết cấm vượt xe tải trên 3.5 tấn',
           44: 'Nơi giao nhau theo vòng xuyến'}

top = tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    try:
        global label_packed
        image = Image.open(file_path)
        image = image.resize((30, 30))
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image = numpy.asarray(image)
        image = numpy.expand_dims(image, axis=0)
        print(image.shape)
        pred = model.predict([image])
        pred_class = pred.argmax(axis=-1)[0]
        sign = classes[pred_class + 1]
        print(sign)
        label.configure(foreground='#011638', text=sign)
    except:
        label.configure(foreground='#011638', text="Error Occurred")

def show_classify_button(file_path):
    classify_b = Button(top, text="Classify", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Traffic Sign Recognition", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()

