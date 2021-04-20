try: from PIL import *
except:
    print("The 'Pillow' librairie is required for this project to work")
else:
    from PIL import Image
    name=input("File name (with extension): ")
    try: img=Image.open(name)
    except: print("No such file, make sure that it is in the same folder as this python project")
    else:
        s=img.size
        if s[0]<=320:
            if s[1]<=222:
                print("Image loaded")
                print("Reading colors...")
                data=list(img.getdata())
                colors=[]
                for i in range(len(data)):
                    try: colors.index(data[i])
                    except: colors.append(data[i])
                print("Building pixels...")
                lines=[]
                for i in range(s[1]):
                    text=""
                    for j in range(s[0]):
                        hexa=hex(colors.index(data[i*s[0]+j])).upper()
                        if len(hexa)==3: hexa='0'+hexa[2]
                        elif len(hexa)==4: hexa=hexa[2]+hexa[3]
                        text+=hexa
                    lines.append(text+'\n')
                print("Translating file...")
                hexacolors=[]
                for i in range(len(colors)):
                    r=hex(colors[i][0]).upper()
                    r=r[len(r)-2:len(r)]
                    if r[0]=='X': r='0'+r[1]
                    g=hex(colors[i][1]).upper()
                    g=g[len(g)-2:len(g)]
                    if g[0]=='X': g='0'+g[1]
                    b=hex(colors[i][2]).upper()
                    b=b[len(b)-2:len(b)]
                    if b[0]=='X': b='0'+b[1]
                    hexacolors.append(r+g+b)
                pixcolors=""
                for i in range(len(hexacolors)-1): pixcolors+=hexacolors[i]+'/'
                pixcolors+=hexacolors[-1]+'\n'
                lines.insert(0,pixcolors)
                final=""
                for i in range(len(lines)): final+=lines[i]
                print('Your image is ready !')
                name=input("Give it a name (without extension): ")
                open(name+'.py','xt')
                file=open(name+'.py','wt')
                print("Writing...")
                file.write(final)
                file.close()
                print("Done !")
                print("You can now go on https://workshop.numworks.com/python and transfer the script to your calculator, then choose 'import' and here you go !")
            else: print("Error: image height is higher than 222 pixels")
        else: print("Error: image widht is higher than 320 pixels")
    