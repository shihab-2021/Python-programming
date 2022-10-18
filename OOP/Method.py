class Phone:
    color = 'black'
    features = ['camera', 'water proof', 'communication']

    def call(self):
        print('ring ring ring')

    def send_sms(self, number, text):
        sms = f'Sending sms: {text} to: {number}'
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01858285438', 'I missed to miss you')
print(sms)