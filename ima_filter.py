from PIL import Image



def red(r,g,b):
    pix_r = r
    pix_g = 0
    pix_b = 0
    return(pix_r,pix_g,pix_b)

def green(r,g,b):
    pix_r = 0
    pix_g = g
    pix_b = 0
    return(pix_r,pix_g,pix_b)

def blue(r,g,b):
    pix_r = 0
    pix_g = 0
    pix_b = b
    return(pix_r,pix_g,pix_b)

def yellow(r,g,b):
    pix_r = g
    pix_g = b
    pix_b = r
    return(pix_r,pix_g,pix_b)

def skyblue(r,g,b):
    newr = b
    newg = g
    newb = r
    return(newr,newg,newb)

def violet(r,g,b):
    pix_r= g
    pix_g= r
    pix_b= b
    return(pix_r,pix_g,pix_b)

def purple(r,g,b):
    pix_r= (r+g)//2
    pix_g= 0
    pix_b= b
    return(pix_r,pix_g,pix_b)



def gray(r,g,b):
    pix_r = (r+g+b)//3
    pix_g= (r+g+b)//3
    pix_b= (r+g+b)//3
    return(pix_r,pix_g,pix_b)

def sepia(r,g,b):
    pix_r= int((r* .393)+(g*.769)+(b*.189))
    
    pix_g= int((r* .349)+(g*.686)+(b*.168))
    pix_b= int((r* .272)+(g*.534)+(b*.131))
    return(pix_r,pix_g,pix_b)




def main():
    path = input('File Path:')
    img =Image.open(path).convert("RGB")
    width,height =img.size

    pixel = img.load()
    print(pixel[1,2])
    print('\tFilters')
    print('*********************')
    print('1.Red\n2.Green\n3.Blue\n4.Yellow\n5.Skyblue\n6.Violet\n7.Purple\n8.Gray\n9.Sepia')
    print('*********************')

    choice ='Enter your choice:'
    print(choice)
    no = int(input())


    for py in range(height):
        for px in range(width):
            r,g,b = (img.getpixel((px,py)))
            if no == 1:
                pixel[px,py]=red(r,g,b)
            elif no ==2:
                pixel[px,py]=green(r,g,b)
            elif no ==3:
                pixel[px,py]=blue(r,g,b)
            elif no ==4:
                pixel[px,py]=yellow(r,g,b)
            elif no ==5:
                pixel[px,py]=skyblue(r,g,b)
            elif no ==6:
                pixel[px,py]=violet(r,g,b)
            elif no ==7:
                pixel[px,py]=purple(r,g,b)
            elif no ==8:
                pixel[px,py]=gray(r,g,b)
            elif no ==9:
                pixel[px,py]=sepia(r,g,b)
            else:
                pixel[px,py]=(r,g,b)
    img.show()
    ans = input('Do you want to save the image? Y/N :')
    if ans == 'Y':
        img.save('file9.jpg')
        
        print('Thank You!!')
    elif ans == 'N':
        ans1 = input('OK!...Do you want to continue to check other filter? Y/N :')
        if ans1 == 'Y':
            main()
        else:
            print('Thank You!!')
        
    else:
        print('Thank You!!')

if __name__ == '__main__':
    main()
