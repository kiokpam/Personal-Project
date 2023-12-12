import pygame,sys,random
pygame.mixer.pre_init(frequency=44100,size=-16,channels=2, buffer=512) #Mix lại âm thanh
pygame.init()                                          #Khởi tạo pygame

#Tạo các hàm
def draw_floor():                                           #tạo 2 sàn chạy chạy
    screen.blit(floor,(floor_x_pos,650)) 
    screen.blit(floor,(floor_x_pos+432,650)) 
def create_pipe():
    random_pipe_pos=random.choice(pipe_height)
    bottom_pipe=pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe=pipe_surface.get_rect(midtop = (500,random_pipe_pos-700))
    return bottom_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom>=600:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top<=-75 or bird_rect.bottom >=650:
        return False
    return True
def rotate_bird(bird1):
    new_bird=pygame.transform.rotozoom(bird1,-bird_movement*3,1)
    return new_bird
def bird_animation():
    new_bird=bird_list[bird_index]
    new_bird_rect=new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state=='main game':
        score_surface=game_font.render(str(int(score)),True, (255,255,255))
        score_rect=score_surface.get_rect(center=(216,100))
        screen.blit(score_surface,score_rect)
    if game_state=='game_over':
        score_surface=game_font.render(str(int(score)),True, (255,255,255))
        score_rect=score_surface.get_rect(center=(216,100))
        screen.blit(score_surface,score_rect)

        high_score_surface=game_font.render(f'High score:{str(int(high_score))}',True, (255,255,255))
        high_score_rect=high_score_surface.get_rect(center=(216,500))
        screen.blit(high_score_surface,high_score_rect)
screen=pygame.display.set_mode((432,768))              #Màn hình chính
running = True                                         #Biến chạy vòng while, vòng lặp chính
clock=pygame.time.Clock()                              #Set fps
keys=pygame.key.get_pressed()                          #Lấy phím được ấn
game_font=pygame.font.Font('04B_19.ttf',40)
gravity= 0.25
bird_movement=0
game_active=True
score=0
high_score=0
#Background
bg=pygame.image.load("assets/background-night.png")    #Load ảnh
bg=pygame.transform.scale2x(bg)                        #scale ảnh lên 2x

#Floor
floor=pygame.image.load("assets/floor.png") 
floor=pygame.transform.scale2x(floor)  
floor_x_pos=0  

#Chim
# bird=pygame.image.load("assets/yellowbird-midflap.png") 
bird_down=pygame.transform.scale2x(pygame.image.load("assets/yellowbird-downflap.png") )  
bird_mid=pygame.transform.scale2x(pygame.image.load("assets/yellowbird-midflap.png") )  
bird_up=pygame.transform.scale2x(pygame.image.load("assets/yellowbird-upflap.png") ) 
bird_list=[bird_down, bird_mid, bird_up] 
bird_index=0
bird=bird_list[bird_index]
bird_rect=bird.get_rect(center=(100,384))              #Vẽ hình chữ nhật quanh con chim
# pygame.draw.rect(screen, color, (x,y,width,height))
#timer cho bird
birdflap=pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)
#Cột
pipe_surface=pygame.image.load("assets/pipe-green.png")  
pipe_surface=pygame.transform.scale2x(pipe_surface) 
pipe_list=[]
pipe_height=[200,300,400]
#Tạo timer:
spawnpipe=pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)                  #Lặp lại sau mỗi 1,2 giây
# def draw_pipe():
#     screen.blit(pipe,(pipe_x_pos,0)) 
#     screen.blit(pipe,(pipe_x_pos+100,0))
#     screen.blit(pipe,(pipe_x_pos+200,0))
#     screen.blit(pipe,(pipe_x_pos+300,0))
#     screen.blit(pipe,(pipe_x_pos+400,0))
#Màn hình thua
over_screen=pygame.transform.scale2x(pygame.image.load("assets/gameover.png") ) 
over_rect=over_screen.get_rect(center=(214,300))
flap_sound=pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound=pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound=pygame.mixer.Sound('sound/sfx_point.wav')
score_countdown=100
while running:
    for event in pygame.event.get():                   #Kiểm soát các sự kiện trong game
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement=0
                bird_movement=-6
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                game_active=True
                pipe_list.clear()                           #Xóa list ống cũ
                bird_rect.center=(110,384)
                bird_movement=-10
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index <2:
                bird_index+=1
            else:
                bird_index=0
            bird, bird_rect=bird_animation()
    screen.blit(bg,(0,0))                              #vẽ lên màn hình
    if game_active:                                    #Nếu còn game thì chim và ống hoạt động
        #Chim
        bird_movement+=gravity                             #chim rơi theo trọng lực
        rotated_bird=rotate_bird(bird)
        bird_rect.centery += bird_movement                 #thay đổi trung tâm hình chữ nhật
        screen.blit(rotated_bird,bird_rect)
        game_active=check_collision(pipe_list)
        #Ống
        pipe_list=move_pipe(pipe_list)
        draw_pipe(pipe_list)
        
        score+=0.01
        score_display('main game')
        score_countdown-=1
        if score_countdown<=100:
            score_sound.play()
            score_countdown=100

    else:
        if score > high_score:
            high_score=score
        score=0
        score_display('game_over')
        screen.blit(over_screen,over_rect)
    #floor
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos<=-432:                              
        floor_x_pos=0
    
    # screen.blit(floor,(floor_x_pos,600))             cho sàn di chuyển liên tục
    pygame.display.update()                            #update màn hình
    clock.tick(60)                                    #set fps

