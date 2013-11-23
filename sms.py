import smtplib

from people import SENDER, PASSWORD, EXAMPLE_NUMBER

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( SENDER, PASSWORD)

def send_text( number, text ):
    server.sendmail( 'Secret Santa', number, text )

if __name__ == '__main__':
    send_text( EXAMPLE_NUMBER, 'Test text.' )

