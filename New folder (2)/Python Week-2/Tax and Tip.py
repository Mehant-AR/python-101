a=int(input())
tax=a*0.05
tip=a*0.18
total=a+tax+tip
print("The tax is ",format(tax,".2f")," and the tip is ",format(tip,".2f"),","," making the total ",format(total,".2f"),sep="")
