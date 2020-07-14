from tkinter import *
from selenium import webdriver
from time import sleep
#interactivity functions
def flamess(firstname,secondname):
    l=[i for i in firstname]
    s=[i for i in secondname]
    for i in range(len(l)):
        for j in range(len(s)):
            if(l[i]==s[j]):
                l[i]=0
                s[j]=0
    l=[i for i in l if i!=0 and i!=' ']
    s=[i for i in s if i!=0 and i!=' ']
    c=len(s)+len(l)
    l=['Friends','Love','Affection','Mariage','Enemies','Sister']
    while(len(l)>1):
        si=(c%len(l)-1)
        if(si>=0):
            l=l[si+1::]+l[:si:]
        else:
            l=l[:len(l)-1:]
    relation="relation :"+l[0]
    p=Tk()
    p.geometry("25x25+400+190")
    l1=Label(p,text=relation)
    l1.pack()
def zodiacc(month,day):
    if month == 'december': 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == 'january': 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == 'february': 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == 'march': 
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == 'april': 
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == 'may': 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == 'june': 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == 'july': 
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == 'august': 
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == 'september': 
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == 'october': 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    else: 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    tk=Tk()
    l=Label(tk,text=astro_sign)
    l.pack()
def run(driver_path,url,search=0,user=0,password=0,mail=0,pwd=0,login=0,instaname=0,instapwd=0,gmailnext=0,gmailpassnext=0,searchb=0,searchclick=0,searchgooglesug=0,searchgoogle=0,satelite=0):
    driver=webdriver.Chrome(driver_path)
    driver.get(url)
    sleep(3)
    if(user!=0 and password!=0):
        if(instaname==0):
            driver.find_element_by_xpath(mail).send_keys(user)
            if(gmailnext!=0):
                driver.find_element_by_xpath(gmailnext).click()
                sleep(3)
            driver.find_element_by_xpath(pwd).send_keys(password)
            if(gmailpassnext!=0):
                driver.find_element_by_xpath(gmailpassnext).click()
            else:
                driver.find_element_by_xpath(login).click()
        else:
            driver.find_element_by_name(instaname).send_keys(user)
            driver.find_element_by_name(instapwd).send_keys(password)
            driver.find_element_by_xpath(login).click()
    else:
        driver.find_element_by_xpath(searchb).send_keys(search)
        if(searchgooglesug!=0):
            sleep(3)
            try:
                driver.find_element_by_xpath(searchgoogle).click()
            except:
                driver.find_element_by_xpath(searchgooglesug).click()
        else:
            driver.find_element_by_xpath(searchclick).click()
            if(satelite!=0):
                sleep(3)
                driver.find_element_by_xpath(satelite).click()
#GUI functions
def logos():
    youtub=Button(window,text="YouTube",command=youtube,fg="white",bg="red",font="ansi 14 bold",height=2,width=8)
    fab=Button(window,text="Facebook",command=fb,fg="white",bg="Royal blue2",font="ansi 14 bold",height=2,width=8)
    inst=Button(window,text="Instagram",command=insta,fg="white",bg="tomato2",font = "ansi 14  bold ",height=2,width=8)
    gmai=Button(window,text="G-mail",command=gmail,fg="white",bg="black",font="ansi 14 bold",height=2,width=8)
    ma=Button(window,text="Maps",command=maps,fg="white",bg="green",font="ansi 14 bold",height=2,width=8)
    niv=Button(window,text="NIVA",command=niva,fg="black",bg="white",font=" ansi 14  bold italic",height=2,width=8)
    flame=Button(window,text="Flames",command=flames,fg="red",bg="khaki",font=" ansi 14  bold italic",height=2,width=8)
    zodia=Button(window,text="Zodiac",command=zodiac,fg="red",bg="bisque4",font=" ansi 14  bold italic",height=2,width=8)
    googlesear=Button(window,text="Google Search",command=googlesearch,fg="black",bg="white",font="system 6 bold",height=1,width=12)
    youtub.place(x=450,y=250)
    fab.place(x=570,y=250)
    inst.place(x=690,y=250)
    gmai.place(x=810,y=250)
    ma.place(x=450,y=350)
    niv.place(x=570,y=350)
    flame.place(x=690,y=350)
    zodia.place(x=810,y=350)
    googlesear.place(x=625,y=195)
