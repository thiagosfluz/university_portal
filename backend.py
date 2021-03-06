import sqlite3
from tkinter import *

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS major (id integer PRIMARY KEY not null, name text not null, courses_id text not null, FOREIGN KEY (courses_id) references courses (id))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS student (id integer PRIMARY KEY not null, name text not null, major_name text not null, "
                         "FOREIGN KEY (major_name) references major (name))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS courses (id integer PRIMARY KEY not null, year integer not null, semester integer not null, course1 integernot null, course2 integer not null, FOREIGN KEY (course1) references course (id),FOREIGN KEY (course2) references course (id) )")
        self.cur.execute("CREATE TABLE IF NOT EXISTS course (id integer PRIMARY KEY not null, name text not null, hourly integer not null)")
        self.conn.commit()

    def insert_student(self, id, name, major_name):
        try:
            self.cur.execute("INSERT INTO student VALUES (?, ?, ?)", (id, name, major_name))
            self.conn.commit()
            self.alert_popup("Success", "The student was recorded!")
            print("Success")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_student(self):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        print("Imprimindo ROWS" + str(rows))
        return rows

    def insert_major(self, id, name, courses_id):
        try:
            self.cur.execute("INSERT INTO major VALUES (?, ?, ?)", (id, name, courses_id))
            self.conn.commit()
            self.alert_popup("Success", "The major was recorded!")
            print("Success")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_major(self):
        self.cur.execute("SELECT name FROM major")
        rows = self.cur.fetchall()
        return rows

    def insert_courses(self, id, year, semester, course1, course2):
        try:
            print(id, year, semester, course1, course2)
            self.cur.execute("INSERT INTO courses VALUES (?, ?, ?, ?, ?)", (id, year, semester, course1, course2))
            self.conn.commit()
            self.alert_popup("Success", "The curriculum was recorded!")
            print("Success")
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            self.alert_popup("Try again", "ERROR")

    def view_courses(self):
        self.cur.execute("SELECT * FROM courses")
        rows = self.cur.fetchall()
        return rows

    def insert_course(self, id, name, hourly):
        try:
            self.cur.execute("INSERT INTO course VALUES (?, ?, ?)", (id, name, hourly))
            self.conn.commit()
            self.alert_popup("Success", "The course was recorded!")
            print("Success")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_course(self):
        self.cur.execute("SELECT id FROM course")
        rows = self.cur.fetchall()
        print("Imprimindo ROWS" + str(rows))
        return rows

    def alert_popup(self, title, message):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)
        w = 400  # popup window width
        h = 200  # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()


