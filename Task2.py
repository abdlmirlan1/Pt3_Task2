def compare():
    sent = (input("Write any sentence: ")).split()
    sent.sort(key=len)
    sent = " ".join(sent)
    print(sent)

compare()   

