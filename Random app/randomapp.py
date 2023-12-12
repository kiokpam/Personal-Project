import pygame,time
import sys,random
from telex_dict import telex
pygame.init()
pygame.display.set_caption("H6 RANDOM")
screen = pygame.display.set_mode((540,732))
font = pygame.font.Font("fonts\Swiss.ttf",30)
font1 = pygame.font.Font("fonts\Swiss.ttf",150)
#Hàm
def draw_name(names, x, y):  # Vẽ nhiều cái thì nên xài hàm
    for i, name in enumerate(names):
        name_surface = font.render(name, True, (255, 255, 255))
        screen.blit(name_surface, (x, y + i * 30))
#bg
bg=pygame.image.load('assets/nen.jpg')
bg=pygame.transform.scale_by(bg,0.5)
#name
entered_name = ['']*12
text_pos=350
current =-15
#Hien thi name
name_dis={}
for i in range(6):
    name_dis[i+1]=(20,350+30*i)
    name_dis[i+7]=(120,350+30*i)
dis=False
dis_pos=150
func=0
#So luong nguoi:
num=''
dup_or_not=False
#Gio
minute='00'
second='00'
clock=pygame.time.Clock()
#Dem gio
counttime=pygame.USEREVENT
pygame.time.set_timer(counttime,1000)
#Sticker
error=pygame.image.load('assets/error.png')
error=pygame.transform.scale(error,(50,50))
error_rect=error.get_rect(center=(65,275))

play=pygame.image.load('assets/play.png')
play=pygame.transform.scale(play,(50,50))
play_rect=play.get_rect(center=(495,175))

res=pygame.image.load('assets/res.png')
res=pygame.transform.scale(res,(50,50))
res_rect=res.get_rect(center=(496,75))

yes=pygame.image.load('assets/yes.png')
yes=pygame.transform.scale(yes,(50,50))
yes_rect=yes.get_rect(center=(65,275))

