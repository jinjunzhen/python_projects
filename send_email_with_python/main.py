import smtplib

my_email = 'jinjunzhen.testing'
password = 'abcd1234()()'

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='jinjunzhen@yahoo.com',
        msg='Subject:testing python email\n\nThis is the body of my email again'
    )