def youtube(event=None):
    tk2=Tk()
    tk2.geometry("375x150+400+190")
    tk2.title("youtube")
    l1=Label(tk2,text="Enter video name",fg="white",bg="black",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    e1=Entry(tk2)
    e1.grid(row=0,column=1)
    def printf2(event):
        x1=e1.get()
        run(driver_path=driver_path,url=youtube_url,search=x1,searchb=youtube_search_box,searchclick=youtube_search_button)
    b1=Button(tk2,text="Go",command=lambda:printf2(event))
    b1.grid(row=2,column=1)
    tk2.bind("<Return>",printf2)
def fb(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("facebook")
    e1=Entry(tk1)
    e2=Entry(tk1,show="*")
    def printf(event):
        x=e1.get()
        y=e2.get()
        run(driver_path=driver_path,url=fb_url,user=x,password=y,mail=fb_mail_box,pwd=fb_pwd_box,login=fb_login_button)
    l1=Label(tk1,text="User-id or Mobile number",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="Password",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Login",command=lambda:printf(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf)
def insta(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("instagram")
    e1=Entry(tk1)
    e2=Entry(tk1,show="*")
    def printf(event):
        x=e1.get()
        y=e2.get()
        run(driver_path=driver_path,url=insta_url,user=x,password=y,instaname=insta_mail_box,instapwd=insta_pwd_box,login=insta_login_button)
    l1=Label(tk1,text="User-id or Mobile number",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="Password",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Login",command=lambda:printf(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf)
def gmail(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("gmail")
    e1=Entry(tk1)
    e2=Entry(tk1,show="*")
    def printf(event):
        x=e1.get()
        y=e2.get()
        run(driver_path=driver_path,url=gmail_url,user=x,password=y,mail=gmail_box,pwd=gmail_pwd_box,gmailnext=gmail_box_next_button,gmailpassnext=gmail_pwd_next_button)
    l1=Label(tk1,text="User-id or Mobile number",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="Password",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Login",command=lambda:printf(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf)
def maps(event=None):
    tk2=Tk()
    tk2.geometry("375x150+400+190")
    tk2.title("maps")
    l1=Label(tk2,text="Enter the location",fg="white",bg="black",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    e1=Entry(tk2)
    e1.grid(row=0,column=1)
    def printf4(event):
        x1=e1.get()
        run(driver_path=driver_path,url=g_maps_url,search=x1,searchb=g_maps_search_box,searchclick=g_maps_search_button,satelite=g_maps_satelite_button)
    b1=Button(tk2,text="Go",command=lambda:printf4(event))
    b1.grid(row=2,column=1)
    tk2.bind("<Return>",printf4)
def niva(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("niva")
    e1=Entry(tk1)
    e2=Entry(tk1,show="*")
    def printf2(event):
        x=e1.get()
        y=e2.get()
        run(driver_path=driver_path,url=niva_url,user=x,password=y,mail=niva_rollno_box,pwd=niva_pwd_box,login=niva_login_button)
    l1=Label(tk1,text="Enter Roll No",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="Enter Password",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Go",command=lambda:printf2(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf2)
def googlesearch(event=None):
    tk2=Tk()
    tk2.geometry("300x155+520+180")
    tk2.title("googlesearch")
    l1=Label(tk2,text="Enter search",fg="white",bg="black",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    e1=Entry(tk2)
    e1.grid(row=0,column=1)
    def printf4(event):
        x1=e1.get()
        run(driver_path=driver_path,url=google_url,search=x1,searchb=google_search_box,searchgooglesug=gsb_search_button_sugest,searchgoogle=gsb_search_button)
    b1=Button(tk2,text="Go",command=lambda:printf4(event))
    b1.grid(row=2,column=1)
    tk2.bind("<Return>",printf4)
def flames(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("flames")
    e1=Entry(tk1)
    e2=Entry(tk1)
    def printf(event):
        x=e1.get()
        y=e2.get()
        flamess(x,y)
        tk1.destroy()
    l1=Label(tk1,text="first person name",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="second person name",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Go",command=lambda:printf(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf)
def zodiac(event=None):
    tk1=Tk()
    tk1.geometry("375x150+400+190")
    tk1.title("zodiac")
    e1=Entry(tk1)
    e2=Entry(tk1)
    def printf(event):
        x=e1.get()
        y=e2.get()
        zodiacc(x,int(y))
    l1=Label(tk1,text="Month",fg="Royal blue4",font="ansi 14 bold")
    l1.grid(row=0,column=0)
    l2=Label(tk1,text="Date",fg="Royal blue4",font="ansi 14 bold")
    l2.grid(row=1,column=0)
    b1=Button(tk1,text="Go",command=lambda:printf(event))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    tk1.bind("<Return>",printf)
#program starts
if __name__=="__main__":
    driver_path="E:\\selenium\\chromedriver.exe"
    fb_url='https://www.facebook.com/'
    fb_mail_box='//*[@id="email"]'
    fb_pwd_box='//*[@id="pass"]'
    fb_login_button="//*[@id='u_0_2']"
    gmail_url='https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession'
    gmail_box='//*[@id="identifierId"]'
    gmail_pwd_box='//*[@id="password"]/div[1]/div/div[1]/input'
    gmail_box_next_button="//*[@id='identifierNext']/content/span"
    gmail_pwd_next_button='//*[@id="passwordNext"]/content/span'
    insta_url='https://www.instagram.com/accounts/login/?hl=en'
    insta_mail_box='username'
    insta_pwd_box='password'
    insta_login_button="//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]"
    niva_url="https://niva.vidyanikethan.edu/Login.aspx"
    niva_rollno_box="//*[@id='UserName']"
    niva_pwd_box="//*[@id='Password']"
    niva_login_button="//*[@id='LoginButton']"
    g_maps_url="https://www.google.com/maps"
    g_maps_search_box="//*[@id='searchboxinput']"
    g_maps_search_button="//*[@id='searchbox-searchbutton']"
    g_maps_satelite_button="//*[@id='minimap']/div/div[2]/button"
    youtube_url="https://www.youtube.com"
    youtube_search_box="//*[@id='search']"
    youtube_search_button="//*[@id='search-icon-legacy']"
    google_url="https://www.google.com/"
    google_search_box="//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input"
    gsb_search_button_sugest="//*[@id='tsf']/div[2]/div/div[2]/div[2]/div/center/input[1]"
    gsb_search_button="//*[@id='tsf']/div[2]/div/div[3]/center/input[1]"
    window=Tk()
    window.title("VIP")
    canvas=Canvas(window,width=1366,height=768)
    canvas.pack()
    my_image=PhotoImage(file="C:\\Users\\deepa\\new.png")
    canvas.create_image(0,0,anchor=NW,image=my_image)
    logos()
