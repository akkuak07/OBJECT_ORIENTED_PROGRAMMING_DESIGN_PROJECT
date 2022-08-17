import foodappui as ui
import foodappclasses as clss


def appflow():

    option = ui.mainmenu()
    if option == 1:
        data = ui.signupmenu()
        userObj = clss.user(data)
        if userObj.validate():
            userObj.insert(data)
            ui.welcomemsg(userObj.getname())
            appflow()
        else:
            ui.alreadyexists()
            appflow()

    elif option == 2:
        data = ui.loginmenu()
        userObj = clss.user(data)
        if userObj.auth():
            userObj.fetchnsetuserdata()
            ui.welcomemsg(userObj.getname())
            userObj.setaddress()
            usradd = userObj.getaddress()
            rObj = clss.restaurants()
            rdetails = rObj.fetchall()
            roption = ui.showrestaurants(rdetails)
            rObj.fetchandsetrestaurant(roption)
            devdata = rObj.calculateeta(usradd)
            mObj = clss.menu()
            mdetails = mObj.fetchall(roption)
            cart = ui.showmenu(mdetails, devdata[1])
            if len(cart) == 0:
                ui.exitmsg()
                appflow()
            else:
                cartObj = clss.cart(list(cart.values()))
                cartObj.calculatebill()
                amount = cartObj.getamount()
                if(amount < 100):
                    ui.amountless()
                    appflow()
                else:
                    paymentObj = clss.payment()
                    deliverychg = paymentObj.deliverycharges(devdata[0])
                    couponstatus = userObj.getcouponstatus()
                    disfac = ui.showbill(amount, deliverychg, couponstatus)
                    print(disfac)
                    tamount = paymentObj.finalpayment(disfac, amount)
                    while(True):
                        paydet = ui.paymentmethod(tamount)
                        email = userObj.getemail()
                        bdObj = clss.bankingdetail(email)
                        bdObj.fetchnsetbd()
                        validflag = bdObj.validate(paydet)
                        if validflag:
                            ui.paymentdone()
                            break
                        else:
                            ui.invaliddata()

        else:
            ui.invaliddata()
            appflow()

    else:
        ui.exitmsg()
        ui.os.system('exit')


if __name__ == "__main__":
    appflow()
