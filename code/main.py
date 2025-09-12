from Imports import *

#* Game Design

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappython')     


#? Game loop

while True:
     
     #todo Event loop

     #todo Quit Game Function

     for event in pygame.event.get():
         
         if event.type == pygame.QUIT:   
             RUNNING = False
             pygame.quit()
             exit()  

         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_q :  
                RUNNING = False
                pygame.quit()
                exit()  


       #todo Player Jump function      

         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 GRAVITY  = -10 
                 jump.play()

       #todo Reset function          

             if event.key == pygame.K_SPACE: RUNNING = True   
 
#? Game Functionality  

     if RUNNING:
            
    #! Player Movement
     
            Y += GRAVITY
            rect = player.get_rect(center = (X,Y))
            GRAVITY += 1 
            rect.y += GRAVITY 

    #! Backround Movement

            XSKY -=  SKY_SPEED
            X1SKY -= SKY_SPEED
            if XSKY <= -1000:
                XSKY = 1000
            if X1SKY <= -1000:
                X1SKY = 1000    
            XGROUND -= GROUND_SPEED
            X1GROUND -= GROUND_SPEED

            if XGROUND <= -1000:
                XGROUND = 1000
            if X1GROUND <= -1000:
                X1GROUND =1000    

    #! Obsatacle movement    

        # linear Change
            pos -= DIFFICULTY
            pos_1 -= DIFFICULTY

        # Loop Function

            if pos <= -100:
                pos = 1200
                pos1 = randint(X_1, Y_1)
                pos2 = randint(X_2,Y_2)
            if pos_1 <= -100:
                pos_1 = 1200    
                pos1_ = randint(X_1, Y_1)
                pos2_ = randint(X_2,Y_2)

    #! Score            

            if rect.x >= pos or rect.x >= pos_1:
                SCORE += 1  
                point.play()
            Score = test.render(f'{SCORE}', False, (64,64,64))

    #! Rectangles

        # Obstacle Rectangles
     
          # Frame 1

            rect_obs = obstacle.get_frect(center = (pos ,pos1))
            rect_obs1 = obstacle1.get_frect(center = (pos, pos2)) 

          # Frame 2 

            rect_ob1s = obstacl1e.get_frect(center = (pos_1 ,pos1_))
            rect_obs11 = obstacl1e1.get_frect(center = (pos_1, pos2_))

    #! Drawing the Game

        #todo Draw Sky

            screen.blit(sky1,(X1SKY,Y1SKY))    
            screen.blit(sky, (XSKY, YSKY))  
           
        #todo Draw Player   

            screen.blit(player,rect)

        #* Draw Obstacle

          #* Frame 1
            screen.blit(obstacle, rect_obs)
            screen.blit(obstacle1, rect_obs1)  
         
          #* Frame 2

            screen.blit(obstacl1e, rect_ob1s)
            screen.blit(obstacl1e1, rect_obs11)  
            
        #todo Draw Ground    

            screen.blit(ground1,(X1GROUND,Y1GROUND))
            screen.blit(ground, (XGROUND , YGROUND)) 

        #todo Draw Score

            screen.blit(Score,(500,10)) 

        #! Collision detection
           
            if rect.centerx == pos:
                        
                        if rect.bottom >= pos2:

                            death.play()
                            GRAVITY = 0
                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE   
                            SCORE= 0
                            X = 100
                            Y = 300  
                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)
                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))             
                            RUNNING = False            
                       
                        if Y <= pos1:

                            death.play()
                            GRAVITY = 0
                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE  
                            SCORE= 0
                            X = 100
                            Y = 300  
                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)
                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))               
                            RUNNING = False         
                                                      

            if rect.centerx == pos_1 :
                        
                        if rect.bottom >= pos2_: 

                            death.play()
                            GRAVITY = 0
                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE    
                            SCORE= 0
                            X = 100
                            Y = 300  
                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)
                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))             
                            RUNNING = False            
                              
                                                      

                        if Y <= pos1_: 
                            death.play()            
                            GRAVITY = 0
                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE
                            SCORE= 0
                            X = 100
                            Y = 300  
                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)
                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))     
                            RUNNING = False              
                                                        

    #! Death Screen

            if rect.bottom >= 750 :
                            death.play()
                            GRAVITY = 0
                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE   
                            SCORE= 0

                            X = 100
                            Y = 300  

                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)

                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))              
                            RUNNING = False             
                       

            if rect.top <= -90:
                            death.play()
                            GRAVITY = 0

                            if SCORE > HIGH_SCORE:
                                HIGH_SCORE = SCORE  
                            SCORE= 0

                            X = 100
                            Y = 300  

                            pos = 600           
                            pos_1 = 1200
                            pos1 = randint(X_1, Y_1)
                            pos2 = randint(X_2,Y_2)
                            pos1_ = randint(X_1, Y_1)
                            pos2_ = randint(X_2,Y_2)

                            high_score = test.render(f'The Highest score is: {HIGH_SCORE}',False , (64,64,64))  
                            screen.blit(menu,(-250,0))
                            screen.blit(high_score,(10,750))              
                            RUNNING = False           
                        
                    
    #! Update Game

     pygame.display.update()
     clock.tick(60)