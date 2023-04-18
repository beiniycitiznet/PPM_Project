# This will be a great library to use
# from webcolors import name_to_rgb
class Ppmimage:
    def __init__ (self, width, height):
        if width<0 or height<0:
            print('Please enter the width and height again!')
            return
        self.width=width
        self.height=height
        self.board=[[[0,0,0] for w in range(width)] for h in range(height)]
        
    def setPixel(self,x,y,color):
        if x>self.width-1 or y>self.height-1 or x<0 or y<0:
            print("Please enter the position again!")
            return
        elif len(color)!=3:
            print("Please enter the color again!")
            return
        for c in color:
            if c<0 or c>255:
                print("Please enter the color again!")
                return
        self.board[y][x]=color 
        return self.board
        
    def writeString(self):
        res='P3 \n'+str(self.width)+' '+str(self.height)+'\n255 \n'
        for h in self.board:
            for w in h:
                for c in w:
                    if c<0 or c>255:
                        print('Please enter the color again!')
                        return
                    res=res+str(c)+' '
            res+='\n'
        return res

    def writeFile(self, filename):
        words=self.writeString()
        with open(filename, 'w') as file:
            file.write(words)


