# 5.4

letter = ['salutation', 'name', 'product', 'verved',
          'room', 'animals', 'amount', 'product',
          'percent', 'spokesman', 'job_title']

print('''Dear {0} {1},\n\nThank you for your letter. We are sorry that our {2} {3} in your {4}.
      Please note that it should never be used in a {4},\nespecially near any {5}.
      \nSend us your receipt and {6} for shipping and handing.
      We will send you another {2} that,in our test,is {7}% less likely to have {3}.
      \nThank you for your support.\nSincerely,\n{9}\n{10}'''.format(*letter))

#5.5
salutation = 'mr'
name = 'lee'
product = 'box'
verbed = 'runover'
room = '204'
animals = 'dog'
amount = '30$'
percent = 79
spokesman = 'kim'
job_title = 'team leader'

letter = '''Dear {s} {n},\n\nThank you for your letter. We are sorry that our {p} {v} in your {r}.
      Please note that it should never be used in a {r},\nespecially near any {a}.
      \nSend us your receipt and {m} for shipping and handing.
      We will send you another {p} that,in our test,is {t}% less likely to have {v}.
      \nThank you for your support.\nSincerely,\n{k}\n{j}'''

print(letter.format(s=salutation,n=name,p=product,v=verbed,r=room,a=animals,m=amount,t=percent,k=spokesman,j=job_title))


#5.6

duck = 'Ducky McDuckface'
gourd = 'Gourdy McGourdface'
spitz = 'Spitzy McSpitzface'
# print("an English submarine 이름은 (%s)로 지어졌다." % (duck))
# print("an Australian racehorse 이름은 (%s)로 지어졌다." % (gourd))
# print("a Swedish train 이름은 (%s)로 지어졌다." % (spitz))
print(" an English submarine 이름은 (%s)로 지어졌다.\n" % (duck),
      "an Australian racehorse 이름은 (%s)로 지어졌다.\n" % (gourd),
      "a Swedish train 이름은 (%s)로 지어졌다." % (spitz))

#5.7

# print("an English submarine 이름은 ({})로 지어졌다.".format(duck))
# print("an Australian racehorse 이름은 ({})로 지어졌다.".format(gourd))
# print("a Swedish train 이름은 ({})로 지어졌다.".format(spitz))

print(" an English submarine 이름은 ({})로 지어졌다.\n".format(duck),
    "an Australian racehorse 이름은 ({})로 지어졌다.\n".format(gourd),
    "a Swedish train 이름은 ({})로 지어졌다.".format(spitz))

#5.8

print(f' an English submarine 이름은 ({duck})로 지어졌다.\n',
      f'an Australian racehorse 이름은 ({gourd})로 지어졌다.\n',
      f'a Swedish train 이름은 ({spitz})로 지어졌다.')

#6.2

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")

    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break

    number += 1


#6.3

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break












