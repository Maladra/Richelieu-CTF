import pdftotext

with open("ctf.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print("\n\n".join(pdf))

print(len(pdf))

myvar = "".join(pdf)
fo = open("myfile", "w")
fo.write(myvar.encode('utf-8'))
fo.close()
