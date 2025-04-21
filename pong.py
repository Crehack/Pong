import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Pong")

white = (255,255,255)
black = (0,0,0)
green =  (0,255,0)
red = (255,0,0)
blue = (0,0,255)



lineSpeed = 10
ballSpeedX = 5
ballSpeedY = 5

largeur = 15
longueur = 100
rayon = 10

raquette_gauche = pygame.Rect(30, hauteur_fenetre // 2 - longueur // 2, largeur, longueur)
raquette_droite = pygame.Rect(largeur_fenetre - 30 - largeur, hauteur_fenetre // 2 - longueur // 2, largeur, longueur)

balle = pygame.Rect(largeur_fenetre // 2 - rayon // 2, hauteur_fenetre // 2 - rayon // 2, rayon, rayon)

score_gauche = 0
score_droite = 0


font = pygame.font.SysFont("Arial", 30)
font_victoire = pygame.font.SysFont("Arial", 50)

def afficher_score():
    score_text = font.render(f"{score_gauche} - {score_droite}", True, white)
    fenetre.blit(score_text, (largeur_fenetre // 2 - score_text.get_width() // 2, 20))

def afficher_victoire(gagnant):
    fenetre.fill(black)
    if gagnant == "gauche":
        victoire_text = font_victoire.render("Joueur Gauche Gagne !", True, green)
    else:
        victoire_text = font_victoire.render("Joueur Droit Gagne !", True, red)
    
    
    fenetre.blit(victoire_text, (largeur_fenetre // 2 - victoire_text.get_width() // 2, hauteur_fenetre // 3))
    
    
    recommencer_text = font.render("Appuyez sur 'R' pour recommencer ou 'Q' pour quitter", True, white)
    fenetre.blit(recommencer_text, (largeur_fenetre // 2 - recommencer_text.get_width() // 2, hauteur_fenetre // 2))
    
    pygame.display.update()



def jeu():
    global ballSpeedX, ballSpeedY, score_gauche, score_droite

    clock = pygame.time.Clock()

    while True:
        fenetre.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


         # Si un joueur a gagné, on affiche l'écran de victoire
        if score_gauche == 10 or score_droite == 10:
            if score_gauche == 10:
                afficher_victoire("gauche")
            else:
                afficher_victoire("droite")
            
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]: 
                score_gauche = 0
                score_droite = 0
                balle.x = largeur_fenetre // 2 - rayon // 2
                balle.y = hauteur_fenetre // 2 - rayon // 2
                ballSpeedX = 5
                ballSpeedY = 5
            elif keys[pygame.K_q]: 
                pygame.quit()
                sys.exit()
            
            clock.tick(60)  
            continue  
            

        touches = pygame.key.get_pressed()

        if touches[pygame.K_z] and raquette_gauche.top > 0:
            raquette_gauche.y -= lineSpeed
        if touches[pygame.K_s] and raquette_gauche.bottom < hauteur_fenetre:
            raquette_gauche.y += lineSpeed
        if touches[pygame.K_UP] and raquette_droite.top > 0:
            raquette_droite.y -= lineSpeed
        if touches[pygame.K_DOWN] and raquette_droite.bottom < hauteur_fenetre:
            raquette_droite.y += lineSpeed

        balle.x += ballSpeedX
        balle.y += ballSpeedY

        if balle.top <= 0 or balle.bottom >= hauteur_fenetre:
            ballSpeedY = -ballSpeedY
        if balle.colliderect(raquette_gauche) or balle.colliderect(raquette_droite):
            ballSpeedX = -ballSpeedX


        if balle.left <= 0:
            score_droite += 1
            balle.x = largeur_fenetre // 2 - rayon // 2
            balle.y = hauteur_fenetre // 2 - rayon // 2
            ballSpeedX = -ballSpeedX

        if balle.right >= largeur_fenetre:
            score_gauche += 1
            balle.x = largeur_fenetre // 2 - rayon // 2
            balle.y = hauteur_fenetre // 2 - rayon // 2
            ballSpeedX = -ballSpeedX

        
        pygame.draw.rect(fenetre, green, raquette_gauche)
        pygame.draw.rect(fenetre, red, raquette_droite)
        pygame.draw.ellipse(fenetre, white, balle)


        afficher_score()

        pygame.display.update()

        clock.tick(60)

            
jeu()


