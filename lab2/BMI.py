if __name__=='__main__':
    weight=float(input('请输入您的体重(单位: 千克): '))
    height=float(input('请输入您的身高(单位: 米): '))
    bmi=weight/(height**2)
    print(bmi)
    if bmi<18.5:
        print("轻体重")
    elif bmi>=18.5 and bmi<24:
        print("正常")
    elif bmi>=24 and bmi<28:
        print("超重")
    else:
        print("肥胖")