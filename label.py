import pygame
import os
import itertools
import time

class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height):
        super(Button, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(text, 1, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.image.blit(self.text, self.text_rect)

class TrajectoryLabel():
    def __init__(self,root):
        pygame.init()
        self.root=root
        self.scale=2
        
    def get_image_size(self,data_path):
        names = os.listdir(data_path)
        image = pygame.image.load(os.path.join(data_path, names[0])) # 1.创建一个surface并加载图片
        image_width,image_height=image.get_size()
        new_image_width=image_width
        new_image_height=image_height

        WIDTH,HEIGHT=new_image_width,new_image_height
        return WIDTH,HEIGHT
    
    def label(self):
    # 设置窗口尺寸
        image_width,image_height = self.get_image_size(self.root)
        new_image_width=image_width/self.scale
        new_image_height=image_height/self.scale
        # 创建窗口
        screen = pygame.display.set_mode((new_image_width, new_image_height))

        # 设置窗口标题
        pygame.display.set_caption("label program")
        going=True
        posList=list()
        for name in os.listdir(self.root):
            if not going:
                break
            image = pygame.image.load(os.path.join(self.root, name))
            resized_image=pygame.transform.scale(image,(new_image_width,new_image_height))
            labelling_one_image=True
            screen.blit(resized_image,(0,0))
            while labelling_one_image:
                for pos in posList:
                    pygame.draw.circle(screen,(255,0,0),(pos[0], pos[1]),5) 
                # 刷新屏幕
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type==pygame.KEYDOWN: 
                        if event.key==pygame.K_RETURN: 
                            labelling_one_image=False
                            print("return")
                        if event.key==pygame.K_ESCAPE:
                            labelling_one_image=False
                            going=False
                            print("escape")
                            pygame.quit()
                            break
                            
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        posList.append((pos[0], pos[1]))
                        print ("x = {}, y = {}".format(pos[0], pos[1]))
        pygame.quit()
        file_name=input("input the file name to save:")
        print(file_name)
        
        with open(file_name, "w", encoding='utf-8') as f:
            # write()：将内容写入文件，默认不换行
            for pos in posList:
                # text = "世界之大,无奇不有！"
                f.write(str(pos[0]*self.scale))
                f.write(',')
                f.write(str(pos[1]*self.scale))
                f.write("\n")
                
        # save the results
        

def main():
    # data_root=input("please input the full path of data root folder:")
    trajectoryLabel=TrajectoryLabel('.\output_images')
    trajectoryLabel.label()
    
if __name__== "__main__" :
    main()