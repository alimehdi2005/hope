import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:")


def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def load_lottieur2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def load_lottieur3(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


goals_lottie = load_lottieur2("https://assets3.lottiefiles.com/packages/lf20_jsignqmt.json")
lottie_coding = load_lottieur1("https://assets4.lottiefiles.com/packages/lf20_cmaqoazd.json")
volunteer_lottie = load_lottieur3("https://assets8.lottiefiles.com/packages/lf20_HF41OKnIK9.json")
img_trade_setup = Image.open("images/IMG_4999 copy 2 Small.jpeg")
img_coding = Image.open("images/IMG_9366.JPG")
img_deca = Image.open("images/IMG_9562.jpg")
img_deca_2 = Image.open("images/IMG_9953.JPG")
projectdemo = open("images/snake.demo.mov", "rb")
calcdemo = open("images/calulator demo.mov", "rb")
icdemo = open("images/i&c demo.mp4", "rb")
pongdemo = open("images/pong demo.mov", "rb")
img_mcgill = Image.open("images/mcgill ss.png")

with st.container():
    st.subheader("Hi, my name is Ali :wave:")
    st.title("Student at St.Roch Secondary School")
    st.write('##')
    st.header('OBJECTIVE')
    st.write('My objective is to use the resources and'
             ' support provided through this program to further '
             'develop my computer programming skills and build '
             'on my business knowledge. In addition, my work experience '
             'at a retail store and an Accounting firm will give me an advantage '
             'and allow me to perform my best in this program. '
             'Finally, this program will enable me to pursue topics I am involved in and envision a career in.')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WORK EXPERIENCE")
        st.write("##")
        st.subheader('Awan CPA')
        st.write(
            """
        - Awan CPA is an accounting firm located in Mississauga Ontario.
          I've been taking part in a cooperative learning programme here for
          five months, which has given me significant exposure with a variety 
          of general accounting procedures, including data entry, preparing 
          financial records, investments, taxes, payroll, and given me an idea 
          of what it takes being a Chartered Accountant.
          """
        )
        st.subheader('Roots Canada')
        st.write(
            """
        - Since October 2022 I have been employed at the Roots outlet store at 
          Toronto Premium Outlets. I've gained extensive knowledge working here,
          involving collaboration, customer relations, organization, and other 
          fundamental retail skills.
            """
        )

    with right_column:
        st_lottie(lottie_coding)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("VOLUNTEER EXPERIENCE")
        st.write("##")
        st.subheader('Kamala Khera office')
        st.write("""
        
        - Door knocking and informing citizens with information regarding 
          the upcoming election and their regional candidate 
          Working collaboratively with other team members to fulfill 
          the needs of voters        
        
        """)
        st.subheader('Remax Canada')
        st.write(
            """
        - Completed sales calls to interested buyers and potential clients regarding listing and inquiries 
        - Recorded appointments and arranged meetings for


            """
        )
        st.subheader('Gradcity Montreal Trip Rep')
        st.write("""
        
        - Responsible for organizing a March Break trip
          for the Graduating class of 2023
        - Informed students about the trip and all that was included,
          helped students sign up and pay for the trip 
        
        """)

    with right_column:
        st_lottie(volunteer_lottie)

with st.container():
    st.write("---")
    st.header("EXTRACURRICULARS & PROGRAMS")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("DECA")
        st.write("""
    
          - I was a member of the DECA team at my school. 
            Being a part of this team was an honour considering 
            I was one of the eight students chosen out of the 
            fifteen hundred students in my school. 
         - I participated in DECA and competed against thousands
             of students from around North America in the business 
             and financial services cluster. I learned a lot of skills 
             through being a part of DECA, including how to communicate, 
             present, and perform under pressure and on a time limit.   
    """)

    with right_column:
        st.image(img_deca)
        st.image(img_deca_2)

    st.subheader("SHSM - Business (Special High Skills Major)")
    st.write("""
    
    - At St.Roch I was enrolled in the SHSM business program. 
      Through out this program i was required to take part in events and acquire certificates related 
      to my major. I would also have to take
      courses that related to my major such as entrepreneur ship,
      marketing and accounting. I was also given the opportunity 
      to learn about General Business Accounting, marketing and 
      entrepreneurship, as well as project management and personal 
      finance skills being a part of SHSM.
    
    """)

with st.container():
    st.write("---")
    st.header("ACHIEVEMENTS & ACCOMPLISHMENTS")
    st.subheader("McGill Personal finance course")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("As part of my SHSM learning I took part in the"
                 " University of McGill Personal Finance course."
                 "I learned the fundamental financial principles I need"
                 " to manage my personal finances in this course. "
                 "These topics included understanding the impact of emotion"
                 " on financial decisions, setting up a budget, investing for "
                 "the future, starting a real estate business, and borrowing prudently.   ")

    # with right_column:
    # add certicface image

with st.container():
    st.write("---")
    st.header("MY CODING PROJECTS")
    st.write("In October of 2021 I took an intrest in Computer Scince "
             "and the Art of Coding. I began my computer scinec journey"
             "by watching youtube vidoes and reading artices online "
             "about algorithms, and diffrecne coding lanugae. This lead "
             "me to enrolling myself in the Harvard CS50 online curce where "
             "I had the opportunity to lean about various concepts including"
             "software engineering, web development, resource management, security,"
             " encapsulation, and abstraction. Using what i had learned from that course "
             "along with articles and free tools online I developed  a few projects of my own")
    st.write("Here is the link to my GitHub page where you can find all my projects")
    st.write(
        "[CLICK ME](https://github.com/alimehdi2005/my-projects-/commits?author=alimehdi2005&since=2022-11-01&until=2022-11-19)")
    st.write("---")
    st.header("DEMO")
    st.subheader("This is a quick demo of on my of favorite projects")
    st.subheader("Snake")
    st.video(projectdemo)
    st.subheader("Calculator")
    st.video(calcdemo)
    st.subheader("Income And Expense Tracker")
    st.video(icdemo)
    st.subheader("Pong")
    st.video(pongdemo)
    st.subheader("And my personal favorite...This Online Resume")

with st.container():
    st.write("---")
    st.header("GOALS")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Short Term")
        st.write("##")
        st.write(
            """
        - Obtain acceptance to a desired and well respected university
        - Obtaining greater programming knowledge, and creating more websites and applications
        - Graduate high school as class valedictorian 
        - Grade form high school with an overall average of 95% or above
          """
        )
    st.subheader("Long term")
    st.write("##")
    st.write("""
             - Graduate from a desired university 
             - Take a position at a financial institution or tech firm
             - Travel to developing nations and aid in constructing homes,
               hospitals, and schools
             - Establish my own financial institution 
             """)
    with right_column:
        st_lottie(goals_lottie)

with st.container():
    st.write("---")
    st.header("My Ambitions")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_trade_setup)
        st.markdown('This is a photo of my setup when I started.')
    with text_column:
        st.subheader("Trading/Market analysis")
        st.write(
            """
             Instead of lying in bed doing nothing in the summer of 2020
             when the epidemic first began, I made the decision to learn 
             about international markets. I gained knowledge on a variety 
             of concepts, including stocks, bonds, futures, and commodities, to 
             mention a few. This pushed me to learn how to day trade, then I started 
             trading on practice accounts before opening up my own trading account to 
             trade commodities and currencies to earn some extra cash on the side. 
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_coding)
        with text_column:
            st.subheader("Coding")
            st.write(
                """
                I became interested in web development and programming 
                towards the beginning of my grade 11 school year.
                Since computer science was not offered at my school,
                I began to teach my programming languages on my own 
                and have since developed a handful number of programs
                and online programs. 
                        
                """
            )

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/alixbox5@outlook.com" method="POST">
    <input type="hidden" name="_captcha" valur="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
      """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
