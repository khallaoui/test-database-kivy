from kivy.lang import Builder
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector

Window.clearcolor = (89/255.0, 7/255.0, 45, 3)
Window.size = (400, 600)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"


        return Builder.load_file('second_db.kv')

    def submit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")



        c = mydb.cursor()
        cmd="INSERT INTO etudiant (name) VALUES (%s)"
        val= (self.root.ids.word_input.text,)
        c.execute(cmd, val)
        self.root.ids.word_label.text=f'{self.root.ids.word_input.text} ADDED '
        self.root.ids.word_input.text=''

        mydb.commit()
        mydb.close()

    def show (self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")

        c = mydb.cursor()
        c.execute("select * from etudiant")
        rec = c.fetchall()


        for rec in rec:
            word = f'{rec[0]}'
            self.root.ids.word_label.text = f'{word}'

            a = f'{rec[1]}'
            self.root.ids.l1.text = f'{a}'

            b = f'{rec[2]}'
            self.root.ids.l2.text = f'{b}'

            d = f'{rec[3]}'
            self.root.ids.l3.text = f'{d}'

            e = f'{rec[4]}'
            self.root.ids.l4.text = f'{e}'

        mydb.commit()
        mydb.close()


if __name__ == '__main__':
    MainApp().run()
