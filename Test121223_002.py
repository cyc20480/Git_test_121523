import  googletrans

trans = googletrans.Translator()

str = input("번역할 문장을 입력하세요 : ")

# pprint(googletrans.LANGUAGES)

result1 = trans.translate(str, dest = 'en')
result2 = trans.translate(str, dest = 'ja')
result3 = trans.translate(str, dest = 'zh-cn')

print(result1.text)
print(result2.text)
print(result3.text)