# Project-Restaurant-System

# ทำการติดตั้ง Packate ที่เกี่ยวข้องไว้ใน Raspberry Pi
    
    sudo apt-ge update
    sudo apt-get upgrade
    sudo apt-get install rpi.gpio
    sudo apt uninstall python
    sudo apt install python3-pip
    sudo pip3 install requests
    sudo pip3 install imutils
    
  ติดตั้ง Environment ของ TensorFlow และ Packate ที่จำเป็นได้จาก วิธีต่อไปนี้ https://qengineering.eu/install-tensorflow-2.1.0-on-raspberry-pi-4.html
  
# การสร้าง Model
  สามารถสร้างได้จากไฟล์ที่ชื่อว่า Train.py 
  โดยไฟล์ Data Set จะอยู่ใน Folder ชื่อ Data_Set และคำตอบของ Data Set จะอยู่ในเดียวกันโดยมีชื่อว่า ANS.csv
  
  เมื่อได้ Model ของ TensorFlow มาแล้วสามารถทำการแปลง TensorFlow Model เป็น TensorFlow Lite Model ได้โดย ไฟล์ชื่อ ConvertTF_Full_to_lite.py

# Web Site
  ทำการติดตั้ง Node js ให้กับ Raspberry Pi
    wget https://nodejs.org/dist/v8.9.0/node-v8.9.0-linux-armv6l.tar.gz
    cd node-v6.11.1-linux-armv6l/
    sudo cp -R * /usr/local/
   
   จากนั้นไปที่ Folder Web Site แล้วทำการพิมพ์คำสั่งต่อไปนี้
    npm install
    npm run build
    
   และสามารถทำการสั่งทำงานได้โดย
    npm run start
  
# ตั้ง Auto Start
  เป็นการตั้งค่าให้ระบบทั้งหมดทำงานโดยอัตโนมัติหลังจากที่ทำการเปิดเครื่อง Raspberry Pi
  สามารถทำตามโดย https://tart-kreangkrai.medium.com/%E0%B8%A3%E0%B8%B1%E0%B8%99%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%9A%E0%B8%B9%E0%B8%95%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87-%E0%B8%9A%E0%B8%99-raspberry-pi-7c18c885d69
  
  โดยที่ถ้าเป็นส่วนของ Node js หรือตัว Web Site ต้องทำการให้สิทธิ sudo ก่อนเสมอ
  
  
# การสั่งโปรแกรมทำงาน
  สามารถที่จะทำการทดสอบการทำการของระบบก่อนที่จะทำการทำงานจริงได้ที่ไฟล์ TestStartShow.py
  
  เมื่อพร้อมเสร็จสิ้นทุกกระบวนการสามารถทำงนระบบได้โดยไฟล์ Start.py 
  
  
#### ต้องทำการทำงาน Web Site ก่อนที่จะทำงาน Start.py


