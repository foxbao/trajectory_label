import pygame
import os
import itertools
import time

class TrajectoryLabel():
    def __init__(self,root):
        pygame.init()
        self.root=root
        self.scale=1.5
        # 颜色定义
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.cursor_speed=3
        
    def get_image_size(self,data_path):
        names = os.listdir(data_path)
        image = pygame.image.load(os.path.join(data_path, names[0])) # 1.创建一个surface并加载图片
        image_width,image_height=image.get_size()
        new_image_width=image_width
        new_image_height=image_height

        WIDTH,HEIGHT=new_image_width,new_image_height
        return WIDTH,HEIGHT
    

    def draw_crosshair(self,pos):
        # self.screen.fill(black)

        # 在鼠标位置画一个十字
        pygame.draw.line(self.screen, self.white, (pos[0], 0), (pos[0], self.new_image_height), 2)
        pygame.draw.line(self.screen, self.white, (0, pos[1]), (self.new_image_width, pos[1]), 2)

        # 刷新屏幕
        pygame.display.flip()
    
    def indication_text(self,name):
        # 设置字体和字号
        font = pygame.font.Font(None, 20)
        text_lines=[]
        text_lines.append("Click left button of mouse to label")
        text_lines.append("Press SPACE to skip the current image")
        text_lines.append("Press ESC to finish")
        text_lines.append("Press RETURN to label the mouse position")
        text_lines.append("Press Up, Down, Left and Right to adjust")
        text_lines.append(name)
        for idx,text_line in enumerate(text_lines):
            text_render_line=font.render(text_line, True, self.white)
            text_rect_line= text_render_line.get_rect(topleft=(0, idx*20))
            self.screen.blit(text_render_line, text_rect_line)

    def label(self,start_idx):
    # 设置窗口尺寸
        clock = pygame.time.Clock()
        image_width,image_height = self.get_image_size(self.root)
        self.new_image_width=image_width/self.scale
        self.new_image_height=image_height/self.scale
        
        # 创建窗口
        self.screen = pygame.display.set_mode((self.new_image_width, self.new_image_height))

        # 设置窗口标题
        pygame.display.set_caption("label program")
        
        # 设置操作说明字符

        # 设置字体和字号
        font = pygame.font.Font(None, 36)

        # 文本内容
        text = "Click left button of mouse to label\n lalalla"
        text_render = font.render(text, True, self.white)
        text_rect = text_render.get_rect(center=(100, 100))
        
        labelling_trajectory=True
        posList=list()
        
        starting_timestamp=0
        for index,name in enumerate(os.listdir(self.root)):
            if index<start_idx:
                continue
            if index==start_idx:
                starting_timestamp=name.split(".")[0]
            if not labelling_trajectory:
                break
            image = pygame.image.load(os.path.join(self.root, name))
            timestamp=int(name.split(".")[0])
            resized_image=pygame.transform.scale(image,(self.new_image_width,self.new_image_height))
            labelling_one_image=True
            self.screen.blit(resized_image,(0,0))
            while labelling_one_image:
                self.screen.blit(resized_image,(0,0))
                self.indication_text(name)
                # self.screen.blit(text_render, text_rect)
                for pos in posList:
                    pygame.draw.circle(self.screen,(255,0,0),(pos[1], pos[2]),5) 
                # 刷新屏幕
                
                mouse_pos_tuple=pygame.mouse.get_pos()
                cursor=list(mouse_pos_tuple)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type==pygame.KEYDOWN: 
                        if event.key==pygame.K_SPACE: 
                            labelling_one_image=False
                            print("next frame")
                        if event.key==pygame.K_ESCAPE:
                            labelling_one_image=False
                            labelling_trajectory=False
                            print("finish job")
                            break
                        if event.key==pygame.K_RETURN:
                            posList.append((timestamp,cursor[0], cursor[1],index))
                            print ("timestamp={},x = {}, y = {}".format(timestamp,cursor[0], cursor[1],))
                            labelling_one_image=False
                        if event.key==pygame.K_LEFT:
                            cursor[0] -= self.cursor_speed
                        if event.key==pygame.K_RIGHT:
                            cursor[0] += self.cursor_speed
                        if event.key==pygame.K_UP:
                            cursor[1] -= self.cursor_speed
                        if event.key==pygame.K_DOWN:
                            cursor[1] += self.cursor_speed
                        
                        pygame.mouse.set_pos((cursor[0], cursor[1]))
                            
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        posList.append((timestamp,cursor[0], cursor[1],index))
                        print ("timestamp={},x = {}, y = {}".format(timestamp,cursor[0], cursor[1]))
                        labelling_one_image=False

            # 在鼠标位置画十字
                self.draw_crosshair(cursor)
                clock.tick(60)

                
        pygame.quit()
        file_name=input("input the file name to save:")
        file_name=file_name+"_"+str(starting_timestamp)+".txt"
        print(file_name)
        
        with open(file_name, "w", encoding='utf-8') as f:
            # write()：将内容写入文件，默认不换行
            for pos in posList:
                # text = "世界之大,无奇不有！"
                f.write(str(pos[0]))
                f.write(',')
                f.write(str(pos[1]*self.scale))
                f.write(',')
                f.write(str(pos[2]*self.scale))
                f.write(',')
                f.write(str(pos[3]))
                f.write("\n")
                
        # save the results
        

def main():
    # data_root=input("please input the full path of data root folder:")
    trajectoryLabel=TrajectoryLabel('.\output_images_ns')
    start_idx=247
    # start_idx=6598

    trajectoryLabel.label(start_idx)
    
if __name__== "__main__" :
    main()