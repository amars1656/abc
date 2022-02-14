str="the lyrics is not that poor"
st1=str.find("not")
st2=str.find("poor")
str=str.replace(str[st1:(st2+4)],"good")
print(str)