stop=pygame.image.load('assets/stop.png')
stop=pygame.transform.scale(stop,(50,50))
stop_rect=stop.get_rect(center=(495,175))
start=False
while True:
    if current>=0 and current<=11:
        entered_name[current]=entered_name[current]+'|'
    mousex,mousey=pygame.mouse.get_pos()
    for i in range(len(entered_name)):
        if current!=i:
            entered_name[i]=entered_name[i].rstrip('|')
        elif current == i and entered_name[i].endswith('||'):
            entered_name[i]=entered_name[i].replace('||','|')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if mousex>=20 and mousex<=220 and mousey >=350 and mousey<=550: #nhap ten
                func=1
                if mousex>=20 and mousex<=120 and mousey >=350 and mousey<380:
                    current=0
                elif mousex>=20 and mousex<=120 and mousey >=380 and mousey<410:
                    current=1
                elif mousex>=20 and mousex<=120 and mousey >=410 and mousey<440:
                    current=2
                elif mousex>=20 and mousex<=120 and mousey >=440 and mousey<470:
                    current=3
                elif mousex>=20 and mousex<=120 and mousey >=470 and mousey<500:
                    current=4
                elif mousex>=20 and mousex<=120 and mousey >=500 and mousey<550:
                    current=5
                elif mousex>=120 and mousex<=220 and mousey >=350 and mousey<380:
                    current=6
                elif mousex>=120 and mousex<=220 and mousey >=380 and mousey<410:
                    current=7
                elif mousex>=120 and mousex<=220 and mousey >=410 and mousey<=440:
                    current=8
                elif mousex>=120 and mousex<=220 and mousey >=440 and mousey<=470:
                    current=9
                elif mousex>=120 and mousex<=220 and mousey >=470 and mousey<=500:
                    current=10
                elif mousex>=120 and mousex<=220 and mousey >=500 and mousey<=550:
                    current=11
            else:    
                current=-15
                if mousex>=130 and mousex<=220 and mousey >=250 and mousey<=300:  #so luong
                    func=2
                elif mousex>=20 and mousex<=110 and mousey >=250 and mousey<=300:   #lap hay khong
                    dup_or_not = not dup_or_not
                # elif mousex>=70 and mousex<=220 and mousey >=50 and mousey<=200:  #phút
                #     func=5
                elif mousex>=150 and mousex<=340 and mousey >=20 and mousey<=210:  #giây
                    func=6
                elif mousex>=470 and mousex<=520 and mousey >=150 and mousey<=250 and (second!='00' or minute!='00'):
                    start=not start
                elif mousex>=470 and mousex<=520 and mousey >=50 and mousey<=100:
                    second='00'
                    start=False
                elif mousex>=names_rect.left and mousex<=names_rect.right and mousey >=names_rect.top and mousey<=names_rect.bottom:
                    if num!='' and entered_name:
                        entered_name_strip=[]
                        for name in entered_name:
                            if name!='' and name!='||' and name !='|':
                                entered_name_strip.append(name.rstrip("|"))
                        if dup_or_not:
                            dup = entered_name_strip *int(num)
                            ran_list=random.sample(dup,k=int(num))
                            ran_list=[str(num+1)+". "+text for num,text in enumerate(ran_list)]
                            dis=True
                        elif not dup_or_not and len(entered_name_strip)>=int(num):
                            ran_list=random.sample(entered_name_strip,k=int(num))
                            ran_list=[str(num+1)+". "+text for num,text in enumerate(ran_list)]
                            dis=True
                elif mousex>=namer_rect.left and mousex<=namer_rect.right and mousey >=namer_rect.top and mousey<=namer_rect.bottom:
                    entered_name=['']*12
                    dis=False
                    num=''

        elif event.type == pygame.KEYDOWN:
            if func == 1:
                if event.key == pygame.K_BACKSPACE:
                    if entered_name[current] == '|' or entered_name[current]=='':
                        current = max(current - 1, 0)
                    else:
                        entered_name[current] = entered_name[current][:-2] + '|'
                elif event.key == pygame.K_RETURN:
                    entered_name[current] = entered_name[current].rstrip('|')
                    current = (current + 1) % 12
                    entered_name[current] = entered_name[current].rstrip('|') + '|'
                else:
                    entered_name[current] = entered_name[current].replace('|', '') + event.unicode + '|'
        
        # ... (Các xử lý khác)
            elif func==2:
                if event.key == pygame.K_BACKSPACE:
                    num = num[:-1] 
                elif event.unicode.isnumeric():
                    num=str(num+str(event.unicode))
            elif func == 4:  # Giờ
                if event.key == pygame.K_BACKSPACE:
                    hour = ('0'+hour[:-1])[-2:]
                elif event.unicode.isnumeric():
                    hour += event.unicode
                    hour=hour[-2:]
            elif func == 5:  # Phút
                if event.key == pygame.K_BACKSPACE:
                    minute = ('0'+minute[:-1])[-2:]
                elif event.unicode.isnumeric():
                    minute += event.unicode
                    minute=minute[-2:]
            elif func == 6:  # Giây
                if event.key == pygame.K_BACKSPACE:
                    second = ('0'+second[:-1])[-2:]
                elif event.unicode.isnumeric():
                    second += event.unicode
                    second=second[-2:]
                
    screen.blit(bg,(0,0))
    #Dongho
    
    pygame.draw.rect(screen, (9, 108, 128),(150,20,190,190))
    
    #nut start
    if start:
        pygame.draw.rect(screen, (9, 108, 128),(470,150,50,50))
        screen.blit(stop, stop_rect)
        second=str('00'+str(int(second)-1))[-2:]
        time.sleep(1)
        if second=='00':
            start=False
        # if int(second)<0:
        #     if int(minute)>=1:
        #         minute=str('00'+str(int(minute)-1))[-2:]
        #         second='59'
        #     else:
        #         second='00'
        #         start=False
    else:
        pygame.draw.rect(screen, (9, 108, 128),(470,150,50,50))
        screen.blit(play, play_rect)
        
    
    # #Lap hay ko
    if not dup_or_not:
        pygame.draw.rect(screen, (9, 108, 128),(20,250,90,50))
        screen.blit(error,error_rect)
    else:
        pygame.draw.rect(screen, (9, 108, 128),(20,250,90,50))
        screen.blit(yes, yes_rect)
    
    pygame.draw.rect(screen, (9, 108, 128),(470,50,50,50))
    screen.blit(res, res_rect)
    #So luong nguoi
    pygame.draw.rect(screen, (9, 108, 128),(130,250,90,50))
    #Nhap ten
    pygame.draw.rect(screen, (9, 108, 128),(20,350,200,200))
    #Hien thi ten
    pygame.draw.rect(screen, (9, 108, 128),(320,250,200,300))
    
    draw_name(entered_name[:6],20,350)
    draw_name(entered_name[6:],120,350)
    if dis:
        draw_name(ran_list,320,250)
    if num:
        num1_surface = font.render(str(num), True, (255, 255, 255))
        num1_rect=num1_surface.get_rect(center=(175,275))
        screen.blit(num1_surface, num1_rect)

    # if int(second)>=60:
    #     minute=str('00'+str(int(minute)+int(second)//60))[-2:]
    #     second=str('00'+str(int(second)%60))[-2:]
    # if int(minute)>=60:
    #     hour=str('00'+str(int(hour)+int(minute)//60))[-2:]
    #     minute=str('00'+str(int(minute)%60))[-2:]
    
    # min_surface = font1.render(str(minute), True, (255, 255, 255))
    # min_rect=min_surface.get_rect(center=(145,125))
    # screen.blit(min_surface, min_rect)
    
    sec_surface = font1.render(str(second), True, (255, 255, 255))
    sec_rect=sec_surface.get_rect(center=(245,115))
    screen.blit(sec_surface, sec_rect)

    name_s = font.render(f'Random', True, (255, 234, 0))
    names_rect=name_s.get_rect(center=(100,630))
    screen.blit(name_s, names_rect)

    name_r = font.render(f'Reset', True, (255, 234, 0))
    namer_rect=name_r.get_rect(center=(430,630))
    screen.blit(name_r, namer_rect)

    dup = font.render(f'Dupli', True, (0, 0, 0))
    dup_rect=dup.get_rect(center=(65,225))
    screen.blit(dup, dup_rect)

    num_surface = font.render(f'Number', True, (0, 0, 0))
    num_rect=num_surface.get_rect(center=(175,225))
    screen.blit(num_surface, num_rect)

    name_e = font.render(f'Enter name', True, (0, 0, 0))
    namee_rect=name_e.get_rect(center=(120,325))
    screen.blit(name_e, namee_rect)
    clock.tick(120)


    pygame.display.flip()