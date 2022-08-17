import sqlite3 as sql
import numpy as np
from geopy.distance import geodesic


class database:

    __dbname = 'project.db'
    __conn = ""

    def openconnection(self):
        self.__conn = sql.connect(self.__dbname)
        return self.__conn

    def closeconnection(self):
        self.__conn.close()


class user(database):  # Inheritance

    # private members(Encapsulation)
    __uname = ""
    __email = ""
    __mobno = ""
    __pass = ""
    __coupon1 = 1
    __coupon2 = 1
    __wallet = "0"
    __address = tuple()

    def __init__(self, data):
        self.__email = data[0]
        self.__pass = data[1]

    def getname(self):
        return self.__uname

    def validate(self):
        db = database()
        conn = db.openconnection()
        email = self.__email
        cur = conn.cursor()
        cur.execute('''
        select * 
        from users
        where email= ?''', (email,))
        check = cur.fetchall()
        db.closeconnection()
        if(len(check) > 0):
            return False
        else:
            return True

    def insert(self, data):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        user = [self.__email,
                data[1],
                data[2],
                self.__pass,
                self.__coupon1,
                self.__coupon2,
                self.__wallet]
        cur.execute('''
        insert 
        into users
        values(?,?,?,?,?,?,?)''', user)
        conn.commit()
        db.closeconnection()

    def auth(self):
        check = self.fetch()
        if(len(check) > 0):
            return True
        else:
            return False

    def fetch(self):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        data = [self.__email, self.__pass]
        cur.execute('''
        select * 
        from users
        where email = ? and pass= ?
        ''', data)
        record = cur.fetchall()
        db.closeconnection()
        return record

    def setaddress(self):
        defadd = np.array([23.535, 87.295])
        self.__address = tuple(defadd - np.random.uniform(-0.005, 0.005))

    def getaddress(self):
        return self.__address

    def fetchnsetuserdata(self):
        record = self.fetch()[0]
        self.__uname = record[2]
        self.__email = record[0]
        self.__mobno = record[1]
        self.__pass = record[3]
        self.__coupon1 = record[4]
        self.__coupon2 = record[5]
        self.__wallet = record[6]

    def getcouponstatus(self):
        return [self.__coupon1, self.__coupon2]

    def getemail(self):
        return self.__email


class restaurants():

    __rid = ""
    __rname = ""
    __lon = ""
    __lat = ""
    __rating = ""
    __preptime = 20

    def fetchall(self):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        cur.execute('''
        select * 
        from restaurants
        ''')
        record = cur.fetchall()
        db.closeconnection()
        return record

    def fetch(self, rid):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        cur.execute('''
        select * 
        from restaurants
        where rid = ?
        ''', (rid,))
        record = cur.fetchall()[0]
        db.closeconnection()
        return record

    def fetchandsetrestaurant(self, rid):
        record = self.fetch(int(rid))
        self.__rid = record[0]
        self.__rname = record[1]
        self.__lon = record[2]
        self.__lat = record[3]
        self.__rating = record[4]

    def calculateeta(self, usradd):
        misctime = np.random.uniform(-5, 10)
        loc1 = (self.__lon, self.__lat)
        loc2 = usradd
        dist = geodesic(loc1, loc2)
        traveltime = (dist.km*60/20)
        eta = int(traveltime + self.__preptime + misctime)
        return [dist, eta]


class menu(restaurants):

    __rid = ""
    __fooditem = ""
    __price = ""
    __qty = ""

    def fetchall(self, rid):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        cur.execute('''
        select * 
        from menu
        where rid = ?
        ''', (rid,))
        record = cur.fetchall()
        db.closeconnection()
        return record


class cart():

    __fooditem = ""
    __price = ""
    __qty = ""
    __amount = 0

    def __init__(self, cart):
        self.__fooditem = [cart[i][0] for i in range(len(cart))]
        self.__price = [cart[i][1] for i in range(len(cart))]
        self.__qty = [cart[i][2] for i in range(len(cart))]

    def calculatebill(self):
        for i in range(len(self.__price)):
            self.__amount += (int(self.__price[i])*int(self.__qty[i]))
            print(self.__amount)

    def getamount(self):
        return self.__amount


class payment():

    __fixeddelchg = 5
    __deliverycharges = 0
    __devchgperkm = 5
    __total = 0

    def deliverycharges(self, dist):
        return self.__fixeddelchg + dist*self.__devchgperkm

    def finalpayment(self, disfac, amount):
        self.__total = disfac*(self.__deliverycharges + amount)
        return self.__total


class bankingdetail(payment):

    __mobno = ""
    __uname = ""
    __email = ""
    __balance = ""
    __ccno = ""
    __dcno = ""
    __pin = ""

    def __init__(self, email):
        self.__email = email

    def fetch(self):
        db = database()
        conn = db.openconnection()
        cur = conn.cursor()
        cur.execute('''
        select * 
        from bankingdetails
        where email = ?
        ''', (self.__email,))
        record = cur.fetchall()[0]
        db.closeconnection()
        return record

    def fetchnsetbd(self):
        record = self.fetch()
        self.__mobno = record[0]
        self.__uname = record[1]
        self.__email = record[2]
        self.__balance = record[3]
        self.__ccno = record[4]
        self.__dcno = record[5]
        self.__pin = record[6]

    def validate(self, paydet):
        if(paydet[0] == "1") and (int(self.__mobno) == int(paydet[1])) and (int(self.__pin) == int(paydet[2])):
            flag = True
        elif(paydet[0] == "2") and (self.__email == paydet[1]) and (int(self.__pin) == int(paydet[2])):
            flag = True
        elif(paydet[0] == "3") and (int(self.__dcno) == int(paydet[1])) and (int(self.__pin) == int(paydet[2])):
            flag = True
        elif(paydet[0] == "4") and (int(self.__ccno) == int(paydet[1])) and (int(self.__pin) == int(paydet[2])):
            flag = True
        else:
            flag = False

        return flag


'''
class order():

    __rid =
    __email =
    __amount =
    __ordertime =
    __scheduledarrival =
    __rating =
    '''
